# TS-VTOLCFG-T1 — Trade Study: Configurazione di decollo/atterraggio verticale per la piattaforma T1/BOXY (Categoria C3, ≤25 kg, ~3 m)

> **Volume:** Analisi bottom-up pre-Studio — approfondimento tecnico di seguito a `10-fasce-engineering.md` §3 (T1 "BOXY") e `22-boxwing-vantaggio-tecnico.md`
> **Data:** 9 luglio 2026
> **Autore:** VTOL/MALE UAS Specialist
> **TS-ID:** TS-VTOLCFG-T1
> **Gate associato:** M+6 Architettura (Percorso 6A/BOXY) — allegato DOCFAP, formato NASA SE Handbook §6.8
> **Metodo:** Weighted Decision Matrix + soglia di ammissibilità stile Pugh (screening must-have) sui criteri hard-constraint

---

## 0. Caveat epistemico

**Confidence aggregata del documento: LOW-MEDIUM**, dichiarata riga per riga secondo lo standard già in uso nel repository (`10-fasce-engineering.md`, `22-boxwing-vantaggio-tecnico.md`). Metodologia: fisica di base (teoria del disco attuatore, momentum theory), letteratura tecnica generale su famiglie VTOL (nessuna fonte proprietaria), benchmark vendor pubblici **non verificati da RFQ diretta**, cross-check con i dati già raccolti nel repository. **Nessun numero di questo documento è una prova di volo, un dato CFD o una quotazione vendor reale per Firmamento.** Tutti i calcoli sono di **fedeltà L0** (back-of-envelope), coerenti con lo stesso livello dichiarato in `22-boxwing-vantaggio-tecnico.md` §0.

**Distinzione dichiarata:** questo trade study è **ortogonale** al trade study sull'ala (`22-boxwing-vantaggio-tecnico.md`, verdetto: il box-wing/three-lifting-surface non dà vantaggio aerodinamico netto a scala C3, confidence media). Qui si tratta **come si aggiunge la capacità di decollo/atterraggio verticale** a una qualunque ala fissa C3, non quale ala scegliere. Il collegamento tra i due temi è trattato esplicitamente al §8.

**[FATTO]** = dato di fisica/ingegneria consolidata o riferimento a documento reale citabile. **[STIMA]** = valutazione dell'autore per analogia o calcolo di primo ordine, confidence dichiarata caso per caso.

---

## 1. Statement of the problem

