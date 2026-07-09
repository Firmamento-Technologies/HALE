# 18 — Rivalutazione: box-wing con tilt-rotor, alla luce di ODYS Aviation e del lignaggio SUPAERO/Prandtl (TiltOne)

> **Cosa è.** Rivalutazione mirata, richiesta dall'utente, dell'ipotesi **box-wing + 4 tilt-rotor** — l'architettura che `14` §9 e `22` §2.2 avevano liquidato come "complicata (dove ruota?)". Prende sul serio due riferimenti esterni forniti dall'utente (**ODYS Aviation** e **"SUPAIR"**), verifica se ribaltano il verdetto "box-wing = dimostratore, non prodotto", e aggiorna onestamente dove l'evidenza lo impone.
>
> **⚠️ Caveat fonti (forte).** Il download integrale dei PDF/pagine (WebFetch) è stato bloccato con **HTTP 403** dall'egress dell'ambiente (ODYS, arXiv, NATO STO, Emerald, Springer). L'analisi si basa su **sintesi WebSearch con triangolazione** su più risultati: ogni fatto ha una fonte citata ma **va riverificato sul PDF/pagina primaria** prima dell'uso in documenti per finanziatori. **Confidence aggregata: MEDIA.**
>
> **⚠️ Nota su "SUPAIR".** Non è stato possibile confermare un progetto/azienda con il nome esatto "SUPAIR". Il riscontro più coerente col contesto (box-wing VTOL tiltante) è il **lignaggio accademico SUPAERO/Prandtl** — in particolare il progetto **TiltOne** (box-wing tilt-wing, "Best Wing System" di Prandtl). Se l'utente intende una fonte specifica diversa, va indicata e questa sezione va aggiornata.

---

## 1. Cosa sono davvero i due riferimenti (e perché il dettaglio cambia tutto)

