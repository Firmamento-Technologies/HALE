# 07 — Red Team: distruzione della sintesi strategica bottom-up

> **Ruolo.** Revisore avversariale. Unico scopo: dimostrare che `00-SINTESI-strategica.md` è sbagliata, o dove regge male. Non propongo soluzioni (lavoro di altri agenti). Rispetto le due boundary condition (scelta cooperativa; posizionamento sovranità EU/IRIS²) come **dati di progetto**: attacco gli *argomenti a supporto* e il *come*, non le scelte.
> **Bersaglio:** `00-SINTESI-strategica.md`. **Evidenze:** report `01`–`06`. **Data:** 2026-07-08.
> **Verdetto in testa:** **CORREGGERE** (non confermare, non ribaltare). La macro-tesi "nessun velivolo dedicato, HALE fuori portata, mercato piccolo/grant-anchored" **sopravvive** all'attacco. Ma la sintesi (a) sceglie una piattaforma sub-ottimale sulla frontiera che lei stessa disegna, (b) gonfia il SOM con un doppio conteggio, (c) appende €1M a un numero founder inesistente e sfasa il kill-criterion, (d) non fa il competitor reality-check che rivela zero barriere all'ingresso, (e) non affronta che "andare piccolo" **squalifica** il progetto dai fondi R&D che la traiettoria sovrana richiede.

---

## 1. Attacchi alle premesse

