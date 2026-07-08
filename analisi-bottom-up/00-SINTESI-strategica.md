# 00 — Sintesi strategica: ripartenza da zero (service-first) — **v2, post red-team**

> **Natura del documento.** Sintesi di sei ricerche indipendenti condotte *ripartendo da zero*, senza assumere le conclusioni pregresse dello Studio (impianto 6A/6B, scelta HALE/JOUAV). La piattaforma è stata trattata come **variabile da determinare**, non come premessa. Ogni flusso aveva mandato di **falsificare** l'idea, non di difenderla. Documento di **supporto alla decisione**, non verdetto chiuso.
>
> **v2:** revisione dopo l'attacco del Red Team (`07-REDTEAM-sintesi.md`). Esito red-team: **la macro-tesi regge** (nessun velivolo dedicato chiude il caso; HALE fuori portata; mercato piccolo e grant-anchored), ma tre dettagli erano **piegati a favore del "vai piccolo"** e sono stati corretti (marcati ⚠️→✅). Confidenza dichiarata per ogni claim.
>
> **Fonti:** i sei report `01`…`06` + red-team `07` + script `lb_bottomup.py`.

---

## 1. La domanda, ribaltata

Non *"come costruiamo un HALE?"* ma:

> **Qual è il servizio che serve alle Aree Interne, quanto vale, e qual è la soluzione minima e finanziabile che lo eroga con il miglior rapporto costi/benefici?**

Nota: *soluzione*, non *velivolo* — perché (vedi §3) la risposta migliore potrebbe **non volare affatto**.

---

## 2. Cosa dicono i sei flussi (convergenza)

| # | Flusso | Verdetto sintetico | Confidenza |
|---|--------|--------------------|-----------|
| 1 | **Connettività** | Il link RF **non è il vincolo** (D2D chiude a ogni quota per prossimità). Ma per la **sola banda larga Starlink batte l'aereo di 1–3 ordini di grandezza**. Razionale solo come *resilienza d'emergenza / IoT d'area*, connettività **secondaria**. | Alta (link/prezzi); Media (quota) |
| 2 | **Osservazione Terra** | Maggior parte dei servizi EO **dominata da Copernicus (gratis) o drone COTS a noleggio**. Unico discriminante: **persistenza**, utile a **2 servizi** (early-detection incendi, overwatch emergenza) — e **anche lì le torri fisse a terra €10–50k battono l'aereo**. | Alta (fatti); Media (economia) |
| 3 | **Mercato** | Mercato pagante **piccolo**. ⚠️→✅ *Corretto*: al netto del doppio conteggio coop, il **ricorrente non-grant reale è ~€40–150k/anno**; il SOM €250–500k regge **solo includendo grant a rischio-ciclo**. HALE (€5,5–11M) **non ripagato di 1–2 ordini**. | Alta (budget); **Bassa (SOM)** |
| 4 | **Regolatorio** | Compliance cresce **a scalini** → minimo attrito **spinge verso il basso**. **C3 <25 kg Open A3 subito** (€1–5k) → **piccolo UAS BVLOS Specific SAIL II**. HALE = Certified, 5–8 anni, **nessun framework HAPS**. | Alta (categorie); Media (SAIL) |
| 5 | **Costi piattaforme** | **Buy COTS batte build custom.** Box-wing C3 custom→certificato = **€3–10M+**. **Aerostato tethered** (€150–700k) dà persistenza senza flotta — ma su **un solo punto**, e ⚠️→✅ *battuto dalle torri fisse / dal drone-in-dock*. | Alta (COTS); Media (custom) |
| 6 | **Finanziabilità** | Tetto "sicuro" **~€1M** (60–75%), **non facile**: stacking 5–6 strumenti + **equity founder €150–350k** + CapEx su 18–24 mesi. Coop con cassa minima **non coprono il cofinanziamento**. Taglia B (€3–8M) solo con equity esterna + SpA. HALE fuori portata. | Alta (Coopfond €50k certo); Media (mix) |

**Convergenza netta:** *piccolo, COTS o addirittura a terra, sotto €1M, servizio territoriale grant-anchored; HALE (e in gran parte MALE) fuori portata di questo veicolo.*

---

## 3. Il risultato scomodo: il "triangolo impossibile" — e la sua soluzione *a terra*

I tre vertici che vorremmo tutti insieme:

