### Relazione Tecnica Comparativa: Architetture HALE e VTOL per Servizi nelle Aree Interne

#### 1.0 Introduzione e Contesto Strategico

La presente relazione fornisce un'analisi tecnica comparativa tra due percorsi architetturali per lo sviluppo di una piattaforma aerea senza pilota: l'architettura pilota a breve termine **VTOL (Vertical Take-Off and Landing)** e la visione strategica a lungo termine **HALE (High Altitude Long Endurance)** . Lo scopo di questo documento è supportare una decisione informata e basata su evidenze per gli stakeholder del progetto di **Firmamento Technologies** , finanziato nell'ambito del bando Cooding Prototypes. La tesi architetturale di fondo è che il pilota VTOL non rappresenta una mera opzione, ma un prerequisito obbligatorio e di riduzione del rischio per la realizzabilità della visione strategica HALE.Il progetto si inserisce nel quadro della **Strategia Nazionale per le Aree Interne (SNAI)** , con l'obiettivo primario di valutare la fattibilità di servizi a elevato valore pubblico — quali monitoraggio ambientale, prevenzione dei rischi naturali e connettività digitale — per le comunità delle aree interne liguri. Questo sforzo è condotto in stretta collaborazione con una rete di cooperative partner, che agiscono come "utenti-pilota" per garantire che le soluzioni tecnologiche rispondano a fabbisogni reali e concreti del territorio.Questa relazione è strutturata per guidare il processo decisionale in modo metodico. Inizieremo con un inquadramento dei due percorsi architetturali, seguito da un'analisi dettagliata di ciascuna opzione, evidenziandone specifiche, rischi e condizioni di successo. Successivamente, un confronto diretto metterà in luce i compromessi (trade-off) strategici tra le due soluzioni. Infine, una sintesi decisionale formulerà delle raccomandazioni operative chiare per le fasi successive del programma.L'analisi condotta nel Piano di Fattibilità ha identificato due percorsi distinti e sequenziali, uno orientato alla validazione immediata e l'altro alla visione a lungo termine. È quindi necessario analizzare in dettaglio questi due percorsi per comprendere appieno le loro implicazioni strategiche, tecniche ed economiche.

#### 2.0 Inquadramento dei Percorsi Architetturali

Per governare la complessità e l'incertezza intrinseche in un progetto tecnologicamente ambizioso, è stato adottato un approccio metodologico rigoroso, basato sul **NASA Systems Engineering Handbook** . Questo approccio, definito "gate-driven" e "risk-informed", permette di scomporre la roadmap in fasi distinte, ciascuna con chiari criteri di Go/No-Go. In questo modo, le decisioni di investimento sono incrementali e subordinate al raggiungimento di evidenze verificabili, riducendo il rischio complessivo.Il Piano di Fattibilità ha identificato due percorsi architetturali complementari, ma temporalmente e tecnologicamente disgiunti:

- **Percorso 6A (Pilota VTOL, 0–12 mesi):** Rappresenta la soluzione a basso rischio tecnologico (TRL 8–9), concepita per una validazione operativa immediata. L'obiettivo è dispiegare una piattaforma commerciale nel sito pilota di Pentema per testare i concetti operativi, interagire con le cooperative e generare dati reali. Questo percorso agisce come un fondamentale abilitatore, fornendo l'esperienza e le evidenze necessarie per informare le decisioni strategiche future con un investimento contenuto.

- **Percorso 6B (HALE Stratosferico, 24–48 mesi):** Costituisce l'evoluzione strategica a medio-lungo termine del progetto. La sua attivazione è condizionata al successo della Fase 1 e al reperimento di finanziamenti dedicati. Questo percorso è finalizzato a colmare i gap tecnologici critici (portando il TRL da 4 a 5) e a validare il quadro regolatorio emergente per gli HAPS (High Altitude Platform Systems), posizionando il progetto come un'infrastruttura "pseudo-satellitare" ad alto impatto.Il razionale strategico dietro questa separazione è la **flessibilità decisionale** . L'approccio duale permette di generare valore immediato e apprendimento operativo tramite il pilota VTOL, senza impegnare da subito le ingenti risorse richieste dalla R&S del sistema HALE. Se il pilota VTOL dimostrasse di essere sufficiente a soddisfare i bisogni primari delle cooperative, il progetto potrebbe stabilizzarsi su questa soluzione. Al contempo, i dati e gli asset (es. Ground Control Station, framework di data governance) sviluppati nel Percorso 6A sarebbero comunque riutilizzabili, de-rischiando e accelerando una futura transizione verso l'architettura HALE qualora le condizioni strategiche e finanziarie lo consentissero.Di seguito, si procederà con l'analisi dettagliata del percorso operativo a breve termine.