- **Decisione da prendere:** quale architettura propulsiva/aerodinamica di decollo e atterraggio verticale (o l'assenza di essa) adottare per la piattaforma T1/BOXY, categoria Open C3 (MTOM ≤ 25 kg, dimensione caratteristica ≤ 3 m), a supporto delle missioni Firmamento a Pentema (EO/monitoraggio, consegna medicale, relay di comunicazione).
- **Stakeholder primari:** Firmamento Technologies (operatore di servizi, non OEM — `CLAUDE.md`), cooperative pilota Legacoop, Protezione Civile/Vigili del Fuoco (utenti finali missione consegna/EO), ENAC (autorità regolatoria SORA/C3), abitanti di Pentema/Torriglia (esposizione a rumore/rischio terzi).
- **Vincoli iniziali (must-have/must-not-have):**
  - MTOM ≤ 25 kg, dimensione ≤ 3 m — **tetto duro** di categoria C3 (Reg. UE 2019/945/947); superarlo esce dalla fascia T1 e non è nello scope di questo documento (il regolatorio di dettaglio è in `13-fasce-regolatorio-missione.md`).
  - Propulsione elettrica (coerente con `10-fasce-engineering.md` §3.2, nessuna ipotesi ibrida a questa taglia).
  - Missione primaria di riferimento: **consegna medicale punto-punto in valle appenninica stretta** (il caso più esigente sul piano di spazio di decollo/atterraggio, per `13-fasce-regolatorio-missione.md` §3); missioni secondarie EO/relay meno esigenti su questo asse.
  - Il concept interno attuale (`Progetto concettuale struttura HALE.md`) è **ala fissa senza VTOL**, con nota che la variante three-lifting-surface C3 è "potenziale per una futura integrazione ibrida VTOL" — cioè **nessuna architettura VTOL è oggi progettata**; questo trade study parte da zero.
- **Riferimento RTM:** requisiti di missione T1 in `10-fasce-engineering.md` §3.2 (payload 3-5 kg, endurance 90 min-3h, cruise 90-120 km/h); requisiti regolatori di missione in `13-fasce-regolatorio-missione.md` §3 (consegna medicale, SAIL II-IV, contenimento carico).

---

## 2. Contesto operativo Pentema (perché il problema esiste)

Pentema (Torriglia, GE) è una valle appenninica stretta a 1100-1300 m s.l.m., con:
- **Spazi di decollo/atterraggio ridotti** — nessuna pista, nessuna area piana ampia nota vicino ai punti di consegna (borgo di montagna, terrazzamenti, terreno alpestre). Questo è il **motivo esplicito per cui si considera il VTOL** invece di un'ala fissa convenzionale con pista.
- **Vento canalizzato/wind shear** tipico di valle stretta — sollecita in modo asimmetrico configurazioni con fasi di transizione o hover prolungato.
- **Inverno rigido** (fino a -10°C, neve, nuvolosità) — penalizza le batterie LiPo/Li-ion (capacità ridotta a freddo, tipicamente -10/-20% a 0°C `[STIMA generica, letteratura batterie, non specifica Pentema]`) e riduce ulteriormente il margine energetico già eroso dall'hover.
- **Quota 1100-1300 m** — densità dell'aria ridotta (~10-15% in meno rispetto al livello del mare) peggiora sia l'efficienza del rotore in hover sia la portanza alare in crociera a parità di velocità.
- **Missione di consegna = atterraggio-e-rilascio o hover-and-drop** su un punto specifico vicino a persone (destinatario), non semplice sorvolo: per `13-fasce-regolatorio-missione.md` §3.3 il SAIL dipende criticamente dal fatto che l'approccio finale sorvoli o meno il costruito.

Questi quattro fattori (spazio, vento, freddo, quota) sono il filtro attraverso cui ogni architettura VTOL viene giudicata nel presente trade study, oltre ai criteri "di catalogo" (efficienza, payload, TRL).

---

## 3. Alternative analizzate

| ID | Architettura | Sintesi |
|---|---|---|
| **A1** | Multirotore puro (quad/esacottero) | Nessuna ala, solo hover; volo intero a portanza propulsiva |
| **A2** | Quadplane / lift+cruise ("VTOL a 5 motori") | 4 rotori di sostentamento dedicati + 1 elica di crociera dedicata, su ala fissa convenzionale |
| **A3** | Tilt-rotor | Rotori che ruotano da verticale a orizzontale, stessi motori per hover e crociera |
| **A4** | Tilt-wing | L'intera ala (con i motori solidali) ruota |
| **A5** | Tail-sitter | Il velivolo decolla/atterra appoggiato sulla coda, poi si inclina di 90° |
| **A6** | Tilt-tri / ibridi asimmetrici | 3 rotori con tilt parziale o layout asimmetrico (varianti di nicchia) |
| **A7 (baseline)** | Ala fissa convenzionale, NON-VTOL, catapulta + recupero (rete/paracadute/belly/skyhook) | Nessuna capacità VTOL; è il concept attuale del documento HALE interno |

**A0 (status quo)** coincide con A7: il concept interno oggi non ha VTOL. A7 è quindi sia baseline di trade-off sia "status quo" nel senso NASA SE.

---

## 4. Analisi tecnica per configurazione

### 4.1 Metodo di calcolo comune (hover)

Per confrontare l'efficienza in hover si usa la teoria del disco attuatore (momentum theory), fedeltà L0:

`P_ideale = T^(3/2) / √(2·ρ·A)`

dove T = peso da sostenere (N), ρ = densità aria, A = area totale dei dischi rotorici. Potenza reale ≈ P_ideale / FM, con Figure of Merit FM ≈ 0.65-0.75 per rotori di piccola scala reali `[STIMA, letteratura generale rotorcraft]`.

**Caso di riferimento** (illustrativo, nessun disegno BOXY reale esiste — `[STIMA L0]`): MTOM 25 kg → W = T = 245 N; ρ = 1,11 kg/m³ (≈1500 m ISA, stessa convenzione di `22-boxwing-vantaggio-tecnico.md` §1.3, proxy ragionevole per la quota Pentema 1100-1300 m). Con 4 rotori Ø 0,5 m (A_tot ≈ 0,785 m²): v_i ≈ 11,9 m/s, P_ideale ≈ 2,9 kW, P_reale (FM 0,7) ≈ **4,15 kW ≈ 166 W/kg**. Ordine di grandezza coerente con i multirotori commerciali da 25 kg-class (tipicamente 150-200 W/kg in hover, confidence media per analogia). Con un pacco batteria ipotetico ~10-12 kg a 200 Wh/kg (≈2.000-2.400 Wh) l'**hover continuo puro** durerebbe **~30-35 minuti** — coerente con l'endurance nota dei multirotori da carico in questa taglia. Questo numero **NON è quello di BOXY** (che non esiste), è un controllo di plausibilità dell'ordine di grandezza.

Questo calcolo di riferimento serve da **metro comune**: ogni configurazione seguente eredita all'incirca la stessa fisica di hover per l'area totale di disco disponibile; le differenze reali stanno in (a) **quanto a lungo** serve hover potenza piena (secondi/minuti vs intero volo), (b) **quanta massa morta** il sistema VTOL aggiunge in crociera, (c) **quanto drag parassita** aggiunge in crociera.

### 4.2 A1 — Multirotore puro

- **Hover:** è il regime nativo, disk loading tipicamente il più basso possibile a parità di ingombro (rotori grandi, nessun compromesso con la crociera) → miglior efficienza di hover in assoluto tra le 7 alternative. `[STIMA media]`
- **Crociera:** **non esiste crociera aerodinamica** — tutto il volo è sostentamento propulsivo. Velocità orizzontale ottenuta per inclinazione del disco rotore (drag indotto aggiuntivo), non per portanza alare. Consumo energetico per km percorso molto superiore a qualsiasi configurazione alata. **Incompatibile con i target di `10-fasce-engineering.md` §3.2** (cruise 90-120 km/h, range 40-80 km): un multirotore da 25 kg realisticamente copre **15-25 km e 20-40 min** di autonomia totale `[STIMA, per analogia DJI M350-class scalato]`.
- **Frazione payload:** penalizzata indirettamente — gran parte della massa utile va in batteria per compensare l'inefficienza di hover-crociera; non c'è "penalità VTOL" separabile perché l'intero velivolo È il sistema VTOL.
- **Complessità/guasti/ridondanza:** il più semplice e maturo. Motore-out gestibile con configurazioni hex/octo (ridondanza N+1 nota, supportata nativamente da PX4/ArduPilot). Nessuna transizione, quindi **zero rischio di transizione per definizione**.
- **Idoneità Pentema:** ottima per lo spazio di decollo (vero point-hover, footprint minimo), ma **sensibilità al vento canalizzato di valle è alta** (superficie dei rotori esposta, nessuna ala a fare da "keel" aerodinamico) e il raggio d'azione limitato rende dubbia la copertura delle missioni a più versanti.
- **TRL/COTS:** **9**, maturità massima. Esempi reali: DJI Matrice 350 RTK (9,2 kg, fuori scala payload/range T1 ma stesso principio), heavy-lift multirotori tipo Freefly Alta X-class `[STIMA, categoria generale, non verificato in repo]`. Nessun prodotto COTS in questa famiglia copre però i target di range T1.
- **Costo/tempo:** il più economico e rapido da adattare (architettura chiusa, ma pezzi di ricambio/expertise ampiamente disponibili).
- **Rumore:** il peggiore delle 7 alternative — rumore multi-rotore ad alto regime per l'**intera durata del volo**, non solo in fase di decollo/atterraggio, particolarmente sfavorevole per una consegna che sorvola un borgo abitato.

### 4.3 A2 — Quadplane / lift+cruise ("VTOL a 5 motori")

- **Hover:** stessa fisica del disco attuatore di A1 (4 rotori dedicati dimensionati per il solo hover, nessun compromesso di crociera) → efficienza di hover paragonabile ad A1. **Ma** la finestra temporale in cui serve è breve: decollo, atterraggio, eventuale hover-and-drop (tipicamente 1-3 minuti su un volo di 20-90 minuti), quindi il costo energetico di hover pesa poco sul bilancio di missione totale.
- **Crociera:** penalità reale = **massa morta** dei 4 motori/ESC/eliche/braccia di sostentamento fermi in volo (stimata **15-22% del MTOM** `[STIMA media, per analogia con architetture COTS pubblicate]`) più **drag parassita aggiuntivo** delle nacelle/booms esposti. Il documento `22-boxwing-vantaggio-tecnico.md` §1.3 ha già stimato per un VTOL "sporco" C3 un **CD0 = 0,040, di cui 0,029 (≈72%) attribuibile a fusoliera/booms/nacelle rotori esposti** e solo 0,011 all'ala — un dato diretto e riutilizzabile qui: **il grosso della resistenza di un lift+cruise a questa scala non è l'ala, è l'hardware VTOL**. Questo è il compromesso centrale della famiglia: efficienza di crociera "buona ma non ottima" per un fixed-wing.
- **Frazione payload:** penalità VTOL stimata **15-22% MTOM** (motori+ESC+eliche+strutture di sostegno dedicate) — la più alta delle famiglie "con motori dedicati separati", ma bilanciata da maturità/affidabilità.
- **Complessità/guasti/ridondanza:** 5 motori totali (4 lift + 1 crociera), nessun elemento meccanico mobile (niente attuatori di tilt) → più parti di un multirotore puro ma **meno rischio meccanico** di ogni famiglia con tilt. **Punto di sicurezza rilevante e sotto-apprezzato**: se il motore di crociera si guasta in volo, i 4 rotori di sostentamento **restano disponibili** per un atterraggio verticale controllato in un punto qualsiasi — un vantaggio specifico per il terreno di Pentema, dove un normale "dead-stick glide" di un'ala fissa pura ha poche zone di atterraggio forzato sicure (pendii, bosco, abitato). Questo non è replicato dalla baseline A7 (motore singolo, nessun paracadute di riserva propulsivo).
- **GNC/transizione:** è la transizione **più matura e più volata** al mondo in ambito VTOL commerciale civile — l'autorità di controllo passa dai rotori (controllo diretto di quota/attitudine) alle superfici aerodinamiche (controllo per stallo/velocità) in una finestra di velocità nota e ben caratterizzata dai vendor. Il rischio residuo principale è un guasto **asimmetrico** di uno dei 4 rotori di sostentamento durante la fase di hover-transizione a bassa quota, dove il margine di tempo/altitudine per compensare è minimo.
- **Idoneità Pentema:** buona — capacità VTOL vera per decollo/atterraggio in spazio ristretto, ma l'ala esposta durante le fasi di hover a bassa quota è sensibile a raffiche laterali di valle (più della A1 pura, meno delle famiglie con superfici mobili A3/A4).
- **TRL/COTS:** **massima disponibilità COTS della famiglia**, è la configurazione dominante sul mercato reale: **JOUAV CW-15/CW-30E**, **Quantum Trinity F90+** (5,5 kg MTOW, 90 min, 1 kg payload `[vendor, non verificato indipendentemente]`) — entrambi già catalogati in `10-fasce-engineering.md` §3.2 come bracket di riferimento diretto per T1.
- **Costo/tempo:** moderato, mercato competitivo con più vendor (coerente col verdetto "Buy COTS vince" di `05-piattaforme-costi.md` §11).
- **Rumore:** alto nelle fasi VTOL (come A1), ma **basso in crociera** (motore singolo tipo aeromodello, elica efficiente) — netto migliore di A1 su una missione punto-punto dove la crociera è la maggioranza del tempo di volo.

### 4.4 A3 — Tilt-rotor

- **Hover:** gli stessi motori che servono la crociera devono anche servire l'hover in modo efficiente — compromesso di dimensionamento dell'elica (un'elica ottimizzata per hover è larga/lenta, una per crociera è stretta/veloce). Risultato tipico: disk loading più alto e potenza di hover **20-40% superiore** a rotori dedicati di pari spinta `[STIMA bassa-media, giudizio ingegneristico generale, nessun dato di test diretto]`.
- **Crociera:** **nessuna massa morta di motori dedicati** (a differenza di A2) → miglior frazione payload di A2, ma l'elica stessa è un compromesso (non è l'elica di crociera ottimale che avrebbe un fixed-wing puro), quindi l'efficienza di crociera è **buona ma non massima**.
- **Frazione payload:** stimata **10-16% MTOM** per il meccanismo di tilt + nacelle rinforzate + attuatori dedicati `[STIMA media]` — migliore di A2 (niente motore di crociera dedicato "extra"), peggiore della tail-sitter (nessun meccanismo di tilt).
- **Complessità/guasti/ridondanza:** gli **attuatori di tilt sono un nuovo modo di guasto** non presente in A1/A2 — inceppamento, disallineamento, guasto asimmetrico del meccanismo (un braccio si blocca a metà rotazione mentre gli altri completano la transizione) sono scenari storicamente critici nella famiglia tilt-rotor a ogni scala (il caso limite, su scala grande, è il programma V-22, dove gli incidenti da transizione/vortex-ring-state in configurazione parziale sono stati un tema ricorrente della storia del programma — riferimento di dominio pubblico, non un dato quantitativo applicabile 1:1 a un UAS C3, ma indicativo della natura del rischio `[FATTO qualitativo, noto pubblicamente; NON quantificabile per un piccolo UAS senza dati di volo dedicati]`).
- **GNC/transizione:** è il **punto debole strutturale della famiglia** — durante la rotazione delle nacelle l'autorità di controllo deve gestire contemporaneamente (a) il momento generato dal cambio di orientamento della spinta, (b) l'evoluzione della portanza alare (che cresce mentre la velocità aumenta), (c) un eventuale guasto motore che in questa finestra produce un'asimmetria doppia (spinta + drag). È il regime di controllo più complesso delle famiglie "con moto meccanico" insieme al tilt-wing.
- **Idoneità Pentema:** capacità VTOL reale come A2 ma **più sensibile a raffiche durante la finestra di tilt** (nacelle a metà rotazione = superficie e spinta esposte in modo non ottimale al vento laterale di valle), aspetto rilevante nel contesto di wind shear canalizzato.
- **TRL/COTS:** reale ma **vendor pool più ristretto** di A2. Esempi citati dal mandato: **Wingcopter 198/178** (25 kg MTOW, payload 4,7-6 kg, sgancio triplo — già catalogato in `10-fasce-engineering.md` §7.3 come benchmark diretto di consegna C3, con **track record operativo reale di consegna medicale/pacchi**, incluso il percorso EASA LUC per la scala multi-sito citato in `13-fasce-regolatorio-missione.md` §3.6); **Quantum Vector**, famiglie AeroVironment `[vendor, citazioni da mandato, non verificate indipendentemente in questa ricerca — confidence media]`.
- **Costo/tempo:** superiore ad A2 per via del meccanismo di tilt (ingegneria aggiuntiva, attuatori, qualifica del meccanismo).
- **Rumore:** meno motori totali di A2 (4 vs 5) e nessun motore "in più" dedicato solo alla crociera — moderatamente favorevole.

### 4.5 A4 — Tilt-wing

- **Hover:** stessa logica di A3 (motori/eliche condivisi tra hover e crociera), ma qui è **l'intera ala** (con motori solidali) a ruotare, non solo le nacelle.
- **Crociera:** in teoria la migliore efficienza propulsiva della famiglia "senza massa morta" (nessun motore dedicato extra, come A3), ma il giunto di rotazione dell'ala introduce **discontinuità/perdite aerodinamiche parassite** alla radice alare.
- **Frazione payload:** penalizzata dal **giunto di rotazione dell'intera ala** (attuatore che deve vincere il momento aerodinamico su tutta la superficie alare, non solo su una nacella) + longherone rinforzato per i carichi di torsione al giunto → stimata **14-20% MTOM**, comparabile o peggiore di A2 nonostante l'assenza di motore dedicato, perché l'attuatore/giunto strutturale è pesante. `[STIMA media]`
- **Complessità/guasti/ridondanza:** la **più complessa meccanicamente** delle 7 alternative — l'attuatore deve muovere una massa (ala + motori + payload sull'ala, se presente) molto maggiore di quella di una singola nacella tilt-rotor, con requisiti di coppia/rigidezza strutturale severi.
- **GNC/transizione:** **il regime di controllo più demandante** di tutte le alternative. Durante la rotazione dell'ala, il profilo alare attraversa angoli d'attacco molto elevati rispetto al flusso libero (quasi-stallo o stallo pieno per una parte della rotazione), con comportamento aerodinamico fortemente non lineare e scarsamente predicibile senza galleria del vento/CFD dedicati. Storicamente, velivoli pilotati tilt-wing (Canadair CL-84, LTV XC-142 — dominio pubblico, anni '60) sono stati abbandonati proprio per la difficoltà di gestione della transizione anche con pilota a bordo; il programma eVTOL Airbus Vahana (tilt-wing, scala passeggeri) è stato chiuso nel 2019 dopo dimostratore volato, non arrivando a certificazione `[FATTO, dominio pubblico]` — indicazione che la famiglia resta impegnativa anche con investimenti importanti.
- **Idoneità Pentema:** **peggiore delle famiglie con capacità VTOL vera** — l'ala che ruota verticalmente vicino al suolo richiede più spazio libero laterale/verticale di un tilt-rotor (spazzata dell'ala + rotori), problematico in un terreno alpestre con ostacoli (alberi, muretti, edifici) vicini al punto di atterraggio.
- **TRL/COTS:** **nessun prodotto COTS maturo identificato in questa ricerca alla scala C3** per uso civile/delivery. I riferimenti esistenti sono demo di ricerca (es. NASA Greased Lightning GL-10, dimostratore tilt-prop/tilt-wing ibrido, TRL 4-5) o programmi a scala maggiore poi sospesi (Vahana). **TRL stimata 3-4** per un prodotto C3 dedicato — va sviluppato da zero, nessun bracket di costo COTS applicabile.
- **Costo/tempo:** il più alto e il più lungo della famiglia VTOL (sviluppo bespoke, nessuna base COTS).
- **Rumore:** comparabile ad A3 (stessa logica propulsiva), ma non è il discriminante qui — lo è la maturità.

