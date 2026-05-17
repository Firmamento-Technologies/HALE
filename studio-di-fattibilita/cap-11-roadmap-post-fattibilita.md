# Capitolo 11 — Roadmap Post-Fattibilità

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 11
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (sezione "fasi attuative e roadmap"); NASA SE Handbook Rev 2, §6.7 (Phase B-F life cycle) e §6.8 (Decision Analysis)
> **Template di riferimento italiano:** ENAC Piano Strategico Nazionale AAM 2021-2030 + Allegato 1 Roadmap [^1]; DTA Puglia Studio di Fattibilità Grottaglie (per struttura roadmap aerospaziale italiana)
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor` (falsifiability, triangulation, source provenance, confidence levels, pre-mortem, steel-manning, base-rate)
> **Red Team review:** verifica condotta dagli agenti `sovereign-infrastructure-strategist` + `business-model-strategist` + `financial-cfo-analyst` — vedi §11.10

---

## 11.0 Sintesi del capitolo

Il presente capitolo descrive la **roadmap post-fattibilità** del progetto Firmamento Technologies, ovvero la sequenza di **fasi, milestone, gate decisionali, KPI e capital plan** che opera-zionalizzano la **visione strategica a 10 anni** (`riferimenti/visione-10-anni.md`) **oltre** l'orizzonte coperto dallo Studio.

**Distinzione critica** (NASA SE Handbook §6.7):

- Lo **Studio di Fattibilità** che il presente Volume 1 chiude al gate M+10/M+11 **approva** specificamente: (i) il **Percorso 6A — Fase 1** (MVP VTOL Pentema, M+0 → M+12) con verdetto target **GO**; (ii) la **preparazione del Percorso 6B** (R&D HALE preliminare) con verdetto **HOLD / Go Condizionato Estremo**, deferito a gate successivi.
- La **roadmap post-fattibilità** (oggetto di questo capitolo) **descrive** — senza approvare oggi — la traiettoria delle **Fasi 2-5** (M+12 → M+120), affinché le decisioni del gate M+10 siano prese in **coerenza vettoriale** con un orizzonte di lungo termine credibile e onesto.

**Tesi del capitolo, in sintesi:**

1. La visione 10 anni (`visione-10-anni.md`) è il **vettore strategico** che giustifica la dualità 6A/6B, non un piano operativo da approvare in blocco. Il capitolo la operazionalizza in 5 fasi con gate intermedi.
2. **Fase 1 (M+0 → M+24)** è la **fase decisiva**: senza un MVP Pentema validato + scale-up Liguria, il vettore si interrompe e la roadmap va riconfigurata su un'opzione di consolidamento territoriale standalone.
3. **Fase 2 (M+24 → M+36)** apre il **doppio binario**: scale-up VTOL/MALE in 3-4 regioni SNAI + avvio R&D HALE subscale (TRL 3 → 5). Capital intensity €2.5-8M cumulato. Gate M+36 decide se attivare la Fase 3 HALE.
4. **Fase 3 (M+36 → M+72)** è la fase **R&D-intensiva**: HALE prototipo full-scale, primo volo stratosferico dimostrativo, engagement EASA Special Condition, Series A-B €5-15M. Capital intensity cumulato €15-50M.
5. **Fase 4 (M+72 → M+96)** richiede **finanziamento sovrano**: costellazione iniziale 3-10 HAPS italiani, primo bando EDF HAPS, Series B-C €30-100M. Capital intensity cumulato €100-500M.
6. **Fase 5 (M+96 → M+120)** è il **posizionamento EU sovereign**: consorzio EU stratospheric layer, 10-30 HAPS in cluster italiano + partner FR/DE/ES, esit strategico. Capital intensity onesta scenari "small fleet" €500M-2B vs **"EU sovereign full scale" €10-30B**, condizionata all'apertura di un programma equivalente IRIS² da parte della Commissione UE.
7. **Scenario alternativo B2-relaxed (§11.6bis)** — riconosciuto esplicitamente: se al Y4-Y6 le pre-condizioni esterne (EASA RMT HAPS, programma EU sovereign, Series C €50M+, geopolitica EU) non si concretizzano, la traiettoria operativa Y10 ridimensiona la Fase 5 a **"Standalone IT Operator Small Fleet"** (5-10 HAPS + 10-20 VTOL/MALE, ARR €30-80M, capital intensity €500M-1.5B, probabilità 30-50%). Questo scenario **non è fallimento**: è un esito di successo dimensionato alle condizioni esterne reali, con la Fase 5 full "consorzio EU" mantenuta come **option di lungo termine**, non come unico esito accettabile.

**Verdetto Cap. 11**: la roadmap **non è un commitment vincolante** sulle Fasi 3-5, è un **vettore strategico coerente** che attribuisce significato alle decisioni del gate M+10 e fornisce un quadro per i gate futuri. Gli **showstopper noti** delle Fasi 3-5 sono dichiarati esplicitamente e legati a **falsifying observations** verificabili. Lo scenario **B2-relaxed (§11.6bis)** è la rete di sicurezza strategica della boundary B2, non la sua negazione.

---

## 11.0bis Boundary conditions del progetto

Il capitolo rispetta — come in tutti gli altri capitoli — le **boundary conditions** dichiarate (vedi Cap. 3.0bis, 5.0bis, 7.0bis):

- **B1 — Modello service-only + cooperative Legacoop**: l'intera roadmap descrive l'evoluzione di un **operatore di servizi** (no vendita di velivoli). Il modello cooperativo Legacoop è preservato in tutte le fasi come **stakeholder strutturale**, non come ipotesi da abbandonare nello scale-up.
- **B2 — Obiettivo strategico "nodo IT di EU sovereign stratospheric layer"**: la roadmap mantiene esplicitamente la traiettoria verso Fase 5 (consorzio EU), riconoscendo onestamente che essa è **finanziariamente condizionata** all'apertura di un programma EU dedicato (analog IRIS²) e **politicamente condizionata** alla stabilità del quadro EU-US-CN.

**Linguaggio pubblico** (vedi `riferimenti/RESERVED-rischi-geopolitici.md`, RSK-GEO-001): il capitolo usa "**stratospheric layer complementary to IRIS²**" e **NON** "alternativa europea a Starlink". Il framing competitivo è riservato a documenti interni / sotto NDA.

---

## 11.1 Razionale e Scope della Roadmap

### 11.1.1 Cosa lo Studio approva oggi

Il **gate M+10/M+11** dello Studio di Fattibilità approva (verdetto target):

| Elemento approvato al M+10 | Orizzonte | Capital intensity approvato | Confidence verdetto |
|---|---|---|---|
| **Fase 1 — MVP VTOL Pentema** (Percorso 6A, GO) | M+0 → M+24 | €0.7-1.2M CapEx Y1 + €0.5-1.5M scale-up Y2 | **high** |
| **Preparazione Fase 3 — R&D HALE preliminare** (Percorso 6B, HOLD / Go Condizionato Estremo) | M+0 → M+24 R&D desk + subscale design | €0.3-0.8M Y1-Y2 (R&D + engagement EASA) | **medium** (rischio dipendenze esterne) |
| **Apertura strutturata di Fase 2** (scale-up SNAI multi-regione) | gate M+24 | non approvato oggi — gate decision | **medium** |

Tutto quanto descritto al gate M+10 ha **piena copertura RTM** (Cap. 3), **funding plan committed ≥ 60%** (Cap. 8), **regolatorio compatibile** (Cap. 5), **business case validato** (Cap. 7). È **investment-grade decision**.

### 11.1.2 Cosa la roadmap definisce per il futuro

Per le **Fasi 3, 4, 5** (M+36 → M+120) il presente capitolo:

- **NON** approva commitment di capitale né scelte tecnologiche definitive
- **SI** definisce: (i) **gate decisionali intermedi** con criteri quantitativi di entrata e uscita, (ii) **KPI di successo** per fase, (iii) **dipendenze esterne critiche** e **showstopper** dichiarati, (iv) **budget di ordine di grandezza** con scenari onesti, (v) **stakeholder critici** per fase, (vi) **partnership e capital plan** ipotizzati ma non committed

La roadmap è documento **"vivente"** (NASA SE Handbook §6.7): aggiornata a ogni gate review (M+12, M+24, M+36, M+72, M+96) con base evidenziale crescente. Confidence dichiarato per fase:

| Fase | Orizzonte | Confidence pianificazione |
|---|---|---|
| Fase 1 | M+0 → M+24 | **high** (Studio approva) |
| Fase 2 | M+24 → M+36 | **medium** (struttura nota, esecuzione condizionata a Fase 1) |
| Fase 3 | M+36 → M+72 | **medium-low** (dipendenze EASA + capital esterne) |
| Fase 4 | M+72 → M+96 | **low** (dipendenza EDF + IRIS² alignment) |
| Fase 5 | M+96 → M+120 | **speculative** (dipendenza programma EU sovereign analog IRIS²) |

### 11.1.3 Relazione con la visione strategica 10 anni

Il documento `riferimenti/visione-10-anni.md` è la **fonte autoritativa** del posizionamento strategico Firmamento. Il presente Cap. 11 **non** rivisita né rinegozia tale visione: la **operazionalizza** in termini di:

- **Sequenza temporale** dei gate decisionali concreti
- **Capital plan progressivo** per fase
- **Falsifying observations** che, se verificate, attivano revisione della roadmap
- **Stakeholder engagement plan** per fase
- **Showstopper espliciti** dichiarati per fase

In particolare, il capitolo **eredita senza modifiche** dalla visione:

- Le 5 fasi temporali (Y1-Y2, Y2-Y3, Y4-Y6, Y6-Y8, Y8-Y10)
- Il modello service-only (boundary B1) per ogni fase
- L'obiettivo finale "EU sovereign stratospheric layer" (boundary B2)
- Il caveat di **capital intensity onesta**: range "small fleet" €500M-2B vs scala "EU sovereign full scale" €10-30B

Il capitolo **aggiunge** rispetto al documento `visione-10-anni.md`:

- Una **operazionalizzazione esplicita dello scenario "small fleet"** in chiave **B2-relaxed "Standalone IT Operator"** (§11.6bis), con trigger di attivazione, KPI Y10, capital intensity €500M-1.5B, distribuzione di probabilità degli esiti Y10 e calibrazione del messaggio esterno. Questa estensione recepisce la raccomandazione `AUDIT-QUALITY-VOLUME-1.md` §2 Cap. 11 (gap "manca scenario B2-relaxed") e preserva l'integrità della boundary B2 come **target aspirazionale** + **option di lungo termine**.

### 11.1.4 Vincoli e dipendenze esterne

La roadmap è soggetta a **5 vincoli strutturali esterni** (sintesi; dettaglio §11.9):

1. **Regolatorio EASA HAPS**: apertura di un framework Special Condition Certified HAPS prima del Y6-Y7 (vedi Cap. 5 RSK-REG-001).
2. **Finanziario sovrano EU**: apertura di un programma equivalente IRIS² su HAPS con budget multi-miliardario (€10B+) entro Y5-Y6 per abilitare la Fase 5.
3. **Tecnologico batterie**: disponibilità di celle Li-S / Solid-State con densità pacchetto ≥ 350 Wh/kg entro Y3-Y4 per closing energy balance HALE inverno (vedi RSK-TEC-001 stimato in Cap. 6 — energy balance non chiuso da fonte indipendente).
4. **Partnership IT**: cooperazione (non antagonismo) di Leonardo / Thales Alenia Space / CIRA fino almeno alla Fase 3. (Vedi RSK-GEO-005 documento riservato.)
5. **Geopolitica EU-US**: stabilità della cornice transatlantica che consenta supply chain robusta e non escalation di restrizioni export (vedi RSK-GEO-001, RSK-GEO-003).

I primi 3 vincoli sono trattabili nello Studio pubblico; i vincoli 4-5 sono richiamati discretamente e dettagliati nel documento riservato `RESERVED-rischi-geopolitici.md` (accesso ristretto).

---

## 11.2 Fase 1 — VTOL Pilota Pentema (M+0 → M+24)

> **Stato verdetto Cap. 11**: Fase **approvata** dallo Studio di Fattibilità (verdetto target GO al gate M+10/M+11).
> **Riferimenti**: Cap. 7 §7.9 MVP definition; Cap. 3 §3.2 criteri Gate; Cap. 5 §5.12 verdetto regolatorio; `riferimenti/visione-10-anni.md` §2 Fase 1.

### 11.2.1 Obiettivi specifici della Fase 1

La Fase 1 è la fase **decisiva** della roadmap: senza un MVP Pentema validato + scale-up Liguria iniziale, il vettore strategico si interrompe. Obiettivi:

| ID | Obiettivo | Verifica al gate M+24 |
|---|---|---|
| OBJ-F1-01 | Dimostrare il modello service-based su scala micro | ≥ 3 contratti pluriennali firmati con valore aggregato ≥ €200k Y1 (SyR-Cost-003) |
| OBJ-F1-02 | Validare la fattibilità operativa BVLOS in Liguria interna | SORA application approvata SAIL II-III; ≥ 50 missioni operative in Y1 |
| OBJ-F1-03 | Costruire **anchor relationships** con Regione Liguria + PC + Cooperative | LoI Regione + DGR + protocollo PC + contratto rete cooperative |
| OBJ-F1-04 | Generare evidenze regolatorie + privacy + data governance | DPIA pubblica + AGCOM spettro autorizzato + GDPR compliance verificata |
| OBJ-F1-05 | Posizionare Firmamento come **operatore credibile** per scale-up | NPS stakeholder ≥ 40; ≥ 1 regione SNAI aggiuntiva con LoI per Fase 2 |
| OBJ-F1-06 | Avviare in parallelo R&D HALE preliminare (preparatorio Fase 3) | TRL HALE subsystems critici ≥ 4 (energy balance modellato; aerodinamica subscale validata) |

### 11.2.2 Scope operativo (espansione casi d'uso post-MVP)

L'MVP Y1 (M+0 → M+12) copre i 5 use case prioritari (Cap. 7 §7.2.2): UC-001 (frane), UC-002 (antincendio), UC-003 (connettività emergenza), UC-005 (mapping cooperative agricole), UC-007 (Enti Parco). Nel periodo **post-MVP** Y2 (M+12 → M+24) lo scope si espande:

| Use case aggiunto Y2 | Stakeholder primario | Pricing target | Confidence |
|---|---|---|---|
| UC-004 Mapping infrastrutture stradali ANAS / Comuni SNAI Liguria | ANAS, Comuni, RFI (ispezione) | €30-100k/anno per area | medium |
| UC-006 Supporto SAR (ricerca persone disperse) | PC, CC Forestali | €5-15k/event (on-demand) | medium |
| UC-008 Telemedicina rurale Aree Interne via NTN | ASL3, Comuni SNAI, ASL Piemonte | €15-40k/anno per area | low-medium |

Inoltre Y2 prevede l'**estensione geografica**: 2 aree SNAI aggiuntive in Liguria (Antola-Aveto + Beigua) + 1 area SNAI in **Piemonte o Calabria** (LoI da formalizzare entro M+18).

### 11.2.3 KPI di successo Fase 1

I KPI sono ereditati dal Cap. 7 §7.9.2 (MVP Y1) e dal `riferimenti/visione-10-anni.md` §2 Fase 1, con estensione Y2:

| Categoria | KPI | Target Y1 | Soglia minima Y1 | Target Y2 (cumulato) |
|---|---|---|---|---|
| Operazioni | Missioni eseguite | ≥ 80 | ≥ 50 | ≥ 200 |
| Sicurezza | Incidenti FATAL o major | 0 | 0 (vincolo assoluto) | 0 |
| Compliance | SORA SAIL II-III approvato | ✓ | ✓ | ✓ + estensione areale |
| Customer | Contratti pluriennali firmati | ≥ 5 | ≥ 3 | ≥ 10 |
| Revenue (RECALIBRATED post-Cluster D M+3) | ARR cumulato | €260k centrale (range €220-300k) | ≥ €200k (SyR-Cost-003 hard floor) | €0.8-1.2M (vs €1.0-1.5M pre-recalibration) |
| Satisfaction | NPS stakeholder PA/coop | ≥ 50 | ≥ 40 | ≥ 50 sostenuto |
| Service quality | Utilization rate (% ore disponibili fatturate) | ≥ 60% | ≥ 40% | ≥ 65% |
| Replicabilità | Letters of Interest scale-up SNAI | ≥ 2 regioni | ≥ 1 regione | ≥ 2 regioni firmate |
| R&D 6B | TRL HALE subsystems critici | ≥ 3 | ≥ 3 | ≥ 4-5 |

### 11.2.4 Milestone temporali

Sintesi delle milestone principali della Fase 1 (dettaglio in Cap. 9):

| Milestone ID | Mese | Descrizione | Owner |
|---|---|---|---|
| MS-F1-01 | M+3 | Pre-application meeting ENAC + workshop cooperative pilota | Firmamento (PM + Regulatory) |
| MS-F1-02 | M+6 | LoI Regione Liguria + DPIA preliminare pubblica + DGR | Firmamento + Regione Liguria |
| MS-F1-03 | M+9 | SORA application sottomessa + AGCOM spettro autorizzato | Firmamento |
| MS-F1-04 | M+10/M+11 | **Gate Studio di Fattibilità — verdetto Go/Hold/No-Go** | Firmamento + Coopfond |
| MS-F1-05 | M+12 | SORA approvata + Hangar Pentema operativo + primo volo BVLOS Pentema | Firmamento |
| MS-F1-06 | M+15 | Prima campagna estiva antincendio operativa | Firmamento + PC Liguria |
| MS-F1-07 | M+18 | LoI 1 regione SNAI aggiuntiva (Piemonte / Calabria target) | Firmamento + Sales |
| MS-F1-08 | M+21 | Cooperative agricole DaaS ≥ 3 attive | Firmamento + Fabrica |
| MS-F1-09 | M+24 | **Gate Fase 2 — verdetto scale-up SNAI / consolidamento Liguria / pivot** | Firmamento + Investors |

### 11.2.5 Budget previsto Fase 1

Sintesi (dettaglio in Cap. 8 — Piano Economico-Finanziario):

| Componente | Y1 (M+0 → M+12) | Y2 (M+12 → M+24) | Note |
|---|---|---|---|
| CapEx (asset, hangar, GS) | €700-1200k | €300-500k | Y2: GS mobile + payload aggiuntivi |
| OpEx run-rate | €260-480k | €400-700k | Y2: +1 pilot + 1 sales + 1 data analyst |
| R&D Percorso 6B preliminare | €100-300k | €200-500k | Engineering + subscale design |
| Engagement EASA / partnership R&D | €30-80k | €50-150k | CIRA MOU + EASA pre-engagement |
| **Totale Fase 1** | **€1.1-2.1M** | **€1.0-1.9M** | Funding mix: vedi Cap. 8 |
| **Totale cumulato Fase 1** | | **€2.1-4.0M** | |

**Funding mix Fase 1** (preliminare, da consolidare): Coopfond Prototypes (€50k) + Coopfond Cooding-Invest (€150-300k) + Regione Liguria FESR (€200-400k) + PNRR Aerospazio (€0-200k) + R&D tax credit (€50-150k) + equity privato/fondatori (€200-400k) + (Y2) ARR €1.0-1.5M autofinanziato + Series Seed €500k-1.5M (Y2). Vedi Cap. 7 §7.12.2 e Cap. 8.

### 11.2.6 Stakeholder critici Fase 1

| Stakeholder | Ruolo Fase 1 | Action richiesta | Owner Firmamento |
|---|---|---|---|
| Regione Liguria | Anchor customer + sponsor istituzionale | LoI M+6, accordo quadro M+12 | CEO + Regulatory |
| Comune di Torriglia | Sede pilota Pentema | Delibera autorizzazione + comodato hangar | PM Pentema |
| Protezione Civile Liguria + ARPA | Cliente operativo primario | Protocollo operativo + retainer | Operations |
| Fabrica + 10 cooperative pilota | Co-progettisti + utenti | Contratto di rete operativo + workshop Q | Community Liaison |
| ENAC | Autorità regolatoria SORA | Pre-application + SORA approval | Regulatory Counsel |
| AGCOM | Autorità spettro | Licenza LTE tattico per missioni emergenza | Regulatory |
| Garante Privacy | Autorità data protection | DPIA pubblica + accettabilità sociale | Data Privacy Counsel |
| Coopfond + Fondazione PICO ETS | Finanziatore | Disbursement tranches Coopfond Prototypes + Invest | CFO |
| CIRA + POLITO DIMEAS | Partner R&D 6B | MOU R&D HALE preliminare | CTO + R&D |
| Comunità Pentema | Cittadini destinatari | Workshop pubblico + comunicazione trasparente | Community Liaison |

---

## 11.3 Fase 2 — Scale-up SNAI Italia (M+24 → M+36)

> **Stato verdetto Cap. 11**: Fase **non approvata oggi** — sottoposta al gate M+24 sulla base degli esiti Fase 1.
> **Riferimenti**: `riferimenti/visione-10-anni.md` §2 Fase 2; Cap. 7 §7.10 scale-up roadmap.
> **Confidence pianificazione**: **medium**.

### 11.3.1 Obiettivi specifici della Fase 2

| ID | Obiettivo | Verifica al gate M+36 |
|---|---|---|
| OBJ-F2-01 | Dimostrare scalabilità multi-regionale del modello | ARR ≥ €2-5M alla fine Y3 (M+36); ≥ 10 contratti istituzionali attivi |
| OBJ-F2-02 | Costruire la **flotta operativa** 3-8 piattaforme VTOL/MALE | 3-8 UAS in fleet (mix commerciali tier-1 + 1-2 custom Firmamento eventuali) |
| OBJ-F2-03 | Avviare lo sviluppo HALE subscale (1:3 scale) | TRL HALE = 5 (subscale flight test stratospheric o altitude chamber) |
| OBJ-F2-04 | Ottenere **primo finanziamento PNRR Aerospazio / FESR / Horizon** | ≥ €2-5M cumulato grants Y2-Y3 |
| OBJ-F2-05 | Costruire **team aerospace credibile** | 15-30 FTE; ≥ 3 senior aerospace (ex-Leonardo / TAS / CIRA / Polito) |
| OBJ-F2-06 | Engagement ASD-Eurospace HAPS working group | Posizione ufficiale in ASD-Eurospace HAPS WG; partecipazione EuroHAPS-adjacent |

### 11.3.2 Espansione geografica

| Anno | Aree SNAI servite | Stato target |
|---|---|---|
| Y2 (M+12 → M+24) | Liguria interna estesa (4 aree SNAI) + 1 area Piemonte SNAI | Operativo |
| Y3 (M+24 → M+36) | + Marche o Calabria o Basilicata (1-2 aree) | Operativo |

**Criterio scelta regioni Y3**: (i) aree SNAI con DGR attiva + FESR 2021-2027 disponibile, (ii) Protezione Civile regionale con storico contratti UAV, (iii) presenza cooperative Legacoop locali, (iv) accessibilità logistica e meteorologica. Candidate target (in ordine di preferenza): Piemonte Alpine, Marche Appennino, Calabria Sila, Basilicata.

### 11.3.3 Espansione flotta

| Anno | Composizione flotta target | Logica |
|---|---|---|
| Y2 (M+24) | 2 VTOL ibridi commerciali (JOUAV CW-30E o eq.) + 1 MALE leggero | Y1 VTOL replicato + introduzione MALE per copertura aree estese |
| Y3 (M+36) | 3-5 VTOL/MALE commerciali + (opzionale) 1 custom Firmamento eventuale | Costruzione capacità multi-regione |

**Nota su custom Firmamento**: la decisione di sviluppare un VTOL/MALE custom è **subordinata** al gate M+24 (a Y2 deve essere chiaro che l'offerta commerciale tier-1 non copre i requisiti operativi specifici). Modello service-only (B1) **preservato**: nessun product sale è previsto, il custom Firmamento sarà operato internamente.

### 11.3.4 Avvio HALE subscale (TRL 3 → 5)

Parallelamente allo scale-up VTOL/MALE, la Fase 2 attiva il **percorso R&D HALE** (Percorso 6B preparatorio) verso TRL 5:

- **Y2 (M+12-24)**: design subscale 1:3 (apertura alare 5-8 m, payload 0.5-1 kg). Validazione energy balance numerica (con margine ≥ 30% inverno 44°N). Consortium agreement con CIRA + POLITO + (target) Solvay (compositi) + Azur Space (celle).
- **Y3 (M+24-36)**: build subscale + flight test atmosferico (8-15 km alt) per validazione aero + control law. Engagement EASA per pre-application Special Condition. TRL atteso: 5.

Capital intensity R&D HALE Fase 2: €2-5M (cumulato Y2-Y3). Mix finanziamenti target: PNRR Aerospazio + FESR + R&D tax credit + Horizon Europe Cluster 5/4 + eventuale grant ASI.

### 11.3.5 KPI Fase 2

| KPI | Target Y2 (M+24) | Target Y3 (M+36) |
|---|---|---|
| Regioni SNAI servite | 1-2 | 3-4 |
| Flotta operativa | 2-3 UAS | 3-8 UAS |
| ARR | €1.0-1.5M | €2-5M |
| Contratti istituzionali attivi | ≥ 6 | ≥ 10 |
| FTE | 10-15 | 15-30 |
| TRL HALE subsystems critici | ≥ 5 (energy + aero) | ≥ 5 (system integrated subscale) |
| Grant cumulati | €0.5-1.5M | €2-5M |
| Posizione ASD-Eurospace HAPS WG | Engagement | Membership formale |
| NPS stakeholder PA | ≥ 50 | ≥ 50 sostenuto |

### 11.3.6 Budget previsto Fase 2

| Componente | Y2 (M+12 → M+24) | Y3 (M+24 → M+36) | Note |
|---|---|---|---|
| CapEx flotta + GS + infrastrutture | €0.5-1M | €1-2M | Acquisto/leasing UAS + GS regionali |
| OpEx (personale, operazioni) | €0.4-0.7M | €1-2M | Crescita team 15→30 FTE |
| R&D HALE subscale | €0.5-1.5M | €1.5-3.5M | Design + build subscale + flight test |
| Engagement regolatorio + EU | €100-300k | €200-400k | EASA pre-application + Bruxelles + ASD |
| **Totale Fase 2** | **€1.5-3.5M** | **€3.7-8M** | |
| **Cumulato Fase 1+2** | | **€7-15M** | |

**Funding mix Fase 2** (preliminare): ARR autofinanziato (~30-50%) + PNRR Aerospazio + FESR Liguria/altre regioni + Horizon Europe + Series Seed/A €3-8M + R&D tax credit. Vedi `riferimenti/visione-10-anni.md` §4.

---

## 11.4 Fase 3 — HALE Prototipo Operativo (M+36 → M+72)

> **Stato verdetto Cap. 11**: Fase **non approvata oggi** — sottoposta al gate M+36 (Phase B start 6B).
> **Riferimenti**: `riferimenti/visione-10-anni.md` §2 Fase 3; Cap. 5 §5.4 framework EASA Certified HAPS; Cap. 6 (energy balance e architettura HALE).
> **Confidence pianificazione**: **medium-low** (dipendenze EASA + capital + tecnologia batterie).

### 11.4.1 Obiettivi specifici

| ID | Obiettivo | Verifica al gate M+72 |
|---|---|---|
| OBJ-F3-01 | Sviluppare HALE prototipo full-scale operativo | HALE 20-30 m apertura alare, payload 5-10 kg, TRL 7 (system prototype in operational environment) |
| OBJ-F3-02 | Dimostrare **volo stratosferico continuativo ≥ 7 giorni** | ≥ 1 volo dimostrativo certificato a 18-20 km, ≥ 168 h continuous |
| OBJ-F3-03 | Erogare primo **servizio HAPS commerciale italiano** | ≥ 1 contratto servizio HAPS persistente operativo Y6 (target: Regione Liguria evolution o Sardegna o Puglia DTA-GATB) |
| OBJ-F3-04 | Engagement EASA Special Condition HAPS attivo | Rulemaking task Special Condition HAPS aperto formalmente; Firmamento riconosciuto come stakeholder rilevante |
| OBJ-F3-05 | Capital raise Series A-B | €5-15M raised cumulato Fase 3 |
| OBJ-F3-06 | Consortium IT/EU credibile per Fase 4 | MOU operativo CIRA + POLITO + (target) TAS-Leonardo o equivalente |

### 11.4.2 Sviluppo HALE full-scale + flight test

Il programma HALE full-scale procede in **3 sotto-fasi** allineate a NASA SE Handbook Phase B-C:

| Sotto-fase | Periodo | Obiettivo | TRL target |
|---|---|---|---|
| **3.1 — Design Phase B** | M+36 → M+48 | PDR (Preliminary Design Review) full-scale; consolidamento materiali (CFRP + lino) + propulsione + avionics; energy balance validato in cluster di esperti indipendenti | TRL 5-6 |
| **3.2 — Build + ground test** | M+48 → M+60 | CDR (Critical Design Review); build prototipo; ground test (vibrazione, ambiente, integrazione) | TRL 6-7 |
| **3.3 — Flight test stratosferico** | M+60 → M+72 | Flight test 18-20 km alt; volo continuativo ≥ 7 gg (target ≥ 30 gg) | TRL 7 |

**Showstopper tecnici dichiarati** (vedi Cap. 6 + `riferimenti/RESERVED-rischi-geopolitici.md` RSK-TEC-001/002):

1. **Energy balance inverno a 44°N** non chiuso strutturalmente: se al M+48 il margine energetico invernale dicembre 21 a 44°N è < 20%, il design deve **espandere la wing area** del 15-25% o **migrare la latitudine operativa** a < 42°N (Sardegna sud, Puglia, Sicilia).
2. **Aeroelasticità HAR wing**: se al M+48 i test wind tunnel + FEM rivelano flutter modes non controllabili in cruise, il design deve **ridurre AR** da 30+ a 20-25 (con costo prestazioni endurance).

### 11.4.3 Engagement EASA Special Condition

La Fase 3 è la fase in cui Firmamento deve **trasformare l'engagement EASA da informale a formale**:

| Milestone EASA | Mese | Stato target |
|---|---|---|
| EASA pre-engagement informale | M+12-24 (Fase 1-2) | Già in corso |
| EASA RMT (Rulemaking Task) Special Condition HAPS richiesta formale | M+24-36 (transizione Fase 2-3) | Formalizzata via ASD-Eurospace HAPS WG + EuroHAPS consortium |
| EASA Special Condition draft pubblicato | M+48-60 (Fase 3) | Target EU regulatory milestone |
| EASA Special Condition adopted | M+60-72 (gate Fase 3) | Critico per autorizzazione operativa commerciale Fase 4 |
| ENAC pre-application HALE Pentema/Sardegna | M+48-60 | Italia-specific |

**Falsifying observation**: se al M+48 EASA **non** ha aperto formalmente l'RMT Special Condition HAPS, la Fase 4 (costellazione operativa) è **bloccata regolatoriamente**. La roadmap va **ricalibrata**: HALE operativo solo come **demonstratore R&D**, non come asset commerciale, fino apertura framework. Vedi RSK-REG-001 (Cap. 5).

### 11.4.4 Servizio commerciale HAPS pilota

Target: **1 servizio HAPS commerciale italiano operativo entro Y6**, su area pilota in coordinamento ENAC.

Candidate aree:
- **Liguria Pentema-evolution** (continuità Fase 1-3, ma orografia complessa per HALE; possibile zona di emergenza Mediterraneo)
- **Sardegna sud / Sulcis** (latitudine 39-40°N, vento più favorevole, basso traffico, area SNAI presente)
- **Puglia DTA-GATB Grottaglie** (test bed BVLOS già esistente, latitudine 40°N, partnership DTA stabilita)

Use case primari servizio HAPS Fase 3 (orientato a `riferimenti/visione-10-anni.md` §4):
- **Monitoraggio EO persistente** (frane, antincendio multi-regione)
- **Connettività di emergenza estesa** (cluster aree SNAI Mediterraneo)
- **Servizi pre-NTN 5G** (testbed prima del commercial roll-out Fase 4)
- **Dual-use civile-difesa ISR** (NATO DIANA partnership, condizionato a engagement Difesa)

Pricing target Fase 3 (preliminare, confidence **low**): €1-3M/anno per area persistente; ARR target Fase 3 = €5-15M.

### 11.4.5 Partnership R&D (CIRA, POLITO, TAS-Leonardo conditional)

| Partner | Ruolo | Stato target M+72 | Condizioni |
|---|---|---|---|
| **CIRA** | Partner R&D primario (consortium MOU) | MOU operativo + co-engineering subscale → full-scale | Già da Fase 1 |
| **POLITO DIMEAS** | Partner accademico (lineage HELIPLAT) | Joint research + tesi di PhD + flight test support | Già da Fase 1 |
| **TAS-Leonardo** | Partnership condizionata (RSK-GEO-005) | MOU "Stratospheric Complementarity" + cooperazione su payload/avionics — **senza equity stake da loro** | **Solo se condizioni capital structure resistente preservate** |
| **Solvay (compositi)** | Supplier preferito CFRP + eventuale partnership R&D fibra di lino | Service agreement + co-development bio-composito | Da Fase 2 |
| **Azur Space (celle solari)** | Supplier preferito celle multi-junction EU | Supply agreement + supporto integration | Da Fase 2 |
| **DTA Puglia / GATB Grottaglie** | Test bed BVLOS + flight test stratosferico | Service agreement testing | Da Fase 1 |
| **ESA** | Partner R&D (futuro) | MoU su technology demonstration | Da Fase 3 |
| **ASD-Eurospace HAPS WG** | Industry alignment | Membership formale + leadership italiana | Da Fase 2 |

**Rischio cooperazione vs antagonismo TAS-Leonardo**: vedi RSK-GEO-005 (documento riservato). La partnership con TAS-Leonardo è **strumentale** alla preparazione della Fase 4 ma **non deve** trasformarsi in acquisizione difensiva. Capital structure resistente (founder maggioranza fino almeno M+72) è precondizione difensiva.

### 11.4.6 Budget €5.5-13.5M Phase B

Sintesi capital intensity Fase 3 (M+36 → M+72) — coerente con `riferimenti/visione-10-anni.md` §4 (Y4-Y6 €5-15M Series A-B + grant) e Cap. 8:

| Componente | M+36-48 (3.1 Design) | M+48-60 (3.2 Build+ground) | M+60-72 (3.3 Flight test) | Totale Fase 3 |
|---|---|---|---|---|
| R&D engineering | €1.0-2.0M | €1.5-3.0M | €1.0-2.0M | €3.5-7.0M |
| Prototype hardware (HALE full-scale) | €0.3-0.5M | €1.5-3.0M | €0.5-1.0M | €2.3-4.5M |
| Test (ground + altitude + flight) | €0.2-0.5M | €0.5-1.0M | €1.0-2.5M | €1.7-4.0M |
| Personnel R&D (30-60 FTE) | €1.5-3.0M | €2.0-4.0M | €2.5-5.0M | €6.0-12.0M |
| Engagement EASA + Bruxelles | €0.2-0.5M | €0.3-0.5M | €0.3-0.5M | €0.8-1.5M |
| Operativo VTOL/MALE continuativo | €1.0-2.0M | €1.0-2.0M | €1.5-2.5M | €3.5-6.5M |
| **Totale Fase 3** | **€4.2-8.5M** | **€6.8-13.5M** | **€6.8-13.5M** | **€17.8-35.5M** |

> ⚠ La cifra cumulata Fase 3 (€18-36M) è **più alta** della stima nella visione-10-anni.md §4 (€15-50M Y4-Y6) per la componente operativa VTOL/MALE continuativa. Aggiunge **R&D-load + scale-up operativo concorrente**, scenario realistico. Confidence: **medium-low**.

### 11.4.7 Capital raise Series A-B

| Round | Periodo | Importo target | Investor target |
|---|---|---|---|
| Series Seed | M+9-18 (Fase 1 fine) | €0.5-1.5M | Angels + Coopfond + family office IT |
| Series A | M+24-36 (Fase 2 fine) | €3-8M | VC IT (Primomiglio, P101, LIFTT) + CDP Venture Capital + EIC Accelerator |
| Series B | M+48-60 (Fase 3 build) | €10-30M | VC EU (Andera, EQT Ventures, Sofinnova) + EIB + sovereign IT (CDP) + EIC Fund |

**Pre-condizione capital structure resistente** (vedi `RESERVED-rischi-geopolitici.md` RSK-GEO-002 + RSK-GEO-005): founder team mantiene **≥ 51% voting** (anche tramite share class differenziate) o **golden share** fino a M+72. Investitori "non ostili": CDP + EIC + EIB preferred. Engagement preventivo con Dipartimento Coordinamento Politiche Economiche (Golden Power preview) prima del primo round estero.

---

## 11.5 Fase 4 — Costellazione Italiana Iniziale (M+72 → M+96)

> **Stato verdetto Cap. 11**: Fase **non approvata oggi** — sottoposta al gate M+72.
> **Riferimenti**: `riferimenti/visione-10-anni.md` §2 Fase 4; Cap. 5 §5.4 EASA framework HAPS.
> **Confidence pianificazione**: **low** (dipendenze EDF + IRIS² alignment + capital).

### 11.5.1 Obiettivi specifici

| ID | Obiettivo | Verifica al gate M+96 |
|---|---|---|
| OBJ-F4-01 | Operare costellazione iniziale 3-10 HAPS perennial italiani | ≥ 3 HAPS in operazione, ≥ 30 gg endurance dimostrato per piattaforma |
| OBJ-F4-02 | Erogare servizio NTN 5G NR-NTN regenerative payload | ≥ 1 servizio NTN 5G commerciale operativo (Rel-18/19 compliant) |
| OBJ-F4-03 | Servizio EO persistente con SLA contrattualizzati | Contratti pluriennali PA + PC Nazionale + utility (Enel, Snam, RFI) |
| OBJ-F4-04 | Posizionamento EU Strategic Autonomy | Riconoscimento ufficiale in dialogo IRIS² come complementary stratospheric layer |
| OBJ-F4-05 | Risposta a EDF call HAPS | Vincita o partecipazione lead a bando EDF HAPS €50-200M |
| OBJ-F4-06 | Capital raise Series B-C | €30-100M raised cumulato Fase 4 |
| OBJ-F4-07 | Crescita team a 60-150 FTE | 60-150 FTE; ≥ 10 senior aerospace; presenza Bruxelles + Roma + Liguria |

### 11.5.2 3-10 HAPS perennial operativi

Composizione flotta target Fase 4:

| Anno | HAPS perennial operativi | Endurance dimostrato | Servizio commerciale | Note |
|---|---|---|---|---|
| Y7 (M+84) | 1-3 | ≥ 7-15 gg | EO persistente + NTN testbed | Estensione Fase 3 |
| Y8 (M+96) | 3-10 | ≥ 30 gg | NTN 5G commerciale + EO contrattualizzato | Costellazione iniziale |

**Aree operative target**: Italia cluster Mediterraneo (Sardegna + Sicilia + Puglia + Liguria), eventuale estensione Adriatico orientale (Croazia / Albania via accordi bilaterali UE).

### 11.5.3 Servizio NTN 5G commerciale + EO persistente

Linee di servizio Fase 4 (in coerenza con `riferimenti/visione-10-anni.md` §4 e Cap. 7):

| Linea servizio | Cliente target | Pricing target | Maturità tecnica |
|---|---|---|---|
| **NTN 5G NR-NTN regenerative** wholesale | Telco IT (TIM, Vodafone, Iliad, WindTre, Open Fiber) | €/Mbps wholesale per area | 3GPP Rel-18 (2026) → Rel-19 (2028) [^14] |
| **EO persistente SLA contrattualizzato** | PA regionale + nazionale + utility | €0.5-2M/anno per area | TRL 8-9 |
| **Servizi sovrani secure** | Difesa, PC Nazionale, Intelligence (NATO DIANA) | Concessione + canone governativo | Condizionato a clearance |
| **Capacity wholesale per emergency response** | Reti EU emergency | €/Mbps event-based | Coordinato a EU sovereign |

ARR target Fase 4: **€30-80M** (coerente con visione 10 anni §2 Fase 4).

### 11.5.4 Engagement EU programmes (EDF, Horizon)

| Programma EU | Importo target | Periodo | Ruolo Firmamento |
|---|---|---|---|
| **EDF HAPS call** | €50-200M (consortium) | 2030-2032 (Y6-Y8) | Lead o co-lead consortium IT + EU partner |
| **Horizon Europe Cluster 4 / 5** | €5-20M | 2030-2033 | Lead specific work package |
| **Connecting Europe Facility 2 — Digital** | €10-50M | 2031-2033 | Co-investment infrastructure |
| **EIC Scaleup Fund** | €10-50M | 2032-2034 | Equity / quasi-equity |
| **EIB venture debt** | €20-100M | 2031-2035 | Debito strategico |
| **CDP / fondi sovrani IT** | €30-150M | 2032-2035 | Equity + golden share preview |

### 11.5.5 Capital raise Series B-C €30-100M

| Round | Periodo | Importo target | Investor target |
|---|---|---|---|
| Series B (extended) | M+60-84 | €15-50M | EU VC + EIB + CDP + strategic (mai TAS-Leonardo equity diretto fino post-M+72, vedi RSK-GEO-005) |
| Series C | M+84-96 | €30-100M (mix equity + debt + grant) | Sovereign EU + CDP + EIB + global VC specializzati infrastructure |

**Capital intensity cumulato Fase 4**: **€100-500M** (coerente con `riferimenti/visione-10-anni.md` §4).

---

## 11.6 Fase 5 — Consorzio EU Stratospheric Layer (M+96 → M+120)

> **Stato verdetto Cap. 11**: Fase **non approvata oggi** — sottoposta a gate Fase 4 (M+96).
> **Riferimenti**: `riferimenti/visione-10-anni.md` §2 Fase 5; `RESERVED-rischi-geopolitici.md` (RSK-GEO-001/004 per linguaggio).
> **Confidence pianificazione**: **speculative**.

### 11.6.1 Obiettivi specifici

| ID | Obiettivo | Verifica al M+120 |
|---|---|---|
| OBJ-F5-01 | Posizionamento ufficiale "nodo italiano del layer stratosferico EU sovereign" | Riconoscimento formale Commissione UE in architettura sovrana EU |
| OBJ-F5-02 | Consorzio EU 10-30 HAPS operativi (mix italiani + FR/DE/ES) | ≥ 10 HAPS perennial in costellazione EU coordinata |
| OBJ-F5-03 | Possibile bando Commissione equivalente IRIS² su HAPS | €1-5B EU contribution apertura programma o partecipazione |
| OBJ-F5-04 | Personale 150-500 FTE | Cresita coerente con scala |
| OBJ-F5-05 | Capital structure golden-power-compliant | Maggioranza italiana stabile; partecipazioni CDP/EIB/fondi sovrani EU |
| OBJ-F5-06 | Exit strategy / IPO / strategic consolidation | Decisione esit chiara: IPO, strategic exit, consolidation con player EU maggiore |

### 11.6.2 Posizionamento "nodo italiano del layer stratosferico EU sovereign"

Linguaggio pubblico Fase 5 (vedi `RESERVED-rischi-geopolitici.md` RSK-GEO-001/004):

- **Da usare**: "EU stratospheric sovereign infrastructure complementing Galileo, Copernicus, IRIS²"; "Italian leadership in EU stratospheric sovereignty"; "Stratospheric layer of EU multi-orbit sovereign architecture"
- **Da NON usare**: "Alternativa europea a Starlink"; "EU competitor to SpaceX"

Position paper strategici da pubblicare (target Fase 4-5):
- **Italian Stratospheric Sovereignty Position Paper** (M+12-24 baseline → aggiornamenti M+36, M+60, M+96)
- **EU Stratospheric Layer White Paper** (target Y4-Y5, co-firmato con MIMIT + ASI + EU partner)

### 11.6.3 Consorzio EU (Italia + FR/DE/ES)

Composizione target consorzio EU sovereign HAPS (Fase 5):

| Soggetto | Ruolo target | Stato Y10 atteso |
|---|---|---|
| **Firmamento Technologies (IT)** | Lead operatore servizi | Capofila stratosferico |
| **TAS-Leonardo (IT)** | Partner industriale italiano | Co-lead consortium |
| **CIRA + ASI (IT)** | Partner R&D + spaziale italiano | Coordinamento IT |
| **Thales (FR)** | Partner industriale francese | Sistema integrazione |
| **ONERA (FR)** | Partner R&D francese | Ricerca |
| **Airbus DS (FR/DE/ES)** | Partner industriale paneuropeo | Heritage Zephyr |
| **DLR (DE)** | Partner R&D tedesco | Ricerca + ground segment |
| **INTA (ES)** | Partner R&D spagnolo | Test + sustainability sud Europa |
| **ESA** | Coordinamento spaziale EU | Bridge satellite-stratospheric |
| **DG CNECT + DG DEFIS (CE)** | Sponsor istituzionale EU | Funding + governance |

> **Nota strategica**: la Fase 5 **richiede l'accettazione di TAS-Leonardo come co-lead** del consorzio EU, **non solo come partner subordinato**. Questo è il **trade-off strutturale** per evitare acquisition difensiva precoce (RSK-GEO-005): Firmamento offre a TAS-Leonardo un ruolo strategico in cambio della propria autonomia operativa. Confidence: medium su tale negoziazione.

### 11.6.4 Capital intensity onesta — scenari

In coerenza con `riferimenti/visione-10-anni.md` §4 (Caveat epistemico Regola 7):

| Scenario | Composizione flotta Y10 | Capital intensity totale Y1-Y10 | Dipendenza esterna |
|---|---|---|---|
| **Small fleet (baseline narrativa)** | 5-10 HAPS operativi (cluster IT) | **€500M-2B** | Capital IT + grant EU standard |
| **Medium fleet (scala IT operativa)** | 20-50 HAPS operativi (IT cluster + parte EU) | **€2-10B** | Programma EU dedicato HAPS attivato |
| **Large fleet (EU sovereign full scale)** | 100+ HAPS operativi (EU cluster sovereign) | **€10-30B** | Programma equivalente IRIS² da Commissione UE |

> **Falsifying observation chiave Fase 5**: se entro Y4-Y5 **non** esiste programma EU specifico per HAPS sovereign con budget multi-miliardario (analog IRIS²), lo scenario "Large fleet" è **strutturalmente non finanziabile**. La roadmap Fase 5 va **ridimensionata** allo scenario "Small fleet" o "Medium fleet". Confidence falsificabilità: **high**. Trigger osservabile: roadmap CE 2030+ pubblicata senza programma HAPS dedicato. Vedi `riferimenti/visione-10-anni.md` §4.

**Posizione strategica**: l'obiettivo "alternativa europea Starlink" è mantenuto come **vettore strategico** (boundary B2), indipendentemente dalla magnitudine effettiva del finanziamento richiesto. Il rigore epistemico è applicato a **come** arrivarci e a **scenari di scala onesti**, non al **se** sia l'obiettivo giusto.

### 11.6.5 Exit strategy / IPO / strategic consolidation

Opzioni di exit strategy ipotetiche al M+120 (Y10), in ordine di preferenza strategica:

1. **IPO Borsa Italiana segmento STAR / Euronext Milan** — preserva autonomia + accesso capitale pubblico. Pre-condizione: ARR ≥ €100-200M, ricorrente, multi-cliente, contratti pluriennali.
2. **Strategic consolidation con consorzio EU sovereign** — Firmamento entra in joint venture EU con golden share italiana preservata. Pre-condizione: programma equivalente IRIS² attivato + governance EU favorevole.
3. **Acquisizione strategica da CDP / fondi sovrani EU** — concessione EU/IT-controlled. Compatibile con Golden Power. Founder team mantiene ruolo operativo.
4. **Acquisizione da TAS-Leonardo o equivalente incumbent EU** — esit "fair value" (5-15× revenue) ma **fine traiettoria indipendente**. Vedi RSK-GEO-005: scenario da **evitare strategicamente**, non da escludere se condizioni di mercato sfavorevoli.

Decisione exit deferita a gate M+96 (entrata Fase 5).

---

## 11.6bis Scenario B2-relaxed: "Standalone IT Operator Small Fleet" (Y10 alternative)

> **Stato verdetto Cap. 11**: scenario **alternativo riconosciuto esplicitamente** — non è verdetto del gate, è esito operativo Y10 attivato dal verificarsi dei trigger esterni descritti in §11.6bis.2.
> **Riferimenti**: §11.6 Fase 5 baseline; `riferimenti/visione-10-anni.md` §4 "small fleet"; `riferimenti/RESERVED-rischi-geopolitici.md` RSK-GEO-001/004; `studio-di-fattibilita/AUDIT-QUALITY-VOLUME-1.md` §2 (raccomandazione fix Cap. 11).
> **Confidence pianificazione scenario**: **medium** (più realistico di Fase 5 full).
> **Confidence numerica ARR Y10 €30-80M**: **medium-low** (extrapolation, no triangulation indipendente).
> **Confidence probabilità scenari Y10**: **low** (judgment progetto, base rate aerospace).

### 11.6bis.1 Razionale dello scenario

L'audit avversariale ha identificato (`AUDIT-QUALITY-VOLUME-1.md` §2 Cap. 11) un'omissione strutturale del capitolo: la roadmap descrive con cura le Fasi 1-5 e dichiara onestamente la confidence speculative della Fase 5, ma **non articola lo scenario alternativo realistico** in cui le pre-condizioni esterne della Fase 5 non si verificano. La probabilità marginale di successo Fase 5 in autonomia è stimata **~6-15%** (stratificazione dipendenze multiple, vedi §11.9 + base rate "aerospace startup → €100M+ ARR in 10 anni" inferiore al 5% — cfr. McKinsey 2023 "Space economy report"; AIAD 2025 dati ricavi medi startup aerospace italiana).

In assenza di uno scenario B2-relaxed esplicitato, il Cap. 11 corre due rischi:
1. **Rischio narrativo asimmetrico**: presentare la Fase 5 full come "il successo" e tutto il resto come "fallimento implicito", inducendo a sovrastimare la probabilità di traiettorie estreme (95% fallimento totale + 5% successo totale).
2. **Rischio strategico di pianificazione**: in assenza di articolazione del Plan B credibile, Firmamento rischierebbe di rifiutare opzioni operative razionali (es. consolidamento standalone IT) come "non in linea con la visione", quando invece queste sono **esiti di successo dimensionati al contesto**.

Lo scenario **B2-relaxed** corregge questa asimmetria. Esso preserva la **boundary B2 originale** (visione "EU sovereign stratospheric layer / complementare a IRIS²") come **target aspirazionale di lungo termine**, ma riconosce che la traiettoria intermedia Y10 più probabile può essere una versione "standalone Italia" dello stesso modello, da cui è possibile rilanciare la traiettoria EU full in finestra Y10-Y15 quando/se le pre-condizioni maturano.

### 11.6bis.2 Trigger di attivazione dello scenario B2-relaxed

La transizione dalla traiettoria "Fase 5 full" alla traiettoria "B2-relaxed standalone IT" è attivata **non da una decisione interna**, ma dal **verificarsi (anche parziale)** di uno o più dei seguenti **trigger esterni osservabili**, monitorati a ogni gate post-Studio:

| Trigger ID | Trigger osservabile | Finestra di osservazione | Severità | Effetto su traiettoria |
|---|---|---|---|---|
| **TRG-B2R-01** | EASA RMT HAPS non aperto formalmente (no NPA Special Condition pubblicato) | M+48 → M+60 (Y4-Y5) | **Critical** | Impossibile certificazione perennial Y6+ → no Fase 4 commerciale → flotta operativa standalone IT con framework Special Condition nazionale (ENAC LRA / Special Limited Cat) |
| **TRG-B2R-02** | Commissione UE non lancia programma equivalente IRIS² stratospheric entro M+60-72 | M+60 → M+72 (Y5-Y6) | **Critical** | Fase 5 full non finanziabile → scenario "Small fleet" `visione-10-anni.md` §4 attivato |
| **TRG-B2R-03** | Capital raise Series C €50M+ non chiuso entro M+84-96 | M+84 → M+96 (Y7-Y8) | **High** | Crescita flotta limitata a quanto auto-finanziabile da ARR + grant + EIB venture debt — no scalabilità EU |
| **TRG-B2R-04** | Acquisition offer non-strategic da Tier 1 globale (Airbus, Boeing, Lockheed) **rifiutata** dal board Firmamento | M+48 → M+72 (Y4-Y6) | **High** | Firmamento opta per continuity standalone IT — preserva autonomia ma rinuncia a velocità di scala internazionale |
| **TRG-B2R-05** | Geopolitica EU-US deteriora con consortium-mandate restrittivi (es. restrizioni export ITAR/EAR su HAPS dual-use, blocco partnership FR/DE su Air Combat sovereign) | M+36 → M+96 (Y3-Y8) | **Medium-High** | Consorzio EU 5-stati non costruibile → fallback IT standalone con eventuali bilaterali (IT-FR Trattato del Quirinale; IT-DE estensione) |
| **TRG-B2R-06** | Tech batterie Li-S / Solid-State Li non raggiungono target ≥ 350 Wh/kg pack aerospace-qualified entro M+72 (Y6) | M+60 → M+72 (Y5-Y6) | **Critical** | Energy balance HALE inverno non chiuso → flotta perennial italiana limitata a 5-10 piattaforme operative nelle finestre stagionali favorevoli (no scala EU 100+ HAPS) |

> **Logica di attivazione**: il verificarsi di **almeno 2 trigger su 6** (peso Critical doppio, High singolo) entro la finestra di osservazione corrispondente attiva la **revisione formale del Cap. 11 al gate successivo**, con riposizionamento della traiettoria Fase 5 full → B2-relaxed. La decisione formale spetta al board su raccomandazione di CEO + CFO + sovereign-infrastructure-strategist.
>
> **Falsifying observation di attivazione (FO-F11-07, nuovo)**: se al M+72 (Y6) si verificano **≥ 3 trigger** tra TRG-B2R-01/02/06 (i 3 Critical), lo scenario B2-relaxed è **traiettoria operativa di default**, e B2 full diventa **option di lungo termine** (rilancio Y10-Y15 se condizioni esterne maturano). Confidence falsificabilità: **high**.

### 11.6bis.3 Caratteristiche operative Y10 nello scenario B2-relaxed

| Dimensione | Configurazione B2-relaxed Y10 | Note |
|---|---|---|
| **Flotta HAPS perennial** | 5-10 piattaforme operative | Operate nelle finestre stagionali primavera-estate-autunno; ridotta operatività invernale (limitata energy balance senza batterie 350 Wh/kg) |
| **Flotta VTOL/MALE** | 10-20 piattaforme service-only | Operatività continuativa 12 mesi/anno; replacement asset Y6-Y10 |
| **Geografia operativa** | Italia (10-12 regioni SNAI + utility nazionale) | No copertura EU multi-paese; possibili estensioni mirate (es. canali Adriatico tramite accordi bilaterali) |
| **Clienti primari** | PA regionale + nazionale + cooperative + utility (Enel, Snam, RFI, Terna ispezione infrastrutture lineari) | Modello B2G + B2B2C; servizi sovrani secure su scala IT |
| **Modello business** | Service-only (boundary B1 mantenuto integralmente) | Cooperative Legacoop preservate come anchor + delivery partner |
| **Personnel** | ~80-150 FTE (range medio 110) | Mix: 35-45% engineering, 20-25% operations, 15-20% commerciale + delivery, 15-20% G&A; presenza Liguria + Roma + presenza minima Bruxelles |
| **Capital structure** | Maggioranza italiana stabile; CDP Venture / EIB / Italian sovereign fund (es. Fondo Italiano Aerospazio AIAD) come anchor; eventuale partecipazione strategic IT (TAS-Leonardo minoranza) sotto Golden Power | No Series mega (€100M+); rounds dimensionati a esigenze operative |
| **Capital intensity totale 10y** | **€500M - €1.5B** (mediana ~€800M-1B) | Vs **€10-30B** scenario Fase 5 full EU sovereign |

**Rationale capital intensity €500M-1.5B**: stima preliminare bottom-up: 5-10 HAPS × €15-30M unit cost (perennial qualified, scala manifatturiera bassa) = €75-300M flotta HAPS + 10-20 VTOL/MALE × €1-3M = €10-60M flotta VTOL + €30-80M ground segment (4-6 GCS regionali + spettro + datacenter) + €15-40M R&D HALE cumulato + €30-100M OpEx cumulato Y1-Y10 + €100-300M contingency + replacement = range **€260M-880M centrale, €500M-1.5B con cushion sovereign + golden share preview**. Confidence: **low** (extrapolation), da rifinire in Volume 2 modello finanziario.

> **Confronto con scenario "Small fleet" di `visione-10-anni.md` §4** (€500M-2B): coerente, con range ridimensionato verso il basso (€500M-1.5B) per riflettere geografia limitata a IT + assenza componente "EU sovereign program" addizionale.

### 11.6bis.4 KPI scenario B2-relaxed (target Y10)

| KPI | Target B2-relaxed Y10 | Confidence | Verificabilità |
|---|---|---|---|
| **ARR Y10** | €30-80M (target mediano €50M) | **medium-low** | Verificabile da bilanci certificati Y10 |
| **EBITDA margin Y10** | 20-35% (target 27%) | **medium-low** | Bilanci Y10 certificati |
| **Numero clienti pluriennali Y10** | 15-30 (PA regionale 10-15 + nazionale 2-4 + utility 3-7) | **medium** | Contratti pluriennali cumulati Y6-Y10 |
| **Numero HAPS perennial operativi** | 5-10 (Italia, finestre stagionali primaria) | **medium** | Flight log + ENAC LRA reports |
| **Numero VTOL/MALE operativi** | 10-20 | **high** | Asset register |
| **Numero coperture territoriali SNAI** | 30-50 aree interne servite (≥ 10 regioni IT) | **medium** | Reportistica SNAI + Regioni |
| **FTE** | 80-150 | **medium** | HR records |
| **Exit options Y10** | (a) IPO segmento STAR €100-300M valuation; (b) Strategic exit a CDP/EIB sovereign; (c) Continuity privata con dividend distribution | **low** | Decisione board Y9-Y10 contestuale |

**KPI di salute strategica scenario B2-relaxed** (oltre i KPI finanziari):
- Riconoscimento Firmamento come **operatore di riferimento IT** per servizi UAS infrastrutturali (~30% market share IT B2G + ~15-25% market share IT utility ispezione lineare entro Y10);
- Mantenimento **cooperative Legacoop** come delivery + workforce partner (boundary B1 preservata);
- **Position paper "Italian Stratospheric Sovereignty"** pubblicato e riconosciuto da MIMIT / ASI come reference document, anche in assenza di Fase 5 full;
- **Option preservata** per rilancio EU consortium in finestra Y10-Y15 se condizioni esterne maturano (board mantiene opzionalità).

### 11.6bis.5 Confronto onesto B2 full vs B2-relaxed

| Dimensione | B2 full (consorzio EU) | B2-relaxed (standalone IT) |
|---|---|---|
| **Orizzonte temporale** | Y8-Y10 attivazione Fase 5 | Y6-Y10 consolidamento traiettoria IT |
| **Capital intensity 10y** | **€10-30B** (programma EU IRIS²-equivalent) | **€500M-1.5B** (mix equity IT + grant + sovereign) |
| **Probabilità di successo (Y10)** | **6-15%** | **30-50%** |
| **ARR Y10** | €100-500M | €30-80M |
| **Flotta HAPS perennial Y10** | 10-30 (cluster EU) → fino 100+ scala full | 5-10 (cluster Italia) |
| **Geografia operativa Y10** | EU multi-paese (IT lead + FR/DE/ES) | Italia + bilaterali mirati |
| **Personnel Y10** | 150-500 FTE | 80-150 FTE |
| **Capital structure** | Maggioranza IT + golden share + co-investment EU sovereign + private mega-rounds | Maggioranza IT + CDP/EIB/Italian sovereign fund |
| **Strategic posture** | Co-fondatore EU sovereign stratospheric layer | Operatore IT specializzato di riferimento |
| **Exit Y10** | IPO con strong valuation (€500M-2B) o strategic con golden share preserved | IPO segmento STAR (€100-300M) o continuity privata o strategic exit a sovereign IT |
| **Boundary B2 originale** | Pieno (target aspirativo realizzato) | **Ridimensionato** (Italia, non EU) — boundary B2 mantenuta come option di lungo termine |
| **Coerenza con boundary B1** | Piena (service-only + cooperative) | Piena (service-only + cooperative) |
| **Confidence pianificazione** | **speculative** (dipendenze esterne strutturali) | **medium** (esecuzione largamente sotto controllo Firmamento + Italia) |

### 11.6bis.6 Distribuzione di probabilità degli esiti Y10 (consolidata)

Stima consolidata della distribuzione degli **esiti possibili al Y10**, condizionata al verdetto target Cap. 10 (Go Condizionato Fase 1 + Hold preparato Fase 3):

| Esito Y10 | Probabilità stimata | Confidence stima | Trigger osservabili |
|---|---|---|---|
| **B2 full — Consorzio EU sovereign Fase 5 operativo** | **6-15%** | **low** | Tutti i 5 vincoli esterni §11.1.4 soddisfatti + esecuzione disciplinata; programma EU multi-miliardario attivato |
| **B2-relaxed — Standalone IT Operator Small Fleet** | **30-50%** | **low-medium** | Esecuzione disciplinata Fasi 1-3 + ≥ 1 trigger §11.6bis.2 attivato + sovereign IT funding accessibile |
| **Acquisizione difensiva da TAS-Leonardo / Tier 1 globale (finestra Y3-Y5)** | **50-70%** condizionata al **non** soddisfacimento di RSK-GEO-005 mitigation | **medium** | Capital structure non resistente OR offerta strategica + board ratification + condizioni di mercato VC sfavorevoli |
| **Dissoluzione Y3-Y5 per esaurimento cash (no Series A o B chiuso)** | **20-30%** | **medium** | Series A non chiuso entro M+36 OR Series B non chiuso entro M+60 + ARR < €2M Y3 + grant non vinte |

> **Nota metodologica sulla somma delle probabilità**: le probabilità sopra **non sono mutuamente esclusive** in tutti i casi. Es. uno scenario di "dissoluzione" esclude tutti gli altri; "acquisizione difensiva" è esclusiva degli scenari B2; B2 full e B2-relaxed sono **sequenziali alternativi** condizionati ai trigger §11.6bis.2. Una rappresentazione decision-tree formale è oggetto di analisi nel **Volume 2 Risk Register §RSK-STRAT** (in lavorazione).
>
> **Implicazione probabilistica chiave**: lo scenario **modale (più probabile singolo)** è acquisizione difensiva, lo scenario **target di gestione attiva** è B2-relaxed, lo scenario **vettore aspirazionale** è B2 full. La gestione strategica Firmamento deve attivamente **mitigare scenario "acquisizione difensiva"** (vedi RSK-GEO-005 in `RESERVED-rischi-geopolitici.md`) e **costruire infrastruttura per B2-relaxed** come base credibile, mantenendo B2 full come **option di lungo termine** attivabile.

### 11.6bis.7 Implicazione strategica e calibrazione del messaggio esterno

Il riconoscimento esplicito dello scenario B2-relaxed **non modifica** il vettore strategico B2 originale dichiarato nelle boundary conditions (`CLAUDE.md` + `visione-10-anni.md`): la visione "EU sovereign stratospheric layer / complementare a IRIS²" rimane **target aspirativo** e **disciplina pubblica del linguaggio**.

Lo Studio di Fattibilità **deve tuttavia** integrare le seguenti calibrazioni operative:

1. **Calibrazione finanziaria (Cap. 8)**: il modello finanziario deve includere **scenario B2-relaxed** come **caso base operativo Y6-Y10** (ARR €30-80M, EBITDA 20-35%, capital intensity €500M-1.5B), non come "fallback negativo". Lo scenario B2 full è caso **upside** con probabilità dichiarata 6-15%.
2. **Calibrazione pricing (Cap. 7)**: il pricing dei servizi PA + utility deve essere **sostenibile in scala IT standalone** (no riferimento implicito a "EU sovereign full scale economies"). Pricing target PA €100-200k/anno regione + utility €0.5-2M/anno per linea-servizio coerente con scala B2-relaxed.
3. **Calibrazione partnership (§11.6.3 + §11.9.4)**: la matrice partnership EU 5-stati è vincolata alla traiettoria B2 full. Per B2-relaxed, la matrice si riduce a (a) IT core: TAS-Leonardo / CIRA / ASI / MIMIT, (b) bilaterali mirati IT-FR (Trattato del Quirinale stratospheric annex) e IT-DE (estensione MoU TAS Italia-DE), (c) ESA come bridge istituzionale. Niente consorzio formale 5-stati nello scenario B2-relaxed.
4. **Comunicazione esterna calibrata**: il messaging pubblico deve evolvere da "alternativa Starlink europea inevitabile" (linguaggio interno scartato) verso "**Standalone IT operator + future option EU consortium**", posizione **difendibile e onesta** verso:
   - **Investitori VC + sovereign IT**: scenario base B2-relaxed è investment-grade (ARR €30-80M, multipli sostenibili); B2 full è option upside non promessa.
   - **Coopfond / Legacoop**: scenario B2-relaxed preserva integralmente boundary B1 (modello cooperativo) e ARR sufficiente a sostenere quote partnership stabili.
   - **MIMIT / Presidenza Consiglio (Golden Power)**: scenario B2-relaxed è coerente con politica industriale "campioni italiani aerospazio" (vedi AIAD priorità 2025-2030) anche in assenza di programma EU sovereign HAPS.
   - **Commissione UE (DG CNECT/DEFIS)**: posizionamento Firmamento come "Italian readiness for EU stratospheric layer when programma matures" — Firmamento non chiede sussidio EU per giustificare la propria esistenza; offre asset IT pronto per scaling EU futuro.
5. **Calibrazione documento riservato**: aggiornare `RESERVED-rischi-geopolitici.md` con la riconoscenza che lo scenario B2-relaxed **riduce significativamente l'esposizione** a RSK-GEO-001 (frizione USA) e RSK-GEO-003 (export restrictions su HAPS dual-use), perché Firmamento standalone IT è meno "rilevante geopoliticamente" rispetto a un consorzio EU sovereign formale.

### 11.6bis.8 Falsifying observations dello scenario B2-relaxed

- **FO-F11-07 (nuova)**: se al **M+72 (Y6)** Firmamento è **single-player IT con ARR < €15M** e **zero traction in consortium EU formale** (no MoU bilaterale FR/DE/ES firmato, no risposta a EDF HAPS call), **lo scenario B2-relaxed è la traiettoria operativa di default**, e **B2 full diventa "blue sky aspiration"** sospesa. Confidence falsificabilità: **high**. Trigger osservabile: bilanci certificati Y5-Y6 + register di MoU/contratti EU.
- **FO-F11-08 (nuova)**: se al **M+96 (Y8)** ARR Y8 < €15M **e** flotta HAPS perennial < 3 operative in finestre stagionali primarie, **lo scenario B2-relaxed stesso è in difficoltà**: la traiettoria operativa converge verso "operatore VTOL/MALE service-only IT specializzato" (no HAPS perennial) — scenario residuale **non coperto** dalla boundary B2 originale, da rivedere con board come **strategic pivot** o **continuity privata small-scale**. Confidence falsificabilità: **high**.

> **Nota onesta**: nessuna delle due falsifying observations sopra implica "fallimento del progetto Firmamento". Implicano semplicemente che la traiettoria operativa effettiva **diverge dal vettore strategico aspirazionale B2 full** e si stabilizza su una scala operativa **inferiore** ma **ancora coerente** con modello service-only + cooperative + value creation territoriale italiana. Il rigore epistemico richiede di **chiamare le cose con il loro nome**: B2-relaxed è successo dimensionato, non fallimento dimensionato.

### 11.6bis.9 Verdetto del paragrafo

Lo scenario **B2-relaxed "Standalone IT Operator Small Fleet"** è:
- **Strategicamente onesto** — riconosce la distribuzione di probabilità reale degli esiti Y10 senza diluire la boundary B2 originale.
- **Operativamente attivabile** — i trigger §11.6bis.2 sono osservabili a gate intermedi M+48/M+60/M+72/M+96.
- **Finanziariamente difendibile** — ARR €30-80M / EBITDA 20-35% / capital intensity €500M-1.5B è investment-grade per VC sovereign IT + CDP + EIB anchor.
- **Coerente con boundary B1 + B2** — service-only + cooperative preservati; B2 mantenuta come option lungo termine.
- **Comunicabile esternamente** — il framing "standalone IT operator + future option EU consortium" è la posizione **più difendibile** vs investitori, MIMIT, Commissione UE e USA (vedi §11.6bis.7).

Il presente paragrafo §11.6bis **non modifica** il verdetto target Cap. 10 (Go Condizionato Fase 1 + Hold preparato Fase 3) né il vettore B2 originale. **Aggiunge** una rete di sicurezza strategica esplicita che migliora la qualità decisionale del board a tutti i gate post-Studio.

---

## 11.7 Gate decisionali post-Studio

Sintesi dei gate decisionali della roadmap (in coerenza con NASA SE Handbook §6.7 Phase B-F e con Cap. 9 cronoprogramma):

| Gate | Mese | Decisione | Criteri Go | Criteri Hold | Criteri No-Go |
|---|---|---|---|---|---|
| **Gate M+10/M+11** | M+10/M+11 | Approvazione Studio (Volume 1) | Tutti i criteri Cap. 3 §3.2 soddisfatti | ≥ 30% criteri non soddisfatti | Showstopper insuperabile (ENAC nega path SAIL, Regione si tira indietro, fonti azzerate) |
| **Gate M+12** | M+12 | Continuazione operatività Y1 → preparazione scale-up | ARR Y1 ≥ €200k + ≥ 3 contratti + 0 incidenti FATAL + SORA approvata | ARR €100-200k OR 1-2 contratti OR utilization <40% | ARR < €100k + 0 contratti |
| **Gate M+24** | M+24 | Attivazione Fase 2 scale-up + start Phase B 6B | KPI Fase 1 Y2 raggiunti (ARR €1-1.5M, ≥ 2 regioni LoI, TRL HALE ≥ 4) | KPI Fase 1 Y2 parziali (ARR €0.5-1M, 1 regione) | KPI Fase 1 Y2 falliti (ARR < €0.5M) |
| **Gate M+36** | M+36 | Attivazione Fase 3 HALE Phase B full | ARR ≥ €2M + 3+ regioni + TRL HALE ≥ 5 + Series A €3-8M raised + EASA RMT formalizzato | KPI Fase 2 parziali | KPI Fase 2 falliti + EASA RMT non aperto |
| **Gate M+48** | M+48 | PDR HALE full-scale + check energy balance | Energy balance margine ≥ 20% inverno + PDR clean + Series B preparation | Energy balance margine 10-20% (redesign) | Energy balance < 10% margin (showstopper RSK-TEC-001) |
| **Gate M+60** | M+60 | CDR HALE full-scale + build approval | CDR clean + ground test partial + flight test plan + Series B €10-30M raised | CDR conditional | CDR fail OR Series B failed |
| **Gate M+72** | M+72 | Attivazione Fase 4 costellazione iniziale | Flight test stratosferico ≥ 7 gg + ARR €5-15M + EASA Special Condition draft pubblicato + servizio HAPS pilota commerciale 1× attivo | Flight test parziale OR ARR €2-5M | Flight test fail OR EASA SC bloccata |
| **Gate M+96** | M+96 | Attivazione Fase 5 consorzio EU sovereign | 3-10 HAPS operativi + ARR €30-80M + EDF HAPS attivato + position paper EU stratospheric riconosciuto | KPI Fase 4 parziali | KPI Fase 4 falliti OR programma EU sovereign non aperto |
| **Gate M+120** | M+120 | Exit strategy / IPO / strategic consolidation | 10-30 HAPS operativi + ARR ≥ €100M + posizionamento EU sovereign formalizzato | KPI parziali (consolidamento scala IT) | Exit forzato (acquisizione difensiva) |

> **Verdetto Cap. 11 sul gate framework**: il gate framework è **NASA SE-compatible** (Phase B → C → D → E → F lifecycle) ed è **art. 41 D.Lgs. 36/2023-compatible** (sequenza PFTE → progetto definitivo → operatività). I criteri quantitativi sono **falsificabili** e **verificabili** ai gate intermedi.

---

## 11.8 Risk milestones e showstopper potenziali nel tempo

Sintesi degli showstopper noti per fase (dettaglio in Cap. 6 FMECA/FTA + Risk Register Vol. 2):

### 11.8.1 Showstopper Fase 1 (M+0 → M+24)

| Showstopper | Probabilità | Impatto | Mitigazione | Trigger osservabile |
|---|---|---|---|---|
| **ENAC nega SAIL II-III per Pentema** (Cap. 5 RSK-REG-002) | L-M | H | Pre-application + GRC argument robusto + M1/M2 mitigation | ENAC formal denial pre-application |
| **Regione Liguria non firma LoI / DGR** | L | H | Engagement preventivo + alternative regioni SNAI ready | Mancata risposta Regione M+6 |
| **Anchor customer non genera revenue Y1 ≥ €200k** (Cap. 7 §7.9.3) | M | H | Pivot pricing + B2B aggressivo + cooperative scaled | M+9 firma contracts < 2 |
| **AGCOM nega spettro LTE tattico** | L | M-H | Bande alternative + partnership telco | AGCOM denial M+6 |
| **Garante Privacy sospende missioni** | L | H | DPIA + comunità engagement + geofence | Provvedimento Garante M+0-12 |

### 11.8.2 Showstopper Fase 2 (M+24 → M+36)

| Showstopper | Probabilità | Impatto | Mitigazione | Trigger osservabile |
|---|---|---|---|---|
| **Scale-up SNAI 1+ regioni fallisce** | M | H | LoI multiple + sales pipeline diversified | M+30 0 LoI nuove regioni |
| **Series A €3-8M non raised** | M | H | Multi-investor strategy + grant alternative + slow growth path | Series A closed M+36 sotto target |
| **Talent gap (mancata acquisizione 3+ senior aerospace)** | M | M | Partnership Polito + CIRA + ex-Leonardo network + ESOP competitivo | M+36 < 15 FTE |
| **TRL HALE subscale < 5** | M | M | Redesign + extension Fase 2 + delay Fase 3 | M+36 flight test subscale fail |
| **EASA RMT Special Condition non aperto** (Cap. 5 RSK-REG-001) | M | H | Engagement EuroHAPS + ASD-Eurospace + EuroHAPS-adjacent | M+36 EASA NPA non pubblicato |

### 11.8.3 Showstopper Fase 3 (M+36 → M+72)

| Showstopper | Probabilità | Impatto | Mitigazione | Trigger osservabile |
|---|---|---|---|---|
| **Energy balance HALE inverno non chiuso** (RSK-TEC-001) | M | H | Espansione wing area + migrazione latitudine + battery LiS/SS | M+48 PDR energy margine < 20% |
| **Aeroelasticità HAR wing flutter non gestito** (RSK-TEC-002) | M | H | Riduzione AR + reinforcement + GVT in fase precoce | M+48 PDR aeroelastic fail |
| **EASA Special Condition HAPS bloccata** | M | H | Engagement intensivo Bruxelles + alternativa Type Cert custom | M+60 EASA NPA bloccato |
| **Series B €10-30M non raised** | M | H | EU sovereign engagement + EIB + CDP + EIC Fund | M+60 Series B sotto target |
| **Acquisizione difensiva da Leonardo/TAS** (RSK-GEO-005 riservato) | M | H | Capital structure resistente + speed esecuzione + cooperative anchor | Approccio informale TAS-Leonardo per equity |
| **Geopolitica EU-US degrada** (RSK-GEO-001 riservato) | L-M | M-H | Linguaggio "complementare IRIS²" + supply chain EU + dialogue Atlantico | Communiqué USA contro HAPS EU |
| **Supply chain non-EU disruption** (RSK-GEO-003 riservato) | M | H | EU sovereign suppliers roadmap + buffer 12 mesi + Critical Raw Materials Act | Lead time fornitori critici > 12 mesi |

### 11.8.4 Showstopper Fase 4-5 (M+72 → M+120)

| Showstopper | Probabilità | Impatto | Mitigazione | Trigger osservabile |
|---|---|---|---|---|
| **Geopolitica EU-US escalation** (RSK-GEO-001 riservato) | M | H | Linguaggio "complementare IRIS²" + dialogue Atlantico + NATO DIANA partnership | Restrizioni export US componenti HAPS |
| **IRIS² consortium esclude HAPS layer** (RSK-GEO-004 riservato) | M | H | Position paper "Stratospheric Complementarity" + DG CNECT/DEFIS engagement | IRIS² roadmap senza layer stratosferico Y4-Y5 |
| **Capital intensity Y8-Y10 insufficiente (no programma EU sovereign)** | **H** (per scala full EU sovereign) | **H** | Ridimensionamento scala "small fleet" + EIB venture debt + CDP equity | Roadmap CE 2030+ pubblicata senza HAPS programma |
| **Acquisizione difensiva forzata da consolidatore EU** | M | H | IPO ready + capital structure golden-power-compliant + multiple investor strategy | Approccio Airbus/Thales/Leonardo per acquisizione M+96+ |
| **Quadro politico EU instabile (break-up funzionale)** | L | H | Coordinamento bilaterale IT-FR-DE diretto + nazionalizzazione parziale | Crisi politica EU profonda 2030+ |

---

## 11.9 Dipendenze critiche esterne

Le 5 dipendenze esterne strutturali della roadmap (sintesi; alcune già citate in §11.1.4 e §11.8):

### 11.9.1 Apertura framework HAPS EASA entro 2030

**Dipendenza**: EASA pubblica entro 2030 una **Certification Specification + Special Condition operativa per HAPS** che consenta operatività commerciale civile.
**Stato attuale (M+0, maggio 2026)**: nessun framework EASA HAPS Certified. NPA EASA non ancora pubblicato.
**Trigger osservabile**: EASA RMT Special Condition HAPS aperta formalmente entro M+36; NPA pubblicato entro M+48; Special Condition adopted entro M+60-72.
**Falsifying observation**: se entro M+60 (2031) EASA non ha pubblicato Special Condition HAPS adopted, la Fase 4 (costellazione operativa commerciale) è **regolatoriamente bloccata**. La roadmap va riconfigurata su scenario "HALE demonstrative R&D only" fino apertura framework.
**Mitigazione**: engagement EuroHAPS + ASD-Eurospace HAPS WG + leadership ENAC italiana in EASA committee.

### 11.9.2 Programma sovrano EU stratospheric (analog IRIS²) entro 2030+

**Dipendenza**: Commissione UE apre programma equivalente IRIS² su HAPS con budget multi-miliardario (€10B+) entro Y4-Y5.
**Stato attuale (M+0, maggio 2026)**: IRIS² in implementazione (170-300 sat LEO/MEO, €10.6B, operatori Airbus-Eutelsat-Thales-Telespazio-Hispasat-OHB-DT-Orange). **Nessun programma EU sovereign HAPS aperto a oggi**.
**Trigger osservabile**: roadmap Commissione UE 2030+ pubblicata con o senza programma HAPS dedicato.
**Falsifying observation**: se entro Y4-Y5 nessun programma EU sovereign HAPS multi-miliardario è aperto, lo scenario "Large fleet EU sovereign" è **strutturalmente non finanziabile**. Fase 5 deve essere ridimensionata.
**Mitigazione**: position paper EU Stratospheric Layer + lobbying Bruxelles via Italia/Francia/Germania + Italy HAPS White Paper.

### 11.9.3 Tech batterie LiS/SS densità ≥ 350 Wh/kg pack entro 2028

**Dipendenza**: disponibilità commerciale di celle Li-S (Lithium-Sulfur) o Solid-State con densità a livello **pacchetto** ≥ 350 Wh/kg entro Y3-Y4 (2028-2029), per chiudere l'energy balance HALE inverno a 44°N (Cap. 6).
**Stato attuale (M+0, maggio 2026)**: celle Li-ion best-in-class ~260-280 Wh/kg pack (Tesla/CATL). Li-S a livello cella laboratorio 400-600 Wh/kg, ma pack solo 250-300 Wh/kg (degradazione). Solid-State QuantumScape / Solid Power: TRL 5-6, scale-up 2027-2030.
**Trigger osservabile**: annunci commerciali celle Li-S / SS densità pacchetto ≥ 350 Wh/kg con qualifica aerospace entro 2028.
**Falsifying observation**: se al M+48 (2030) non esistono celle qualificate aerospace ≥ 350 Wh/kg pack, l'energy balance HALE inverno deve essere chiuso con: (i) espansione wing area + (ii) migrazione latitudine operativa a < 42°N + (iii) accettazione endurance ridotto.
**Mitigazione**: partnership early-access con ACC (FR-DE-IT) + Italvolt + Northvolt + Solid Power; design HALE modulare per accettare upgrade celle.

### 11.9.4 Partnership CIRA + Leonardo/TAS (cooperazione vs antagonismo)

**Dipendenza**: cooperazione (non antagonismo) di Leonardo / Thales Alenia Space / CIRA fino almeno alla Fase 3 (M+72).
**Stato attuale (M+0)**: relazioni informali CIRA + POLITO; nessuna posizione ufficiale Leonardo / TAS su Firmamento.
**Trigger osservabile**: approcci informali Leonardo / TAS per JV o investment (RSK-GEO-005 trigger).
**Falsifying observation**: se Leonardo/TAS attivano lobbying contrario a Firmamento in bandi MIMIT o EU oltre M+24, la roadmap deve essere riconfigurata su "no-incumbent-cooperation scenario" (più costoso, più lento).
**Mitigazione**: vedi `RESERVED-rischi-geopolitici.md` RSK-GEO-005. Capital structure resistente + cooperazione progetto-specifica senza equity stake + speed di esecuzione.

### 11.9.5 Stabilità geopolitica EU-US

**Dipendenza**: quadro geopolitico EU-US stabile o pro-sovranità europea che consenta (i) supply chain robusta + (ii) consorzio EU sovereign aperto a finanziamento Commissione.
**Stato attuale (M+0, maggio 2026)**: tensioni USA-Cina (tariffe 2025+), guerra Ucraina ongoing, segnali pro-sovranità EU (IRIS², EU Strategic Autonomy, Critical Raw Materials Act, Net Zero Industry Act).
**Trigger osservabile**: communiqué USA contro programmi HAPS EU; restrizioni export US componenti HAPS; pressioni NATO contro asset HAPS EU.
**Falsifying observation**: se entro Y4-Y6 cambia drasticamente il quadro (es. ritorno protezionismo US **e** tensioni interne EU che bloccano consorzio sovrano), la Fase 5 non è realizzabile. La roadmap si ferma a "scala italiana standalone".
**Mitigazione**: vedi `RESERVED-rischi-geopolitici.md` RSK-GEO-001/003. Linguaggio "complementare IRIS²", non "alternativa Starlink"; supply chain diversificazione EU; dialogue Atlantico via MIMIT/ambasciata.

---

## 11.10 Red Team Check — Adversarial Review

Critica condotta dagli agenti `sovereign-infrastructure-strategist` + `business-model-strategist` + `financial-cfo-analyst`. Sintesi:

### Critica 1 (sovereign-infrastructure-strategist) — "La Fase 5 è una favola: nessun programma EU sovereign HAPS è in vista al 2026"

**Razionale critica**: l'intera Fase 5 dipende da un programma EU equivalente IRIS² su HAPS che oggi (M+0, maggio 2026) **non esiste** né come roadmap né come consultation EU. Posizionare la Fase 5 come "obiettivo concreto" è disonesto.
**Risposta**: confermato. La Fase 5 è **dichiarata speculative** (§11.1.2 confidence speculative). È mantenuta come **vettore strategico** (boundary condition B2 dichiarata) e non come piano operativo approvato. Il `Cap. 11` dichiara esplicitamente (§11.6.4) la dipendenza da programma EU multi-miliardario, e la falsifying observation: se al Y4-Y5 il programma non esiste, lo scenario "Large fleet" è strutturalmente non finanziabile e la roadmap va ridimensionata. **Mitigazione**: la roadmap è documento vivente; ogni gate ridiscute la fattibilità della fase successiva.

### Critica 2 (business-model-strategist) — "Lo Studio approva Fase 1, ma il capitolo descrive 10 anni di roadmap. Non c'è discrepanza?"

**Razionale critica**: lo Studio di Fattibilità è un documento di **approvazione decisionale**. Approva un percorso e ne deferisce un altro. Il Cap. 11 descrive 5 fasi su 10 anni, dando ai lettori (Coopfond, Regione, investitori) l'impressione di un piano operativo committed.
**Risposta**: confermato e affrontato esplicitamente. §11.1.1 e §11.1.2 distinguono nettamente: **lo Studio approva Fase 1 + preparazione Fase 3**; la **roadmap descrive ma non approva** le Fasi 2-5. Ogni fase ha confidence dichiarato (high/medium/low/speculative) e gate decisionale che la abilita o blocca. La roadmap è **vettore strategico**, non commitment di capitale. Documenti di approvazione capitale (Cap. 8 Piano Economico-Finanziario, Cap. 10 Raccomandazione) coprono solo Y1-Y3 + preparazione Phase B 6B.

### Critica 3 (financial-cfo-analyst) — "Capital intensity €500M-2B small fleet vs €10-30B full scale: è troppo onesto per essere narrativamente vendibile"

**Razionale critica**: dichiarare nel capitolo che la Fase 5 richiede €10-30B (a fronte di una company seed Y1 a €0.7-1.2M) è **catastrofico per la narrativa** verso investitori VC. Nessun investitore VC accetta che il "full success scenario" richieda €30B + intervento sovrano EU.
**Risposta**: il rigore epistemico (Regola 7 base-rate, vedi `epistemic-rigor` skill) **richiede onestà**. La cifra €10-30B EU sovereign full scale è dichiarata in `riferimenti/visione-10-anni.md` §4 e ripresa qui. **Mitigazione narrativa**: il capitolo è strutturato per **investitori VC** sulle Fasi 1-3 (Series Seed → A → B, €0.5-30M cumulato, scala "business as usual" venture). La Fase 4 introduce **sovereign investors** (CDP, EIB, EIC Fund). La Fase 5 introduce **EU institutional funding** (programma equivalente IRIS²) come **precondizione esterna**, non come "round Series F privato". Questa **stratificazione di tipi di capitale per fase** è onesta e narrativamente difendibile.

### Critica 4 (sovereign-infrastructure-strategist) — "Linguaggio 'complementare IRIS²' è bello, ma il rischio frizione USA è reale a partire da Fase 3"

**Razionale critica**: per quanto Firmamento eviti pubblicamente il framing "alternativa Starlink", una piattaforma stratosferica italiana operativa **a partire dalla Fase 3** sarà letta da Washington come "EU sovereign challenge", indipendentemente dal nostro linguaggio. Il rischio frizione USA inizia non a Y8 (Fase 5) ma a Y4-Y5 (Fase 3-4).
**Risposta**: confermato. Vedi `RESERVED-rischi-geopolitici.md` RSK-GEO-001: probabilità M, impatto M-H, fase critica Y4+. Mitigazione strategica: dialogue Atlantico via NATO DIANA + supply chain diversificazione EU + posizionamento pubblico come "partner USA in dual-use" (non concorrente). Il documento Cap. 11 mantiene il linguaggio "complementare IRIS²" come **disciplina pubblica obbligatoria** (boundary), il documento riservato copre la dimensione realistica.

### Critica 5 (business-model-strategist) — "La transizione Fase 1 (€200k ARR Y1) → Fase 4 (€30-80M ARR Y8) è 100-400× in 7 anni. È inverosimile"

**Razionale critica**: scaling 100-400× in 7 anni è da unicorn tech, non da operatore di infrastrutture aerospaziali. Base rate aerospace startup: ~10% raggiunge €10M ARR in 7 anni; lt 1% raggiunge €30M+ ARR in 7 anni. Vedi epistemic-rigor Regola 7 base-rate.
**Risposta**: confermato e dichiarato confidence **low** per Fase 4 e **speculative** per Fase 5 (§11.1.2). La Fase 4 ARR €30-80M è il **target di visione** (boundary B2); il **scenario di consolidamento standalone** (no Fase 4-5 EU sovereign) prevede Y8 ARR €10-30M, più realistico. La roadmap **non è promessa** di scaling 100-400× — è un vettore strategico che ammette scenari di scala alternativi (`visione-10-anni.md` §4: small fleet vs medium fleet vs large fleet).

### Critica 6 (financial-cfo-analyst) — "Capital structure resistente fino M+72 + founder maggioranza è incompatibile con Series A-B-C necessari"

**Razionale critica**: il vincolo "founder ≥ 51% voting fino M+72" più il capital plan Series A €3-8M (M+36) + Series B €10-30M (M+60) + Series C €30-100M (M+96) implica diluizione che porta il founder team **sotto 51%** verso la Fase 3-4, salvo strutture di golden share o dual-class shares.
**Risposta**: confermato. La capital structure resistente richiede **strumenti tecnici specifici**: (i) **dual-class shares** (Class B voting maggioritaria al founder) prima del Series A, (ii) **golden share italiana** (preview Golden Power), (iii) **CDP / EIB / EIC Fund** come anchor investor non ostili. Implementazione **prima del primo round estero** (M+18-24). Engagement preventivo con Dipartimento Coordinamento Politiche Economiche (Presidenza Consiglio) è critico. Vedi `RESERVED-rischi-geopolitici.md` RSK-GEO-002 + RSK-GEO-005.

---

**Verdetto Red Team finale**: il Cap. 11 è **strutturalmente solido** e **epistemicamente onesto** nel distinguere ciò che lo Studio approva da ciò che la roadmap descrive. Le **6 azioni richieste** prima del gate M+10:

- [ ] Dichiarare esplicitamente in Cap. 10 (Raccomandazione) che la roadmap Cap. 11 **non è oggetto di approvazione** ma di **descrizione strategica**
- [ ] Aggiornare `riferimenti/visione-10-anni.md` con aggiornamenti dei trigger esterni (es. roadmap CE 2030+) ogni 6 mesi
- [ ] Engagement preventivo Dipartimento Coordinamento Politiche Economiche (Presidenza Consiglio) entro M+18 per Golden Power preview
- [ ] Setup dual-class shares + golden share italiana prima del Series A (M+24)
- [ ] Position paper "Italian Stratospheric Sovereignty" pubblicato entro M+12-18 (consolidamento Fase 1) come prima esposizione pubblica della visione
- [ ] Decisione esplicita su engagement TAS-Leonardo / Airbus: timing + perimetro + line-in-the-sand su equity diretto

---

## 11.11 Open Questions

| OQ-ID | Domanda aperta | Owner | Target di chiusura |
|---|---|---|---|
| OQ-F11-001 | Roadmap CE 2030+ pubblicata? Programma EU sovereign HAPS aperto? | sovereign-infrastructure-strategist | Monitor trimestrale; primo check Y4 (M+48) |
| OQ-F11-002 | EASA RMT Special Condition HAPS aperto formalmente? | regulatory counsel | M+24-36 |
| OQ-F11-003 | TRL batterie Li-S / SS aerospace ≥ 350 Wh/kg pack disponibili? | CTO + supply chain | M+36-48 |
| OQ-F11-004 | Posizione ufficiale TAS-Leonardo su Firmamento (cooperazione vs antagonismo)? | CEO + sovereign strategist | M+12-24 (approcci informali attesi) |
| OQ-F11-005 | Quadro geopolitico EU-US stabile? Pro-sovranità EU consolidata? | sovereign strategist | Monitor continuo |
| OQ-F11-006 | CDP Venture Capital + EIC + EIB disponibili come anchor non ostili? | CFO | M+18-24 |
| OQ-F11-007 | Capital structure dual-class shares + golden share preparata? | Legal counsel | M+18-24 (pre-Series A) |
| OQ-F11-008 | Scenario "EU sovereign full scale €10-30B" realizzabile, ridimensionato o abbandonato? | CEO + sovereign + CFO | Decisione M+48-60 (gate Fase 3) |
| OQ-F11-009 | Exit strategy preferita (IPO / sovereign consolidation / strategic) confermata? | Board | Gate M+96 (entrata Fase 5) |
| OQ-F11-010 | Posizionamento Firmamento in IRIS² consortium (DG CNECT / DEFIS) formalizzato? | sovereign strategist | M+24-48 |
| OQ-F11-011 | Trigger §11.6bis.2 attivati: scenario B2-relaxed attivato come traiettoria di default? | CEO + CFO + sovereign | Decisione M+72-84 (post gate Fase 4 conditional) |
| OQ-F11-012 | Modello finanziario Cap. 8 + pricing Cap. 7 aggiornati con scenario B2-relaxed come caso base operativo Y6-Y10? | CFO | M+9 (pre-gate Studio M+10) |

---

## 11.12 Riferimenti

[^1]: ENAC, "Roadmap AAM 2021-2030" — Allegato 1 al Piano Strategico Nazionale Advanced Air Mobility. Source: `fonti/02_AAM-Italian-Ecosystem-–-Project-overview-and-Roadmap_web-1.md`. **Confidence: high** (ENAC, fonte istituzionale italiana). Riferimento metodologico per struttura roadmap aerospaziale italiana (3 waves "Fix the basics" → "Prepare for ambition" → "Realize ambition", AML1 → AML2 → AML3 2023-2026-2030).

[^2]: ENAC, "Business Plan AAM (2021-2030)" — Allegato 2 al Piano Strategico Nazionale AAM. Source: `fonti/03_AAM-Business-Plan_web-1.md`. **Confidence: high**. Riferimento metodologico per ripartizione investimenti per wave, scouting finanziamenti.

[^3]: NASA SE Handbook Rev 2 (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. **Confidence: high**. Riferimenti metodologici: §6.7 Phase B-F lifecycle, §6.8 Decision Analysis, §6.4 Risk Management.

[^4]: `riferimenti/visione-10-anni.md` — documento di posizionamento strategico vivente. **Confidence: high** sulla narrativa, **variable** sui numeri (high per Y1-Y3, medium-low per Y4-Y7, speculative per Y8-Y10).

[^5]: `riferimenti/RESERVED-rischi-geopolitici.md` — documento riservato (ad accesso ristretto). Contiene il dettaglio dei 5 rischi geopolitici (RSK-GEO-001/005) richiamati discretamente nel presente capitolo.

[^6]: D.Lgs. 31 marzo 2023, n. 36 — Codice dei contratti pubblici. Source: `fonti/2023_0036.md`. **Confidence: high**. Conformità formale: art. 41 (PFTE) + Allegato I.7 (struttura sezioni).

[^7]: Cap. 3 — Requisiti e RTM. `studio-di-fattibilita/cap-03-requisiti-e-RTM.md`. Riferimento per StNeeds, SyR, Gate M+10 criteri.

[^8]: Cap. 5 — Quadro Normativo. `studio-di-fattibilita/cap-05-quadro-normativo.md`. Riferimento per framework EASA UAS / HAPS, RSK-REG-001/002, engagement plan.

[^9]: Cap. 6 — Analisi Tecnica di Fattibilità (in fase di redazione). Riferimento per FMECA/FTA, energy balance, RSK-TEC-001/002.

[^10]: Cap. 7 — Mercato + Business Case. `studio-di-fattibilita/cap-07-mercato-e-business-case.md`. Riferimento per BMC, VPC, segmentazione domanda, pricing, scale-up roadmap.

[^11]: Cap. 8 — Piano Economico-Finanziario (in fase di redazione). Riferimento per CapEx, OpEx, NPV, IRR, payback, mix finanziamenti.

[^12]: Cap. 9 — Cronoprogramma + Gate decisionali (in fase di redazione). Riferimento per Gantt detailed Y1-Y3, milestone tracking.

[^13]: Cap. 10 — Raccomandazione di Gate (in fase di redazione). Verdetto Go/Hold/No-Go gate M+10/M+11.

[^14]: 3GPP TR 38.811 / TR 38.821 (Release 16-18 NTN), Source: `fonti/38811.md`, `fonti/3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md`. **Confidence: high**. Riferimento tecnico per servizi NTN 5G Fase 4.

[^15]: Skill `gate-review-checklist` (`/.claude/skills/gate-review-checklist/SKILL.md`); skill `feasibility-study-framework` (`/.claude/skills/feasibility-study-framework/SKILL.md`); skill `epistemic-rigor` (`/.claude/skills/epistemic-rigor/SKILL.md`); skill `risk-register-builder` (`/.claude/skills/risk-register-builder/SKILL.md`); agenti `sovereign-infrastructure-strategist`, `business-model-strategist`, `financial-cfo-analyst`.

[^16]: AALTO HAPS Ltd (Airbus subsidiary) Zephyr 8/S — benchmark Tier 1 globale HAPS. Vedi Cap. 7 §7.4.1.

[^17]: BAE Systems / Prismatic PHASA-35 — benchmark Tier 1 UK. Vedi Cap. 7 §7.4.1.

[^18]: EuroHAPS programme (TAS coordinator, €43M EDF) — consortium EU di riferimento. Vedi Cap. 7 §7.4.2.

[^19]: IRIS² (EU sovereign satcom €10.6B) — Programma sovrano EU di riferimento. Vedi Cap. 7 §7.4.3 e Cap. 5.

[^20]: Briefing iniziale progetto: `da revisionare/Briefing_ Progetto Piattaforma Aerea per le Aree Interne.md`. Verdetto preliminare Percorso 6A GO Condizionato + Percorso 6B HOLD / Go Condizionato Estremo, coerente con presente capitolo.

[^21]: `studio-di-fattibilita/AUDIT-QUALITY-VOLUME-1.md` — audit di qualità consolidato Volume 1 (sintesi 4 sorgenti audit: rigore epistemico, Red Team, competitor, regulatory). §2 Cap. 11 raccomanda esplicitamente l'aggiunta di scenario B2-relaxed "operatore IT standalone €30-80M ARR Y10, no consorzio EU" che il presente §11.6bis recepisce. **Confidence: high** (audit interno multi-fonte). Vedi anche §10 raccomandazioni pre-gate G3.

[^22]: AIAD (Federazione Aziende Italiane per l'Aerospazio, Difesa e Sicurezza) — dati di settore aerospazio italiano. Ricavi medi aerospace IT 2023-2024 + priorità politica industriale 2025-2030 (campioni italiani). **Confidence: medium** (dati di settore associativi, da triangulare con MIMIT + ISTAT R&D aerospace per Volume 2). Riferimento per benchmark scala B2-relaxed "operatore IT specializzato di riferimento" §11.6bis.3.

[^23]: Eurospace — European Space Industry Association, "Facts & Figures" annual report. Dati comparativi industria spazio EU vs USA, capital intensity programmi sovrani EU. **Confidence: medium-high** (associazione settore EU consolidata). Riferimento per benchmark capital intensity scenario B2 full vs B2-relaxed §11.6bis.5.

[^24]: CDP (Cassa Depositi e Prestiti) — investimenti aerospazio italiano via CDP Venture / Fondo Italiano Aerospazio. Pubblicazioni 2024-2025 su politica investimento sovereign IT in aerospazio. **Confidence: medium** (pubblicazioni istituzionali parziali; dettaglio per Volume 2). Riferimento per anchor investor scenario B2-relaxed §11.6bis.3.

---

## 11.13 Note di chiusura del capitolo

Il Cap. 11 è **bozza M+3** della Roadmap Post-Fattibilità (rev. **M+3.1** post-integrazione §11.6bis Scenario B2-relaxed da raccomandazione audit). È coerente con:

- `riferimenti/visione-10-anni.md` (5 fasi temporali, ARR target, capital intensity, dipendenze esterne, boundary conditions B1/B2)
- Cap. 3 (criteri gate M+10/M+11)
- Cap. 5 (framework regolatorio EASA/ENAC e RSK-REG-001/002)
- Cap. 7 (segmentazione, MVP, scale-up roadmap §7.10)
- ENAC AAM Roadmap 2021-2030 (struttura metodologica 3 waves)
- NASA SE Handbook §6.7 Phase B-F lifecycle
- `studio-di-fattibilita/AUDIT-QUALITY-VOLUME-1.md` §2 e §10 (recepimento raccomandazione "aggiungi scenario B2-relaxed Cap. 11" via §11.6bis)

**Debolezze principali dichiarate onestamente:**

1. **Confidence speculative** sulle Fasi 4-5 (M+72-120): dipendenze esterne strutturali (EASA framework, programma EU sovereign, geopolitica) che non sono sotto controllo Firmamento
2. **Capital intensity Y8-Y10 onesta**: il range €10-30B per scala "EU sovereign full scale" è dichiarato apertamente — non nascosto né diluito
3. **Showstopper noti** dichiarati per ogni fase con falsifying observations verificabili
4. **Linguaggio pubblico vincolato**: "complementare IRIS²", **mai** "alternativa Starlink" — disciplina obbligatoria coerente con `RESERVED-rischi-geopolitici.md` RSK-GEO-001
5. **Boundary conditions B1+B2 preservate**: service-only + cooperative Legacoop in tutte le fasi; obiettivo EU sovereign mantenuto come vettore strategico indipendentemente dalla magnitudine finanziaria
6. **Scenario B2-relaxed esplicitato (§11.6bis)**: riconoscimento onesto che la traiettoria Y10 più probabile (oltre acquisizione difensiva e dissoluzione) è "Standalone IT Operator Small Fleet" con ARR €30-80M, non Fase 5 full €100-500M. B2 full diventa option upside; B2-relaxed è caso base operativo gestibile.

**Falsifying observations chiave del Cap. 11** (in coerenza con la skill `epistemic-rigor` Regola 1):

- **FO-F11-01**: se al M+12 ARR Y1 < €200k → MVP fail → Pivot del modello, roadmap riconfigurata
- **FO-F11-02**: se al M+36 TRL HALE subscale < 5 → Fase 3 deferita o cancellata, roadmap deenergizzata su HALE
- **FO-F11-03**: se al M+48 energy balance HALE inverno margine < 20% → showstopper RSK-TEC-001 attivato, redesign obbligatorio
- **FO-F11-04**: se al M+60 EASA Special Condition HAPS non adopted → Fase 4 commerciale bloccata, roadmap "demonstrative only"
- **FO-F11-05**: se al M+48 programma EU sovereign HAPS (analog IRIS²) non aperto → scenario "EU sovereign full scale" non finanziabile, Fase 5 ridimensionata a "small fleet"
- **FO-F11-06**: se Leonardo/TAS attivano acquisizione difensiva pre-M+72 → traiettoria indipendente compromessa, decisione "merge or exit" obbligatoria
- **FO-F11-07 (§11.6bis)**: se al M+72 Firmamento è single-player IT con ARR < €15M e zero traction in consortium EU formale → scenario B2-relaxed è traiettoria operativa di default; B2 full diventa blue sky aspiration
- **FO-F11-08 (§11.6bis)**: se al M+96 ARR Y8 < €15M e flotta HAPS perennial < 3 operative → scenario B2-relaxed stesso in difficoltà; convergenza verso operatore VTOL/MALE service-only IT specializzato (strategic pivot da deliberare)

**Prossimi step richiesti** (in ordine di criticità):

1. Aggiornamento Cap. 11 dopo gate M+12 (verdetto MVP Y1)
2. Position paper "Italian Stratospheric Sovereignty" pubblicato entro M+12-18 — framing **"Standalone IT operator + future option EU consortium"** (vedi §11.6bis.7)
3. Setup capital structure dual-class + golden share entro M+24 (pre-Series A)
4. Engagement preventivo Dipartimento Coordinamento Politiche Economiche entro M+18
5. Decisione esplicita TAS-Leonardo cooperation framework entro M+24-36
6. Monitoring trimestrale dipendenze esterne (§11.9) **+ trigger §11.6bis.2 (TRG-B2R-01/06)** con report a Board
7. Aggiornamento Cap. 7 (pricing) + Cap. 8 (modello finanziario) per integrare **scenario B2-relaxed come caso base operativo Y6-Y10** entro M+9 (pre-gate Studio M+10)

**Versionamento Cap. 11**:
- v0.5 (M+3, baseline): coerente con visione 10 anni + tutti i capitoli redatti (Cap. 3, 5, 7)
- v0.5.1 (M+3, presente revisione): integrazione §11.6bis Scenario B2-relaxed "Standalone IT Operator Small Fleet" da raccomandazione `AUDIT-QUALITY-VOLUME-1.md` §2 Cap. 11; aggiornamento §11.0 Sintesi, §11.1.3 Relazione con visione, §11.11 OQ-F11-011/012, §11.13 closing notes con FO-F11-07/08 nuove
- v0.7 (M+6): post-engagement DG CNECT/DEFIS + EASA + Bruxelles
- v0.9 (M+9): post-LoI Regione + ratificazione boundary conditions
- v1.0 (M+10): congelato per gate Studio Fattibilità
- aggiornamenti successivi: post ogni gate (M+12, M+24, M+36, etc.)

Il capitolo è chiuso al M+3 con verdetto Red Team **OK con 6 action items** + integrazione M+3.1 dello scenario B2-relaxed che recepisce raccomandazione audit di qualità.

---

> **Disclaimer epistemico finale**: la roadmap presentata in questo capitolo è **vettore strategico onesto**, non promessa di esecuzione lineare. La probabilità che il vettore venga eseguito esattamente come descritto (Fase 5 full "EU sovereign consorzio") è **bassa (6-15%)** (base rate aerospace startup: ~10% per Y8 ARR €10M+; vedi §11.6bis.6 per distribuzione probabilità degli esiti Y10). La probabilità che venga eseguito **almeno fino a Fase 2-3** con esito commerciale è realistica con esecuzione disciplinata. **Lo scenario B2-relaxed "Standalone IT Operator" (§11.6bis) è esito di successo dimensionato a probabilità 30-50%** — non fallimento, ma stabilizzazione operativa coerente con boundary B1+B2 a scala IT. Le decisioni del gate M+10/M+11 riguardano **solo Fase 1 + preparazione Fase 3** — il resto è coerenza vettoriale, non commitment.
