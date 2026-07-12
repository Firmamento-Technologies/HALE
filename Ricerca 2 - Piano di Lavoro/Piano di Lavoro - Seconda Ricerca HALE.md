# Piano di Lavoro — Seconda Ricerca Approfondita e Nuovo Studio di Fattibilità H.A.L.E.

**Reset metodologico: dal prodotto al mercato**

| | |
|---|---|
| **Progetto** | H.A.L.E. / Piattaforma aerea per servizi al territorio — Firmamento Technologies |
| **Documento** | Piano di lavoro per la seconda ricerca (nuovo Studio di Fattibilità) |
| **Versione** | 0.1 — bozza per discussione |
| **Data** | 2026-07-12 |
| **Base** | Verbale di riunione (Luca, Fede, Gigi, Ema) + archivio prima ricerca |
| **Destinatari** | Gruppo di progetto Firmamento Technologies |
| **Stato** | Da validare in kickoff (voci contrassegnate `[DA CONFERMARE]`) |

---

## 0. Premessa — perché ripartire da capo

### 0.1 Cosa esiste già (archivio prima ricerca)

La prima ricerca ha già prodotto un corpus consistente, che **non va buttato ma riusato come base dati e come benchmark**:

| Documento (in archivio) | Contenuto | Riuso nella 2ª ricerca |
|---|---|---|
| *Studio di Fattibilità e Analisi Comparativa … (SNAI) Regione Liguria* (≈250 pag.) | Studio completo con metodo Systems Engineering NASA: stakeholder, requisiti, trade-study, V&V, rischi, costi | Base metodologica + dati stakeholder/normativa |
| *Relazione Tecnica Comparativa HALE e VTOL* | Confronto architetturale a due percorsi (6A/6B) | Benchmark tecnico da estendere |
| *Briefing Progetto Piattaforma Aerea* | Sintesi executive | Onboarding rapido |
| *Come può un drone stratosferico rivitalizzare i borghi* | Documento divulgativo/visione | Materiale comunicazione |
| Cartella *Aree interne* | Dossier SNAI, elenco aree, tabella comuni e finanziamenti, rapporto Regione Liguria | Dati mercato "ancora" pubblica (Fase A) |
| Cartella *bando* | Business Plan, progetto/sintesi/piano economico Cooding, elenco 10 cooperative, lettera CdA Coopfond | Vincoli di funding, rete cooperative, struttura costi |
| Cartella *cad* | Immagini concept del velivolo | Punto di partenza design |

### 0.2 I verdetti della prima ricerca (da mettere in discussione, non da assumere)

La prima ricerca era impostata **"vision-first"**: è partita dalla visione HALE e ha costruito attorno un'analisi comparativa. Ha concluso con una **strategia a due percorsi**:

- **Percorso 6A — Pilota VTOL** (piattaforma commerciale tipo JOUAV, TRL 8–9): budget €600k–900k, 0–12 mesi, rischio basso → **GO condizionato**.
- **Percorso 6B — HALE stratosferico** (ala fissa solare, ~20 km, allungamento >40, settimane/mesi): CAPEX €35–65M, 24–48 mesi → **HOLD / Go-condizionato estremo**, per showstopper irrisolti: energia invernale (−30 °C, bassa irradianza), aeroelasticità/flutter, avionica >48 h non COTS, vuoto normativo HAPS, finanziamenti non assicurati.

### 0.3 Il limite metodologico emerso in riunione

Il gruppo ha riconosciuto che **l'ordine va invertito**. Come sintetizzato da Ema: *«io mi concentrerei come prima cosa sull'analisi del mercato, perché è quello che definisce il prodotto … non parto dalle conclusioni, ma dai parametri da massimizzare o minimizzare»*.

La 1ª ricerca ha scelto l'architettura **prima** di dimensionare a fondo il mercato del downstream. La 2ª ricerca deve fare il contrario: **market pull, non technology push**.

### 0.4 Cosa cambia rispetto alla prima ricerca

