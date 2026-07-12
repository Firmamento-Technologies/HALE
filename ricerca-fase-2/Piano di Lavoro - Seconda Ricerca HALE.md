# Piano di Lavoro — Seconda Ricerca Approfondita H.A.L.E.
### Fase 2: Analisi di mercato downstream e trade study di prodotto (ripartenza dello studio di fattibilità)

Documento preparato sulla base della riunione di brainstorming del 10/07/2026 (Luca, Fede, Gigi, Ema) e di una revisione dell'archivio di progetto esistente (Piano di Fattibilità H.A.L.E., Business Plan, documentazione bando Cooding II), integrata con una ricerca esterna di validazione su mercato, normativa e benchmark tecnici.

---

## 0. Premessa

Il progetto dispone già di un **Piano di Fattibilità H.A.L.E.** molto esteso (14 capitoli in stile NASA Systems Engineering Handbook, oltre 120.000 parole), di un **Business Plan** finanziato dal bando Cooding II – Prototypes (Coopfond/Legacoop) e di un impianto di stakeholder consolidato (10 cooperative liguri aderenti a Legacoop, capofila Fabrica, e Regione Liguria come interlocutore istituzionale, con la frazione di Pentema come sito pilota candidato). Questo lavoro **non va buttato via**: framework metodologico, mappatura regolatoria (ENAC/EASA/AGCOM/GDPR) e struttura di costo sono riutilizzabili.

Quello che la riunione del 10/07 ha rimesso in discussione è **l'ordine logico** con cui si è arrivati alla raccomandazione attuale (percorso duale VTOL pilota → MALE → HALE, focalizzato su Pentema). Il Capitolo 5 del Piano v1 deriva i criteri di trade-off direttamente dai bisogni delle 10 cooperative e da un singolo sito, senza che a monte sia stata condotta un'analisi di mercato downstream ampia e trasversale ai settori. Come sintetizzato da Ema in riunione: *"mi concentrerei prima sull'analisi del mercato, perché è quello che definisce il prodotto"*. La Fase 2 descritta in questo documento colma esattamente questo vuoto, prima di tornare a chiudere il resto del Piano di Fattibilità.

**Nota di metodo importante:** una revisione a campione del Piano v1 ha rilevato diverse cifre e riferimenti estremamente specifici ma non verificabili (es. "conversazione febbraio 2025 Firmamento–ENAC", nomi di funzionari, date di delibere non riscontrabili) accanto a dati marcati onestamente come `[DA CONFERMARE]`. La Fase 2 deve applicare uno standard "evidence-based" più severo: ogni numero usato per convincere investitori o istituzioni deve avere una fonte verificabile o essere esplicitamente marcato come assunzione da validare.

---

## 1. Obiettivo della Fase 2

Produrre un **dossier di mercato e un trade study di prodotto aggiornato**, da integrare nel Piano di Fattibilità come nuova versione dei Capitoli 2 (Stakeholder/Contesto), 3 (Requisiti), 5 (Alternative e trade-off), mantenendo intatta l'impalcatura NASA-SE per le parti a valle (fattibilità tecnica, V&V, CONOPS, costi, regolatorio, rischi, roadmap), da rivedere solo nei punti impattati dalla nuova scelta architetturale.

Non è un restart totale del progetto: è un **restart del ragionamento a monte** (mercato → nicchia → requisiti di prodotto), come esplicitamente concordato in riunione — *"queste non sono decisioni, sono linee guida per la ricerca"* (Ema).

---

## 2. Metodologia: due fasi, in sequenza logica ma con esecuzione in parte parallela

| Fase | Contenuto | Guida dalla riunione |
|---|---|---|
| **Fase A — Analisi di mercato downstream** | Mappatura dei segmenti di servizio (non del velivolo) erogabili da una piattaforma aerea, dimensionamento, crescita, accessibilità per un nuovo entrante | "prima cosa direi di fare un'analisi di mercato molto approfondita su tutto quello che può essere il mercato del downstream" (Luca); suggerimento del membro ASI al Festival dello Spazio di concentrarsi sul downstream |
| **Fase B — Analisi comparativa di prodotto (trade study)** | Confronto HALE/MALE/VTOL/ibridi/configurazioni alternative rispetto ai requisiti emersi dalla Fase A e ai criteri di ottimizzazione | "sulla base di quello realizziamo il prodotto" (Ema) |

