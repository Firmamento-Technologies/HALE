# 11 — Fasce di piattaforma × famiglie di missione: mappa delle nicchie multi-missione

**Progetto HALE / Firmamento Technologies — riframing "famiglia modulare a fasce con payload intercambiabile"**
**Data:** 2026-07-08 · **Autore:** aerospace-market-analyst · **Confidenza complessiva:** media sui fatti-benchmark, bassa/molto-bassa sulle stime di sizing italiano.

> **Mandato (riframing).** Non più "la piattaforma minima per UN servizio (connettività/EO)", ma una **famiglia di piattaforme modulari a fasce** il cui payload intercambiabile (connettività / sensori-EO / **trasporto**) aggredisce nicchie diverse. Pentema/connettività = trampolino politico, non il fine. Domanda: *per ogni famiglia di missione, quanto vale il mercato indirizzabile IT/EU, chi paga, qual è la WTP, e quale FASCIA di piattaforma la serve meglio?* Poi: **esiste una fascia che sblocca abbastanza nicchie da giustificare l'investimento?**
>
> **Base di partenza:** i report `01`–`07` di questa cartella (in particolare `03-mercato.md` per connettività+EO e `05-piattaforme-costi.md` per il benchmark di fascia). Qui si **aggiungono** TRASPORTO/logistica medicale, consegna pacchi, sorveglianza/sicurezza, difesa/dual-use, e si rilegge tutto con la lente modulare.
>
> **Regola epistemica.** Ogni cifra è marcata `[fatto|stima; fonte; confidence]`. Le stime di sizing italiano medical/delivery sono **preliminari** (nessuna riga di spesa SSN ricorrente ancora esiste): trattarle come ordine di grandezza, non baseline.

---

## 0. Sintesi (il resto la argomenta)

**Le fasce** (allineate al mandato T1–T4, con la baseline COTS T0 come termine di paragone):

| Fascia | Descrizione | Payload utile | Profilo aero | Regolatorio | CapEx unità | Ancora (report 05) |
|---|---|---|---|---|---|---|
| **T0** (baseline COTS) | Multirotore/VTOL COTS spot (DJI M350, Wingtra) | 2,7 kg | hover/spot, 40–60 min | Open/Specific | €11–120k | Classe 1 |
| **T1** | C3 box-wing/fixed-wing <25 kg, <3 m (**concept Firmamento**) | 1–3 kg | **high-AR, loiter/endurance** | Specific SAIL II | €150–400k demo | Classe 2 |
| **T2** | **Mid VTOL/fixed-wing heavy 25–150 kg** (CW-30E, Tekever AR3, Wingcopter-class) | 3–10 kg | VTOL + crociera, 6–16 h | Specific SAIL III | €0,6–1,6M TCO | Classe 3 |
| **T3** | MALE >150 kg (Tekever AR5, Eurodrone) | 6–350 kg | long-endurance, quota media | Certified/mil | €2–8M+ / €7,5–8,75M/anno-as-a-service | Classe 5 |
| **T4** | HALE stratosferico ~20 km, perennial | modulare | pseudo-satellite | Certified, no framework | $50M–1B/programma | Classe 6 |

**Verdetto sintetico in tre righe:**
1. Le **3 missioni a maggior valore reale accessibile** sono **(a) logistica medicale time-critical**, **(b) EO-persistenza in finestra (incendi/emergenza PC)**, **(c) sorveglianza ambientale/PC locale** — e **tutte e tre le serve la fascia T2** (mid VTOL con payload swap), non T1 né T4.
2. Il **trasporto medicale cambia qualitativamente il quadro del report 03**: è la prima missione in cui **volare è intrinsecamente necessario** (una torre non consegna nulla) e in cui il **sostituto non è gratuito** (elisoccorso €2.000/h, corriere terra lento) → esiste una WTP genuina e un pagatore nuovo (SSN/ASL/Regioni/118). **Ma** non riscatta l'HALE né il box-wing: punta a un **cargo-VTOL dedicato**, dove l'incumbent italiano (**ABzero**) è già avanti, ed è **pilot/grant-stage**, non mercato ricorrente.
3. **Nessuna singola fascia sblocca abbastanza nicchie *pagate e non-contese* da giustificare da sola l'investimento in una piattaforma custom.** La fascia che ne sblocca di più (**T2**) è largamente coperta da **COTS** (buy, non build) ed è dominata mission-per-mission da sostituti/incumbent. **T1 (box-wing custom)** e **T4 (HALE)** sono le fasce peggio allineate alle missioni a valore. → **Buy T2 COTS + payload modulare** è razionale come *operatore*; **build T1/T4 custom** resta R&D di opzione, da finanziare a parte (vedi `00-SINTESI` §8, barbell).

