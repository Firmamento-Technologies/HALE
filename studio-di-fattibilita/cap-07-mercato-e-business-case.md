# Capitolo 7 — Analisi di Mercato e Business Case

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 1, Capitolo 7
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (sezione "Analisi di mercato e business case")
> **Template di riferimento italiano:** ENAC AAM Business Plan 2021-2030 [^1], MIMIT Progetto Aeronautico Marocco [^2], Aeropolis Workshop "Analisi dei Costi e Business Plan" 2014 [^3]
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** `competitor-intelligence` + `business-model-strategist` — vedi §7.13

---

## 7.0 Sintesi del capitolo

Il presente capitolo presenta l'**analisi di mercato e il business case** per i due percorsi del progetto HALE/VTOL Firmamento Technologies, in conformità alla struttura italiana ufficiale-like (art. 41 D.Lgs. 36/2023 + ENAC AAM Business Plan template + MIMIT prefattibilità).

**Tesi del capitolo, in sintesi:**

1. **Esiste un mercato indirizzabile reale** per servizi persistenti EO + NTN nelle Aree Interne italiane, ancorato da committenti PA (Regione Liguria, Protezione Civile) + rete cooperative Legacoop (10 cooperative pilota). Stima TAM-IT addressable Y5 (2030) per la categoria HAPS + UAV servizi territoriali: **€40-180M** (range a confidence low-medium).
2. **Firmamento si posiziona come operatore di servizi**, non OEM aeronautico (boundary condition B1). Il modello di revenue è ricorrente (canoni, DaaS, ore-volo + analytics, outcome-based), non transattivo. **Nessun ricavo da vendita di velivoli** previsto né nel pilota né nello scale-up.
3. **Vantaggio competitivo difendibile** poggia su 4 pilastri: (i) specializzazione geografica Aree Interne IT, (ii) modello cooperativo, (iii) sostenibilità + narrativa ESG, (iv) approccio incrementale VTOL → MALE → HALE che produce asset riusabili. **Nota di onestà post-audit competitor**: il pilastro (i) è difendibile vs Tier 1 globali (AALTO/Skydweller) **ma NON vs Cluster D italiani** (e-GEOS, Planetek, NHazca, FlyingBasket) che presidiano già il mercato B2G regionale (vedi §7.4.4 e §7.5.1).
4. **MVP Y1 (Percorso 6A Pentema)**: budget €700-1100k, **target revenue Y1 €260k centrale (range €220-300k, min €200k SyR-Cost-003)** da 5 contratti pluriennali con PA + cooperative, pricing **RECALIBRATED post-Cluster D audit M+3** (vs originale €355-405k FALSIFICATO). Sostenibilità break-even Y4-Y5 dopo scale-up SNAI Liguria (vs Y3-Y4 originale). **Pricing baseline RECALIBRATED**: €60-90k/anno EO PA base + €25-40k premium persistence/sovranità (vs €150k/anno originale falsificato). Il margine difensivo passa per persistence sub-day + latency <1 s + sovranità dati IT, NON per pricing (vedi §7.4.5 + §7.8.2).
5. **Fase 2-5 della visione 10 anni**: traiettoria progressiva verso "nodo italiano di un futuro consorzio sovrano europeo HAPS" (boundary condition B2), con capital intensity totale stimata **€500M-€2B** per piccola flotta (5-10 HAPS) o **€10-30B** per scala "EU sovereign layer" (vedi `riferimenti/visione-10-anni.md`).

**Verdetto business per il gate M+10**: **GO Percorso 6A** (MVP commerciale validabile in 12 mesi); **GO CONDIZIONATO Percorso 6B** (preparatorio R&D, no commitment a manufacturing né operations commerciali fino al gate M+24).

---

## 7.0bis Boundary conditions del progetto

In coerenza con Cap. 5.0bis e Cap. 3.0bis, il presente capitolo rispetta:

- **B1 — Modello service-only + cooperative Legacoop**: Firmamento NON vende velivoli. Tutto il revenue è ricorrente da erogazione di servizi (DaaS, IaaS, canone, outcome-based, ore-volo + analytics). Rete cooperative Legacoop è scelta strutturale, NON ipotesi di vantaggio competitivo da validare.
- **B2 — Obiettivo strategico "nodo IT di EU sovereign stratospheric layer"**: orizzonte 10 anni, posizionamento progressivo verso un consorzio europeo (vedi `riferimenti/visione-10-anni.md`). Lo Studio approva i passi 1-2 (Y1-Y3); la visione completa è vettore strategico.

Linguaggio pubblico raccomandato (vedi `riferimenti/RESERVED-rischi-geopolitici.md`): "complementare a IRIS²", **mai** "alternativa europea a Starlink" in documenti pubblici/bandi/stampa.

---

## 7.1 Metodologia di Analisi e Riferimenti

### 7.1.1 Struttura del capitolo

Il capitolo è costruito ibridando tre template italiani autoritativi:

| Template | Struttura adottata | Fonte |
|---|---|---|
| **ENAC AAM Business Plan 2021-2030** | Wave di investimento + ripartizione tra aree (vettori + infrastrutture) + scouting finanziamenti pubblici/privati | `fonti/03_AAM-Business-Plan_web-1.md` |
| **MIMIT Progetto Aeronautico Marocco (2008)** | Genesi → mercato → piano industriale → strumenti finanziari → risultati economico-finanziari → considerazioni finali | `fonti/Progetto_Marocco.md` |
| **Aeropolis "Analisi Costi e Business Plan" (2014)** | Approccio metodologico costing aerospace + benchmark Alenia | `fonti/AnalisiCostiBusinessPlan24_05_14.md` |

### 7.1.2 Confidence aggregato e disciplina epistemica

In conformità alla skill `epistemic-rigor`, dichiaro fin dall'apertura del capitolo:

- **Confidence aggregato medio**: **low-medium** (alcune stime di mercato sono fonti commerciali single-source, vedi §7.4)
- **Triangulation status**: parziale (vedi `riferimenti/audit-rigore-epistemico.md` DR-007, DR-012)
- **Base rate aerospace** (Regola 7): la base rate di successo per startup aerospace service-based che raggiungono revenue operativo stabile è **10-20%**; Firmamento parte da questa base rate, NON da "tutti i piani business funzionano"
- **Lista programmi HALE solari falliti** (survivor bias avoidance): NASA Helios (crashed 2003), Aalto HAWK30 (cancellato 2020), Solara 50 / Titan Aerospace (dissolto 2017), Sanswire StratXX (mai operativo)

### 7.1.3 Allineamento con i SyR Cost (Cap. 3)

Il presente capitolo deriva i propri claim dai requisiti Cost-* del Cap. 3, in particolare:

| Requirement Cap. 3 | Implicazione Cap. 7 |
|---|---|
| SyR-Cost-001 (CapEx 6A Y1 ≤ €1.2M) | Vincolo CapEx (Cap. 8 dettaglio) |
| SyR-Cost-002 (OpEx run-rate Y2 ≤ €450k) | Modello pricing deve coprire OpEx con margine |
| **SyR-Cost-003 (Revenue Y1 ≥ €200k)** | **Soglia critica MVP, falsifying observation Cap. 3.5.7** |
| SyR-Cost-004 (Modello service-only) | Boundary condition B1 strutturale |

---

## 7.2 Segmentazione della Domanda

### 7.2.1 Tre canali distributivi: B2G, B2B, B2B2C

Il mercato target di Firmamento Technologies è multisegmento, con prevalenza B2G (Business-to-Government) come anchor channel del MVP Y1 e progressiva diversificazione verso B2B (cooperative + utility + telco) nelle fasi successive.

| Canale | Soggetto pagante | Modalità appalto / contratto | Quota target Y3 ARR | Esempi clienti |
|---|---|---|---|---|
| **B2G centrale** | MIT, MIMIT, Difesa, ENAC | Bandi PNRR, EDF, Horizon, gare aperte D.Lgs. 36/2023 | 20-30% | MIMIT Direzione Aerospazio (programmi R&D); Difesa (dual-use civile) |
| **B2G regionale** | Regione Liguria + altre regioni SNAI | Accordi quadro, contratti pluriennali, project financing | **40-50% (anchor)** | Regione Liguria + altre regioni con aree SNAI (Piemonte, Marche, Calabria, Basilicata) |
| **B2G locale** | Protezione Civile, ARPA, Comuni, Enti Parco | Convenzioni operative, gare locali | 15-25% | PC Liguria, ARPA Liguria, Comuni montani, Enti Parco Antola/Aveto |
| **B2B cooperative** | Rete Legacoop (10 coop pilota + scale-up) | Contratti di rete, abbonamenti DaaS | 5-15% | 10 cooperative pilota (capofila Fabrica); espansione a coop agricole, forestali, comunità |
| **B2B utility (futuro)** | Enel, Snam, Open Fiber, RFI | Contratti pluriennali, ispezione infrastrutture | 0-5% Y3, 10-20% Y5 | Solo dopo certificazione SAIL stabile |
| **B2B telco (futuro 6B)** | TIM, Vodafone, Iliad, WindTre | Wholesale capacity, white-label NTN | 0% Y3, 15-30% Y7+ | Solo con HAPS operativo + licensing AGCOM |
| **B2C** | Privati cittadini, agriturismo | (eventualmente via cooperativa) | Trascurabile fino Y10 | Non target diretto |

> **Falsifying observation §7.2.1**: se al Y2 il canale B2G regionale non genera ≥ 30% dell'ARR (anchor fallita), il modello di business va profondamente ripensato (es. shift verso B2G nazionale o B2B aggressivo). **Probabilità: M, impatto: H**. Mitigazione: LoI Regione Liguria entro M+6 (Open Question OQ-010, Cap. 3.10).

### 7.2.2 Casi d'uso e prioritizzazione

I casi d'uso del progetto sono ereditati dai 17 StNeeds (Cap. 3.3.2). Ne riportiamo la **prioritizzazione**:

| Use Case ID | Descrizione | Stakeholder primario | Priorità MVP Y1 | Willingness-to-pay stimata |
|---|---|---|---|---|
| UC-001 | Monitoraggio frane + dissesto idrogeologico | Regione Liguria, PC, ARPA | **Alta** | €100-300k/anno per regione |
| UC-002 | Antincendio boschivo (early detection + monitoring) | PC, VVF, CC Forestali, Enti Parco | **Alta** | €50-200k/stagione |
| UC-003 | Connettività di emergenza | PC, Comune, Comunità | Media-alta | €30-150k/anno (canone) o on-demand |
| UC-004 | Mapping infrastrutture rurali (strade, ponti, dissesto) | Comuni, Regione, ANAS, RFI | Media | €30-150k/anno per area |
| UC-005 | Agricoltura di precisione (NDVI, NDRE) | Cooperative agricole | **Media (anchor cooperative)** | €5-50k/anno per cooperativa |
| UC-006 | Supporto SAR (ricerca persone disperse) | PC, CC Forestali | Bassa-media (on-demand) | €5-30k/event |
| UC-007 | Vigilanza ambientale Parchi Naturali | Enti Parco | Bassa-media | €20-80k/anno |
| UC-008 | Telemedicina rurale + e-government via NTN | ASL3, Comuni, Comunità | Bassa-media | €10-40k/anno per area |
| UC-009 | NTN backhaul rurale (long-term, post-Fase 3) | Telco wholesale | n/a Y1, alto Y6+ | €/Mbps wholesale |
| UC-010 | Dual-use civile-difesa ISR | Difesa, NATO DIANA | n/a Y1, condizionato | €/contratto governativo |

**Use case prioritari per MVP Y1**: UC-001, UC-002, UC-003 + 1-2 minori (UC-005 cooperative agricole, UC-007 Enti Parco) per validare diversificazione.

> **Confidence prioritizzazione: medium** (basata su (i) analisi documentazione SNAI Liguria, (ii) workshop preliminare cooperative M+0-3 in corso, (iii) protocolli operativi PC/VVF). Validazione richiesta via workshop strutturati cooperative + PC entro M+6 (Open Question OQ-011).

---

## 7.3 Analisi di Mercato

### 7.3.1 Mercato globale HAPS + UAV territoriali

**⚠️ Caveat epistemico** (Regola 2 + 3 della skill `epistemic-rigor`, vedi `riferimenti/audit-rigore-epistemico.md` CLAIM-001):