### 4.6 A5 — Tail-sitter

- **Hover:** l'intero velivolo (fusoliera + ala + coda) è nella scia del rotore durante l'hover verticale, non solo un disco isolato — genera **perdite di download** paragonabili o superiori a un lift+cruise convenzionale (superficie bagnata investita dalla scia più estesa). Tuttavia il disk loading del singolo rotore (spesso di diametro generoso, unico) può essere più favorevole di un piccolo tilt-rotor multi-motore. Netto: **efficienza di hover intermedia**, dipendente fortemente dal design specifico. `[STIMA bassa]`
- **Crociera:** **zero massa morta** — lo stesso motore/elica serve hover e crociera, nessun motore extra, nessun meccanismo di tilt. È la configurazione con **la miglior frazione payload teorica** delle 7 alternative (stimata penalità incrementale solo **3-6% MTOM**, per superfici di controllo dedicate alla gestione della transizione e avionica di stima d'assetto più sofisticata). `[STIMA media]`
- **Complessità/guasti/ridondanza:** meccanicamente semplice (nessun tilt, spesso un solo motore/elica) — **ma questo è anche il suo punto debole critico**: **motore singolo = nessuna ridondanza propulsiva in nessuna fase di volo**, a differenza di A1/A2/A3/A6 dove più motori offrono un margine in caso di guasto singolo. Un guasto motore in hover o in transizione è, per un tail-sitter monomotore, un evento senza mitigazione propulsiva — il paracadute/BRS diventa **l'unica rete di sicurezza**, non un backup tra altri.
- **GNC/transizione:** è il **problema di controllo più demandante insieme al tilt-wing**, ma di natura diversa: transizione di **90° di assetto** (da verticale a orizzontale) attraverso un regime ad alto angolo d'attacco dove le superfici di controllo convenzionali (equilibrate per il volo orizzontale) sono in un regime aerodinamico atipico, e l'autopilota deve gestire stima di stato (attitude/velocity estimation) attraverso l'intero inviluppo. Storicamente i tail-sitter pilotati anni '50 (Convair XFY Pogo, Lockheed XFV) furono abbandonati per il carico di lavoro/visibilità del pilota in hover verticale `[FATTO, dominio pubblico]` — per un UAS il problema si sposta dal fattore umano al software di stima e controllo, mitigato dagli autopiloti moderni (il successo commerciale di WingtraOne lo dimostra), ma resta il regime di volo più esigente per il tuning del controllore.
- **Idoneità Pentema:** footprint di ingombro a terra compatto come A1, ma la postura verticale su un terreno non preparato/in pendenza è delicata (rischio di ribaltamento al contatto, specie con vento laterale in fase di touchdown) — problematico su un terreno alpestre irregolare senza piazzola dedicata. Inoltre un tail-sitter tipicamente **non è pensato per un meccanismo di sgancio cargo mentre è appoggiato in verticale** (il vano payload è orientato per il volo orizzontale) — la missione di consegna richiede quindi un rilascio in **hover** (non a terra), aggiungendo un ulteriore hover-and-drop oltre a decollo/atterraggio.
- **TRL/COTS:** reale — **WingtraOne GEN II** è un prodotto maturo e ampiamente venduto in ambito mapping/EO (citato anche in `10-fasce-engineering.md` §2 come riferimento T0). **Ma è ottimizzato per un payload fisso da rilevamento, non per un meccanismo di sgancio cargo**: l'adattamento a una missione di consegna è **non dimostrato** in questa ricerca. TRL 9 per la piattaforma-base EO, TRL stimata 3-4 per una variante cargo-release.
- **Costo/tempo:** moderato per un adattamento EO (COTS esistente), ma alto se serve sviluppare da zero il meccanismo di sgancio in hover verticale (nessun precedente COTS diretto).
- **Rumore:** motore singolo, moderato.

### 4.7 A6 — Tilt-tri / ibridi asimmetrici

- **Hover/crociera:** logica intermedia tra A3 (tilt parziale) e configurazioni sperimentali con layout asimmetrico (es. 2 rotori fissi di crociera + 1 rotore centrale di sostentamento con tilt, o varianti a 3 rotori con tilt differenziato). La letteratura su queste famiglie è **scarsa e per lo più accademica**; le prestazioni dipendono fortemente dal layout specifico, poco generalizzabile. `[STIMA bassa, categoria eterogenea]`
- **Frazione payload:** intermedia, stimata **12-18% MTOM**, comparabile alla fascia A3 ma con maggiore incertezza per la minore standardizzazione. `[STIMA bassa]`
- **Complessità/guasti/ridondanza:** l'**asimmetria del layout complica l'analisi dei modi di guasto** — un layout a 3 rotori con tilt parziale non ha la simmetria a 4 bracci di A2/A3, per cui un guasto singolo produce momenti di reazione meno standard e meno studiati in letteratura pubblica; il catalogo dei failure mode è meno maturo.
- **GNC/transizione:** eredita la complessità di A3 più l'onere aggiuntivo di gestire l'asimmetria del layout nel controllore.
- **Idoneità Pentema:** nessun vantaggio specifico identificato rispetto ad A3 per questo contesto operativo; introduce solo incertezza aggiuntiva.
- **TRL/COTS:** **bassa** — nessun prodotto COTS mainstream a scala C3 identificato con confidenza in questa ricerca. Famiglia essenzialmente di ricerca/nicchia.
- **Costo/tempo:** essenzialmente sviluppo bespoke, nessuna base di costo COTS applicabile.
- **Rumore:** variabile, non discriminante.

**Nota metodologica:** A6 è incluso per completezza del mandato ma **non emerge come alternativa competitiva** in nessuno scenario di questo trade study — la sua inclusione serve a documentare che lo spazio di soluzioni è stato esplorato, non a suggerire che meriti sviluppo dedicato.

### 4.8 A7 (baseline) — Ala fissa NON-VTOL, catapulta + recupero

- **Hover:** non applicabile — nessuna capacità di hover.
- **Crociera:** **la migliore delle 7 alternative** — nessuna massa morta di sistema VTOL, nessun drag parassita di nacelle/booms esposti, aerodinamica ottimizzabile senza compromessi (esattamente il concept HALE monoplano high-AR/T-tail del documento interno, pensato per questo). Riferimento diretto: `22-boxwing-vantaggio-tecnico.md` ha mostrato che il **CD0 di un VTOL "sporco" C3 è ~4x quello di un'ala pulita equivalente** (0,040 vs un'ipotetica ~0,011 di sola ala) — un fixed-wing non-VTOL recupera gran parte di quel margine.
- **Frazione payload:** **la migliore delle 7 alternative** — zero massa dedicata a sistemi VTOL. Piccola penalità (stimata **3-8% MTOM** `[STIMA media]`) se il recupero richiede paracadute/BRS dedicato invece di un semplice belly-landing su pista preparata.
- **Complessità/guasti/ridondanza:** il **velivolo** è il più semplice di tutti (nessun hardware VTOL a bordo), ma la complessità **si sposta a terra**: la catapulta e il sistema di recupero (rete/paracadute/skyhook) sono infrastrutture separate, da trasportare, montare e mantenere a ogni sito. Motore singolo in crociera = nessuna ridondanza propulsiva; un guasto motore forza un atterraggio di emergenza (planata) che in terreno montano ha **poche zone sicure** (pendii, bosco, abitato) — un rischio operativo specifico di questa geografia che pesa contro la baseline indipendentemente dal punteggio "transizione" (qui massimo per assenza strutturale della fase).
- **GNC/transizione:** **nessuna transizione VTOL da gestire** — punteggio massimo su questo asse specifico, ma va letto insieme al punto precedente (rischio di guasto motore in crociera non mitigato da una capacità di atterraggio verticale di riserva, a differenza di A2/A3).
- **Idoneità Pentema:** **il vincolo che la rende inadatta come prodotto operativo per questa missione**: una catapulta richiede una corsia di lancio libera di decine di metri, e un recupero a rete/paracadute richiede un'area di atterraggio sgombra comparabile — **incompatibile con "spazi di decollo ridotti in valle" e "atterraggio in zone alpestri"**, il vincolo che ha motivato l'intero mandato VTOL. È esattamente il motivo per cui il documento `10-fasce-engineering.md` §4.1 nota che un analogo militare comparabile (Insitu Integrator/RQ-21A Blackjack, lancio a catapulta/recupero skyhook) **non è compatibile con le aree ridotte di Pentema**.
- **TRL/COTS:** maturità alta in generale (catapulta+rete è tecnologia consolidata in ambito ISR tattico — es. famiglia Insitu ScanEagle/Integrator, ~20-61 kg, già citata in `10-fasce-engineering.md` §4.1 come riferimento di peso vicino a T1, sebbene non sia un prodotto COTS acquistabile per uso civile-delivery), ma **nessun vendor COTS orientato alla consegna civile in questa famiglia** è stato identificato — la famiglia catapulta+recupero è quasi esclusivamente ISR, non delivery.
- **Costo/tempo:** l'airframe stesso è il più economico, ma l'infrastruttura di lancio/recupero (catapulta portatile, sistema di rete) aggiunge costo e **logistica da replicare a ogni sito** — problematico per una famiglia di missioni multi-versante/multi-borgo come quella SNAI a cui Firmamento punta oltre Pentema.
- **Rumore:** il migliore in crociera (nessun hover), ma il lancio a catapulta (pneumatica/a molla) è un evento acustico/meccanico impulsivo, e il recupero a rete può essere brusco.