---

## 1. Perché la lente "fascia × missione" (e i due assi che contano)

Il riframing modulare promette che *una famiglia di airframe copra molte nicchie cambiando payload*. Va testato su **due assi indipendenti** che il pitch tende a confondere:

- **Asse payload** (cosa porta): sensore-EO | radio-relay | **carico fisico**. La modularità *è* qui ed è reale: un vano payload standard può ospitare gimbal EO **oppure** un nodo LTE **oppure** una capsula-cargo.
- **Asse profilo di missione** (come vola): **loiter** su area (EO/connettività, serve endurance e basso consumo → high-AR) vs **sprint point-to-point** (consegna, serve VTOL/velocità e vano-carico) vs **orbita persistente** (sorveglianza). **Questi profili chiedono airframe diversi.** Un high-AR endurance (T1/T4) è ottimo a loiter e **pessimo** a consegnare; un VTOL tilt-wing (Wingcopter/T2) è ottimo a consegnare e mediocre a loiter lungo.

> **Conseguenza-chiave (rigore):** la modularità di *payload* non implica modularità di *missione*. La fascia che massimizza il numero di missioni servibili con **un compromesso accettabile** è **T2 (mid VTOL)** — non le fasce endurance-ottimizzate del concept Firmamento (T1 box-wing, T4 HALE), che sono ottimizzate proprio per le missioni (EO wide-area, connettività) **già dominate dai sostituti gratuiti** (Copernicus, Starlink — report 02/03).

---

## 2. Sizing per missione (pagatore → WTP → ticket → sostituto → verdetto → fascia)

### Missione 1 — TRASPORTO / LOGISTICA MEDICALE ⭐ (nuova, il caso "volare è necessario")

**Cos'è:** consegna time-critical di sangue/emocomponenti, campioni, farmaci salvavita, vaccini, **defibrillatori (AED)** a borghi montani, isole minori, tra ospedali. Telemedicina-logistica.