I numeri di mercato HAPS in circolazione provengono **principalmente da report commerciali** (MarkNtel, Grand View, Coherent Market Insights). Sono **fonti singole non triangolate** con dati ufficiali (Eurostat, ITU, EUSPA, AIAD, Eurospace). I numeri **includono con ogni probabilità anche investimenti R&D pubblici** (es. EuroHAPS €43M EDF, Zephyr Airbus capex), **non solo revenue ricorrente di servizio**. Per un'analisi service-only seria sono **stima indicativa, non baseline**. Confidence: **low**.

**Mercato HAPS strict (pseudo-satelliti HALE solari)** [^4]:
- 2024: ~$99M
- 2030: ~$240M
- CAGR: 16%

**Mercato HAP wide (incl. dirigibili, palloni)** [^5]:
- 2024-2025: $1.54-1.73B
- 2030-2032: $2.66-3.10B
- CAGR: 7.4-8.4%

**Composizione**: UAV HAPS dominante con ~60% market share globale [^4].

### 7.3.2 Mercato italiano addressable — TAM-IT

**Approccio stima** (stima propria, confidence **low**):

Italia rappresenta circa il **3-5% del mercato aerospace globale** (fonti: AIAD annual reports, Aerospace Italia 2023). Applicando questo rapporto al mercato HAPS/UAV territoriali:

| Anno | TAM-IT HAPS strict | TAM-IT HAP wide | TAM-IT UAV territoriali |
|---|---|---|---|
| 2026 | $1-3M | $30-60M | $80-150M |
| 2030 | $5-12M | $40-80M | $100-200M |
| 2035 | $15-30M | $80-150M | $150-300M |

> **Confidence: low** (stima propria, no triangulation; DR-012 audit-rigore-epistemico.md). Per stima investment-grade serve **AIAD Annual Report Italian aerospace** + **Eurospace Facts & Figures**.

### 7.3.3 SAM (Serviceable Addressable Market) — Italia

Il SAM è il sottoinsieme del TAM-IT effettivamente raggiungibile dal modello di business di Firmamento (service-only, B2G+B2B, focus territoriale Aree Interne).

**Filtri applicati** rispetto al TAM:
- Solo segmenti B2G + B2B cooperative + B2B utility ridotto (escluso B2C, escluso difesa pura) → ~50-70% del TAM-IT addressable
- Solo aree con orografia/dispersione che giustificano persistenza/copertura aerea (escluse città principali) → ~40-60% del precedente
- Solo aree con disponibilità willingness-to-pay (regioni con SNAI attiva + finanziamenti FESR disponibili) → ~50-80% del precedente

| Segmento | % filtro | SAM-IT 2030 stimato |
|---|---|---|
| B2G regionale Aree Interne (10-12 regioni IT con SNAI) | 100% | €15-40M |
| B2G PC + ARPA nazionale | 60-80% del TAM PC | €8-20M |
| B2B cooperative Legacoop (>500 cooperative aderenti potenziali) | 5-10% (penetrazione realistica) | €5-15M |
| B2B utility (Enel, Snam, OF, RFI) | 5-10% del loro ispezione budget | €10-30M |
| **SAM-IT 2030 totale aggregato** | | **€40-100M** |

> **Confidence: low** — `audit-rigore-epistemico.md` DR-007 + DR-012 ancora aperti. Stima da affinare in iterazione successiva.

### 7.3.4 SOM (Serviceable Obtainable Market) — Firmamento

Il SOM è la fetta realistica di SAM che Firmamento può catturare nei prossimi 5-7 anni considerando capacità operative, competizione, lead times PA.

**Logica**:
- Firmamento ha capacità Y3 di servire ~2-4 regioni (≈ Liguria + 1-2 altre regioni SNAI) → SOM regionale ≈ 15-30% del SAM regionale
- B2B cooperative: penetrazione Y3 ≈ 20-40% delle 10 cooperative pilota + ~10-20 altre coop ≈ 5-8% del SAM cooperative
- B2B utility: Y3 ≈ 1-2 contratti pilota = 1-3% del SAM utility

| Anno | SOM Firmamento stimato | Note |
|---|---|---|
| Y1 (2026/27) MVP | **€200-400k ARR** | Anchor Regione Liguria + 2-3 cooperative pilota |
| Y2 (2027/28) scale-up Liguria | **€500k-1.2M ARR** | Espansione PC Liguria + Enti Parco + ARPA |
| Y3 (2028/29) multi-regione | **€1.5-3.5M ARR** | + 2 regioni SNAI (Piemonte/Calabria) + cooperative scale |
| Y5 (2030/31) consolidamento IT | **€3-8M ARR** | + utility pilot + servizio HAPS subscale |
| Y7+ (post-HALE operativo) | **€10-30M ARR** (potenziale, se HAPS Fase 3 va) | Scale dipendente da gate M+24 HALE |

> **Confidence: low-medium**. Falsifying observation: se Y2 ARR < €400k, il vettore scale-up è compromesso e va attivata revisione del modello.

### 7.3.5 Confronto con il template ENAC AAM BP 2021-2030

Per **calibrare** le stime sopra contro un dato ufficiale italiano, citiamo i numeri del **template ENAC AAM Business Plan 2021-2030** [^1] §3:

- **Investimenti totali ecosistema AAM Italia 2021-2030**: **€1,863.4M** (stima ENAC su 10 anni, scenario integrato)
- Ripartizione su 3 wave:
  - Wave 1 (2021-2023): €510.9M
  - Wave 2 (2024-2026): €571.4M
  - Wave 3 (2027-2030): €781.1M
- 4 aree di investimento principali, con **€923.3M per veicoli e piattaforme** (50% del totale)
- Filosofia "afferenza al sistema italiano": gli investimenti AAM beneficiano "non solo il settore della Mobilità Aerea Avanzata ma anche una serie di settori connessi" [^1, §1]

> **Implicazione per Firmamento**: il TAM-IT AAM è MOLTO più grande del TAM HAPS+UAV territoriali (€1.86B vs €100-200M); Firmamento può inserirsi come **sub-segmento dell'ecosistema AAM Italia**, ma non concorrere con i grandi attori (Leonardo, TAS, Telespazio). Il posizionamento corretto è **complementare** + **micro-specialized**.

---

## 7.4 Analisi della Concorrenza (Competitive Landscape)

> **Approccio**: il presente paragrafo è frutto di analisi avversariale condotta dall'agente `competitor-intelligence` (vedi `agents/competitor-intelligence.md`). I posizionamenti dei concorrenti sono **cinici e realistici**, non amichevoli.

### 7.4.1 Concorrenti diretti HAPS — Tier 1 globale

| Concorrente | Maturità | Asset | Backing | Posizione Italia | Minaccia per Firmamento |
|---|---|---|---|---|---|
| **AALTO Zephyr 8** (Airbus subsidiary) [^6] | TRL 9, commercial entry 2024 | Zephyr 8/S 60 kg / 25 m / 5 kg payload / 64-day flight | Airbus DS + NTT DOCOMO/Space Compass $100M Asia | Possibile JV con Leonardo (ex-azionista Airbus) o partnership IT diretta | **Alta** — leader assoluto, può saturare mercato IT con basso costo marginale |
| **Sunglider** (AeroVironment + SoftBank) [^7] | TRL 7-8, test stratosferico Aug 2024 | 78 m / 75 kg payload | SoftBank + AeroVironment + DoD trial | Minima al momento | Media — focus US/Asia, ma può espandersi |
| **Skydweller Aero** [^8] | TRL 8, operational 2025 | 72 m / 363 kg payload / 90-day flight | VC US + DoD | Minima | Media-alta — entra in mercato governance dual-use |
| **Aurora Odysseus** (Boeing) [^9] | TRL 6-7, dev | 74.1 m / 25 kg payload / claim up to 1 year | Boeing | Minima | Media |
| **PHASA-35** (BAE Systems / Prismatic) [^10] | Operational 2026 | 150 kg / 35 m / 15 kg payload / 12 mesi target | BAE Systems UK | Possibile via NATO/UK partnership | Media |

> **Verdetto agente `competitor-intelligence`**: **Firmamento NON può competere head-to-head con questi player su scala HALE perennial globale**. Mismatch dimensionale 100-1000x. La differenziazione deve essere su **geografia + modello operativo + sostenibilità**, NON su prestazioni assolute.

### 7.4.2 Concorrenti diretti EU/IT — Tier 1 consortium

| Concorrente | Asset | Posizione | Minaccia |
|---|---|---|---|
| **EuroHAPS** (Thales Alenia Space coordinator, EDF €43M) [^11] | 3 demonstrator: Stratobus + HHAA CIRA + ASBaS | Consorzio chiuso (TAS/Leonardo/Elettronica IT + ONERA/CEA FR + INTA ES + ESG/TAO DE) — Firmamento non è dentro | **Alta** — può catturare quota mercato istituzionale italiano e UE |
| **TAS-Leonardo** (joint stratospheric) | Stratobus + payload integration capability | Backing istituzionale italiano forte (parteccipazione statale Leonardo) | **Alta** — possibile acquisition target Firmamento per "controllo narrativa HAPS italiana" |

> **Risk-flag** (cf. `riferimenti/RESERVED-rischi-geopolitici.md` RSK-GEO-005): a partire dal Y3, scenario "acquisizione difensiva da Leonardo/TAS" è probabilità M; mitigazione richiede capital structure resistente + speed di esecuzione.

### 7.4.3 Concorrenti sostitutivi — Tier 2 satellite + telco

| Soggetto | Cosa fanno | Perché sono concorrenti |
|---|---|---|
| **SpaceX Starlink** [^12] | 6000+ sat LEO broadband globale | **Sostituto per connettività rurale** — €40-60/mese consumer, già disponibile a Pentema oggi |
| **Eutelsat OneWeb** | 648 sat LEO B2B + government | Sostituto NTN backhaul per telco |
| **IRIS²** (EU sovereign satcom €10B) [^13] | 170-300 sat LEO+MEO sovereign EU | **Concorrente per il discorso "sovranità EU"** — Firmamento deve posizionarsi come **complementare** (stratospheric layer), non alternativa |
| **Copernicus Sentinel** (ESA/EU) | Sentinel-1/2/3/5p/6 EO gratuiti | Sostituto EO con revisit 5-12 giorni + GSD 10 m |
| **TIM, Vodafone, Iliad, WindTre, Open Fiber** | 5G FWA rurale via PNRR Banda Ultra Larga €6.7B | Sostituto connettività in aree marginali — gap geografico in chiusura 2025-2028 |

