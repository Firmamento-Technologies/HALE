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
3. **Vantaggio competitivo difendibile** poggia su 4 pilastri: (i) specializzazione geografica Aree Interne IT, (ii) modello cooperativo, (iii) sostenibilità + narrativa ESG, (iv) approccio incrementale VTOL → MALE → HALE che produce asset riusabili.
4. **MVP Y1 (Percorso 6A Pentema)**: budget €700-1100k, target revenue Y1 €200-400k da 3-5 contratti pluriennali con PA + cooperative. Sostenibilità break-even Y3-Y4 dopo scale-up SNAI Liguria.
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

### 7.4.4 Concorrenti VTOL commerciali — Tier 3 per Percorso 6A

Per il Percorso 6A baseline (VTOL pilota), Firmamento **utilizza** piattaforme commerciali (es. JOUAV CW-30E), non concorre con i vendor. I concorrenti **operativi** del Percorso 6A sono:

| Operatore IT | Categoria | Posizione | Minaccia per 6A |
|---|---|---|---|
| **ItaliaMeteo + Servizi droni regionali** | EO + monitoraggio PA | Operatori incumbent in alcune regioni | Media — accesso preferenziale a PA esistenti |
| **Imprese ingegneria droni commerciali** (es. Dronebee, FlyingBasket) | Servizi mapping commerciali | Mercato frammentato | Bassa — focus diverso (commerciale, no SNAI) |
| **Carabinieri / VVF flotte UAS interne** | Operazioni di emergenza | Capacità interna PA | Bassa — non concorrono ma sono "clienti potenziali" |

---

## 7.5 Posizionamento Firmamento Technologies

### 7.5.1 4 pilastri del vantaggio competitivo

Il posizionamento di Firmamento è giustificato da **4 pilastri di differenziazione difendibile**:

1. **Specializzazione geografica Aree Interne italiane**
   - Focus esclusivo SNAI Liguria + scale-up SNAI nazionale
   - Vantaggio "first mover" + reti di rapporti istituzionali consolidate
   - Difensibile vs Tier 1 globali (Zephyr/Skydweller non sono interessati a micro-mercati regionali)

2. **Modello cooperativo Legacoop (boundary condition B1)**
   - 10 cooperative pilota come utenti + co-progettisti
   - Community ecosystem → barrier to entry per competitor (no easy replication of cooperative trust)
   - Allineamento valoriale con PA regionale + SNAI mission

3. **Sostenibilità + narrativa ESG**
   - Propulsione 100% solare (HALE) / elettrica (VTOL)
   - Materiali bio-compositi (fibra di lino) per strutture secondarie
   - Carbon footprint operativo basso vs alternative satellitari (no detriti spaziali)
   - Storia narrativa forte per finanziatori ESG-aware (FESR, EIC, ESG-funds)

4. **Approccio incrementale VTOL → MALE → HALE**
   - Riduzione progressiva del rischio tecnologico (TRL 8-9 commerciale → R&D HALE)
   - Asset riusabili: ground segment, data governance, brand, competenze, autorizzazioni regolatorie
   - Capital efficiency superiore vs concorrenti "HAPS-only" (es. Zephyr) che non hanno revenue intermedio
   - **Falsifying observation**: se il Percorso 6A non genera revenue Y1 ≥ €200k entro M+12, il "ladder" è interrotto e gli investitori per Phase B 6B non sono convinti.

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
| **Cost Structure** | CapEx Y1: €700-1200k (vedi Cap. 8 dettaglio). OpEx Y2 run-rate: €260-480k/anno. Costo capitale fisso (asset + cert + privacy + training). Costo variabile per ora-volo: €200-500/ora |

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

### 7.8.2 Pricing baseline MVP Y1 (preliminare, confidence low)

Lo Studio adotta i seguenti **pricing baseline** per il MVP Y1, da validare con LoI/contratti effettivi:

