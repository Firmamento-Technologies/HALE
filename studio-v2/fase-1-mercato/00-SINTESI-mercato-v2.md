# Sintesi Decisionale — Fase 1 Mercato (v2)
### Studio di Fattibilità HALE / Firmamento Technologies — aggiornamento lug-2026 con 9 lenti verificate dal Red Team

---

## 1. Il verdetto in una pagina

**Nessuna delle nicchie downstream analizzate ha oggi un pagatore che FIRMA e paga in modo ricorrente per un servizio aereo di Firmamento.** Questa è la conclusione dirimente, confermata da 9 lenti indipendenti e da 9 verifiche avversariali: la domanda osservata è quasi ovunque *desiderata* (piloti, grant, LoI potenziali), non *domanda pagante contrattualizzata*. Dove esiste un budget vero (dissesto PNRR M2C4 €500M, AIB, Frontex €184M, EMSA), è presidiato in-house dalla PA, va a opere civili, o è aggiudicato ai prime via framework pluriennali.

**I dati 2026 CONFERMANO e RAFFORZANO il verdetto d'archivio (barbell), non lo ribaltano.** Le tre dinamiche 2026 spingono tutte nella stessa direzione:
- **I sostituti gratuiti migliorano:** Copernicus Sentinel-1D (apertura dati 17/04/2026, revisit 6gg), Starlink IT a 29 €/mese con hardware azzerato, OroraTech thermal-sat (alert <3min, contratto Grecia €20M).
- **La PA internalizza:** ARPAL (team droni RTK/multispettrale), CUFAA (SAPR+NIAB), Parchi via PNRR MASE, ARPA Lazio/Umbria/Veneto — il pagatore locale smette di comprare servizi per comprare droni propri.
- **Gli incumbent chiudono i mercati wide-area:** AST/Vodafone "SatCo" D2D dal 2026, Sicral 3 (€767M) + IRIS² per la sovranità emergenza, EMSA/Tekever (€30M) + Frontex/IAI-Airbus (€184M) sul marittimo.

**Il MARITTIMO — le due lenti nuove — NON apre spazio non-conteso.** È lo spazio *più* presidiato e sussidiato del portafoglio: EMSA vola RPAS da Sarzana (Liguria) sul Golfo di Genova, gratis alla Guardia Costiera; l'ispezione cavi/seabed è dominio subacqueo dei prime sovrani (Fincantieri/IDS); la nicchia commerciale (porto/MSC) è desiderata non verificata con volo_necessario=false in 5 servizi su 8. Il marittimo va trattato come **posizionamento narrativo/co-location**, mai come pilastro di ricavo.

**Implicazione prodotto (invariata e rafforzata):** nessun servizio con domanda reale giustifica un **T3-MALE** o **T4-HALE** dedicato. La classe ottimale per l'operatore è **T2-midVTOL / T1-C3 / T0-COTS**, da **COMPRARE non costruire**. L'HALE resta **vettore strategico extra-mercato** (opzione di posizionamento EU/HAPS), da contabilizzare a parte, non come VAN.

**Chi paga davvero, oggi:** i **FONDI** (Coopfond €50k già deliberato, one-shot; FESR R&S) — non clienti di servizio. L'unico candidato-ricavo ricorrente credibile è una **convenzione Regione/Protezione Civile per un DaaS territoriale in bundle** — non firmata, di taglia €100-300k/anno, contesa da sostituti gratuiti. La leva 2026 è **politica, concentrata su un nodo**: l'assessore Piana (Lega, deleghe FESR + blue economy + porti + innovazione).

---

## 2. Ranking di tutte le nicchie

Ordinate per attrattività netta (WTP ricorrente × leva politica × difendibilità × fit modulare × facilità normativa). Nessuna raggiunge "verde": la migliore è "giallo tenue, grant-dipendente".