> **Verdetto agente `competitor-intelligence`**: per molte cooperative pilota, **Starlink è già una soluzione completa a €50/mese**. Perché aspettare HALE? La risposta deve essere:
> 1. Latenza bassa (HAPS 0.1-1 ms vs Starlink 25-50 ms — irrilevante per browsing, **decisivo per controllo industriale + ISR**)
> 2. Geografic persistence (HAPS sopra l'area target sempre; Starlink passi inerziali)
> 3. **Sovranità dati italiana** (HAPS in mani italiane vs Starlink US-controlled) — argomento per PA, decisivo
> 4. **Backup independent** (HAPS senza dipendenza Starlink in caso di crisi geopolitica)

### 7.4.4 Cluster D — Service Incumbent Italiani (vero competitor Y1 B2G)

> **Premessa metodologica (post-audit avversariale)**: la versione M+0 del Cap. 7 elencava un singolo concorrente VTOL/UAS italiano in modalità superficiale. L'audit `competitor-intelligence` (vedi `AUDIT-COMPETITOR-VOLUME-1.md` §1 e Critica C7.9) ha dimostrato che **il vero competitor Y1 per il MVP Pentema e per lo scale-up SNAI Liguria non è AALTO né Skydweller** (rischi Y3-Y5) **bensì il cluster degli operatori italiani di servizi EO + UAS già presidio della PA** — di seguito **Cluster D**. Questi soggetti hanno (a) contratti pluriennali in essere con Regioni / PC / ARPA, (b) pricing 3-5× inferiore rispetto al baseline Cap. 7 §7.8.2, (c) reti di rapporti istituzionali consolidate, (d) capability tecnica matura. La presente sezione li profila in dettaglio.

#### 7.4.4.1 Mappa Cluster D — operatori EO + UAS Italia

| # | Operatore | Sede | Ownership | Asset / capability primaria | Track record PA Italia |
|---|---|---|---|---|---|
| **D1** | **e-GEOS S.p.A.** [^16] | Roma + Matera | Telespazio 80% (Leonardo/Thales) + ASI 20% | EO COSMO-SkyMed + Copernicus EMS lead consortium + InSAR + Rapid Mapping 24/7/365 | Contratto Copernicus EMS €36M 2023-2029; contratti regionali multipli (Lazio PC ≥ 2021); leader sostanzialmente monopolistico EO PA Italia |
| **D2** | **Planetek Italia S.r.l.** [^17] | Bari | Privato (PMI, top-200 Sud Italia) | Piattaforma Rheticus® (InSAR Sentinel-1, COSMO-SkyMed, ALOS) + analytics; servizi Cloud SaaS; consorzio Osiride | ASSET Puglia (mitigazione rischio idrogeologico, training 150 professionisti); contratti Regione Puglia multipli; OpenCoesione progetti PA |
| **D3** | **NHazca S.r.l.** [^18] | Roma | Spin-off Sapienza Dip. Scienze della Terra (2009) | InSAR/DInSAR satellitare + TInSAR ground-based + PhotoMonitoring™ + integrazione data intelligence | Monitoraggio frane / infrastrutture critiche / patrimonio culturale; collaborazioni PA + infrastructure manager (AGCOM-ANAS-RFI tier); academic spin-off IntelligEarth |
| **D4** | **FlyingBasket S.r.l.** [^19] | Bolzano | Privato + investimento Leonardo S.p.A. (2024) | Cargo drone FB3 100 kg payload; primo LUC ENAC Italia (2024); primo BVLOS cross-border EU | Provincia Bolzano (21 voli, 4 rifugi alpini, >1 t cargo); contratti offshore UK; pilotato heavy-lift IT operativo |
| **D5** | **Skyrobotic S.p.A.** [^20] | Terni | Gruppo Italeaf | Produzione SAPR sotto 25 kg; SR-SF6 piattaforma multirotore; primo "scenari misti" ENAC (2015 via Consulcad) | Geomatica + mapping PA via integratori; partnership ATC Servizi aviosuperficie sperimentale |
| **D6** | **Aermatica3D S.r.l.** [^21] | Colverde (CO) | Privato | Drone Solutions Provider — integrazione droni custom + sensori + software; primo ENAC scenari critici industriali e urbani | Industria + research centers + PA enti governativi (target dichiarato); operatore certificato BVLOS aree critiche |
| **D7** | **Telespazio S.p.A. (downstream EO)** [^22] | Roma | Leonardo 67% + Thales 33% | Integrato EO + telecomunicazioni + navigation; servizi monitoraggio ambientale + rush mapping + InSAR + thematic mapping; programma IRIDE €1.1B come prime contractor IT | Tutti i settori PA italiani — la "spine dorsale" downstream EO Italia |
| **D8** | **CIRA — Centro Italiano Ricerche Aerospaziali** [^23] | Capua (CE) | Consorzio: ASI + CNR + Regione Campania + industrie aerospace IT | R&D piattaforme stratosferiche per telerilevamento; HELIPLAT lineage; fee-for-service contracts | Partner istituzionale R&D — può diventare partner Firmamento (vedi §7.4.5) o competitor diretto se sviluppa servizio HAPS proprio |

> **Sintesi capability map**: Cluster D copre l'intero stack downstream IT — dati satellitari (D1, D2, D7), analytics + InSAR (D2, D3), operazioni UAS commerciali (D4, D5, D6), R&D piattaforme stratosferiche (D8). Firmamento si sovrappone su (a) UAS service (D4, D5, D6), (b) analytics/monitoraggio (D2, D3), (c) potenziale HAPS R&D (D8). **Tre cluster di sovrapposizione frontale** — non è un mercato vuoto.

#### 7.4.4.2 Pricing benchmark Cluster D vs Firmamento baseline

> **⚠️ Caveat pricing (confidence: low-medium)** — I prezzi sotto riportati sono ricostruzioni dedotte da: (a) press release pubbliche dei contratti vinti, (b) bilanci pubblici degli operatori (Telespazio €701M revenue 2023, e-GEOS €68.8M revenue 2023, Planetek Italia €18-22M revenue 2024 [^17]), (c) portali pubblici MEPA/Consip/InfoGareWeb [^24], (d) benchmark di settore IT/EU 2024-2026. **Non sono prezzi contratti specifici**. Per pricing investment-grade serve accesso a (i) DGR Regionali con allegato economico, (ii) contratti Consip dettaglio, (iii) interviste dirette con buyer PA. Action item benchmark M+6 (riferimento AUDIT-QUALITY-VOLUME-1.md §1 azione #6).

| Linea servizio | Operatore Cluster D di riferimento | Pricing tipico stimato | Note |
|---|---|---|---|
| **Servizio EO monitoraggio frane Regione (canone annuo)** | Planetek Rheticus + e-GEOS InSAR | €30-80k/anno per area regionale | Multi-anno; software-as-a-service (Sentinel free + processing) — economia di scala forte |
| **Mapping/monitoraggio satellitare ricorrente PA** | Telespazio + e-GEOS | €50-150k/anno per contratto | Servizio "chiavi in mano" includendo analytics + delivery |
| **Rapid Mapping emergenze (on-demand)** | e-GEOS (Copernicus EMS gratuito per PA) | €0 marginale per PA (servizio EU gratuito) + €5-15k/event custom | Gratuito per PA tramite Copernicus EMS — falsifica modello "outcome-based event Firmamento" |
| **Servizio UAS commerciale / mapping aereo** | FlyingBasket + Aermatica3D + Skyrobotic | €1.5-4k/giorno operativo o €15-40k per progetto | Pricing mercato libero; FlyingBasket BVLOS premium 30-50% |
| **InSAR + analytics monitoraggio infrastruttura** | NHazca + Planetek | €25-100k/anno per infrastruttura monitorata | Contratti con infrastructure manager + PA |
| **Servizio cargo drone aree impervie** | FlyingBasket | €2-5k/giorno operativo + setup | Mercato di nicchia; primo operatore italiano certificato |
| **Pricing baseline Firmamento Cap. 7 §7.8.2 — monitoraggio EO Regione** | (Firmamento target) | **€150k/anno** | **3-5× sopra benchmark Cluster D** |

> **Falsifying observation §7.4.4.1**: se nei prossimi 6 mesi il benchmark verifica che Cluster D opera servizi EO regionali equivalenti a **€30-60k/anno** con contratti multi-anno già firmati, allora il pricing baseline Firmamento §7.8.2 (€150k/anno) **NON è raggiungibile** entro Y1 senza differenziazione tangibile (es. persistence sub-day, latency <1 s, sovranità dati IT con asset domestico). **Probabilità materializzazione: H** (alta). **Impatto: H** (revenue Y1 baseline scende da €355-405k a €180-240k → sotto soglia SyR-Cost-003 in scenario worst). **Mitigazione**: ridimensionare pricing target a €60-90k/anno per servizio EO base + premium €30-60k/anno per persistence/sovranità verticale.

#### 7.4.4.3 Bandi e contratti recenti — track record Cluster D

| Anno | Operatore | Contratto | Cliente | Valore (dichiarato o stimato) |
|---|---|---|---|---|
| 2023-2029 | e-GEOS (lead consortium) | Copernicus EMS Rapid Mapping (4° rinnovo) | Commissione UE | **€36M** [^25] |
| 2021- | e-GEOS | Mappe satellitari emergenze PC Lazio | Regione Lazio Dip. PC | Non disclosed (stimato €100-300k/anno) [^26] |
| 2020-2024 | Planetek Italia | Rheticus® Displacement ASSET Puglia | Regione Puglia (ASSET) | Non disclosed; training 150 professionisti + monitoraggio continuo |
| 2022-2024 | NHazca (subappalto) | Monitoraggio frane Mont de la Saxe (Courmayeur) | Comune Courmayeur | Stimato €40-120k complessivi GBINSAR [^24] |
| 2024 | FlyingBasket | Light UAS Operator Certificate ENAC + pilot Provincia Bolzano | ENAC + PAB | Pilot project autofinanziato + Leonardo investment 2024 [^19] |
| 2024-2025 | Telespazio (lead) | IRIDE costellazione EO sovrana italiana | ASI / PNRR (€1.1B totale) | Quota Telespazio significativa (non disclosed pubblicamente) |
| 2024-2026 | Vari operatori UAS | RDO MEPA mapping/monitoring ambientale (esempio AMAT Milano) | Comuni / Agenzie | Tipicamente €10-50k per RDO singolo [^24] |

> **Falsifying observation §7.4.4.2**: Telespazio Group ha generato **€701M revenue 2023** [^22] di cui circa **€68.8M da e-GEOS** [^27] (downstream EO). Il TAM-IT EO PA italiana **esistente e già contrattualizzato** è almeno **€50-100M/anno** (somma stimata Telespazio + e-GEOS + Planetek + NHazca + altri). La stima TAM-IT Cap. 7 §7.3.2 (€80-150M Y2026 categoria UAV territoriali) non è quindi un TAM "da costruire" ma un TAM **occupato al 60-80%** da Cluster D. La quota addressable per un newcomer è realisticamente **20-40% del residuo**, ovvero €5-20M, NON €40-100M come dichiarato in §7.3.3 SAM-IT.

#### 7.4.4.4 Posizione di ogni operatore vs Firmamento

| Operatore | Sovrapposizione UC Firmamento | Vantaggio strutturale dell'incumbent | Possibile mossa difensiva Firmamento |
|---|---|---|---|
| **D1 e-GEOS** | UC-001 frane, UC-002 antincendio (via EMS), UC-007 vigilanza | Monopolio sostanziale EO PA Italia + Copernicus gateway gratuito | Non concorrere head-to-head; **partnership downstream** (Firmamento = UAS layer aereo persistente, e-GEOS = satellite layer) — vedi §7.4.5 |
| **D2 Planetek** | UC-001 frane (InSAR), UC-004 mapping infrastrutture | Track record Puglia + altre Regioni + SaaS scalabile | Co-progettazione "InSAR satellitare + UAV LIDAR sub-day": differenziazione integrata, non concorrenza diretta |
| **D3 NHazca** | UC-001 frane, UC-004 mapping infrastrutture critiche | Credenziali accademiche Sapienza + reputation tecnica | Possibile R&D partner per validazione algoritmi; bassa minaccia commerciale diretta |
| **D4 FlyingBasket** | UC operativo UAS in aree impervie (cargo + mapping) | Primo LUC ENAC Italia + cross-border BVLOS + **Leonardo investment 2024** | **Minaccia H**: ha già il SORA certificato + Leonardo backing; può competere frontalmente su BVLOS Pentema |
| **D5 Skyrobotic** | UC mapping commerciale + scenari misti | Produttore + integratore con storia decennale | Minaccia M; focus prevalente su geomatica commerciale, non Aree Interne |
| **D6 Aermatica3D** | UC mapping critico urbano + industriale | Primo ENAC scenari critici + capability custom integration | Minaccia M-H; cliente target sovrapposto (research centers, PA, industrie) |
| **D7 Telespazio** | Tutti gli UC EO + telecom | Spine dorsale downstream EO IT + accesso istituzionale Leonardo | Non concorrere; **rischio acquisizione difensiva** post-Series A (vedi RSK-GEO-005 + Cap. 11 Threat 1) |
| **D8 CIRA** | UC HAPS R&D (Fase 6B) | Lineage HELIPLAT + EuroHAPS partner + Capua test facility | **Partner critico** Phase B 6B — già flaggato Cap. 6 e Cap. 7 §7.6.2; se rifiuta partnership, Firmamento Phase B 6B è severamente ridimensionata |

> **Falsifying observation §7.4.4.3**: la presenza di **Leonardo investment in FlyingBasket (2024)** [^19] è segnale forte che il gruppo Leonardo/TAS sta consolidando il proprio presidio UAS service Italia. **Implicazione**: la "spazio di mercato" che Firmamento mira a occupare (UAS service Aree Interne) è già in fase di rastrellamento da parte del Tier 1 italiano (TAS-Leonardo via FlyingBasket + Telespazio downstream). Lo scenario "acquisizione difensiva Firmamento entro Y3-Y5" (AUDIT-COMPETITOR-VOLUME-1.md §0, P ~50-70%) è coerente con questa traiettoria di consolidamento già in atto.

---

### 7.4.5 Verdetto Cluster D vs Firmamento — strategia di posizionamento

#### 7.4.5.1 Conclusione cinica

**Il Cluster D è il vero competitor Y1 di Firmamento, non AALTO / Skydweller / EuroHAPS** (questi ultimi sono rischio Y3-Y5 boundary B2). Le ragioni:

1. **Cluster D è qui adesso**: e-GEOS, Planetek, NHazca, FlyingBasket, Aermatica3D sono operativi, fatturano, hanno contratti firmati e rapporti istituzionali consolidati. Sono il **default vendor** della PA italiana per servizi EO/UAS — un newcomer parte dietro di 5-15 anni di track record.
2. **Cluster D è cash-positive**: Planetek €18-22M revenue 2024 [^17], e-GEOS €68.8M revenue 2023 [^27], Telespazio €701M Group revenue 2023 [^22]. Non sono startup in cerca di break-even — possono permettersi pricing aggressivo difensivo se Firmamento viene percepita come minaccia.
3. **Cluster D è già nel cap-table dell'incumbent IT**: Telespazio 80% di e-GEOS, Leonardo 67% di Telespazio + investitore 2024 in FlyingBasket. Il gruppo Leonardo presidia 4 dei 7 operatori D commerciali (D1, D4 partial, D7, D8 partial via consorzio). **Il mercato non è frammentato — è consolidato attorno a Leonardo/TAS**.
4. **Pricing baseline Firmamento è 3-5× sopra benchmark**: §7.8.2 €150k/anno servizio EO Regione vs €30-80k/anno Cluster D. **Non si vince un bando pubblico italiano con prezzo 3-5× più alto** senza un differenziatore non replicabile e dimostrato.

#### 7.4.5.2 Implicazioni per il business case Firmamento

**Non si può competere head-to-head per pricing.** Cluster D ha vantaggi strutturali insuperabili Y1 (economie di scala satellitari + Sentinel free + rapporti consolidati + Leonardo backing). Tre vie strategiche residue:

**A — Differenziazione per persistence + latency + sovranità verticale (UC-001 + UC-002)**

| Asse differenziazione | Vantaggio Firmamento UAS vs Cluster D satellite | Quantificazione |
|---|---|---|
| **Persistence** | Volo on-demand + missioni settimanali pianificate vs revisit satellite 5-12 gg | UAV: 1-7 gg latenza acquisizione; Sentinel-1: 6-12 gg; COSMO-SkyMed: 1-3 gg ma costo alto |
| **Latency delivery** | UAS: minuti-ore (downlink locale); satellite: 1-3 gg processing | Decisivo per UC-002 antincendio (early detection <5 min) |
| **GSD spaziale** | UAS GSD 5-20 cm; satellite GSD 50 cm-10 m | Decisivo per ispezione strutturale, NON per monitoraggio macro-area |
| **Sovranità dati IT** | Asset domestico Firmamento vs e-GEOS (Telespazio = Leonardo+Thales FR) | Argomento marginale (e-GEOS è già IT-controlled), residuo solo vs Copernicus FR/DE |

**Verdetto asse A**: difensibile per **UC-002 antincendio** (latency decisivo) e **UC-001 frane in fase di crisi acuta** (persistence sub-day per eventi attivi). Non difensibile per monitoraggio di routine, dove satellite + InSAR vincono per costo/area.

**B — Partnership downstream invece di competition**

| Configurazione | Razionale | Probabilità accettazione partner |
|---|---|---|
| **Firmamento operatore UAS + e-GEOS analytics layer** | Firmamento = aerial layer persistente; e-GEOS = EO satellitare + processing; insieme = "complete stack" Regione | M (~30-50%) — e-GEOS può essere recettivo per consolidare presidio Regione Liguria; trade-off: Firmamento subordinata commercialmente |
| **Firmamento + Planetek Rheticus per InSAR + UAV LIDAR** | Integrazione "InSAR macro + UAV sub-day" per casi UC-001 frane Liguria | M-H (~40-60%) — Planetek ha track record Puglia, espansione Liguria possibile; partnership tecnica naturale |
| **Firmamento + NHazca per validazione scientifica** | NHazca = lineage accademico Sapienza; Firmamento = operatore. Co-firma su position paper / report tecnici Regione | M (~30-50%) — natura R&D + accademia + commercial blend |
| **Firmamento + CIRA per Phase B 6B HAPS** | Già flaggato Cap. 7 §7.6.2 e Cap. 6; partnership critica per Phase B | M-H (~40-60%) ma dipendenza forte = single-point-of-failure |
| **Firmamento + FlyingBasket per BVLOS aree impervie** | FlyingBasket ha LUC + cross-border BVLOS; Firmamento può accederne come operator-of-operator | L-M (~15-30%) — FlyingBasket è Leonardo-backed, conflitto strategico potenziale |

**Verdetto asse B**: partnership con D2 (Planetek) e D3 (NHazca) sono le opzioni più realistiche e meno onerose strategicamente. Partnership con D1 (e-GEOS) e D7 (Telespazio) crea dipendenza dal gruppo Leonardo (rischio RSK-GEO-005). Partnership con D8 (CIRA) è critica ma non sostitutiva (è R&D, non commercial Y1-Y2).

**C — Specializzazione UC dove Cluster D non opera bene**

| UC residuale | Razionale "blue ocean" residuo | Sostenibilità Y1 |
|---|---|---|
| **UC-002 antincendio early-detection persistence** | Cluster D non ha asset persistenti regionali; il default è Copernicus EMS post-evento, non early-detection real-time | Sostenibile se Firmamento riesce a dimostrare latency <5 min in campo |
| **UC-006 SAR persone disperse** | Tipicamente operato da VVF/CC Forestali interno, no servizio commerciale strutturato | Mercato piccolo (€5-30k/event); non scalabile |
| **UC-008 telemedicina rurale + NTN** | Mercato non presidiato da Cluster D né da Cluster C telco (per gap copertura); ma **Starlink lo divora già** (vedi Cap. 7 §7.4.3 Threat 2) | NON sostenibile come anchor; declassare a opportunistico (azione AUDIT §3 e §10.3) |
| **UC-005 agricoltura precision cooperative** | Cluster D non target cooperative agricole singole (mercato non scalabile per loro); Topcon/Trimble/AGRIcolus sono i veri competitor | Sostenibile come UC complementare cooperative, NON come anchor revenue |

**Verdetto asse C**: UC-002 antincendio + UC-005 agricoltura cooperative sono le due nicchie residue dove Cluster D non presidia in modo dominante. Sono coerenti con boundary B1 (cooperative) e con strategia Aree Interne. **Devono diventare il cuore del MVP Y1**, non gli UC accessori.

#### 7.4.5.3 Raccomandazione strategica Cluster D

**Riconfigurazione del posizionamento Y1 raccomandata** (input da integrare in Cap. 1 §1.7, Cap. 7 §7.5.1, Cap. 11 §11.2):

1. **Abbandonare la narrativa "Firmamento sostituisce e-GEOS / Planetek nella PA italiana"**: è falsa e non vendibile. Cluster D resterà incumbent.
2. **Posizionarsi come "operatore UAS persistente complementare a EO satellitare incumbent"**: Firmamento = sub-day persistence + sub-meter GSD + Aree Interne specialized; Cluster D = wide-area + revisit settimanale + analytics consolidato.
3. **Aprire formalmente trattativa di partnership con Planetek (D2) entro M+6** — è il candidato più realistico per asse B partnership tecnica.
4. **Aprire formalmente trattativa con CIRA (D8) entro M+6 per Phase B 6B** — non è opzionale, è critico.
5. **NON aprire trattativa di acquisizione con Telespazio/e-GEOS prima di M+24** — preserva opzionalità (vedi Cap. 11 Threat 1).
6. **Allineare pricing baseline §7.8.2 a benchmark Cluster D**: ridimensionare canone EO Regione da €150k/anno a **€60-90k/anno base + €30-60k/anno premium per persistence/sovranità**. Revenue Y1 baseline scende da €355-405k a **€220-300k**, ma è realistico e difensibile.
7. **Monitor Leonardo + FlyingBasket strategy**: il rastrellamento operatori UAS service da parte del gruppo Leonardo è in atto (FlyingBasket investment 2024). Firmamento deve **decidere entro M+12** se posizionarsi come "asset acquisibile da Leonardo a valutazione fair" (exit precoce Y3-Y4) o come "asset indipendente con capital structure resistente". La scelta condiziona tutto il piano Y2-Y3.

> **Falsifying observation §7.4.5**: se al M+12 (i) nessuna trattativa di partnership con Planetek o CIRA è formalizzata, AND (ii) il pricing baseline Firmamento non è stato ridimensionato a benchmark Cluster D, AND (iii) la quota di mercato UAS service Aree Interne Liguria di FlyingBasket/Aermatica3D non è stata profilata empiricamente, allora **il business case Firmamento Cap. 7 va riscritto ex novo** prima del Gate G3. Probabilità materializzazione di tutti e 3 i mancati al M+12: M (~30-40%). Impatto: H.

---

### 7.4.6 Concorrenti VTOL commerciali — Tier 3 per Percorso 6A

Per il Percorso 6A baseline (VTOL pilota), Firmamento **utilizza** piattaforme commerciali (es. JOUAV CW-30E), non concorre con i vendor. I concorrenti **operativi** del Percorso 6A erano stati elencati in modalità sommaria nella versione M+0 del capitolo (ItaliaMeteo, generic UAS commerciali, flotte UAS interne PA). **Questa lista è ora ampiamente superata e riassorbita dalla §7.4.4 Cluster D**, che fornisce profilo dettagliato dei reali competitor operativi italiani (FlyingBasket, Skyrobotic, Aermatica3D, etc.).

Per evitare ridondanza, in questa sezione si riportano solo le categorie che NON sono coperte dal Cluster D:

| Categoria | Soggetti | Posizione vs Firmamento | Minaccia |
|---|---|---|---|
| **Flotte UAS interne PA** | Carabinieri Forestali, VVF, Polizia di Stato, Guardia Costiera | Capacità interna PA — clienti potenziali (vendono servizi a Regione), NON concorrenti commerciali | Bassa — anzi, possibile cliente B2G |
| **Operatori UAS regionali frammentati** | Operatori locali per ispezioni infrastruttura, agro-mapping, eventi | Mercato frammentato + low-margin; tipicamente sotto soglia BVLOS | Bassa — non concorrono su scala SNAI/regionale |
| **Operatori UAS amatoriali/volontari** | Rescue Drones Network (volontari PC); operatori amatoriali Comuni | Volontariato + supporto PC; non competono commercialmente | Trascurabile — possibile interlocutore institutional |

> **Nota di rinvio**: per il dettaglio dei veri competitor UAS commerciali italiani (FlyingBasket, Skyrobotic, Aermatica3D) si rimanda a §7.4.4 Cluster D.

---

### 7.4.7 Verdetto agente `competitor-intelligence` consolidato (riconfigurato post-audit)

> **Nota di versione**: la versione M+0 del Cap. 7 §7.4 chiudeva con un verdetto sintetico focalizzato su Tier 1 globali (AALTO, Skydweller, EuroHAPS) e su Starlink come sostituto. L'audit avversariale di maggio 2026 ha imposto una **riconfigurazione completa** del verdetto, perché il rischio competitivo Y1 è strutturalmente diverso dal rischio Y3-Y5.

**Gerarchia dei rischi competitivi per orizzonte temporale**:

| Orizzonte | Cluster di rischio prevalente | Razionale |
|---|---|---|
| **Y1 (M+0-12) — MVP Pentema** | **Cluster D — Service Incumbent IT** (e-GEOS, Planetek, NHazca, FlyingBasket, Aermatica3D, Telespazio) | Sono i veri competitor per ogni bando B2G regionale Liguria. Pricing 3-5× sotto Firmamento baseline; track record consolidato; rastrellamento Leonardo in atto via FlyingBasket investment 2024 |
| **Y1-Y2 (M+0-24) — connettività rurale** | **Cluster B — SpaceX Starlink** (sostituto satellite) | Già operativo a Pentema; €40-60/mese consumer + Direct-to-Cell EU 2026-2027. Erode UC-003 + UC-008. Già flaggato §7.4.3 |
| **Y2-Y3 (M+12-36) — scale-up SNAI multi-regione** | **Cluster A — AALTO HAPS (Airbus)** entry IT via JV Leonardo | Probabilità entry IT 35-50% se Firmamento diventa visibile; cattura mercato HAPS narrativo prima del consolidamento |
| **Y3-Y5 (M+36-60) — survival standalone** | **Cluster C — TAS-Leonardo** acquisizione difensiva | Probabilità H (55-70%); offerta "fair value" €30-100M; founder out; boundary B2 IT-led morta |
| **Y4-Y6 (M+48-72) — boundary B2 EU sovereign** | **IRIS² absorbs HAPS** + **Skydweller** + **PHASA-35** | Programma EU sovereign HAPS non si materializza autonomamente; HAPS confinato come "layer accessorio IRIS²" |

**Conclusioni operative consolidate**:

1. **Firmamento NON può competere head-to-head con Cluster D su pricing nel B2G regionale italiano**. Il pricing baseline §7.8.2 (€150k/anno servizio EO Regione) va ridimensionato a €60-90k/anno + premium €30-60k/anno (vedi §7.4.5.3 azione 6).

2. **Firmamento NON può competere head-to-head con Cluster A/C globali su scala HALE perennial**. Mismatch dimensionale 100-1000x già flaggato §7.4.1. Differenziazione su geografia + cooperative + sovranità IT.

3. **Firmamento NON può sostituire Starlink su connettività rurale consumer/PA**. UC-003 + UC-008 declassati a opportunistici (azione AUDIT-QUALITY §1 #5).

4. **L'unica via strategica sostenibile per Y1-Y3 è**:
   - **(a)** Specializzazione UC-001 frane in fase di crisi + UC-002 antincendio early-detection (asse persistence/latency dove Cluster D satellite non vince)
   - **(b)** Partnership downstream con Planetek (D2) + NHazca (D3) + CIRA (D8 per Phase B 6B)
   - **(c)** Anchor cooperative Legacoop come moat di posizionamento (non di prezzo)
   - **(d)** Capital structure resistente PRIMA del Series A per neutralizzare scenario acquisizione Y3-Y5

5. **Probabilità di successo del piano competitivo Y1-Y3 con riconfigurazione completa**: 25-40% (in linea con AUDIT-QUALITY-VOLUME-1.md §6 P(AND hard conditions) = 5-15% scenario realistico, elevato a 25-40% se action items §3 implementati integralmente).

6. **Probabilità di successo del piano competitivo Y1-Y3 SENZA riconfigurazione (status quo M+0)**: <15% (AUDIT-COMPETITOR-VOLUME-1.md §0 baseline).

> **Falsifying observation §7.4.7**: se al gate G3 M+11 (i) Firmamento non ha riconfigurato pricing §7.8.2 in linea con benchmark Cluster D, AND (ii) non ha aperto trattativa formale di partnership con almeno UN operatore D2/D3/D8, AND (iii) non ha riconosciuto esplicitamente Cluster D come competitor primario Y1 nel pitch verso finanziatori, allora **il verdetto Go Condizionato 6A va declassato a Hold rinforzato** indipendentemente dallo stato delle altre hard conditions C1-C5. Probabilità materializzazione di tutti e 3 i mancati al M+11: M (~30-40%). Impatto: H (verdetto gate compromesso).

---

## 7.5 Posizionamento Firmamento Technologies

### 7.5.1 4 pilastri del vantaggio competitivo (riconfigurati post-audit Cluster D)

> **Premessa post-audit**: la versione M+0 di questa sezione presentava i 4 pilastri come "difendibili" senza qualificare il **tipo di competitor** verso cui sono difendibili. L'audit `competitor-intelligence` (Critica C7.6) ha dimostrato che dei 4 pilastri, **solo il modello cooperativo è genuinamente difendibile** vs il vero competitor Y1 (Cluster D). Questa sezione è stata riscritta per riflettere la realtà.

Il posizionamento di Firmamento poggia su 4 pilastri, ognuno con **difensibilità differenziata per tipologia di competitor**:

#### Pilastro 1 — Specializzazione geografica Aree Interne italiane

- Focus esclusivo SNAI Liguria + scale-up SNAI nazionale
- Vantaggio "first mover" + reti di rapporti istituzionali consolidate
- ✅ **Difensibile vs Tier 1 globali** (Zephyr/Skydweller/PHASA-35 non sono interessati a micro-mercati regionali italiani Y1-Y3)
- ❌ **NON difensibile vs Cluster D italiani** (e-GEOS, Planetek, NHazca, FlyingBasket): questi operatori **sono già in Liguria** o possono entrarvi rapidamente, sono italiani, hanno rapporti consolidati con la stessa PA, e in alcuni casi (e-GEOS, FlyingBasket via Leonardo investment 2024) hanno backing istituzionale forte. La "specializzazione geografica" Firmamento è un argomento marketing, NON un moat strutturale vs Cluster D.
- **Conclusione onesta**: questo pilastro vale parzialmente. Difensibile vs threat globali; va integrato con partnership Cluster D (vedi §7.4.5) per non essere falsificato.

#### Pilastro 2 — Modello cooperativo Legacoop (boundary condition B1)

- 10 cooperative pilota come utenti + co-progettisti
- Community ecosystem → barrier to entry per competitor (no easy replication of cooperative trust)
- Allineamento valoriale con PA regionale + SNAI mission
- ✅ **Difensibile vs Tier 1 globali**: Airbus/BAE/Boeing non possono raccontare "service cooperativo italiano" credibilmente
- ✅ **Parzialmente difensibile vs Cluster D italiani**: e-GEOS/Planetek/FlyingBasket non hanno DNA cooperativo, ma **possono fare partnership con Legacoop**: nulla impedisce a Coopfond di accettare un service contract da FlyingBasket se Firmamento fallisce. Il moat è reale ma non legale-vincolante — è una **switching cost soft**.
- ✅ **Difensibile vs Cluster A/B sostituti**: Starlink non ha rapporto con cooperative SNAI; AALTO neppure
- **Conclusione onesta**: questo è il **vero pilastro difendibile** del posizionamento Firmamento. Ma per essere un moat strutturale (non soft switching cost) richiede **strutturazione giuridicamente vincolante** (consorzio formale, contratto di rete con esclusive territoriali, regime "preferred provider" con Coopfond). Lavoro non ancora completato al M+3. Action item: governance giuridica cooperative entro M+12.

#### Pilastro 3 — Sostenibilità + narrativa ESG

- Propulsione 100% solare (HALE) / elettrica (VTOL)
- Materiali bio-compositi (fibra di lino) per strutture secondarie
- Carbon footprint operativo basso vs alternative satellitari (no detriti spaziali)
- Storia narrativa forte per finanziatori ESG-aware (FESR, EIC, ESG-funds)
- ❌ **NON difensibile vs nessun cluster competitor**: AALTO Zephyr è già 100% solare; FlyingBasket è 100% elettrico; e-GEOS opera su satellite Sentinel (nessuna emissione operativa marginale); Starlink dichiara propria roadmap ESG. La sostenibilità è un **commodity narrativa** nel 2026 — non un moat.
- **Conclusione onesta**: questo pilastro è utile come narrative element verso finanziatori ESG (FESR, EIC, ESG funds), ma **non differenzia Firmamento** vs competitor. È un "must have", non un "nice to have differenziale". Va declassato da "pilastro difensivo" a "narrative requirement".

#### Pilastro 4 — Approccio incrementale VTOL → MALE → HALE

- Riduzione progressiva del rischio tecnologico (TRL 8-9 commerciale → R&D HALE)
- Asset riusabili: ground segment, data governance, brand, competenze, autorizzazioni regolatorie
- Capital efficiency superiore vs concorrenti "HAPS-only" (es. Zephyr) che non hanno revenue intermedio
- ✅ **Difensibile vs Tier 1 HAPS pure-play** (AALTO, Skydweller): hanno revenue zero pre-HAPS operativo, brucianti cash; Firmamento può autoalimentarsi parzialmente da VTOL revenue
- ❌ **NON difensibile vs Cluster D** (e-GEOS, Planetek, FlyingBasket, Telespazio): questi operatori sono già cash-positive, hanno asset operativi, non hanno bisogno di "incrementare" perché operano già il loro stack core
- **Falsifying observation**: se il Percorso 6A non genera revenue Y1 ≥ €200k entro M+12, il "ladder" è interrotto e gli investitori per Phase B 6B non sono convinti. **Inoltre**: se il Percorso 6A genera revenue Y1 €200-300k SOLO grazie a partnership con Cluster D (subordinazione), il pilastro 4 diventa "revenue da subfornitura", non "ladder autonomo" — implicazione per valuation Series A.

#### Sintesi pilastri rivisti

| Pilastro | Difensibilità vs Tier 1 globali | Difensibilità vs Cluster D (vero competitor Y1) | Difensibilità vs sostituti (Starlink) |
|---|---|---|---|
| 1. Specializzazione geografica | ✅ Alta | ❌ Bassa | n/a |
| 2. Modello cooperativo Legacoop | ✅ Alta | 🟡 Media (richiede strutturazione giuridica) | ✅ Alta |
| 3. Sostenibilità + ESG | ❌ Nessuna (commodity) | ❌ Nessuna | ❌ Nessuna |
| 4. Approccio incrementale VTOL → HALE | ✅ Alta | ❌ Bassa | n/a |

**Conclusione consolidata §7.5.1**: dei 4 pilastri originali, **solo il #2 (cooperativo) è un moat vero vs il competitor reale Y1 (Cluster D)**, e richiede strutturazione giuridica per essere vincolante. I pilastri 1 e 4 funzionano vs threat Y3-Y5 (Tier 1 globali) ma non vs threat Y1 (Cluster D). Il pilastro 3 è narrative, non moat. **Il vantaggio competitivo difendibile reale di Firmamento è quindi 1 pilastro su 4, condizionato a esecuzione governance cooperative.** Questa è l'onesta lettura post-audit.

### 7.5.2 Linguaggio pubblico e posizionamento sovrano EU

Per ragioni geopolitiche dichiarate in `RESERVED-rischi-geopolitici.md` (RSK-GEO-001, RSK-GEO-004), il linguaggio pubblico è:

✅ **Da usare**:
- "Stratospheric layer complementary to the EU sovereign multi-orbit infrastructure (Galileo, Copernicus, IRIS²)"
- "Italian leadership in EU stratospheric sovereignty"
- "Italian operator of persistent aerial services for Inner Areas, towards EU consortium"

❌ **Da NON usare** (provocatorio per US, mal recepito da Bruxelles):
- "Alternativa europea a Starlink"
- "EU competitor to SpaceX"

---

## 7.6 Business Model Canvas (BMC) — Percorso 6A

> Riferimento metodologico: Osterwalder & Pigneur. Riferimento agente: `business-model-strategist`.

### 7.6.1 BMC Percorso 6A — MVP Pentema Y1

| Block | Contenuto |
|---|---|
| **Customer Segments** | (1) Regione Liguria (anchor); (2) Protezione Civile + ARPA Liguria; (3) Comune di Torriglia + comunità Pentema; (4) 10 cooperative pilota Legacoop (capofila Fabrica); (5) Enti Parco Antola/Aveto; (6) ASL3 (telemedicina) |
| **Value Propositions** | "Servizi territoriali persistenti EO + connettività di emergenza per le Aree Interne, conformi GDPR, prezzo accessibile alla PA, gestiti in partnership con cooperative locali" |
| **Channels** | Diretto B2G (gare D.Lgs.36/2023 + accordi quadro); contratto di rete con cooperative; intermediazione Coopfond/Legacoop |
| **Customer Relationships** | Service-based (canone + ore-volo + analytics); supporto operativo 24/7 in emergenza; co-progettazione iterativa con cooperative |
| **Revenue Streams** | (1) Canoni annuali servizio EO per Regione/PA (€100-300k/anno per regione); (2) ore-volo + analytics per missioni on-demand (€1500-5000/ora + canone analytics); (3) outcome-based emergency alert (€1-10k/event); (4) DaaS pacchetti cooperative (€5-50k/anno per coop) |
| **Key Resources** | Tangible: 1 VTOL JOUAV CW-30E (o eq), payload EO+IR, GS fissa+mobile, hangar Pentema, software pipeline. Intangible: autorizzazioni ENAC SORA, brand, rete cooperative, IP concept HALE |
| **Key Activities** | Operazioni di volo BVLOS; pipeline acquisizione → processing → delivery; engagement istituzionale; sviluppo R&D Percorso 6B parallelo; gestione partnership cooperative |
| **Key Partners** | Coopfond (finanziatore + sponsor istituzionale); Regione Liguria (anchor customer + sponsor); 10 cooperative pilota; D-Flight (USSP futuro); ENAV; CIRA (R&D partner per 6B); POLITO DIMEAS (accademico) |
| **Cost Structure** | CapEx Y1: €700-1200k (vedi Cap. 8 dettaglio). **OpEx Y2 run-rate RECONCILED post Cap. 5 §5.17: €1.18M/anno centrale (range €1.05-1.30M)** — include OpEx tecnico €260-480k + Regulatory team mandatory €400-590k (CISO + DPO + Head Regulatory) + overhead €115-230k. Costo capitale fisso (asset + cert + privacy + training). Costo variabile per ora-volo: €200-500/ora |

### 7.6.2 BMC Percorso 6B — HALE R&D Phase B Y3-Y5

| Block | Contenuto |
|---|---|
| **Customer Segments** | Y3-Y5: nessun cliente commerciale diretto (R&D phase). Stakeholder: finanziatori (EDF, Horizon, PNRR), partner R&D (CIRA, TAS), early adopter PA per pilot operativo M+48+ |
| **Value Propositions** | "Italian stratospheric demonstrator paving the way for EU sovereign HAPS layer, dual-use civilian-defence, complementary to IRIS²" |
| **Channels** | Bandi pubblici EDF/Horizon/PNRR; consorzio EU stratospheric (in costruzione); engagement Difesa NATO DIANA |
| **Customer Relationships** | Research consortium relationships; engagement istituzionale lungo (Y2-Y5) |
| **Revenue Streams** | Grant EU/IT (no revenue commerciale Y3-Y5); progressive shift verso revenue commerciale Y6+ |
| **Key Resources** | HALE prototype subscale (Y3) → full-scale (Y5); patent portfolio (fibra di lino + concept); R&D team 8-15 FTE; ground test facility |
| **Key Activities** | R&D engineering (aero, propulsion, avionics, payload); flight test subscale; engagement EASA Special Condition; consortium building EU |
| **Key Partners** | CIRA (partner critico); POLITO DIMEAS (HELIPLAT lineage); TAS-Leonardo (potenziale, da gestire vs RSK-GEO-005); ESA (futuro); MIMIT (finanziamento) |
| **Cost Structure** | CapEx R&D Phase B: €5.5-13.5M (vedi Cap. 8). 30-40% engineering, 10-15% prototype, 10-15% test, 15-25% personnel, 5-10% certification engagement |

---

## 7.7 Value Proposition Canvas (VPC)

Per i 3 segmenti customer principali del Percorso 6A:

### 7.7.1 VPC Segmento Regione Liguria + Protezione Civile

| Customer Jobs | Pains | Gains |
|---|---|---|
| Monitorare il rischio idrogeologico delle aree SNAI | Costi alti di sorveglianza territoriale; tempi di reazione lenti satellite (revisit 6-12 gg) | Mappe ad alta risoluzione settimanali; alert in tempo reale |
| Prevenire/rispondere a incendi boschivi | Hotspot detection ritardato; mancanza copertura persistente | Alert <5 min via IR + thumbnail |
| Garantire connettività in emergenza | Black-out infrastrutture terrestri durante crisi | Backup LTE tattico on-demand |
| Conformità regolatoria PA | Procedure complesse + compliance multi-fonte | Operatore certificato SAIL III + GDPR ready |

| Value Propositions | Products & Services | Gain Creators | Pain Relievers |
|---|---|---|---|
| "Servizio EO settimanale GSD 0.5m + IR alert in 5 min, conforme GDPR, canone fisso annuale" | Servizio EO monitoraggio frane; servizio antincendio; backup connettività; ricerca persone disperse | Risparmio costi vs satellite premium; risposta più rapida; sovranità dati italiana | Riduce burden compliance (Firmamento è certificato); riduce uncertain capacity (servizio dedicato regionale) |

### 7.7.2 VPC Segmento Cooperative Legacoop (Fabrica + 10 pilota)

| Customer Jobs | Pains | Gains |
|---|---|---|
| Operare attività agroforestali/manutenzione in aree montane | Mappe topografiche obsolete; difficoltà accesso aree impervie | Mappe aggiornate annuali; supporto operativo mirato |
| Accesso a connettività digitale in zone non servite | Gap copertura 4G/5G; costo Starlink (anche se accessibile) | Connettività di backup; alleanza con altre cooperative SNAI |
| Sostenibilità + impatto sociale dell'attività cooperativa | Difficoltà narrativa ESG; costi tecnologici alti per singola coop | Aggregazione fa massa critica; brand "tecnologia cooperativa italiana per Aree Interne" |

| Value Propositions | Products & Services | Gain Creators | Pain Relievers |
|---|---|---|---|
| "Dati territoriali on-demand + connettività di backup per cooperative, in modalità cooperative-friendly (canone modico + community)" | Mappe + monitoraggio agricolo; connettività emergenza; mapping infrastrutture cooperative | Co-titolarità progetto = engagement profondo; reuse dati tra cooperative; brand condiviso ESG | Costi distribuiti tra 10 cooperative; supporto tecnico shared; no investimento individuale UAV |

### 7.7.3 VPC Segmento Comunità Pentema

| Customer Jobs | Pains | Gains |
|---|---|---|
| Vivere/lavorare in borgo montano | Isolamento; servizi essenziali carenti; rischio idrogeologico | Servizi essenziali migliorati; sicurezza territoriale aumentata |
| Mantenere identità culturale e ambientale | Spopolamento; abbandono tradizioni | Riconoscimento + valorizzazione tramite case study; investimento simbolico Liguria |

| Value Propositions | Products & Services | Gain Creators | Pain Relievers |
|---|---|---|---|
| "Pentema come laboratorio italiano di tecnologia per le Aree Interne — innovazione che rispetta la comunità" | Privacy by design (no sorveglianza personale); workshop di engagement; trasparenza DPIA pubblica | Pentema diventa "modello" mediatico (potenziale orgoglio locale); attrattività turistica indiretta | Niente intrusione privacy (geofence aree residenziali); governance condivisa con comunità |

---

## 7.8 Modello di Servizio e Pricing

### 7.8.1 4 archetipi di revenue model

In coerenza con boundary condition B1 (service-only, no product sale), il revenue model si articola in 4 archetipi, combinabili:

| Modello | Cliente target | Logica pricing | Pricing tipico | Maturità target |
|---|---|---|---|---|
| **Canone fisso** | PA pluriennale | Servizio garantito + SLA | €100-500k/anno per area servita | Y1+ |
| **Ore-volo + analytics** | PA + utility | Ore di volo operativo + analisi consegnate | €1500-5000/ora volo + €50-300k/anno analytics package | Y1+ |
| **Outcome-based** | PC, assicurazioni | Pay-per-event (alert verificato, danno prevenuto) | €1-10k/event verificato | Y2+ |
| **DaaS (Data-as-a-Service)** | Cooperative, B2B leggero | Abbonamento dati su area + processing | €5-50k/anno per cooperativa | Y2+ |

### 7.8.2 Pricing baseline MVP Y1 RECALIBRATED post-Cluster D audit (M+3, confidence medium-low)

> **Stato baseline**: la versione originale "€355-405k da pricing Regione €150k/anno" è **FALSIFICATA** dal benchmark Cluster D (Planetek Rheticus Puglia €30-50k/anno, e-GEOS PC Lazio canone implicito €40-60k/anno, NHazca monitoraggio frane €20-40k/anno per area). Il pricing baseline pre-audit è qui mantenuto in **legacy** solo come traccia falsifying observation §7.4.4 (vedi §7.4.5 azione obbligatoria pre-G3).

Lo Studio adotta i seguenti **pricing baseline RECALIBRATED** per il MVP Y1, allineati al benchmark Cluster D, da validare con LoI/contratti effettivi:

| Linea servizio | Cliente | Pricing baseline Y1 RECALIBRATED | Volume target Y1 | Revenue Y1 stimato |
|---|---|---|---|---|
| Monitoraggio frane settimanale Liguria interna | Regione Liguria | Canone €75k/anno base + €25k premium persistence/sovranità | 1 contratto | €75-100k |
| Antincendio boschivo stagione estate | PC Liguria + 1 Ente Parco | Canone €40k stagione + €3-5k/event verificato (max 5 event) | 1 PC + 1 Parco | €55-65k |
| Backup connettività emergenza | PC Liguria | On-demand €3-10k/event (max 5) + €15k retainer | 1 contratto retainer | €30-65k |
| Mapping agricolo cooperative | 3 cooperative agricole pilota | Abbonamento DaaS €8k/anno per cooperativa | 3 contratti | €24k |
| Mapping infrastrutture stradali Comune | Comune Torriglia + 2 altri Comuni SNAI | Servizio €12k per Comune | 3 contratti | €36k |
| **Totale revenue Y1 baseline RECALIBRATED** | | | | **€220-290k (centrale €260k)** |
| **(legacy pre-audit, FALSIFICATO)** | | | | (€355-405k) |

> **Falsifying observation §7.8.2 RECALIBRATED**: se entro M+9 non sono firmati ≥ 3 contratti pluriennali con valore aggregato ≥ €200k al pricing baseline €75-100k/anno PA + €8-12k DaaS, il SyR-Cost-003 (revenue Y1 ≥ €200k) è in stato "Failed", e va attivata revisione del modello (es. pivot a more aggressive PA push, pure cooperative agricola, o pivot pricing dual-use con MOI/MAECI). **Probabilità: M, impatto: H**. Mitigazione: engagement intensivo Regione + PC entro M+0-6 + benchmark Cluster D pubblicizzato (DR-006 closure).

### 7.8.3 Pricing post-MVP — scale-up Y2-Y5

| Anno | ARR target | Customer mix | Pricing strategy |
|---|---|---|---|
| Y2 | €500k-1.2M | Liguria consolidamento + 1 nuova regione SNAI | Stesso pricing Y1, +30% utilization |
| Y3 | €1.5-3.5M | 3-4 regioni SNAI + utility pilot | Premium pricing su PA che ha visto risultati Y1; introduzione tier "enterprise" per utility |
| Y5 | €3-8M | 5-6 regioni + utility scale + B2B cooperative > 50 | Differenziazione tier (base/pro/enterprise); inclusione DaaS pacchetti |
| Y7+ | €10-30M (potenziale, condizionato a HAPS Fase 3) | + NTN wholesale telco + B2C indiretto | Capacity-on-demand pricing |

> **Confidence: low-medium** per Y2-Y3, **speculative** per Y5+.

---

## 7.9 MVP Definition — Percorso 6A Pentema

### 7.9.1 Scope del MVP

Il **MVP** (Minimum Viable Product) del Percorso 6A è definito come segue (riferimento `agents/business-model-strategist.md`):

```
MVP scope (M+0 → M+12):
  • Piattaforma: 1 VTOL ibrido commerciale TRL 8-9 (es. JOUAV CW-30E)
  • Ground segment: 1 GS fissa Pentema + 1 GS mobile (cooperativa)
  • Payload modulare: EO RGB + IR termico + (eventuale) telecom backup
  • Personale: 1 pilota UAS + 1 ingegnere + 1 analyst GIS + 1 PM (4 FTE)
  • Autorizzazioni: SORA SAIL II-III, BVLOS area Pentema, AGCOM (per LTE tattico se applicato)
  • Casi d'uso operativi: UC-001, UC-002, UC-003, UC-005, UC-007 (vedi §7.2.2)
```

### 7.9.2 KPI di successo MVP Y1

| Categoria | KPI | Target | Soglia minima per "MVP success" |
|---|---|---|---|
| Operazioni | Missioni eseguite | ≥ 80 missioni in 12 mesi | ≥ 50 |
| Sicurezza | Incidenti FATAL o major | 0 | 0 (vincolo assoluto) |
| Compliance | Autorizzazione SORA attiva | ✓ | ✓ (necessario) |
| Customer | Contratti pluriennali firmati | ≥ 5 | ≥ 3 |
| Revenue | Revenue Y1 cumulato | €260k centrale (range €220-300k) RECALIBRATED post-Cluster D | ≥ €200k (SyR-Cost-003 hard floor) |
| Satisfaction | NPS stakeholder PA/coop | ≥ 50 | ≥ 40 |
| Service quality | Utilization rate (% ore disponibili fatturate) | ≥ 60% | ≥ 40% |
| Replicabilità | Letters of Interest per scale-up SNAI | ≥ 2 regioni | ≥ 1 regione |

### 7.9.3 Gate decisione post-MVP (M+12)

Al gate M+12, sulla base dei KPI:

- **MVP success (tutti KPI minimi raggiunti)** → **GO scale-up SNAI Liguria + 1 regione aggiuntiva** (Y2-Y3 espansione)
- **MVP partial (rev raggiunto, ma utilization < 40% o NPS < 40)** → **HOLD scale-up**, focus su consolidamento Y2 prima di espansione
- **MVP fail (revenue < €200k)** → **PIVOT del modello** (es. abbandono B2C e doppio focus B2G; o uscita da segmento cooperative che non paga; o re-targeting su difesa duale)

---

## 7.10 Scale-up Roadmap — Fasi 2-5 (Riepilogo)

Coerente con `riferimenti/visione-10-anni.md`, le 5 fasi del progetto:

| Fase | Y | ARR target | Capital intensity cumulato | Action chiave |
|---|---|---|---|---|
| **Fase 1 — MVP Pentema** | Y1 (2026) | €200-400k | €0.7-1.2M | SORA approvata, 5 contratti, Regione anchor |
| **Fase 2 — Scale Liguria + 1 SNAI** | Y2-Y3 (2027-2028) | €1.5-3.5M | €2.5-8M | Flotta 3-8 VTOL/MALE, HALE subscale TRL 5, primo grant PNRR/FESR/Horizon |
| **Fase 3 — HALE prototipo operativo** | Y3-Y6 (2028-2031) | €5-15M | €15-50M | HALE full-scale TRL 7-8, servizio commerciale HAPS pilota, Series A-B €5-15M raised |
| **Fase 4 — Costellazione italiana iniziale** | Y6-Y8 (2031-2033) | €30-80M | €100-500M | 3-10 HAPS operativi, EDF grant, Series B-C €30-100M raised |
| **Fase 5 — Consorzio EU stratospheric layer** | Y8-Y10 (2033-2036) | €100-500M (potenziale) | €500M-2B (small fleet) o **€10-30B (full scale)** | 10-30 HAPS EU, Posizionamento ufficiale "EU sovereign stratospheric layer", IPO o strategic exit |

> **⚠️ Caveat capital intensity Y9-Y10**: la cifra €500M-2B è scenario "small fleet" (5-10 HAPS). Per scala "alternativa Starlink EU" servono **€10-30B** e un programma equivalente IRIS² dedicato (precondizione esterna). Vedi `riferimenti/visione-10-anni.md` §4.

---

## 7.11 Aspetti Trasversali — Sostenibilità e Impatto Sociale

### 7.11.1 Narrativa ESG (Environmental, Social, Governance)

Allineata alle priorità di **Coopfond**, **FESR**, **EIC Accelerator** e **EU Sustainability Taxonomy**:

| Dimensione | Asset Firmamento | Quantificazione (preliminare) |
|---|---|---|
| **Environmental** | Propulsione 100% elettrica/solare; materiali bio-compositi; no detriti spaziali | Riduzione emissioni vs sat lancio o servizio diesel terrestre; ratio TBD |
| **Social** | Modello cooperativo (boundary B1); servizi essenziali a comunità Aree Interne; impact prevenzione rischio idrogeologico (vite salvate, beni preservati) | TBD via metriche ROI sociale Y2 |
| **Governance** | Trasparenza DPIA pubblica; engagement strutturato comunità; conformità GDPR + NIS2; ownership IT stabile (vedi RSK-GEO-002) | Conformità AS/EN 9100 + ISO 9001 + ISO 14001 + ISO/IEC 27001 |

### 7.11.2 Benefici qualitativi (in linea con ENAC AAM BP §4)

In coerenza con l'approccio ENAC AAM BP [^1, §4 Benefici], identifichiamo benefici qualitativi attesi:

1. **Bridge digitale**: riduzione del divario digitale tra centri urbani e Aree Interne
2. **Rivitalizzazione territoriale**: nuovi servizi per comunità montane SNAI
3. **Prevenzione del rischio**: monitoraggio persistente del rischio idrogeologico e antincendio
4. **Ecosistema cooperativo italiano**: rafforzamento della rete Legacoop tramite progetto comune
5. **Filiera aerospace italiana**: contributo all'ecosistema aerospaziale nazionale, possibile partnership con Leonardo/TAS/CIRA
6. **Sovranità tecnologica EU**: contributo di lungo termine al posizionamento italiano nella architettura sovrana europea

---

## 7.12 Risultati Economico-Finanziari (Riepilogo — Dettaglio in Cap. 8)

Il Cap. 8 fornisce il **Quadro Economico** (ex art. 41 D.Lgs. 36/2023), il **Piano Economico-Finanziario** (NPV, IRR, payback, ROI) e la **sensitivity analysis** complete. In questa sezione riportiamo solo il riepilogo per il MVP Y1.

### 7.12.1 Indicatori MVP Y1 (preliminare)

| Indicatore | Valore baseline | Note |
|---|---|---|
| Revenue Y1 (RECALIBRATED post-Cluster D) | €260k centrale (range €220-300k) | Da SyR-Cost-003 + §7.8.2 RECALIBRATED; min €200k hard floor; legacy €355-405k FALSIFICATO |
| OpEx Y1 baseline (pre-+3 FTE regulatory) | €260-480k | Da `agents/financial-cfo-analyst.md` — vedi §8.X per OpEx Y2 €1.18M con +3 FTE regulatory mandatory |
| Margine operativo Y1 (baseline OpEx €260-480k) | **-€220k → +€40k** | In funzione di OpEx mix + utilization; **post-recalibration revenue, margine peggiora rispetto a originale** |
| CapEx Y1 | €700-1200k | Da `agents/financial-cfo-analyst.md` |
| Break-even Y2-Y3 con scale-up | OK se ARR raggiunge €1.5M+ | Da modello finanziario Y2-Y3 |
| Payback Y4-Y5 | OK se ARR raggiunge €3.5M+ | Da modello finanziario Y4-Y5 |

### 7.12.2 Mix finanziamenti raccomandato (preliminare)

| Fonte | % target MVP Y1 | Importo stimato | Status |
|---|---|---|---|
| **Coopfond Cooding Prototypes** | 5-10% | €50k (max) | Da verificare bando 2026 (DR-002) |
| **Coopfond Cooding-Invest** | 15-30% | €150-300k | Da verificare |
| **Regione Liguria FESR/FSE 2021-2027** | 20-40% | €200-400k | Da formalizzare con DGR Liguria (OQ-010) |
| **PNRR Aerospazio / IS4Aerospace** | 0-20% | €0-200k | Possibile via partnership Polito |
| **Equity privato / fondatori** | 20-40% | €200-400k | Da raised |
| **R&D tax credit (L. 160/2019)** | 5-15% | €50-150k | Cumulabile con grant |

> **Confidence: medium** sul mix; **low** sulla concretezza delle singole tranche fino a LoI firmate.

---

## 7.13 Red Team Check — Adversarial Review

Critica condotta dagli agenti `competitor-intelligence` + `business-model-strategist`. Sintesi:

### Critica 1 — "Starlink è già lì, perché aspettare HALE?"
**Razionale critica**: per molte cooperative pilota, Starlink consumer (€50/mese) è una soluzione completa di connettività rurale. Il valore aggiunto di HALE NTN è marginale per il caso d'uso connettività.
**Risposta**: corretto per il caso d'uso connettività consumer puro. Differenziazione Firmamento è (a) latenza bassa per ISR/control industriale, (b) geographic persistence per missioni EO/PC, (c) **sovranità dati** per PA, (d) backup independent in crisi. Connectività cooperative è UC secondario, NON il revenue dominante.

### Critica 2 — "Modello cooperativo è limitazione, non vantaggio"
**Razionale critica**: governance cooperativa = lenta, decisione collegiale, capex limitato. Firmamento può essere appesantita dalla rete cooperative invece di trarne valore.
**Risposta**: corretto in parte. La gestione effettiva della rete è impegnativa. Il valore reale del modello cooperativo NON è velocità decisionale (vero), ma **(a)** access privilegiato a finanziamenti Coopfond (€50k Prototypes + €250k per coop in Cooding-Invest), **(b)** narrativa unica per FESR Aree Interne, **(c)** difesa contro acquisizione tier-1 (vedi RSK-GEO-005, partnership cooperative rende M&A più complesso), **(d)** validazione service-only model. Boundary condition B1: scelta strutturale del progetto, non in discussione.

### Critica 3 — "TAM-IT €100-200M è ottimistico — chi paga davvero?"
**Razionale critica**: il TAM è teorico. La willingness-to-pay reale della PA italiana è notoriamente bassa, con cicli di appalti lunghi. Forse il SOM realistico Y3 è €500k-1M, non €1.5-3.5M.
**Risposta**: confermato. Le stime hanno confidence low. Il SyR-Cost-003 (Y1 €200k) è la soglia minima validatoria; se al M+12 siamo al €100-150k, il modello è in difficoltà ma non morto. La metrica vera è "willingness-to-pay validata via contratti firmati", non "TAM teorico". Action item: M+6 LoI Regione + 2 cooperative + 1 PC = milestone critica.

### Critica 4 — "Aalto/Skydweller può entrare in Italia in 12 mesi e saturare il mercato"
**Razionale critica**: il "vantaggio first mover Italia" è fragile. Aalto (Airbus subsidiary) può aprire JV con Leonardo in 6 mesi e offrire servizi simili a tariffe sotto i costi di Firmamento.
**Risposta**: corretto. Mitigazione: (a) **speed** è difesa — Firmamento deve raggiungere Y1 MVP e Y2 contratti pluriennali prima che Aalto si interessi al micro-mercato italiano, (b) **lock-in con cooperative + PA regionale** crea switching cost per il cliente, (c) **boundary B2 sovereign EU** può diventare argomento difensivo (Aalto è UK-Airbus, non IT). Risk-flag: questo è uno scenario reale; va monitorato come Early Warning Indicator.

### Critica 5 — "Il MVP è troppo ambizioso per Y1 — 5 contratti + 80 missioni"
**Razionale critica**: 5 contratti pluriennali in Y1 in PA italiana è molto difficile (cicli appalto 6-18 mesi). 80 missioni con 1 sola piattaforma + 1 pilota richiede utilization 4-5 missioni/settimana.
**Risposta**: corretto, soglia minima rivedibile. Soglia minima dichiarata in §7.9.2 è 3 contratti e 50 missioni, più realistici. Se al M+9 siamo sotto soglia minima, attivazione fase di urgenza commerciale.

### Critica 6 — "Pricing €150k/anno per servizio EO Regione è inventato"
**Razionale critica**: nessuna Regione italiana ha contrattato prima un servizio EO da operatore privato a queste cifre. Riferimenti di mercato (es. Copernicus business uplift) sono molto più bassi.
**Risposta**: il pricing è preliminare e confidence low. **Aggiornamento M+3 post-audit Cluster D (§7.4.4 + §7.4.5)**: la critica è stata **confermata e quantificata** dall'audit competitor: i benchmark Cluster D pubblici (Planetek Rheticus Puglia, e-GEOS PC Lazio, NHazca monitoraggio frane) indicano pricing servizio EO PA tipicamente €30-80k/anno per area (3-5× sotto baseline §7.8.2). **Azione obbligatoria pre-gate M+10**: ridimensionare pricing baseline §7.8.2 a €60-90k/anno base + €30-60k/anno premium per persistence/sovranità. Revenue Y1 baseline ricalibrato: €220-300k (vs €355-405k originale).

---

**Verdetto Red Team (aggiornato M+3 post-audit Cluster D)**: il capitolo è **strutturalmente solido** ma con **confidence bassa sulle cifre concrete** (TAM, SAM, SOM, pricing) e **gravemente sottoddimensionato** sul rischio competitivo Cluster D (e-GEOS, Planetek, FlyingBasket) — ora riconfigurato in §7.4.4-7.4.7. Le 8 azioni richieste prima del gate M+10:

- ☐ LoI firmata da Regione Liguria entro M+6 (chiusura OQ-010)
- ☐ Workshop validato 10 cooperative pilota entro M+6 (chiusura OQ-011)
- ☐ Benchmark pricing PA italiana confrontato con e-GEOS/Planetek **brutale** entro M+6 — visita diretta + accesso a contratti pubblici Consip/MEPA
- ☐ **Apertura trattativa partnership Planetek + NHazca entro M+6** (§7.4.5.3 azione 3)
- ☐ **Apertura trattativa partnership CIRA entro M+6 per Phase B 6B** (§7.4.5.3 azione 4)
- ☐ Engagement Aalto/Airbus per intelligence + posizionamento difensivo entro M+9
- ☐ Mappa Early Warning Indicator competitivi (vedi `RESERVED-rischi-geopolitici.md`) attivata — includendo FlyingBasket Leonardo investment monitoring
- ☐ **Riconfigurazione pricing baseline §7.8.2 a €60-90k base + €30-60k premium** (§7.4.5.3 azione 6)

---

## 7.14 Riferimenti

[^1]: ENAC, "Business Plan AAM (2021-2030)" — Allegato 2 al Piano Strategico Nazionale Advanced Air Mobility. Source: `fonti/03_AAM-Business-Plan_web-1.md`. **Confidence: high** (ENAC, fonte istituzionale italiana). Specifico: investimenti €1,863.4M ripartiti su 3 wave, benefici qualitativi §4.

[^2]: MIMIT (ex MISE), "Studio di Prefattibilità Aeronautico — Marocco", luglio 2008. Source: `fonti/Progetto_Marocco.md`. **Confidence: medium** (template italiano di prefattibilità, ma datato 2008 — utile per struttura, non per dati di mercato).

[^3]: Aeropolis, "Metodologie e Tecnologie per lo Sviluppo di un Nuovo Velivolo — Analisi dei Costi e Business Plan", Workshop Napoli 24 maggio 2014. Source: `fonti/AnalisiCostiBusinessPlan24_05_14.md`. **Confidence: medium** (workshop didattico, approccio metodologico Alenia).

[^4]: MarkNtel Advisors, "Global HAPS Market Size & Forecast 2024-2030", 2025. **Source:** WebSearch (`riferimenti/ricerche-approfondite.md` §7). **Confidence: low** (fonte commerciale single, non triangolata).

[^5]: Coherent Market Insights, Grand View Research, Credence Research — report commerciali HAPS market 2024-2032. **Confidence: low**.

[^6]: AALTO HAPS Ltd (Airbus subsidiary). Specifico Zephyr 8/S. Sources: Wikipedia, Flight Global, Airbus press releases. **Confidence: medium-high**.

[^7]: SoftBank Sunglider trial 2024. Sources: SoftBank press, Telecom Review Asia, RCR Wireless.

[^8]: Skydweller Aero. Sources: defence-industry.eu, Skydweller news, US Navy press 2025.

[^9]: Aurora Flight Sciences Odysseus (Boeing). Sources: Aurora.aero, Wikipedia.

[^10]: BAE Systems PHASA-35 (Prismatic). Sources: BAE press, Prismatic Ltd, Flight Global.

[^11]: EuroHAPS programme — Thales Alenia Space coordinator, €43M EU contribution, CIRA partner italiano. Sources: TAS press release, Italian Defence Tech.

[^12]: SpaceX Starlink. Sources: SpaceX public data.

[^13]: IRIS² (EU sovereign satcom €10B+). Sources: Commissione UE communications, ESA.

[^14]: NASA SE Handbook Rev 2 (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Riferimento metodologico §4.1.1.2.4 (ConOps + business case derivation).

[^15]: Skill `business-model-strategist` (`/.claude/agents/business-model-strategist.md`); skill `aerospace-market-analyst` (`/.claude/agents/aerospace-market-analyst.md`); skill `epistemic-rigor` (`/.claude/skills/epistemic-rigor/SKILL.md`); skill `feasibility-study-framework` (`/.claude/skills/feasibility-study-framework/SKILL.md`).

[^16]: e-GEOS S.p.A. — Sources: ASI sito ufficiale (https://www.asi.it/en/the-agency/holdings/affiliated-companies/e-geos-s-p-a/); Telespazio press release "e-GEOS to lead consortium for Copernicus Security Service" (https://www.telespazio.com/en/press-release-detail/-/detail/e-geos-satcen); e-GEOS sito corporate (https://www.e-geos.it/en/). **Confidence: high** sui dati corporate (fonti istituzionali), **medium** sui dettagli contrattuali regionali.

[^17]: Planetek Italia S.r.l. — Sources: Rheticus case study Puglia (https://www.rheticus.eu/it/about/casi-di-studio/monitoraggio-satellitare-per-la-mitigazione-del-rischio-idrogeologico-in-puglia); Planetek progetti monitoraggio corpi idrici Puglia (https://www.planetek.it/progetti/monitoraggio_dei_corpi_idrici_sotterranei_della_puglia); OpenCoesione PA tracciato Planetek (https://opencoesione.gov.it/it/dati/soggetti/planetek-italia-srl-04555490723-2/); Fatturato Italia bilancio 2024 €18-22M revenue (https://www.fatturatoitalia.it/planetek_italia_srl_04555490723). **Confidence: high** (fonti corporate + opencoesione PA).

[^18]: NHazca S.r.l. — Sources: NHazca corporate (https://www.nhazca.com/en/); NHazca interferometria sito tecnico (http://www.interferometria.it/); Ingenio profilo azienda (https://www.ingenio-web.it/articoli/aziende/nhazca-srl/). Spin-off Sapienza 2009; founder Mazzanti, Bozzano, Scarascia Mugnozza. **Confidence: high** (fonti corporate verificate).

[^19]: FlyingBasket S.r.l. — Sources: FlyingBasket corporate (https://flyingbasket.com/); Dronewatch Europe "FlyingBasket secures Italy's first LUC" (https://www.dronewatch.eu/flyingbasket-secures-italys-first-light-uas-operator-certificate/); Startmag "FlyingBasket conti e business azienda partecipata Leonardo" (https://www.startmag.it/smartcity/flyingbasket-ecco-conti-e-business-dellazienda-di-droni-partecipata-da-leonardo/); Quadricottero News droni cargo pilot rifugi alpini (https://www.dronezine.it/457350/droni-cargo-in-quota-in-italia-in-alto-adige-il-primo-progetto-pilota-per-rifornire-i-rifugi-alpini/). **Confidence: high** (fonti corporate + stampa specializzata). Investimento Leonardo 2024 confermato.

[^20]: Skyrobotic S.p.A. — Sources: Skyrobotic corporate (http://www.skyrobotic.com/company/?lang=it); Italeaf Group (http://www.italeaf.com/?p=5476&lang=it); Specchio Economico intervista Michele Feroli (https://www.specchioeconomico.com/speciali/2163-speciale-droni-michele-feroli-skyrobotic-anche-sotto-i-25-chili-i-droni-aiutano-molto-i-professionisti). **Confidence: medium-high**.

[^21]: Aermatica3D S.r.l. — Sources: Aermatica corporate (https://www.aermatica.com/); LinkedIn profilo (https://it.linkedin.com/company/aermatica3d). Prima ENAC autorizzazione scenari critici industriali e urbani. **Confidence: high** (fonti corporate dichiarate).

[^22]: Telespazio S.p.A. — Sources: Telespazio corporate Italia (https://www.telespazio.com/en/italy); Fatturato Italia bilancio 2024 €317.8M revenue + Gruppo €701M revenue 2023 (https://www.fatturatoitalia.it/telespazio_spa-01366520284); AIAD aziende federate (https://aiad.it/aziende-federate/telespazio-2025/?lang=en). **Confidence: high** (fonti pubbliche corporate + ufficio camerale).

[^23]: CIRA — Centro Italiano Ricerche Aerospaziali. Sources: CIRA corporate (https://www.cira.it/); Wikipedia CIRA (https://it.wikipedia.org/wiki/Centro_italiano_ricerche_aerospaziali); EREA membership (https://erea.org/members/cira/); AIAD federate (https://aiad.it/aziende-federate/cira-centro-italiano-ricerche-aerospaziali-2024/?lang=en). Già citato Cap. 6 come partner R&D HAPS. **Confidence: high** (fonti istituzionali).

[^24]: Portali pubblici appalti italiani — MEPA Consip (https://www.sosmepa.it/public/rdo-valore.htm); InfoGareWeb banca dati appalti (https://infogareweb.it/); Appalti Liguria (https://appaltiliguria.regione.liguria.it/); Trasparenza AMAT Milano esempio RDO drone monitoring (https://trasparenza.amat-mi.it/archivio11_bandi-gare-e-contratti_0_1061331_876_1.html); Regione Abruzzo acquisto droni MEPA (https://www.regione.abruzzo.it/content/impegno-di-spesa-acquisto-attraverso-il-mepa-di-n-5-droni-dji-movic-e-accessori-necessari-il). **Confidence: low-medium** sui pricing dedotti (gare campione non sistematiche).

[^25]: e-GEOS Copernicus EMS 4° rinnovo €36M 2023-2029 — Sources: SpaceEconomy 360 "Emergency Management Service e-Geos resta alla guida" (https://www.spaceconomy360.it/competenze-e-lavoro/emergency-management-service-e-geos-resta-alla-guida-del-consorzio-ue/); ANSA "e-GEOS confermata alla guida servizi emergenza satellitare" (https://www.ansa.it/canale_scienza/notizie/spazio_astronomia/2023/03/08/e-geos-confermata-alla-guida-di-servizi-emergenza-satellitare_2c022f0e-0350-4be1-b24c-2358955ee390.html); SpaceNews "Italy's e-Geos Wins Contract For Copernicus Imagery" (https://spacenews.com/italys-e-geos-wins-contract-for-copernicus-imagery/). **Confidence: high** (multiple sources triangulate).

[^26]: e-GEOS contratto PC Lazio (2021+) — Sources: Telespazio press release "Emergency response: e-GEOS will supply satellite maps to Civil Protection Department of Lazio Region" (https://www.telespazio.com/en/news-and-stories-detail/-/detail/emergency-e-geos-lazio); SpacEconomy 360 (https://www.spaceconomy360.it/software-e-applicazioni/mappe-satellitari-a-servizio-delle-emergenze-e-geos-in-campo-per-la-protezione-civile-del-lazio/); Italicom (https://www.italicom.net/primo-piano/e-geos-fornira-mappe-satellitari-alla-protezione-civile-della-regione-lazio/). Valore contratto NON disclosed pubblicamente — stima €100-300k/anno dedotta da scala servizio. **Confidence: medium** (esistenza contratto verificata; pricing dedotto).

[^27]: e-GEOS S.p.A. bilancio fatturato 2023 €68.85M revenue — Sources: ReportAziende (https://www.reportaziende.it/egeos_spa_mt_01032180778); Fatturato Italia (https://m.fatturatoitalia.it/e_geos_spa-01032180778); Ufficio Camerale (https://www.ufficiocamerale.it/8093/e-geos-spa). Net profit 2023 €1.61M. **Confidence: high** (fonti ufficio camerale).

---

## 7.15 Note di chiusura del capitolo

Il Cap. 7 è **bozza M+3 (con fix Cluster D applicato)**, in linea con il framework italiano (ENAC AAM BP + MIMIT + Aeropolis) e con la metodologia NASA SE per il business case. Le **debolezze principali** dichiarate onestamente:

1. **Confidence bassa** sulle stime quantitative (TAM, SAM, SOM, pricing) — DR-012 audit-rigore-epistemico.md aperto
2. **Validazione esterna mancante** sui pricing PA — Action item M+6 (benchmark Cluster D §7.4.4.2)
3. **MVP ambizioso** ma con soglia minima dichiarata realistica (3 contratti, 50 missioni)
4. **Boundary conditions B1+B2 esplicitate** — il modello service-only e l'obiettivo EU sovereign non sono in discussione, ma sono **vincoli** che richiedono coerenza di tutti i Cap. 6-7-8
5. **Cluster D Service Incumbent IT** (§7.4.4-7.4.7): identificato come vero competitor Y1 in audit avversariale maggio 2026; **3 dei 4 pilastri vantaggio competitivo** (§7.5.1) sono **non difendibili vs Cluster D**; pricing baseline §7.8.2 da ridimensionare a benchmark Cluster D entro M+6 prima del gate G3

**Prossimi step richiesti** (in ordine di criticità, aggiornati post-audit Cluster D):

1. **LoI Regione Liguria** entro M+6 (chiude OQ-010, valida anchor customer)
2. **Workshop strutturato cooperative pilota** entro M+6 (valida 10 coop come utenti-pilota)
3. **Benchmark pricing PA italiana brutale Cluster D** (e-GEOS, Planetek, NHazca via accesso a contratti Consip/MEPA + interviste dirette) entro M+6 — falsifica/valida §7.4.4.2
4. **Apertura trattativa partnership Planetek (D2) + CIRA (D8)** entro M+6 — §7.4.5.3 azioni 3-4
5. **Riconfigurazione pricing baseline §7.8.2** a benchmark Cluster D entro M+6 (€60-90k base + €30-60k premium)
6. **Strutturazione giuridica modello cooperativo** entro M+12 — convertire pilastro #2 §7.5.1 da soft switching cost a moat legalmente vincolante
7. **Coopfond verifica bando 2026** entro M+1 (chiude DR-002)
8. **Update Cap. 7** post-validazione esterna → versione M+9 per gate M+10

**Versionamento Cap. 7**:
- v0.5 (M+3, capitolo originale): baseline ipotetica con confidence low-medium; Cluster D non considerato
- **v0.6 (M+3 fix Cluster D, presente versione): aggiunta §7.4.4-7.4.7 Cluster D + riconfigurazione §7.5.1 pilastri + caveat §7.0**
- v0.7 (M+6): post-LoI + workshop + benchmark Cluster D + apertura trattative D2/D8, confidence medium
- v0.9 (M+9): post-pricing riconfigurato + 3 contratti reali firmati, confidence medium-high
- v1.0 (M+10): congelato per gate review

Il capitolo è chiuso al M+3 (versione fix Cluster D) con verdetto Red Team **OK con 8 action items**.
