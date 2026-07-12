# Fase A — Analisi di Mercato del Downstream (output preliminare Deep Research)

| | |
|---|---|
| **Progetto** | H.A.L.E. / Piattaforma aerea per servizi al territorio — Firmamento Technologies |
| **Documento** | Output Fase A (WP-A1/A2/A4–A6) — analisi di mercato del downstream |
| **Data** | 2026-07-12 |
| **Metodo** | Deep research harness: 5 angoli di ricerca → 24 fonti scaricate → 43 affermazioni estratte → 25 verificate (verifica avversariale 3 voti) → **24 confermate, 1 confutata** → 12 findings dopo sintesi |
| **Stato** | Preliminare. I dati vanno triangolati; le lacune (§9) sono da colmare con una seconda passata mirata |

> **Nota di lettura.** Ogni dato riporta la **confidenza** assegnata dalla verifica (alta / media) e la fonte. Molte pagine dei report proprietari (Grand View, trade.gov, EUSPA) hanno restituito errori HTTP 403: diverse verifiche si appoggiano a snippet dei motori di ricerca + comunicati primari, non al testo integrale. Trattare le cifre di mercato come **direzionali**, non puntuali.

---

## 0. Messaggio chiave (executive summary)

1. **Il mercato dei servizi downstream da droni è ampio e in crescita solida**, ma il segmento professionale italiano è ancora piccolo (~€160 mln nel 2024) e **in consolidamento** (operatori in calo): il valore non sta nel "fare il service provider generico", ma nel presidiare una **nicchia ad alta willingness-to-pay**.

2. **La nicchia con la domanda pubblica più chiara, già finanziata e ricorrente è quella MARITTIMA/costiera istituzionale.** L'agenzia europea **EMSA** compra servizi RPAS "as-a-service" in modo centralizzato e li eroga **gratis** agli Stati membri, con **contratti quadro da ~30 mln EUR ciascuno nel 2025** (Airbus Flexrotor, TEKEVER AR5) e il rinnovo Frontex/Heron. Modello puro **data-as-a-service**: l'agenzia **non compra il velivolo**, compra il dato.

3. **Lead strategico per la Liguria:** tra i risultati compare un servizio EMSA RPAS **operativo sul Golfo di Genova** a supporto della Guardia Costiera italiana (AR-5 Evo, consorzio REACT = CLS + Tekever). Se confermato, significa **domanda marittima già finanziata nel nostro territorio** → sia opportunità sia concorrente in casa. **DA VERIFICARE come priorità** (§9).

4. **Il benchmark tecnico valida l'ipotesi C3 < 25 kg.** Le piattaforme che vincono i contratti EMSA sono nella classe **~25 kg** (Flexrotor: 25 kg VTOL, payload 8 kg, endurance 10–14 h) o MALE ala fissa (AR5: 12 h, max 20 h). Il velivolo ipotizzato dal gruppo (C3 < 25 kg, alta endurance) è **direttamente confrontabile** con i sistemi già in servizio.

5. **Strategia "ancora politica → scala di mercato" (prodotto multi-ruolo).** Le due direttrici **non sono in competizione ma in sequenza**. Le **aree interne / SNAI** sono l'**ancora**: è la domanda che ha **già fatto ottenere il bando**, con spinta politica, sito pilota e accesso a **fondi pubblici non diluitivi** — il suo valore è **legittimazione + funding + primo cliente captive**, *non* la dimensione di mercato. Il **marittimo** è il **mercato di scala**: domanda pubblica ricorrente e finanziata (modello EMSA ~30 mln EUR/contratto). Un **prodotto multi-ruolo modulare (C3 < 25 kg)** aggancia l'interesse politico per raccogliere fondi e poi scala sul mercato. → **Nota metodologica:** misurare l'ancora con la metrica *sbagliata* (TAM di mercato) la fa sembrare "debole"; la metrica giusta è la **spesa pubblica attivabile** (§9, lacuna 2), che è la vera priorità della seconda passata.

---

## 1. Dimensionamento del mercato (TAM / SAM / SOM)