---

## 5. Analisi trasversale — GNC, modi di guasto, BRS/paracadute

| Configurazione | Autorità di controllo critica | Scenario di guasto più severo | Ruolo del BRS/paracadute |
|---|---|---|---|
| A1 Multirotore | Nessuna transizione; ridondanza hex/octo nota | Guasto multi-motore simultaneo (raro) | Backup secondario, raramente necessario vicino al suolo |
| A2 Lift+cruise | Handoff rotori→superfici in finestra di velocità nota | Guasto asimmetrico di un rotore di sostentamento durante hover a bassa quota | Backup; **ma i 3 rotori residui + motore crociera spesso permettono un atterraggio controllato senza BRS** — vantaggio specifico di questa famiglia |
| A3 Tilt-rotor | Gestione simultanea di spinta+portanza+eventuale asimmetria durante rotazione nacelle | Guasto motore o inceppamento meccanismo a metà rotazione | Backup primario raccomandato durante la finestra di tilt |
| A4 Tilt-wing | Come A3, aggravato da regime aerodinamico non lineare dell'ala in rotazione | Guasto durante rotazione ala (ala quasi in stallo, poco margine) | Backup primario fortemente raccomandato — probabile mitigazione obbligata in fase di certificazione |
| A5 Tail-sitter | Stima di assetto/velocità attraverso 90° di rotazione, superfici di controllo fuori regime nominale per gran parte della transizione | **Guasto motore singolo in qualsiasi fase = nessuna ridondanza propulsiva** | **BRS è la rete di sicurezza primaria, non secondaria** — punto debole strutturale della famiglia |
| A6 Tilt-tri | Come A3 più asimmetria di layout | Guasto motore con reazione non simmetrica, meno caratterizzata | Backup primario raccomandato, catalogo guasti meno maturo |
| A7 Baseline non-VTOL | N/A (nessuna transizione) | Guasto motore in crociera = planata forzata su terreno montano con poche aree sicure | **Paracadute/BRS è già parte integrante del sistema di recupero standard**, non un'aggiunta di sicurezza incrementale |