#### 3.0 Analisi Architettura Pilota: Percorso 6A (VTOL Ibrido)

L'obiettivo architetturale primario del Percorso 6A non è il mero dispiegamento di un drone, ma l'acquisizione dell'intelligence operativa, regolatoria e di stakeholder non negoziabile, necessaria per validare il business case dell'intero programma con un dispendio iniziale minimo. Questa architettura è la soluzione raccomandata per la Fase 1 (0-12 mesi). Utilizzando una piattaforma commerciale ad alta maturità tecnologica, questo percorso permette di concentrarsi sulla fattibilità operativa e sull'integrazione con gli stakeholder territoriali, piuttosto che sulla ricerca e sviluppo di base.La tabella seguente riassume la valutazione di fattibilità per l'architettura VTOL, basata su un'analisi multidimensionale

3.1 Specifiche Tecniche e Operative

Le specifiche chiave dell'architettura VTOL (Percorso 6A) sono state definite per garantire una rapida implementazione e la validazione degli obiettivi pilota.

- **Velivolo:** Si prevede l'utilizzo di un modello commerciale come il **JOUAV CW-30E** o un suo equivalente. La piattaforma offre un'endurance nominale di **6-10 ore** in ciclo operativo, un'altitudine massima di **5 km** e un sistema di propulsione ibrido (batterie e turbogeneratore) che garantisce flessibilità e sicurezza.

- **Payload:** La configurazione prevede una architettura a doppio slot per ospitare simultaneamente moduli di **comunicazione** (es. relay LTE/5G emulato) e di **osservazione** (es. telecamera elettro-ottica). L'interfaccia payload sarà standardizzata per permettere uno scambio rapido dei moduli (\<30 min).

- **Segmento di Terra (GCS):** La Ground Control Station sarà localizzata a Pentema e richiederà un'infrastruttura minima: un'area dedicata per l'antenna e il landing pad, un'alimentazione elettrica stabile (es. 400V 16A con UPS) e una connessione internet di backhaul con una capacità di almeno **10 Mbps** .

- **Budget Energetico e di Massa:** L'analisi preliminare conferma che l'endurance di 6-10 ore è fattibile con il sistema ibrido, anche in condizioni invernali (con una prevedibile riduzione delle prestazioni). Il budget di massa è accettabile, ma presenta un potenziale **rischio regolatorio** : se il peso massimo al decollo (MTOW) dovesse superare i **25 kg** , si renderebbe necessaria una procedura autorizzativa ENAC più complessa (SORA Specific).

- **Link Budget e Copertura:** L'analisi del collegamento di comunicazione conferma un margine positivo di **+11 dB** , indicando una connessione robusta e affidabile anche in condizioni non ottimali, e garantendo un link stabile fino a 50+ km in linea di vista. La latenza end-to-end è stimata inferiore a **120 ms** , pienamente compatibile con le operazioni tattiche. La copertura effettiva da una quota di 5 km è di circa **80 km di diametro** , anche se si prevedono zone d'ombra del 20-30% a causa della complessa orografia ligure.

##### 3.2 Roadmap, Rischi e Condizioni di Successo

La roadmap operativa per il pilota VTOL è strutturata in quattro fasi sequenziali, con "funding gates" che condizionano l'avanzamento al raggiungimento di evidenze specifiche.\| **Fase** \| **Durata** \| **Obiettivo Principale** \| **Costo Stimato (Range)** \|\| ------ \| ------ \| ------ \| ------ \|\| **F1: Design Preliminare** \| M+0 – M+2 \| Definizione CONOPS, selezione piattaforma COTS e avvio procurement. \| €50k – €100k \|\| **F2: Integrazione e Test a Terra** \| M+2 – M+8 \| Integrazione payload, setup GCS a Pentema, test software e batterie. \| €150k – €300k \|\| **F3: Flight Test Controllati** \| M+8 – M+10 \| Primo volo, validazione avionica e performance in ambiente reale. \| €100k – €150k \|\| **F4: Operazioni Pilota** \| M+10 – M+12 \| Esecuzione di missioni ordinarie e di emergenza, training cooperative. \| €57k – €118k \|