| Livello | Cifra | CAGR | Anno | Confidenza | Fonte |
|---|---|---|---|---|---|
| **TAM globale** — mercato civile droni | 44,4 mld USD → **83,0 mld USD** (2035) | 7,2% | 2026→2035 | **Alta** (3-0) | DRONEII, *Global Drone Market Report 2026-2035* |
| **SAM Europa** — droni commerciali | 7,63 mld USD → **12,96 mld USD** (2030) | 9,3% | 2024→2030 | Media (3-0) | Grand View Research |
| **SAM/SOM Italia** — professionale B2B/B2G | **~160 mln EUR** (~188 mln USD) | +10% YoY | 2024 | Media (2-1) | trade.gov / Osservatorio Polimi |
| Italia — combinato droni + AAM (più ampio) | >700 mln USD (2025) → 1,73 mld USD (2030) | ~20% | 2025→2030 | Media (2-1) | trade.gov / PwC |

**Note critiche:**
- Lo scope DRONEII "civil" include il **dual-use del settore pubblico** (polizia, antincendio, emergenza sanitaria) — cioè proprio i casi d'uso aree interne/protezione civile del progetto. L'Italia **non** è tra i deep-dive nazionali del report.
- Il "combinato droni + AAM" (1,73 mld USD) **sovrastima** il solo downstream servizi perché include eVTOL/taxi volanti (speculativi) e difesa/cargo. La proiezione 2030 PwC è stata **rivista al ribasso** tra edizioni. Da usare come ordine di grandezza, non come target.
- **Il segmento commerciale "non-consumer a 54,6 mld USD entro il 2030" è stato CONFUTATO** dalla verifica (voto 1-2): non usarlo.

**Struttura competitiva Italia (confidenza alta, 3-0):** operatori professionali ~**657 nel 2024** (da 664 nel 2023, 706 nel 2022), **in consolidamento** (uscite ~5%/anno, ingressi ~2%/anno, soprattutto piccoli player). Le **operazioni aeree valgono ~96%** del valore di mercato; il professionale tradizionale è concentrato su **ispezione, monitoraggio e mappatura**; l'espansione più rapida è trainata dal **settore pubblico** e da infrastrutture/logistica.

---

## 2. Segmentazione e struttura della domanda

La ricerca conferma la centralità della **domanda pubblico-istituzionale** come driver di crescita. Sui singoli segmenti terrestri (antincendio, dissesto, agricoltura di precisione, connettività, ispezione infrastrutture) **non è sopravvissuta alcuna cifra TAM/SAM verificata** → vedi lacuna §9. Il quadro qualitativo per segmento (cliente pagante, requisiti impliciti) resta quello impostato nel Piano di Lavoro (WP-A1) e va riempito con dati nella seconda passata.

Segmenti dove l'evidenza economica è **forte e verificata**: **sorveglianza marittima/costiera, SAR, controllo pesca, monitoraggio ambientale marino** (canale EMSA/Frontex — §3).

---

## 3. Il dominio marittimo — la nicchia a domanda pubblica più chiara

Questa è la scoperta principale della ricerca ed è dove Gigi aveva ragione a chiedere "pari profondità".

### 3.1 Il modello EMSA (confidenza alta, 3-0)
- **EMSA** (Agenzia europea per la sicurezza marittima) eroga servizi RPAS di sorveglianza **gratuitamente** a Stati membri UE, Paesi candidati ed EFTA. **Chi paga il fornitore è l'agenzia UE centrale** (EMSA come *Entrusted Entity* nel Copernicus Contribution Agreement 2021-2028), non il singolo Stato.
- Il pacchetto include **velivolo, pilotaggio, comunicazioni e disseminazione dati**. Modello **procurement-a-servizio finanziato centralmente**, non pay-per-mission al cliente finale.
- Copertura: per le **autorità nazionali** → inquinamento marino, monitoraggio emissioni, **SAR**; per le **agenzie europee** → pesca illegale (EFCA), anti-narcotraffico, immigrazione/confini (Frontex). Supporta **>20 autorità nazionali** + EFCA.

### 3.2 Willingness-to-pay pubblica — data point 2024-2025 (confidenza alta, 3-0)
| Committente | Fornitore / piattaforma | Valore | Data | Modello |
|---|---|---|---|---|
| EMSA | **Airbus Flexrotor** (VTOL), operatore terzo Extensee | **~30 mln EUR** (2 anni, est. a 4) | dic 2025, avvio 2026 | RPAS/DaaS |
| EMSA | **TEKEVER AR5** (ala fissa MALE) | **~30 mln EUR** (2+2 anni, 2 sistemi) | nov 2025 | RPAS/DaaS |
| Frontex | **Heron** (Airbus DS + IAI), Mediterraneo | rinnovo 4 anni | annuncio dic 2024 | RPAS/DaaS |