**Osservazione chiave:** la mitigazione M2 (paracadute/BRS), citata come opzione di mitigazione ground-risk in `13-fasce-regolatorio-missione.md` §3.3, **non ha lo stesso peso in ogni configurazione**. Per A5 (tail-sitter monomotore) è strutturalmente necessaria in ogni fase; per A2 (lift+cruise) la ridondanza propulsiva nativa la rende un backup vero, non l'unica linea di difesa — un argomento a favore di A2 che il solo criterio "sicurezza transizione" della matrice §7 non cattura pienamente e che va portato in sede di ConOps/SORA.

---

## 6. Criteri di valutazione e pesi

| ID | Criterio | Peso | Rationale del peso (specifico Firmamento/Pentema) |
|---|---|---|---|
| C1 | **Idoneità confined-space Pentema** (spazio di decollo/atterraggio ridotto, tolleranza a vento di valle/raffiche, superficie non preparata) | **20%** | È la ragione esplicita per cui si considera il VTOL (mandato, `13-fasce-regolatorio-missione.md` §3); peso massimo perché è il vincolo generativo del problema |
| C2 | **Sicurezza della transizione** (autorità GNC, modi di guasto, ridondanza) | **15%** | Fase più critica per qualunque VTOL con superfici mobili; rilevante per SORA ground-risk su missione di consegna sorvolando un borgo |
| C3 | **Frazione di payload utile** (quanto "mangia" il sistema VTOL sui 25 kg MTOM) | **15%** | C3 ≤25 kg è un **tetto duro**; ogni kg speso in hardware VTOL è un kg tolto a payload/batteria/range |
| C4 | **Efficienza in crociera / range-endurance** | **15%** | Necessaria per le missioni EO/relay ad area vasta oltre alla consegna punto-punto; coerente coi target 90-120 km/h, 40-80 km di `10-fasce-engineering.md` §3.2 |
| C5 | **TRL / disponibilità COTS** | **15%** | Coerente col verdetto "Buy COTS vince" (`05-piattaforme-costi.md` §11) e col modello operatore-di-servizi-non-OEM (`CLAUDE.md`): Firmamento non vuole finanziare R&D di airframe salvo necessità comprovata |
| C6 | **Semplicità meccanica / affidabilità / manutenibilità** | **10%** | Un operatore di servizi con flotta distribuita su più siti SNAI ha bisogno di basso carico di manutenzione, non di un banco prova sperimentale |
| C7 | **Costo/tempo di sviluppo o acquisto incrementale** | **5%** | Peso ridotto perché già ampiamente vincolato dai bracket dimostratore/prodotto di `10-fasce-engineering.md` §3.3 — è più un discriminante tra "dimostratore vs prodotto" che tra sotto-famiglie VTOL |
| C8 | **Rumore/impatto acustico** | **5%** | Rilevante per consegna su borgo abitato, ma secondario rispetto a sicurezza e spazio operativo |
| | **TOTALE** | **100%** | |

---

## 7. Matrice di scoring e soglia di ammissibilità (gate)

### 7.1 Scoring (1-10, 10 = ottimo), con nota metodologica

**Nota metodologica importante:** una matrice pesata pura può nascondere un vincolo "must-have" dietro una media ponderata favorevole su altri assi. Per questo, coerentemente con la logica Pugh (must-have prima del weighted score), si applica **prima** una **soglia di ammissibilità minima su C1** (idoneità confined-space): punteggio C1 < 5/10 → **alternativa esclusa dal ranking finale indipendentemente dal punteggio ponderato totale**, perché C1 è il vincolo generativo del problema (§6). Le alternative escluse restano comunque nella tabella per trasparenza.