1. Premessa non dichiarata: *"persistenza su un punto = deve volare qualcosa."* Falso. Il report `02` (riga 83) dichiara che per la persistenza antincendio (2b — l'**unico** vero differenziatore secondo `02` §4) le **torri camera fisse su crinale (€10-50k/torre, h24)** sono *"concorrente diretto e più economico dell'aereo"*. La sintesi §4 costruisce la wedge su *"un aerostato/drone tethered per la persistenza locale … il vero elemento che nessun sostituto offre"* — affermazione **contraddetta dalla stessa evidenza `02`**. Il sostituto esiste, è a terra, costa 1/10, non cade, non ha limite di vento.
2. Premessa non verificata: *"il differenziatore è la persistenza."* `02` §4 stabilisce che la persistenza serve a **2 soli servizi** (2b incendi, 5 emergenza) e che **entrambi hanno sostituti più economici** (torri fisse; drone tattico in standby). Un differenziatore che vale per 2 nicchie e che in entrambe è battuto da un sostituto **non è un differenziatore**: è un residuo.
3. Termini usati in modo intercambiabile: *"servizio persistente"* oscilla tra (i) hotspot connettività always-on, (ii) early-detection incendi in finestra, (iii) overwatch d'evento. Sono tre prodotti diversi con tre pagatori diversi e tre piattaforme minime diverse. La sintesi li impacchetta in un'unica "wedge" per farla sembrare più densa di quanto sia.
4. Premessa plausibile ma falsificabile: *"la rete cooperativa è radicamento e canale verso la PA."* Il canale PA è una **gara pubblica** (D.Lgs. 36/2023): la cooperativa non ha corsia preferenziale. `03` §2 (riga 2) segnala che ARPAL ha **team droni interno (4 piloti)**: il "canale" è già occupato dall'in-house.
5. Assunzione nascosta: *"i fondi che esistono continueranno a esistere."* La wedge è ancorata a FESR 2021-27 e PNRR. PNRR chiude **2026**; FESR 2021-27 esaurisce la coda ~2028-29; FESR 2028-34 non è definito e il FESR digitale attuale è **€10M, 90% a imprese** (`03` §2). La "solidità per allineamento a fondi che esistono" è una finestra di 2-3 anni, non una base ricorrente.

---

## 2. Attacchi ai numeri

1. **Doppio conteggio del veicolo cooperativo (letale per il SOM).** Le 10 coop sono contabilizzate **come clienti paganti €40-80k/anno** (`03` riga 110, riga "10 coop di comunità bundle") **e simultaneamente come equity conferibile €20-100k** (`06` righe 61, 78, 155). È lo **stesso patrimonio** (`06` §3: €7,8M totali su 106 coop, ~€74k medio, mediana inferiore, illiquido, sotto-media per le 10 liguri). Una micro-coop con **€2-10k di cassa conferibile** non può essere anche cliente stabile da €4-8k/anno: è la stessa tasca vuota contata due volte. Togli una delle due: il SOM base scende sotto €250k, o l'equity floor scende sotto €20k.
2. **Il numero che conta è nascosto.** La headline è SOM €250-500k, ma è **grant+commerciale**. L'unica metrica di business — *ricorrente commerciale non-grant* — è **€120-280k base**, **€30-70k worst** (`03` §0, §5). E `03` §4 assegna al worst **probabilità 30-40%**: non è coda, è esito quasi-modale. L'aspettativa ponderata del business genuino è ~€150-200k, cifra che a malapena serve il debito Marcora e due stipendi.
3. **€1M appeso a un numero che non esiste.** Il Gate 1 della sintesi (§6) richiede *"equity founder €150-350k impegnato"*. `06` §6 (azioni di validazione, punto 4) dichiara che l'impegno di equity founder è *"numero oggi assente dai documenti"*. L'intero edificio "≤€1M" poggia su un buco da €150-350k etichettato "il founder lo riempirà". `06` §5: il floor "in proprio" a M+12 è **€120-300k** — non basta per una flotta.
4. **La regola 2-3x dell'aerospazio è già scattata nei loro stessi dati.** `05` §4: il modello finanziario interno mostra CapEx Y1 "sliding" **€2,5-3,5M** contro nominale €1,4M. Applicando il 2-3x standard al "prudente" €1M si ottiene €2-3M reale = Taglia B, che `06` dà finanziabile al **30-50%** e solo con equity esterna incompatibile col veicolo mutualistico. Il "andare piccolo" **sottostima il costo anche dell'andare piccolo**.
5. **Il worst è distruttivo e non è remoto.** `03` §4: con €30-70k non-grant, *"un investimento >€0,3M distrugge valore"*. Se il worst (35% prob) si avvera, la Taglia A da €1M **non doveva essere costruita**. La sintesi non pesa questo scenario nel disegno dei gate.

---

## 3. Attacchi alla logica

1. **Il "triangolo impossibile" (§3) è in parte un falso dilemma.** La sintesi restringe il vertice B a *"aerostato tethered single-point OPPURE MALE/HALE"* e conclude "due su tre". Ma ha **omesso configurazioni** che stanno sulla stessa frontiera e battono l'aerostato dentro €1M (vedi §5 sotto). L'impossibilità *"sostituto-del-satellite-sotto-€1M"* è reale; ma la **soluzione raccomandata (aerostato) non è il punto ottimo** della frontiera che loro disegnano. Impossibilità genuina + scelta sub-ottimale sono due cose diverse: la seconda è un difetto, non una legge di natura.
2. **Sfasamento gate/kill-criterion (errore di sequenza).** La falsificazione di mercato scatta a **M+24** (`00` §7; `03` §4; `06`), ma l'impegno di CapEx da €1M scatta a **Gate 1 = M+12**, spalmato su 18-24 mesi. Si scopre che il mercato è morto **dopo** aver speso il milione. Il kill-criterion è messo dove non può salvare il capitale.
3. **Argomento circolare sul valore.** §3 conclude *"il valore non è nell'hardware, è nel servizio integrato che la cooperativa gestisce"*. Ma il "servizio integrato" è *"orchestrare Copernicus (gratis) + droni a noleggio"* (`02` §7, `00` §4): un'attività senza asset, senza IP, senza dato esclusivo, senza barriera regolatoria. Dire "il valore è nell'integrazione" senza dimostrare cosa la rende difendibile è spostare l'etichetta, non trovare il valore.
4. **Survivorship/anchoring: la sintesi si ferma all'aerostato per non uccidere sé stessa.** La conclusione onesta bottom-up dei suoi stessi report è *"nessun velivolo posseduto: torri sensori + Copernicus + drone a noleggio"* (`02` righe 70, 83). La sintesi non lo scrive, perché scriverlo rimuove l'ultima ragione per cui esiste una società aero/aerospace. Fermarsi all'aerostato è **conservare un residuo di aviazione** contro la propria evidenza.
5. **Nessun competitor reality-check.** La sintesi non chiede mai: *perché Wesii (Chiavari, 20 km, finanziata Terna €2,8M — `03` riga 52) o ARPAL in-house non aggiungono domani una riga "orchestrazione Copernicus" e mangiano questa wedge?* Risposta: **possono, banalmente.** `03` §3.4: Firmamento *"entrerebbe come una delle 657 [imprese droni], non come categoria nuova"*. Una raccomandazione che non sopravvive a questa domanda non è una strategia.

---

## 4. La configurazione mancante che batte la raccomandazione

Il mandato chiede di testare 4 config che i 6 flussi non hanno considerato. Esito:

- **(b) Infrastruttura FISSA a terra (torri sensori/camera + ripetitore su crinale). → BATTE la raccomandazione.** È la config che detona la premessa aviazione. `02` riga 83 la dà **più economica dell'aereo** proprio per 2b (l'unico differenziatore). Persistenza h24, zero SORA, zero BVLOS, zero spettro, zero batteria, zero limite-vento, €10-50k/torre. Se il vero bisogno è *persistenza su un punto/valle*, la risposta ingegneristica è **non volare**. La sintesi §5 mette "VTOL COTS + 1 aerostato tethered" nella soglia ≤€1M; la config corretta sarebbe "**torri fisse + Copernicus + drone a noleggio, nessun velivolo posseduto**" — ancora più deflazionata, e assente dalla tabella §5.
- **(c) Drone in dock/hangar-in-a-box con ricarica automatica (DJI Dock-class, €30-60k). → BATTE l'aerostato dentro la wedge.** I flussi `02`/`05` scartano il COTS come "non persistente (40-60 min)" (`05` §8) — **errore**: il dock sostituisce l'endurance con il ciclo di ricarica, dando quasi-persistenza a costo COTS, mobile e riposizionabile, con LOS migliore del tether a quota fissa. Mai valutato. A parità di "persistenza in finestra ad alto rischio", costa ~€50k contro €150-700k dell'aerostato. Rende **non cost-ottimale** la piattaforma raccomandata in §5.
- **(a) Rete di 2-3 aerostati/tethered alle imboccature di valle (€60-390k con Elistair, sotto €1M).** Config sotto-esplorata ma **dominata da (b)**: il tether resta a 100-1000 m, non scavalca le creste 400-800 m (`01` §3.2), quindi copre i fondovalle dove lo fanno già le torri fisse — più caro e col rischio-vento moltiplicato per il numero di siti (`05` §5).
- **(d) Noleggio di capacità aerea (drone-as-a-service dai 657 operatori; MALE-as-a-service à la EMSA).** Non "chiude il caso dentro €1M": lo **dissolve**. Se noleggi tutto, la domanda "quale piattaforma" (l'intero framing `01`–`05`) svanisce e Firmamento è un rivenditore di orchestrazione — cioè il problema-barriera del §3.

**Conclusione:** la configurazione mancante che batte la raccomandazione è **(b) infrastruttura fissa a terra**, con **(c) dock COTS** come secondo che batte comunque l'aerostato. Nessuna delle due è nella tabella §5. La sintesi ha scelto l'aerostato — il punto sub-ottimale — perché è l'unico che tiene in vita una parvenza di aviazione.

---

## 5. La wedge è un business o un sussidio? (Front 2)

Sussidio. Prova sui loro numeri: (i) il segmento #1 è dichiarato *grant-anchored* (`00` §4; `03` §7); (ii) il ricorrente non-grant worst è €30-70k (`03` §0); (iii) le coop-clienti sono grant-dipendenti (`03` riga 110 lo scrive); (iv) i €50k Coopfond sono **per lo studio, non per la flotta** (`06` §1). Rimuovi tutte le righe FESR-2021-27/PNRR/coop-sovvenzionate dal SOM `03` §5 e resta ~€40-150k di ricorrente genuino. **Un'entità con ~100% ricavi grant-anchored non è un mercato: è una funzione del ciclo politico dei fondi.** Replicabilità: `03` §1 ammette che lo scale-up SNAI nazionale è ×22 aree *"con gli stessi vincoli di budget"* e ×22 di overhead-bando, senza network effect e con un incumbent GIS/droni per regione. Non è SaaS che scala: è una pratica di consulenza da ricostruire regione per regione. E la coda FESR si ritira (~2028-29) **proprio quando** il debito Marcora (`06` §2, da rimborsare) arriva a scadenza: trappola di solvibilità.

---

## 6. "Andare piccolo" squalifica dai fondi che la sovranità richiede (Front 5)

Rispetto la boundary condition (obiettivo sovrano EU = dato); attacco il **come/funding-attraction**. La money è bimodale: (A) pool piccolo B2G (Coopfond/FESR) che vuole un pilota concreto; (B) pool grande R&D (EDF, Horizon Cluster 4/5, PNRR Aerospazio, EUSPA — `06` §2 righe 11-14) che è **l'unica rampa** che la sintesi stessa lascia per tenere vivo l'HALE come "vettore strategico" (§6 punto 5). Ma quei fondi finanziano **R&D aerospace ambiziosa, non rivendita di Copernicus**. Ridefinendosi "orchestratore asset-light EO", Firmamento diventa **ineleggibile** esattamente per le rampe (B) che servono alla traiettoria sovrana — e raffredda anche il capitale-innovazione cooperativo (Cooding Invest €250k: perché rivendere dati satellitari gratis dovrebbe assorbire €250k di capitale di rischio?). I €50k Coopfond sono arrivati per *"H.A.L.E. – Cooding II – Prototype"* (`06` §1): il nome è HALE, la pitch è aerospazio. La raccomandazione "prudente" cade **nella valle tra i due modi di funding**: troppo deflazionata per convincere il pool grande, troppo affamata di capitale (€1M + founder equity inesistente) per il pool piccolo (ticket €50-250k). Rischio concreto: **non finanziabile per difetto di ambizione**, non nonostante essa.

---

## 7. Steel-man del "no" (perché la sintesi va corretta, non confermata)

Il caso più forte contro la raccomandazione, costruito onestamente: *la sintesi ha fatto bottom-up rigoroso fino a un passo dalla conclusione, e poi si è fermata per autoconservazione.* La conclusione a cui i suoi stessi report `02`/`05` puntano — **"nessun velivolo posseduto; torri fisse + Copernicus + drone a noleggio; il business è ~€40-150k non-grant senza barriera all'ingresso"** — è più deflazionata di quella scritta. Fermarsi all'aerostato non è prudenza: è il punto in cui i dati diventavano incompatibili con l'esistenza di una società aerospace, e la sintesi ha scelto i dati che la tenevano in vita. Questo è il difetto da correggere: **la raccomandazione non è troppo pessimista, è troppo ottimista di un gradino** (tiene un aerostato che le torri fisse battono, tiene un €1M che il founder non ha, tiene un SOM che conta due volte le coop).

---

## 8. Pre-mortem a 5 anni (mid-2031, seguendo ESATTAMENTE questa sintesi)

In ordine di importanza (Klein), non cronologico:

1. **Il mercato era un sussidio e il ciclo è girato.** Il ricorrente non-grant restò a €40-80k; FESR 2021-27 chiuse, PNRR finì (2026), il successore deprioritizzò l'EO-servizio; la Regione monitorò in-house via ARPAL. I ricavi (90% grant-anchored) collassarono. La falsificazione M+24 scattò *dopo* l'impegno CapEx M+12. *(Prob. HIGH; trigger: <€150k non-grant firmato a M+24 — `03`/`06`.)*
2. **L'equity founder non arrivò mai.** Il numero "assente dai documenti" (`06` §6) non si materializzò a scala; la Taglia A si bloccò al floor €300-600k e degradò a Gate 0 (drone demo + rivendita Copernicus). *(Prob. HIGH; trigger: nessun impegno ≥€150k scritto entro M+9.)*
3. **Nessun moat: mangiati da un incumbent.** Wesii (Terna-funded, Chiavari) o ARPAL aggiunsero una riga orchestrazione e servirono la Regione direttamente. Firmamento fu "una delle 657". *(Prob. MED-HIGH; trigger: Wesii/ARPAL bandiscono/erogano l'offerta Copernicus+drone entro 12 mesi.)*
4. **Piattaforma sbagliata comprata.** L'aerostato €150-700k fu vanificato dal vento canalizzato invernale (rischio non testato, `05` §5) *oppure* il cliente scelse una torre camera €30k (`02` riga 83) che faceva meglio l'antincendio. Il dock COTS, mai valutato, sarebbe costato 1/10. *(Prob. MED; trigger: uptime aerostato invernale <60% al primo test anemometrico.)*
5. **Squalificati dalla money grande per essere andati piccoli.** Ridefiniti "orchestratori EO", non poterono più bandire EDF/Horizon/PNRR-Aero credibilmente; l'HALE "vettore strategico" restò senza rampa; Cooding Invest si raffreddò. Fine come micro-consulenza GIS grant-funded, solvibile finché si scriveva il prossimo bando. *(Prob. MED; trigger: primo rifiuto EDF/Horizon con motivazione "TRL/ambizione insufficiente".)*
6. **Il costo esplose 2-3x comunque.** Il "prudente" €1M diventò €2-3M (lo "sliding" €2,5-3,5M dei loro stessi dati, `05` §4), spingendo in Taglia B che richiedeva VC incompatibile col veicolo mutualistico: il round non chiuse. *(Prob. MED-HIGH; trigger: primo consuntivo CapEx >€1,3M a M+12.)*

---

## 9. Falsifying observations (i miei attacchi sono falsificabili)

| Attacco | Osservazione che lo confermerebbe | Osservazione che lo falsificherebbe |
|---|---|---|
| Torre fissa batte aerostato (§4b) | Testa carta-contro-carta: torre €30-50k + ripetitore crinale eroga la SLA antincendio/relay dell'aerostato €150-700k | Un requisito specifico (mobilità, copertura multi-versante) che **solo** l'aerostato soddisfa e la torre no |
| Nessun moat (§3.5) | Wesii/ARPAL assemblano l'offerta Copernicus+noleggio in <6 mesi a costo minore | Un asset esclusivo (dato, licenza, IP, contratto pluriennale blindato) che loro non possono replicare |
| Wedge = sussidio (§5) | Rimosse le righe FESR-2021-27/PNRR, il SOM sopravvivente <€150k | Esiste ≥€200k di ricorrente non-grant firmato indipendente dal ciclo fondi |
| Doppio conteggio coop (§2.1) | Le coop-clienti (`03` €40-80k) sono le stesse coop-equity (`06` €20-100k): rimuovendone una il SOM base <€250k | Le coop pagano da cassa operativa distinta dal capitale conferito, dimostrata sui bilanci 2024-25 |
| Founder equity inesistente (§2.3) | A M+9 nessun impegno scritto ≥€150k | Term sheet/delibera founder ≥€150k datata |

---

## 10. Verdetto

**CORREGGERE.** Non confermabile così com'è, non ribaltabile (la macro-tesi regge).

Cosa correggere, in ordine:
1. **Testare (b) infrastruttura fissa e (c) dock COTS prima di impegnare l'aerostato.** L'aerostato è il punto sub-ottimale della frontiera; le loro `02`/`05` puntano più in basso ("non volare").
2. **Ricostruire il SOM senza il doppio conteggio coop e senza le righe grant a rischio-ciclo**, per esporre il business reale (~€40-150k non-grant) invece di €250-500k.
3. **Spostare la falsificazione di mercato PRIMA del gate CapEx** (verificare la convenzione regionale ≥€100k/anno a M+9, non subire il CapEx e scoprirlo a M+24).
4. **Ottenere il numero founder-equity per iscritto prima di qualunque gate** (oggi assente — `06` §6): senza, il tetto reale è il floor €300-600k, non €1M.
5. **Risolvere esplicitamente la contraddizione ambizione/eleggibilità:** decidere se si insegue il pool piccolo B2G o il pool grande R&D, perché la raccomandazione attuale **abbandona entrambi**.

*Fine red team.*