> Ordine di grandezza: **~30 mln EUR per contratto quadro pluriennale**. ⚠️ Sono **tetti di contratto quadro**, non spesa confermata; le operazioni di volo sono spesso **subappaltate** a fornitori terzi.

### 3.3 Servizio e payload tipo (confidenza alta, 3-0)
Il servizio consiste in **imagery EO/IR + dati radar in tempo reale** all'EMSA RPAS Data Centre, seguibili live dalle autorità nazionali. Il fornitore **opera la piattaforma e consegna il dato, non vende il velivolo**. Payload: **EO/IR + radar** (l'AR5 aggiunge AIS, SATCOM, EPIRB).

### 3.4 Lead Liguria — DA VERIFICARE (priorità alta)
Tra i risultati di ricerca (fonte primaria EMSA, pagina non scaricabile → **non confermato**): un servizio EMSA RPAS **sul Golfo di Genova** a supporto della **Guardia Costiera italiana**, con **AR-5 Evo** e consorzio **REACT (CLS + Tekever)**. Se confermato è la prova di **domanda marittima già finanziata sul territorio ligure** — da chiarire subito con i contatti Cegeno/porto e verso EMSA/Guardia Costiera.

---

## 4. Analisi competitiva — benchmark piattaforme (input Fase B)

| Piattaforma | Tipo | MTOW | Payload | Endurance | Note (confidenza) |
|---|---|---|---|---|---|
| **Airbus Flexrotor** | VTOL | **25 kg** | 8 kg | 12–14 h (10 h config EMSA) | Decollo/recupero autonomo in 3,7×3,7 m; ceiling ~21.000 ft. **Confrontabile 1:1 con HALE C3 <25 kg** (alta) |
| **TEKEVER AR5** | Ala fissa MALE | tattico | EO/IR+radar+AIS | 12 h (max 20 h), SATCOM | Vincitore EMSA nov 2025 (alta) |
| EMSA — 3 tipologie in uso | mix | — | — | Hermes 900 >12 h; Skeldar V-200 VTOL >4 h/>50 km; Indago2 VTOL leggero | Taxonomia persistenza×taglia (alta) |
| **Airbus Zephyr 8** (HAPS) | Ala fissa solare stratosferica | ~60–75 kg | **solo ~5 kg** (frazione ~8%) | settimane/mesi | Payload fraction molto bassa → vincola i sensori. Attività scorporata in **AALTO HAPS** (media) |

**Implicazioni:**
- Gli **incumbent nel marittimo** sono Airbus (Flexrotor + Heron), TEKEVER, IAI: player grandi, ben finanziati. Lo spazio per un nuovo entrante è come **service provider di nicchia / subappaltatore / operatore locale**, non come sfidante frontale.
- Il benchmark **HAPS (Zephyr)** conferma quanto già visto nella 1ª ricerca: payload fraction bassissima, complessità alta. **Rafforza la scelta di un C3 < 25 kg** rispetto all'HALE stratosferico "puro".
- **Make-vs-buy** resta domanda aperta (§9): integrare una piattaforma commerciale (Flexrotor/AR5) come service provider vs costruire un velivolo proprio.

---

## 5. Modelli di business e pricing

- **Modello dominante nel pubblico marittimo: data-as-a-service finanziato centralmente.** EMSA compra il dato, non il mezzo; il fornitore opera la piattaforma. Massimizza ricavi ricorrenti e riduce il rischio d'asset per il cliente.
- **Pricing:** i soli data point robusti sono i **contratti quadro EMSA ~30 mln EUR** pluriennali. **Non è stato quantificato** il prezzo unitario (ora di volo, pay-per-mission, canone annuo, €/km² monitorato) → lacuna §9.
- **Per gli investitori**, il modello a servizio/DaaS con committente pubblico ricorrente (EMSA/Frontex/Regioni) è più attrattivo della vendita spot, perché genera **backlog contrattuale pluriennale** — coerente con la scelta "servizi > vendita del mezzo" già fatta dal gruppo.

---

## 6. Abilitatori normativi