### 1.1 ODYS Aviation — box-wing, ma **NON tilt-rotor**: è *blown lift*
[Fonti: [Aviation Week](https://aviationweek.com/aerospace/aircraft-propulsion/odys-takes-uncrewed-cargo-route-fielding-evtol), [FlightGlobal](https://www.flightglobal.com/airframers/2022/04/odys-aviation-pitches-unique-vtol-as-replacement-for-regional-airliners/), [New Atlas](https://newatlas.com/aircraft/odys-evtol-interview-james-dorris/), [Aerospace Global News](https://aerospaceglobalnews.com/news/fiji-airways-odys-vtol-trial-2026/)]

- **Configurazione:** box-wing con **eliche fisse** distribuite lungo le ali + **flap ipersostentatori** al bordo d'uscita. In decollo/hover i flap deflettono il flusso verso il basso (**blown lift / deflected slipstream**), generando portanza **senza alcun meccanismo di tilt**. In transizione i flap si retraggono e l'ala genera portanza in modo convenzionale.
- **Punto chiave [FATTO, alta confidence]:** ODYS **rinuncia deliberatamente** al tilt-rotor e al tilt-wing — la sua tesi di vendita è proprio *"evitare la complessità meccanica del tilt"* e ridurre la turbolenza in transizione. **Quindi ODYS non è un esempio di "box-wing + 4 tilt-rotor": è un esempio di box-wing che ha scelto un'integrazione VTOL alternativa al tilt.**
- **Scala e mercato:** velivolo **regionale ibrido-elettrico da 9 posti**, ~555 km/h, 750 mi ibrido / 200 mi elettrico. Percorso di ingresso: **cargo senza pilota** prima del passeggeri; primi flight test con Fiji Airways attesi **2026**. È un *airliner regionale*, migliaia di kg — **scala e missione lontanissime dal C3 (≤25 kg) di Firmamento**.

### 1.2 "SUPAIR" ≈ lignaggio SUPAERO/Prandtl — il progetto **TiltOne**
[Fonti: [Emerald AEAT "Preliminary design of a box-wing VTOL UAV"](https://www.emerald.com/insight/content/doi/10.1108/aeat-06-2019-0121/full/html), [Springer Aerotecnica Missili & Spazio "Preliminary design of a Tiltwing UAV with a box wing configuration"](https://link.springer.com/article/10.1007/BF03406054), [NATO STO MP-AVT-323-27](https://publications.sto.nato.int/publications/STO%20Meeting%20Proceedings/STO-MP-AVT-323/MP-AVT-323-27.pdf), [ResearchGate](https://www.researchgate.net/publication/337700902_Preliminary_design_of_a_box-wing_VTOL_UAV)]

- **Configurazione:** **TiltOne** è un box-wing **tilt-WING** con **4 eliche montate su 2 ali basculanti** (una anteriore bassa + una posteriore alta con gap verticale = schema box/Prandtl). Le due ali ruotano di 90° insieme ai gruppi motore-elica: **da multicottero (ali verticali) a box-wing (ali orizzontali)**. Full electric, propulsione distribuita, dimensionato con codice di ottimizzazione in-house; realizzato un **prototipo per test di volo verticale preliminari**.
- **Punto chiave [FATTO, media confidence]:** la versione "reale" del **box-wing con 4 eliche tiltanti** non usa **4 nacelle indipendenti** (l'ipotesi problematica "dove ruota?" di `22`), ma **fa ruotare le due ali** — ciascuna porta 2 eliche. È **l'obiezione geometrica risolta elegantemente**: il pivot è l'asse dell'ala, non 4 giunti separati su un anello chiuso.
- **Maturità:** **ricerca/dimostratore** (preliminary design + primi test verticali). Nessun prodotto commerciale.

### 1.3 Ecosistema di riscontro (per triangolazione)
- **Elytron / VTOL Aerospace "Converticopter":** ala chiusa/box + **2 tilt-rotor centrali**, apertura ~2,4 m, mercato UAV (SAR, border patrol, ispezioni). Concept di lunga gestazione, **nessun prodotto commerciale** ([New Atlas](https://newatlas.com/converticopter-uav-vtol-aerospace/51128/)).
- **Letteratura:** IEEE *"Transition Flight Control and Test of a New Kind Tilt Prop Box-Wing VTOL UAV"* ([IEEE Xplore](https://ieeexplore.ieee.org/document/8467657/)) — box-wing **tilt-prop** (eliche tiltano, ali fisse), testato in transizione; *"variable pitch quadrotor biplane VTOL for payload delivery"* ([arXiv 1801.02938](https://arxiv.org/pdf/1801.02938)) — quad biplano tail-sitter per consegna. → esiste un **corpo di ricerca reale** su box/biplano + eliche tiltanti, in tutte le varianti (tilt-wing, tilt-prop, tail-sitter).

---

## 2. Cosa CORREGGO del giudizio precedente (update onesto)

L'utente ha ragione su un punto e la disciplina epistemica impone di dirlo:

1. **La liquidazione "box-wing + tilt-rotor = complicato, dove ruota?" (`22` §2.2, ripresa in `14` §9) era troppo sbrigativa.** L'architettura **esiste, è studiata e in parte volata** (TiltOne, Elytron, tilt-prop IEEE). La versione sensata **non** monta 4 tilt indipendenti su un anello chiuso: **fa tiltare le due ali del box** (tilt-wing-box) — e così l'obiezione geometrica cade. Va accreditato.
2. **`14` non aveva valutato il *blown lift* (deflected slipstream) come opzione di integrazione VTOL.** ODYS mostra che, per un'ala box/chiusa, il blown lift è un'alternativa reale a lift+cruise e al tilt: **niente rotori di sostentamento morti in crociera, niente meccanismo di tilt** — gli stessi motori/flap fanno hover e crociera. È una **lacuna di copertura** del trade study `14`, da colmare.
3. **Quindi il box-wing-tiltante passa, nella mia valutazione, da "incoerente" a "coerente ma immaturo e control-hard".** Non è un dettaglio: è un cambio di categoria del giudizio.

## 3. Cosa NON cambia (red-team: dove l'update si ferma)

Prese sul serio le fonti, **nessuna ribalta il verdetto "box-wing = dimostratore, non prodotto operativo"** — anzi lo **rafforzano**:

1. **Tutti i casi reali sono dimostratore / ricerca / pre-commerciale.** TiltOne = prototipo accademico. ODYS = primi flight test 2026, via cargo-uncrewed, **non ancora in servizio**. Elytron/Converticopter = concept mai commercializzato in 10+ anni. **Nessun box-wing VTOL eroga un servizio operativo oggi.** I riferimenti forniti dall'utente sono, essi stessi, **dimostratori** — coerente con `40`/`30`/`22`.
2. **Scala non trasferibile.** ODYS è un **regionale da 9 posti** (migliaia di kg): i benefici strutturali/aerodinamici del box-wing scalano col quadrato/cubo e con il Reynolds — **non si trasferiscono al C3 da 25 kg**. Gli analoghi alla scala giusta (TiltOne, Elytron, quad biplani accademici) sono **esattamente quelli fermi allo stadio di ricerca**.
3. **Il verdetto aerodinamico a C3 regge.** `R6`/`22` avevano stabilito vantaggio d'ala ≈0% a C3 (regime attrito-dominato, crossover Re≈4×10⁵). **Nessuna delle fonti fornisce un dato di efficienza di crociera a scala C3 che lo smentisca** (i numeri ODYS sono a scala regionale; TiltOne è preliminary design senza dati di crociera pubblicati). Il caveat 403 impedisce di leggere i PDF: finché non si leggono, **non c'è misura che falsifichi il ≈0%**.
4. **`14` §9 regge sul punto dominante:** il CD0 di un VTOL C3 è dominato dall'hardware VTOL (~72%) non dall'ala (~28%). Il blown lift **attenua** questo (meno rotori esposti) ma **non lo annulla** a piccola scala (servono comunque motori/flap potenti e superfici grandi); il tilt-wing-box **riduce** i booms ma **aggiunge** il giunto di tilt di un'intera ala — il regime di controllo più duro (`14` §4.5, famiglia A4).
5. **Base-rate.** Il box-wing è "promettente" in accademia da Prandtl (1924) ed Elytron (~2011): **~15 anni di promesse, 0 prodotti di consegna commerciali**. Due riferimenti brillanti non spostano un base-rate così, specie quando uno (ODYS) è di un altro mercato/scala.

## 4. La novità genuina che i riferimenti aggiungono

Al netto del red-team, l'utente ha portato **due contributi reali** che arricchiscono il progetto:

- **(a) Il blown lift come 8ª opzione di integrazione VTOL** — non valutata in `14`. Merita una riga nel trade study: per un'ala chiusa è forse **più coerente** di lift+cruise (nessun rotore morto in crociera) e del tilt (nessun meccanismo). **Ma** a scala C3 la sua fattibilità è dubbia (potenza installata elevata, flap grandi, download in hover non caratterizzato, nessun COTS piccolo). Va tenuta come **opzione da dimostratore**, non da prodotto.
- **(b) Il tilt-wing-box (TiltOne) risolve l'obiezione "dove ruota"** e dà un'ala di crociera pulita. **Costo:** il regime di transizione più difficile (ala intera attraverso lo stallo — il punto debole già segnalato per la famiglia tilt-wing A4 in `14`), attuazione di tilt pesante, TRL 3-4, nessun COTS. È la **versione tecnicamente onesta** dell'idea dell'utente, e la sua **casa naturale è la linea R&D/dimostratore**, non il prodotto di servizio 0-12 mesi.

## 5. Impatto sulle decisioni (aggiorna `17` D2 e D3)

- **D2 (architettura VTOL del prodotto operativo): invariata.** Per il prodotto che eroga servizio a Pentema nell'orizzonte finanziabile, vince ancora **A2 lift+cruise COTS** (maturità, buy-not-build, servizio-non-OEM). Né TiltOne né ODYS offrono un COTS acquistabile a scala C3.
- **D3 (ruolo del box-wing): rafforzata, con lignaggio reale.** L'opzione **(A) box-wing come dimostratore R&D** esce **arricchita**: ora ha un lignaggio credibile e citabile (Prandtl → TiltOne/SUPAERO; ODYS blown-lift; Elytron), utile come **vetrina di sovranità tecnologica** verso l'HALE. Se Firmamento vuole un dimostratore box-wing, le **due strade più difendibili** sono **tilt-wing-box (TiltOne-like)** o **blown-lift (ODYS-like)**, non "4 tilt-rotor indipendenti". L'opzione **(B) box-wing come prodotto** resta **non giustificata** dall'evidenza: nessun caso reale a scala C3 è un prodotto operativo.
- **Conseguenza pratica:** il box-wing-tiltante **non entra nel P&L del prodotto**; entra (se l'utente lo vuole) come **Pool B / linea dimostratore**, con la prova di falsificazione a costo quasi nullo che segue.

## 6. Falsifying observations e prove a basso costo

1. **2 simulazioni (VLM → RANS transizionale)** a scala C3 su tilt-wing-box e su blown-lift: se mostrano L/D di crociera e download in hover **competitivi** con un lift+cruise pulito, l'opzione (B) riacquista una base tecnica. Se confermano ≈0% / download peggiore, (B) resta solo vetrina. **Costo ~nullo, in-house** ([`aerodynamics-structures-engineer`]).
2. **Lettura dei PDF primari** (Emerald/Springer TiltOne, arXiv quad biplano, ODYS tech) appena l'egress lo consente: estrarre **numeri reali** di massa/payload/potenza hover/efficienza a scala piccola → oggi mancano (caveat 403).
3. **RFQ a chi vende davvero** un box/tilt-wing UAV a scala C3 (se esiste): se nessun vendor lo offre COTS, è la conferma operativa che è R&D, non prodotto.
4. **Dato di transizione**: log/prova che il tilt-wing-box a 25 kg abbia un tasso di guasto in transizione comparabile a un lift+cruise → se peggiore, conferma il declassamento a dimostratore.
5. **Conferma della fonte "SUPAIR"**: se indica un progetto/prodotto specifico con dati di volo e maturità superiori a TiltOne, va letto e questa valutazione aggiornata.

---

## Riga di fondo

> I due riferimenti dell'utente **correggono un mio eccesso di sbrigatività** — il box-wing VTOL tiltante è reale, e nella sua versione sensata (**tilt-WING dell'intera ala**, come TiltOne/SUPAERO-Prandtl, non 4 nacelle indipendenti) l'obiezione "dove ruota" cade; ODYS aggiunge una via ancora diversa (**blown lift**, senza alcun tilt) che `14` non aveva considerato. **Ma nessuno dei due ribalta il verdetto**: sono **dimostratori** (TiltOne accademico; ODYS primi voli 2026, altra scala e mercato; Elytron mai commercializzato), a scala non trasferibile al C3, e senza un solo dato che falsifichi il vantaggio d'ala ≈0% a scala C3. Il netto: **il prodotto operativo resta il lift+cruise COTS (A2); il box-wing-tiltante si rafforza come linea R&D/dimostratore** — con un lignaggio ora citabile — **non come prodotto**. La prova che potrebbe promuoverlo a prodotto è sempre la stessa e costa quasi nulla: **due simulazioni**. Finché non le si fa, l'onere della prova per "box-wing come prodotto" resta non assolto.

---

## Fonti e confidence

| Fonte | Tipo | Confidence | Uso |
|---|---|---|---|
| ODYS Aviation (Aviation Week, FlightGlobal, New Atlas, Aerospace Global News) | Stampa di settore, WebSearch (fetch 403) | media | Config blown-lift, no-tilt, scala regionale 9-posti, status 2026 |
| TiltOne — Emerald AEAT, Springer Aerotecnica Missili & Spazio, NATO STO, ResearchGate | Accademico, WebSearch (fetch 403) | media | Box-wing tilt-wing 4 eliche su 2 ali, Prandtl BWS, stadio prototipo |
| Elytron/VTOL Aerospace Converticopter (New Atlas) | Stampa di settore, WebSearch | media | Box/closed wing + 2 tilt-rotor, ~2,4 m, UAV, mai commercializzato |
| IEEE Xplore (tilt-prop box-wing); arXiv 1801.02938 (quad biplano delivery) | Accademico, WebSearch (fetch 403) | bassa-media | Esistenza di un corpo di ricerca su box + eliche tiltanti |
| `22-boxwing-vantaggio-tecnico.md`, `R6-boxwing-aerodinamica.md` (repo) | Interne | media | Verdetto aero ≈0% a C3, CD0 dominato dal VTOL |
| `14-vtol-config-tradestudy-C3.md`, `17-...decisioni.md` (repo) | Interne | media | Vincitore A2 lift+cruise; decisioni D2/D3 |

**Limiti dichiarati:** WebFetch integrale bloccato (403) su tutte le fonti esterne → nessun numero primario (massa/payload/efficienza) di TiltOne/ODYS è stato letto direttamente; tutto è da sintesi WebSearch, da riverificare sui PDF. "SUPAIR" non confermato come denominazione esatta. Nessun dato di crociera a scala C3 disponibile per box-wing tiltante.
