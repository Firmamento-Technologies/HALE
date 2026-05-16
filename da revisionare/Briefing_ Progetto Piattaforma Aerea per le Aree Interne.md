### Briefing: Progetto Piattaforma Aerea per le Aree Interne

#### Executive Summary

Il presente documento analizza il Piano di Fattibilità per una piattaforma aerea senza pilota, sviluppato da **Firmamento Technologies** nell'ambito del bando **Cooding Prototypes** . L'obiettivo primario del progetto è valutare la fattibilità tecnica, operativa e regolatoria di un'infrastruttura aerea per erogare servizi a elevato valore pubblico (monitoraggio ambientale, prevenzione dei rischi, connettività) nelle Aree Interne italiane, con un focus specifico sulla Liguria e un caso studio pilota identificato nel comune di **Pentema** . Il progetto si avvale della collaborazione di una rete di dieci cooperative aderenti a Legacoop, che agiscono come "utenti-pilota" per la definizione dei fabbisogni.La visione strategica a lungo termine è centrata su una piattaforma **H.A.L.E. (High Altitude Long Endurance)** : un velivolo solare stratosferico operante a circa 20 km di quota, concepito come un'infrastruttura "pseudo-satellitare" persistente. Tuttavia, dati gli elevati rischi tecnologici, regolatori e finanziari associati, il Piano di Fattibilità raccomanda un approccio incrementale e duale per la riduzione del rischio:

1.  **Percorso 6A (Operatività Immediata - 0–12 mesi):** Un progetto pilota basato su una piattaforma **VTOL (Vertical Take-Off and Landing) ibrida** di tipo commerciale (es. JOUAV). Questo percorso, a basso rischio e con un budget stimato di **€600k–900k** , è ritenuto **tecnicamente fattibile (Go Condizionato)** . Il suo scopo è validare sul campo la fattibilità operativa, generare dati reali, consolidare la collaborazione con le cooperative e la Protezione Civile, e affrontare le prime sfide regolatorie con ENAC e AGCOM.

2.  **Percorso 6B (Visione Strategica - 24–48 mesi e oltre):** L'evoluzione verso la piattaforma **HALE stratosferica** . Questo percorso è attualmente classificato come ad alto rischio **(Hold / Go Condizionato Estremo)** a causa di showstopper critici non risolti, tra cui la gestione dell'energia in condizioni invernali, la stabilità aeroelastica, l'assenza di un quadro normativo definito per gli HAPS (High Altitude Platform Systems) e l'incertezza sui finanziamenti su larga scala. La raccomandazione è di posticipare un impegno su questo fronte, utilizzando le evidenze e gli asset del percorso VTOL per ridurre progressivamente le incertezze.L'intera metodologia si basa sul NASA Systems Engineering Handbook, adottando un approccio "gate-driven" e "risk-informed", dove il superamento di specifici gate decisionali, basati su evidenze verificabili, determina l'avanzamento del progetto e il rilascio dei finanziamenti.

#### 1. Inquadramento del Progetto e Contesto Strategico

##### 1.1 Contesto e Soggetti Coinvolti

L'obiettivo è analizzare la fattibilità di una piattaforma aerea senza pilota per fornire servizi avanzati alle Aree Interne. Il piano non prevede la costruzione di un velivolo in questa fase, ma si concentra su analisi, modellazione, simulazione e co-progettazione.Un elemento centrale è la rete di dieci cooperative, con **Fabrica** come capofila, che agiscono come utenti pilota per definire i requisiti operativi.

| **Soggetto**                | **Ruolo**                                                                |
|-----------------------------|--------------------------------------------------------------------------|
| **Firmamento Technologies** | Soggetto proponente, responsabile dello Studio di Fattibilità            |
| **Rete di Cooperative**     | Utenti-pilota, fonte primaria per i fabbisogni di servizio               |
| **Regione Liguria**         | Stakeholder istituzionale, capofila decisionale e potenziale sito pilota |
| **ENAC / AGCOM**            | Enti regolatori per lo spazio aereo e lo spettro radio                   |

