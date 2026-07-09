# 16 — Espansione delle fasce alte T3 (MALE civile) e T4 (HALE stratosferico)

> **Volume:** Analisi bottom-up pre-Studio — approfondimento di `10-fasce-engineering.md` §5-6 e `13-fasce-regolatorio-missione.md`
> **Data:** 9 luglio 2026
> **Autore:** Aerospace Systems Engineer (NASA SE Handbook framework)
> **Mandato:** le fasce alte della famiglia modulare (T3 MALE, T4 HALE) sono trattate nei documenti esistenti in modo più sintetico delle fasce basse (T0-T2). Questo documento le espande con profondità di ingegneria di sistema — segmentazione interna, architetture candidate e trade tecnici, missioni abilitate e valore di servizio, nodo regolatorio, economia, posizionamento Firmamento e roadmap/gate — **senza ribaltare** i verdetti già consolidati (HALE standalone impossibile, 0 HALE solari commerciali in 20+ anni, MALE certificato civile senza precedente EASA). L'espansione aggiunge risoluzione tecnica, non ottimismo.

---

## 0. Caveat epistemico e ancoraggio ai verdetti esistenti

**Confidence aggregata: LOW-MEDIUM**, dichiarata riga per riga. Marcatura: **[FATTO]** = dato normativo/contrattuale/prestazionale verificato con fonte; **[STIMA]** = valutazione ingegneristica per analogia con banda di incertezza dichiarata.

**Capisaldi non negoziabili preservati in questo documento** (invarianti da `00`, `05`, `10`, `13`, R3, R7 e `CLAUDE.md`):
1. **Firmamento è operatore di servizi, non OEM.** Su T3/T4 non compete come costruttore con Tekever/Elbit/Airbus/BAE. Gioca da **nodo di consorzio, operatore di servizio o partner R&D di minoranza**.
2. **T4 (HALE) è vettore strategico Y6+, non procurement.** Nessun servizio HALE è nell'orizzonte finanziabile Y1-Y3 dello Studio.
3. **Showstopper HALE noti e invarianti:** (a) energy balance invernale a 20 km, lat. 44°N (dic-gen è la condizione dimensionante); (b) assenza totale di framework HAPS civile EASA/ENAC; (c) capital-intensity (centinaia di M€ per un servizio operativo, prototipo singolo $10-25M — R7 claim 13).
4. **Base-rate HALE solare = 0% operativo commerciale in 20+ anni** (R7: Loon ~$1B bruciato e chiuso, Aquila cancellato, HAPSMobile dissolta, 2 crash Zephyr/AALTO 2022+2025). Questo documento non contraddice il base-rate: lo usa come vincolo.

**Cosa NON fa questo documento:** non trasforma T3 in un procurement raccomandato per il pilota (resta sproporzionato per Pentema, cfr. `13` matrice), non riapre T4 come business core, non produce quotation vendor reali (non esistono nel repo per queste fasce).

---

## 1. Perché T3 e T4 non sono monolitiche

L'errore ricorrente nel linguaggio "famiglia a fasce" è trattare T3 come "il MALE" e T4 come "l'HALE", come se ciascuna fosse un singolo punto di progetto. Non lo sono. **All'interno di T3 la forbice di MTOM è 3× (150→450+ kg) e quella di costo unitario è 5× (€2→10M+); all'interno di T4 la distinzione dimostratore-vs-operativo è un salto di due ordini di grandezza di capitale ($10-25M → centinaia di M€) e di TRL (5 → 8-9 mai raggiunto).** Segmentare internamente non è pedanteria: cambia il tipo di ente finanziatore, il percorso regolatorio, il TRL di partenza e la posizione difendibile di Firmamento. Le sezioni 2 e 3 definiscono i sotto-punti di progetto.

---

## 2. T3 — MALE civile: segmentazione interna e ingegneria di sistema

### 2.1 Tre sotto-punti di progetto T3