**Perché è diverso da EO/connettività:** il sostituto **non** è gratuito (Copernicus) o quasi-gratuito (Starlink), è **costoso o lento**: elisoccorso privato **~€2.000/h**, e nelle Regioni a pagamento fino a **€115–120/min** (Valle d'Aosta, Piemonte) `[fatto; ambulanza.it/prealpina; medium]`; corriere terra = lento, non praticabile per isole/valli. Il drone si incunea **nel gap prezzo/tempo**. **Una torre fissa non consegna nulla** → la componente volante è **strutturalmente insostituibile**, a differenza di 2b/EO.

**Evidenza-benchmark (fatti):**
- **ABzero** (spin-off Scuola Sant'Anna, Pisa) — *Smart Capsule* per sangue/organi/farmaci; **U-ELCOME Varese: 20 voli notturni, −80% tempi di trasporto intra-ospedaliero**; rotte Grottaglie–Taranto 17 km, Eolie 37 km (Vulcano), Langhirano 245 km in ~20 voli BVLOS. **Round da soli €190k (lug. 2025)** `[fatto; abzero.it, quadricottero, lanazione; medium]`. → **incumbent italiano, già davanti a Firmamento, con IP di capsula e track-record BVLOS.**
- **Progetti regionali** attivi: ASP Messina/Patti→Eolie (sangue/emocomponenti), ASL Lecce Gallipoli–Casarano, Campania Pozzuoli→Ischia, **SEUAM/118** (defibrillatori). Claim vendor: **−80% tempi, −40% costi diretti** vs mezzo convenzionale `[stima vendor; quotidianosanita, mobilitafutura, dtascarl; low-medium — dato di parte]`.
- **Wingcopter** (DE): sangue Greifswald 26 km in 18 min, payload 250 g, BVLOS; $119M raccolti, 15 Paesi `[fatto; wingcopter.com, tech.eu; medium]`.
- **AED-drone / arresto cardiaco (il caso clinico più forte):** studio Karolinska (Svezia), 5 droni-AED su ~200.000 abitanti, **arrivo prima dell'ambulanza nella maggioranza dei casi** (mediana ambulanza 11 min); con shock AED precoce sopravvivenza **50–70%** `[fatto; Karolinska/Lancet Digital Health 2023; high per l'evidenza clinica]`.
- **Mercato (report commerciali, da declassare a stima):** *EU medical drone delivery services* **$0,5B (2025) → $5,5B (2035), CAGR ~29%**; "medical aid" segmento a CAGR più alto (43,56%) del delivery `[stima; towardshealthcare/grandview/mobilityforesights; **low** — single-source commerciale, include hardware+pilota+grant]`.

**Sizing Italia (bottom-up, stima):**
- **Pagatore:** SSN via ASL/Aziende Ospedaliere, **Regioni** (sanità = ~l'80% dei bilanci regionali), **118/centrali operative**, centri trasfusionali (SIMT, ~300 strutture). **NON** l'utente finale.
- **WTP:** medio-alta ma **ancorata a grant/sperimentazione oggi**; diventa alta *solo* se il servizio entra in un capitolato SSN ricorrente (non ancora accaduto in IT).
- **Ticket plausibile:** €50–150k/rotta-anno come servizio "as-a-service" (drone+capsula+operazioni+compliance), 2–5 consegne/giorno. Confronto costo-unitario di riferimento a regime: **Zipline $3–13/consegna** — ma con **$600M di capitale bruciato e non-profittevole** `[fatto; dronexl/TT/contrary; medium]`; i pilot italiani sono ancora **decine di € sussidiati**.
- **TAM-IT a maturità (2030–35):** ~50–200 rotte isola/montagna/urbano-congestionato indirizzabili × €50–150k ⇒ **~€5–25M/anno** `[stima; confidence low]`. Coerente per ordine di grandezza con la frazione IT (~8–10%) del dato EU.
- **SAM Firmamento (Liguria + limitrofe):** **debole in Liguria** — nessuna isola abitata rilevante (Gallinara disabitata); il valore ligure è (i) borghi montani isolati (sangue/AED a valli tipo Antola) e (ii) rete ospedaliera genovese congestionata (trasporto intra-urbano). SAM ~€0,5–3M/anno a maturità, **conteso da ABzero** `[stima; low]`.
- **SOM Firmamento 5 anni:** €0–0,5M, e **solo** come operatore regionale in partnership (o rivendendo tecnologia ABzero/Wingcopter), non come sviluppatore di capsula. `[stima; very low]`

**Sostituto & dominanza:** il sostituto non è gratis (elisoccorso caro / terra lento) → **la missione NON è dominata da un sostituto economico**; è però **occupata dall'incumbent** (ABzero) sul piano tecnologico, e **immatura sul piano del pagatore** (nessun capitolato SSN ricorrente). **È un business reale nel medio termine, oggi grant/pilota.**

**Fascia ottimale:** **T2 cargo-VTOL** (Wingcopter/ABzero-class, payload 2–6 kg, autonomia 40–110 km) per rotte isola/valle; **T0 multirotore** per AED-a-arresto-cardiaco (risposta rapida, corto raggio, pre-posizionato). **NON T1 box-wing** (high-AR loiter = airframe sbagliato per consegna) né T4 HALE (assurdo).

---

### Missione 2 — CONSEGNA PACCHI / E-COMMERCE aree remote

**Cos'è:** last-mile drone per pacchi <2,5 kg in aree difficili (Prime Air, Meituan, Wing).

**Evidenza-benchmark (fatto decisivo):** **Amazon Prime Air ha SOSPESO l'Italia (dic. 2025)**, ritirando la certificazione operatore a San Salvo (Abruzzo) **giorni prima del lancio**, spostando lancio+cert in altro Stato UE; ENAC ha comunque attivato il **primo U-space europeo** dal 1° gen 2026 `[fatto; ENAC comunicati, CNBC, quadricottero; high sul fatto della sospensione]`. Economia: **~$10–13/consegna drone vs ~$2 terra** `[fatto; dronexl/Zipline; medium]`.

**Sizing / verdetto:** **Pagatore** = e-tailer/corriere; **WTP** dell'utente rurale = zero-premium (vuole spedizione gratis). In un Paese con rete postale/corriere densa ed economica e volumi rurali bassi, **il corriere terrestre domina sul costo** e i volumi non ripagano l'infrastruttura di vertiporti. Se **Amazon** (capitale illimitato, sito pronto, partnership ENAC) **si è ritirata**, un operatore cooperativo non ha alcuna chance economica.

**Sostituto & dominanza:** **DOMINATA dal corriere terrestre.** **Vetrina/grant, non business.** **Fascia:** irrilevante (nessuna la salva). **Scartare** come linea di ricavo; usare solo come narrativa/demo se un partner logistico finanzia.

---

### Missione 3 — EO / SENSING (frane, incendi, agricoltura, infrastrutture, ispezioni)

**Sintesi (da report 02/03, rilettura modulare):** la maggior parte dei servizi EO utili alle Aree Interne è **dominata da Copernicus (gratis)** per il wide-area lento (frane EGMS mm/anno, post-incendio Sentinel-2 NBR, vegetazione) **o da drone COTS a noleggio** per il dettaglio point-in-time (ispezione ponti/corridoi, plot agricoli, fronte-frana) `[fatto; report 02; high]`. Il **solo** discriminante aereo è la **PERSISTENZA**, utile a 2 servizi: **early-detection incendi in finestra estiva** e **overwatch emergenza PC** — ed **entrambi sono battuti da sostituti più economici** (torri-camera fisse €10–50k; drone tattico in standby) `[fatto; report 02 §4; medium]`.

**Sizing (da report 03):** mercato droni-servizi professionale IT **€160M (2024), 657 imprese**, 96% operazioni tradizionali, pricing **€350–3.000/lavoro** `[fatto; Osservatorio Droni Polimi; high]`. Utility (Terna €50M/anno ispezioni) **in-house + Wesii** = porta chiusa. **Pagatore accessibile:** Regione/Enti Parco/PC grant-anchored. **Ticket:** micro-commesse o convenzioni €20–150k. **SAM/SOM:** come report 03 (ricorrente non-grant €40–150k/anno).

**Sostituto & dominanza:** **DOMINATA** salvo la nicchia persistenza (stretta, contesa). **Fascia ottimale per la nicchia residua:** **T2 loiter 6–10 h** (o T0/dock COTS); **T1** marginale, **T4** sovradimensionato/sprecato (swath 3 km su valle 200 km²). Business **reale ma piccolo e grant-anchored**.

---

### Missione 4 — CONNETTIVITÀ / IoT relay d'emergenza e d'area

**Sintesi (da report 01/03):** per la **banda larga**, **Starlink batte l'aereo di 1–3 ordini di grandezza** (€29–40/mese vs infrastruttura HAPS) + BUL fibra pubblica €43,1M in Liguria `[fatto; report 01/03; high]`. Resta valore **solo** come **resilienza d'emergenza / IoT d'area** (LoRa 868, backhaul temporaneo, relay PC durante evento) — episodico, piccolo, difficile da contrattualizzare come ricorrente. Spettro: via **MNO-hosting o ISM**, **non** banda HAPS dedicata (WRC-27-dipendente) `[fatto; report 04 §4; high]`.

**Sizing:** **Pagatore** = PC/Regione (resilienza), MNO (wholesale, post-Rel.18/19 = ~0 a 5 anni). **WTP** near-zero per il ricorrente broadband; bassa-media per relay-emergenza a progetto. **SOM:** trascurabile come linea autonoma. **Sostituto & dominanza:** **DOMINATA da Starlink** (broadband). **Fascia:** T2 loiter con relay-payload, o tethered/torre; **T4 HALE** farebbe connettività regionale persistente ma è **unfinanceable e senza framework/spettro**. **Secondaria**, non fondante.

---

### Missione 5 — SORVEGLIANZA / SICUREZZA / AMBIENTE (antibracconaggio, coste, confini, monitoraggio)

**Due sotto-mercati distinti:**
- **B2G "grande" (coste/confini/ISR):** dominato dai **prime**. Leonardo **Falco EVO** su gara Frontex sorveglianza marittima (contratto 300 h volo + estensioni; Frontex **10.800 h volo nel 2024**); Guardia di Finanza **V-BAT** (via Siralab) `[fatto; Leonardo, IrpiMedia; medium]`. Budget reali e grandi ma **presidiati da Leonardo/prime + operatori mil**; **fascia T3 MALE**, **certified/mil**, fuori portata Firmamento.
- **B2G "locale" (parchi/ambiente/PC):** antibracconaggio, monitoraggio coste locali, discariche/sversamenti, controllo territorio Enti Parco. **Pagatore:** Enti Parco, ARPA, Regione, Comuni costieri — budget €5–50k a progetto, **grant-anchored**. **WTP** medio-bassa. **Sostituto:** drone COTS a noleggio + guardie/telecamere fisse.

**Sizing:** sotto-mercato locale ~stessa cassa dell'EO territoriale (dentro i €40–150k non-grant del report 03, non aggiuntivo). **Sostituto & dominanza:** grande mercato **DOMINATO dai prime**; nicchia locale **contesa dai 657 operatori droni**. **Fascia:** T2 (locale) / T3 (coste-confini, inaccessibile). Business **piccolo (locale) o inaccessibile (nazionale)**.

---

### Missione 6 — DIFESA / DUAL-USE (solo inquadramento del potenziale)

**Il potenziale:** il MALE/HALE apre l'adiacenza difesa, dove i budget sono ordini di grandezza sopra il civile. **Eurodrone** (MALE europeo): **€7B totali**, quota **Italia ~€1,9B / 15 velivoli / 23%**, Leonardo su AMS+ala; consegne 2028–35; **EDF €7,9B (2021–27)** `[fatto; Sole24Ore, aresdifesa, it.wikipedia; medium-high]`. Benchmark servizio persistente reale: EMSA **€7,5–8,75M/anno** per 4 MALE (report 05).

**Verdetto (inquadramento):** mercato enorme ma **interamente presidiato dai prime nazionali** (Leonardo) e dai consorzi (Airbus/Dassault). Firmamento a T3/T4 potrebbe solo essere **sub-fornitore di sottosistema** o partner di minoranza (come Skydweller–Leonardo per l'HALE). **Non accessibile near-term** come operatore/OEM; rilevante **solo** come vettore-opzione di lungo periodo (Pool B / EDF, `00-SINTESI` §8) e come **narrativa dual-use** che abbassa alcune barriere (finanziamento) mentre ne alza altre (golden power, `RESERVED-rischi-geopolitici`). **Fascia:** T3–T4. **Inquadramento, non business a 5 anni.**

---

## 3. LA MATRICE MISSIONE × FASCIA (deliverable centrale)

Legenda: **●●** = sweet-spot della fascia per quella missione · **●** = servibile ma sub-ottimale/overkill · **�altro** = marginale · **✗** = airframe sbagliato o dominato · **—** = fuori scope.
Colonna "Sostituto dominante" = cosa batte la piattaforma dedicata. Colonna "Business?" = **Sì** (mercato reale) / **Parz.** (reale ma piccolo/conteso/grant) / **Vetrina** (dominato).

| Missione | T0 COTS | T1 box-wing C3 | **T2 mid VTOL** | T3 MALE | T4 HALE | Pagatore | Sostituto dominante | **Business?** |
|---|---|---|---|---|---|---|---|---|
| **1. Logistica medicale** | ●● (AED corto raggio) | ✗ (loiter≠consegna) | **●● (rotte isola/valle)** | ● (overkill) | ✗ | SSN/ASL/Regioni/118 | elisoccorso (caro) / terra (lento) — **NON economico** → volo necessario; ma **ABzero** incumbent | **Sì (medio termine); oggi pilot/grant** |
| **2. Consegna pacchi** | ● | ✗ | ● | — | — | e-tailer/corriere | **corriere terrestre ~$2** (Amazon si è ritirata IT) | **Vetrina** |
| **3. EO / sensing** | ●● (spot/dettaglio) | ● (BVLOS area) | **●● (persistenza finestra)** | ● (regionale) | ✗ (sprecato) | Regione/Parchi/PC/agri | **Copernicus (gratis) + drone COTS + torri fisse** | **Parz. (nicchia persistenza)** |
| **4. Connettività/IoT** | ~ | ~ | **●● (relay emergenza)** | ● | ● (regionale, unfin.) | PC/Regione; MNO (futuro) | **Starlink** (broadband) | **Parz. (solo resilienza)** |
| **5a. Sorv. coste/confini** | ✗ | ✗ | ● | **●● (ISR)** | ● | Difesa/GdF/Frontex | **Leonardo/prime** (presidiato) | **Inaccessibile** |
| **5b. Sorv. ambientale locale** | ●● | ● | **●●** | ✗ | ✗ | Parchi/ARPA/Comuni | drone COTS noleggio + 657 operatori | **Parz. (piccolo, grant)** |
| **6. Difesa/dual-use** | ✗ | ✗ | ~ | **●● (Eurodrone-class)** | ● (HALE mil) | MoD/EDF | **prime (Leonardo/Airbus)** | **Inquadramento (Y6+)** |

**Lettura per colonna — quante nicchie *accessibili e pagate* sblocca ciascuna fascia:**

| Fascia | Nicchie in sweet-spot (●●) | Verdetto d'insieme |
|---|---|---|
| **T0 COTS** | AED-medicale, EO-spot, sorv. locale | Copre molto a **costo minimo (€11–120k)**, ma **nessuna persistenza** e **niente cargo di rotta**. È il **buy di default**. |
| **T1 box-wing custom** | *(nessuna ●●)* — solo EO-BVLOS ● | **La fascia peggio allineata alle missioni a valore.** Loiter-ottimizzata → serve bene le missioni **già dominate** (EO/connettività), male quella forte nuova (consegna). **Build custom non giustificato dal mercato.** |
| **T2 mid VTOL** | **Medicale, EO-persistenza, connettività-relay, sorv. locale (4 su 6)** | **La fascia che sblocca più nicchie civili accessibili** con payload swap. **MA:** ognuna è piccola/contesa, e la fascia è **coperta da COTS (CW-30E/Tekever/Wingcopter)** → **buy, non build.** |
| **T3 MALE** | Sorv. coste/confini, difesa | Grandi budget ma **presidiati dai prime**; certified/mil; **inaccessibile** a Firmamento standalone. |
| **T4 HALE** | *(nessuna ●● accessibile)* | Missioni teoriche (connettività+EO regionale, HALE-mil) tutte **unfinanceable / senza framework / dominate**. **R&D di opzione, non servizio.** |

---

## 4. Il trasporto medicale cambia il quadro del report 03?

**Sì, qualitativamente; no, sul verdetto d'investimento.**

**Cosa cambia (a favore):**
- È la **prima missione in cui il sostituto non è gratuito**. Report 03 concludeva "mercato piccolo perché Starlink e Copernicus sono gratis/quasi": nel medicale il confronto è con **elisoccorso €2.000/h** e corriere terra lento/impossibile per isole → **la value proposition del volo è genuina e difendibile** ("volare è necessario, e costa meno del sostituto premium").
- Introduce un **pagatore nuovo e capiente** (SSN/sanità regionale) con logica **mission-critical** (vite, tempo), non "nice-to-have". Le narrative AED/arresto-cardiaco hanno **evidenza clinica solida** (sopravvivenza 50–70% con shock precoce) → forte leva politica e di ROI sociale.
- Sposta il baricentro tecnologico verso una **capacità reale (cargo-VTOL)** anziché la rivendita di Copernicus (che il red-team `07` giudicava senza barriera).

**Cosa NON cambia (contro):**
- **Non è un mercato ricorrente oggi in Italia:** è **pilot/grant-stage** (U-ELCOME, progetti regionali, round ABzero €190k, Amazon che si ritira). Nessun capitolato SSN ricorrente esiste ancora → stessa **grant-dipendenza** del report 03, con in più un ciclo di adozione sanitaria lento (procurement, risk-averse, HTA).
- **Incumbent già davanti:** **ABzero** ha IP (Smart Capsule), BVLOS track-record e backing Sant'Anna; Wingcopter domina l'hardware EU. Firmamento entrerebbe **come follower**, non come categoria nuova — lo stesso problema-moat del report 03/07.
- **Geografia ligure debole:** il medicale-drone rende di più dove ci sono **isole abitate e arcipelaghi** (Sicilia/Campania/Puglia/Toscana), **non** in Liguria (nessuna isola rilevante). Pentema/Antola dà solo il caso "borgo montano isolato" + AED, che è **B2G-118 grant-anchored** a volumi bassi.
- **Airframe:** premia un **cargo-VTOL dedicato (T2, buy)**, **non** il box-wing high-AR del concept (T1) né l'HALE (T4). Cioè: **il trasporto rafforza la tesi "servizio con COTS mid-VTOL", indebolisce ulteriormente la tesi "costruiamo il box-wing/HALE".**

**Netto:** il trasporto medicale **alza il tetto di plausibilità del mercato** (nuovo pagatore, WTP reale, volo necessario) e **migliora la difendibilità narrativa**, ma **non sposta l'ordine di grandezza dell'investimento razionale** del report 03 (€0,3–1M, grant-prevalente) né riscatta le fasce custom T1/T4. Aggiunge una **linea di ricavo potenziale** (SOM +€0–0,5M a 5 anni, very-low confidence), da perseguire **in partnership/buy**, non in build.

---

## 5. VERDETTO: esiste una fascia che sblocca abbastanza nicchie da giustificare l'investimento?

**No, se "investimento" = build di una piattaforma custom (T1 box-wing o T4 HALE).** Sì, se "investimento" = **capacità operativa asset-light su fascia T2 COTS con payload modulare**, e solo entro il tetto del report 03.

Argomento:
1. **La fascia che sblocca più nicchie accessibili è T2** (mid VTOL): 4 missioni su 6 in sweet-spot (medicale, EO-persistenza, relay-emergenza, sorv. locale). Questo è il **cuore dell'idea modulare** ed è **corretto**: un mid-VTOL con vano payload standard è realmente multi-missione.
2. **Ma T2 è terreno COTS** (CW-30E €0,6–1,6M TCO, Tekever, Wingcopter): **buy batte build** di 1–2 ordini di grandezza (report 05 §11). Costruire un T2 custom non aggiunge nicchie, aggiunge costo e rischio.
3. **Le fasce che il concept Firmamento vuole costruire (T1 box-wing, T4 HALE) sono le peggio allineate** alle missioni a valore: loiter/endurance ottimizza per EO-wide e connettività, cioè **le missioni dominate da Copernicus e Starlink**. La missione forte nuova (consegna) le **rifiuta** (airframe sbagliato).
4. **Ogni singola nicchia sbloccata da T2 è piccola e/o contesa:** medicale (ABzero + pilot-stage), EO-persistenza (torri fisse + Copernicus), relay (Starlink), sorv. locale (657 operatori). **La somma di quattro nicchie piccole e contese non è automaticamente un mercato grande e difendibile** — è il rischio "morte per mille nicchie sottili".
5. **Il valore multi-missione modulare esiste** e giustifica **posizionarsi come operatore di servizi su fascia T2 (buy)**, orchestrando payload EO + relay + eventuale cargo, dentro il tetto d'investimento del report 03 (**€0,3–1M, grant-prevalente**). **Non** giustifica R&D di piattaforma custom sul P&L del servizio: quella resta **opzione strategica separata** (barbell, `00-SINTESI` §8), da candidare a Pool B (EDF/Horizon/PNRR-Aero) e da tenere fuori dal conto economico operativo.

**In una riga:** *la modularità di payload è reale e la fascia T2 la incarna, ma la si compra (COTS), non la si costruisce; le fasce che Firmamento vorrebbe costruire (T1/T4) servono proprio le missioni già perse. Il trasporto medicale è la nicchia più promettente ma è presidiata (ABzero), pilot-stage e off-geografia per la Liguria — apre una linea da partnership, non da OEM.*

---

## 6. Falsificazione per missione (kill-criteria)

| Missione | Osservazione che la **conferma** business | Osservazione che la **falsifica** |
|---|---|---|
| **1. Medicale** | ≥1 capitolato SSN/ASL/Regione **ricorrente pluriennale** (non-pilota) firmato con Firmamento entro M+24 | ABzero/Wingcopter chiudono i contratti regionali; i progetti restano grant-pilota; Liguria senza rotte isola → nessun ricavo |
| **2. Pacchi** | Un partner logistico finanzia infra e paga il servizio con margine positivo | *Già falsificata:* Amazon si è ritirata dall'Italia (dic. 2025); corriere terra €2 domina |
| **3. EO persistenza** | Un ente firma SLA antincendio/overwatch che **una torre fissa €30k non può erogare** | Torre-camera crinale + Copernicus eroga la stessa SLA a 1/10 del costo (report 07 §4) |
| **4. Connettività** | Contratto PC/MNO per relay-emergenza ricorrente | Starlink Direct-to-Cell copre il caso residuo → nicchia svanisce |
| **5. Sorveglianza** | Convenzione Ente Parco/ARPA pluriennale non-contesa dai 657 operatori | Leonardo/prime (nazionale) o COTS-a-noleggio (locale) coprono tutto |
| **6. Difesa** | Ruolo di sub-fornitore in un programma EDF/Eurodrone-adiacente | Prime chiudono la filiera; golden power/geopolitica bloccano (`RESERVED`) |
| **Tesi modulare** | Un cliente paga per **≥2 payload diversi sulla stessa piattaforma** entro M+24 | Ogni missione richiede un airframe diverso → la "famiglia" è marketing, non ingegneria |

**Missioni che sono business reale vs vetrina/grant:**
- **Business reale (medio termine):** **Logistica medicale** (con i caveat: partnership, non build; off-Liguria).
- **Business reale ma piccolo/grant-anchored:** **EO-persistenza**, **sorveglianza ambientale locale**, **connettività-resilienza** (secondaria).
- **Vetrina / dominata:** **Consegna pacchi** (Amazon si è ritirata), **broadband** (Starlink).
- **Inquadramento non accessibile a 5 anni:** **sorveglianza coste/confini** e **difesa** (presidiati dai prime; rilevanti solo come vettore-opzione Pool B e narrativa dual-use).

---

## 7. Confidenza, limiti, fonti

**Fatti (confidence medium-high):** ritiro Amazon Prime Air Italia (dic. 2025) + primo U-space UE San Salvo; ABzero Smart Capsule + rotte/round €190k; Wingcopter Greifswald; studio AED Karolinska/Lancet; costi elisoccorso IT; Eurodrone €7B/Italia €1,9B; Frontex/Leonardo Falco; mercato droni-servizi IT €160M/657 imprese (report 03); benchmark fasce (report 05). Fonti terze verificabili.

**Stime (confidence low / very-low):** TAM-IT medicale €5–25M a maturità; SAM/SOM Firmamento medicale; sizing per-nicchia. Sono **elaborazioni dell'analista** su benchmark commerciali single-source e su assunzioni di rotte/ticket **non validate** da un capitolato SSN reale. Le proiezioni 2030–35 sono **scenari**, non forecast.

**Limiti dichiarati (da chiudere prima di ogni commitment):**
- Nessun dato primario sul **costo-per-consegna reale in Italia** (i pilot sono sussidiati): il "−40% costi" è claim vendor.
- Nessuna verifica che esista una **linea di spesa SSN ricorrente** per logistica-drone (oggi: grant EU/regionali, non capitolato strutturale).
- **Tensione airframe loiter-vs-cargo** non risolta ingegneristicamente: la "famiglia modulare" va dimostrata su un airframe reale, non assunta.
- Geografia: sizing medicale calibrato su isole/arcipelaghi; **la Liguria ne è quasi priva** → il caso forte è nazionale/multi-regione, non il pilota ligure.

**Fonti web (nuove per questo documento):**
- Medicale: [abzero.it](https://www.abzero.it/?lang=en); [Quadricottero – ABzero organi](https://www.quadricottero.com/2025/11/trasporto-organi-con-i-droni-potremmo.html); [La Nazione – ABzero sangue](https://www.lanazione.it/pisa/cronaca/emergenza-sangue-lo-consegnano-i-droni-per-il-trasporto-biomedicale-firmati-santanna-bd01a478); [Quotidiano Sanità – Messina/Eolie](https://www.quotidianosanita.it/regioni-e-asl/farmaci-e-sangue-nelle-isole-grazie-ai-droni-asp-messina-avvia-servizio/); [Mobilità Futura – droni salvavita](https://www.mobilitafutura.eu/aria/droni/droni-salvavita-litalia-sperimenta-la-sanita-del-futuro-nei-cieli/37725/); [DTA – ASL Lecce](https://www.dtascarl.org/en/2025/02/13/experimental-project-for-the-transport-of-medical-materials-using-drones-in-the-territory-of-asl-lecce/); [Wingcopter Greifswald](https://wingcopter.com/project/germany_greifswald_blooddelivery); [Tech.eu – Wingcopter](https://tech.eu/2025/03/07/wingcopter-expands-its-capabilities-from-medical-cargo-deliveries-to-surveying-missions/).
- AED/arresto cardiaco: [Karolinska Institutet](https://news.ki.se/drones-delivered-defibrillators-to-patients-with-suspected-cardiac-arrests); [Lancet Digital Health 2023](https://www.thelancet.com/journals/landig/article/piis2589-7500(23)00161-9/fulltext).
- Elisoccorso/costi: [ambulanza.it](https://www.ambulanza.it/eliambulanza/); [Prealpina](https://www.prealpina.it/pages/elisoccorso-quanto-mi-costi-349890.html).
- Pacchi: [ENAC – U-space San Salvo](https://comunicati.enac.gov.it/it/announcement/show/enac-da-gennaio-2026-lancia-il-primo-u-space-europeo-nonostante-la-sospensione-del-progetto-amazon-prime-air-in-italia); [CNBC – Amazon halts Italy](https://www.cnbc.com/2025/12/28/amazon-halts-plans-for-drone-delivery-in-italy.html); [Quadricottero – Amazon/U-space](https://www.quadricottero.com/2025/12/amazon-ferma-i-droni-in-italia-san.html).
- Zipline economia: [DroneXL – Zipline economics](https://dronexl.co/2026/01/21/zipline-economics-of-drone-delivery/); [Contrary Research – Zipline](https://research.contrary.com/company/zipline).
- Mercato delivery EU: [Mobility Foresights](https://mobilityforesights.com/product/europe-delivery-drones-market); [Grand View – drone package delivery](https://www.grandviewresearch.com/industry-analysis/drone-package-delivery-market-report); [Towards Healthcare – medical drone delivery](https://www.towardshealthcare.com/insights/medical-drone-delivery-services-market-sizing).
- Difesa/sorveglianza: [Il Sole 24 Ore – Eurodrone/Leonardo](https://www.ilsole24ore.com/art/primi-fondi-drone-targato-ue-leonardo-quota-25percento-AE1WDyW); [Ares Difesa – Eurodrone Italia](https://aresdifesa.it/il-rpas-male-eurodrone-per-litalia/); [Leonardo – Falco EVO Frontex](https://www.leonardo.com/en/press-release-detail/-/detail/leonardo-deploys-its-falco-evo-remotely-piloted-air-system-for-drone-based-maritime-surveillance-as-part-of-the-frontex-test-programme); [IrpiMedia – droni GdF](https://irpimedia.irpi.eu/en-the-silence-of-italys-guardia-di-finanza-on-drones-deployed-in-the-mediterranean/).

**Fonti interne (repo):** `analisi-bottom-up/03-mercato.md`, `02-osservazione-terra.md`, `01-connettivita.md`, `04-regolatorio.md`, `05-piattaforme-costi.md`, `07-REDTEAM-sintesi.md`, `00-SINTESI-strategica.md`; `riferimenti/DR-research-closure-M3.md`.