Il successo di questo percorso dipende dalla gestione proattiva dei rischi critici. I principali cinque rischi identificati sono:

- **T-A3-01 (Spettro Radio AGCOM):** La mancata o ritardata autorizzazione per la banda di comunicazione è un potenziale blocco operativo (impatta direttamente la fattibilità del link descritto in Sez. 3.1).

- **Mitigazione Tecnica:** Avviare una consultazione immediata con AGCOM e preparare un piano di fallback tecnico sulla banda ISM a 2.4 GHz.

- **T-A3-07 (Validazione CONOPS):** Procedure operative incomplete o non validate con la Protezione Civile possono compromettere la prontezza operativa.

- **Mitigazione Tecnica:** Dedicare un ingegnere CONOPS a tempo pieno e organizzare workshop iterativi con gli stakeholder per validare gli scenari.

- **T-A3-06 (Coinvolgimento Cooperative):** Un basso livello di partecipazione da parte delle cooperative ridurrebbe la qualità del feedback e il valore del pilota.

- **Mitigazione Tecnica:** Formalizzare la collaborazione tramite Memorandum of Understanding (MOU) e strutturare incentivi per la partecipazione.

- **T-A3-04 (Superamento MTOW \>25 kg):** Il superamento della soglia di peso di 25 kg complicherebbe l'iter regolatorio (direttamente legato al budget di massa e alla configurazione del payload descritti in Sez. 3.1).

- **Mitigazione Tecnica:** Progettare una configurazione di payload leggera e condurre un'analisi di impatto SORA se il limite viene superato.

- **T-A3-02 (Ritardi Autorizzativi ENAC):** Ritardi nel percorso SORA (Specific Operations Risk Assessment) potrebbero far slittare l'avvio dei test di volo.

- **Mitigazione Tecnica:** Avviare una pre-consultazione con ENAC per identificare il percorso autorizzativo più rapido.Infine, l'avvio del percorso è subordinato al soddisfacimento di cinque condizioni critiche di attivazione:

- **Autorizzazione Spettro AGCOM:** Ottenere una risposta formale sulla disponibilità della banda L-band o validare il fallback su ISM.

- **Percorso Regolatorio ENAC Chiaro:** Ricevere un'indicazione preliminare da ENAC sul percorso SORA applicabile.

- **Disponibilità Sito GCS:** Formalizzare l'allocazione del terreno a Pentema con le relative utenze e autorizzazioni.

- **MOU con le Cooperative:** Sottoscrivere accordi di collaborazione con almeno l'80% della rete di cooperative partner.

- **Completezza Integrazione Payload:** Firmare l'Interface Control Document (ICD) e completare i test di mock-up per validare la compatibilità.Superata l'analisi della soluzione a breve termine, è necessario ora esaminare l'opzione strategica a lungo termine: l'architettura HALE.

#### 4.0 Analisi Architettura Strategica: Percorso 6B (HALE Stratosferico)

L'architettura HALE (Percorso 6B) rappresenta la visione a lungo termine del progetto, una piattaforma stratosferica concepita per colmare il "vuoto di quota" tra le infrastrutture terrestri e quelle satellitari. Operando a circa 20 km di altitudine per settimane o mesi, un velivolo HALE può offrire servizi di connettività e osservazione persistente su scala regionale. Questa sezione valuta la sua fattibilità attuale, concentrandosi sui gap tecnologici e sui rischi sistemici che oggi ne condizionano l'avvio e che ne giustificano la classificazione come opzione strategica e non come soluzione immediata.La tabella seguente offre una sintesi del verdetto tecnico-economico-regolatorio per l'architettura HALE.

##### 4.1 Specifiche Concettuali e Gap Tecnologici

Le specifiche concettuali delineano una piattaforma altamente performante ma tecnologicamente sfidante.

- **Velivolo:** Si tratta di un'ala fissa ad altissimo allungamento alare (aspect ratio \>40), con una struttura ultraleggera in materiali compositi, progettata per operare a quote stratosferiche ( **18–24 km** ) con un'endurance nominale di **settimane o mesi** .