##### 1.2 Motivazione: Aree Interne e Razionale Pubblico

Il progetto si allinea pienamente con la **Strategia Nazionale per le Aree Interne (SNAI)** e il successivo **Piano Strategico Nazionale (PSNAI)** , che mirano a contrastare le criticità strutturali di territori a bassa densità demografica e con orografia complessa. Gli obiettivi sono duplici: migliorare i servizi essenziali (salute, istruzione, mobilità) e promuovere progetti di sviluppo locale.La **Liguria** è identificata come un "laboratorio avanzato" per le Aree Interne, con 8 aree riconosciute nelle programmazioni 2014-2020 e 2021-2027. **Regione Liguria** ha manifestato interesse per una sperimentazione, individuando la frazione di **Pentema** come caso studio rappresentativo.

##### 1.3 Visione Tecnologica: Il Concetto H.A.L.E.

La visione a lungo termine del progetto si basa su una piattaforma **H.A.L.E. (High Altitude Long Endurance)** .

- **Tipologia:** Velivolo solare stratosferico ad ala fissa.

- **Quota Operativa:** Circa 20 km, al di sopra del traffico aereo commerciale.

- **Autonomia:** Prolungata (settimane o mesi).

- **Carico Utile (Payload):** Modulare, per sensori di osservazione e apparati di telecomunicazioni.

- **Funzione:** Infrastruttura "pseudo-satellitare" a bassa latenza, ideale per colmare il **"vuoto di quota"** tra le infrastrutture terrestri (spesso inadeguate in aree montane) e quelle satellitari (con limiti di latenza, costi e tempi di rivisita).Tuttavia, l'ambizione H.A.L.E. comporta investimenti elevati e rischi tecnologico-regolatori significativi, rendendo indispensabile un approccio incrementale.

#### 2. Approccio Strategico a Due Percorsi

Per gestire la complessità e ridurre il rischio, il Piano di Fattibilità definisce una strategia duale, separando l'operatività a breve termine dalla visione a lungo termine.

| **Percorso**    | **Titolo**         | **Orizzonte Temporale** | **Tecnologia**                              | **Rischio** | **Budget Stimato**     | **Obiettivo Primario**                                                                                               |
|-----------------|--------------------|-------------------------|---------------------------------------------|-------------|------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Percorso 6A** | Pilota VTOL        | 0–12 mesi               | Piattaforma commerciale TRL 8-9 (es. JOUAV) | Basso       | €600k – 900k           | Validare fattibilità operativa, raccogliere dati, generare evidenze regolatorie.                                     |
| **Percorso 6B** | HALE Stratosferico | 24–48+ mesi (Opzionale) | R&D su velivolo solare HALE, TRL basso      | Alto        | €5.5M – 11M (Fase R&D) | Chiudere gap tecnologici critici (energia, aeroelasticità, avionica), definire il percorso regolatorio per gli HAPS. |

Questa separazione offre **flessibilità strategica** : il progetto può stabilizzarsi su un modello operativo basato su VTOL e MALE (Medium Altitude Long Endurance) se il percorso HALE non dovesse materializzarsi, riutilizzando comunque gli asset sviluppati (infrastruttura di terra, data governance, competenze).

#### 3. Percorso 6A: Pilota VTOL (Fase 1, 0-12 Mesi)

##### 3.1 Verdetto e Architettura

**Verdetto:** **GO CONDIZIONATO** L'architettura VTOL ibrida (A3) è ritenuta tecnicamente fattibile per una fase pilota. Utilizza una piattaforma commerciale matura (TRL 8-9) come la **JOUAV CW-30E** , capace di un'autonomia di 6-10 ore, copertura locale di 30-50 km e payload modulare.

##### 3.2 Valutazione di Fattibilità Tecnica

La valutazione tecnica evidenzia una fattibilità generale, con alcune aree che richiedono attenzione.