| Criterio (peso) | A1 Multirotore | A2 Lift+cruise | A3 Tilt-rotor | A4 Tilt-wing | A5 Tail-sitter | A6 Tilt-tri | A7 Baseline non-VTOL |
|---|---|---|---|---|---|---|---|
| C1 Confined-space (20%) | 9 | 7 | 7 | 5 | 6 | 6 | **2** |
| C2 Sicurezza transizione (15%) | 10 | 6 | 4 | 3 | 3 | 4 | 10 |
| C3 Frazione payload (15%) | 3 | 6 | 7 | 5 | 9 | 6 | 10 |
| C4 Efficienza crociera (15%) | 2 | 8 | 7 | 7 | 7 | 6 | 10 |
| C5 TRL/COTS (15%) | 9 | 10 | 6 | 2 | 6 | 3 | 8 |
| C6 Semplicità/affidabilità (10%) | 8 | 6 | 4 | 2 | 6 | 3 | 8 |
| C7 Costo/tempo (5%) | 8 | 7 | 5 | 3 | 6 | 3 | 7 |
| C8 Rumore (5%) | 3 | 5 | 6 | 6 | 6 | 5 | 8 |
| **Score ponderato** | **6,75** | **7,10** | **6,95** | **4,20** | **6,15** | **4,75** | **7,65** |
| **Ammissibile (C1≥5)?** | Sì | Sì | Sì | Sì | Sì | Sì | **NO — escluso** |
| **Rank tra gli ammissibili** | 3° | **1°** | 2° | 6° | 4° | 5° | — |

### 7.2 Lettura del risultato — il paradosso apparente della baseline

La baseline non-VTOL (A7) **vince la matrice pesata pura (7,65, il punteggio più alto in assoluto)** grazie a punteggi massimi su transizione, payload, crociera e buon TRL — ma **fallisce la soglia di ammissibilità su C1** (score 2, ben sotto la soglia 5) perché catapulta e recupero a rete/paracadute **non sono fisicamente compatibili** con gli spazi di decollo/atterraggio disponibili a Pentema (§4.8, §2). Questo non è un artefatto della matrice: è **il motivo stesso per cui il mandato ha richiesto questo trade study** — dimostrare esplicitamente cosa si perde (efficienza, payload, semplicità, costo) rinunciando al VTOL, e perché a Pentema quella perdita è comunque necessaria.

**Conseguenza pratica:** A7 resta la scelta ottimale **per missioni EO/area-vasta su terreno dove esiste spazio per catapulta/recupero** (non è detto che tutti i futuri siti SNAI abbiano lo stesso vincolo di Pentema — vedi falsifying observation §10.2), ma è **squalificata come prodotto operativo per Pentema stessa**, in particolare per la missione di consegna.

Tra le alternative VTOL ammissibili, il vincitore è **A2 — Quadplane/lift+cruise (score 7,10)**, seguito a distanza ravvicinata da **A3 — Tilt-rotor (6,95)**.

---

## 8. Analisi di sensitività

### 8.1 Scenario baseline (pesi §6)
Vincitore tra gli ammissibili: **A2 (7,10)** > A3 (6,95) > A1 (6,75) > A5 (6,15) > A6 (4,75) > A4 (4,20). Margine A2-A3 stretto (0,15 punti su una scala 1-10 pesata) — **non un vantaggio schiacciante**, la decisione è sensibile a piccole variazioni di score o pesi su C2/C4.

### 8.2 Scenario "safety-first" (enfasi su sicurezza transizione)
Pesi modificati: C1→10%, C2→30% (da 15%), C5→15%, altri invariati proporzionalmente. Risultato: **A1 (multirotore puro) vince con 7,25**, superando A2 (6,90). Interpretazione: se un incidente regolatorio o una posizione ENAC/SORA particolarmente conservativa penalizza pesantemente il rischio di transizione (es. richiesta di margini di sicurezza aggiuntivi per qualunque fase di hand-off rotori↔ali), il multirotore puro — che per definizione non ha transizione — diventa la scelta razionale, **al prezzo però di rientrare potenzialmente sotto soglia sui requisiti di range/cruise** di `10-fasce-engineering.md` §3.2. Questo scenario è plausibile in una fase iniziale di dimostratore dove la tolleranza al rischio è bassa e le missioni sono a corto raggio.