| # | Nicchia | Chi paga (ricorrente reale) | Verdetto business | Sostituto dominante | Classe prodotto ottimale | Leva politica | Conf. |
|---|---------|------------------------------|-------------------|---------------------|--------------------------|---------------|-------|
| **1** | **EO / monitoraggio territorio-dissesto (aree interne)** | Regione/ARPAL/PC via **grant-convenzione** (one-shot, non ARR) | reale-ma-piccolo-o-conteso → **ridimensionare verso €80-150k** | Copernicus EGMS/S1D **gratis** (migliora 2026) + 675 op. drone COTS | **T0-COTS / T2-midVTOL** | Media (B2G grant-anchored) | Bassa (sizing) |
| **2** | **Protezione Civile / overwatch emergenza episodico** | PC/Prefettura **a-evento** (spot, non abbonamento) | vetrina-o-dominato → **residuo ~€0 ricorrente** | Droni VVF/ARPAL propri + Copernicus EMS gratis | **T0-COTS / T1-C3** | **Alta come narrativa**, nulla come cassa | Alta (fatti) / Bassa (SOM) |
| **3** | **Logistica medicale (sangue/AED/farmaci)** | SSN/ASL/118 — **nessun codice tariffario, solo pilot-grant** | reale-ma-piccolo-o-conteso → **da-ridimensionare (~0 in Liguria)** | Corriere/traghetto (routine, più economico); elisoccorso solo per raro | **T2-midVTOL cargo COTS** (comprare/rivendere ABzero) | Alta apri-porta, sottile su ricavo | Alta (verifica) |
| **4** | **Sorveglianza-sicurezza locale ambientale** | Parchi/ARPA/Comuni — **affidamenti sotto-soglia episodici** | reale-ma-piccolo-o-conteso (solido) | PA **internalizza** (flotte ARPA) + Copernicus + COTS noleggio | **T2-midVTOL COTS** | Media (locale) / nulla (nazionale = prime) | Alta (verifica) |
| **5** | **Connettività NTN / IoT-relay / resilienza** | Nessuno per cella-da-quota; PC "canone prontezza" **inesistente** | reale-ma-piccolo-o-conteso → **residuo ~0 non-grant** | Starlink 29€ + BUL €660M + AST/SatCo D2D 2026 | **T0-COTS** (nodo emergenza/gateway), **mai T3/T4** | Debole (Stato ha scelto satellite) | Media (verifica) |
| **6** | **Marittimo commerciale / blue economy** | Nessun firmatario commerciale; MSC/Cegeno = **lead non verificato** | vetrina-o-dominato → **da-ridimensionare (~€0-100k)** | RINA REMOTE, CCTV/tethered, sensori in-water, surveyor con droni propri | **T2-midVTOL / T1-C3** (nicchia porto) | Reale ma per de-risk, non ricavo | Media/Molto-bassa |
| **7** | **Marittimo security / ambientale (MDA/SAR/oil-spill)** | Agenzie UE che comprano **centralmente e regalano** agli Stati | **vetrina-o-dominato → da-SCARTARE** | **EMSA gratis da Sarzana** + CleanSeaNet + ICEYE SAR; CUI militarizzato | (nessuna costruibile) — T3-MALE dei prime | **Ostile** (territorio Leonardo/Fincantieri) | Alta (verdetto) |

**Lenti trasversali (non nicchie):**
- **Domanda politica-funding** → il "pagatore" vero è il grant one-shot; leva concentrata su Piana (single point of failure); vincolo binding = **cofinanziamento 50% + equity founder, oggi assenti**. Rischio: FESR 1.1.1 "downstream spaziale" richiede dati **satellitari** → possibile inammissibilità di una piattaforma aerea.
- **Competitor-sostituti** → conferma: il sostituto vince strutturalmente; gli "incumbent che hanno vinto" (ABzero) non hanno neanche loro ricorrente firmato → il segmento è **pilot-grant per tutti**, terreno sbagliato per un asset persistente capital-intensive.

---

## 3. Il marittimo cambia il quadro?

**No. Il marittimo non apre nicchie non-contese; conferma il pattern del portafoglio, in forma più severa.**

Le due lenti marittime rispondono alla domanda che il progetto si poneva ("il mare è lo spazio bianco che giustifica la persistenza?") con un **no** documentato su fonti primarie:

1. **Il pagatore premium riceve già il servizio gratis, in casa.** EMSA opera RPAS AR-5 da Sarzana (La Spezia) sul Golfo di Genova a supporto della Guardia Costiera italiana — monitora persino i cetacei del Santuario Pelagos — **offerto a costo zero agli Stati membri** [EMSA id=4774/4928; alta]. Non esiste una linea di budget locale da spiazzare.