| Dimensione | 1ª Ricerca | 2ª Ricerca (questo piano) |
|---|---|---|
| **Sequenza logica** | Visione → prodotto (HALE) → mercato a supporto | **Mercato (downstream) → requisiti → prodotto** |
| **Punto di partenza** | Architettura HALE stratosferica | Parametri da ottimizzare + nicchia di mercato |
| **Classe di velivolo** | HALE (>>25 kg) + VTOL commerciale | **Focus C3 < 25 kg** (leggero, modulare) come ipotesi guida |
| **Domini di missione** | Aree interne (connettività, osservazione, emergenze) | Aree interne **+ marittimo/costiero** (pari profondità) |
| **Modularità** | Payload intercambiabile (citata) | **Modularità come criterio di progetto primario** |
| **Endurance target** | Settimane/mesi (HALE) | **24 h+ con velivolo C3** da verificare |
| **Modello** | Servizi > vendita mezzo | Confermato; + verifica "1 prodotto generalista vs 2 specializzati" |
| **Metodo** | Systems Engineering NASA | **Mantenuto** (rigore, tracciabilità, gate) |

### 0.5 Nota strategica su nome e prodotto

"**H.A.L.E.**" ha ormai valore **politico e mediatico** (Telenord, Repubblica, Genova24, ANSA; interlocuzione Regione/Legacoop) ed è legato al bando Cooding. Tuttavia il prodotto tecnicamente ed economicamente realizzabile che emerge dalla riunione (C3 < 25 kg, alta endurance, modulare) **non è un HALE stratosferico in senso stretto**: è più vicino a un MALE leggero / long-endurance ad ala fissa. La 2ª ricerca deve **gestire esplicitamente questo disallineamento nome↔prodotto**, valutando se mantenere "HALE" come ombrello di visione/brand mentre il primo oggetto costruito è un velivolo di classe inferiore. → trattato in **WP-C3** (comunicazione) e **WP-C1** (raccomandazione).

---

## 1. Obiettivi della seconda ricerca

### 1.1 Obiettivo generale

Produrre un **nuovo Studio di Fattibilità decision-ready** che, partendo da un'analisi di mercato del downstream, individui **la nicchia (o le nicchie) a maggior valore** e determini **quale prodotto/architettura** realizzare per servirla, ottimizzando i parametri concordati e massimizzando l'attrattività per investitori e istituzioni.

### 1.2 Il "triplo vincolo"

Il caso è particolare perché il prodotto deve stare all'intersezione di tre domande simultanee:

```
        DOMANDA DI MERCATO (downstream, servizi)
                     ∩
        INTERESSE POLITICO-ISTITUZIONALE (SNAI, Regione, cooperative, Protezione Civile)
                     ∩
        OBIETTIVO DI FINANZIAMENTO/RECUPERO (bandi, pubblico-privato, investitori)
                     =
              PRODOTTO TARGET
```

**Sequenza operativa del vincolo — strategia "ancora → scala" (emersa in Fase A):** i tre insiemi non vanno soddisfatti simultaneamente da zero, ma **in sequenza temporale**. L'**ancora politico-istituzionale** (aree interne/SNAI: bando già vinto, spinta politica, fondi pubblici non diluitivi, primo pilota) **finanzia e legittima** il primo prodotto; il **mercato di scala** (marittimo, domanda ricorrente EMSA-like) ne sostiene la **crescita**. Il ponte è **un unico prodotto multi-ruolo modulare (C3 < 25 kg)**. L'ancora si misura con la **spesa pubblica attivabile**, non con il TAM di mercato.

### 1.3 Funzione obiettivo — parametri da ottimizzare

Criteri emersi in riunione, con direzione di ottimizzazione:

| # | Parametro | Direzione | Note |
|---|---|---|---|
| P1 | Autonomia / endurance | **max** | Target ambizioso 24 h+ |
| P2 | Costo di realizzazione | **min** | CAPEX unitario + sviluppo |
| P3 | Modularità | **max** | Piattaforma + payload plug-and-play |
| P4 | Numero di casi d'uso serviti | **max** | Leva per investitori e per il generalista |
| P5 | Peso (MTOM) | **min** | Ipotesi guida C3 < 25 kg |
| P6 | Attrazione per investitori | **max** | Storytelling + scalabilità + IP |
| P7 | Capacità di attivare funding pubblico-privato | **max** | Bandi, Regione, Coopfond, PNRR, ESA/ASI |
| P8 | Impatto politico e visibilità mediatica | **max** | Coerenza con agenda aree interne |

