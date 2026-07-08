# 01 — Connettività da piattaforma aerea per le Aree Interne (caso pilota Pentema)

> **Analisi bottom-up — Ripartenza da zero dal SERVIZIO**
> Firmamento Technologies — progetto HALE
> Autore: Telecom / NTN Payload Expert (Claude) — 2026-07-08
> Skill applicate: `link-budget-calculator`, `epistemic-rigor`
> Domanda: *può una piattaforma aerea a basso costo portare connettività utile a una valle/borgo montano come Pentema, facendo "un po' il mestiere del satellite ma limitato"? E qual è il requisito minimo di QUOTA e AUTONOMIA?*

**Nota di metodo (rigore epistemico).** Questo documento NON assume le conclusioni pregresse del repo (impianto 6A/6B, scelta HALE/JOUAV). Riparte dalla fisica e dal fabbisogno. Ogni numero porta `[fonte | anno | tipo | confidenza]`. La classe di piattaforma è variabile aperta. La sezione 8 è una falsificazione obbligatoria dell'ipotesi.

---

## 0. Sintesi e verdetto

**Fisica: facile. Economia: perde.** Il link RF da quota verso un borgo montano **chiude con ampio margine** in tutte le architetture (dal drone a 300 m all'HALE a 20 km) usando bande sub-6 GHz. Anche l'**uplink da smartphone** (0.2 W) chiude — cosa che il satellite LEO/GEO fatica a fare — perché la piattaforma è *vicina*. Quindi, sul piano puramente radio, una piattaforma aerea **può davvero fare "un po' il mestiere del satellite"** (direct-to-device di prossimità).

I vincoli veri **non sono il link budget**, sono tre:
1. **Geometria LOS in montagna** — servono quote elevate per "vedere oltre le creste"; è esattamente questo che una piattaforma alta compra e un satellite ha per definizione.
2. **Persistenza (ore/giorno)** — la connettività è un servizio *always-on*; la persistenza è precisamente ciò che manca alle piattaforme economiche (tranne l'aerostato tethered, che però è basso e locale).
3. **Costo marginale vs Starlink** — Starlink spalma il CapEx su una costellazione globale e connette Pentema a ~€40-75/mese *oggi*; l'aereo-per-un-borgo concentra tutto il CapEx su qualche decina di persone.

**Verdetto:** per la **sola connettività broadband** di Pentema, la piattaforma aerea **non è competitiva** con Starlink + ponte radio da Torriglia. Diventa razionale **solo** cambiando la domanda: (a) **resilienza d'emergenza multi-valle** per Protezione Civile, (b) **direct-to-device di area vasta** aggregando molti borghi, (c) **capacity surge per eventi**, (d) abbinata a **EO/monitoraggio**. Dettaglio in §9.

---

## 1. La domanda e il metodo

Confrontiamo bottom-up 4 regimi di quota per un servizio di connettività a un borgo/valle montana:

| # | Regime | Quota | Piattaforma tipica | Persistenza intrinseca |
|---|---|---|---|---|
| 1 | Bassa quota / relay | 100–500 m AGL | Aerostato/drone tethered, multirotore | Tethered: alta (giorni). Free-flight: min |
| 2 | Loiter tattico | 1–4 km | VTOL / fixed-wing (classe <25–150 kg) | Media (ore per sortita) |
| 3 | Media quota (MALE) | 5–9 km | MALE endurance | Alta (20–40 h) ma costo/regolatorio elevati |
| 4 | Stratosferico (HALE) | ~20 km | UAV solare / aerostato stratosferico | Molto alta (mesi) *se funziona* |

Per ciascuno: geometria di copertura reale in terreno montano, tipo di servizio, ore/giorno realistiche, capacità aggregata, ordine di grandezza costo.

---

## 2. Contesto fattuale di Pentema

Fonte primaria: sub-analisi territoriale (triangolata) + Dossier SNAI locale.

| Dato | Valore | `[fonte | anno | tipo | confidenza]` |
|---|---|---|
| Quota borgo | **839 m s.l.m.** | `[Wikipedia/Parco Antola/Wikidata | 2024 | enciclopedico | alta]` |
| Coordinate | ~44.533°N, 9.133°E | `[Wikidata | 2024 | enciclopedico | media]` |
| Morfologia | Su **versante di Monte Prelà (1.408 m)**, non fondovalle stretto; case "a pettine" sul pendio | `[Parco Antola/Wikipedia | 2024 | istituzionale | alta]` |
| Rilievo dominante | **Monte Antola 1.597 m** a N/NE | `[Wikipedia | 2024 | enciclopedico | alta]` |
| Residenti stabili | **~23** (una dozzina permanenti) | `[Mentelocale/Wikipedia | 2022-24 | stampa | media-alta]` |
| Stagionalità | **Presepe di Pentema** (dic-gen): migliaia di visitatori | `[La Mia Liguria | 2024 | istituzionale | media]` |
| Torriglia capoluogo | ~2.200 ab., ~10 km, **FTTH Open Fiber (BUL) attiva** | `[comune Torriglia/Open Fiber | 2024-25 | istituzionale | media-alta]` |
| Fibra a Pentema (frazione) | **Non confermata FTTH**; probabile FWA o area bianca | `[portali copertura | 2024 | commerciale | bassa-media]` |
| Mobile 4G/5G puntuale Pentema | **Non verificato a livello di frazione**; dato d'area SNAI ottimistico (pop-pesato su Torriglia) | `[GAP dichiarato]` |
| Starlink | **Disponibile nazionale**, incl. montagna | `[starlink.com/it | 2025-26 | primario | alta]` |

**Implicazioni chiave per la geometria.**
- Pentema è **su versante, non incassato in fondovalle stretto**: verso una piattaforma *alta* l'angolo di elevazione resta buono anche con grande offset laterale (≈34° a 30 km orizzontali, ≈22° a 50 km per HALE 20 km), quindi **l'ombreggiamento orografico verso una HAPS è marginale** (salvo settore azimutale schermato dalla cresta Prelà/Antola). `[stima geometrica | media]`
- Verso una piattaforma *bassa* (poche centinaia di m – pochi km), la LOS è **fortemente vincolata dalla cresta**: va posizionata sopra/oltre la linea di cresta o sull'asse valle.
- **Un borgo da ~23 abitanti non regge un business case di connettività**: ha senso **solo come pilota dimostrativo**, con scala reale sull'area SNAI Antola-Tigullio (16 comuni, ~16.700 ab.). `[Dossier SNAI | 2021-23 | ufficiale | alta]`

> **Red flag epistemica.** I documenti pregressi del repo richiedono per il ground segment a Pentema "una connessione internet di backhaul di almeno **10 Mbps**" `[da revisionare/Relazione Tecnica Comparativa | riga 27 | interno]`. Questo implica che a Pentema **la connettività esiste già o è ottenibile** — il che indebolisce la premessa "Pentema è senza connettività".

---

## 3. Geometria di copertura in terreno montano

La copertura **geometrica** (LOS) e la copertura **operativa** (SNR sufficiente) sono cose diverse (Errore 6 della skill epistemic-rigor). In montagna il collo di bottiglia è la LOS.

### 3.1 Orizzonte radio geometrico (4/3 earth, utente h=2 m)

| Regime | Quota | Orizzonte geometrico (terreno piatto) |
|---|---|---|
| Aerostato | 300 m | **77 km** |
| VTOL | 2 km | **190 km** |
| VTOL | 4 km | **266 km** |
| MALE | 7 km | **351 km** |
| HALE | 20 km | **589 km** |

L'orizzonte teorico è enorme già a bassa quota. **Ma in montagna non conta l'orizzonte piatto: contano le creste.**

### 3.2 Clearance orografico — la quota che serve per "vedere oltre la cresta"

Per servire un utente in una valle adiacente, schermato da una cresta di altezza `h_ridge` sopra di lui a distanza `d_ridge`, la piattaforma a distanza orizzontale `D` deve stare a quota minima ≈ `D · h_ridge/d_ridge`.

| Cresta schermante | D=10 km | D=20 km | D=30 km | D=50 km |
|---|---|---|---|---|
| 200 m @ 1 km | 2.0 km | 4.0 km | 6.0 km | 10 km |
| 400 m @ 1 km | 4.0 km | 8.0 km | 12 km | 20 km |
| 600 m @ 2 km | 3.0 km | 6.0 km | 9.0 km | 15 km |
| 800 m @ 2 km | 4.0 km | 8.0 km | 12 km | 20 km |

*(quota minima piattaforma, in km, per LOS a quella distanza orizzontale)*

**Lettura — è il cuore della questione "mestiere del satellite":**
- Per servire **solo la propria valle** (utente in LOS diretta col borgo): basta stare **sopra il borgo**, 300 m–2 km.
- Per servire utenti **oltre creste di 400–800 m a 20–50 km** (copertura di *area vasta multi-valle*): serve quota di **8–40 km**, cioè il regime **MALE/HALE**. È esattamente ciò che fa un satellite: sta così in alto da vedere tutti sopra le creste. Una piattaforma bassa **non** fa il mestiere del satellite; una piattaforma alta sì, ma paga in costo/rischio.

### 3.3 Slant range al bordo cella (per link budget)

| Regime | elev 10° | elev 5° |
|---|---|---|
| VTOL 2 km | 11.5 km | 22.9 km |
| VTOL 4 km | 23.0 km | 45.9 km |
| MALE 7 km | 40.3 km | 80.3 km |
| HALE 20 km | 115 km | **229 km** |

Il valore HALE a 5° elev = 229 km coincide con 3GPP TR 38.811 §5.3.3 `[3GPP TR 38.811 v15 | 2019 | norma | alta]`.

---

## 4. Link budget di prima approssimazione

Metodo: free-space (Friis) + margini atmosferici/clutter, `C/N0 = EIRP − L_tot + G/T − k`, `SNR = C/N0 − 10log10(BW)` (skill `link-budget-calculator`, coerente con Allegato A.7 e ITU-R P.525/P.618). Script riproducibile: `analisi-bottom-up/lb_bottomup.py`. Sub-6 GHz ⇒ rain fade trascurabile in zona K Liguria (<0.05 dB a 99.99% a 2.1 GHz, cfr. A.7 §6.2). `[ITU-R P.618-14 | 2023 | norma | alta]`

**Assunzioni dichiarate** (confidenza media salvo diverso avviso): handheld 0 dBi, NF 7 dB (Tsys≈1450 K) ⇒ G/T ≈ −31.6 dB/K; piattaforma RX beam 10 dBi, NF 3 dB ⇒ G/T ≈ −18.6 dB/K; EIRP piattaforma modesto e compatibile con payload leggero (13–23 dBW).

### 4.1 Downlink piattaforma → smartphone (cell-on-wings)

| Scenario | Freq | Dist | EIRP | L_tot | C/N0 | SNR | Verdetto |
|---|---|---|---|---|---|---|---|
| VTOL 2 km, r=15 km | 700 MHz | 15 km | 13 dBW | 116 dB | 94.1 | **27.1 dB** | OK ampio |
| VTOL 2 km, r=30 km | 700 MHz | 30 km | 13 dBW | 122 dB | 88.1 | **21.1 dB** | OK |
| VTOL 2 km, r=15 km | 2.6 GHz | 15 km | 16 dBW | 128 dB | 84.7 | **14.7 dB** | OK |
| MALE 7 km, r=50 km | 700 MHz | 50 km | 16 dBW | 127 dB | 85.7 | **18.7 dB** | OK |
| HALE 20 km, r=55 km | 700 MHz | 55 km | 20 dBW | 128 dB | 88.8 | **21.8 dB** | OK |
| HALE 20 km, r=36 km | 2.6 GHz | 36 km | 23 dBW | 137 dB | 83.1 | **13.1 dB** | OK |

Tutti gli scenari chiudono con SNR ≥ 13 dB (sufficiente per 16-64QAM). **Il downlink non è un problema a nessuna quota.**

### 4.2 Uplink smartphone (23 dBm) → piattaforma — *il presunto collo di bottiglia*

| Scenario | Freq | Dist | C/N0 | SNR (BW 1.4 MHz) | Verdetto |
|---|---|---|---|---|---|
| r=15 km | 700 MHz | 15 km | 87.1 | **25.7 dB** | OK ampio |
| r=30 km | 700 MHz | 30 km | 81.1 | **19.6 dB** | OK |
| r=50 km | 700 MHz | 50 km | 75.7 | **14.2 dB** | OK |
| r=15 km | 2.6 GHz | 15 km | 74.7 | **13.3 dB** | OK |
| HALE r=55 km | 700 MHz | 55 km | 74.8 | **19.3 dB** (BW 360 kHz) | OK |

**Risultato chiave e controintuitivo.** L'uplink handheld **chiude ovunque** (SNR 14–26 dB). Questo è il **vantaggio strutturale della piattaforma aerea sul satellite**: a 20 km il path loss è ~20–30 dB minore che a LEO 550 km e ~65 dB minore che a GEO. Il direct-to-device dal telefono *nudo* (che LEO/GEO fanno solo con enormi antenne satellitari e/o solo in downlink) qui è **facile**. È il senso tecnico di "fare un po' il mestiere del satellite, ma limitato".

### 4.3 Backhaul punto-punto (relay a bassa quota) — piattaforma ↔ dish a terra, 5.8 GHz

| Scenario | Dist | C/N0 | SNR (BW 20 MHz) | Verdetto |
|---|---|---|---|---|
| Aerostato, r=5 km | 5 km | 105.3 | **32.3 dB** | OK ampio |
| VTOL, r=15 km | 15 km | 94.7 | **21.7 dB** | OK |
| VTOL, r=30 km | 30 km | 88.7 | **15.7 dB** | OK |

Un relay a bassa quota può fare da **backhaul aereo** verso un CPE direttivo a terra (es. rilanciare la fibra di Torriglia). Chiude con margine.

### 4.4 IoT LoRa 868 MHz — sensore (14 dBm) → gateway a bordo

| Scenario | Prx | Margine vs sensib. SF12 (−137 dBm) | Verdetto |
|---|---|---|---|
| r=20 km | −101 dBm | **+35.8 dB** | OK ampio |
| r=50 km | −109 dBm | **+27.8 dB** | OK |
| r=80 km | −113 dBm | **+23.7 dB** | OK |

Un gateway LoRa da quota copre **decine di km di raggio** con margine enorme: il caso d'uso **IoT ambientale** (sensori idrogeologici, meteo, frane) è quello dove la piattaforma aerea è tecnicamente più efficiente (pochi bit, tolleranti al ritardo, molti sensori dispersi).

> **Falsifying observation §4.** Se in un test a Pentema l'RSSI misurato a 20–30 km LOS risultasse >15 dB peggiore della predizione free-space (per diffrazione/clutter forestale non modellati), i margini downlink/uplink andrebbero rivisti. Ma i margini attuali (13–35 dB) assorbono gran parte di un simile scarto. **Il rischio-link è basso; il rischio-LOS/orografia e il rischio-persistenza restano i dominanti.**

---

## 5. Confronto bottom-up dei 4 scenari

| Dimensione | 1. Aerostato/drone 100–500 m | 2. VTOL/FW 1–4 km | 3. MALE 5–9 km | 4. HALE ~20 km |
|---|---|---|---|---|
| **Copertura LOS montana** | Solo borgo/valle immediata; schermato dalle creste | Valle + versanti; scavalca creste basse; raggio utile 10–30 km | Area vasta multi-valle; raggio 40–80 km | Regionale; raggio 50–100 km (fino 229 km a 5°) |
| **Servizio erogabile** | Backhaul→CPE, WiFi locale, LoRa gateway, hotspot | Cell-on-wings 4G/5G locale, backhaul, LoRa | Cella 4G/5G d'area, NTN | Cella 4G/5G-NTN persistente, D2C, IoT wide |
| **Capacità aggregata** | 10–100 Mbps (1 backhaul + WiFi) | 20–100 Mbps/settore | 100–300 Mbps multi-beam | 0.1–1 Gbps multi-beam (3GPP NR-NTN) `[TR 38.821 | 2023 | norma | media]` |
| **Ore copertura/giorno** | **Tethered: 24/7** (giorni-settimane). Free-flight: 0.5–1 h | 6–10 h/sortita; per 24/7 servono 2–3 mezzi | 20–40 h/volo → quasi persistente con 1–2 mezzi | Mesi *se il velivolo regge* (inverno 44°N critico) |
| **Persistenza reale** | Alta (tethered) | Bassa senza flotta | Media-alta | Alta ma TRL basso |
| **Ordine di grandezza costo** | **€20–150k** | €0.1–0.9M | **€5–50M+** (Certified) | €5.5–11M R&D → realisticamente ≫€100M a operatività |
| **Maturità/rischio** | TRL 9, basso | TRL 8–9, basso-medio | TRL 8–9 ma regolatorio/costo alti | TRL 4–6, alto (base rate HALE <30%) `[epistemic-rigor base-rate | alta]` |
| **Regolatorio ENAC** | VLOS/tethered semplice | Specific/SORA BVLOS | **Certified** (spazio aereo controllato) | Nuovo framework HAPS |

**Sintesi del confronto.** C'è una **tensione irriducibile**: le architetture *economiche e persistenti* (aerostato tethered) sono *basse* e coprono solo il borgo; le architetture che coprono *area vasta scavalcando le creste* (MALE/HALE) sono *costose e/o immature*. Il VTOL sta in mezzo: economico ma **non persistente** senza flotta. **Nessuna singola architettura economica offre insieme copertura d'area + persistenza 24/7** — che è invece esattamente ciò che Starlink offre di serie.

---

## 6. Requisito minimo di QUOTA e AUTONOMIA per connettività utile

Il requisito **bifurca** secondo l'ambizione del servizio:

**A) Connettività del solo borgo (Pentema stesso).**
- **Quota minima:** ~200–500 m sopra il borgo (LOS diretta al versante abitato).
- **Autonomia minima:** per essere *utile come servizio*, la connettività deve essere **quasi continua**. Ciò impone o **tethered persistente** (aerostato/drone frenato, 24/7) oppure una **flotta** in rotazione. Un singolo VTOL da 6–10 h **non** eroga un servizio di connettività residenziale credibile (copre solo finestre programmate). → **Requisito: tethered 24/7 a bassa quota**, oppure niente.

**B) Connettività di area vasta multi-borgo ("mestiere del satellite").**
- **Quota minima:** **≥ ~8–12 km** per scavalcare le creste appenniniche (400–800 m) e servire utenti a 20–50 km oltre i rilievi (§3.2). Sotto questa quota la copertura resta intra-valle.
- **Autonomia minima:** per un servizio persistente d'area serve **endurance multi-giorno** (MALE ≥24 h in rotazione, o HALE settimane/mesi). Il VTOL è escluso.

