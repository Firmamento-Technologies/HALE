# Capitolo 1 — Inquadramento del Progetto e Obiettivi (Quadro Esigenziale ex art. 41 D.Lgs. 36/2023)

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 1
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Stato:** capitolo redatto con fonti normative e di programmazione aggiornate al maggio 2026 (PSNAI 30 luglio 2025; D.Lgs. 36/2023 + Allegato I.7; ENAC Piano AAM 2021-2030)
> **Conformità formale:** art. 41 D.Lgs. 36/2023 + Allegato I.7, Sezione I — Quadro Esigenziale (QE)
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor` (falsifiability, triangulation, source provenance, confidence levels, pre-mortem, steel-manning, base-rate)
> **Red Team review:** stress-test condotto da `red-team-skeptic` con prospettiva Coopfond + Regione Liguria + Commissione UE — vedi §1.10

---

## 1.0 Sintesi del capitolo

Il presente capitolo è l'**Inquadramento di Progetto** dello Studio di Fattibilità per una piattaforma aerea senza pilota dedicata ai servizi pubblici e cooperativi delle **Aree Interne italiane**, con focus sulla Regione Liguria e caso pilota nella frazione di **Pentema (Comune di Torriglia, GE)**. Il capitolo svolge contemporaneamente la funzione di **Quadro Esigenziale (QE) ex art. 41 D.Lgs. 36/2023 e Allegato I.7 Sezione I**: dichiara gli obiettivi generali dell'intervento, i fabbisogni quantitativi e qualitativi che lo Studio deve soddisfare e l'orizzonte temporale di attuazione[^1].

In sintesi:

- **Soggetto proponente**: Firmamento Technologies, PMI italiana early-stage, in qualità di **operatore di servizi**, non di OEM aeronautico. La piattaforma non viene venduta, ma utilizzata per erogare servizi ricorrenti.
- **Bando di riferimento**: Cooding Prototypes (Coopfond / Legacoop), strumento di finanziamento dello Studio di Fattibilità tecnico-economico-regolatorio[^2][^3].
- **Rete cooperative pilota**: 10 cooperative aderenti a Legacoop, con **Fabrica** come capofila, prevalentemente cooperative di comunità delle Aree Interne[^2].
- **Stakeholder istituzionali**: Regione Liguria (anchor istituzionale), Comune di Torriglia (sito pilota), ENAC (autorità UAS), AGCOM (spettro radio), Protezione Civile Liguria + ARPA Liguria (cliente operativo primario).
- **Razionale pubblico**: contrasto allo spopolamento, al digital divide e all'isolamento informativo delle Aree Interne, in coerenza con la **Strategia Nazionale Aree Interne (SNAI)** 2021-2027 e con il **Piano Strategico Nazionale Aree Interne (PSNAI)** approvato dal Ministro per la Coesione il 30 luglio 2025[^4].
- **Visione tecnologica di lungo termine**: piattaforma **H.A.L.E. (High Altitude Long Endurance)** solare, capace di operare in stratosfera (~20 km AGL) per settimane/mesi continuativi, posizionata come **layer stratosferico complementare** all'infrastruttura sovrana europea multi-orbita (Galileo, Copernicus, IRIS²).
- **Strategia duale risk-informed**: Percorso **6A** (pilota VTOL commerciale TRL 8-9, 0-12 mesi, €600k-900k, rischio Basso) come deliverable operativo; Percorso **6B** (R&D HALE stratosferico, 24-48+ mesi, €5.5-11M, rischio Alto) come orizzonte preparatorio.
- **Orizzonte dello Studio**: M+0 → M+11, gate decisionale M+10/M+11 con verdetto **Go Condizionato** per 6A e **Hold / Go Condizionato Estremo** per 6B.

Il capitolo non duplica i contenuti già coperti: i requisiti dettagliati sono nel Cap. 3 (Requisiti e RTM); il quadro normativo è nel Cap. 5; il business case è nel Cap. 7. Qui si dichiara **a cosa serve l'intervento, perché è necessario, chi sono i destinatari e quale forma di attuazione si propone**, in conformità all'art. 1 dell'Allegato I.7 del Codice dei Contratti[^1].

---

## 1.0bis Boundary conditions del progetto

Il presente capitolo, e l'intero Studio di Fattibilità, presuppone — come **scelte strategiche-politiche** del fondatore di Firmamento Technologies, non come ipotesi soggette a falsificazione epistemica — due posizioni di progetto vincolanti:

- **B1 — Modello cooperativo e service-only**. Firmamento Technologies opera con un modello cooperativo, in partnership stabile con cooperative Legacoop (rete utenti-pilota, capofila Fabrica), e si configura come **operatore di servizi** (analogo al modello Starlink come operatore broadband, non OEM satellitare puro). La piattaforma HALE/VTOL **non viene venduta**: è asset di Firmamento e viene utilizzata per erogare **servizi ricorrenti** (monitoraggio EO, connettività NTN, alert events, capacity wholesale) a cooperative e PA. Tutte le considerazioni di governance, business model, struttura finanziaria e architettura tecnica del presente Studio riflettono questa scelta strutturale. Non sono validate ipotesi alternative (es. vendita diretta UAV a clienti terzi).

- **B2 — Vettore strategico "EU sovereign stratospheric layer"**. L'obiettivo strategico di lungo termine (10 anni, vedi `riferimenti/visione-10-anni.md`) è costituire un **nodo italiano fondatore di una futura infrastruttura sovrana europea HAPS**, complementare a IRIS² (LEO sovrano EU) e a Galileo/Copernicus, posizionata come **risposta europea strategica al modello di servizio Starlink sul layer stratosferico**. Nel linguaggio pubblico (bandi, stampa, investitori non sotto NDA) il posizionamento è **"complementare a IRIS²"**, mai "alternativa a Starlink" (vedi `riferimenti/RESERVED-rischi-geopolitici.md` per le ragioni geopolitiche). Lo Studio di Fattibilità approva esclusivamente i passi intermedi Y1-Y3 (Percorso 6A pilota + Percorso 6B preparatorio R&D); l'orizzonte completo è descritto nel documento di visione e non è in scope di gate M+10.

Le boundary conditions B1 e B2 non sono soggette a stress-test epistemico nel presente capitolo: il rigore si applica a **come** le si supporta e **come** ci si arriva, non al **se** sono gli obiettivi giusti. Le sezioni che seguono, e in particolare la sezione "Visione tecnologica" (§1.3) e "Strategia duale" (§1.5.2), sono coerenti con queste boundary conditions.

---

## 1.1 Contesto e bando di riferimento

### 1.1.1 Soggetto proponente: Firmamento Technologies

Firmamento Technologies è una **PMI italiana early-stage** che si propone come **operatore di servizi pseudo-satellitari** sulla classe stratosferica, con focus sulla erogazione di servizi a elevato valore pubblico nelle Aree Interne. La società non si configura come **manifatturiero aeronautico (OEM)**: il modello di business inderogabile (boundary condition B1) prevede che la piattaforma sia asset operativo di Firmamento e che il valore sia generato dall'**erogazione ricorrente di servizi** alle cooperative, alla PA e a clienti terzi (B2G/B2B).

Stato attuale dell'organizzazione (M+3 maggio 2026):

| Dimensione | Stato |
|---|---|
| Stadio | Early-stage / pre-seed |
| Esperienza R&D interna | Concept HALE solare sviluppato (`Progetto concettuale struttura HALE.md`) |
| Capital structure | Da consolidare; round seed in preparazione |
| Track-record industriale | Nessuna piattaforma in volo operativo, nessun servizio ricorrente in essere |
| Partnership | 10 cooperative Legacoop + interesse Regione Liguria su Pentema |

> **Caveat epistemico**: il presente Studio non assume come acquisito alcun risultato industriale di Firmamento. Tutte le metriche di output del Percorso 6A sono dichiarate come **obiettivi target sottoposti a gate review**, non come capacità già dimostrate. La base rate aerospace early-stage è esplicitamente riconosciuta nella sezione `riferimenti/visione-10-anni.md` §0. *Confidence: high* sulla descrizione dello stato attuale (fonte: dichiarazioni dirette del proponente).

### 1.1.2 Rete cooperative pilota (10 cooperative Legacoop, capofila Fabrica)

Il progetto si fonda strutturalmente su una **rete di dieci cooperative aderenti a Legacoop**, prevalentemente **cooperative di comunità**, che assumono il duplice ruolo di:

1. **Co-progettisti** dei requisiti operativi del sistema (workshop di co-design M+0 → M+6, vedi Cap. 3 §3.3.2 per la lista StNeeds derivanti);
2. **Utenti-pilota** della Fase 1 (M+12-24) per la validazione operativa dei servizi.

Il capofila della rete è **Fabrica**, cooperativa di comunità con presenza territoriale consolidata e funzione di aggregatore degli interessi della rete[^2]. Le 10 cooperative coprono cinque cluster funzionali identificati nel Briefing di progetto[^3]:

| Cluster | Tipologia | Fabbisogno-tipo |
|---|---|---|
| Sanità di prossimità | Cooperative sociali, mutue | Telemedicina, teleassistenza, continuità sanitaria |
| Soccorso mutualistico | Cooperative emergenza, Protezione Civile-affiliate | Ponte radio multi-standard, C2 backup, mappatura danni |
| Agro-forestale | Cooperative agricole, forestali | IoT capillare (acqua, suolo, antincendio), tracciabilità |
| Energia / servizi | Cooperative energetiche, comunità energetiche | Connettività affidabile per micro-reti, monitoring |
| Cultura / turismo | Cooperative culturali, turistiche | Copertura temporanea eventi, fruizione digitale |

> **Caveat epistemico**: l'identità nominale delle 10 cooperative è dato sensibile commerciale (in formalizzazione tramite NDA) e non è qui riportata. Le letters of intent (LoI) sono in raccolta — completamento previsto M+4. *Confidence stato attuale: medium* (rete identificata, formalizzazione in corso).

### 1.1.3 Stakeholder istituzionali

Il progetto si appoggia a una **costellazione di stakeholder istituzionali**, le cui posizioni sono dettagliate nel Cap. 2 §2 e nella stakeholder map del Cap. 3 §3.3.1:

| ID stakeholder | Soggetto | Ruolo nel progetto |
|---|---|---|
| **S-04** | **Regione Liguria** | Sponsor istituzionale, anchor customer, sito pilota (Pentema) |
| **S-05** | **Comune di Torriglia (Pentema)** | Autorizzazioni locali, accettabilità comunità |
| **S-06** | **Protezione Civile Liguria + ARPA Liguria** | Cliente operativo primario (frane, antincendio) |
| **S-08** | **ENAC** | Autorità nazionale UAS — autorizzazione SORA + certificazione |
| **S-10** | **AGCOM** | Autorità nazionale telecomunicazioni — spettro radio |
| **S-13** | **MIMIT** (Aerospazio + Comunicazioni) | Indirizzo strategico, PNRF, finanziamenti PNRR |
| **S-11** | **Garante Privacy** | Vigilanza GDPR su trattamento dati EO |
| **S-16** | **Coopfond + Fondazione PICO ETS** | Finanziatore Studio di Fattibilità (Cooding Prototypes) |

L'engagement plan dettagliato è nel Cap. 5 §5.11. Lo Studio è strutturato per **non richiedere committment vincolanti** prima del gate M+10: tutti gli stakeholder sono in fase di interlocuzione preliminare.

---

## 1.2 Motivazione: Aree Interne italiane e razionale pubblico

### 1.2.1 La Strategia Nazionale Aree Interne (SNAI) 2021-2027 e PSNAI 2025

Il razionale pubblico del progetto è ancorato alla **Strategia Nazionale Aree Interne (SNAI)** e al successivo **Piano Strategico Nazionale Aree Interne (PSNAI)**, approvato dal Ministro per gli Affari Europei, il Sud, le Politiche di Coesione e il PNRR in data 30 luglio 2025[^4]. Il PSNAI riconosce come priorità nazionale il contrasto a una **triade di criticità strutturali** che affligge i territori a bassa densità demografica e con orografia complessa[^4, premessa]:

> *"Le Aree Interne si trovano ad affrontare criticità più accentuate, in quanto sono maggiormente esposte a fenomeni come il forte spopolamento, l'invecchiamento della popolazione e la carenza di servizi. [...] Per affrontare queste problematiche, è fondamentale adottare interventi mirati e strategie integrate."* [^4]

Il PSNAI individua **quattro leve strategiche di intervento**[^4, premessa]:

1. **Investimento in servizi pubblici essenziali** (sanità, istruzione, mobilità), incluse soluzioni di **telemedicina e e-learning** per aumentarne efficienza e accessibilità;
2. **Colmamento del divario digitale**, con investimenti in **infrastrutture di rete ad alta velocità e 5G** nelle aree periferiche;
3. **Sostegno alle economie locali**, garanzia del "**diritto di restare**", incentivazione dell'imprenditorialità;
4. **Sviluppo sostenibile**, con energie rinnovabili e trasporti sostenibili.

Il PSNAI sottolinea inoltre il ruolo del **terzo settore** e delle **cooperative** come attori centrali per la "creazione di ecosistemi economici resilienti" e per garantire la "diffusione e la sostenibilità degli interventi"[^4, cap. 6]. Cita esplicitamente, tra gli strumenti attuativi, la **co-programmazione e co-progettazione (art. 55 Codice del Terzo Settore — CTS)** come modalità preferenziale di partenariato pubblico-privato-sociale per il rafforzamento della coesione[^4].

🎯 **Allineamento del progetto al PSNAI**: il Piano di Fattibilità HALE/VTOL si pone come **intervento abilitante delle leve 1 e 2 del PSNAI** (servizi essenziali resilienti + divario digitale), attraverso un'infrastruttura cooperativa che integra terzo settore, PA e operatore privato.

> **Source provenance** [^4]: `fonti/psnai_finale_30072025_clean_ministro.md` (6.415 righe, Premessa + 7 capitoli + 11 allegati). **Confidence: high** (documento programmatico nazionale firmato dal Ministro, in vigore).

> **Falsifying observation**: se nel ciclo di programmazione 2028-2034 (post-PSNAI corrente) la SNAI fosse de-prioritizzata o assorbita in altre strategie territoriali, il razionale pubblico del progetto richiederebbe re-framing (es. inquadramento in PNRR Aerospazio + FESR + EU Cohesion Policy). **Probabilità: L** (la SNAI è strumento consolidato dal 2014, con risorse multi-fondo); **impatto: M**. Mitigazione: progetto inquadrabile autonomamente anche fuori SNAI, grazie alla pluralità di stakeholder (PC, AGCOM, MIMIT).

### 1.2.2 La Liguria come laboratorio italiano per le Aree Interne (4 aree SNAI riconosciute)

La **Regione Liguria** è esempio paradigmatico di territorio italiano caratterizzato da Aree Interne ad alta densità di criticità. Nell'istruttoria del Comitato Nazionale Aree Interne[^5], la Regione Liguria figura con:

- **4 Aree SNAI confermate dal ciclo 2014-2020**: Antola Tigullio (16 comuni), Beigua Sol (10 comuni), Val di Vara (13 comuni), Valle Arroscia (11 comuni)[^5];
- **4 nuove Aree SNAI per il ciclo 2021-2027**: Imperiese (19 comuni, 13.000 abitanti), Fontanabuona (11 comuni, 15.000 abitanti), Bormida Ligure (13 comuni, 14.000 abitanti), Valle Scrivia (9 comuni, 20.000 abitanti)[^5];
- **8 Aree SNAI complessivamente attive** sul territorio regionale.

Sintesi delle caratteristiche strutturali ricorrenti (estratto dal rapporto istruttoria DPCoe[^5]):

| Caratteristica | Dato |
|---|---|
| Variazione demografica media aree 2011-2020 | -4.9% / -8.2% (a fronte di -3.32% / -6.01% regionale) |
| Densità abitativa aree | 30-80 ab/km² (media regionale: 280 ab/km²) |
| % superficie forestale | 70-80% |
| % comuni "piccoli" (< 5.000 ab) | ~80-90% in tutte le aree |
| Orografia | Prevalentemente montana / collinare appenninica |
| Distanza media dal polo di servizi | 30-45 minuti |

Le aree Antola Tigullio, Fontanabuona e Valle Scrivia ricadono nell'**Appennino Ligure interno della Città Metropolitana di Genova**, oggetto di particolare interesse per il progetto pilota (vedi §1.2.3 sul caso Pentema).

> **Caveat epistemico**: i dati sopra sono presentati come **estratti rappresentativi** non come tabella completa. Il rapporto istruttoria DPCoe[^5] è documento di programmazione 2022, da incrociare con dati ISTAT 2024 (vedi Cap. 2 per dataset territoriale aggiornato). *Confidence dati istruttoria: high*; *confidence proiezione 2026: medium*.

### 1.2.3 Pentema (Torriglia, GE) come caso studio pilota

La **frazione di Pentema**, nel **Comune di Torriglia (Città Metropolitana di Genova)**, è stata individuata da Regione Liguria come **caso studio rappresentativo** per la sperimentazione del progetto. Il Comune di Torriglia ricade nell'**Area SNAI Antola Tigullio** (16 comuni, ciclo 2014-2020, confermata 2021-2027)[^5]. Caratteristiche di Pentema rilevanti per la pilota:

| Dimensione | Caratteristica |
|---|---|
| Popolazione | Poche centinaia di abitanti (borgo storico) |
| Quota | ~870 m s.l.m. |
| Orografia | Vallata appenninica stretta, esposizione nord |
| Connettività esistente | Marginale (linea fissa rame storica, copertura mobile parziale) |
| Vie d'accesso | Strada provinciale unica, soggetta a interruzioni invernali |
| Servizi essenziali | Carenti (no scuola attiva, presidio sanitario di prossimità) |
| Esposizione rischi | Frane, incendi boschivi, isolamento da eventi meteo |

🎯 **Razionale di scelta**: Pentema rappresenta un **archetipo concentrato delle criticità delle Aree Interne italiane** — bassa densità, orografia complessa, connettività marginale, esposizione a eventi estremi. Una pilota che dimostri efficacia operativa su Pentema è **generalizzabile per analogia** alle altre 7 aree SNAI Liguria e, per estensione, alle 71 aree SNAI nazionali del ciclo 2021-2027.

> **Caveat epistemico**: la rappresentatività di Pentema è un'**assunzione del progetto** (registrata come ASM-001 nel Cap. 3 §3.9), non un fatto dimostrato. Esistono Aree Interne con caratteristiche differenti (es. zone insulari, aree desertiche del meridione). La generalizzazione richiede verifica nella Fase 2 (M+12-24) con replica in almeno 2-3 contesti diversi. *Confidence rappresentatività: medium*.

> **Falsifying observation**: se al gate M+10/M+11 il Comune di Torriglia o la comunità Pentema **non concedono accettabilità sociale** al volo persistente (es. per ragioni di rumore residuo, percezione di sorveglianza, opposizione locale al concept), il caso pilota va spostato in altra frazione/area SNAI Liguria (es. Beigua Sol, Val di Vara, Fontanabuona). *Probabilità: L-M* (comunità minima — 14 abitanti ISTAT — quindi basso rischio assoluto numerico ma alto rischio relativo se un singolo evento mediatico polarizza); *impatto: M-H* (slittamento timeline 6 mesi). Mitigazione: workshop pubblico + DPIA pubblica + governance condivisa entro M+9 (vedi Cap. 5 §5.6.2 e OQ-CAP1-03).

### 1.2.4 Le criticità delle Aree Interne che il progetto affronta

Sintesi delle criticità che lo Studio di Fattibilità si propone di affrontare, derivata dall'incrocio tra PSNAI[^4], Briefing[^3] e rapporto istruttoria Liguria[^5]:

| # | Criticità | Manifestazione concreta | Risposta progettuale |
|---|---|---|---|
| C-1 | **Spopolamento** | Variazione 2011-2020 negativa (-4.9% / -16% per singoli comuni) | Servizi digitali che migliorano qualità della vita ("diritto di restare") |
| C-2 | **Digital divide** | Connettività fissa rame / mobile partial | Connettività cooperativa "above-the-clouds" ridondante |
| C-3 | **Isolamento informativo emergenze** | Black-out comunicativi da frane/alluvioni/incendi | Ponte radio multi-standard, C2 di backup, alert events |
| C-4 | **Vulnerabilità rischio idrogeologico** | Frane, alluvioni, incendi crescenti per cambiamento climatico | Monitoraggio EO persistente (alta risoluzione, refresh continuo) |
| C-5 | **Servizi sanitari carenti** | Distanza media 30-45 min dal polo, presidi locali deboli | Telemedicina di prossimità abilitata da connettività NTN |
| C-6 | **Mobilità interrotta** | Strade soggette a interruzioni meteo | Coordinamento PC + situational awareness real-time |
| C-7 | **Costi unitari infrastrutture terrestri** | CAPEX antieconomico per torri, dorsali in aree impervie | Infrastruttura "above-the-clouds" senza opere civili a terra |
| C-8 | **Cooperative di comunità sotto-dotate** | Connettività inaffidabile per gestione servizi | Connectivity-as-a-Service cooperativo, data-commons territoriale |

Queste otto criticità costituiscono i **fabbisogni quantitativi e qualitativi della collettività** ai sensi dell'art. 1, comma 1.b dell'Allegato I.7 D.Lgs. 36/2023[^1]. Sono il fondamento del Quadro Esigenziale del progetto.

> **Falsifying observation**: se uno o più dei programmi nazionali di infrastrutturazione terrestre (es. BUL — Banda Ultra Larga, dorsali Open Fiber, 5G dei principali MNO) raggiungesse copertura piena delle Aree Interne italiane entro M+24, le criticità C-2 e C-3 sarebbero **strutturalmente attenuate** e il razionale del progetto andrebbe ridimensionato a casi specifici (es. emergenze, monitoraggio EO). **Probabilità: L-M** (la storia del BUL mostra ritardi sistemici di 5-10 anni sui target); **impatto: H** sul value proposition connettività. Mitigazione: diversificazione del portfolio servizi (EO + alert events + connettività emergenza, non solo connettività ordinaria).

---

## 1.3 Visione tecnologica: piattaforma H.A.L.E. e "vuoto di quota"

### 1.3.1 Concept tecnologico HALE/HAPS

La visione tecnologica di lungo termine si fonda sul concetto di **piattaforma H.A.L.E. (High Altitude Long Endurance)**: un velivolo stratosferico ad ala fissa, a energia solare, capace di operare in quota a **~20 km AGL** per durate di **settimane / mesi continuativi**. Nella terminologia ITU e 3GPP, la classe è denominata **HAPS — High Altitude Platform Station**[^6][^7][^8].

Caratteristiche tecnologiche di riferimento (concept Firmamento, vedi `Progetto concettuale struttura HALE.md`):

| Parametro | Valore di concept |
|---|---|
| Quota operativa | 18-22 km AGL (stratosfera bassa, sopra il traffico aereo commerciale) |
| Autonomia di missione | Settimane / mesi (continuativi, energia solare + batterie LiPo/LiS) |
| Apertura alare target | 20-30 m (high aspect ratio, AR > 25) |
| MTOM target | 50-150 kg (concept attuale, scenario lightweight) |
| Payload utile | 5-15 kg modulare (EO + Telecom) |
| Velocità di crociera | 30-50 kt (compatibile con jet stream stratosferico) |
| Materiali primari | Compositi (fibra di lino + epossidica bio, narrativa ESG) |
| Architettura aerodinamica | High AR, T-tail (vedi `Progetto concettuale struttura HALE.md`) |
| Categoria EASA | **Certified** (vedi Cap. 5 §5.4.2) |
| Caso d'uso | Pseudo-satellite locale per EO + Telecom NTN |

Il termine "**pseudo-satellite**" descrive in maniera sintetica la funzione: una piattaforma che combina la **persistenza tipica del satellite** con la **prossimità geografica e la riconfigurabilità tipiche del segmento aereo**.

> **Caveat epistemico**: il concept tecnologico è **preliminare di Phase A**. La specifica MTOM, l'apertura alare, la durata della batteria e i margini energetici invernali sono dichiarati come **target di progettazione**, non come capacità verificate. Il **bilancio energetico invernale a 44°N** è esplicitamente registrato come **showstopper tecnico RSK-TEC-001** nel Risk Register (Cap. 6 §6.4). *Confidence: medium* (analogia con PHASA-35 e Zephyr-S, ma senza validazione interna).

### 1.3.2 Vantaggi vs satellitare e vs terrestre — il "vuoto di quota"

Il razionale tecnologico della classe HAPS è descritto in maniera sintetica come **colmamento del "vuoto di quota"** tra le infrastrutture terrestri (suolo, torri 4G/5G, dorsali in fibra) e le infrastrutture spaziali (satelliti GEO a ~36.000 km, costellazioni LEO a 500-1.500 km)[^3]. Tabella comparativa:

| Dimensione | Infrastruttura terrestre | HAPS (HALE @ 20 km) | LEO satellitare | GEO satellitare |
|---|---|---|---|---|
| Latenza one-way | < 1 ms (locale) | ~3-5 ms | ~5-25 ms | ~120 ms |
| Footprint singolo nodo | 0.5-30 km (4G/5G cell) | 50-200 km (cella service link) | 500-3.000 km (cella) | continentale |
| CAPEX per nodo | €50-500k/torre + dorsali | €5-50M/HAPS (stima) | €0.5-5M/sat (Starlink-class) | €100-500M/sat (GEO classico) |
| Persistence | Continua (se non guasti) | Settimane/mesi | Visibilità < 10 min per pass | Continua |
| Riconfigurabilità | Bassa (infra fissa) | **Alta** (riposizionamento ore) | Bassa (orbita fissa) | Nulla |
| Tempi di attivazione zona scoperta | 6-24 mesi (sito + permessi) | **Ore / giorni** | Anni (deployment costellazione) | Anni (lancio dedicato) |
| Vulnerabilità a eventi meteo | Alta (torri, dorsali) | Media (vento stratosferico) | Bassa | Nulla |
| Sostenibilità in operazione | Variable (mix energetico rete) | **Zero emissioni** (solare) | Zero emissioni in orbita | Zero emissioni in orbita |
| Sovranità tecnologica | Dipendente da supply chain MNO | **Italiana / europea** (B2 boundary) | Estera (Starlink US, Eutelsat partim) | Mista |

Le **tre proprietà strutturali** del HAPS che lo distinguono come categoria sono[^3]:

1. **Persistenza** continuativa multi-settimana/mese senza ricollocamento;
2. **Bassa latenza** (decine di km vs migliaia/decine di migliaia di km dello spaziale);
3. **Riconfigurabilità** in tempo reale del footprint e dei carichi utili.

### 1.3.3 Architettura preliminare di sistema (richiamo)

L'architettura preliminare del sistema HALE è dettagliata nel Cap. 6 (Analisi tecnica) e in `Progetto concettuale struttura HALE.md`. Sintesi:

- **Segmento volante**: HALE singolo o in **mesh** (cluster operativo coordinato);
- **Segmento di terra**: gateway di comunicazione + **NOC** (Network Operations Center) per controllo di volo, orchestrazione payload, sicurezza end-to-end;
- **Segmento dati**: data-lake / **data-commons** territoriale, governance condivisa con cooperative + PA, conformità GDPR + privacy-by-design, API interoperabili per servizi terzi[^3].

L'architettura logica e di sicurezza (BlockDiagram + Trust Boundaries) è dettagliata nel Cap. 4 (Perimetro, scope, ICD) e nel Vol. 2 Allegato A.4.

---

## 1.4 Necessità di analisi comparativa e approccio scalabile

Lo Studio di Fattibilità non si limita a una valutazione "monolitica" della piattaforma HALE: l'art. 41 D.Lgs. 36/2023 richiede esplicitamente — nell'**Allegato I.7, Sezione I, Articolo 2 (DOCFAP)** — l'analisi comparativa di **alternative progettuali**, inclusa l'ipotesi di non realizzazione dell'intervento[^1, all. I.7 art. 2]. Il presente Studio adotta questo principio in due modi:

1. **Analisi comparativa interna alla classe HAPS**: confronto tra alternative architetturali (HALE solare vs MALE ibrido vs lighter-than-air / aerostato stratosferico), formalizzato come **trade study** sintetizzato nel Cap. 6 §6.3 e nel Vol. 2 Allegato A.3 (`DOCFAP`).

2. **Approccio scalabile risk-informed (Strategia duale)**: separazione del progetto in **due percorsi indipendenti** che condividono asset, governance e cliente — ma con orizzonti, tecnologie e rischi differenziati. Il rationale è esplicitamente quello di **ridurre il rischio totale del programma**, permettendo (a) operatività immediata con tecnologia matura e (b) preparazione progressiva della tecnologia di lungo termine, con la possibilità di pivot se uno dei due percorsi fallisce.

🎯 **Principio guida**: il fallimento di 6B (HALE stratosferico) non deve compromettere l'operatività di 6A (VTOL pilota); ogni asset, ogni processo e ogni learning del Percorso 6A è progettato per essere **riutilizzabile** anche in uno scenario "HALE non si materializza" (vedi `riferimenti/visione-10-anni.md` §1).

Questo principio è la **giustificazione strategica della separazione 6A/6B** ed è coerente con la prassi NASA SE Handbook §3 (risk-informed decision making) e con i criteri di **proporzionalità** dell'art. 41 D.Lgs. 36/2023[^1, art. 41 c. 5].

---

## 1.5 Obiettivi del Piano di Fattibilità

### 1.5.1 Sei obiettivi del PFTE

Ai sensi dell'art. 1, comma 1.a dell'Allegato I.7 D.Lgs. 36/2023[^1], il Quadro Esigenziale deve riportare "gli obiettivi generali da perseguire attraverso la realizzazione dell'intervento, con gli associati indicatori chiave di prestazione". Per il presente Studio di Fattibilità, gli obiettivi generali sono **sei**:

🎯 **Obiettivi del Piano di Fattibilità HALE/VTOL**:

1. **OB-01 — Validare la fattibilità tecnico-economico-regolatoria** della piattaforma HALE/VTOL per le Aree Interne italiane, in coerenza con la SNAI e il PSNAI 2025[^4].
2. **OB-02 — Co-progettare con le 10 cooperative Legacoop** un Concept of Operations operativo, in linea con i fabbisogni dei cinque cluster funzionali (sanità prossimità, soccorso, agro-forestale, energia/servizi, cultura/turismo)[^3].
3. **OB-03 — Definire e validare il Percorso 6A** (VTOL commerciale pilota Pentema) come deliverable operativo a 12 mesi, con verdetto Go Condizionato.
4. **OB-04 — Definire e validare il Percorso 6B** (R&D HALE stratosferico) come orizzonte di sviluppo a 24-48+ mesi, con verdetto Hold / Go Condizionato Estremo e piano di chiusura showstopper.
5. **OB-05 — Predisporre la documentazione formale** richiesta dall'art. 41 D.Lgs. 36/2023 + Allegato I.7 (Quadro Esigenziale, DOCFAP sintetico, struttura PFTE, Quadro Economico) per consentire la partecipazione del progetto a bandi pubblici italiani[^1].
6. **OB-06 — Costruire la base evidenziale** (RTM, Risk Register, Trade Study, V&V Plan, ICD) richiesta per il gate review M+10/M+11 e per i finanziatori istituzionali (Coopfond, Regione Liguria, PNRR Aerospazio, FESR, Horizon Europe).

**KPI di gate** (riepilogati nel Cap. 3 §3.2; dettaglio nel Cap. 9):

| Obiettivo | KPI di gate M+10 | Soglia GO |
|---|---|---|
| OB-01 | Studio di Fattibilità completo, 3 volumi | ✓ pubblicato + Red Team review |
| OB-02 | StNeeds consolidati da 10 cooperative | ≥ 17 StNeeds tracciati in RTM |
| OB-03 | Verdetto Percorso 6A | Go Condizionato motivato |
| OB-04 | Verdetto Percorso 6B | Hold + piano R&D Phase B con gate M+24 |
| OB-05 | Documentazione art. 41 | ✓ QE + DOCFAP + PFTE + QE |
| OB-06 | Risk Register top-10 | ✓ tutti con piano di mitigazione |

### 1.5.2 Strategia duale: Percorso 6A (VTOL pilota) + Percorso 6B (HALE R&D)

Il cuore del Quadro Esigenziale è la **strategia duale risk-informed**, articolata in due percorsi paralleli e tecnicamente disaccoppiati:

#### **Percorso 6A — Pilota VTOL (0-12 mesi, Go Condizionato)**

- **Tecnologia**: piattaforma commerciale **VTOL ibrida TRL 8-9** (riferimento: JOUAV CW-30E o Quantum Trinity F90+ o equivalente, in trade study Cap. 6).
- **Caratteristiche operative**: autonomia 6-10 ore, copertura locale 30-50 km, payload modulare 10-25 kg, MTOM ~38 kg.
- **Categoria EASA**: **Specific Category, SAIL II-III** (vedi Cap. 5 §5.4.1).
- **Sito pilota**: Pentema (Torriglia, GE), con possibile estensione altre frazioni Area SNAI Antola Tigullio.
- **Orizzonte temporale**: M+12 → M+24 operatività Fase 1.
- **Budget stimato**: **€600k – 900k** (acquisto piattaforma + integrazione + SORA + operatività Y1).
- **Rischio complessivo**: **Basso**, con verdetto **Go Condizionato** (vedi Cap. 5 §5.12 e Cap. 10).
- **Output operativi attesi**:
  - ≥ 50 missioni operative eseguite (M+12-24);
  - ≥ 3 contratti pluriennali con anchor customers (Regione Liguria + PC + cooperative scaled);
  - Primo revenue ricorrente da servizi.

#### **Percorso 6B — HALE Stratosferico (24-48+ mesi, Hold / Go Condizionato Estremo)**

- **Tecnologia**: **UAV solare HALE stratosferico**, sviluppo proprietario in consorzio (potenziale: Firmamento + CIRA + POLITO DIMEAS + partner industriale).
- **Caratteristiche operative**: quota 18-22 km, autonomia settimane/mesi, payload 5-15 kg, apertura alare 20-30 m.
- **Categoria EASA**: **Certified, Special Condition HAPS** in negoziazione (vedi Cap. 5 §5.4.2).
- **Orizzonte temporale**: R&D Phase B M+12 → M+48; Phase C operativo M+48-72.
- **Budget stimato R&D Phase B**: **€5.5-13.5M** (range realistico Cap. 8 §8.3.3); Phase C operativa post-Studio non in scope attuale.
- **Rischio complessivo**: **Alto**, con verdetto **Hold / Go Condizionato Estremo** in attesa di chiusura showstopper.
- **Showstopper noti** (vedi Cap. 5 §5.10 + Cap. 6 §6.4):
  - RSK-TEC-001 — bilancio energetico invernale 44°N non validato;
  - RSK-TEC-002 — margini aeroelastici (flutter) ali high AR;
  - RSK-REG-001 — assenza framework regolatorio HAPS civile EASA;
  - RSK-FIN-001 — capital intensity Phase B-C non finanziata sul mercato attuale.
- **Posizionamento strategico**: **preparazione progressiva** della tecnologia di lungo termine, con asset e learning del Percorso 6A che riducono progressivamente il rischio di 6B.

#### **Sintesi comparativa**

| Dimensione | **Percorso 6A** | **Percorso 6B** |
|---|---|---|
| Titolo | Pilota VTOL Pentema | R&D HALE stratosferico |
| Orizzonte | 0-12 mesi (operatività Y1-Y3) | 24-48+ mesi (R&D + operatività Y4+) |
| Tecnologia | Commerciale TRL 8-9 | R&D, TRL 3-4 → 7-8 |
| Categoria EASA | Specific SAIL II-III | Certified, Special Condition |
| Budget | €600k – 900k (operatività Y1) | €5.5M – 11M (R&D Phase B) |
| Rischio | Basso | Alto |
| Verdetto target M+10 | **GO Condizionato** | **HOLD / Go Condizionato Estremo** |
| Funzione strategica | Validazione operativa, revenue Y1-Y3 | Preparazione visione 10 anni |
| Reuse degli asset | Diretto (ground segment, governance, customer base) | Selettivo (NOC, customer relationships, regulatory experience) |

🎯 **Posizionamento del Percorso 6A nel ciclo di vita strategico (vedi `riferimenti/visione-10-anni.md`)**: il Percorso 6A coincide con la **Fase 1** della visione 10 anni ("Pilota validato", Y1: M+0 → M+12). Lo Studio di Fattibilità **approva esplicitamente solo Fase 1 e l'avvio di Phase B per 6B**. Le Fasi 2-5 (scale-up Italia, prototipo HALE, costellazione, consorzio EU sovrano) non sono in scope del presente gate.

> **Falsifying observation**: se entro M+12 la pilota Pentema mostra **failure mode strutturale** (es. accettabilità sociale negata dalla comunità, vincoli normativi ENAC insormontabili, technical failure delle missioni con MTBF < 50 h), il Percorso 6B perde la sua **base operativa** di learning e va rinviato a oltranza, congelando il progetto a livello strategico. *Probabilità di failure mode 6A: L-M; impatto: H sul progetto complessivo*. Mitigazione: gate M+6 di re-baselining della pilota; gate M+9 prima dell'avvio missioni operative.

### 1.5.3 Articolazione temporale M+0 → M+11

Lo Studio di Fattibilità si svolge sull'arco temporale **M+0 → M+11 (12 mesi)**, con i seguenti gate decisionali maggiori (dettaglio nel Cap. 9):

| Gate | Mese | Output / Decisione |
|---|---|---|
| Kickoff | M+0 | Avvio Studio, baseline metodologica |
| **G-1 — Architettura baselined** | M+6 | Concept architettura 6A + 6B baseline, pre-application ENAC fatto, StNeeds consolidati |
| G-2 — Mid-term review | M+8 | RTM v0.5, FMECA preliminare, ConOps validato cooperative |
| **G-3 — Studio completo** | M+10 | Studio di Fattibilità 3 volumi pronto, Red Team chiuso |
| **G-4 — Verdetto di Gate** | M+11 | Decisione formale Go Condizionato 6A / Hold 6B, condivisione con Coopfond + Regione Liguria |

🎯 **Gate M+10/M+11 — decisione strutturale**: è il gate dove lo Studio di Fattibilità si chiude con un **verdetto formale di Go / Hold / No-Go** per ciascuno dei due percorsi. Il **Go Condizionato** del Percorso 6A è la base per richiedere l'avvio della **Fase 1 operativa** (Pentema VTOL pilota M+12 → M+24), con i finanziamenti raccolti per quella fase.

I gate post-Studio (M+24 ARR validation, M+36 Phase B decision, etc.) sono **out of scope** del presente Studio e sono descritti nel Cap. 11 (Roadmap post-fattibilità).

---

## 1.6 Conformità alla struttura del Quadro Esigenziale art. 41 + Allegato I.7

Il presente Capitolo 1 è strutturato per soddisfare formalmente i requisiti minimi del **Quadro Esigenziale** ai sensi dell'**Allegato I.7, Sezione I, Articolo 1** del D.Lgs. 36/2023[^1]:

> *"Il quadro esigenziale tiene conto di quanto previsto negli strumenti di programmazione del committente. Esso, per ciascun intervento da realizzare, in relazione alla tipologia dell'intervento stesso, riporta:*
> *a) gli obiettivi generali da perseguire attraverso la realizzazione dell'intervento, con gli associati indicatori chiave di prestazione;*
> *b) i fabbisogni, le esigenze qualitative e quantitative del committente, della collettività o della specifica utenza alla quale l'intervento è destinato, che dovranno essere soddisfatti attraverso la realizzazione dell'intervento stesso."* [^1, all. I.7 art. 1]

**Tabella di mappatura**:

| Requisito Allegato I.7 art. 1 | Sezione del Cap. 1 che lo soddisfa |
|---|---|
| **Coerenza con strumenti di programmazione** (PSNAI, ENAC AAM, programmazione SNAI) | §1.2.1 (PSNAI) + §1.2.2 (SNAI Liguria) + Cap. 5 §5.3.4 (ENAC AAM) |
| **Obiettivi generali con KPI** (lett. a) | §1.5.1 (sei obiettivi OB-01..OB-06 + tabella KPI di gate) |
| **Fabbisogni qualitativi della collettività** (lett. b) | §1.2.4 (otto criticità C-1..C-8) + Cap. 3 §3.3.2 (StNeeds consolidati) |
| **Fabbisogni quantitativi della specifica utenza** (lett. b) | §1.1.2 (cinque cluster cooperative) + §1.2.3 (caratteristiche Pentema) |
| **Coerenza con DIP successivo** | §1.5.2 (strategia duale che diventa input per il DIP post-M+11) |

Lo Studio di Fattibilità si pone come **PFTE (Progetto di Fattibilità Tecnico-Economica)** ai sensi dell'art. 41, comma 1 D.Lgs. 36/2023[^1, art. 41]. La **redazione del Quadro Esigenziale è di esclusiva competenza del committente** ai sensi dell'art. 1, comma 3 dell'Allegato I.7[^1, all. I.7 art. 1 c. 3]. Nel caso del presente Studio, il **committente coincide con il proponente Firmamento Technologies** (il progetto è iniziativa privata-cooperativa, non opera pubblica in senso stretto): pertanto il QE è redatto direttamente da Firmamento in collaborazione con la rete cooperative e con Regione Liguria come stakeholder istituzionale.

Per la formalizzazione a beneficio di bandi pubblici futuri (FESR Liguria, PNRR Aerospazio), il QE potrà essere **adottato per estratto in atti di committenza pubblica** (es. delibera Regione Liguria sull'avvio della Fase 1 operativa post-M+11).

> **Source provenance** [^1]: `fonti/2023_0036.md` (D.Lgs. 31 marzo 2023, n. 36 — Codice dei contratti pubblici, testo integrale + Allegati incluso I.7), in vigore. *Confidence: high*.

---

## 1.7 Coerenza con la cornice istituzionale ENAC AAM

Sebbene il presente progetto non si configuri formalmente come progetto di **Advanced Air Mobility (AAM)** nel senso classico ENAC (mobilità di persone/beni in ambito urbano)[^9], esiste una **convergenza istituzionale rilevante** con il Piano Strategico Nazionale AAM 2021-2030 di ENAC[^9]:

1. **Visione tecnologica condivisa**: il Piano AAM definisce un ecosistema multi-stakeholder per nuove forme di trasporto aereo, includendo **UAS e droni** tra le categorie centrali (executive summary)[^9].
2. **Approccio gap analysis**: il Piano AAM articola la sua strategia su tre livelli (regolatorio, tecnologico, infrastrutturale), che è lo stesso approccio adottato dal presente Studio (vedi Cap. 5 §5.4 sulla gap analysis regolatorio + tecnologico).
3. **Stakeholder model**: il Piano AAM disegna una cabina di regia ENAC + ENAV + MIT + MIMIT + soggetti industriali (Leonardo, Telespazio, ADR)[^9]; il presente Studio si inserisce in questo ecosistema con la specificità del **layer stratosferico HAPS** (vedi Cap. 5 §5.3.4 sul posizionamento Firmamento nel Piano AAM).

🎯 **Posizionamento strategico**: il presente Studio argomenta l'**inserimento del layer HAPS** come **estensione naturale** dell'ecosistema AAM-Italy delineato da ENAC, posizionando Firmamento come **operatore di servizi stratosferici complementare** (non concorrente) ai player già citati nel Piano AAM. Questo posizionamento è coerente con la boundary condition B2 ("complementare a IRIS²") e con il vettore strategico 10 anni (`riferimenti/visione-10-anni.md` §7).

---

## 1.8 Riferimenti

[^1]: D.Lgs. 31 marzo 2023, n. 36 — "Codice dei contratti pubblici in attuazione dell'articolo 1 della legge 21 giugno 2022, n. 78, recante delega al Governo in materia di contratti pubblici". In particolare: art. 41 (Livelli e contenuti della progettazione) + Allegato I.7 (Contenuti minimi del quadro esigenziale, del documento di fattibilità delle alternative progettuali, del documento di indirizzo della progettazione, del progetto di fattibilità tecnica ed economica e del progetto esecutivo) — Sezione I, Articoli 1-4. **Source:** `fonti/2023_0036.md` (testo integrale, righe 7608-7799). **Confidence: high** (norma in vigore).

[^2]: Coopfond / Fondazione PICO ETS, bando "Cooding Prototypes" 2025-2026 — Strumento di finanziamento per studi di fattibilità di prototipi cooperativi. Capofila rete: **Fabrica** (cooperativa di comunità). 10 cooperative aderenti a Legacoop come utenti-pilota. **Source:** `bando/progetto prototype cooding.md` + `bando/Sintesi prototype cooding.md`. **Confidence: high** (documentazione bando in possesso del proponente).

[^3]: Firmamento Technologies, "Briefing: Progetto Piattaforma Aerea per le Aree Interne", documento interno di sintesi del Piano di Fattibilità in lavorazione (2025-2026). **Source:** `da revisionare/Briefing_ Progetto Piattaforma Aerea per le Aree Interne.md`. **Confidence: high** (documento del proponente).

[^4]: Ministero per gli Affari Europei, il Sud, le Politiche di Coesione e il PNRR (Dipartimento per le Politiche di Coesione), **Piano Strategico Nazionale per le Aree Interne (PSNAI)**, approvato dal Ministro in data 30 luglio 2025. Documento programmatico nazionale, 7 capitoli + 11 allegati. **Source:** `fonti/psnai_finale_30072025_clean_ministro.md` (6.415 righe). **Confidence: high** (documento ufficiale in vigore).

[^5]: Comitato Nazionale Aree Interne (DPCoe + NUVAP), "Rapporto di Istruttoria per la Selezione delle Aree Interne 2021-2027 — Regione Liguria", ottobre 2022. Identifica 4 nuove Aree SNAI Liguria (Imperiese, Fontanabuona, Bormida Ligure, Valle Scrivia) + conferma 4 Aree del ciclo 2014-2020 (Antola Tigullio, Beigua Sol, Val di Vara, Valle Arroscia). **Source:** `Aree interne/rapporto-istruttoria_regione-liguria.md` (860 righe). **Confidence: high** (documento istituzionale firmato CTAI 29 settembre 2022).

[^6]: ITU Radio Regulations 2024 (Edition 2024), Article 5 + Resolution 122 (WRC-19), 122-bis (WRC-23). Bande HAPS riconosciute per service link e feeder link. **Source:** vedi Cap. 5 §5.5.1 per dettaglio. **Confidence: high**.

[^7]: 3GPP TR 38.811 V15.4.0 (2020-09), "Study on New Radio (NR) to support non-terrestrial networks". HAPS esplicitamente supportata come scenario NTN. **Source:** `fonti/38811.md`. **Confidence: high**.

[^8]: 3GPP TR 38.821 V16.2.0 (2023-03), "Solutions for NR to support non-terrestrial networks (NTN) (Release 16)". **Source:** `fonti/3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md`. **Confidence: high**.

[^9]: ENAC, "Piano Strategico Nazionale Advanced Air Mobility (AAM) 2021-2030 — Per lo sviluppo della Mobilità Aerea Avanzata in Italia". Con Allegati 1 (Roadmap) e 2 (Business Plan). **Source:** `fonti/01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.md` + Allegati. **Confidence: high** (documento ENAC ufficiale).

[^10]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105), in particolare §4.1-4.2 (Stakeholder Expectations + Technical Requirements) e §3 (Risk-Informed Decision Making). Citato come framework metodologico. **Confidence: high**.

[^11]: Firmamento Technologies, "Visione strategica 10 anni — Firmamento Technologies", documento interno di posizionamento strategico. **Source:** `riferimenti/visione-10-anni.md`. **Confidence: high** (documento del proponente).

[^12]: Comunicazione della Commissione Europea, "Demographic Change in Europe — A Toolbox for Action" (Talent Booster Mechanism), gennaio 2023. Citata dal PSNAI[^4] come sfondo europeo della SNAI. **Confidence: medium** (riferimento secondario via PSNAI).

---

## 1.9 Assumptions e Open Questions del Capitolo 1

### 1.9.1 Assumptions baseline del Cap. 1

Coerentemente con la skill `epistemic-rigor`, le assunzioni del presente capitolo sono dichiarate esplicitamente:

| ID | Assunzione | Confidence | Mitigazione se falsa |
|---|---|---|---|
| ASM-CAP1-01 | Pentema è rappresentativa delle Aree Interne italiane | medium | Replica in 2-3 contesti diversi in Fase 2 (M+12-24) |
| ASM-CAP1-02 | La rete delle 10 cooperative resterà aderente al progetto fino a M+24 | medium | LoI bilaterali in raccolta M+0-4 |
| ASM-CAP1-03 | Regione Liguria conferma il pilota Pentema con delibera o LoI entro M+10 | medium | Engagement bilaterale Q1-Q2 2026, gate M+10 condizionato |
| ASM-CAP1-04 | PSNAI 2025 resta cornice di riferimento per Y2-Y3 (ciclo 2027 invariato) | high | Cambio cornice darebbe risk acceptable se rimpiazzo con FESR/PNRR |
| ASM-CAP1-05 | Boundary conditions B1 e B2 non vengono ritirate dal fondatore di Firmamento durante il progetto | high (dichiarata) | Cambio richiede re-baselining intero Studio |
| ASM-CAP1-06 | Il concept HALE solare resta coerente con state-of-the-art (PHASA, Zephyr, Skydweller) entro M+11 | medium | Cambio concept (es. dirigibile, idrogeno) richiederebbe ridefinizione |

Le assunzioni sono cross-referenced nel Cap. 3 §3.9 (Assumptions consolidate) e nel Risk Register Vol. 2 Allegato A.2.

### 1.9.2 Open Questions del Cap. 1

Le **Open Questions** sono questioni aperte che devono essere chiuse prima del gate M+10/M+11:

| ID | Domanda aperta | Owner | Target | Stato |
|---|---|---|---|---|
| OQ-CAP1-01 | LoI Regione Liguria sul caso pilota Pentema (delibera o equivalente) | Firmamento + Regione Liguria | M+8 | Open |
| OQ-CAP1-02 | NDA + LoI 10 cooperative Legacoop (capofila Fabrica) | Firmamento + Fabrica | M+4 | Open (in corso) |
| OQ-CAP1-03 | Confidenza accettabilità sociale Pentema (workshop pubblico) | data-privacy-counsel + Firmamento | M+9 | Open |
| OQ-CAP1-04 | Verifica formale che il committente del PFTE coincida con il proponente (vs richiesta committente pubblico) | aviation-regulatory-counsel | M+6 | Open |
| OQ-CAP1-05 | Confidence intervalli budget Percorso 6A €600k-900k post-trade study M+6 | systems-engineer + finance-counsel | M+8 | Open |
| OQ-CAP1-06 | Mappa Aree SNAI 2026 aggiornata (vs istruttoria 2022) | territorial-planning | M+5 | Open |
| OQ-CAP1-07 | Posizionamento Firmamento nel Piano ENAC AAM (formalizzato in position paper) | sovereign-strategist | M+12 | Open |

Le OQ qui dichiarate convergono con le OQ del Cap. 3 §3.10 e con il debito di rigore (`riferimenti/audit-rigore-epistemico.md`).

---

## 1.10 Red Team Check — Stress-Test del Capitolo

Il presente capitolo è stato sottoposto a stress-test dall'agente `red-team-skeptic`, con prospettiva simulata di tre potenziali finanziatori critici:

- **R1 — Coopfond / Fondazione PICO ETS** (finanziatore istituzionale cooperativo, focus su impatto sociale e replicabilità)
- **R2 — Regione Liguria** (anchor istituzionale, focus su valore aggiunto territoriale e accountability)
- **R3 — Commissione UE** (DG CNECT / DEFIS / MOVE, focus su sovranità tecnologica e proporzionalità)

### Critica R1 (Coopfond): "Il modello cooperativo è davvero centrale o è un wrapper retorico?"

**Critica dettagliata**: il bando Cooding finanzia studi di fattibilità di **prototipi cooperativi**. Il presente progetto presenta un velivolo HALE/VTOL con architettura tecnologica complessa, dove il ruolo delle cooperative è descritto in termini generici ("utenti-pilota", "co-progettisti", "cluster funzionali"). Cosa garantisce che le cooperative siano **decisori strutturali** del progetto e non semplicemente **clienti di un servizio venduto da una PMI tecnologica**? Se la struttura proprietaria di Firmamento è interamente privata, dove sta la cooperatività?

**Risposta**:

1. La boundary condition B1 dichiara esplicitamente che il modello è **cooperativo + service-only**: Firmamento opera **in partnership stabile** con la rete cooperative (non meramente come fornitore terzo). La governance dello shared data layer è **data-commons territoriale** (vedi §1.3.3 e Cap. 4).
2. La fase di co-design dei requisiti (M+0 → M+6) è **strutturale**: i requisiti operativi del sistema (Cap. 3 §3.3.2) derivano direttamente dai workshop con le cooperative, non sono imposti top-down.
3. **Riconoscimento del limite**: la struttura societaria di Firmamento attualmente è privata. La cooperatività si esprime nella **filiera del servizio** (data layer, governance, pricing differenziato per cooperative), non nella **struttura proprietaria** del velivolo. Questo è un tema aperto, da formalizzare nel Cap. 7 §7.6 (BMC) e potenzialmente da rafforzare con strumenti di **partecipazione cooperativa** (es. partecipazione minoritaria al data layer, co-governance del NOC, formula consortile della Fase 2).
4. **Azione di rafforzamento richiesta**: definire entro M+8 il modello di governance cooperativa formale (vedi OQ-CAP1-02), inclusa l'eventuale formula consortile della Fase 1 operativa.

### Critica R2 (Regione Liguria): "Perché Pentema? Cosa garantisce che il pilota produca valore per la Regione?"

**Critica dettagliata**: la Liguria ha **8 Aree SNAI riconosciute**, con criticità diverse (entroterra Imperia vs Antola Tigullio vs Val di Vara). Pentema è una frazione di sole **14 persone ISTAT** (dimensione micro-pilota deliberata). Se il pilota funziona a Pentema, qual è il **percorso verso scale-up regionale**? Quali sono i **KPI quantitativi** che giustificano l'allocazione di tempo della Regione Liguria su una pilota di scala micro? Quali sono i **risultati che la Regione può portare a casa** per giustificarne politicamente l'adesione?

**Risposta**:

1. Pentema è **caso archetipo** di criticità Aree Interne — concentra in una sola frazione tutte le criticità descritte in §1.2.4 (orografia, isolamento, digital divide, vulnerabilità eventi). La pilota Pentema non vale solo per Pentema: vale **per analogia** a tutte le frazioni simili nelle 8 Aree SNAI Liguria.
2. **KPI quantitativi del pilota Y1-Y2** (dettaglio Cap. 7 §7.9 + Cap. 8): ≥ 50 missioni operative, ≥ 3 contratti pluriennali firmati, ≥ €200k revenue cumulati (vedi `riferimenti/visione-10-anni.md` Fase 1). Gli output PA-facing sono: mappe di rischio frane ad alta risoluzione, alert antincendio early-warning, telemedicina di prossimità abilitata.
3. **Scale-up regionale** è esplicitamente Fase 2 della visione 10 anni (M+12 → M+36): flotta 3-8 piattaforme + copertura 4 Aree SNAI Liguria + estensione 2-3 regioni (Piemonte, Marche, Calabria). La Regione Liguria è **anchor istituzionale** del path verso scale-up.
4. **Risultati politici per la Regione** (linguaggio Cap. 7 §7.11 sull'impatto): Liguria come **prima regione italiana** che valida un layer stratosferico di servizio pubblico cooperativo — **brand positioning** nei tavoli nazionali (PNRR Aerospazio, AAM Italy, Strategic Autonomy EU).
5. **Riconoscimento del limite**: l'LoI Regione Liguria non è ancora formalizzata (OQ-CAP1-01); il gate M+10 dipende strutturalmente da questo. Mitigazione: engagement bilaterale dedicato Q1-Q2 2026.

### Critica R3 (Commissione UE): "Cosa rende il progetto strategicamente diverso da PHASA-35, Zephyr, AALTO, Skydweller? È duplicazione di asset EU già in corso?"

**Critica dettagliata**: la Commissione UE ha già investito risorse significative su HAPS attraverso il programma **EuroHAPS** (Airbus, BAE Systems, Thales, etc.) e si sta posizionando per ulteriori call su HAPS sovrano. La Commissione potrebbe chiedersi: **cosa aggiunge un nuovo player italiano early-stage** rispetto agli incumbent europei? Se il progetto si propone come "nodo italiano fondatore" di un'infrastruttura EU sovrana (B2), perché non semplicemente partecipare ai bandi EuroHAPS-adjacent come subcontractor?

**Risposta**:

1. **Differenziatore strutturale**: nessun player HAPS EU attuale (Airbus Zephyr/AALTO, BAE PHASA-35, Skydweller) si propone come **operatore di servizi** per Aree Interne italiane, con modello cooperativo + co-progettazione con utenti istituzionali italiani. Tutti sono **OEM** che vendono o leasano la piattaforma a clienti finali (prevalentemente DoD US/UK, governi).
2. **Differenziatore di servizio**: il presente progetto si pone come **layer stratosferico operatore di servizi di valore pubblico** (Aree Interne italiane), non come prodotto industriale aerospaziale. La filiera del valore è **B1 + B2 + cooperatività territoriale**, non export industriale.
3. **Path EU compatibile**: la visione 10 anni prevede esplicitamente partnership progressive con CIRA, Leonardo, TAS, EuroHAPS-adjacent (vedi `riferimenti/visione-10-anni.md` §2 Fase 3-5). Il presente Studio non si propone come **alternativa antagonista** ai progetti EU esistenti, ma come **nodo italiano specifico** in una possibile architettura EU sovrana multi-orbita.
4. **Boundary condition B2 — linguaggio pubblico**: il posizionamento ufficiale è "**complementare a IRIS²**", **non** "alternativa a Starlink" o "alternativa a EuroHAPS". Questo è scelta strategica esplicita del fondatore e linguaggio da mantenere in ogni interlocuzione con la Commissione UE.
5. **Riconoscimento del limite**: la posizione attuale di Firmamento nell'ecosistema EU non è dichiarata formalmente. Mitigazione: position paper "Italian Stratospheric Layer" da pubblicare entro M+12 (vedi Cap. 5 §5.13 azione richiesta + OQ-CAP1-07).

### Critica R4 (cross-finanziatore): "La strategia duale 6A/6B è davvero risk-reducing, o è una scusa per non scegliere?"

**Critica dettagliata**: un revisore critico potrebbe argomentare che la separazione 6A/6B è una **finte ottimizzazione**: in pratica, si chiedono soldi per due percorsi paralleli (uno operativo, uno R&D di lungo periodo) sperando che almeno uno funzioni. La vera disciplina strategica richiederebbe di scegliere una sola direzione. Mantenere entrambi è **costoso in tempo direzionale**, in capitale di attenzione e in messaggistica verso finanziatori (che possono confondersi sul "cosa stiamo finanziando?").

**Risposta**:

1. La separazione 6A/6B è **rigorosamente disaccoppiata in termini di budget e gate**: il finanziamento Cooding (€XXk per lo Studio) finanzia **solo lo Studio di Fattibilità**, non l'operatività 6A o il R&D 6B. I due percorsi richiedono **fonti di finanziamento diverse**:
   - Percorso 6A: revenue commerciale + LoI Regione Liguria + grant minori FESR/Coopfond Invest;
   - Percorso 6B: grant institutional (PNRR, Horizon, EDF) + venture institutional.
2. La separazione è **risk-reducing** perché: (a) se 6B fallisce, 6A resta come business operativo indipendente; (b) se 6A fallisce, 6B viene rinviato; (c) gli asset di 6A (NOC, customer relationships, regulatory experience) **abilitano** 6B se 6A funziona.
3. **Comunicazione coerente**: il presente Studio dichiara esplicitamente Go Condizionato per 6A e Hold / Go Condizionato Estremo per 6B. La narrativa per finanziatori è: "**finanziate 6A perché è il deliverable operativo; tenete 6B come opzione di crescita di lungo termine, decisa al gate M+24**".
4. **Riconoscimento del limite**: c'è un rischio reale di **dispersione di attenzione** della PMI early-stage Firmamento sui due percorsi. Mitigazione: governance interna con **commitment esplicito di tempo direzionale 80/20 sui due percorsi nei primi 24 mesi** (80% 6A, 20% 6B preparatorio).

### Critica R5 (Coopfond): "Avete davvero base evidenziale, o solo desk research?"

**Critica dettagliata**: il presente capitolo cita estensivamente fonti documentali (PSNAI, D.Lgs. 36/2023, Briefing, istruttoria Liguria, ENAC AAM), ma il **lavoro empirico sul campo** sembra ancora limitato. Le 10 cooperative non sono nominate, l'LoI Regione non c'è, l'engagement ENAC è dichiarato ma non ancora documentato. C'è il rischio che lo Studio risulti **interamente da scrivania**, senza validation esterna.

**Risposta**:

1. **Riconoscimento del fatto**: il presente capitolo è una **bozza M+3**. Il lavoro empirico (engagement esterni) è esplicitamente programmato nei mesi M+3 → M+9 (workshop cooperative, pre-application meeting ENAC, bilateral Regione Liguria, DPIA pubblica, position paper).
2. **Gate M+10 condizionato** all'effettiva chiusura del lavoro empirico: senza LoI Regione Liguria + ≥8 NDA cooperative + pre-application ENAC documentata + workshop accettabilità Pentema, **il gate non è superabile**. Vedi Cap. 3 §3.2 per i criteri specifici.
3. **Audit di rigore epistemico**: gli item residui sono trackati in `riferimenti/audit-rigore-epistemico.md` (DR-001..DR-007). Il documento è strumento di trasparenza verso finanziatori.
4. **Validation esterna formale**: per la presentazione a bandi pubblici, lo Studio può essere sottoposto a **review indipendente** (es. RINA o DNV come ente terzo), come delineato in `riferimenti/analisi-fac-simili-IT.md` §5.

### Verdetto Red Team

Il capitolo è **sostanzialmente robusto** dal punto di vista di inquadramento, ma con le seguenti **azioni esplicite richieste** prima del gate M+10:

- ☐ Formalizzazione governance cooperativa (model definition + commitment) entro M+8 (R1, OQ-CAP1-02)
- ☐ LoI Regione Liguria o equivalente entro M+8 (R2, OQ-CAP1-01)
- ☐ Position paper "Italian Stratospheric Layer" entro M+12 (R3, OQ-CAP1-07)
- ☐ Commitment direzionale 80/20 6A/6B esplicitato in governance interna (R4)
- ☐ Pre-application ENAC documentata + workshop accettabilità Pentema + ≥8 NDA cooperative entro M+9 (R5)

Il Red Team conferma che lo Studio non chiude senza il completamento di queste 5 azioni.

---

## 1.11 Note di chiusura del capitolo

Il presente Capitolo 1 ha la duplice funzione di **inquadramento del progetto** (volume 1 dello Studio di Fattibilità) e di **Quadro Esigenziale formale ex art. 41 D.Lgs. 36/2023** + Allegato I.7 Sezione I[^1]. Tutti i contenuti dell'Allegato I.7 art. 1 sono soddisfatti, con citazioni esplicite alle fonti normative e di programmazione (PSNAI, ENAC AAM, istruttoria Liguria).

Il capitolo non duplica contenuti che sono trattati in maggior dettaglio in altri capitoli dello Studio:

- **Cap. 2** — analisi stakeholder estesa, obiettivi SMART derivati dagli obiettivi OB-01..OB-06 del presente capitolo;
- **Cap. 3** — requisiti dettagliati (StNeeds, SyR, SsR), RTM, criteri di gate;
- **Cap. 4** — perimetro, scope, deliverable, ICD preliminare;
- **Cap. 5** — quadro normativo dettagliato (UAS, U-Space, ENAC, EASA, AGCOM, GDPR, NIS2);
- **Cap. 6** — analisi tecnica (architettura 6A/6B, prestazioni, trade study/DOCFAP, FMECA/FTA, infrastrutture);
- **Cap. 7** — analisi di mercato, business model canvas, MVP, pricing, scale-up;
- **Cap. 8** — analisi economica e finanziaria, NPV/IRR/payback, sensitivity, funding strategy;
- **Cap. 9** — cronoprogramma e gate decisionali (dettaglio M+0 → M+11 e oltre);
- **Cap. 10** — raccomandazione di gate (verdetto Go / Hold / No-Go per ciascuno dei due percorsi);
- **Cap. 11** — roadmap post-fattibilità (Fase 1 → Fase 5 della visione 10 anni).

**Debito di rigore residuo per il Cap. 1** (cross-ref `riferimenti/audit-rigore-epistemico.md`):

- ☐ DR-CAP1-01 — Formalizzazione LoI Regione Liguria sul caso pilota Pentema
- ☐ DR-CAP1-02 — Formalizzazione NDA + LoI con le 10 cooperative Legacoop
- ☐ DR-CAP1-03 — Verifica accettabilità sociale comunità Pentema (workshop + survey)
- ☐ DR-CAP1-04 — Mappa Aree SNAI Liguria 2026 aggiornata (cross-check istruttoria 2022 vs realtà 2026)
- ☐ DR-CAP1-05 — Position paper "Italian Stratospheric Layer" per posizionamento Firmamento nell'ecosistema EU
- ☐ DR-CAP1-06 — Modello formale di governance cooperativa (post-Critica R1 Red Team)

Questi item sono **bloccanti per il gate M+10/M+11**: senza la loro chiusura, il verdetto Go Condizionato 6A non è difendibile davanti a Coopfond + Regione Liguria + revisori UE.

**Prossima revisione**: M+6 post-workshop cooperative + pre-application meeting ENAC + bilateral Regione Liguria. Aggiornamento previsto delle assunzioni e delle Open Questions, con possibile re-baselining del set di criticità C-1..C-8 sulla base dei feedback empirici.

---

> **Boundary conditions check** (riepilogo, coerentemente con la disciplina del progetto):
>
> - **B1** (modello cooperativo + service-only): coerente con §1.1.1, §1.1.2, §1.3.3, §1.5.2 (Percorso 6A revenue ricorrente da servizi, no product sale). ✓
> - **B2** (vettore strategico "EU sovereign stratospheric layer", linguaggio "complementare a IRIS²"): coerente con §1.3, §1.5.2 (Percorso 6B preparatorio), §1.7 (posizionamento ENAC AAM). Linguaggio pubblico mantenuto. ✓

— *Fine Capitolo 1* —