2. **Il wide-area è aggiudicato centralmente ai prime.** Framework Tekever-EMSA €30M (2+2 anni), piano Frontex €184M/4y ad Airbus/IAI (Heron), Leonardo Falco EVO come alternativa. Firmamento vi entrerebbe solo come sub-fornitore di consorzio, mai come prime.

3. **Il sostituto satellitare vince sul wide-area ambientale.** CleanSeaNet (oil-spill via Sentinel-1, gratis, immagini <30min), ICEYE SAR (50.000 km²/immagine, ~75% dark vessel non-AIS). Il volo resta solo verifica in-situ, svolta da asset pubblici già posseduti.

4. **Mismatch fisico sull'unica idea a provenienza interna.** "Ispezione cavi/condotte dall'alto" (contatto Gigi/Cegeno-MSC): **una piattaforma aerea non vede sotto la superficie**. L'ispezione reale è ROV/AUV/USV, dominio di Fincantieri/IDS (revenue subacqueo +43,3% a €135M Q1-2026) + Marina Militare/NATO (nave Tritone €53,5M, Agenzia ASAS). È un errore di dominio fisico, non una nicchia.

5. **Geografia disgiunta.** Il caso ship-to-shore ha valore solo nelle grandi rade off-Liguria (Singapore/Rotterdam/Fujairah); nei porti liguri le navi ormeggiano in banchina e la pilotina batte il drone. **Dove c'è il pagatore (MSC globale) non c'è la geografia operabile; dove c'è la Liguria non c'è il caso d'uso.** E Pentema (entroterra montano) è ortogonale al mare.

**L'unica sacca marittima con ricavo ricorrente firmato** (sorveglianza B2G EMSA-like) **non è blue economy commerciale, richiede MALE certificato + seat istituzionale, ed è già presa.** Rischio da presidiare esplicitamente nello Studio: **non gonfiare il TAM marittimo per giustificare Pentema** — clienti, pagatori e geografie sono disgiunti, e un revisore Coopfond/Legacoop che cerca il ponte Pentema↔MSC e non lo trova declasserebbe la credibilità dell'intero documento.

**Uso legittimo del marittimo:** (a) *use-case di modularità payload* (stessa piattaforma, EO/IR intercambiabile); (b) *posizionamento narrativo* verso Piana (Cabina blue economy + DLTM) e ancoraggio a FESR S3 "Tecnologie del mare"; (c) *co-location/LoI* (AdSP, RINA) come segnali di de-risk. **Mai come SAM/SOM nel modello finanziario.**

---

## 4. Le TOP 3 nicchie raccomandate

Premessa onesta: si raccomandano le "meno peggio" di un campo strutturalmente debole. Tutte e tre convergono su **una piattaforma COTS multiservizio in bundle**, non su tre business separati.

### TOP 1 — EO / monitoraggio territorio-dissesto in bundle con emergenza PC (aree interne Liguria)
**Perché:** è l'unico segmento dove (a) il volo aggiunge valore reale (persistenza/on-demand alta-risoluzione che il satellite non dà), (b) esiste un pagatore identificabile (Regione/ARPAL/PC) con missione pubblica e fondi di coesione, (c) c'è fit territoriale forte (rischio idrogeologico Antola-Tigullio, PSNAI). Regge il criterio "fit modulare + più casi d'uso": un DaaS che **orchestra Copernicus gratis + drone COTS on-demand + layer VTOL nelle sole finestre red-flag**.
**Caveat / kill-criteria:**
- **KILL se** a **M+12** non esiste **≥1 convenzione Regione/PC firmata ≥€100k/anno** → il base case (€250-500k) è falsificato, si scende al worst €80-150k, si congela ogni piattaforma dedicata. *Ad oggi: zero convenzioni, zero capitolato ARPAL/SUAR EO ricorrente individuato.*
- **KILL se** DPC replica il modello Grecia (thermal-sat nazionale) → chiude l'early-detection incendi dall'alto (unico moat di persistenza).
- Moat debole: l'orchestrazione è system-integration a competizione diretta con 675 operatori + team PA interni. Il vantaggio è politico-cooperativo (operatore Legacoop credibile), non tecnico.