Le due fasi non sono rigidamente sequenziali: la Fase B può iniziare a raccogliere dati tecnici in parallelo, ma **il trade study finale (WP3) non si chiude finché la Fase A non ha prodotto un ranking dei segmenti di mercato**, per evitare di ripetere l'errore metodologico del Piano v1 (architettura scelta prima del mercato).

### Criteri di ottimizzazione del prodotto (griglia comune a Fase A e B)

Dalla sintesi di Luca, condivisa in riunione:

- **Massimizzare:** autonomia di volo; modularità (numero di casi d'uso coperti a parità di piattaforma, tramite payload intercambiabili); attrattività per investitori; capacità di leva su finanziamenti pubblico-privati; impatto mediatico/politico
- **Minimizzare:** costo di realizzazione e di esercizio; peso al decollo (target: **categoria C3, MTOM < 25 kg**, per il regime normativo semplificato)

Questi criteri sono **una griglia di ricerca, non una conclusione precotta** — vanno usati per pesare la matrice di trade-off (aggiornamento del Cap. 5 del Piano v1), non per pre-selezionare l'architettura.

---

## 3. Cosa riusare dall'archivio esistente e cosa va rifatto

| Riusabile dal Piano v1 / Business Plan | Da rifare o aggiungere ex novo |
|---|---|
| Framework metodologico NASA Systems Engineering (baseline, trade study, V&V, gate Go/No-Go) | Analisi di mercato downstream multi-verticale, con dimensionamento quantitativo (assente nel Piano v1) |
| Mappatura stakeholder (10 cooperative Legacoop, Regione Liguria, ENAC/AGCOM) | Verticale marittimo/costiero (Cegeno, MSC, Autorità Portuale) — **completamente assente** nel Piano v1 |
| Quadro regolatorio ENAC/EASA/AGCOM/GDPR già mappato (SORA, DPIA, spettro) | Vincolo di peso C3 (<25 kg) come **design driver esplicito** del prodotto, non solo come rischio da evitare (nel Piano v1 compare solo come soglia MTOW da non superare, es. rischio T-A3-04) |
| Cost model e struttura WBS (CAPEX/OPEX, personale, benchmark VTOL JOUAV) | Configurazioni box-wing / joined-wing / a tre superfici portanti come alternative architetturali nel trade study (oggi solo accennate nel documento "Progetto concettuale struttura HALE") |
| Relazioni istituzionali già avviate (Regione Liguria, Pentema, bando Cooding) | Framework decisionale esplicito "prodotto generalista vs due prodotti verticali specializzati" (dibattito Gigi/Ema in riunione, mai affrontato nel Piano v1) |
| Business case narrow su Pentema/aree interne | Validazione se Pentema/aree interne restano il caso d'uso primario o se il mercato indica una priorità diversa (es. ispezione infrastrutture, sanitario) |

---

## 4. Work Package

### WP0 — Validazione critica del Piano di Fattibilità v1 (1-2 settimane)
- Passata "anti-hallucination": separare nel documento esistente i dati con fonte verificabile da quelli con specificità sospetta o assunzioni non marcate; aggiornare/correggere le citazioni non riscontrabili.
- Workshop interno (Luca, Fede, Gigi, Ema + eventuali consulenti) per validare formalmente i criteri di ottimizzazione del §2 come griglia di lavoro condivisa.
- **Output:** nota di validazione + griglia di scoring approvata.

### WP1 — Analisi di mercato downstream multi-verticale (3-4 settimane)
Verticali da coprire (elenco preliminare emerso dalla ricerca di supporto, si veda §6):
1. Ispezione infrastrutture critiche (energia, telco, gasdotti) — segmento oggi più maturo e con clienti ricorrenti in Italia (Terna, E-Distribuzione)
2. Osservazione della Terra / monitoraggio ambientale (incendi, dissesto idrogeologico)
3. Gestione emergenze e protezione civile
4. Logistica sanitaria in aree interne (trasporto farmaci/campioni biologici) — priorità politica con fondi PNRR Missione 6
5. Agricoltura di precisione
6. Connettività (HAPS/4G-5G) — segmento pre-commerciale in Europa, capital-intensive
7. Monitoraggio costiero/marittimo (trattato a parità di profondità nel WP2)
8. Logistica/delivery — CAGR più alto in assoluto ma frenato dalla regolamentazione BVLOS

Task:
- **1.1** Dimensionamento quantitativo di ciascun verticale (mercato globale/UE/Italia, CAGR, fonti primarie) — punto di partenza: dati raccolti in §6.
- **1.2** Interviste di validazione con potenziali clienti reali B2B/B2G (utility, ASL, Protezione Civile, Regione Liguria, Comuni SNAI) per capire disponibilità a pagare e canali di accesso — azione già indicata in riunione ("consultare la documentazione già in archivio... ").
- **1.3** Mappatura competitiva: chi offre già questi servizi in Italia/Europa (in Italia 675 aziende attive nel settore drone professionale) e dove c'è spazio per un nuovo entrante piccolo.
- **Output:** rapporto di mercato con ranking dei verticali per attrattività, incrociando dimensione/crescita/accessibilità con la missione politica del progetto (aree interne, SNAI, cooperative).

### WP2 — Verticale marittimo (parallelo a WP1, pari profondità — azione esplicita dalla riunione)
- Mappare i contatti già disponibili (Cegeno, MSC, Autorità Portuale/Porto di Genova) e i casi d'uso realistici: sorveglianza costiera, sicurezza portuale, ispezione dall'alto di cavi sottomarini (magnetometria aviotrasportata).
- **Attenzione:** la ricerca ha rilevato che nel Golfo di Genova è **già operativo** un servizio di sorveglianza marittima RPAS finanziato da EMSA (European Maritime Safety Agency) tramite il consorzio Tekever (drone AR5, base a Sarzana) per conto della Guardia Costiera italiana. Questo non è necessariamente un ostacolo, ma va capito subito se il posizionamento verso MSC/Autorità Portuale è complementare (es. servizi B2B specifici per il singolo terminal/compagnia, non sorveglianza istituzionale) o in competizione diretta con un fornitore già radicato.
- **Output:** nota di posizionamento sul verticale marittimo, con raccomandazione se includerlo come caso d'uso primario, secondario, o scartarlo.

### WP3 — Trade study di prodotto aggiornato (dopo un primo output di WP1/WP2, 3-4 settimane)
- Aggiornare la matrice di trade-off del Cap. 5 del Piano v1 aggiungendo: vincolo hard C3 (<25 kg), criterio "modularità multi-verticale" (copertura di più segmenti di mercato con lo stesso air segment e payload intercambiabili), coerenza con il verticale vincente identificato in WP1.
- Includere come alternative esplicite, oltre a HALE/MALE/VTOL già presenti nel Piano v1: ala fissa a lancio catapulta/bungee in categoria C3, configurazioni box-wing/joined-wing, tre superfici portanti (canard, già esplorata nel documento "Progetto concettuale struttura HALE").
- **Output:** matrice di trade-off aggiornata + raccomandazione architetturale (o shortlist) con motivazione tracciabile.

### WP4 — Fattibilità tecnica del "prodotto C3 ad alta endurance" (parallelo a WP3)
La ricerca di supporto (§6) mostra che **non esiste sul mercato, ad oggi, un UAV ad ala fissa che combini simultaneamente MTOW < 25 kg, lancio a catapulta/bungee ed endurance reale di 16-24+ ore**: è uno spazio bianco tecnico, non un problema già risolto altrove. Questo può essere letto in due modi opposti, ed è compito di questo WP dirimere quale dei due sia corretto:
- **(a)** è un'opportunità di differenziazione tecnologica genuina (nessuno l'ha ancora fatto bene, chi ci riesce ha un vantaggio);
- **(b)** è un vincolo fisico troppo stringente (il trade-off drag/peso rende la combinazione impraticabile con la tecnologia attuale, e altri l'hanno già scartata per questo).
- Valutare il contributo di configurazioni box-wing/joined-wing (rigidezza strutturale maggiore a parità di peso, apertura alare ridotta 20-30%) e la loro compatibilità con un'eventuale futura integrazione VTOL.
- **Output:** nota tecnica su fattibilità realistica del target C3 + 24h endurance, con raccomandazione su range di endurance realmente perseguibile.

### WP5 — Decisione strategica: prodotto generalista vs due prodotti specializzati (sintesi, dopo WP1-4)
Dal dibattito Gigi/Ema in riunione: un "barcone" generalista attira di più gli investitori (Ema) vs. due prodotti verticalizzati sono più semplici da realizzare e altrettanto efficaci per missione (Gigi). Il framework decisionale deve incrociare:
- risultati WP1 (quanti verticali di mercato sono realmente serviti dalla stessa piattaforma con solo cambio payload?)
- risultati WP3/WP4 (la modularità hardware è davvero a costo marginale basso, o richiede compromessi ingegneristici pesanti?)
- **Output:** raccomandazione motivata, non vincolante fino a questo punto del processo.

### WP6 — Integrazione nel Piano di Fattibilità
- Riscrivere Cap. 1-5 del Piano v1 (Inquadramento, Stakeholder, Requisiti, Scope, Trade-off) alla luce dei risultati WP1-WP5.
- Rivedere solo i punti dei Cap. 6-14 (fattibilità tecnica, CONOPS, costi, regolatorio, rischi, roadmap) effettivamente impattati dalla nuova architettura selezionata — non un rifacimento integrale.
- **Output:** Piano di Fattibilità v2, pronto per la presentazione a investitori/Regione Liguria.

---

## 5. Domande aperte dalla riunione → Research Question con criterio di chiusura

| # | Domanda aperta (dalla riunione) | Work Package | Criterio di chiusura |
|---|---|---|---|
| 1 | Prodotto generalista ("barcone") o due prodotti specializzati? | WP5 | Framework di decisione con dati WP1-WP4, non una preferenza a priori |
| 2 | VTOL, ala fissa tradizionale o box-wing/tre superfici? | WP3, WP4 | Matrice di trade-off pesata con criteri §2 e vincolo C3 |
| 3 | Si riesce a fare <25 kg con 24h+ di endurance? | WP4 | Nota tecnica con range di endurance realisticamente raggiungibile e configurazione consigliata |
| 4 | Che peso avrà il payload e come impatta la scelta piattaforma? | WP1 (requisiti sensori per verticale), WP4 (budget di massa) | Tabella payload-per-verticale con budget di massa associato |
| 5 (nuova, da WP2) | Il verticale marittimo è presidiato da un fornitore incumbent (EMSA/Tekever)? Come ci si posiziona? | WP2 | Nota di posizionamento competitivo |

---

## 6. Sintesi della ricerca esterna di supporto (punto di partenza per WP1-WP4)

*Ricerca effettuata a supporto di questo piano; da approfondire e verificare con fonti primarie nel corso di WP1-WP4, non da considerarsi definitiva.*

### 6.1 Mercato downstream dei servizi drone
- Il segmento **servizi** (non hardware) è già oggi il più grande dell'industria drone: **$29,4 mld nel 2025** a livello globale (Drone Industry Insights), su un mercato commerciale totale che cresce da $40,6 a $57,8 mld entro il 2030.
- **Italia:** mercato professionale B2B/B2G di **€168 milioni nel 2025** (+5% sul 2024, in forte decelerazione rispetto al +29% del 2021), dominato al 95% da ispezione infrastrutture/monitoraggio territorio (Osservatorio Politecnico di Milano).
- **Ispezione infrastrutture critiche** è il segmento globale più maturo e ricorrente: $15,3 mld (2025) → $84,6 mld (2035), CAGR ~19%; in Italia clienti reali e ricorrenti come **Terna** (flotta di 34 droni, 3.500+ tralicci ispezionati/anno) ed E-Distribuzione (Enel).
- **Logistica sanitaria nelle aree interne** ha priorità politica concreta: fondi PNRR Missione 6 già attivi su pilot in Abruzzo, Veneto, Lombardia, Sicilia; 93% dei cittadini italiani favorevole.
- **Connettività HAPS** resta pre-commerciale in Europa: il progetto di punta europeo (EuroHAPS/Stratobus, Thales Alenia Space/Leonardo) è ancora in fase dimostrativa, capital-intensive, non adatto a un operatore di piccola scala.
- **Agricoltura di precisione**: crescita elevata (CAGR 20-38% a seconda della fonte) ma clientela privata frammentata.
- **Conclusione preliminare (da validare in WP1):** per un operatore che vuole vendere *servizi* in aree interne, la combinazione più promettente sulla carta è **ispezione infrastrutture + emergenza/logistica sanitaria rurale**, non necessariamente HAPS/connettività persistente su cui il Piano v1 si è concentrato.

### 6.2 Categoria C3 (<25 kg) ed endurance realistica
- La classe **C3** (Reg. UE 2019/945) copre UAS con MTOM < 25 kg e dimensione < 3 m; abilita operazioni Open A3 (≥150 m da aree residenziali) senza autorizzazione preventiva. Sopra i 25 kg si esce dall'Open category e serve la categoria *Specific* con SORA/PDRA/LUC — onere autorizzativo molto più pesante.
- **Non esiste, verificabilmente, un UAV di produzione reale che combini MTOW < 25 kg + lancio a catapulta/bungee + endurance 16-24h+.** Il caso più vicino è l'**Insitu ScanEagle** (~18-22 kg, lancio a catapulta pneumatica, 18-24h, record 22h08m) ma con classificazioni di peso discordanti tra fonti. Tutti gli altri sistemi a endurance comparabile superano nettamente i 25 kg (AeroVironment T-20: 102 kg/24h+; UAVOS Albatross 2.2: 550 kg/20h). I sistemi coreani reali verificati (Uconsystem RemoEye-006A, 6,5 kg) hanno endurance modesta (~2h).
- **Implicazione per WP4:** il target "C3 + 24h" richiede probabilmente un compromesso — o si accetta un'endurance inferiore (8-14h, come Silent Falcon UAS, 13,6-15,9 kg) restando in C3, oppure si supera i 25 kg e si accetta il regime Specific.

### 6.3 Box-wing e configurazioni alternative
- Il box-wing promette fino al 40% di riduzione della resistenza indotta in teoria, ma il vantaggio si riduce molto imponendo vincoli reali di stabilità; per UAV HALE il **joined-wing** riduce l'apertura alare del 20-30% a parità di portanza con maggiore rigidezza strutturale (programma Boeing/AFRL/NASA "SensorCraft", poi abbandonato per motivi non aerodinamici).
- **Precedenti reali di box-wing + VTOL esistono**: progetto TiltOne (Politecnico di Torino) e un tilt-prop box-wing UAV cinese, entrambi con transizione hover-crociera dimostrata in volo — segnale positivo per una futura integrazione VTOL se necessaria.
- Le configurazioni a tre superfici (canard, tipo Piaggio P180 Avanti, già esplorata nel documento "Progetto concettuale struttura HALE") mostrano benefici misurati ma modesti (+4% L/D) e letteratura scarsa specifica per HALE/MALE.

### 6.4 Mercato marittimo/costiero
- Verticale piccolo ma in crescita, dominato da **committenti pubblici/difesa** (EMSA, Frontex, guardie costiere) più che da clienti commerciali puri.
- **Nel Golfo di Genova è già operativo** il servizio EMSA di sorveglianza marittima con drone Tekever AR5 (base Sarzana) per la Guardia Costiera italiana — incumbent da considerare nel posizionamento (WP2).
- Per cavi sottomarini si usano droni con magnetometro in acque basse (SPH Engineering); il tema è diventato strategicamente rilevante dopo i sabotaggi nel Mar Baltico (2023+) e l'operazione NATO "Baltic Sentry" (2025).
- Non risulta un programma pubblico documentato riconducibile specificamente a MSC al porto di Genova — da verificare direttamente con il contatto Cegeno.

### 6.5 Benchmark di costo HALE vs MALE — la risposta è "dipende dalla categoria di piattaforma"

La ricerca di supporto restituisce un quadro più sfumato di quanto ipotizzato in riunione: **"HALE = centinaia di milioni" è vero solo per una sotto-categoria di piattaforme (ISR pesanti a getto/turboelica derivate da programmi militari), mentre è falso per gli HALE leggeri a energia solare tipo Zephyr**, che è la categoria concettualmente più vicina a ciò di cui si è discusso in riunione. Questa distinzione è probabilmente il singolo dato più importante emerso da questa ricerca per orientare la Fase 2.

**HALE leggeri a energia solare (categoria Zephyr — la più rilevante per il progetto):**
- **Airbus Zephyr**: costo per esemplare **£4-14 milioni / $5-45 milioni** a seconda del contratto (US Navy 2009: ~$5,6M/unità incl. stazione di terra; UK MoD 2016: £10,6M per 2 esemplari, poi £13M per un terzo). Nessun costo di programma complessivo pubblico reperito. Oggi gestito da AALTO HAPS Ltd (controllata Airbus): $100M di investimento da un consorzio giapponese (2024), target di servizio commerciale 2026.
- **BAE Systems PHASA-35**: costo di programma e costo unitario non pubblicamente disclosed; contratto AFRL/NASA fino a $10M (2025-2030) per missioni ISR. Stato: dimostratore operativo.
- **Skydweller Aero**: capitale raccolto totale (equity + prestiti + contratti governativi), non costo di sviluppo di un singolo velivolo: Series A $40M (2021, Leonardo tra gli investitori), prestito BEI €30M (2023), contratti US Navy/DIU $5-14M. Fondato su airframe Solar Impulse 2 riconvertito.
- **Thales Alenia Space/Leonardo Stratobus (EuroHAPS)**: progetto UE da **€63,5M totali** (contributo UE fino a €43M) — ancora in fase dimostrativa, nessun volo full-scale confermato.
- **HAPSMobile/SoftBank Sunglider**: impegni contrattuali cumulativi con AeroVironment 2018-2023 **oltre $200M** in tranche successive — ma nessun costo per singolo esemplare disclosed. Programma assorbito in SoftBank nel 2023.
- **Conclusione categoria "HALE leggero solare"**: costi per esemplare nell'ordine di **decine di milioni**, non centinaia; gli impegni cumulativi pluriennali di sviluppo/investimento possono però avvicinarsi o superare le centinaia di milioni se sommati su più anni e più round.

**HALE/MALE pesanti derivati da programmi militari (per confronto, categoria diversa):**
- **RQ-4 Global Hawk** (Northrop Grumman, HALE ISR a getto): costo unitario **$131-223M** (dati GAO/DoD 2012-13); programma totale **~$13,9 mld/66 velivoli**; export Giappone $490M/3 velivoli (2018), Corea del Sud $657M/4 velivoli (2014).
- **MQ-4C Triton** (derivato Global Hawk, navale): costo unitario in forte crescita, da $286M a **$513-618M/unità** (GAO, 2024) dopo il taglio della produzione da 70 a 27 velivoli.
- **Eurodrone/EuroMALE** (Airbus/Dassault/Leonardo, OCCAR — tecnicamente un MALE, non un HALE): contratto **€7,1 mld, poi rivisto a ≥€7,6 mld**, per 20 sistemi/60 velivoli — costo unitario stimato da terzi ~$114M.
- **General Atomics MQ-9 Reaper/SkyGuardian**: costo unitario **$14-30M** (fino a $50M secondo fonti 2026); contratti export molto variabili: Taiwan $250M/4 velivoli, India $3,9-4 mld/31 velivoli, Germania €1,52 mld/8 velivoli.
- **Conclusione categoria "HALE/MALE pesante militare"**: qui "centinaia di milioni" per esemplare è confermato (Triton) o comunque l'ordine di grandezza corretto per il programma complessivo (miliardi).

**MALE civili/commerciali più leggeri (termine di confronto per il "MALE più appetibile" citato da Fede in riunione):**
- **TEKEVER AR3/AR5** (Portogallo/UK): nessun prezzo unitario pubblico; capitale VC raccolto Series A+B **~€90M** (2022-2024) più investimento industriale proprio £400M/5 anni per scalare produzione UK (non costo di sviluppo prodotto); contratti pubblici aggregati UK-Ucraina £270M cumulativi; valutazione azienda >£1 mld (2025).
- **Elbit Hermes 900/450** (Israele): stime non ufficiali **$2M (Hermes 450) / $6-7M (Hermes 900)** per esemplare nudo; contratti "sistema completo" (velivoli+GCS+sensori+training) tipicamente $25M per 2 velivoli (Messico), $25M/velivolo (India, con trasferimento tecnologico).
- **Baykar Bayraktar TB2** (Turchia, il MALE economico più venduto al mondo, 30+ paesi clienti): costo per esemplare ricostruibile da contratti reali **~4-11 milioni di $/unità** (es. Polonia 2021: $270M/24 velivoli; Marocco 2021: $70M/13 velivoli+GCS; Kuwait 2023: $367M/18 velivoli+munizioni+supporto). Nessun singolo contratto o lotto si avvicina alle centinaia di milioni per esemplare.
- **Conclusione:** i MALE commerciali/civili "leggeri" (TEKEVER, Hermes, TB2) confermano l'intuizione di Fede — sono effettivamente un ordine di grandezza più economici dei grandi HALE/MALE militari pesanti, con costi per esemplare **single-digit/low-double-digit milioni** invece di centinaia.

**Nota di affidabilità:** in questa sessione lo strumento di lettura diretta delle pagine web (WebFetch) è risultato bloccato dalla policy di rete; i dati sopra derivano da sintesi di ricerca (WebSearch) con URL di fonte tracciabili ma non da lettura integrale dei documenti primari. Vanno riverificati con fetch diretto (specialmente i PDF GAO/DoD su Triton e Global Hawk) prima di un uso pubblicativo in un dossier per investitori.

---

## 7. Timeline indicativa

| Settimane | Attività |
|---|---|
| 1-2 | WP0 — Validazione critica Piano v1 + workshop criteri |
| 2-6 | WP1 (mercato downstream) e WP2 (marittimo) in parallelo |
| 5-9 | WP3 (trade study) e WP4 (fattibilità tecnica C3) in parallelo, avviati su risultati preliminari di WP1/WP2 |
| 9-10 | WP5 — Decisione generalista vs specializzato |
| 10-13 | WP6 — Integrazione nel Piano di Fattibilità v2 |

Totale indicativo: **~13 settimane (3 mesi)**, compatibile con un aggiornamento del Piano di Fattibilità senza perdere lo slancio istituzionale già costruito con Regione Liguria e bando Cooding.

---

## 8. Ruoli (da confermare nel workshop WP0)

| Workstream | Owner proposto |
|---|---|
| WP0 (validazione) | Luca + tutto il gruppo |
| WP1 (mercato downstream) | Ema (già orientata all'analisi di mercato) |
| WP2 (marittimo) | Gigi (contatti Cegeno/MSC già suoi) |
| WP3 (trade study prodotto) | Luca + Fede |
| WP4 (fattibilità tecnica C3) | Fede + Gigi (competenze aerodinamiche) |
| WP5 (sintesi strategica) | Luca |
| WP6 (integrazione documento) | Da assegnare (redazione tecnica) |

---

## 9. Rischi del processo di ricerca stesso

- **Rischio "paralisi da analisi":** la Fase A/B va time-boxata (13 settimane, §7) per non perdere lo slancio già costruito con Regione Liguria e il bando Cooding già finanziato.
- **Rischio di ripetere l'errore del Piano v1:** usare dati con specificità sospetta senza fonte primaria (vedi WP0) mina la credibilità verso investitori/istituzioni.
- **Rischio di scope creep sul marittimo:** WP2 va tenuto a "pari profondità" come richiesto in riunione, ma con un chiaro punto di stop se il verticale risultasse presidiato in modo non aggirabile dall'incumbent EMSA/Tekever.
- **Rischio double-work:** il Piano v1 contiene già molto materiale valido (regolatorio, cost model, stakeholder) — WP6 deve integrare, non riscrivere da zero.

---

## 10. Bibliografia di partenza (da consolidare durante WP1-WP4)

*Fonti raccolte nella ricerca esterna di supporto a questo piano; molte sono fonti secondarie (aggregatori di mercato) e vanno incrociate con report primari a pagamento (Teal Group, Drone Industry Insights) prima dell'uso in un business plan definitivo.*

- Drone Industry Insights, *Drone Market Size and Growth 2025-2030* — droneii.com
- Osservatorio Droni e Mobilità Aerea Avanzata, Politecnico di Milano — osservatori.net
- SESAR Joint Undertaking, *European Drones Outlook Study* — sesarju.eu
- EUSPA, *EO and GNSS Market Report* — euspa.europa.eu
- SNS Insider, *Inspection Drones Market Report* — snsinsider.com
- EASA, Regolamento UE 2019/945 (classi C0-C6) e quadro SORA/Specific category — easa.europa.eu
- Insitu/Boeing, ScanEagle/MQ-27 datasheet — insitu.com
- Wiley, *International Journal of Aerospace Engineering* — studi 2025-2026 su UAV HALE joined-wing
- CORDIS H2020, progetto PARSIFAL (box-wing PrandtlPlane) — cordis.europa.eu
- EMSA, servizio RPAS di sorveglianza marittima — emsa.europa.eu
- Defense Industry Daily / Airbus newsroom / FlightGlobal / Aerospace America — cronologia e costi programma Zephyr/AALTO

---

*Documento di lavoro — le cifre di mercato e i benchmark tecnici raccolti in questa fase sono un punto di partenza per la ricerca, non conclusioni definitive. Vanno verificati con fonti primarie durante l'esecuzione dei Work Package.*