| **Area Tecnica**            | **Valutazione** | **Note e Driver Principali**                                                                                                            |
|-----------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Energia/Autonomia**       | 🟢 Verde        | L'autonomia ibrida di 6-10 ore è adeguata per missioni tattiche e non presenta criticità invernali insormontabili.                      |
| **Comunicazioni**           | 🟢 Verde        | La latenza del link (\<100 ms) è sufficiente per il controllo e la telemetria; il video in tempo reale non è un requisito di fase.      |
| **Copertura**               | 🟡 Giallo-Verde | Copertura locale (30-50 km), limitata dall'orografia ligure. Adeguata per il pilota ma non per l'intera area SNAI.                      |
| **Payload & Modularità**    | 🟡 Giallo       | La piattaforma supporta il peso richiesto (10-25 kg), ma l'integrazione richiede la definizione di un Interface Control Document (ICD). |
| **Ground Segment (GCS)**    | 🟡 Giallo       | Richiede l'allocazione di un sito a Pentema con alimentazione e connettività internet adeguate (\>10 Mbps).                             |
| **Data/IT & Cybersecurity** | 🟡 Giallo       | La versione base del drone non ha telemetria criptata. È richiesto un upgrade per la conformità GDPR e la sicurezza.                    |

#### 4. Percorso 6B: Sviluppo H.A.L.E. (Fase 3, 24-48 Mesi)

##### 4.1 Verdetto e Sfide

**Verdetto:** **HOLD / GO CONDIZIONATO ESTREMO** La fattibilità tecnica e regolatoria del percorso HALE **non è attualmente dimostrata** . L'avvio di questa fase è subordinato alla risoluzione di showstopper critici e richiede un investimento significativo solo per la fase di R&D (Fase 3), stimato in **€0.7M–1.6M** , che precede la costruzione vera e propria del velivolo (Fase 4, stimata in €5-15M).

##### 4.2 Showstopper Tecnici e Regolatori

La valutazione preliminare ha identificato diverse criticità di livello "Rosso".

| **Dimensione**              | **Valutazione**  | **Motivazione Sintetica**                                                                                                                                             |
|-----------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fattibilità Tecnica**     | 🔴 Rosso-Ambra   | **Energia invernale non validata (rischio showstopper)**, margini di flutter per ali ad alto allungamento incerti, assenza di un autopilota COTS per lunga autonomia. |
| **Fattibilità Regolatoria** | 🔴 Rosso         | Il quadro normativo EASA/ENAC per gli HAPS è inesistente o non finalizzato. L'allocazione dello spettro radio richiede negoziati internazionali (ITU).                |
| **Sostenibilità Economica** | 🔴 Rosso-Critico | I costi di sviluppo (CAPEX) non sono finanziati e la loro entità richiede un impegno strategico a livello nazionale/europeo.                                          |
| **Maturità Tecnologica**    | 🔴 Rosso         | Il TRL di partenza per i sottosistemi critici è basso (3-4). Il piano si basa su 8 assunzioni critiche con un livello di confidenza medio-basso.                      |

#### 5. Stato di Avanzamento e Risultati della Fase 1 dello Studio

La rendicontazione delle attività svolte tra aprile e dicembre 2025 (Fase 1 dello Studio di Fattibilità) conferma che il lavoro si è concentrato su analisi, modellazione e pianificazione.

**Risultati Intermedi Ottenuti:**

- **Impianto Metodologico:** Struttura del Piano di Fattibilità, definizione di requisiti e criteri di successo.

- **Analisi di Contesto:** Ricostruzione del quadro SNAI/PSNAI e del ruolo delle cooperative in Liguria.

- **Quadro Regolatorio:** Chiara distinzione dei percorsi normativi per VTOL e HALE.

- **Roadmap Strategica:** Definizione del percorso duale (6A/6B) come traiettoria per le fasi successive.È fondamentale sottolineare che questa fase **non ha incluso alcuna sperimentazione fisica, prototipazione o decisione Go/No-Go definitiva** . Tali elementi sono oggetto delle fasi successive del progetto.