### TOP 2 — Logistica medicale (sangue/AED/farmaci) come operatore asset-light in partnership
**Perché:** è la **value proposition tecnicamente più genuina** del portafoglio — il sostituto premium (elisoccorso €2.000-7.200/h) NON è gratis e il volo è strutturalmente necessario per isole/valli; evidenza clinica AED forte; ROI politico-sociale altissimo (apri-porta con 118/Regione).
**Caveat / kill-criteria (severi):**
- **Nessun meccanismo di pagamento SSN** (no codice tariffario/DRG) → finanziabile solo come grant/pilota. L'incumbent ABzero, meglio posizionato, dopo anni **non ha alcun capitolato SSN ricorrente**: prova regina che il mercato non ha buyer nemmeno per il leader.
- **Fit Liguria ~nullo:** zero isole abitate; il caso-forte è nazionale multi-regione, off-thesis per un bando ligure.
- **Trappola regolatoria:** scalare rotte-valle = una SORA per rotta (50-200 SORA) → distrugge l'unit economics asset-light.
- **Usare come leva narrativa/demo AED su Pentema, NON proiettare come ARR.** Se perseguita: solo come operatore in partnership su T2 COTS o rivendita ABzero/Wingcopter, mai build custom.

### TOP 3 — Sorveglianza-sicurezza locale ambientale + connettività-resilienza come funzioni SECONDARIE del dimostratore
**Perché:** completano il bundle multiservizio e la narrativa "borgo resiliente" (early-warning + gateway IoT/LoRa frane + nodo comms d'emergenza multi-valle). Massimizzano il criterio "numero casi d'uso sulla stessa piattaforma".
**Caveat / kill-criteria:**
- **Erosione strutturale:** PA internalizza (protocollo Viminale-ENAC droni polizia, flotte ARPA); connettività dominata da Starlink+BUL+SatCo.
- Difendibili **solo in bundle** con EO+emergenza e a finanziamento grant. **Mai value proposition core; nessun payload telecom dedicato T3/T4 giustificabile.**

---

## 5. Menu per i finanziatori

Ogni interlocutore riceve la narrazione allineata alla nicchia che lo attiva. **Regola aurea: al finanziatore-grant si vende R&S/prototipo e missione pubblica; non gli si promette ARR che non esiste.**

| Finanziatore | Nicchia da mettere in vetrina | Narrazione | Cosa NON dire |
|---|---|---|---|
| **Coopfond / Cooding** | (già firmato €50k) rete 10 coop + dimostratore multiservizio aree interne | Mutualità + innovazione cooperativa + resilienza borghi SNAI. È capitale d'avvio one-shot per lo Studio/prototipo. **Verificare apertura ciclo 2026 (DR-002).** | Che il €50k copra hardware/flotta (copre attività intellettuale; gap 5-10x alla prima flotta) |
| **FESR Liguria 1.1.1 / FILSE** | EO+NTN "downstream spaziale per tecnologie del mare + aree interne" | Unisce le **due priorità S3 di Piana** (Tecnologie del mare #1 + Sicurezza #3). MPMI 50% fondo perduto max €150k. Pool incrementato 2→5M. | **VERIFICARE PRIMA:** il bando richiede "dati da sistemi satellitari" → una piattaforma aerea può essere inammissibile. Rischio esclusione tecnica. |
| **Regione Liguria / Protezione Civile / ARPAL** | DaaS territorio + early-detection incendi + overwatch emergenza | Convenzione pluriennale di co-progettazione, complementare a Copernicus/IRIS². Metrica: **LoI + convenzione ≥€100k/anno entro M+12**. | "Resilienza broadband stratosferica sovrana" (confligge con Sicral 3/IRIS² e con RESERVED geopolitico) |
| **Autorità Portuali (AdSP) / MSC** | Security/monitoraggio ambientale portuale + ship-to-shore (pilota) | Pilota co-finanziato (EU Action Plan Drone & Counter-Drone), co-location cooperativa, radicamento ligure. **Convertire il lead Cegeno in LoI/pilota pagato entro M+6.** | Sorveglianza costiera "sovrana" (coperta da EMSA/Frontex, sconfina nel militare) |
| **PNRR-Aero / EDF / Horizon** | HALE come vettore strategico EU/HAPS | Nodo cooperativo di futura infrastruttura sovrana EU HAPS, complementare a IRIS²/Copernicus. Accesso solo indiretto/prime-led o come sub-fornitore di consorzio. | Che sia un ricavo di Fase 1 (è valore-opzione, orizzonte Y6+) |
| **Fondi Blue Economy** | Posizionamento cluster (DLTM + Cabina Piana) | Canale corretto = **FESR S3 "tecnologie del mare" + Interreg Marittimo IT-FR + Horizon**. DLTM come aggregatore/porta d'ingresso. | **NON FEAMPA** (fondo-pesca scoped, €1,1M Liguria, inaccessibile a un servizio aereo — trappola narrativa) |

---

## 6. Handoff alla Fase 2 (trade study prodotto)

Per ciascuna nicchia top: servizio → classi di velivolo da confrontare nel trade study DOCFAP, con requisiti-chiave. **La tensione centrale da risolvere è C3<25kg vs endurance vs payload vs categoria normativa.**

### TOP 1 — EO / monitoraggio territorio
| Servizio | Classi da confrontare | Requisiti-chiave |
|---|---|---|
| Monitoraggio frane fronte attivo + rapid mapping post-evento | **T0-COTS** vs **T2-midVTOL** | Payload EO RGB-stereo + LiDAR/termico; GSD 1-2cm; on-demand (NO persistenza); raggio <10km; Open/Specific category |
| Early-detection incendi finestra red-flag | **T2-midVTOL** (loiter 6-10h) vs T0-COTS in standby | Loitering rilocabile sub-nuvola; LWIR + latenza alert ≤5min; **NON always-on** (utilizzo <10% anno) |
| Gateway IoT/LoRa frane (bundle) | **T0-COTS** / C3 | Gateway LoRa 868MHz; raccolta a campionamento; link budget +24-36dB su decine km |

### TOP 2 — Logistica medicale
| Servizio | Classi da confrontare | Requisiti-chiave |
|---|---|---|
| Trasporto sangue/farmaci rotte valle | **T2-midVTOL cargo** (Wingcopter/CW-30E/ABzero-class) — COMPRARE | Payload 2-6kg; autonomia 40-110km; capsula climatizzata IP tracciata; **profilo sprint point-to-point + VTOL** (opposto a loiter/high-AR) |
| AED-drone risposta arresto cardiaco | **T0-COTS** multirotore pre-posizionato | Corto raggio; risposta <3-4min; integrazione centrale 118 |
| **Esclusi esplicitamente** | ~~T1-box-wing~~ (airframe sbagliato), ~~T4-HALE~~ (assurdo per delivery) | — |

### TOP 3 — Sorveglianza locale + connettività-resilienza (bundle secondario)
| Servizio | Classi da confrontare | Requisiti-chiave |
|---|---|---|
| Antibracconaggio/AIB Parchi + controllo territorio | **T2-midVTOL COTS** | Gimbal EO/IR; loiter 6-10h; decollo da banchina/campo; **buy-not-build** |
| Nodo comms d'emergenza multi-valle | **T0-COTS / T1-C3** (aerostato tethered o VTOL deployable) | Backhaul temporaneo senza SPOF a terra; neutral-host/MOCN (ipotesi critica: nessun MNO ha firmato) |

### Tensioni tra criteri da esplicitare nel trade study
1. **C3<25kg vs endurance 24h vs payload:** i tre vincoli-obiettivo sono in conflitto diretto. Un C3 sotto 25kg non regge simultaneamente 24h di autonomia e un payload multi-sensore pesante. Il trade study deve mostrare la frontiera di Pareto e scegliere il punto (probabilmente: C3<25kg + endurance 6-10h + payload EO leggero modulare, sacrificando la persistenza 24h — che nessun servizio con domanda reale richiede).
2. **Loiter high-AR (box-wing/HALE) vs cargo point-to-point VTOL:** la logistica medicale richiede l'airframe opposto all'EO-persistenza. Una "famiglia modulare" unica che serva entrambi è un'assunzione da **dimostrare**, non da dare per acquisita.
3. **Persistenza vs facilità normativa:** l'overwatch persistente su valle richiede BVLOS/U-Space non ancora di routine (23 autorizzazioni BVLOS IT nel 2023; nuovi requisiti STS da 1-dic-2026 alzano la barriera per operatori piccoli). Il criterio "facilità normativa" penalizza proprio le missioni-persistenza.
4. **T3-MALE / T4-HALE:** confermati **fuori mercato** per ogni servizio a domanda reale. Il loro razionale è extra-mercato (opzione strategica). Il trade study li includa **solo** come scenario "vettore strategico Y6+", non come baseline finanziabile Y1-Y3.

**Raccomandazione di ingresso Fase 2:** confermare la strategia **barbell** — operatore su **T2-midVTOL/T0-COTS comprato** (Percorso 6A, Go Condizionato) + dimostratore R&D come opzione strategica (Percorso 6B, Hold). Il trade study prodotto deve partire da qui, non da un HALE custom.

---

## 7. Confidenza e limiti dichiarati

**Confidenza ALTA (fatti-budget e verdetti qualitativi):** su fonti primarie 2026 verificate — EMSA da Sarzana, Starlink 29€, AST/SatCo, Sicral 3/IRIS², Frontex €184M, ARPAL/CUFAA in-house, PNRR M2C4 €500M, Copernicus S1D, OroraTech Grecia €20M, Coopfond €50k firmato. Il verdetto strutturale ("nessun payer ricorrente; sostituto vince; T3/T4 non giustificati; barbell confermato") **regge a tutte le verifiche avversariali**.

**Confidenza BASSA/MOLTO-BASSA (tutti i sizing SAM/SOM):** sono giudizi d'analista bottom-up, non dati di mercato verificabili — il mercato HAPS/downstream aereo è pre-commerciale (stime 2030 divergono fino a 30x). **Direzione univoca del Red Team: i residui positivi vanno ridimensionati verso il basso, mai al rialzo.** In particolare:
- EO: base case €250-500k → ridimensionare a €80-150k finché non c'è 1 convenzione firmata.
- Connettività: "canone di prontezza" PC e SOM 0-150k → verso ~0 ricorrente non-grant.
- Protezione Civile: SOM €30-60k → verso €0 ricorrente-PC (è grant ri-etichettato).
- Marittimo commerciale: SOM €50-300k → ~€0-100k non-grant.
- Marittimo security: da-scartare come pilastro di ricavo.

**Limiti e gap non colmati (azioni pre-gate):**
1. **Zero LoI/convenzioni firmate** in nessuna nicchia. Metrica di verità unica: convenzione Regione/PC ≥€100k/anno entro M+12.
2. **Vincolo binding finanziario:** cofinanziamento 50% + equity founder + floor equity 10 coop — **oggi assenti dai documenti**. È il vero collo di bottiglia, non la disponibilità di bandi.
3. **Ammissibilità FESR 1.1.1** (aereo vs "dati satellitari") da verificare PRIMA di impostare la strategia funding.
4. **Contatto MSC/Cegeno** è desiderata: convertire in LoI/pilota pagato entro M+6 o trattare come inesistente.
5. **Apertura ciclo Cooding 2026** (DR-002) da confermare con Coopfond.
6. **Single point of failure politico:** l'intera leva 2026 poggia su un assessore (Piana). Da diversificare.

**Nota metodologica:** ogni cifra citata è tracciata [fatto|stima; fonte; confidenza] nelle 9 analisi sorgenti. La disciplina `epistemic-rigor` è rispettata: domanda reale (overwatch spot + rapid-mapping, commoditizzati) rigorosamente distinta dai desiderata (early-warning persistente, connettività emergenza, cavi-dall'alto — senza pagatore). **Il capitolo mercato NON si chiude con il marittimo come "scoperta devastante ad alta confidenza" (fonti EMSA/TED non verificate in primaria, confidenza reale = media), ma con "assenza di payer ricorrente in tutto il portafoglio, confidenza alta" come tesi portante, e il marittimo come conferma a media confidenza.**

*File di destinazione: `studio-v2/fase-1-mercato/00-SINTESI-mercato-v2.md`*