- **Primo spazio aereo U-space d'Europa** attivato in **Italia** (San Salvo, prov. Chieti, Abruzzo), zona geofenced R100 via NOTAM/AIP ENAV, attiva dal **28 nov 2024**; abilita operazioni complesse incluse **BVLOS** (confidenza media, 2-1).
- ⚠️ **Caveat importante:** la prontezza *operativa/di business* è risultata fragile (Amazon Prime Air si è ritirata poco prima del lancio operativo di inizio 2026 — "sobering lessons of San Salvo"). Il **milestone regolatorio è valido**; il modello di business BVLOS su aree interne **non è ancora provato sul campo**.

---

## 7. Profili di missione benchmark → input per la Fase B

Griglia di confronto derivata dai sistemi realmente in servizio (per WP-B1/B2/B3):

| Parametro | Marittimo istituzionale (EMSA-like) | HAPS connettività (Zephyr-like) |
|---|---|---|
| Classe/peso | ~25 kg (VTOL) o MALE ala fissa | ~60–75 kg, stratosferico |
| Payload | 8 kg (EO/IR + radar) | ~5 kg (comms) |
| Endurance | 10–14 h (fino a 20 h) | settimane/mesi |
| Quota | fino a ~21.000 ft | ~20 km |
| Dato | EO/IR + radar, streaming real-time | relay connettività |
| Latenza | bassa (real-time al Data Centre) | bassa |

→ **Il profilo "marittimo ~25 kg, 10–14 h, EO/IR+radar" è il target-benchmark più concreto e finanziato**, ed è quello su cui il velivolo C3 < 25 kg del gruppo va confrontato nella Fase B.

---

## 8. Shortlist nicchie prioritarie (tesi di valore)

| # | Nicchia | Tesi di valore | Evidenza | Confidenza domanda |
|---|---|---|---|---|
| **N1** | **Sorveglianza marittima/costiera istituzionale** (SAR, pesca, ambiente, confini) | Domanda pubblica ricorrente e finanziata centralmente (EMSA/Frontex); lead sul Golfo di Genova; benchmark ~25 kg valida l'architettura | Forte (verificata) | **Alta** |
| **N2** | **Monitoraggio ambientale marino** (sversamenti, plastica, emissioni) | Sotto-segmento di N1, stessa piattaforma/payload; leva ESG e fondi UE | Media | Media |
| **N3** | **Aree interne — connettività, monitoraggio, emergenze/protezione civile** (ancora del progetto) | **Ancora politica e di funding**: ha già ottenuto il bando; sito pilota, sponsorship Regione/Legacoop/SNAI, **fondi pubblici non diluitivi**; U-space IT come abilitatore. Da misurare con la **spesa pubblica attivabile**, non con il TAM | Politica/funding **forte**; dimensione di mercato non quantificata | **Alta (funding/politica)** |
| **N4** | **Ispezione infrastrutture critiche** (energia, coste, offshore) | Mercato B2B maturo, willingness-to-pay privata | Non quantificata | Da valutare |

> **Raccomandazione preliminare — strategia "ancora → scala":** **N3 (aree interne) è l'ancora** che porta bando, spinta politica e fondi pubblici; **N1 (marittimo) è il mercato di scala** con willingness-to-pay ricorrente. La strategia vincente è **un prodotto multi-ruolo modulare (C3 < 25 kg)**: stesso velivolo, payload intercambiabili, che aggancia l'interesse politico (N3) per raccogliere fondi e poi scala sul mercato (N1). Questo **risolve di fatto la domanda "generalista vs specializzati" (WP-B7)** a favore di una **piattaforma comune modulare** — né due velivoli separati né un "barcone" indifferenziato.

---

## 9. Lacune ed evidenze da completare (seconda passata mirata)

La ricerca ha prodotto evidenza forte su marittimo istituzionale + dimensionamento aggregato, ma **restano lacune** da colmare prima di chiudere la Fase A:

1. **TAM/SAM quantitativo dei segmenti terrestri** prioritari (antincendio boschivo, dissesto/alluvioni, agricoltura di precisione, ispezione infrastrutture, connettività backhaul/IoT-LoRaWAN) — Italia/Liguria/UE. *Nessun dato segmentato è sopravvissuto alla verifica.*
2. **Spesa pubblica italiana attivabile**: fondi SNAI/PSNAI, misure PNRR pertinenti (dissesto ~8,5 mld EUR iniziali, poi rimodulati), dotazioni Protezione Civile nazionale/Regione Liguria, schemi PPP/cooperative Legacoop → per dimensionare il **SOM pubblico**.
3. **Prezzi unitari reali** nel downstream (€/ora di volo, pay-per-mission, canone DaaS, €/km²) oltre agli ordini di grandezza dei contratti quadro EMSA.
4. **Mercato cavi sottomarini/energia offshore e monitoraggio ambientale marino** nel Mediterraneo, e **chi paga** (operatori cavi/energia, autorità portuali, MSC/shipping) oltre alle agenzie UE.
5. **Economia make-vs-buy** (integrare Flexrotor/AR5 come service provider vs costruire) e **spazi non presidiati** dagli incumbent (Airbus/AALTO, TEKEVER, IAI).
6. **VERIFICA PRIORITARIA del lead Golfo di Genova** (EMSA/AR-5 Evo/REACT/Guardia Costiera) — potenziale domanda finanziata sul territorio.

---

## 10. Implicazioni per il progetto e ponte verso la Fase B

- **Impostare la strategia "ancora → scala":** N3 (aree interne) come **ancora** politica e di funding che finanzia il primo velivolo/pilota; N1 (marittimo) come **mercato di scala** che ne sostiene la crescita; **un unico prodotto multi-ruolo modulare C3 < 25 kg** a fare da ponte. Usare N1 come benchmark tecnico-economico nella Fase B.
- **Il vincolo C3 < 25 kg del gruppo è validato dal mercato**: i sistemi che vincono i contratti pubblici marittimi sono proprio in quella classe. La Fase B deve verificare se un C3 proprietario può competere su endurance/payload con Flexrotor/AR5 (WP-B3), o se conviene **integrare** una piattaforma commerciale (make-vs-buy, WP-B2/B5).
- **Il modello data-as-a-service** con committente pubblico ricorrente è la via più attrattiva per gli investitori → alimenta WP-A6/C2.
- **Prossimo passo operativo:** lanciare la **seconda passata di ricerca** sulle 6 lacune di §9 (in particolare segmenti terrestri quantificati, spesa pubblica IT attivabile e verifica del lead ligure), poi chiudere il Market Analysis Report e aprire la Fase B.

---

## Fonti (verificate)

- **DRONEII**, *Global Drone Market Report 2026-2035* — TAM globale — https://droneii.com/product/drone-market-report
- **Grand View Research**, *Europe Commercial Drone Market* — SAM Europa — https://www.grandviewresearch.com/industry-analysis/europe-commercial-drone-market-report
- **trade.gov (US ITA)** / Osservatorio Droni Politecnico di Milano — mercato Italia — https://www.trade.gov/market-intelligence/italy-civil-drone-market
- **EMSA**, *RPAS surveillance services* — modello e segmenti marittimi — https://www.emsa.europa.eu/we-do/surveillance/rpas.html
- **EMSA / Golfo di Genova** (da verificare) — https://emsa.europa.eu/thetis-mrv/items.html?cid=2&id=4928
- Contratto **Airbus Flexrotor** EMSA — https://aviationnews.eu/news/2025/12/airbus-wins-e30-million-emsa-contract-for-flexrotor-maritime-surveillance-services/ · https://www.unmannedsystemstechnology.com/2026/01/emsa-selects-airbus-flexrotor-for-enhanced-maritime-surveillance-coast-guard-support/
- Contratto **TEKEVER AR5** EMSA — https://www.unmannedsystemstechnology.com/2025/11/tekever-secures-emsa-agreement-for-ar5-fixed-wing-uas-deployment/
- Rinnovo **Frontex/Heron** — https://euro-sd.com/2025/01/major-news/41918/frontex-heron-ops-continue/
- **Airbus Zephyr / AALTO HAPS** — https://en.wikipedia.org/wiki/Airbus_Zephyr · https://www.airforce-technology.com/projects/zephyr-s-high-altitude-pseudo-satellite-haps/

*Fonti richieste ma non scaricabili in questa passata (403/blocco), da recuperare: EUSPA EO & GNSS Market Report; PSNAI (politichecoesione.governo.it); Regione Liguria SNAI; PNRR Protezione Civile.*

---

*Output preliminare della Fase A. Confidenze e caveat come da verifica avversariale del deep research harness (24 claim confermati / 1 confutato su 25 verificati). Le cifre di mercato sono direzionali: triangolare prima di usarle nello Studio di Fattibilità.*