- **(A) Servizio che si differenzia davvero** dai sostituti gratuiti/economici (Starlink, Copernicus, droni COTS). Unico candidato reale: **presenza persistente** (resilienza d'emergenza + overwatch continuo).
- **(B) Soluzione finanziabile & a basso attrito regolatorio** (sotto ~€1M).
- **(C) Finanziabile dall'ecosistema cooperativo** (tetto ~€1M).

**Se ne ottengono due, non tre:**

| Vuoi… | Ottieni | Ma violi |
|---|---|---|
| Persistenza **su area vasta** (A) | ≥8–12 km + endurance multi-giorno → **MALE/HALE** | **B** e **C** (decine–centinaia di M€) |
| Soluzione economica & finanziabile (B+C) | copertura di **un solo punto/valle**, o EO spot | **A** (dominato dai sostituti) |

**Conseguenza (confidenza medio-alta):** *non esiste una **piattaforma aerea** dedicata che chiuda il business case come "sostituto del satellite" dentro l'inviluppo finanziabile.* La cornice "pseudo-satellite" **non sopravvive all'urto con Starlink + Copernicus**.

**⚠️→✅ Correzione red-team — la risposta migliore potrebbe non volare.** Se il vero bisogno è *persistenza su un punto* (una testata di frana, un versante boscato a rischio incendio, un ripetitore di valle), la soluzione ingegneristica dominante **non è un aerostato né un velivolo, ma infrastruttura FISSA a terra**: torri sensori/camera + ripetitore su crinale, **€10–50k/sito**, persistenza h24, **zero SORA/BVLOS/spettro/vento**. Lo dice il report EO stesso (`02`, il "concorrente più economico dell'aereo" per l'early-detection). Dove serve *mobilità* tra siti, il gradino successivo è un **drone COTS in dock con ricarica automatica (~€50k)**, non l'aerostato €150–700k. **L'aerostato/velivolo entra solo se serve coprire più punti mobili o una geometria che una torre non vede** — un caso da dimostrare, non da assumere.

Morale: *più si guarda onestamente al bisogno di Pentema, più la componente volante si assottiglia.* Questo **non** uccide il progetto: sposta il baricentro **dall'hardware al servizio**.

---

## 4. La nicchia difendibile (se c'è)

> **Operatore cooperativo di servizi territoriali di monitoraggio & resilienza per le Aree Interne**, *asset-light*, che **orchestra**:
> 1. **Copernicus** (gratis) per il wide-area lento (frane, vegetazione, post-incendio);
> 2. **droni COTS on-demand** (propri o a noleggio) per il dettaglio point-in-time;
> 3. **persistenza locale** nelle finestre ad alto rischio — **prima con infrastruttura fissa a terra / drone-in-dock**, e *solo se dimostrato necessario* con aerostato/velivolo;
> 4. **connettività d'emergenza/IoT d'area** come funzione **secondaria** (LoRa 868 subito; broadband solo via hosting MNO, non banda HAPS dedicata).

Il differenziatore **non è il velivolo**: è **il servizio persistente, locale, organizzato + la resilienza in emergenza + il radicamento cooperativo** verso la PA.

**Segmento pagante-àncora:** B2G territorio (Regione Liguria + Unioni SNAI + Enti Parco + Protezione Civile), grant-anchored.

**⚠️ Avvertenza red-team (barriera all'ingresso).** "Orchestrare Copernicus + droni" è ciò che **società di rilievo/GIS già fanno** (es. **Wesii**, Chiavari — la stessa che Terna finanzia). La cooperativa vince **solo** se la barriera è **non-tecnologica**: mandato pubblico/convenzione pluriennale, radicamento SNAI, mutualità con i Comuni. Se la barriera è tecnologica, **perde**. Da verificare, non da dare per scontato.

---

## 5. La soluzione che ne deriva (per soglia di budget)

La soluzione **non si sceglie a priori**: la seleziona il budget finanziabile — e parte **da terra**.

| Soglia | Soluzione con miglior costi/benefici | Cosa eroga |
|---|---|---|
| **≪ €1M (partenza)** | ✅ **Infrastruttura fissa a terra** (torri sensori/camera + ripetitore, €10–50k/sito) + **orchestrazione Copernicus** + **drone COTS spot** (€40–120k) | Persistenza h24 su punti fissi + EO d'area + IoT. **Zero SORA. Massima finanziabilità.** |
| **≤ €1M (target)** | **Drone COTS in dock** (~€50k, quasi-persistenza mobile) + eventuale **piccolo UAS BVLOS Specific SAIL II** | Aggiunge mobilità tra siti e EO BVLOS di valle. |
| **~€0,3–0,7M (solo se giustificato)** | **Aerostato tethered** (Elistair/Hemeria) | Persistenza single-point **mobile** — *solo se una torre non basta e il vento di valle lo consente* (non verificato). |
| **< decine di M€** | Flotta **VTOL heavy ridondante** (2–3 unità, €2–5M) o **MALE** (benchmark EMSA €7,5–8,75M/anno) | Persistenza su area più ampia. **Richiede equity esterna + SpA.** |
| **centinaia di M€** | **HALE stratosferico** | Copertura regionale persistente. **Fuori portata del veicolo cooperativo.** |

**Build vs Buy:** *Buy COTS* vince per il servizio Y1. Costruire custom (box-wing C3, o HALE) ha senso **solo** come **banco-prova IP** di lungo periodo, **finanziato a parte** (R&D UE) e **scorporato dal P&L del servizio** — vedi §8, dove questa scelta diventa il vero bivio.

---

## 6. Raccomandazione operativa (a gate) — *demand-first*

⚠️→✅ *Correzione red-team: la prova di domanda viene **prima** dell'impegno CapEx, non dopo.*

1. **Riorientare lo Studio (€100k, Coopfond €50k già deliberati):** da "fattibilità di un HALE" a **"fattibilità di un operatore cooperativo di servizi territoriali di monitoraggio e resilienza"**, con la soluzione tecnica come *scelta derivata*.
2. **Gate 0 — subito, <€30k, PROVA DI DOMANDA:** drone **C3 Open A3 VLOS** + Copernicus su un caso reale; obiettivo **non tecnico ma commerciale**: ottenere **1 LoI Regione Liguria + 1 convenzione Ente Parco/Unione SNAI**. **Nessun CapEx di piattaforma finché non c'è un ente che firma.**
3. **Gate 1 — solo dopo la firma, ≤€1M su 18–24 mesi:** persistenza (**prima torre fissa / drone-dock**, aerostato solo se necessario) + IoT/emergenza via MNO. **Condizioni d'ingresso, per iscritto:** (a) ≥1 convenzione regionale pluriennale; (b) **equity founder €150–350k impegnata con delibera** (oggi assente: `06` §6).
4. **Gate 2 — solo con ricavi dimostrati:** Taglia B (VTOL/MALE) con SpA + equity di rischio.
5. **Traiettoria HALE:** **vettore strategico Y6+** e **linea R&D separata** (vedi §8), **non** procurement del servizio.

---

## 7. Pre-mortem e criteri di falsificazione (kill criteria)

⚠️→✅ *La falsificazione di mercato è stata spostata **prima** del gate CapEx.*

- **PRIMA del Gate 1 (≈M+9–12):** se **nessun ente firma** una convenzione ≥ €100k/anno *o* una LoI vincolante → *il mercato è falsificato **prima** di spendere*; il progetto resta al perimetro Gate 0 (servizio a noleggio/grant, zero CapEx).
- **Gate 1:** il **founder non delibera l'equity** €150–350k → il cofinanziamento del €1M non si chiude (le coop non hanno cassa) → non si supera Gate 0.
- **Persistenza:** se **una torre fissa a terra risolve il bisogno**, l'aerostato/velivolo **non entra** (kill della componente volante a Y1).
- **Connettività:** **Starlink Direct-to-Cell** raggiunge copertura utile → la componente connettività (già secondaria) diventa **irrilevante**.
- **Barriera all'ingresso:** se un competitor GIS/rilievi (Wesii, ecc.) o la Regione in-house eroga lo stesso servizio → la wedge cade se la barriera non è il mandato pubblico/cooperativo.
- **M+24 (verifica di sostenibilità):** manca **≥€150k di ricorrente non-grant** *o* la convenzione regionale non si rinnova → il "business" è un **sussidio a termine**, non un mercato; riconsiderare l'intera iniziativa.

---

## 8. Il bivio irrisolto: **ambizione vs eleggibilità** (la decisione che spetta all'utente)

Il red-team solleva la tensione più importante, che i sei flussi *singolarmente* non vedono. Ci sono **due pool di denaro**, con requisiti **opposti**:

| | **Pool A — piccolo B2G territoriale** | **Pool B — grande R&D aerospazio/sovranità** |
|---|---|---|
| Fonti | Coopfond, FESR Liguria, SNAI, convenzioni PA | PNRR-Aerospazio, Horizon Europe, EDF, EUSPA, CDP Venture |
| Premia | servizio concreto, asset-light, ricavi vicini | **ambizione tecnologica**, IP, sovranità EU, TRL-raising |
| Taglia | €50k–€1M | €1M–€30M+ |
| La versione "vai piccolo/COTS"… | **✅ è eleggibile** | **❌ la squalifica** ("non è abbastanza aerospazio") |
| La versione "HALE ambizioso"… | ❌ troppo grande/rischioso | **✅ è il suo target** |

**Il rischio della raccomandazione prudente (§4–6):** cadere **tra due sedie** — troppo piccola per essere un business autosufficiente (mercato €40–150k non-grant), troppo poco ambiziosa per attrarre i fondi R&D che ripagherebbero la traiettoria HALE. Un pilota COTS+torri da €1M potrebbe **respingere** il capitale ambizioso invece di attrarlo.

**Le tre strade possibili — è una scelta di posizionamento, non tecnica:**

1. **Servizio puro (asset-light).** Massimizza Pool A. Accetta di essere una società di servizi territoriali con margini piccoli e grant-dipendente. HALE abbandonato. *Basso rischio, basso upside, dubbia sostenibilità non-grant.*
2. **R&D-first (banco-prova IP).** Il servizio Pentema è la **dimostrazione applicativa** di una linea R&D (box-wing → HALE) che punta a Pool B. Il velivolo custom torna in gioco **come oggetto di ricerca finanziata**, non come procurement. *Alto upside, alto capital-need, il servizio è il pretesto non il fine.*
3. **Barbell (raccomandata per lo Studio).** Tenere **entrambi scorporati**: (a) un **servizio Gate-0/1 asset-light e autofinanziabile** su Pool A (torri+COTS+Copernicus, la parte che *sopravvive alla falsificazione*), **e** (b) una **linea R&D separata** che candida la traiettoria box-wing/HALE ai fondi Pool B, **senza** contaminare il P&L del servizio né appendere il servizio al successo dell'R&D. Lo Studio di Fattibilità li presenta come **due gambe indipendenti con una narrazione comune** (sovranità + Aree Interne), così nessuno dei due pool viene respinto dall'altro.

> Questa è **la** domanda che la ricerca mette sul tavolo e che non può decidere al posto tuo: **Firmamento vuole essere un operatore di servizi territoriali, un attore di R&D aerospaziale, o gestire consapevolmente entrambi in parallelo?** La piattaforma — e persino il *se* volare — discende da questa scelta.

---

## 9. Cosa cambia rispetto all'impianto pregresso

- L'impostazione **6A (VTOL) / 6B (HALE)** partiva dalla **piattaforma**; qui la soluzione è **derivata** da servizio+budget → l'esito naturale è **più in basso** (fino a *terra*) di quanto lo Studio assuma.
- L'allegato SORA (`A11`) fissa **SAIL III** su densità sovrastimata; a Pentema (<5 ab/km²) un piccolo UAS è **SAIL II** → scendere di piattaforma abbassa anche l'onere regolatorio.
- Il capitolo mercato (`cap-07`, SOM €1,5–3,5M) è **non supportato**; il ricorrente non-grant realistico è **€40–150k/anno**.
- La tesi "operatore di servizi, non OEM" **è corretta** e va spinta oltre: il vantaggio è nell'**integrazione di servizio asset-light**, non nell'hardware — ma **attenzione al bivio §8**.

---

### Riga di fondo

> Ripartendo da zero, la ricerca **non** conferma un velivolo dedicato come risposta — e nel caso della persistenza single-point suggerisce di **non volare affatto** (torri fisse). Conferma un **servizio territoriale cooperativo asset-light** sotto €1M, con connettività secondaria e HALE relegato a R&D di lungo periodo. La domanda decisiva **non è più "quale velivolo"** ma due:
> 1. **operativa:** *esiste un ente disposto a firmare e pagare la persistenza?* → è il **primo esperimento** (Gate 0, <€30k), prima di ogni CapEx.
> 2. **strategica (§8):** *Firmamento vuole fare servizi, R&D, o entrambi in barbell?* → è la scelta di posizionamento che seleziona tutto il resto.
>
> Costruire un aereo, oggi, è la risposta a nessuna delle due.