- **Propulsione:** Il sistema si basa interamente sull'energia solare. Pannelli fotovoltaici ad alta efficienza coprono le superfici alari per alimentare i motori elettrici durante il giorno e per ricaricare un pacco batterie che garantisce la persistenza operativa durante la notte.

- **Payload:** Le capacità target sono quelle di un'infrastruttura avanzata, come un **relay HAPS conforme allo standard 3GPP** per la connettività 4G/5G e sensori per l' **osservazione geospaziale** persistente.L'analisi di fattibilità ha però messo in luce diversi *showstopper* e gap tecnologici che attualmente impediscono l'avvio di un programma di sviluppo su larga scala:

- **Energia Invernale:** La sfida principale è la persistenza durante l'inverno a latitudini europee. Il ciclo di accumulo e scarica delle batterie a bassissime temperature (-30°C) e con bassa irradiazione solare non è stato ancora validato in modo affidabile. Un fallimento in questo ambito renderebbe l'operatività possibile solo per una parte dell'anno, minando il business case.

- **Aeroelasticità (Flutter):** Le ali ad altissimo allungamento, necessarie per l'efficienza aerodinamica in stratosfera, sono suscettibili a fenomeni aeroelastici come il flutter, **una vibrazione auto-amplificata che può portare a una rottura catastrofica della struttura in volo** . Il margine di sicurezza su configurazioni così estreme è ancora oggetto di ricerca.

- **Avionica e Autonomia:** Non esistono sul mercato autopiloti commerciali (COTS) certificati per missioni di durata superiore alle 48 ore. Lo sviluppo di un sistema di controllo del volo affidabile per operazioni di settimane o mesi richiede un significativo sforzo di R&S.

- **Vuoto Normativo:** Manca un percorso regolatorio consolidato per la certificazione e l'operatività degli HAPS sia a livello europeo (EASA) che nazionale (ENAC). Anche l'allocazione dello spettro radio per i servizi HAPS è ancora oggetto di negoziazioni internazionali, creando un'incertezza critica.

- **Sostenibilità Economica:** I costi di sviluppo e costruzione sono di un ordine di grandezza superiore a quelli del pilota VTOL (CAPEX Fase 3 stimato tra **€35M e €65M** ). Attualmente, non vi sono finanziamenti assicurati per un impegno di questa portata.In sintesi, i gap tecnologici non sono isolati, ma interconnessi: l'incertezza aeroelastica impatta il peso, che a sua volta aggrava la criticità del bilancio energetico invernale, il tutto in un contesto di totale vuoto normativo. Questo profilo di rischio sistemico, e non un singolo ostacolo, rende attualmente non avviabile lo sviluppo su larga scala.

##### 4.2 Roadmap di R&D e Rischi

Data l'immaturità tecnologica, il Percorso 6B non prevede la costruzione immediata di un velivolo su scala reale. La roadmap proposta per i prossimi 24-48 mesi è una fase di **Ricerca e Sviluppo** mirata a ridurre il rischio tecnico-regolatorio. Le attività includerebbero il design preliminare, la prototipazione e il test di sottosistemi critici (es. batterie, sezioni alari) e lo sviluppo di un dimostratore in scala ridotta per validare i modelli aerodinamici e di controllo.

Avendo analizzato separatamente le due architetture, è ora possibile procedere al loro confronto diretto per evidenziare i compromessi strategici.

#### 5.0 Analisi Comparativa e Compromessi Strategici

Questa sezione distilla le analisi precedenti in un confronto diretto per evidenziare i compromessi (trade-off) fondamentali che gli stakeholder devono considerare. L'obiettivo è mettere in luce come le due architetture rispondano a obiettivi diversi, operando su scale temporali, di rischio e di investimento radicalmente differenti. Non si tratta di determinare quale architettura sia "migliore" in assoluto, ma quale percorso strategico sia più coerente con gli obiettivi e i vincoli attuali del programma.La tabella seguente riassume i parametri chiave di confronto tra il Percorso 6A (VTOL) e il Percorso 6B (HALE).