**Conclusione sul requisito minimo.** *Se* l'obiettivo è connettività-servizio (always-on), il **minimo realistico è: quota che scavalca le creste (≥8–12 km per l'area vasta; ≥0.2 km per il solo borgo) E persistenza ≥ multi-giorno / tethered 24/7.* Le due condizioni insieme spingono verso **(i) aerostato tethered locale (basso costo, copertura minima)** oppure **(ii) MALE/HALE (copertura d'area, costo/rischio alti)**. La fascia intermedia VTOL a batteria, benché la più finanziabile, **fallisce il requisito di persistenza** per un servizio di connettività continuo (resta ottima per EO a campionamento e per emergenza).

---

## 7. Spettro: quali bande, quale via autorizzativa

Il link budget usa bande sub-6 GHz. Il problema non è la fisica ma **il diritto d'uso dello spettro**. La Delibera AGCOM 93/26/CONS (2026) è istruttiva sul *metodo* (procedura comparativa/beauty contest, avvio→consultazione→assegnazione su ciclo >12 mesi, diritti a scadenza fissa non cedibili per 2 anni, artt. 11/42/62 D.Lgs. 259/2003): **ottenere un proprio diritto d'uso è lento e procedurale — da evitare per un pilota in 6-18 mesi.** `[Delibera 93/26/CONS | 2026 | norma | alta]`

### 7.1 Le vie possibili (dalla più rapida/basso-rischio alla più lenta)

| Via | Banda | Titolare licenza | Idoneità piattaforma aerea | Tempi | Rischio |
|---|---|---|---|---|---|
| **A. Partnership MNO (neutral-host / MOCN / RAN sharing)** | IMT già licenziate all'MNO: 700/800/1800/2600/3700 MHz | **L'MNO** (Firmamento = infrastructure provider) | **Alta** — nessuna nuova licenza; modello Loon/AT&T, FirstNet | **6–12 mesi** (accordo + autorizzazione deployment aereo MIMIT/AGCOM) | **Basso-medio** — dipende da disponibilità MNO + ok deployment aereo |
| **B. Autorizzazione sperimentale MIMIT** | banda a definire, uso locale | Firmamento (temporanea) | Media — **solo pilota/trial** | **~2–4 mesi** | Basso, ma **tetto 6 mesi, ≤3.000 utenti, natura non commerciale** |
| **C. LoRa/868 SRD licence-exempt** | 868 MHz (ERC 70-03) | Nessuno (uso libero) | **Solo IoT/telemetria** (duty cycle 0.1–1%, ERP ~25 mW) | **Immediato** | Basso, ma **non broadband** |
| **D. Deroga emergenza / Protezione Civile** | temporanea MIMIT su evento, o piggyback MNO; PMR VHF/UHF dedicata = **solo fonia** | Autorità pubblica / MNO | Alta *ma solo emergenza* | Rapido in emergenza | Basso (non è business continuativo) |
| **E. WiFi 2.4/5 GHz airborne** | RLAN | Nessuno | **NON conforme** — EN 300 328/301 893 non coprono la base radiante airborne verso terra; Dec. (UE) 2022/179 ammette RLAN solo *in cabina*; la Finlandia vieta 5470-5725 MHz sugli UAS | — | **Alto / di fatto bloccato** |
| **F. NTN MSS diretto (n255 L-band / n256 S-band)** | 2 GHz MSS | **Inmarsat/Viasat + Solaris/EchoStar** (Dec. 626/2008/EC, 18 anni non trasferibili) | Riservata a 2 operatori UE | — | **Non disponibile** per una PMI |
| **G. Autorizzazione HAPS/HIBS dedicata (ITU/AGCOM)** | bande HAPS mm-wave (Art. 1.66A) | Firmamento (individuale) | **Lenta e incerta**; mm-wave ⇒ rain fade | **Anni** | **Alto** — esattamente ciò da evitare |

Fonti: `[ETSI EN 300 328/301 893 | 2019-24 | standard | alta]`, `[Dec. (UE) 2022/179 / Traficom | 2022-23 | decisione UE/regolatore | alta]`, `[ERC-REC 70-03 | 2024 | CEPT | alta]`, `[Dec. 626/2008/EC | 2008 | norma UE | alta]`, `[MIMIT autorizzazioni temporanee | 2025-26 | regolatore | alta sui parametri]`.

### 7.2 L'abilitatore chiave: WRC-23 Risoluzione 213 (HIBS)

Le **HIBS** (HAPS as IMT Base Station) usano **le stesse bande e gli stessi terminali** dell'IMT terrestre — 694-960, 1710-1885, 2500-2690 MHz `[ITU Res. 213 WRC-23 | 2023 | norma ITU | alta]`. Quindi **la licenza terrestre dell'MNO è, in principio, estendibile a una cella aerea nella *sua* banda** — l'utente usa il proprio smartphone senza modifiche. In Italia il costrutto **MOCN/RAN sharing è consolidato e regolato**: accordo **PRISM** TIM–Fastweb+Vodafone (gen 2026, ~15.500 siti, sotto MIMIT+AGCM+AGCOM) e precedente **Zefiro Net** WindTre–Iliad `[Corriere Comunicazioni/Agenda Digitale | 2026 | stampa specializzata | alta]`. **Caveat:** la Res. 213 è pensata per la quota **stratosferica** (18-25 km); per una cella a **bassa quota** non c'è cornice HIBS dedicata (ma resta la stessa licenza MNO), e il deployment aereo richiede comunque ok MIMIT/AGCOM + coordinamento ENAC/ENAV — l'implementazione nazionale HIBS è **immatura**. `[analisi regolatoria | 2026 | media]`

### 7.3 Raccomandazione spettro

Disaccoppiare due tracce:
1. **Pilota/dimostratore Pentema → Via B (sperimentale MIMIT, ~2–4 mesi)** + eventuale **layer IoT 868 MHz (Via C)** subito. Copre il trial senza attendere accordi complessi.
2. **Servizio a regime → Via A (neutral-host / MOCN con un MNO che porta il proprio spettro licenziato).** Così **lo spettro non è mai un rischio di Firmamento ma un asset del partner**; abilitato in prospettiva da HIBS/Res. 213 per la quota alta. Nessuna nuova assegnazione AGCOM.
3. **Emergenza/Protezione Civile → Via D** (deroghe rapide), tenuta separata dal business continuativo. È anche il caso d'uso più difendibile.
4. **Evitare** la Via E (WiFi airborne, non conforme), la Via F (MSS bloccata su Inmarsat/EchoStar) e la Via G (HAPS dedicata ITU, pluriennale) come basi del servizio.

> **Falsifying observation §7.** Se nessun MNO italiano accetta un accordo neutral-host aereo entro ~18 mesi (fabbisogno di copertura su borghi da 23 abitanti nullo; per eventi/emergenza preferiscono COW terrestri o Starlink D2C), la Via A crolla e resta solo la Via B (pilota ≤6 mesi, non commerciale). **Questa è la dipendenza critica del percorso connettività a regime.**

---

## 8. Falsificazione (obbligatoria): quando l'aereo NON sostituisce nemmeno "un po'" il satellite

Ipotesi da falsificare: *"una piattaforma aerea economica compete anche solo un po' con Starlink/terrestre per la SOLA connettività di Pentema."*

### 8.1 Le alternative già disponibili oggi

| Soluzione | CapEx borgo | OpEx/canone | Prestazioni | Disponibilità | `[fonte | anno | conf.]` |
|---|---|---|---|---|---|
| **Starlink** (LEO) | ~€0–349 kit (o €10/mese noleggio) | **€29–75/mese** | 100–250 Mbps, **20–60 ms** | **Oggi, online** | `[TechPost/Selectra/Starlink | 2025-26 | primario+stampa | alta]` |
| **Eutelsat Konnect** (GEO Ka) | installazione | €29.90–69.90/mese | 16–50 Mbps, **>600 ms**, data cap | Oggi | `[offerta-internet/pluscom | 2025 | aggregatore | media]` |
| **EOLO FWA** | rateizzata nel canone | **~€24.90/mese** | fino 300 Mbps, 20–40 ms | Oggi *se LOS a BTS* | `[EOLO/Selectra | 2025-26 | primario | media-alta]` |
| **Ponte radio dedicato** Torriglia→Pentema + WiFi | **~€10–50k** una tantum | backhaul €30–100/mese | 1.4 Gbps radio, 1–5 ms | 1–3 mesi *se LOS* | `[pontiradiowifi/Ubiquiti | 2025-26 | distributori | media]` |
| **Fibra Infratel** (aree bianche, Piano 1 Giga) | **€0 al committente** (PNRR) | canone ISP | fino 1 Gbps | Quando arriva (Liguria <70% target, deadline giu-2026 mancata) | `[innovazione.gov.it/CorCom | 2025-26 | primario+stampa | media-alta]` |
| **Piattaforma aerea "economica"** | **€100k–1.000k+** | ops/energia/spettro/BVLOS 24/7 | variabile | **Mai, prima di anni** | `[stima interna | 2026 | media]` |

### 8.2 Il colpo da KO (matematica del costo marginale)

Pentema ≈ 30 nuclei (residenti + seconde case).

| Soluzione | CapEx totale | OpEx/anno | Costo/nucleo/anno (5 anni) | Quando |
|---|---|---|---|---|
| Starlink comunitario (1–2 terminali Business + mesh) | ~€10–20k | ~€6–10k | **~€400–600** | Oggi |
| Ponte radio da Torriglia + WiFi | ~€10–50k | ~€2–5k | **~€300–700** | 1–3 mesi |
| Piattaforma aerea | **€100k–1M** | ops elevate | **€7k–300k+** | Anni |

Il **costo marginale** di collegare un altro utente su Starlink è ~€50/mese su una costellazione da 6.000+ satelliti già in orbita, ammortizzata su milioni di clienti. Il costo marginale di collegare Pentema con una piattaforma aerea è **l'intero programma**: la costellazione *spalma*, l'aereo-per-un-borgo *concentra*. Su ogni metrica (€/famiglia, €/Mbit, time-to-service, rischio esecuzione) **l'aereo perde di 1–3 ordini di grandezza**. Aggravante: Starlink è ordinabile stasera; l'aereo deve prima superare SORA/BVLOS ENAC, spettro AGCOM, energy balance invernale, link budget NTN.

**La debolezza reale di Starlink a Pentema** (valle, versanti boscati) è l'**ostruzione parziale del cielo** (FOV cono ~100°, usabile da ~20° sopra l'orizzonte; fogliame/creste ⇒ micro-drop) `[Starlink Help | 2025 | primario | alta]`. **Ma si risolve alzando la parabola su un palo/tetto con vista cielo** — non giustifica una piattaforma da €100k–1M.

