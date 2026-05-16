# **1. Introduzione e finalità**

Il presente progetto richiede il finanziamento del **Piano di Fattibilità H.A.L.E.** (High Altitude Long Endurance), con l’obiettivo di validare in modo tecnico-scientifico, operativo e regolatorio l’adozione di uno strumento a supporto delle aree interne italiane e del network di dieci cooperative aderenti a Legacoop (prevalentemente **cooperative di comunità**.  
**Che cos’è H.A.L.E.:** un velivolo stratosferico solare ad ala fissa, a lunga autonomia (settimane/mesi), con payload modulare (sensori e telecomunicazioni), capace di operare ~20 km sopra il suolo come “pseudo-satellite” a bassa latenza e copertura mirata.

Il piano di fattibilità definirà se H.A.L.E. possa costituire uno strato infrastrutturale resiliente, integrato e complementare a reti terrestri e satellitari, per connettività di emergenza/ordinaria, osservazione geospaziale in tempo reale e servizi dati abilitanti per le cooperative partner e i territori serviti. Non si prevede costruzione di velivoli; l’attività riguarda analisi, modellazione, simulazione, co-progettazione, pre-verifica regolatoria e definizione del pilota per la fase successiva.

# **2. Quadro conoscitivo: contesto e fabbisogni delle aree interne**

Le aree interne italiane combinano bassa densità insediativa, orografia complessa (montagne, vallate, isole minori) e reti fisiche e digitali discontinue: questa triade genera costi unitari elevati per infrastrutture di connettività e tempi di ripristino lunghi dopo guasti o eventi estremi. Ne derivano: (i) “vuoti” di servizio sanitario, scolastico e di mobilità; (ii) isolamento informativo e operativo nelle emergenze; (iii) difficoltà di attrarre e trattenere persone e attività economiche. La crescente frequenza di incendi, alluvioni e frane interrompe dorsali e accessi locali, attivando black-out comunicativi che rallentano triage, teleconsulto e coordinamento dei soccorsi, con impatti diretti su sicurezza e continuità operativa.

In questo quadro, le cooperative di comunità presidiano servizi di prossimità e spazi collettivi, agendo da “integrazione di ultima miglio” dove mercato e PA non arrivano con continuità; le cooperative sociali e le mutue gestiscono protezione sociale e sanitaria in logica non lucrativa, integrando il SSN e orientandosi al benessere complessivo della persona, con centralità del socio e partecipazione democratica (assenza di scopo di lucro, porta aperta, responsabilità sociale) . La cornice pubblico–privato sociale è rafforzata dagli strumenti di co-programmazione e co-progettazione (art. 55 CTS) che la Corte Costituzionale ha riconosciuto come legittimi partenariati volti a elevare coesione e protezione sociale, oltre il mero scambio economico . In tale ecosistema, le cooperative agro-forestali richiedono telemetrie IoT capillari (acqua/suolo, antincendio, tracciabilità), le cooperative energia/servizi necessitano connettività affidabile per micro-reti e servizi essenziali, mentre cultura/turismo domandano coperture temporanee per eventi e fruizione digitale.

Il fabbisogno trasversale può essere formalizzato in tre requisiti di sistema:

1.  **Connettività capillare, on-demand ed emergenziale**: accesso diretto per utenze diffuse (cittadini, operatori, sensori) senza opere civili invasive, con disponibilità elevata e tempi di attivazione/riattivazione rapidi.

2.  **Osservazione geospaziale persistente a bassa latenza**: dati ad alta risoluzione e refresh continuo per prevenzione e decisione (incendi, dissesto, traffico, asset critici), con targeting mirato e retasking operativo.

3.  **Data-commons territoriale**: piattaforma condivisa per dati di comunità (standard aperti, API interoperabili), con **privacy-by-design** e **cybersecurity** end-to-end, a supporto di servizi replicabili delle cooperative.

Quanto sopra menzionato abilita nuovi modelli cooperativi (“connectivity & data-as-a-service”), rafforza il welfare territoriale mutualistico e rende effettiva l’integrazione socio-sanitaria orientata alla prevenzione e alla domiciliarità, nel solco del ruolo storico e attuale delle società di mutuo soccorso nell’economia sociale .

# **3. Motivazioni strategiche dell’intervento**

Le sole reti terrestri (torri, dorsali) risultano antieconomiche e lente in contesti impervi con domanda variabile: CAPEX elevati per sito, iter autorizzativi lunghi, vulnerabilità a eventi meteo-idrogeologici e difficoltà di ripristino post-evento. Le sole soluzioni satellitari, pur preziose per copertura ampia, presentano limiti di latenza, tempi di rivisita e spesso richiedono terminali dedicati, poco adatti a missioni time-critical e a integrazione diretta con l’ecosistema 4G/5G/IoT territoriale. È quindi necessario uno strato intermedio capace di proiettare copertura e capacità dall’alto, senza infrastrutture fisse a suolo, con ampio footprint, bassa latenza e persistenza.

H.A.L.E. risponde a questa esigenza come infrastruttura “above-the-clouds”: un velivolo stratosferico solare, a lunga autonomia e design modulare, operante ~20 km sopra il livello del mare, che agisce da “satellite pseudo-geostazionario” regionale. L’avvicinamento geometrico alla domanda (20 km vs centinaia/decine di migliaia) migliora il link budget, riduce la latenza a pochi millisecondi e consente riconfigurazione in tempo reale: si staziona su un’area critica, si espande o concentra la copertura, si riposiziona rapidamente su nuovi hotspot. In telecomunicazioni, payload HAPS multi-beam possono erogare celle 4G/5G direttamente ai terminali esistenti e servizi IoT massivi, oltre a costituire dorsali aeree HAPS-to-HAPS (RF/ottico) per instradare traffico senza dipendere da backhaul a terra. In osservazione, sensori ottici/IR (e, a maturità, SAR/LiDAR) forniscono alta risoluzione e refresh continuo, abilitando rilevazione precoce incendi, mappatura danni alluvionali, monitoraggio asset e mobilità, con edge-AI a bordo per allarmi e prodotti informativi a banda ridotta.

Dal punto di vista sistemico, H.A.L.E. integra tre proprietà difficilmente co-presenti in alternative singole: (i) rapidità di attivazione senza opere civili; (ii) continuità operativa con energia solare e gestione intelligente del ciclo giorno/notte; (iii) interoperabilità NTN-ready con reti esistenti (handover verticale, interfacce standard, sicurezza by-design). Ciò abilita: connettività on-demand in emergenza, ridondanza comunicativa per la resilienza del sistema-Paese, e situational awareness persistente a supporto di decisioni pubbliche e cooperative.

L’intervento risulterebbe dunque strategico perché colmerebbe il “vuoto di quota” tra suolo e spazio con un’infrastruttura **scalabile, riconfigurabile e a basse emissioni in esercizio**, capace di trasformare fabbisogni critici delle aree interne—connettività, osservazione, dati condivisi—in servizi affidabili e replicabili, coerenti con l’azione integrativa delle reti cooperativo-mutualistiche nei territori

# **4. Soluzione proposta: architettura e principio di funzionamento di H.A.L.E.**

H.A.L.E. (*High Altitude Long Endurance*) è un velivolo stratosferico a lunga permanenza progettato per operare stabilmente a 18–22 km di quota (al di sopra del traffico commerciale), erogando servizi di osservazione della Terra e di telecomunicazione con continuità temporale e ampia estensione spaziale. La piattaforma realizza, in termini funzionali, un “satellite locale”: mantiene la persistenza tipica degli asset spaziali con tempi di risposta e riconfigurabilità propri dei sistemi aeronautici. Tale carattere ibrido consente di colmare le lacune delle sole infrastrutture terrestri (scarsamente economiche o lente da implementare in aree impervie) e delle sole costellazioni satellitari (tempi di rivisita e latenze non ottimali per usi mission-critical).

## **Piattaforma aerea ed economia dell’energia**

Il velivolo è un ala-fissa ad alto allungamento, ultraleggero, con celle fotovoltaiche integrate sulle superfici superiori e batterie a bordo per il volo notturno. La gestione energetica è affidata a un autopilota che ottimizza i profili di missione mediante:

- ciclo diurno/notturno (salita con surplus solare; planata controllata in notturna, sfruttando l’energia potenziale accumulata);

- ottimizzazione altitudinale rispetto ai campi di vento, selezionando gli strati con migliore compromesso tra deriva e consumo;

- ridondanza dei sottosistemi critici (comandi, sensori, alimentazione) per garantire continuità operativa multi-settimana/mese.

## **Carichi utili per l’osservazione (EO)**

Il modulo EO (*Earth Observation*) integra sensori elettro-ottici ad alta definizione, infrarossi/IR per termografia notturna, multispettrali/iperspettrali per analisi biofisiche (stato della vegetazione, umidità, inquinanti) e, ove richiesto, un radar ad apertura sintetica leggero per condizioni all-weather. L’elaborazione a bordo (cosiddetta edge-AI, ossia intelligenza artificiale eseguita sul velivolo) effettua rilevazioni automatiche di eventi rilevanti (es. principi d’incendio, frane, anomalie su opere civili), riducendo la banda necessaria e abilitando flussi quasi in tempo reale (*near-real-time*: secondi/minuti) verso gli operatori territoriali. Ne derivano capacità di prevenzione e situa­tional awareness coerenti con le esigenze delle aree interne, caratterizzate da morfologie complesse e vie di accesso fragili.

## **Carichi utili per le telecomunicazioni (HAPS)**

In configurazione HAPS (*High Altitude Platform Station*, stazione radio ad alta quota), H.A.L.E. opera come nodo di rete mobile 4G/5G (reti di quarta/quinta generazione) con copertura dal cielo su aree tipiche di 100–200 km di diametro. La formazione digitale dei fasci (beamforming) consente di concentrare l’energia radio sulle zone d’interesse, aumentando l’efficienza spettrale e mitigando interferenze. Il collegamento di dorsale (backhaul) verso la rete principale è realizzato tramite radiofrequenza (RF), onde millimetriche (mmWave) o link ottico in spazio libero (raggio laser), diretti a gateway a terra o ad altri H.A.L.E., costituendo una rete a maglia (mesh, rete in cui ogni nodo può instradare traffico per gli altri, senza punto singolo di guasto).  
Per i servizi IoT (*Internet of Things*, reti di oggetti/sensori connessi) la piattaforma supporta sia LPWAN (*Low-Power Wide-Area Network*, reti a bassa potenza e lunga portata, es. LoRaWAN/NB-IoT) sia profili 5G NR-RedCap (*New Radio Reduced Capability*, terminali 5G semplificati a basso costo/consumo). L’architettura è NTN-ready (*Non-Terrestrial Networks*, integrazione delle reti mobili con piattaforme non terrestri), permettendo a dispositivi esistenti di connettersi senza terminali dedicati: aspetto determinante in scenari di interruzione infrastrutturale o isolamento prolungato.

## Architettura di sistema e livello dati

Lo strato stratosferico (uno o più H.A.L.E. eventualmente interconnessi in mesh) eroga tre modalità operative: stazionamento prolungato su aree prioritarie, copertura su richiesta (on-demand) al variare dei fabbisogni, disaster recovery a seguito di eventi estremi. Il segmento di terra comprende gateway di comunicazione e un NOC (*Network Operations Center*, centro operativo) per controllo di volo, orchestrazione dei payload, sicurezza crittografica end-to-end e qualità del servizio.  
Il data layer si configura come data-lake (archivio scalabile) con governance data-commons (patrimonio informativo condiviso tra cooperative e PA), conformità GDPR (Reg. UE 2016/679), pseudonimizzazione/anonimizzazione, controlli di accesso e audit (tracciabilità degli accessi e degli usi). Interfacce API (*Application Programming Interface*) consentono l’integrazione con applicativi di teleassistenza, gestione eventi culturali, agricoltura di precisione, manutenzione di reti idriche ed energetiche.

## **Concetto d’operazione e coerenza con i fabbisogni delle aree interne**

In regime ordinario, la piattaforma colm a i vuoti di copertura laddove l’infrastruttura terrestre è assente o antieconomica, abilita servizi di cittadinanza digitale (telemedicina di prossimità, istruzione e sportelli remoti), supporta IoT rurale (monitoraggio suolo/acque, antincendio) e fornisce monitoraggio ambientale persistente con frequenze di aggiornamento dell’ordine dei minuti.  
In regime di emergenza, l’attivazione rapida abilita ponti radio/5G temporanei, canali sicuri per i moduli di soccorso(triage, teleconsulto, C2 – *Comando e Controllo*) e mappature danni quasi in tempo reale, riducendo i tempi di ripristino dei servizi essenziali e le giornate di isolamento.  
Per stagionalità ed eventi, sono previste coperture temporanee (cultura/turismo), campagne agro-forestali(prevenzione incendi, irrigazione di precisione) e manutenzione predittiva di infrastrutture, contribuendo alla resilienza socio-economica dei territori a bassa densità.

In conclusione, H.A.L.E. fornisce un’infrastruttura “above-the-clouds” a bassa latenza, persistente e modulare, tecnicamente integrabile con le reti esistenti e governata da principi privacy-by-design. Tale configurazione affronta in modo diretto le criticità strutturali delle aree interne—connettività capillare, osservazione ad alta risoluzione e data-commons territoriale—abilitando servizi cooperativi replicabili e sostenibili.

# **5. Obiettivi progettuali e approccio per il Piano di Fattibilità**

## **Finalità del piano**

Produrre, in forma rapida ma rigorosa, una decisione informata go/no-go sull’adozione della piattaforma H.A.L.E. nelle aree interne, dimostrando (i) coerenza con i fabbisogni delle dieci cooperative coinvolte, (ii) fattibilità tecnico-operativa preliminare, (iii) compatibilità regolatoria e di tutela dati, (iv) disegno di un pilota realistico per la fase successiva.

## Risultati attesi (selezionati e misurabili)

1.  **Quadro dei fabbisogni e degli scenari d’uso** delle 10 cooperative (sanità/prossimità, soccorso, agro-forestale, energia/servizi, cultura/turismo), con mappa dei punti a connettività carente e dei processi critici.

2.  **Studio tecnico preliminare**: mappe di copertura ipotizzate, stima di latenza e capacità di rete per i casi d’uso, profilo energetico di missione del velivolo, configurazioni di carico utile (osservazione/telecomunicazioni) pertinenti ai contesti cooperativi.

3.  **Pre-verifica regolatoria e di protezione dati**: checklist per operazioni nello spazio aereo superiore (Higher Airspace Operations), profili di salita/discesa, gestione dello spettro radio, telerilevamento, GDPR (Regolamento europeo sulla protezione dei dati), DPIA preliminare (Valutazione d’Impatto sulla Protezione dei Dati).

4.  Disegno del pilota: siti candidati, livelli minimi di servizio (SLA, Service Level Agreement), metriche di prova, piano permessi/stakeholder e schema di monitoraggio con KPI (Indicatori Chiave di Prestazione).

## Articolazione operativa (sette passi sequenziali ma leggeri)

**1. Inquadramento e raccolta dati di base.  
**Consolidamento delle specifiche iniziali del velivolo (quota operativa, endurance, configurazioni di carico utile), raccolta di dati territoriali open (orografia, uso del suolo, reti esistenti) in un GIS (Sistema Informativo Geografico) unificato. Output: *dossier di contesto* e *catalogo dati*.

**2. Co-design con le cooperative (interviste rapide e mapping).  
**Sessioni semi-strutturate (una per cooperativa) per elicitare requisiti, livelli minimi di servizio e priorità; georeferenziazione dei “black-spot” di rete e dei siti sensibili (presidi sanitari di comunità, aree a rischio incendio/frana, infrastrutture essenziali, spazi culturali aperti). Output: *specifica dei requisiti utente* e *geodatabase dei bisogni*.

**3. Copertura, capacità e latenza: modellazione rapida.  
**Calcoli parametrici di **link-budget** (bilancio di potenza radio) alla quota H.A.L.E. ipotizzando: celle mobili 4G/5G (quinta generazione) con beam-forming (puntamento elettronico del segnale), servizi IoT (Internet degli Oggetti) a bassa potenza per sensori diffusi, e dorsali di ritorno verso terra (radio direzionale o ottico). Generazione di mappe di copertura e stime di latenza end-to-end per ciascuno scenario cooperativo. Output: *atlante di copertura* e *schede prestazionali per caso d’uso*.

**4. Profilo energetico e vincoli di missione.  
**Bilancio energia/potenza del velivolo: raccolta solare, consumo propulsivo ed elettronico, strategie di gestione energetica (salita diurna, planata notturna, scelta dell’altitudine in funzione dei venti), margini in condizioni invernali o meteo avverso. Output: *curva di fattibilità energetica* e *finestre operative consigliate*.

**5. Architettura tecnica e sicurezza/privacy-by-design.  
**Definizione dello schema complessivo: segmento stratosferico (H.A.L.E. singolo o in rete), segmento di terra (gateway e centro di controllo), strato dati (data-lake/commons). Disegno dei flussi informativi, cifratura end-to-end, gestione identità e ruoli, minimizzazione e pseudonimizzazione dei dati personali, auditing. Redazione della DPIA preliminare. Output: *architettura logica e di sicurezza* con *matrice delle interfacce*.

**6. Verifica regolatoria “desk” e gestione dello spettro.  
**Allineamento preliminare ai requisiti per operazioni ad alta quota; ipotesi di corridoi di salita/discesa in aree poco trafficate; ricognizione delle bande radio utilizzabili e delle regole di coesistenza con reti a terra; linee guida sul telerilevamento (risoluzioni, autorizzazioni). Output: *nota regolatoria* e *checklist permessi*.

**7. Impatto atteso e disegno del pilota.  
**Costruzione della Teoria del Cambiamento (catena input-attività-output-outcome-impatti) e definizione di KPI: disponibilità di rete (uptime), tempo di ripristino in emergenza, latenza mediana, capacità per utente, accuratezza e frequenza dei dati di osservazione, giorni di isolamento evitati, adozione dei servizi, indicatori ambientali in esercizio. Selezione di 2–3 siti candidati per il pilota, schema prove e livelli di servizio minimi (**SLA**), registro rischi con misure di mitigazione. Output: *dossier pilota* e *piano di monitoraggio e valutazione*.

## **Metodologia e strumenti**

La conduzione privilegia strumenti pre-configurati (modelli di propagazione standard, fogli di calcolo tracciati, librerie GIS), template di qualità e checklist regolatorie; ciò consente di ottenere evidenze solide in tempi contenuti, mantenendo trasparenza delle assunzioni e replicabilità dei risultati.

## **Deliverable sintetici**

- Specifica dei requisiti e geodatabase dei bisogni.

- Atlante di copertura e schede prestazionali per caso d’uso.

- Curva di fattibilità energetica e finestre operative.

- Architettura logica, sicurezza e DPIA preliminare.

- Nota regolatoria e checklist permessi.

- Dossier pilota con KPI/SLA e piano di monitoraggio.

- Rapporto finale del Piano di Fattibilità con raccomandazione motivata go/no-go.

# **Conclusione e motivazione al finanziamento**

Il Piano di Fattibilità proposto produrrà, in forma integrata e verificabile, gli esiti seguenti: (i) co-progettazione dei requisiti con le dieci cooperative e formalizzazione del *Concept of Operations*—Concetto Operativo—e dell’architettura sistema/terra; (ii) analisi regolatoria preliminare comprensiva di SORA (*Specific Operations Risk Assessment*, Valutazione del Rischio per Operazioni Specifiche), gestione dello spettro radio, e DPIA-GDPR (*Data Protection Impact Assessment*, Valutazione d’Impatto sulla Protezione dei Dati, ai sensi del Regolamento europeo); (iii) modello di servizio cooperativo e business case/TCO (*Total Cost of Ownership*, costo totale di possesso) a scala di vallata; (iv) selezione dell’area pilota, con piano di test ed esercitazioni; (v) cronoprogramma (diagramma di Gantt) e quadro economico della successiva fase prototipale. Tali risultati saranno consegnati come dossier tecnici, mappe di copertura, schemi architetturali, checklist autorizzative e metriche di valutazione pronte per l’uso operativo.

Il finanziamento del Piano di Fattibilità è strategico perché abbatte i principali rischi di progetto—tecnologici (prestazioni, integrazione di carichi utili), autorizzativi (operazioni in quota, spettro, telerilevamento), operativi(processi dei moduli di soccorso e dei servizi di prossimità) e di conformità (privacy e sicurezza)—e allinea H.A.L.E. ai fabbisogni effettivi delle aree interne. L’esito sarà una base solida, misurabile e immediatamente attuabile per avviare il prototipo e il pilota territoriale: un’infrastruttura cooperativa, a zero emissioni in esercizio, scalabile e replicabile, capace di generare impatti tangibili per tutte le cooperative coinvolte (continuità operativa, riduzione dei giorni di isolamento, nuovi servizi digitali e data-commons condiviso). In tal modo, il Piano di Fattibilità trasforma una soluzione tecnologica avanzata in una capacità territoriale concreta, pronta a entrare in esercizio nella fase successiva con rischi ridotti e valore pubblico massimizzato.