> ⚠️ **Tensione nota da risolvere nella ricerca:** P1 (endurance 24 h+) e P5 (< 25 kg) sono in conflitto fisico diretto; anche P2 (costo min) vs P4 (max casi d'uso / generalista). La ricerca deve **quantificare i trade-off**, non assumerli risolti.

### 1.4 Vincolo temporale

Tutto è finalizzato alla **consegna dello Studio di Fattibilità** (primo passaggio per convincere a investire). Scadenza assoluta: `[DA CONFERMARE]` (legata al cronoprogramma bando Cooding II / Coopfond). La timeline in §8 è espressa in settimane relative a T0 (kickoff).

---

## 2. Principi metodologici

1. **Market pull, non technology push.** La nicchia definisce il prodotto, non viceversa.
2. **Rigore Systems Engineering mantenuto.** Si conserva l'impianto evidence-based/tracciabile della 1ª ricerca (requisiti "shall", trade-study pesati, V&V, risk register, gate Go/No-Go), applicandolo però alla nuova sequenza.
3. **Catena di tracciabilità unica:**
   `Mercato/Nicchia → Profilo di missione → Requisiti tecnici → Architettura → Costi/Benefici → Raccomandazione → Decisione`.
4. **Riuso dell'archivio.** Dati SNAI, stakeholder, normativa, rete cooperative e struttura costi della 1ª ricerca sono input, non da rifare da zero.
5. **Nessuna conclusione anticipata.** HALE, MALE, VTOL, box-wing restano tutte candidate finché il trade-study non decide.
6. **Gestione esplicita di incertezza.** Ogni affermazione decision-driving è marcata come evidenza, assunzione (`[ASSUNZIONE]`) o open question (`[OQ]`).

---

## 3. Architettura del lavoro — le tre fasi

```
┌─────────────────────────────────────────────────────────────────────┐
│ FASE A — ANALISI DI MERCATO DEL DOWNSTREAM                            │
│ Segmentazione → dimensionamento → domanda pubblica → marittimo →     │
│ competizione → business model → SHORTLIST NICCHIE + requisiti missione│
└───────────────────────────────┬─────────────────────────────────────┘
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│ FASE B — ANALISI COMPARATIVA DEI PRODOTTI (TRADE STUDY)               │
│ Profili missione → catalogo architetture → analisi tecnica first-order│
│ → matrice trade-off → costi/tempi/TRL/rischi → costi-benefici →       │
│ generalista vs specializzati → normativa                             │
└───────────────────────────────┬─────────────────────────────────────┘
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│ FASE C — SINTESI, STUDIO DI FATTIBILITÀ E ROADMAP                     │
│ Raccomandazione integrata → modello economico/funding → impatto       │
│ politico-mediatico → redazione studio → roadmap/pilota/gate           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Fasi e Work Package (WP)

> Legenda WP: **Obiettivo · Attività · Fonti · Output · Domande a cui risponde**

### FASE A — Analisi di Mercato del Downstream

#### WP-A1 · Tassonomia e segmentazione dei servizi downstream
- **Obiettivo:** mappare tutti i servizi erogabili da una piattaforma aerea (downstream), non i velivoli.
- **Attività:** costruire una tassonomia dei segmenti — osservazione/monitoraggio ambientale, prevenzione rischi (incendi, dissesto idrogeologico), connettività (4G/5G, IoT/LoRaWAN, backhaul, emergenza), agricoltura di precisione, ispezione infrastrutture critiche (linee elettriche, dighe, viadotti), monitoraggio coste/confini, logistica/consegne, media/eventi, difesa/dual-use. Per ciascuno: cliente tipo, valore, frequenza, requisiti impliciti.
- **Fonti:** archivio SNAI + report ASI/ESA downstream, EUSPA/EUSPA market report, EASA, letteratura settore UAS-as-a-service, ricerca web mirata.
- **Output:** matrice segmenti × attributi; mappa di calore "valore vs accessibilità".
- **Domande:** quali servizi hanno domanda reale e pagante? quali si legano all'agenda politica?

#### WP-A2 · Dimensionamento del mercato (TAM / SAM / SOM)
- **Obiettivo:** quantificare i segmenti prioritari.
- **Attività:** stima TAM/SAM/SOM per segmento su tre livelli geografici — **Liguria / Italia / EU** (scalabilità). Dinamica di crescita, driver regolatori, spesa pubblica attivabile.
- **Fonti:** report di mercato droni/EO/connettività, bilanci Protezione Civile/Regioni, fondi SNAI (tabella comuni e finanziamenti in archivio), PNRR.
- **Output:** modello di dimensionamento con assunzioni esplicite e scenari (basso/medio/alto).
- **Domande:** dov'è la "nicchia più larga" (Luca)? qual è la scala di ricavo credibile?

#### WP-A3 · Domanda "ancora" pubblico-istituzionale (aree interne)
- **Obiettivo:** consolidare la domanda già presente e politicamente sponsorizzata.
- **Attività:** rileggere i fabbisogni SNAI/aree interne; formalizzare i bisogni delle **10 cooperative** (Fabrica capofila) come utenti-pilota; interlocuzione Regione Liguria / assessore Piana / Legacoop / Protezione Civile; caso Pentema.
- **Fonti:** cartella *Aree interne*, cartella *bando*, elenco cooperative, contatti diretti del gruppo.
- **Output:** requisiti di servizio "ancora" + lettere di interesse/MOU potenziali.
- **Domande:** quanta domanda è "garantita" dal canale politico? quali KPI attesi?

#### WP-A4 · Dominio marittimo e costiero *(nuovo — pari profondità)*
- **Obiettivo:** valutare il mercato marittimo con la stessa profondità (richiesta di Gigi).
- **Attività:** mappare casi d'uso via contatti **Cegeno → MSC / Autorità Portuale**: monitoraggio coste e confini, sorveglianza traffico, ispezione dall'alto di **cavi sottomarini**, supporto subacquea, controllo ambientale marino, sicurezza portuale. Requisiti specifici (autonomia sul mare, sensori, meteo, regolamentazione marittima).
- **Fonti:** contatti Cegeno/MSC/porto, EMSA, Guardia Costiera, letteratura maritime UAS.
- **Output:** scheda dominio marittimo con dimensionamento e requisiti; confronto vs dominio aree interne.
- **Domande:** il marittimo è nicchia primaria, complementare o alternativa? condivide la stessa piattaforma modulare?

#### WP-A5 · Analisi competitiva e benchmark
- **Obiettivo:** capire chi già offre questi servizi e con cosa.
- **Attività:** censimento operatori/piattaforme (droni service provider, HAPS come Airbus Zephyr, MALE, VTOL long-endurance coreani/israeliani citati in riunione, catapulta/lancio elastico), con prezzi di servizio, modelli, punti deboli. Analisi make-vs-buy.
- **Fonti:** ricerca web, schede prodotto costruttori, gare/appalti pubblici comparabili.
- **Output:** landscape competitivo + posizionamento differenziante.
- **Domande:** dove c'è spazio non presidiato? build vs integrazione di piattaforma commerciale?

#### WP-A6 · Modelli di business, pricing e willingness-to-pay
- **Obiettivo:** confermare/qualificare il modello "servizi > vendita mezzo".
- **Attività:** definire modelli (servizio a canone, pay-per-mission, dato-as-a-service, PPP con enti); stimare pricing e willingness-to-pay per segmento; segmento di terra cooperativo (gateway/NOC/data platform).
- **Fonti:** business plan in archivio, benchmark pricing, co-design cooperative.
- **Output:** ipotesi di ricavo per nicchia; unit economics preliminare.
- **Domande:** quale modello massimizza P6/P7? il generalista genera più ricavi del verticale?

#### WP-A7 · Sintesi Fase A — shortlist nicchie + requisiti di missione
- **Obiettivo:** chiudere la Fase A con l'input per la Fase B.
- **Attività:** selezionare 2–4 nicchie prioritarie con tesi di valore; per ciascuna derivare il **profilo di missione** (payload, persistenza, area di copertura, quota, latenza, refresh, meteo).
- **Output:** **Market Analysis Report** + tabella "nicchia → requisiti di missione".
- **Gate A→B:** shortlist e requisiti approvati dal gruppo.

---

### FASE B — Analisi Comparativa dei Prodotti (Trade Study)

#### WP-B1 · Da nicchia a requisiti tecnici (ponte A→B)
- **Obiettivo:** tradurre i profili di missione in requisiti tecnici verificabili ("shall").
- **Attività:** definire, per la/e nicchia/e, i **budget di missione**: massa e potenza payload, endurance, quota, raggio/area, data rate/latenza, condizioni ambientali. **Determinare il peso realistico del payload** (sensori) e il suo impatto sulla piattaforma.
- **Output:** baseline requisiti di sistema (core), matrice tracciabilità Needs→Requirements.
- **Domande:** *(OQ riunione)* qual è il peso effettivo del carico utile e come vincola la piattaforma?

#### WP-B2 · Catalogo delle architetture candidate
- **Obiettivo:** definire l'insieme completo delle opzioni, senza escluderne a priori.
- **Attività:** schedare — **HALE** stratosferico solare · **MALE** leggero · **VTOL ibrido** · **ala fissa** con decollo assistito (catapulta/elastico) · **box-wing** · tail-sitter · configurazioni ibride/retrattili. Per ognuna: principio, pro/contro, TRL, esempi reali.
- **Output:** catalogo architetture con schede tecniche.
- **Domande:** *(OQ riunione)* VTOL vs ala fissa tradizionale vs box-wing per il profilo target?

#### WP-B3 · Analisi tecnica first-order per architettura
- **Obiettivo:** verificare la fattibilità fisica di ciascuna opzione sui requisiti.
- **Attività:** **mass budget**, **energy/power budget**, **link budget**, analisi aerodinamica di massima. Nodo chiave: **quantificare il drag-penalty del VTOL** (motori di sollevamento) vs ala fissa sull'endurance (osservazione di Gigi); e verificare **se un C3 < 25 kg può raggiungere 24 h+**. Sensibilità endurance↔peso↔payload↔propulsione (batteria/solare/ibrido-termico).
- **Output:** schede di fattibilità tecnica + identificazione showstopper/gap TRL per architettura.
- **Domande:** *(OQ riunione)* fattibile C3 < 25 kg con endurance 24 h+? a quali condizioni (payload, propulsione, lancio)?

#### WP-B4 · Matrice di trade-off pesata
- **Obiettivo:** confrontare le architetture sui parametri P1–P8.
- **Attività:** costruire matrice decisionale con **pesi** dei criteri (§6) e scoring tracciabile; analisi di sensibilità sui pesi.
- **Output:** ranking architetture con motivazione; shortlist 1–2 vincitrici.
- **Domande:** quale architettura massimizza la funzione obiettivo per la nicchia scelta?

#### WP-B5 · Costi, tempi, TRL, rischi per architettura
- **Obiettivo:** dimensionare sviluppo e realizzazione.
- **Attività:** per le architetture shortlist: CAPEX sviluppo + unitario, tempi, TRL di partenza, WBS preliminare, risk register tecnico. Riuso stime 1ª ricerca (VTOL €600–900k; HALE €35–65M) come estremi di riferimento.
- **Output:** cost/schedule/risk model per opzione.

#### WP-B6 · Analisi costi-benefici (architettura × nicchia)
- **Obiettivo:** incrociare fattibilità tecnica e valore di mercato.
- **Attività:** matrice costi-benefici per combinazioni architettura×nicchia; ritorno atteso, break-even, sensibilità.
- **Output:** ranking combinazioni; base per la raccomandazione.

#### WP-B7 · Generalista vs specializzati *(domanda aperta della riunione)*
- **Obiettivo:** rispondere in modo argomentato al dilemma Gigi (2 progetti verticali) vs Ema ("barcone" generalista più attrattivo).
- **Attività:** modellare tre strategie di prodotto — (a) piattaforma unica generalista modulare, (b) due velivoli verticali specializzati, (c) piattaforma comune + payload verticali — confrontandole su costo, casi d'uso, time-to-market, attrattività investitori, rischio.
- **Ipotesi guida (da Fase A):** strategia **"ancora → scala"** con **prodotto multi-ruolo modulare** = opzione (c) → piattaforma comune C3 < 25 kg + payload intercambiabili. L'ancora **aree interne/SNAI** (bando vinto, politica, fondi pubblici) aggancia l'interesse e i fondi; il **mercato marittimo** (domanda ricorrente EMSA-like) fa scalare. WP-B7 deve **validare o falsificare** questa ipotesi con i numeri, non assumerla.
- **Output:** raccomandazione motivata sulla strategia di prodotto.

#### WP-B8 · Normativa per la configurazione candidata
- **Obiettivo:** verificare il percorso regolatorio della/e opzione/i vincente/i.
- **Attività:** analizzare categoria **C3 / open A3** (Reg. UE 2019/945 e 2019/947) e i suoi limiti; chiarire che operazioni **BVLOS long-endurance** ricadono verosimilmente in categoria **"specific" con SORA/ENAC** anche sotto 25 kg → il vantaggio del < 25 kg è reale ma parziale. Spettro AGCOM, quadro HAPS (se resta l'opzione stratosferica), regole operazioni marittime.
- **Output:** matrice compliance per opzione; impatto normativo sul trade-off (feedback a WP-B4).
- **Domande:** quanto pesa davvero il vincolo dei 25 kg sul percorso autorizzativo?

---

### FASE C — Sintesi Decisionale, Studio di Fattibilità e Roadmap

#### WP-C1 · Raccomandazione integrata
- **Obiettivo:** convergere su nicchia + architettura + strategia di prodotto + fasaggio.
- **Attività:** integrare Fasi A/B in una raccomandazione con verdetto Go/No-Go/Hold per opzione; gestire il nodo brand "HALE" vs prodotto reale (§0.5).
- **Output:** raccomandazione esecutiva tracciabile.

#### WP-C2 · Modello economico-finanziario e strategia di funding
- **Obiettivo:** rendere il progetto "investibile".
- **Attività:** modello economico (CAPEX/OPEX, ricavi da servizio, TCO), pipeline di finanziamento **pubblico-privato**: Coopfond/Cooding, bandi Regione Liguria, PNRR, **ESA/ASI (downstream)**, Horizon Europe, investitori privati. Struttura costi coerente con quella già impostata (>80% personale qualificato).
- **Output:** piano finanziario + funding roadmap.

#### WP-C3 · Impatto politico e visibilità mediatica
- **Obiettivo:** massimizzare P6/P7/P8.
- **Attività:** definire narrativa e KPI di visibilità; allineare a agenda aree interne/Regione/Legacoop; piano media (riuso track record Telenord/Repubblica/ANSA); gestione coerente del brand HALE.
- **Output:** strategia di posizionamento e comunicazione.

#### WP-C4 · Redazione del nuovo Studio di Fattibilità
- **Obiettivo:** produrre il documento decision-ready.
- **Attività:** stendere lo studio con struttura: Executive Summary → Mercato/Nicchia → Requisiti → Trade-study architetture → Costi-benefici → Normativa → Modello economico/funding → Raccomandazione → Roadmap/Rischi. Mantenere tracciabilità e appendici evidenze.
- **Output:** **Studio di Fattibilità 2.0** + Executive Summary per investitori.

#### WP-C5 · Roadmap, pilota, rischi, gate residui
- **Obiettivo:** definire i passi successivi allo studio.
- **Attività:** roadmap di sviluppo/pilota, risk register finale, open questions residue, criteri Go/No-Go per la fase realizzativa.
- **Output:** roadmap + gate framework.

---

## 5. Domande di ricerca — mapping alle domande aperte della riunione

| Domanda aperta (riunione) | WP che risponde | Metodo / evidenza attesa |
|---|---|---|
| Prodotto generalista ("barcone") vs due prodotti specializzati? | **WP-B7** (+ A6, B6) | Modellazione 3 strategie su costo/casi d'uso/investitori |
| VTOL vs ala fissa tradizionale vs box-wing per il profilo target? | **WP-B2, B3, B4** | Analisi aerodinamica first-order + trade-off pesato |
| Fattibile un C3 < 25 kg con endurance 24 h+? | **WP-B3** | Mass/energy budget, sensibilità peso↔endurance↔propulsione |
| Peso effettivo del payload e impatto sulla piattaforma? | **WP-B1, B3** | Requisiti payload da nicchia → budget di massa |
| Quanto vale davvero il vincolo normativo dei 25 kg? | **WP-B8** | Analisi C3/open vs specific/SORA per BVLOS long-endurance |
| Qual è la nicchia downstream più larga? | **WP-A1, A2, A7** | Segmentazione + TAM/SAM/SOM |
| Il marittimo è nicchia primaria o complementare? | **WP-A4, B6** | Dimensionamento + costi-benefici marittimo vs aree interne |
| Mantenere il brand "HALE" se il prodotto è un C3/MALE? | **WP-C1, C3** | Analisi nome↔prodotto, valore politico-mediatico |

---

## 6. Criteri di valutazione (funzione obiettivo) — pesi proposti

Pesi iniziali `[DA VALIDARE in kickoff]`, usati in WP-B4 e WP-B6. Somma = 100.

| Criterio | Peso proposto | Fonte |
|---|---|---|
| P1 — Autonomia/endurance | 15 | riunione |
| P2 — Costo realizzazione | 15 | riunione |
| P3 — Modularità | 12 | riunione |
| P4 — N° casi d'uso | 12 | riunione |
| P5 — Peso (C3 < 25 kg) | 10 | riunione |
| P6 — Attrazione investitori | 14 | riunione |
| P7 — Funding pubblico-privato | 12 | riunione |
| P8 — Impatto politico/mediatico | 10 | riunione |

**Metodo scoring:** scala 1–5 per criterio, punteggio pesato, analisi di sensibilità sui pesi per verificare la robustezza del ranking.

---

## 7. Deliverable e output

| ID | Deliverable | Fase | Note |
|---|---|---|---|
| D-A | Market Analysis Report (downstream, incl. marittimo) | A | + shortlist nicchie |
| D-A′ | Tabella "nicchia → requisiti di missione" | A/B | gate A→B |
| D-B1 | Baseline requisiti di sistema + RTM | B | |
| D-B2 | Catalogo architetture | B | |
| D-B3 | Schede fattibilità tecnica first-order | B | mass/energy/link budget |
| D-B4 | Matrice trade-off + ranking | B | |
| D-B5 | Cost/schedule/risk model | B | |
| D-B6 | Analisi costi-benefici architettura×nicchia | B | |
| D-B7 | Nota "generalista vs specializzati" | B | |
| D-B8 | Matrice compliance normativa | B | |
| D-C | **Studio di Fattibilità 2.0** + Executive Summary | C | deliverable finale |
| D-C′ | Funding roadmap + piano di comunicazione | C | |

---

## 8. Timeline indicativa (relativa a T0 = kickoff)

> Assoluta `[DA CONFERMARE]` sulla scadenza bando. Durata comprimibile/estendibile secondo risorse.

| Settimana | Attività | Gate |
|---|---|---|
| T0 | Kickoff, RACI, validazione pesi e vincoli | — |
| T0 → T0+4 | **Fase A** (WP-A1…A7) | **Gate A→B** (settimana 4): shortlist nicchie |
| T0+4 → T0+9 | **Fase B** (WP-B1…B8) | **Gate B interim** (settimana 7): fattibilità tecnica |
| T0+9 → T0+12 | **Fase C** (WP-C1…C5) + redazione | **Gate finale** (settimana 12): Studio di Fattibilità |

Milestone chiave: **M1** shortlist mercato (T0+4) · **M2** trade-off architetture (T0+9) · **M3** Studio consegnato (T0+12).

---

## 9. Ruoli e responsabilità (RACI proposto)

La riunione ha lasciato "chi: da definire". Proposta iniziale `[DA CONFERMARE]`, allineata ai profili del piano economico esistente:

| Area | Responsabile (R) | Approva (A) | Contribuisce (C) |
|---|---|---|---|
| Coordinamento / PMO | `[?]` | Luca | Tutti |
| Analisi di mercato (Fase A) | Ema `[?]` | Gruppo | Cooperative, Cegeno |
| Dominio marittimo | Gigi `[?]` | Gruppo | Cegeno/MSC/porto |
| Analisi tecnica/architetture (Fase B) | Fede/Gigi `[?]` | Gruppo | Ing. sistema/aero |
| Normativa/regolatorio | `[?]` | — | ENAC/AGCOM |
| Economico-finanziario/funding | `[?]` | Luca | — |
| Comunicazione/politica | Luca `[?]` | Gruppo | — |
| Redazione Studio | Luca/Gruppo | Gruppo | Tutti |

Profili tecnici richiamabili dal budget bando: ing. sistema aerospaziale, telecom/RF, Modeling & Simulation, EO/GIS, regolatorio, governance dati/cyber, analisi economica.

---

## 10. Fonti e materiale d'archivio da consultare

- **Interne (repo):** cartelle `Aree interne`, `bando`, `cad`, `da revisionare`; *Progetto concettuale struttura HALE.docx*; elenco 10 cooperative.
- **Istituzionali:** SNAI/PSNAI, Regione Liguria (rapporto istruttoria), Coopfond/Cooding, PNRR, ENAC, AGCOM, EASA.
- **Mercato/tecnica:** report EO/connettività/UAS, ESA/ASI downstream, EUSPA, schede costruttori (HAPS, MALE, VTOL, catapult-launch), letteratura aeroelasticità/energia solare/endurance.
- **Marittimo:** Cegeno, MSC, Autorità Portuale, EMSA, Guardia Costiera.
- **Contatti diretti:** Legacoop, assessore Piana, Protezione Civile, rete cooperative.

---

## 11. Rischi del piano di ricerca (meta-rischi) e mitigazioni

| Rischio | Impatto | Mitigazione |
|---|---|---|
| Bias di conferma verso HALE (per brand/lavoro pregresso) | Alto | Trade-study cieco sui pesi; opzioni non escluse a priori |
| Dati di mercato downstream scarsi/opachi | Medio | Triangolazione fonti + interviste stakeholder |
| Scope creep (troppi domini: aree interne + marittimo + …) | Medio | Gate A→B che forza shortlist 2–4 nicchie |
| Conflitto irrisolvibile P1↔P5 (endurance vs 25 kg) | Alto | Quantificare a WP-B3; ammettere fasaggio prodotto |
| Disallineamento nome/prodotto verso investitori/politica | Medio | Strategia brand esplicita WP-C1/C3 |
| Scadenza bando non nota → timeline a rischio | Medio | Confermare T0 e deadline in kickoff |

---

## 12. Prossimi passi immediati (kickoff)

1. **Confermare** scadenza Studio di Fattibilità e T0 (→ timeline §8).
2. **Assegnare** i RACI (§9) e i pesi dei criteri (§6).
3. **Validare** la lista delle nicchie candidate di partenza (§4 WP-A1) e l'inclusione del dominio marittimo.
4. **Attivare** i contatti (cooperative, Cegeno/MSC, Regione) per input Fase A.
5. **Avviare WP-A1–A2** (segmentazione + dimensionamento) come primo blocco operativo.

---

*Documento di lavoro. Le voci `[DA CONFERMARE]` / `[DA VALIDARE]` vanno chiuse nel kickoff. Impostazione metodologica coerente con la 1ª ricerca (Systems Engineering, evidence-based), con sequenza invertita: prima il mercato, poi il prodotto.*