**→ Falsificazione riuscita:** l'ipotesi è **respinta**. Per la sola connettività broadband, le condizioni in cui la piattaforma aerea NON compete affatto sono **la norma**, non l'eccezione.

### 8.3 Gli scenari residui dove l'aereo torna razionale (onestà intellettuale)

Questi **non sono "connettere Pentema"**: sono prodotti diversi.

1. **Emergenza/disaster multi-valle** (il più difendibile). Sisma/frana/incendio che abbatte torri *e* taglia fibra *e* toglie corrente (Starlink fisso a terra muore senza alimentazione): un VTOL/aerostato schierabile come nodo comms d'area per Protezione Civile. Rafforzato dal fatto che **Starlink stesso ha un single point of failure** (outage globale 24/7/2025, ~2.5 h, guasto control-plane) `[ThousandEyes/Forbes | 2025 | monitoraggio+stampa | alta]`. Ma è **asset d'emergenza**, non business ricorrente. Confidenza nicchia reale: media-alta; business sostenibile: bassa.
2. **Direct-to-device di area vasta multi-borgo (NTN da quota).** Sensato solo aggregando molti punti sottoserviti. **In rotta di collisione con Starlink Direct-to-Cell**: SMS commerciale da lug-2025, dati per app da ott-2025, voce 2026; **nessun accordo MNO italiano annunciato a metà 2026** `[AstroSpace/T-Mobile | 2025-26 | primario+stampa | media-alta]`. Finestra temporale stretta: appena TIM/Iliad/WindTre firma, l'orbita fa lo stesso da 550 km. Confidenza: bassa-media.
3. **Capacity surge per eventi** (raduni, presepe di Pentema, incendi con centinaia di operatori). Nicchia reale ma piccola, contendibile con COW terrestri + carri Starlink. Confidenza: media.
4. **Sovranità del dato / EO persistente.** Argomento valido ma è **altro mercato** (osservazione, non connettività); per la connettività-sovrana la risposta europea è **IRIS² (satellitare)**, non la stratosfera. Confidenza: media.