| Linea servizio | Cliente | Pricing baseline Y1 | Volume target Y1 | Revenue Y1 stimato |
|---|---|---|---|---|
| Monitoraggio frane settimanale Liguria interna | Regione Liguria | Canone €150k/anno | 1 contratto | €150k |
| Antincendio boschivo stagione estate | PC Liguria + 1 Ente Parco | Canone €60k stagione + €5k/event verificato (max 5 event) | 1 PC + 1 Parco | €85k |
| Backup connettività emergenza | PC Liguria | On-demand €5-15k/event (max 5) + €20k retainer | 1 contratto retainer | €45-95k |
| Mapping agricolo cooperative | 3 cooperative agricole pilota | Abbonamento DaaS €10k/anno per cooperativa | 3 contratti | €30k |
| Mapping infrastrutture stradali Comune | Comune Torriglia + 2 altri Comuni SNAI | Servizio €15k per Comune | 3 contratti | €45k |
| **Totale revenue Y1 baseline** | | | | **€355-405k** |

> **Falsifying observation §7.8.2**: se entro M+9 non sono firmati ≥ 3 contratti pluriennali con valore aggregato ≥ €200k, il SyR-Cost-003 (revenue Y1 ≥ €200k) è in stato "Failed", e va attivata revisione del modello (es. pivot a more aggressive PA push o pure cooperative agricola). **Probabilità: M, impatto: H**. Mitigazione: engagement intensivo Regione + PC entro M+0-6.

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
| Revenue | Revenue Y1 cumulato | €355-405k baseline | ≥ €200k (SyR-Cost-003) |
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
| Revenue Y1 | €355-405k | Da SyR-Cost-003 + §7.8.2 |
| OpEx Y1 | €260-480k | Da `agents/financial-cfo-analyst.md` |
| Margine operativo Y1 | -€125k → +€145k | In funzione di OpEx mix + utilization |
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
**Risposta**: il pricing è preliminare e confidence low. Action item: benchmark contrattualistico con (a) operatori EO che già lavorano con Regioni IT (e-GEOS, Planetek, NHazca), (b) analoghi PA per servizio monitoraggio (es. SiCura Liguria, sistema allerta nazionale). Validazione tramite LoI prima del gate M+10.

---

**Verdetto Red Team**: il capitolo è **strutturalmente solido** ma con **confidence bassa sulle cifre concrete** (TAM, SAM, SOM, pricing). Le 6 azioni richieste prima del gate M+10:

- ☐ LoI firmata da Regione Liguria entro M+6 (chiusura OQ-010)
- ☐ Workshop validato 10 cooperative pilota entro M+6 (chiusura OQ-011)
- ☐ Benchmark pricing PA italiana confrontato con e-GEOS/Planetek entro M+6
- ☐ Engagement Aalto/Airbus per intelligence + posizionamento difensivo entro M+9
- ☐ Mappa Early Warning Indicator competitivi (vedi `RESERVED-rischi-geopolitici.md`) attivata
- ☐ Pricing test su almeno 2 contratti reali entro M+9

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

---

## 7.15 Note di chiusura del capitolo

Il Cap. 7 è **bozza M+3**, in linea con il framework italiano (ENAC AAM BP + MIMIT + Aeropolis) e con la metodologia NASA SE per il business case. Le **debolezze principali** dichiarate onestamente:

1. **Confidence bassa** sulle stime quantitative (TAM, SAM, SOM, pricing) — DR-012 audit-rigore-epistemico.md aperto
2. **Validazione esterna mancante** sui pricing PA — Action item M+6 (benchmark)
3. **MVP ambizioso** ma con soglia minima dichiarata realistica (3 contratti, 50 missioni)
4. **Boundary conditions B1+B2 esplicitate** — il modello service-only e l'obiettivo EU sovereign non sono in discussione, ma sono **vincoli** che richiedono coerenza di tutti i Cap. 6-7-8

**Prossimi step richiesti** (in ordine di criticità):

1. **LoI Regione Liguria** entro M+6 (chiude OQ-010, valida anchor customer)
2. **Workshop strutturato cooperative pilota** entro M+6 (valida 10 coop come utenti-pilota)
3. **Benchmark pricing PA italiana** (e-GEOS, Planetek, ARPA) entro M+6
4. **Coopfond verifica bando 2026** entro M+1 (chiude DR-002)
5. **Update Cap. 7** post-validazione esterna → versione M+9 per gate M+10

**Versionamento Cap. 7**:
- v0.5 (M+3, presente capitolo): baseline ipotetica con confidence low-medium
- v0.7 (M+6): post-LoI + workshop, confidence medium
- v0.9 (M+9): post-benchmark + 3 contratti reali, confidence medium-high
- v1.0 (M+10): congelato per gate review

Il capitolo è chiuso al M+3 con verdetto Red Team **OK con 6 action items**.