Definisco tre punti di progetto distinti dentro la fascia T3, con parametri realistici ancorati ai benchmark di `10` §5.1 [confidence: media per i benchmark [FATTO], bassa per l'interpolazione a punti di progetto [STIMA]].

| | **T3a — MALE tattico "piccolo"** | **T3b — MALE tattico "pieno"** | **T3c — MALE-adjacent VTOL/STOL** |
|---|---|---|---|
| **Archetipo di mercato** | Tekever AR5, Schiebel S-100 | Elbit Hermes 450/900 | (nessun archetipo maturo — vedi §2.3) |
| **MTOM** | 150-220 kg | 450-1.200 kg | 200-400 kg [STIMA] |
| **Apertura** | 8-13 m [STIMA] | 15-17 m [FATTO Hermes] | 10-14 m [STIMA] |
| **Quota operativa** | 3.000-5.500 m | 6.000-9.000 m | 3.000-5.000 m [STIMA] |
| **Endurance** | 12-20 h [FATTO EMSA AR5 16-20 h] | 24-36 h [FATTO Hermes 900] | 8-14 h [STIMA — penalità hover] |
| **Payload utile** | 4-40 kg (EO/IR + AIS + SAR radar leggero) | 50-300 kg (multi-sensore, SIGINT, SAR pieno) | 20-80 kg [STIMA] |
| **Propulsione** | ICE heavy-fuel (Jet-A1/diesel) | ICE heavy-fuel / turboprop | ibrido serie (lift elettrico + cruise ICE) |
| **CapEx unitario** | €2-5M [FATTO bracket] | €5-10M+ [FATTO/STIMA] | €5-15M+ [STIMA — sviluppo, no COTS] |
| **TRL (vendor, non EASA-validated)** | 8-9 | 8-9 | 3-5 (nessun prodotto in serie civile) |
| **Take-off** | pista corta / catapulta / (S-100 rotary VTOL) | pista (runway-dipendente) | VTOL/STOL — no runway |

**Nota chiave sul valore dei sotto-punti:** T3a e T3b **esistono come prodotti maturi** che Firmamento potrebbe *usare come servizio* (buy/lease + operate), coerente col modello non-OEM. T3c **non esiste maturo** e sarebbe un programma di sviluppo — territorio della linea R&D, non del procurement.

### 2.2 Trade tecnico #1 — Ala fissa vs VTOL-MALE: il tema "no runway in Appennino"

Il vincolo geografico reale (valli appenniniche strette, assenza di piste; cfr. Pentema in `13`) solleva la domanda: **serve VTOL/STOL anche in fascia MALE?**

- **Ala fissa pura (T3a/T3b classici):** massima efficienza aerodinamica (L/D alto → endurance), ma richiede pista o infrastruttura di lancio/recupero (catapulta+skyhook stile RQ-21, oppure pista ≥300-500 m). **Incompatibile con l'orografia appenninica** senza un sito attrezzato dedicato. [confidence: high [FATTO] — vincolo fisico noto]
- **VTOL-MALE ibrido (T3c):** elimina la pista, ma la penalità è severa a questa scala. La potenza di hover cresce con W^1,5 / √(disk area); a 200-400 kg il gruppo lift (rotori + motori + energia) sottrae 15-30% di massa/potenza alla missione di crociera → **endurance dimezzata rispetto a un fisso di pari MTOM** e complessità certificativa maggiore. Nessun prodotto commerciale MALE-VTOL 200-400 kg maturo esiste (il segmento si ferma sotto ~60 kg, cfr. Latitude HQ-60 in `10` §4). [confidence: medium [STIMA] — scaling laws + assenza di prodotti]
- **Rotary-wing (Schiebel S-100, 200 kg):** è già un VTOL-MALE reale, ma con endurance limitata (~6 h [FATTO]) e costo/ora elevato. È l'unico VTOL-MALE COTS-maturo, ma paga la persistenza.

**Verdetto trade #1 [STIMA, confidence medium]:** in fascia MALE il VTOL **non si giustifica per la persistenza** (la penalità energetica cancella il vantaggio di endurance che è la ragione d'essere di un MALE). Se serve operare senza pista in Appennino, la risposta corretta **non è un MALE-VTOL** ma (a) un sito attrezzato con catapulta/skyhook per un fisso T3a, oppure (b) **scendere di fascia** a un VTOL T2 (30-150 kg) accettando meno endurance. Questo rafforza il verdetto di `10` §7.5: la modularità VTOL vive nelle fasce basse, non in T3.

### 2.3 Trade tecnico #2 — Propulsione: ICE heavy-fuel vs ibrido vs turboprop

| Opzione | Pro | Contro | Applicabilità |
|---|---|---|---|
| **ICE heavy-fuel (Jet-A1/diesel)** | Densità energetica carburante ~11.900 Wh/kg; logistica NATO single-fuel; endurance 16-36 h dimostrata (AR5, Hermes) [FATTO] | Rumore/firma termica; manutenzione motore; emissioni | **Standard T3a/T3b** — è la scelta reale del mercato |
| **Ibrido serie (gen-set + e-motor)** | Consente lift elettrico (VTOL) + cruise efficiente; ridondanza | Peso doppio powertrain; TRL basso a questa scala; efficienza di conversione | Solo T3c, R&D |
| **Turboprop** | Potenza/peso alto a quote alte; salita rapida | Consumo specifico alto → endurance minore; costo | Fascia superiore (Hermes 900-class), non necessario sotto 450 kg |

**Verdetto trade #2 [STIMA, confidence medium-high]:** per un MALE civile persistente **l'ICE heavy-fuel è la scelta dominante e collaudata**. L'ibrido ha senso solo se il requisito VTOL è vincolante — ma il trade #1 ha appena mostrato che in fascia MALE il VTOL non si giustifica. Coerenza interna: **T3 realistico = fisso, heavy-fuel, no VTOL.**

### 2.4 Trade tecnico #3 — Payload multi-sensore

Il valore di un MALE è la **persistenza multi-sensore su area vasta**. Configurazione tipo (payload bay 40-150 kg su T3a/T3b):
- **EO/IR gimbal** (giorno/notte, 30× zoom, MWIR) — maturo, COTS.
- **SAR leggero / GMTI** — sorveglianza all-weather, penetrazione nuvole/notte; abilita monitoraggio marittimo e movimento.
- **AIS receiver** — correlazione tracce navali (sorveglianza marittima EMSA-like).
- **Relay/SATCOM BLOS** — il MALE come nodo di comunicazione mobile.

La combinazione EO/IR + SAR + AIS è esattamente il payload del **servizio EMSA di sorveglianza marittima** (cfr. §2.6). È il caso d'uso a più alta maturità e più alto valore di servizio in fascia T3.

### 2.5 Missioni realmente abilitate da T3 e valore di servizio (modello non-OEM)

| Missione | Cosa abilita T3 (che T2 non fa) | Cliente-tipo | Cosa si vende |
|---|---|---|---|
| **ISR persistente area vasta** | 16-36 h su area di centinaia di km², multi-sensore | Difesa, PA sicurezza | Ore-di-copertura, non velivolo |
| **Sorveglianza marittima / confini** | AIS+SAR+EO su ZEE, endurance oceanica | Guardia Costiera, EMSA-like, Frontex-like | Servizio RPAS-as-a-Service |
| **EO area vasta / disaster response** | Mapping ripetuto multi-versante, loiter su evento | Protezione Civile, PA regionale | Dataset + persistenza on-event |
| **Relay/connettività mobile** | Nodo BLOS che segue un evento | Emergenza, difesa | Capacity temporanea |

**Valore di servizio coerente col modello inderogabile:** Firmamento **non venderebbe il MALE**, ma erogherebbe un **servizio di sorveglianza/EO persistente a PA e agenzie**, sul modello EMSA-Tekever (che è precisamente RPAS-as-a-Service con equipaggio del contractor incluso — R3 §2.2). Questo è l'unico modo in cui T3 è compatibile con `CLAUDE.md`. [confidence: high sul modello, medium sulla accessibilità a Firmamento]

### 2.6 Economia T3 — perché standalone non chiude, e con quali fondi

**Benchmark reale (il più solido dell'intera fascia) [FATTO, confidence media-alta]:** contratto EMSA per servizio MALE marittimo = **€30M tetto framework, 2 anni fermi + opzione fino a 4** (R3 §2.1, correzione del precedente "€30-35M"). Costo/anno implicito **€7,5-15M/anno** a seconda dell'esercizio delle opzioni, equipaggio+operazioni multi-sito inclusi. Lo stesso ~€30M/2-4 anni ricorre per Airbus Flexrotor e Schiebel su EMSA → è una **soglia di budget-quadro standard EMSA per lotto RPAS marittimo**, non un prezzo di mercato aperto (R3 §2.2).

**Perché non chiude dentro un budget finanziabile da Firmamento standalone:**
- Il **tetto di finanziabilità "comodo" del progetto è ~€1M** (`06-finanziabilita.md`), il CapEx Y1 realistico del Percorso 6A €2,5-3,5M (`05` §4). Un servizio MALE persistente costa **€7,5-15M/anno** — 1 ordine di grandezza sopra. [confidence: high [FATTO]]
- Lo **sviluppo custom** di un MALE certificato (T3c o un airframe proprietario) è territorio €5-15M+ solo di sviluppo (R3 §3, benchmark CORDIS/STUAS/Watchkeeper), **senza** che nessun UAS abbia mai ottenuto un Type Certificate EASA pieno (R3 §4 [FATTO]).

**Fonti di finanziamento possibili e a quali condizioni:**
- **EDF / Horizon Europe / EUSPA** — un servizio ISR/sorveglianza marittima dual-use è finanziabile via bandi difesa/sicurezza UE, **ma solo in consorzio** (Firmamento come operatore/integratore di servizio, non come OEM). Condizione: anchor customer pubblico (PA/agenzia) firmato.
- **Servizio contrattualizzato PA (modello EMSA):** sostenibile solo con un contratto pluriennale che copra OpEx — cioè **serve l'anchor prima dell'asset**, non dopo.

**Verdetto economico T3 [STIMA, confidence medium-high]:** T3 è **fuori portata come procurement autonomo Y1-Y3**, ma **potenzialmente accessibile come servizio-in-consorzio Y3+** se e solo se esiste un anchor pubblico che copre gli OpEx. La via è "operate a leased/consortium MALE for a PA customer", non "buy and hope".

### 2.7 Nodo regolatorio T3 — perché MTOM>150 kg è lo spartiacque

Approfondimento tecnico (la sostanza; il dettaglio procedurale è in `13` e `04`):

- **La soglia dei 150 kg** è lo spartiacque storico: sopra i 150 kg di MTOM l'operazione esce dalla Specific Category "leggera" e ricade, con alta probabilità, in **Certified Category** o **Specific SAIL IV-VI** con requisiti tecnici e assicurativi quasi assimilabili all'aviazione con equipaggio. [FATTO — art. 6 Reg. 947 + `13` fascia T3]
- **Il problema dirimente:** **nessun UAS ha mai ottenuto un Type Certificate EASA pieno** (luglio 2026; il caso più avanzato è il primo Design Verification Report per il Camcopter S-100, set. 2024 — non un TC) (R3 §4 [FATTO, confidence alta]). Quindi un MALE civile 150-450 kg in BVLOS continuativo su territorio SNAI **non ha precedente autorizzativo in Italia** — è un rischio regolatorio potenzialmente showstopper **indipendentemente dal costo**.
- **Via di mitigazione:** operare via **Specific SAIL IV-VI con Design Verification Report** (€250/h EASA, ~€45k/anno per progetto tipico — R3 §4 [FATTO]) invece del TC pieno, se il ConOps lo consente; oppure operare in contesto difesa/agenzia (regime speciale fuori Reg. 947 civile, cfr. `13` §2 riga sorveglianza law-enforcement). Il servizio EMSA opera in questo spazio "agenzia".

**Verdetto regolatorio T3 [confidence: high sul rischio, medium sulla via]:** lo spartiacque 150 kg rende T3 un **nodo non risolto** che richiede lavoro dedicato di `aviation-regulatory-counsel`/`regulatory-adversary` prima di qualsiasi commitment (invariato da `10` §5.3). L'espansione qui è: la via praticabile passa da **DVR + regime agenzia**, non dal TC pieno che non esiste per nessuno.

---

## 3. T4 — HALE stratosferico: segmentazione interna e ingegneria di sistema

### 3.1 Due sotto-punti di progetto T4 (più un terzo "operativo" fuori orizzonte)

| | **T4a — Dimostratore HALE subscale** | **T4b — HALE prototipo persistente** | **T4c — HALE operativo commerciale** |
|---|---|---|---|
| **Scopo** | De-risk tecnologico, TRL 3→5 | Primo volo persistente, TRL 5→7 | Servizio commerciale, TRL 8-9 |
| **Scala** | 1:3 subscale, apertura ~8-10 m | Full-scale, apertura 20-30 m | Flotta full-scale |
| **Durata volo target** | ore-giorni (voli diurni, buon meteo) | giorni→settimane (superare la notte) | mesi (persistenza vera) |
| **Payload** | strumentazione di test | 5-10 kg (EO leggero / relay) | payload di servizio |
| **Quota** | 15-20 km (test) | 20 km nominale | 20 km persistente |
| **CapEx** | **$10-25M** (prototipo singolo) [FATTO R7] | **centinaia di M€** (programma) [FATTO R7] | centinaia di M€ - $1B+ |
| **TRL realistico oggi** | 3-4 | 3-5 | **mai raggiunto da nessuno (0%)** |
| **Orizzonte Firmamento** | Y3-Y6 (co-finanziato consorzio) | Y6+ (vettore strategico) | Y8-Y10 (visione, non piano) |

**Il punto critico della segmentazione:** il salto **T4a → T4b non è incrementale, è un cambio di regime.** T4a (voli diurni/giorni in buona stagione) è tecnicamente alla portata di un consorzio ben finanziato — è ciò che Zephyr/PHASA-35 dimostrano da anni. T4b (**superare la notte invernale in modo ripetibile a 44°N**) è precisamente ciò che **nessuno ha mai fatto commercialmente in 20+ anni** (R7 base-rate 0%). La distanza tra i due è lo showstopper energetico (§3.3).

### 3.2 Trade tecnico #4 — Solare-puro vs ibrido solare+H2/fuel-cell

| Architettura energetica | Principio | Pro | Contro | Maturità |
|---|---|---|---|---|
| **Solare puro + batterie** (Zephyr, PHASA-35) | PV di giorno carica batterie per la notte | Nessun consumabile, "eterno" in teoria | **Fallisce il bilancio invernale a 44°N** (§3.3); batterie pesanti | TRL 5-6 (estate/basse lat.), mai persistente inverno UE |
| **Ibrido solare + fuel-cell H2 rigenerativa** | Elettrolisi di giorno, fuel-cell di notte | Densità energetica H2 superiore alle batterie per lo stoccaggio notturno lungo | Sistema elettrolisi+FC+serbatoi pesante e immaturo a bordo; TRL basso | TRL 3-4 |
| **Airship stratosferico** (Sceye) | Galleggiamento + PV | Grande superficie PV, station-keeping | Volume enorme, controllo, tecnologia diversa | Pre-commerciale (Sceye ~$580M, Giappone 2026 — R7) |

**Trade #4 [STIMA, confidence medium]:** per un HALE ad ala fissa a 44°N, **il solare-puro non chiude in inverno** (§3.3) — è la ragione tecnica per cui i programmi di successo (Zephyr) operano a basse latitudini/estate. L'ibrido H2/fuel-cell **potrebbe** chiudere il bilancio invernale sulla carta, ma a costo di massa e a TRL 3-4, mai volato persistente. Nessuna delle due architetture è oggi una soluzione dimostrata per il caso 44°N-inverno. Questo **non è un trade da chiudere ora**: è una domanda di ricerca aperta che definisce l'intera fase R&D T4. Rimando a `propulsion-energy-engineer` per il calcolo del bilancio.

### 3.3 Il caso critico — energy balance inverno a 20 km, lat. 44°N: perché è LO showstopper

Sostanza tecnica del perché dicembre/gennaio è la condizione dimensionante [confidence: high sulla struttura del problema [FATTO fisico], medium sui numeri puntuali [STIMA]]:

1. **Notte lunga, giorno corto.** Al solstizio d'inverno a 44°N il fotoperiodo utile è ~9 h; la batteria deve alimentare volo + payload + avionica per **~15 h di buio**. L'energia notturna richiesta è massima proprio quando quella diurna raccoglibile è minima.
2. **Angolo solare basso.** L'irraggiamento sul pannello (orizzontale sull'ala) scala con il seno dell'elevazione solare; a mezzogiorno del solstizio a 44°N l'elevazione è ~22° → l'energia incidente per m² è una frazione di quella estiva. La stessa ala raccoglie molta meno energia in inverno.
3. **Massa batteria.** Chiudere il bilancio notturno invernale richiede una densità energetica batteria che oggi **non è commercialmente matura**: le Li-S (Litio-Zolfo, ~400-500 Wh/kg target) sono il candidato ma **non a maturità di serie/qualifica aeronautica** (`10` §6 [FATTO]). Con Li-ion attuali (~250-300 Wh/kg utili) la massa batteria per superare la notte invernale rende il velivolo troppo pesante per volare con quel PV ridotto → **circolo che non chiude.**
4. **Vento stratosferico invernale.** Il getto invernale a quote di transizione e la maggiore intensità dei venti stratosferici invernali aumentano la potenza di station-keeping richiesta, peggiorando ulteriormente il lato "consumo" del bilancio proprio quando il lato "raccolta" è al minimo.

**Sintesi [confidence high]:** i quattro fattori si sommano **tutti nello stesso periodo** (dic-gen) e **tutti nella stessa direzione sfavorevole**. Questo è il motivo per cui il bilancio invernale a 44°N è la condizione dimensionante e il vero showstopper: non è un margine da limare, è un bilancio che **con le tecnologie di batteria commerciali oggi non si chiude**. È coerente con l'analisi Firmamento stessa (Cap. 6 §6.2.2.3 citata in `10` §6) e con il fatto che **0 HALE solari operano commercialmente a latitudini/stagioni UE**.

### 3.4 Trade tecnico #5 — Ala high-AR e aeroelasticità

L'ala HALE ha allungamento (AR) estremo (20-30+) per massimizzare L/D e ospitare superficie PV. Conseguenza strutturale: **estrema flessibilità → problematiche aeroelastiche** [confidence: high sul rischio, medium sui dettagli]:
- **Flutter e divergenza** a basso numero di Reynolds e bassa densità (a 20 km la densità dell'aria è ~7% di quella al livello del mare).
- **Grandi deformazioni non lineari** (l'ala flette del 20-30% della semiapertura — cfr. i crash Helios NASA 2003 e Zephyr/AALTO 2022+2025, in parte riconducibili a dinamica strutturale/batteria in condizioni fuori inviluppo, R7 claim 5).
- **Materiali:** il concept Firmamento (`Progetto concettuale struttura HALE.md`) esplora anche compositi a fibra naturale (lino); la fibra di lino ha smorzamento intrinseco favorevole ma modulo/resistenza inferiori al CFRP → trade da chiudere con `aerodynamics-structures-engineer`.

**Trade #5:** l'aeroelasticità di un'ala high-AR HALE a 20 km **mai validata su scala di serie** è, insieme all'energy balance, il secondo blocco tecnico duro. Non è nuovo (invariante da `10` §6), ma qui si esplicita che è un **problema di sistema accoppiato** (aero-struttura-controllo-energia), non un sottoproblema isolabile.

### 3.5 Missioni abilitate da T4 e valore di servizio (se e quando esistesse)

| Missione | Cosa abiliterebbe T4 | Cliente | Valore di servizio (non-OEM) |
|---|---|---|---|
| **Connettività NTN persistente** | Cella 5G/relay da 20 km su area vasta | MNO (neutral-host), PA | Capacity wholesale €/Mbps/area |
| **EO persistente / stare** | Ripresa continua H24 (che il satellite LEO non fa — revisita, non permanenza) | PA, Protezione Civile, difesa | Dataset persistente, alert on-event |
| **Sorveglianza marittima/confini** | Loiter oceanico multi-giorno | Agenzie sicurezza | Servizio persistente |

**Il valore distintivo teorico del HALE** è la **persistenza su un punto** (station-keeping), che né il satellite LEO (passa e va) né il MALE (endurance ore-giorni) offrono. **Ma** — vincolo da `00-SINTESI` e R7 — per la **sola banda larga a un borgo, Starlink batte l'aereo di 1-3 ordini di grandezza** (verdetto rafforzato: prezzo ingresso €29/mese, hardware gratis — R7 §3.1). Quindi il valore HALE non è la connettività di consumo, ma la **persistenza EO/sorveglianza dual-use e la sovranità del layer** (complementare a IRIS², linguaggio `CLAUDE.md`), un valore **strategico e istituzionale**, non un business case a corto raggio.

### 3.6 Economia T4 — perché è capital-intensity fuori scala, e le uniche vie

**Distinzione fondamentale ancorata a fonti reali (R7 claim 13 [FATTO, confidence media-alta]):**
- **Prototipo singolo HALE:** **$10-25M** — l'unico frammento potenzialmente co-finanziabile (EDF/ESA/ASI/Horizon/PNRR), **fuori portata di Firmamento standalone** ma alla portata di un consorzio.
- **Servizio operativo commerciale persistente:** **centinaia di M€** (Sceye ~$580M raccolti, Loon ~$1B bruciato, Stratospheric Platforms ~£200M target — R7 §4). **Fuori portata standalone in assoluto.**

**Base-rate spietato [FATTO]:** due dei più capitalizzati attori tech al mondo (Google/Loon, Facebook/Aquila) hanno **rinunciato non per mancanza di capitale ma per impossibilità di chiudere l'economia** ("we haven't found a way to get the costs low enough" — Loon, R7 §4.1). Se Google con ~$1B non ha chiuso, il caso base per chiunque altro è negativo.

**Le uniche vie realistiche per Firmamento su T4:**
1. **Partner di minoranza in consorzio** (AALTO/Airbus, Sceye, TAS-Leonardo, Space42, EuroHAPS) — R7 §5 raccomandazione: "partnership di minoranza con un prime", non OEM stratosferico.
2. **Nodo italiano di un programma sovrano EU** — la visione 10 anni è **finanziariamente possibile solo con un programma equivalente IRIS² (€10B+ Commission-funded)** come precondizione, non come bonus (`visione-10-anni.md` riga 176 [FATTO interno]).
3. **Dimostratore co-finanziato tenuto contabilmente separato** dal procurement di servizio Y1 (R7 §6.4).

### 3.7 Nodo regolatorio T4 — vuoto normativo totale

Sostanza (dettaglio in `13` fascia T4 e `04`) [confidence: high [FATTO]]:
- **Nessun framework HAPS civile EASA/ENAC esiste.** Categoria Certified, Type Certificate ottenibile solo via **Special Condition negoziata caso-per-caso** — showstopper RSK-REG-001 (`13`).
- **Attraversamento spazio controllato FL195+** in salita/discesa → coordinamento ENAV obbligatorio, procedure dedicate inesistenti.
- **Spettro HAPS non allocato** in modo utilizzabile: dipende da **WRC-27** (World Radiocommunication Conference 2027) per identificazioni di banda HAPS → incertezza pluriennale.
- **Tempi/costi solo certificazione:** 5-8+ anni, €5-15M+ (`13` fascia T4 [STIMA]).

**Verdetto regolatorio T4 [confidence high]:** il framework non esiste e **non abilita alcun servizio nell'orizzonte finanziabile.** Un asset riutilizzabile dal Percorso 6A/6B qui è **l'evidenza regolatoria accumulata** (pratica SORA, dialogo ENAV, relazioni ENAC) — coerente con la strategia duale (ogni evidenza 6A prepara 6B).

---

## 4. Posizionamento Firmamento su T3/T4 — coerenza coi verdetti

**Principio invariante:** Firmamento **non compete come costruttore** con Helsing/Quantum/Tekever/Airbus/Elbit/BAE. Il posizionamento difendibile:

| Fascia | Ruolo Firmamento | Cosa NON è | Precondizione |
|---|---|---|---|
| **T3 MALE** | **Operatore di servizio** ISR/sorveglianza/EO su piattaforma leased/consortium (modello EMSA-as-a-Service) | Non OEM di MALE, non compete con Tekever/Elbit sul prodotto | Anchor pubblico che copre OpEx (€7,5-15M/anno) |
| **T4 HALE** | **Nodo di consorzio / partner R&D di minoranza / nodo italiano di programma sovrano EU** | Non OEM stratosferico, non "il costruttore dell'HALE italiano" standalone | Programma co-finanziato EDF/ESA/ASI o equivalente IRIS² |

**La "casa naturale" della linea R&D** è precisamente il box-wing/HALE (precedente CIRA, concept `Progetto concettuale struttura HALE.md`): è dove Firmamento accumula IP e competenze di lungo periodo **senza pretendere di industrializzare da sola**. Il box-wing T1 (fasce basse) è il banco di prova IP che alimenta la credibilità nel consorzio T4 — è così che la strategia duale 6A→6B produce asset riusabili (ground segment, competenze, evidenze regolatorie).

---

## 5. Roadmap e gate di attivabilità

Quando ciascun sotto-punto diventa attivabile e a quali condizioni di de-risk [confidence: medium [STIMA], ancorata a `visione-10-anni.md`]:

| Sotto-punto | Finestra | Condizioni de-risk (gate di attivazione) |
|---|---|---|
| **T3a MALE tattico (servizio)** | Y3-Y4 | Anchor PA/agenzia firmato che copre OpEx; nodo regolatorio DVR/regime-agenzia chiarito; consorzio operativo costituito |
| **T3b MALE pieno** | Y4-Y6 | Come T3a + scala del contratto che giustifica la fascia superiore; mai standalone |
| **T3c MALE-VTOL** | **Non raccomandato** | Il trade #1 lo sconsiglia; attivabile solo se emerge requisito no-runway inderogabile non risolvibile con T2 |
| **T4a Dimostratore HALE** | Y3-Y6 | Co-finanziamento consorzio ($10-25M non da Firmamento); TRL 3→5 su subscale; partner prime (CIRA/Polito/TAS) |
| **T4b HALE prototipo persistente** | Y6+ | Energy balance invernale **risolto** (Li-S mature o ibrido H2); aeroelasticità validata; framework regolatorio in evoluzione; programma centinaia di M€ |
| **T4c HALE operativo** | Y8-Y10 | Programma sovrano EU equivalente IRIS² (€10B+); vettore strategico, non piano |

**Gate decisionali di riferimento** (da `visione-10-anni.md` e Briefing): **M+24** evaluation HALE R&D (Go subscale / Hold); **M+36** Go Phase B HALE / Hold / continuare solo VTOL-MALE; **M+72** Go costellazione. Nessuno di questi gate approva T3/T4 come procurement Y1-Y3.

---

## 6. Falsifying observations (cosa falsificherebbe l'attivabilità di T3/T4)

Almeno 7 osservazioni che, se occorressero, cambierebbero il verdetto — o, non occorrendo, confermano l'inattivabilità nell'orizzonte dato:

1. **[T3] Anchor MALE mancante.** Se **nessuna PA/agenzia italiana firma un contratto di servizio ISR/sorveglianza pluriennale** che copra €7,5-15M/anno di OpEx entro Y3-Y4, T3 resta inattivabile (non c'è business case standalone). *Osservazione al 2026: nessun anchor firmato → T3 non attivo.* [FATTO negativo]
2. **[T3] Precedente regolatorio Certified.** Se **nessun UAS >150 kg ottiene un percorso autorizzativo civile (TC o DVR+SAIL VI) in Italia/UE** entro Y3, il nodo regolatorio T3 resta showstopper. *Al 2026: 0 TC EASA mai rilasciati → confermato.* [FATTO — R3 §4]
3. **[T4] Energy balance invernale mai chiuso.** Se **nessun attore dimostra un HALE solare persistente >7 giorni continui in dicembre a lat. ≥44°N** con batteria commerciale, T4b resta non fattibile. *Al 2026: 0 dimostrazioni in 20+ anni → confermato showstopper.* [FATTO — R7 base-rate 0%]
4. **[T4] Li-S non matura.** Se le batterie Li-S **non raggiungono maturità di serie/qualifica aeronautica a ~400+ Wh/kg** entro Y6, il bilancio invernale non chiude con solare-puro. *Al 2026: Li-S non commerciale → confermato.* [FATTO]
5. **[T4] Capital-intensity confermata.** Se un attore dimostrasse un **HALE solare operativo commerciale con revenue >$1M a lat. ≥44°N con budget <€50M**, il verdetto "impossibile standalone" sarebbe indebolito. *Nessuno l'ha fatto in 20+ anni → verdetto regge* (R7 falsifying observation). [FATTO negativo]
6. **[T4] Programma sovrano EU assente.** Se **la Commissione UE non lancia un programma HAPS equivalente-IRIS² (€1-10B)** entro Y6-Y8, la via "nodo sovrano" della visione 10 anni non ha veicolo di finanziamento. *Al 2026: EDF call HAPS €50-200M ipotizzata ma non programma sovrano → precondizione non soddisfatta.* [STIMA]
7. **[T4] Spettro HAPS non allocato.** Se **WRC-27 non identifica bande HAPS utilizzabili in Regione 1**, la missione connettività T4 resta senza spettro. *Al 2026: dipende da WRC-27 futura → aperto.* [FATTO]
8. **[Trasversale] Sostituti che erodono il valore.** Se **Starlink D2C broadband arriva in Italia via un MNO** prima di un HALE operativo, la nicchia connettività NTN da quota si chiude (R7 claim 4). *Al 2026: nessun deal MNO IT → finestra aperta ma in chiusura.* [FATTO — R7 §3.2]

**Lettura:** al luglio 2026, **7 delle 8 falsifying observations puntano nella direzione della non-attivabilità** di T3/T4 nell'orizzonte Y1-Y3 (e T4b/T4c nell'intero orizzonte finanziabile). Questo **conferma e non ribalta** i verdetti esistenti: l'espansione tecnica di questo documento aumenta la risoluzione, non l'ottimismo.

---

## 7. Riga di fondo

**T3 (MALE civile)** si segmenta in tre punti: T3a tattico piccolo (150-220 kg, EMSA-class, l'unico realistico come *servizio*), T3b pieno (450+ kg, Hermes-class), T3c MALE-VTOL (non esistente, sconsigliato dal trade). I trade chiave dicono: **fisso e non VTOL** (la penalità hover cancella la persistenza), **ICE heavy-fuel** (dominante e collaudato), **payload multi-sensore EO/IR+SAR+AIS** (il valore vero). T3 **non chiude standalone** (€7,5-15M/anno di servizio vs ~€1M finanziabile), è accessibile solo **come servizio-in-consorzio con anchor pubblico Y3+**, e ha un **nodo regolatorio non risolto** (150 kg = spartiacque Certified, 0 TC EASA mai emessi) superabile solo via DVR/regime-agenzia.

**T4 (HALE)** si segmenta in dimostratore (T4a, $10-25M, co-finanziabile in consorzio Y3-Y6), prototipo persistente (T4b, centinaia di M€, Y6+) e operativo (T4c, visione Y8-Y10 subordinata a un programma sovrano EU). I due blocchi tecnici duri sono **l'energy balance invernale a 44°N** (quattro fattori che si sommano tutti sfavorevolmente in dic-gen → bilancio che con batterie commerciali non chiude) e **l'aeroelasticità dell'ala high-AR** (mai validata su scala di serie). Base-rate 0% in 20+ anni, Google/Facebook ritirati per economia non chiudibile.

**Posizionamento Firmamento:** su entrambe le fasce, **operatore di servizio / nodo di consorzio / partner R&D di minoranza — mai OEM.** T4 resta **vettore strategico Y6+, non procurement.** L'espansione tecnica di questo documento **conferma i verdetti esistenti con più dettaglio**, non li ribalta.

---

## 8. Fonti e confidence

| Elemento | Confidence | Fonte |
|---|---|---|
| Benchmark MALE (Tekever/Elbit/Schiebel), EMSA €30M/2-4 anni | media-alta [FATTO] | `10` §5.1; R3 §2 (correzione €7,5-15M/anno) |
| T3 segmentazione a punti di progetto | bassa-media [STIMA] | interpolazione ingegneristica su benchmark |
| Trade VTOL-MALE / propulsione (scaling laws) | media [STIMA] | scaling laws + assenza prodotti maturi |
| Nodo regolatorio T3 (150 kg, 0 TC EASA) | alta [FATTO] | R3 §4; `13` fascia T3; `04` |
| Capital-intensity HALE ($10-25M prototipo / centinaia M€ programma) | media-alta [FATTO] | R7 claim 13, §4 |
| Base-rate HALE 0% operativo commerciale 20+ anni | alta [FATTO] | R7 §4.1 (Loon/Aquila/HAPSMobile/Zephyr) |
| Energy balance invernale 44°N showstopper | high struttura [FATTO fisico], medium numeri [STIMA] | `10` §6; Cap.6 §6.2.2.3 Firmamento; `propulsion-energy-engineer` da invocare |
| Aeroelasticità high-AR mai validata serie | alta rischio [FATTO], medium dettagli [STIMA] | `10` §6; concept doc; `aerodynamics-structures-engineer` da invocare |
| Framework HAPS assente, WRC-27, ENAV FL195+ | alta [FATTO] | `13` fascia T4; `04` |
| T4 = vettore Y6+, via consorzio/sovrana | alta interno [FATTO] | `CLAUDE.md`; `visione-10-anni.md` riga 176 |
| Starlink batte l'aereo (connettività), D2C IT non ancora | alta [FATTO] | R7 §3, claim 3-4 |

**Limiti dichiarati:**
- Nessuna quotation vendor reale per T3/T4 esiste nel repo — tutti i CapEx sono benchmark pubblici o stime per analogia (R3: RFQ diretta a vendor è l'unica via per numeri reali).
- I numeri puntuali dell'energy balance invernale (fotoperiodo, elevazione, massa batteria) sono strutturalmente corretti ma **da validare quantitativamente** con `propulsion-energy-engineer` (calcolo dic-21 a 44°N).
- La segmentazione a punti di progetto T3a/b/c e T4a/b/c è un **framework di analisi**, non un progetto di dettaglio: va sviluppata con `aerodynamics-structures-engineer` e `avionics-gnc-engineer` prima di essere specificabile.
- Vincolo di sessione R3/R7: WebFetch/curl bloccati da policy egress; le fonti esterne derivano da snippet WebSearch con URL primario dichiarato.