---

## 9. Verdetto e raccomandazione

**(1) Requisito minimo quota + autonomia per connettività utile.**
- Solo-borgo: **≥0.2–0.5 km sopra il borgo + persistenza 24/7 (tethered)**.
- Area vasta ("mestiere del satellite"): **≥8–12 km per scavalcare le creste + endurance multi-giorno**.
- La fascia VTOL a batteria (1–4 km, 6–10 h), la più finanziabile, **non soddisfa la persistenza** richiesta da un servizio di connettività continuo.

**(2) Percorso spettro raccomandato.**
- Servizio continuativo → **partnership MNO (neutral-host/MOCN, spettro sub-6 GHz dell'operatore)**; evitare la dipendenza dalla licenza HAPS ITU dedicata.
- Emergenza → **deroghe Protezione Civile / spettro pubblica sicurezza**.
- IoT ambientale → **LoRa 868 MHz** subito. RLAN airborne da evitare come servizio primario.

**(3) Verdetto se/quando ha senso una piattaforma aerea per la SOLA connettività vs Starlink/terrestre.**
- **Per la sola connettività broadband residenziale di Pentema: NO.** Battuta da Starlink + ponte radio da Torriglia di 1–3 ordini di grandezza in costo, tempo e rischio. La piattaforma aerea **non è finanziabile come "porta-Internet-al-borgo"**.
- **Ha senso solo** se il servizio primario è ridefinito: **resilienza d'emergenza multi-valle (Percorso più difendibile), EO/monitoraggio idrogeologico, IoT d'area, capacity d'evento**, con la connettività come funzione *secondaria/di emergenza*, non come business core.
- **Implicazione strategica per il progetto:** il pilota Pentema va posizionato come **dimostratore multi-servizio (EO + emergenza + IoT)**, non come soluzione di connettività broadband. Chi finanzia (Coopfond/PNRR/Regione) confronterà inevitabilmente con Starlink; la value proposition "connettività" da sola **non regge una due diligence competente**.

---

## 10. Livelli di confidenza e falsifying observations (sintesi)

| Claim | Confidenza | Falsifying observation |
|---|---|---|
| Link RF sub-6 GHz chiude a tutte le quote (DL e UL handheld) | **Alta** | RSSI misurato a Pentema >15 dB sotto free-space a 20–30 km |
| Orografia richiede ≥8–12 km per copertura d'area oltre creste | Media-alta | Viewshed su DTM TINITALY 10 m mostra corridoi LOS a quota inferiore |
| Persistenza è il vincolo dominante (non il link) | **Alta** | — |
| Starlink batte l'aereo per connettività-borgo di 1–3 ordini | **Alta** | Costi Starlink IT raddoppiano e/o cella Liguria sold-out cronico |
| Via spettro MNO è la più rapida | Media | Nessun MNO firma neutral-host aereo entro 18 mesi |
| Starlink D2C erode la nicchia NTN multi-borgo | Media | Nessun accordo MNO italiano D2C entro 3–4 anni |
| HALE base rate <30% | **Alta** | `[epistemic-rigor | interno]` |

**Lacune dichiarate (da colmare prima di chiudere un capitolo):** (a) viewshed reale di Pentema su DTM 10 m; (b) copertura mobile/fissa *puntuale* su Pentema (non dato d'area); (c) catasto tralicci Torriglia/Prelà/Antola (ARPAL CEM + Registro AGCOM/MIMIT); (d) adozione Starlink effettiva tra i residenti (= do-nothing baseline del business case); (e) conferma via spettro con sub-analisi regolatoria.

---

## 11. Fonti

- 3GPP TR 38.811 v15 (geometria HAPS, 229 km a 5°) — `fonti/38811.md` §5.3.3. `[norma | alta]`
- 3GPP TR 38.821 v16.2.0 (capacità NR-NTN) — `fonti/3GPP_TR_38821...md`. `[norma | media-alta]`
- ITU-R P.618-14 (rain fade) — `fonti/R-REC-P.618-14...md`. `[norma | alta]`
- Link budget methodology — `fonti/Link_budget_uvigo.md` (Univ. Vigo) + skill `link-budget-calculator` + Allegato A.7. `[media-alta]`
- AGCOM Delibera 93/26/CONS (PNRF, metodo) — `fonti/Delibera 93-26-CONS.md`. `[norma | alta]`
- Contesto territoriale Pentema — sub-analisi territoriale + `Aree interne/Dossier SNAI.md`. `[triangolato | media-alta]`
- Alternative Starlink/terrestri — sub-analisi competitor (fonti web 2025-26: TechPost, Selectra, Starlink IT, EOLO, Ubiquiti, Innovazione.gov.it, ThousandEyes, T-Mobile/AstroSpace). `[stampa+primario | media-alta]`
- Spettro/regolatorio — sub-analisi regolatoria: ETSI EN 300 328/301 893; Dec. (UE) 2022/179; ERC-REC 70-03; Dec. 626/2008/EC (MSS); MIMIT autorizzazioni temporanee; ITU Res. 213 WRC-23 (HIBS); MOCN IT (PRISM, Zefiro Net); Loon/AT&T; Protezione Civile Rete Radio nazionale. `[norma+stampa | media-alta]`
- Script di calcolo riproducibile: `analisi-bottom-up/lb_bottomup.py`.

*Documento completo. Le lacune §10 (viewshed DTM, copertura puntuale Pentema, catasto tralicci, adozione Starlink effettiva) restano da colmare prima di chiudere un eventuale capitolo dello Studio.*