L'analisi comparativa converge su un compromesso architetturale irriducibile. Il **percorso VTOL** rappresenta una strategia di **"apprendimento rapido" e "valore immediato"** . Con un investimento contenuto e un basso profilo di rischio, permette di testare il mercato, validare i servizi con le cooperative, stabilire relazioni con gli enti regolatori e generare risultati concreti in meno di un anno. Il suo limite è la scalabilità: la sua natura tattica non può soddisfare l'ambizione di una copertura regionale persistente.Al contrario, il **percorso HALE** costituisce un investimento ad alto rischio per una **"capacità strategica futura"** . Richiede un impegno finanziario e temporale di un ordine di grandezza superiore, affrontando rischi tecnici e regolatori che potrebbero bloccarne lo sviluppo. Tuttavia, il suo potenziale è trasformativo: se realizzato con successo, creerebbe un'infrastruttura aerea unica, in grado di offrire servizi impossibili da replicare con le attuali piattaforme VTOL.Dal punto di vista architetturale, i percorsi 6A e 6B devono essere considerati sequenziali e non alternativi. Il successo del primo è una condizione abilitante per il secondo. Il pilota VTOL agisce come un passo fondamentale per il percorso HALE: i dati operativi, il feedback delle cooperative, i protocolli con la Protezione Civile e gli asset riutilizzabili (come la Ground Control Station e il framework di data governance) generati dalla Fase 1 sono essenziali per ridurre l'incertezza e informare il design del futuro sistema HALE, rendendo l'investimento iniziale nel VTOL una mossa strategica anche per la visione a lungo termine.Questa analisi comparativa ci porta ora alla sintesi finale e alle raccomandazioni operative.

#### 6.0 Sintesi Decisionale e Raccomandazioni

Questa sezione finale ha l'obiettivo di tradurre l'analisi comparativa in un verdetto chiaro e in una serie di raccomandazioni operative per gli stakeholder. In linea con l'approccio "evidence-based" e "risk-informed" del progetto, le conclusioni sono formulate per fornire una base solida e tracciabile per le decisioni strategiche da intraprendere.Il verdetto integrato per ciascun percorso architetturale è il seguente:

- **Percorso 6A (VTOL): GO CONDIZIONATO.** La fattibilità tecnica e operativa del pilota VTOL è dimostrata. La piattaforma è matura, i rischi sono gestibili e l'investimento è proporzionato ai risultati attesi a breve termine. L'avvio è tuttavia subordinato alla chiusura di specifiche condizioni abilitanti di natura regolatoria, logistica e contrattuale, da finalizzare nei primi mesi del programma.

- **Percorso 6B (HALE): HOLD / GO-CONDIZIONATO ESTREMO.** La fattibilità dell'architettura HALE non è attualmente dimostrata. Esistono showstopper tecnici e regolatori critici che richiedono un significativo sforzo di ricerca e sviluppo prima di poter giustificare un impegno finanziario su larga scala. Si raccomanda un approccio di de-risking mirato, posticipando ogni decisione di investimento massiccia.

##### Raccomandazione Esecutiva Finale

Sulla base delle evidenze raccolte e del verdetto integrato, si formulano le seguenti raccomandazioni esecutive:**1. Procedere con l'avvio immediato del Percorso 6A (Pilota VTOL), allocando il budget necessario stimato tra €450k e €750k.** Questa azione permetterà di capitalizzare il lavoro di pianificazione svolto, generare valore immediato per il territorio e raccogliere dati essenziali per le decisioni future. Questo budget si riferisce ai costi diretti di fase, coerentemente con il verdetto finale del Piano di Fattibilità (Fonte: 12C.5). Il costo complessivo del programma pilota, incluse le attività preparatorie, è stimato in un range di €600k-900k (Fonte: 12A.1).**2. Porre il Percorso 6B (HALE) in stato di HOLD, posticipando ogni decisione di investimento significativa.** L'avanzamento su questo percorso dovrà essere condizionato ai risultati positivi del pilota VTOL e al completamento di specifiche attività di riduzione del rischio (es. test di laboratorio su batterie, finalizzazione di partnership strategiche per l'avionica, chiarimento del percorso regolatorio con EASA).

##### 10 Condizioni Essenziali Go/No-Go per il Percorso 6A (VTOL)

L'avvio operativo del pilota VTOL (Percorso 6A) è propedeutico al soddisfacimento delle seguenti dieci condizioni critiche. Il loro completamento entro le scadenze indicate costituisce il framework Go/No-Go per il progresso del progetto.