### 8.3 Scenario "payload-first" (enfasi su frazione payload utile)
Pesi modificati: C3→30% (da 15%), C5→5%, altri invariati proporzionalmente. Risultato: **A5 (tail-sitter) sale a 6,75, quasi alla pari con A2 (6,70)** — un ribaltamento quasi-completo, ma **entro il rumore di stima** (±1 punto di scoring soggettivo sposterebbe l'esito). Interpretazione: se il payload utile diventa il vincolo dominante (es. un pod cargo medicale pesante che spinge contro il tetto dei 25 kg), il tail-sitter merita una valutazione più approfondita nonostante il suo handicap di sicurezza propulsiva (§5) e la mancanza di un meccanismo di sgancio in hover dimostrato.

### 8.4 Robustezza complessiva
**A2 (lift+cruise) è il vincitore più robusto** attraverso gli scenari testati (vince nel baseline, resta 2° nello scenario safety-first, resta competitivo nello scenario payload-first) — coerente con la sua posizione dominante nel mercato COTS reale (JOUAV, Quantum, la maggioranza dei vendor citati nel briefing di piattaforma), il che è un utile controllo di plausibilità esterno: il mercato converge dove la matrice converge. **Non è però un vincitore schiacciante**: A3 (tilt-rotor) resta una seconda scelta credibile con un profilo di rischio diverso (miglior payload, peggior sicurezza di transizione), e A1 (multirotore) diventa preferibile in un regime di massima avversione al rischio di transizione o per missioni a corto raggio dove il deficit di range non è dirimente.

---

## 9. Interazione tra scelta VTOL e scelta d'ala — collegamento al verdetto box-wing

Il mandato chiede esplicitamente se un lift+cruise "sporchi" l'ala e annulli il residuo vantaggio del three-lifting-surface. La risposta, ancorata ai numeri di `22-boxwing-vantaggio-tecnico.md`, è **sì, in modo quantitativamente dominante**:

1. **Il CD0 di un VTOL C3 "sporco" è dominato dall'hardware VTOL, non dalla forma dell'ala.** `22-boxwing-vantaggio-tecnico.md` §1.3 attribuisce **0,029 su 0,040 di CD0 totale (≈72%)** a fusoliera/booms/nacelle rotori esposti, contro **0,011 (≈28%)** alla sola ala. Il delta aerodinamico tra monoplano e three-lifting-surface stimato nello stesso documento (banda −5%…+8% su L/D di crociera, centrale ≈0%) è quindi **un effetto di second'ordine rispetto alla scelta stessa dell'architettura VTOL**: qualunque vantaggio o svantaggio di configurazione alare viene ampiamente sovrastato dalla resistenza aggiunta dai rotori di sostentamento e dalle loro strutture di supporto. **In altre parole: la scelta della configurazione VTOL (A1-A7) pesa sulla crociera più della scelta ala-monoplano-vs-box-wing.**

2. **Il lift+cruise è l'unica famiglia VTOL geometricamente coerente con un'ala chiusa/box.** `22-boxwing-vantaggio-tecnico.md` §2.2 individua nell'"integrazione strutturale della propulsione VTOL" (montare i 4 rotori di sostentamento ai 4 spigoli di un telaio box, eliminando i booms dedicati) **l'unica sinergia strutturale forte** del box-wing. Le altre famiglie non si adattano bene a un'ala chiusa: il tilt-rotor su un box-wing è esplicitamente definito "complicato (dove ruota?)" nello stesso documento; il tilt-wing richiederebbe di far ruotare un intero anello strutturale chiuso (impraticabile); il tail-sitter, con un'unica elica in prua, non ha bisogno di 4 punti di sostentamento e quindi non trae alcun beneficio geometrico da un box.

3. **Ma quella sinergia non salva il caso economico del box-wing.** Anche ammettendo che un lift+cruise "stia bene" geometricamente su un telaio box (risparmio stimato in `22-boxwing-vantaggio-tecnico.md` §2.2: 0,5-1,2 kg di booms evitati), la **penalità di download in hover peggiora** per un box-wing (scia dei rotori che impatta due ali invece di una: stimata 10-18% contro 5-10% di un monoplano, `22-boxwing-vantaggio-tecnico.md` §3) — un costo energetico che si scarica esattamente nella fase più critica del VTOL elettrico. Il verdetto combinato di questo documento e di `22-boxwing-vantaggio-tecnico.md` è quindi: **il lift+cruise è la famiglia VTOL meno incoerente con un box-wing, ma il box-wing stesso resta un dimostratore, non un prodotto**, perché il vantaggio aerodinamico residuo (già ≈0% in crociera pulita) viene ulteriormente eroso dal download in hover quando gli si aggiunge il VTOL.

4. **Per il concept attuale (monoplano high-AR/T-tail, elica traente in prua), l'add-on architetturalmente più economico non è il vincitore di questo trade study.** Il tail-sitter (A5) condivide la posizione dell'elica (prua, tirante) e la geometria alare del concept HALE esistente quasi senza modifiche — è, sulla carta, il minor salto architetturale dal disegno oggi esistente. Il lift+cruise vincitore (A2), al contrario, richiede l'aggiunta di 4 motori/booms/bracci **non previsti nel concept attuale** — un'estensione, non un adattamento. Questo non cambia la raccomandazione (A2 resta il vincitore su merito tecnico/regolatorio/di mercato, §7-8), ma va dichiarato come **costo di integrazione aggiuntivo non catturato dalla matrice**: adottare A2 significa ridisegnare sostanzialmente l'architettura del concept interno, non solo aggiungere un sottosistema.

**Sintesi per governance:** la scelta VTOL (questo documento) e la scelta d'ala (`22-boxwing-vantaggio-tecnico.md`) non sono indipendenti nella pratica realizzativa, ma **sono indipendenti nel giudizio di merito**: qualunque configurazione alare (monoplano o three-lifting-surface) sceglierà Firmamento, il verdetto di questo trade study (A2 lift+cruise per il prodotto operativo, con A1/A3 come alternative credibili) non cambia, perché l'effetto della configurazione VTOL sul CD0 totale domina l'effetto della configurazione alare di circa un ordine di grandezza (72% vs 28% del CD0, §1 sopra).

---

## 10. Raccomandazione

### 10.1 Raccomandazione primaria — prodotto di servizio operativo

**Per T1/BOXY come prodotto destinato a erogare un servizio operativo a Pentema, la configurazione raccomandata è A2 — Quadplane/lift+cruise ("VTOL a 5 motori").**

Razionale (ancorato a §7-8):
- Vince la matrice pesata tra le alternative ammissibili nello scenario baseline e resta il più robusto attraverso gli scenari di sensitività testati.
- È l'unica famiglia con **piena disponibilità COTS testata sul mercato alla scala T1** (JOUAV CW-15/CW-30E, Quantum Trinity F90+, già nel bracket di riferimento di `10-fasce-engineering.md` §3.2), coerente col verdetto "Buy COTS vince" già raggiunto per il Percorso 6A (`05-piattaforme-costi.md` §11) e col modello operatore-di-servizi-non-OEM (`CLAUDE.md`).
- Offre un vantaggio di sicurezza specifico per il terreno di Pentema non catturato pienamente dalla matrice: **guasto del motore di crociera ≠ perdita della capacità di atterraggio verticale** (i 4 rotori di sostentamento restano un'opzione di emergenza), rilevante su un terreno con poche zone di atterraggio forzato sicure.
- **Condizione necessaria dichiarata:** l'adattamento a BOXY richiede un'estensione strutturale del concept attuale (4 motori/booms aggiuntivi), non un semplice add-on — va budgetizzato come tale nella roadmap 0-12 mesi.

### 10.2 Alternativa credibile — tilt-rotor (A3)

**A3 (tilt-rotor, es. famiglia Wingcopter) è una seconda scelta legittima**, in particolare se: (a) la frazione di payload è il vincolo più stringente (missione cargo pesante vicino al tetto 25 kg), oppure (b) esiste un vendor con track record di consegna reale che riduce il rischio percepito rispetto al profilo teorico di sicurezza transizione (§5). **Wingcopter ha già un track record operativo di consegna medicale/pacchi** citato in `13-fasce-regolatorio-missione.md` §3.6, un dato concreto che pesa a suo favore oltre il punteggio astratto della matrice.

### 10.3 Dimostratore vs prodotto — distinzione esplicita richiesta dal mandato

- **Come dimostratore tecnologico/banco di prova IP** (coerente con `10-fasce-engineering.md` §3.3, target €150-400k, 12-24 mesi), **qualunque configurazione VTOL tra A1-A3 è difendibile**, incluso l'eventuale abbinamento con il three-lifting-surface per scopi di vetrina tecnica (§9) — a patto di dichiarare esplicitamente che l'obiettivo è dimostrativo, non operativo, coerentemente col verdetto di `22-boxwing-vantaggio-tecnico.md` §7.
- **Come prodotto pronto per erogare un servizio operativo autorizzato PA/Protezione Civile**, la raccomandazione è netta: **adattare un lift+cruise COTS esistente (A2)**, non sviluppare un'architettura VTOL proprietaria da zero. Sviluppare A4 (tilt-wing) o A6 (tilt-tri) da zero per un prodotto operativo non è giustificato da nessuno scenario di questo trade study (score più bassi in ogni sensitività, TRL insufficiente, nessuna base COTS).

### 10.4 Sul VTOL puro vs "VTOL leggero + STOL/catapulta" vs restare non-VTOL

Il mandato chiede di valutare anche un'ipotesi ibrida. La risposta di questo trade study:
- **Per la missione di consegna a Pentema, non esiste un'alternativa credibile al VTOL vero** (§7.2: A7 è squalificata dal gate C1 per questa missione specifica) — non c'è spazio per una corsia di lancio a catapulta né per un'area di recupero a rete in un borgo di montagna.
- **Per missioni EO/area-vasta su terreno diverso da Pentema** (altri siti SNAI, versanti con più spazio), **A7 resta l'opzione col miglior rapporto efficienza/costo/semplicità** e non va scartata a priori per l'intera famiglia di prodotto T1 — è una decisione **per-sito**, non per-piattaforma. Una possibile strategia di famiglia: **due varianti T1** (VTOL lift+cruise per siti confined-space come Pentema; fixed-wing catapulta-recupero per siti con spazio disponibile), condividendo ala/avionica/payload dove possibile (coerente col framework di modularità di `10-fasce-engineering.md` §7). Questa ramificazione **non è stata validata in dettaglio in questo documento** e andrebbe sviluppata come TS separato se la strategia multi-sito matura.
- **Un "VTOL leggero" ibrido** (es. STOL con rullata assistita corta + recupero morbido, invece di hover pieno) non è stato modellato come alternativa a sé in questo trade study per assenza di un caso d'uso Pentema credibile (nessun dato di sopralluogo su spazi anche minimi disponibili) — è segnalato come falsifying observation aperta (§11.2).

---

## 11. Falsifying observations

Osservazioni che, se verificate, cambierebbero la raccomandazione di questo documento:

1. **Test CFD/galleria (L2, per analogia con `22-boxwing-vantaggio-tecnico.md` §5) che misuri un download in hover per un lift+cruise su three-lifting-surface superiore al 20%** (oltre la banda stimata 10-18%) — sposterebbe il bilancio energetico a favore di A3 (tilt-rotor) o di un'architettura senza rotori di sostentamento dedicati.
2. **Sopralluogo a Pentema che riveli almeno un'area piana libera di 40-60 m in prossimità di un punto di missione** (anche non del punto di consegna finale, es. per un hub di lancio a monte) — riaprirebbe la valutazione di A7 (baseline non-VTOL) o di un'ipotesi ibrida STOL come opzione parziale per alcune missioni (non annullerebbe comunque il bisogno di VTOL per il punto di consegna finale in borgo).
3. **RFQ vendor reale (non stima) che mostri un TCO 5 anni di un tilt-rotor COTS (es. Wingcopter-class) inferiore o comparabile a un lift+cruise equivalente (JOUAV CW-15-class)** — falsificherebbe il vantaggio di costo assegnato ad A2 (C7, score 7 vs 5) e rafforzerebbe A3 come vincitore alternativo.
4. **Dati di volo reali (log vendor o prova diretta Firmamento) che mostrino un tasso di guasto della fase di transizione lift+cruise superiore a quanto assunto** (score C2=6, "ben nota/gestibile") — sposterebbe la raccomandazione verso A1 (multirotore puro) o A5 (tail-sitter), coerentemente con lo scenario di sensitività "safety-first" (§8.2).
5. **Conferma ENAC in pre-application che la missione di consegna medicale a Pentema richieda SAIL III-IV con dimostrazione di contenimento più severa del previsto** (`13-fasce-regolatorio-missione.md` §3.3) — potrebbe penalizzare qualunque configurazione con hover prolungato su abitato, ribilanciando il peso di C1 verso configurazioni a minimo tempo di sorvolo (es. approccio ad alta quota + discesa verticale rapida, meglio supportata da A2/A3 che da A1).
6. **Misura acustica in campo (non stima) che mostri un lift+cruise superiore a 75-80 dB(A) alla distanza tipica di sgancio del carico** — falsificherebbe il punteggio rumore assegnato ad A2 (C8=5) e potrebbe favorire A5/A3 (meno motori attivi in fase di sgancio).
7. **Analisi L1 VLM del box-wing con rotori ai 4 angoli (raccomandata in `22-boxwing-vantaggio-tecnico.md` §5) che mostri un ΔCD0 aggiuntivo inferiore alla stima 0,029** — attenuerebbe la conclusione del §9 secondo cui la scelta VTOL domina la scelta d'ala sul CD0 totale, riaprendo (parzialmente) il caso per il three-lifting-surface come base di un prodotto, non solo di un dimostratore.

---

## Riga di fondo

Tra le architetture VTOL disponibili per una piattaforma C3 da 25 kg, il **quadplane/lift+cruise (A2)** è la scelta più robusta per un prodotto di servizio operativo a Pentema: vince la matrice pesata nello scenario baseline, resta competitivo nelle sensitività testate, ha la maggiore disponibilità COTS reale (coerente col modello Buy-COTS/operatore-non-OEM di Firmamento), e offre un margine di sicurezza specifico — la capacità di atterraggio verticale di riserva in caso di guasto del motore di crociera — particolarmente rilevante su un terreno montano povero di zone di atterraggio forzato sicure. Il tilt-rotor (A3, famiglia Wingcopter) resta una seconda scelta legittima con un profilo di rischio diverso (miglior payload, transizione meno matura). La baseline non-VTOL (A7), pur vincendo la matrice pesata pura su ogni criterio "di volo" (crociera, payload, semplicità), è **esclusa per un vincolo di soglia non negoziabile**: catapulta e recupero a rete non stanno fisicamente negli spazi di Pentema — il che conferma, con numeri, il motivo stesso per cui il mandato ha richiesto un VTOL. Il lift+cruise vincitore, tuttavia, non è un semplice add-on al concept interno attuale (monoplano, elica in prua): richiede una ri-progettazione strutturale (4 motori/booms aggiuntivi), e la scelta VTOL pesa sul drag totale di crociera più della scelta tra monoplano e three-lifting-surface — per cui, coerentemente con `22-boxwing-vantaggio-tecnico.md`, qualunque investimento nel box-wing va tenuto **esplicitamente confinato al ruolo di dimostratore**, non di base per il prodotto BOXY operativo.

---

## Fonti e confidence

| Fonte | Tipo | Confidence | Uso in questo documento |
|---|---|---|---|
| `10-fasce-engineering.md` (repo) | Interna, dati T1 già triangolati | media | Target prestazionali T1, bracket COTS JOUAV/Quantum, riferimento Wingcopter/ScanEagle |
| `22-boxwing-vantaggio-tecnico.md` (repo) | Interna, calcolo L0/L1 | media | CD0 breakdown VTOL "sporco", download in hover box-wing, sinergia telaio-box/rotori VTOL (§9 di questo doc) |
| `13-fasce-regolatorio-missione.md` (repo) | Interna, regolatorio | medium-high per i FATTO normativi, medium per le stime SAIL | Vincoli di missione consegna medicale, SAIL atteso, contenimento carico |
| `Progetto concettuale struttura HALE.md` (repo) | Interna, concept design | alta (verifica diretta) | Baseline architetturale attuale (monoplano, elica prua, T-tail), assenza di VTOL nel concept |
| Teoria del disco attuatore (momentum theory) | Fisica consolidata | alta (fisica), media (applicazione ai valori assunti) | Calcoli hover §4.1 |
| JOUAV CW-15/CW-30E, Quantum Trinity F90+ | Datasheet vendor | medium (non verificato da RFQ diretta) | Esempi COTS lift+cruise |
| Wingcopter 198/178 | Datasheet vendor + track record pubblico consegna | medium-alta (prodotto reale con operazioni documentate) | Esempio COTS tilt-rotor, benchmark peso/payload C3 |
| WingtraOne GEN II | Datasheet vendor | media | Esempio COTS tail-sitter (mapping, non cargo) |
| Insitu ScanEagle/Integrator/RQ-21A Blackjack | Dominio pubblico, contratti governativi | media (bundling rende difficile isolare unit cost, già segnalato in `10-fasce-engineering.md`) | Esempio catapulta+recupero a scala vicina, incompatibilità con spazi ridotti |
| NASA Greased Lightning GL-10 | Dominio pubblico, programma di ricerca | alta (esistenza del programma), non vendor | Assenza di COTS maturo per tilt-wing |
| Canadair CL-84, LTV XC-142, Airbus Vahana | Dominio pubblico, storia aviazione | alta (fatti storici), qualitativo | Difficoltà storica della famiglia tilt-wing anche con pilota/investimenti importanti |
| Convair XFY Pogo, Lockheed XFV | Dominio pubblico, storia aviazione | alta (fatti storici), qualitativo | Difficoltà storica della famiglia tail-sitter pilotata (analogia parziale per il carico GNC in un UAS) |
| Quantum Vector, AeroVironment (tilt-rotor) | Citazione da mandato, non verificata in questa ricerca | bassa-media | Esempi aggiuntivi famiglia tilt-rotor |
| Tutte le stime di frazione MTOM (§4, per configurazione) | Stima ingegneristica per analogia, nessun dato di test | bassa-media, dichiarata per riga | Confronto qualitativo tra famiglie, non specifiche di un design BOXY reale (che non esiste) |

**Limiti dichiarati:** nessun prototipo BOXY esiste in nessuna configurazione (coerente con `10-fasce-engineering.md` e `22-boxwing-vantaggio-tecnico.md`); tutti i punteggi della matrice §7 sono giudizio ingegneristico esperto, non output di un modello quantitativo validato; la matrice pesata è per sua natura sensibile a scelte soggettive di scoring — la sensitività §8 mitiga ma non elimina questo limite. Nessuna quotazione vendor reale è stata usata: tutti i costi sono per analogia/bracket, coerentemente col vincolo del mandato.
