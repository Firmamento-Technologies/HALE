# R3 — Costi Piattaforma, Prezzi COTS e Certificazione: Verifica Avversariale con Fonti Reali

> **Firmamento Technologies S.r.l.**, Progetto HALE, Ricerca Approfondita — Percorso 6A
> **Data:** luglio 2026 | **Owner:** ricerca avversariale su claim dei report `05`, `10`, `21`, `23` (`analisi-bottom-up/`)
> **Metodologia:** WebSearch estensivo (60+ query mirate su 5 filoni, tramite 5 agenti paralleli + ricerca diretta di sintesi) + verifica incrociata multi-fonte. **WebFetch/curl risultati bloccati per l'intera sessione da policy di rete dell'ambiente (HTTP 403 su CONNECT verso praticamente ogni dominio esterno testato, incl. TED, EASA, ENAC, Wikipedia, CNBC — confermato dal log del proxy `/root/.ccr/README.md` e riprodotto indipendentemente da tutti e 5 gli agenti).** Tutti i dati sotto derivano quindi da **sintesi del motore WebSearch** (che opera su un canale non soggetto allo stesso blocco), non da lettura diretta di pagina/PDF integrale — dichiarato esplicitamente in ogni fonte salvata. Dove possibile, ogni cifra è triangolata su 2+ fonti indipendenti; dove non lo è, è segnalato come single-source.
> **Fonti salvate:** 29 file pertinenti al mandato in `/home/user/HALE/ricerca-approfondita/fonti/` (elenco completo in fondo). Altri ~76 file nella stessa cartella appartengono a filoni di ricerca paralleli/diversi (competitor intelligence, aerodinamica box-wing, mercato HALE stratosferico) condotti da altre sessioni concorrenti sullo stesso repository e **non fanno parte di questo report**.

---

## 0. Executive summary (verdetti in una riga)

| # | Claim originale | Verdetto | Confidenza aggiornata |
|---|---|---|---|
| 1a | WingtraOne GEN II ~€27-29k | **Confermato**, ordine di grandezza corretto (reale €30-37k IVA escl. da 2 tender pubblici UK) | bassa→**media-alta** |
| 1b | Quantum Trinity F90+ ~€17k | **Superato**: successore Trinity Pro attivo, prezzo reale €17-26k (range più ampio) | bassa→**media** |
| 1c | JOUAV CW-30E/CW-15 "no listino pubblico" | **Confermato** (assenza sistematica su 8+ canali) + **nuovo rischio**: JOUAV in lista DOD 1260H, bandita da procurement USA da dic-2025 | bassa (invariata su prezzo), **nuovo rischio da aggiungere** |
| 1d | Threod Stream C "no listino pubblico" | **Confermato**, nessun dato nuovo | bassa (invariata) |
| 1e | Fascia T0 "€40-120k" | **Confermato/rafforzato** | media→**media-alta** |
| 1f | Fascia T2 "€0,8-1,8M" | **Non falsificato ma nemmeno confermato** — nessuna evidenza pubblica trovata | bassa (invariata) |
| 2 | Contratto EMSA-Tekever "€30-35M/4 anni ≈ €7,5-8,75M/anno" | **Parzialmente corretto ma fuorviante**: è €30M (non un range), 2 anni fermi + opzione fino a 4, quindi il costo/anno implicito varia €7,5-15M/anno a seconda dello scenario di esercizio delle opzioni | media (era già "high" nel report 05, ora declassata a **media**, va corretta la derivazione) |
| 3 | Sviluppo box-wing C3 certificato serie "€3-10M+" | **Non smentito, ora corroborato da una fonte istituzionale reale (non VC-proxy)**: grant CORDIS WingtraOne €3,54M per la sola fase di industrializzazione di un drone già maturo | low-medium→**medium** |
| 4a | "C-marking assessment €9-25k" (non tracciato) | **Rintracciato**: fonte reale ma single-source (EU Drone Port, un solo Notified Body commerciale), copre solo la fee di assessment, non il costo totale di conformità | non tracciato→**media (ma parziale/ottimistica)** |
| 4b | EASA Design Verification Report / Type Certificate | **Nuovo dato reale**: DVR = €250/ora EASA, fino a ~€45k/anno per progetto "tipico"; **nessun UAS ha mai ottenuto un Type Certificate EASA pieno** (luglio 2026) — qualunque cifra di TC pieno resta teorica | n/d→**alta sul DVR, non applicabile sul TC pieno (nessun precedente)** |
| 5 | Costo/tempo BVLOS SORA Italia (nessun claim pregresso) | **Nuovo benchmark**: tariffa ENAC fissa €355 (bassa, irrilevante), istruttoria 15-45 gg lavorativi; costo di consulenza **nessun listino pubblico in Italia/UE** — proxy UK CAA per SAIL II-III: £3.806-10.380 (~€4.400-12.000) di sola fee regolatoria | n/d→**media sul proxy UK, bassa sulla trasferibilità a ENAC** |

---

## 1. Prezzi reali COTS VTOL/fixed-wing

### 1.1 Tabella claim → fonte → verdetto

| Claim (report 05/10) | Fonte trovata (URL) | Verdetto | Confidenza |
|---|---|---|---|
| WingtraOne GEN II $29.000 (fonte: blog Robotomated) | UK Find a Tender (equivalente britannico di TED), notice **UKRI-5251**, fornitore **Korec**, **£30.947,64 IVA escl. / £37.137,17 IVA incl.**, firmato 24/09/2025 — https://www.find-tender.service.gov.uk/Notice/060190-2025/PDF ; secondo riscontro: tender Ulster Wildlife Trust, stima **£35.000** | **Confermato**, +20-30% vs stima originale | **media-alta** (2 notice di appalto pubblico britannico indipendenti, stessa categoria evidenziale di TED ma non TED/UE) |
| Quantum Trinity F90+ ~$18.300 (datasheet PDF 2023) | Rivenditori USA multipli: measur.ca ($28.550), dronenerds.com, comunicato ufficiale Quantum Systems Series D 2/7/2026 (conferma segmento civile attivo) | **Aggiornato**: Trinity F90+ superato dal successore **Trinity Pro** (lanciato maggio 2023, MTOW 5,75kg, 90+ min, 700 ha/volo), prezzo reale $23.800-28.550 | **media** (nessun listino ufficiale fetchato, solo rivenditori terzi, ma convergenti) |
| JOUAV CW-30E/CW-15 "nessun prezzo pubblico" | 8 rivenditori/distributori distinti (mach-sales/SUMEC, geo-matching, druav, pusatdrone Indonesia, airframer) tutti "price negotiable"/"contact for quote" | **Confermato** con alta confidenza (pattern negativo ripetuto su 8 canali indipendenti) | **alta sul "non trovato"**, resta stima interna non falsificabile |
| — (nuovo, non nel claim originale) | American Security Drone Act / lista **DOD 1260H**: da **22 dicembre 2025** procurement federale USA vieta droni JOUAV; interrogazione Europarlamento (P-10-2025-003323) valuta misure UE analoghe (non ancora in vigore) | **Nuovo rischio regolatorio concreto**, non presente nei report interni | alta sull'esistenza del rischio, incerta la tempistica UE |
| Threod Stream C "no listino pubblico, stima €500k-1,5M+" | 6 fonti dedicate Stream C, nessun prezzo; contratto adiacente reale (lanciatori CATA, UK MoD, £4.996.500/$6,6M, marzo 2026) — **prodotto diverso**, non Stream C | **Non trovato, resta stima** | bassa (invariata) |
| — (nuovo) Delair DT18/DT26 | Fonte radice L'Usine Nouvelle, **maggio 2013**: DT18 ~€30.000, DT26 ~€100.000; abbonamento UX11 "Delair Takeoff" €1.250/mese (dato 2019) | **Dati reali ma obsoleti di 7-13 anni**, non rappresentativi del 2026 | bassa (obsolescenza esplicita) |
| — (nuovo) Delair contesto | BOAMP (Bollettino appalti pubblici francese) notice 20-51423 (2020), Ministero Interno francese, **€3,795M totale multi-lotto** (micro-drone €3.185/u, drone "capacità nazionale" €23.939/u) — **aggiudicatario 2021 non confermato come Delair** | Dato di mercato reale ma **non attribuibile con certezza a Delair** | bassa-media (gap di attribuzione dichiarato) |

### 1.2 Verdetto sulle due fasce aggregate del mandato

- **Fascia T0 "€40-120k sistema completo"**: **confermata e rafforzata**. WingtraOne GEN II da solo (bare kit, IVA esclusa) è già a ~€30-37k da due tender pubblici reali; un sistema completo con payload avanzato/training/formazione si colloca plausibilmente nella metà superiore del range. Confidence aggiornata: **media-alta** (era media).
- **Fascia T2 "€0,8-1,8M sistema completo" (JOUAV CW-30E-class / Threod Stream C)**: **nessuna nuova evidenza, né a favore né contro**. Dopo ricerca estesa (30+ query mirate su entrambi i vendor), **nessun prezzo pubblico è emerso** per nessuno dei due riferimenti di mercato usati per calibrare questa fascia. Resta una **stima interna non verificabile con fonti pubbliche disponibili**, confidence **bassa invariata**. Azione raccomandata: RFQ diretta a JOUAV (tramite reseller EU, es. MARIDS Spagna) e Threod Systems — unico modo per ottenere un dato reale.

---

## 2. Contratto EMSA–Tekever (valore reale del servizio MALE-as-a-Service)

### 2.1 Tabella

| Claim (report 05) | Fonte trovata (URL) | Verdetto | Confidenza |
|---|---|---|---|
| "€30-35M / fino 4 anni / 2 sistemi × 2 UAS (4 velivoli), RPAS-as-a-Service" | defence-industry.eu, AI Business, ASD News, Portugal Startup News, ADS Advance — tutte convergenti su **€30 milioni** (non un range €30-35M) | **Parzialmente corretto, semplificazione fuorviante** | media (triangolato da fonti secondarie convergenti, non da TED/EMSA primario — accesso bloccato in questa sessione) |
| Componente "$35M" | UAS Vision (titolo in USD) | **Chiarito**: $35M è la STESSA cifra €30M convertita in USD dal titolo di una testata, non un valore superiore indipendente | il "range €30-35M" del report interno va corretto a "**€30M, cifra singola**" |
| "fino 4 anni" | Stesse fonti | **Corretto ma da qualificare**: struttura reale = **2 anni fermi + opzioni fino a 4 anni totali** (non 4 anni garantiti) | media |
| "2 sistemi × 2 UAS (4 velivoli totali)" | Stesse fonti, ripetuto identico su 6 testate | **Confermato** | media-alta |
| "≈€7,5-8,75M/anno" (derivazione lineare) | — | **Da correggere**: se si contano solo i 2 anni fermi, il costo/anno implicito è **€15M/anno** (il doppio); se si esercitano tutte le opzioni fino a 4 anni, **€7,5M/anno**. Il framework contract è inoltre un **tetto massimo**, non spesa garantita/lineare, con copertura multi-paese (Italia, Spagna, Francia, Baltico) probabilmente ad attivazione scaglionata | **bassa sulla derivazione lineare specifica**, il range corretto da usare è **€7,5-15M/anno a seconda dello scenario** |

### 2.2 Scoperta aggiuntiva rilevante

Il rapporto EMSA-Tekever/CLS (consorzio "REACT") **non è un evento isolato**: esiste almeno un contratto quasi identico nell'**ottobre 2021** ("four-year contract, maximum budget €30M" — Naval News, Army Recognition), che sostituiva un primo accordo del 2018. **Nello stesso trimestre (nov-dic 2025), Airbus ha vinto un contratto EMSA separato da altrettanti €30M** per Flexrotor, e Schiebel un altro contratto multi-anno a gennaio 2025 — pattern che suggerisce **€30M/2-4 anni sia una soglia di budget-quadro EMSA standard per questa categoria di lotto RPAS marittimo**, non un "prezzo di mercato aperto" scoperto specificamente per l'AR5 di Tekever. Questo è un dato utile per la strategia di posizionamento Firmamento: **il benchmark "vero" per un servizio MALE persistente multi-sito europeo con equipaggio è ~€7,5-15M/anno**, un ordine di grandezza sopra qualsiasi scenario realistico per il solo pilota Pentema.

**Raccomandazione:** correggere il file `05-piattaforme-costi.md` §6 da "€30-35M" a "**€30M (tetto massimo framework contract, 2 anni fermi + opzione fino a 4)**"; sostituire la derivazione €7,5-8,75M/anno con "**€7,5-15M/anno a seconda dell'esercizio delle opzioni**"; segnalare che il dato non è stato verificato su TED/EMSA primario in questa sessione (verifica manuale raccomandata prima di uso in documento investment-grade).

---

## 3. Costo di sviluppo di un UAV custom (benchmark reali vs proxy VC)

### 3.1 Tabella

| Claim (report 05/10) | Fonte trovata (URL) | Verdetto | Confidenza |
|---|---|---|---|
| Box-wing C3 <25kg certificato/industrializzato/serie: "€3-10M+" (proxy: funding VC Wingtra $60M/8 anni, Quantum $8Md) | **CORDIS** (grant ID 967019), H2020 SME Instrument, **€3.541.185** di contributo UE, 2021-2023, per "achieve broader commercialisation of the WingtraOne" (industrializzazione/scale-up di un prodotto già maturo, MTOW 4,8kg) | **Confermato da fonte istituzionale reale (non VC-proxy)**, stesso ordine di grandezza | low-medium→**medium** |
| — (bracket superiore, classe di peso diversa) | **NAVAIR/Insitu STUAS Tier II (RQ-21A Blackjack)**: contratto EMD (Engineering & Manufacturing Development) **$43,7M** (2010), per navalizzare la piattaforma civile Integrator (MTOW ~61kg, 2,4× il C3) a requisiti militari — https://www.gpsworld.com/insitu-awarded-71m-blackjack-uas-contract-by-navair/ | **Non comparabile 1:1** (classe di peso 2,4× superiore, requisiti militari vs civile) ma mostra che il salto da civile-leggero a militare moltiplica il costo 5-15× anche per un raddoppio di peso | media (dato contrattuale pubblico verificabile) |
| — (bracket superiore, MALE-adjacent) | **Watchkeeper** (UK MoD/NAO): budget iniziale £700-800M → costo finale **£1,31-1,35 miliardi**, 54 velivoli, MTOW ~450kg (18× il C3), 13 anni di ritardo | **Non comparabile** (classe di peso 18× superiore, requisiti militari all-weather NATO) | media-alta sulle cifre (multiple fonti giornalistiche convergenti su dati NAO/parlamentari), bassa utilità comparativa diretta |
| — (bracket superiore) | **Safran Patroller** (Francia): contratto 2016 **€300-330M** per 14 velivoli + manutenzione 12 anni, MTOW ~1.100kg (44× il C3); **programma cancellato nel 2026** dopo 6 anni di ritardo | **Non comparabile** (classe di peso) ma segnala pattern di rischio: anche piattaforme derivate da prodotto esistente (non sviluppo ex-novo) sforano sistematicamente | media-alta |
| — (classe di peso più vicina) | **Insitu ScanEagle**: sistema completo (4 velivoli + GCS + lanciatore/recupero) **$3,2M (2006)**, MTOW ~18-22kg — **classe di peso più comparabile trovata** al C3 <25kg | Utile come ordine di grandezza di "sistema fixed-wing completo in questa classe di peso", ma non è un costo di sviluppo/certificazione (piattaforma derivata da prodotto commerciale preesistente, dato del 2006) | media |
| — (contesto regolatorio) | **EASA Certified Category**: nessun UAS ha mai ottenuto un Type Certificate EASA pieno (luglio 2026); il caso più avanzato (Schiebel Camcopter S-100, set. 2024) è solo il primo Design Verification Report per rotary-wing, non un TC | **Nessun benchmark diretto "concept-to-Type-Certificate" esiste per nessuna classe di UAS al mondo** | alta sull'assenza di precedenti |

### 3.2 Verdetto

Il claim "€3-10M+" per portare un box-wing C3 <25kg da prototipo a prodotto certificato/industrializzato/supportabile in serie **regge come ordine di grandezza plausibile**, ora corroborato da una fonte istituzionale reale (grant CORDIS, non proxy VC) per il **solo tratto di industrializzazione/scale-up** (non l'intero percorso concept-to-market). I benchmark di classe di peso superiore (STUAS $43,7M per un raddoppio di peso con requisiti militari, Watchkeeper/Patroller centinaia di milioni-miliardi per classi MALE) **non smentiscono il claim**, anzi suggeriscono che €3-10M potrebbe essere **conservativo se emergessero requisiti oltre il civile-leggero puro**. **Nessun benchmark diretto esiste** per "concept-to-Certified-Type-Certificate" in nessuna classe di UAS — coerente con l'assenza di precedenti EASA. Confidenza aggiornata: **da low-medium a medium**.

---

## 4. Certificazione come prodotto (Reg. UE 2019/945)

### 4.1 Tabella

| Claim (report 21, riga 190) | Fonte trovata (URL) | Verdetto | Confidenza |
|---|---|---|---|
| "C-marking assessment €9-25k" (non tracciato nel testo originale) | **EU Drone Port**: "Pricing ranges from €9,000 to €25,000, based on the drone class, complexity of the system, and the number of payloads & accessories" — https://eudroneport.com/uas-certification/class-label/ | **Rintracciato**: la cifra è reale e attribuibile a una fonte primaria pubblica, ma è **single-source** (un solo Notified Body commerciale su 5+ attivi consultati — TÜV SÜD, DEKRA, TÜV Rheinland, NavCert, Applus+ non pubblicano prezzi) | **media (ma va qualificata come "stima ottimistica single-source", non "fatto")** |
| — | (nessuna seconda fonte indipendente trovata) | Copre **solo** la fee di assessment/audit del Notified Body, **non** il costo totale di conformità (ingegneria interna per i requisiti tecnici Allegato Reg. 2019/945, test EMC/RF/acustica di laboratorio, iterazioni, per Modulo H anche il sistema qualità certificato ricorrente) | il costo totale reale è quasi certamente **superiore**, per analogia con altri regimi di certificazione prodotto |
| Modulo A solo C0/C4/C5/C6; C1-C3 richiede Notified Body (Modulo B+C o H) | EASA (pagine ufficiali), EU Drone Port | **Confermato** da più fonti indipendenti | alta (invariata) |
| — (nuovo) EASA Design Verification Report (Specific, SAIL III/IV) | Pagina ufficiale EASA DVR: **"EASA will charge using the applicable hourly rate equal to 250 Euro"**, tetto indicativo **180 ore/anno per progetto di complessità tipica** → **fino a ~€45.000/anno di sola fee EASA** | **Nuovo dato reale, fonte regolatoria ufficiale diretta (non commerciale)** — il dato più solido di questo intero filone | **alta** (percorso diverso dal C-marking: si applica a operazioni Specific SAIL III/IV, non a conformità di prodotto C1-C3) |
| — (nuovo) EASA Type Certificate Certified category | Pagina ufficiale EASA Certified Category; caso Schiebel Camcopter S-100 (settembre 2024, primo DVR mai rilasciato per rotary-wing, non un TC) | **Nessun UAS ha mai ottenuto un TC EASA pieno** — qualunque cifra circolante è stima teorica/analogica, non empirica | n/d |
| — (proxy indiretto, aviazione con equipaggio) | Fonte aggregata: **~$1M categoria "primary"**, **~$25M aviazione generale**, **centinaia di milioni aviazione commerciale** per type certificate velivoli con equipaggio | Proxy di ordine di grandezza per la categoria Certified UAS (trattata da EASA con requisiti tecnici quasi assimilabili all'aviazione con equipaggio) | bassa (proxy cross-dominio, non UAS diretto) |

### 4.2 Verdetto

Il numero "€9-25k" **esiste realmente ma è single-source e ottimistico**: copre solo la parcella dell'assessment Notified Body, non il costo pieno di conformità. Il dato più solido e citabile emerso da questa ricerca è la **fee oraria ufficiale EASA (€250/ora, tetto ~€45k/anno) per il Design Verification Report** — ma questo è un percorso regolatorio diverso (Specific SAIL III/IV) dal C-marking C1-C3 (conformità di prodotto sotto Reg. 2019/945). **Nessun Type Certificate EASA pieno è mai stato rilasciato a un UAS** (luglio 2026): qualsiasi stima di "costo di certificazione Certified category" resta teorica. Raccomandazione: correggere riga 190 del report 21 da `[fatto; ...]` a **`[stima ottimistica single-source; EU Drone Port; media]`**, esplicitando che copre solo la fee NB, non il costo totale (che resta, per il salto dimostratore→prodotto, dell'ordine di **€3-10M+** come da §3).

---

## 5. Costo/tempo autorizzazione operativa BVLOS/SORA in Italia (nuovo filone, nessun claim pregresso)

### 5.1 Tabella

| Voce | Fonte trovata (URL) | Dato | Confidenza |
|---|---|---|---|
| Onere amministrativo ENAC | enac.gov.it, pagina ufficiale "Autorizzazione operativa" — codice tariffa **R66-1A** | **€355** (anticipo fisso, indipendente dal SAIL) — solo diritto di segreteria/istruttoria | **alta** (fonte ufficiale, cifra precisa) |
| Dichiarazione Scenari Standard (STS) | enac.gov.it — codice tariffa **R66-1** | **€114** | alta |
| Attestato pilota UAS A1-A3 | enac.gov.it | **€31** (rinnovo ogni 5 anni) | alta |
| Tempi istruttoria ENAC | overfly.me (secondaria) + raccomandazione ufficiale ENAC di presentare domanda 60 gg prima | **15-45 giorni lavorativi** (dossier completo); ENAC stessa ha riconosciuto pubblicamente tempi "ancora troppo lunghi" per casi non-standard | media (fonte secondaria ma coerente con raccomandazione ufficiale) |
| Costo consulenza dossier SORA in Italia/UE | D-Flight, DL Droni, EuroUSC Italia (ora gruppo Terra Drone Corporation Giappone), Professione Drone, EU Drone Port, AirHub — **7 operatori identificati** | **Nessun prezzo pubblicato da nessuno** — tutti "preventivo su richiesta" | alta sull'esistenza del mercato, **assenza di prezzo confermata su 7 fonti indipendenti** |
| Proxy quantitativo (UK CAA, non EASA/ENAC) | caa.co.uk, Scheme of Charges 2026/27; commento sUAS News maggio 2026 | **SAIL 2: £3.806 / SAIL 3: £10.380** (fee regolatoria iniziale, copre 7h; extra a £346/h fino a £40.015/anno); "una domanda SAIL 2 costa il 74% in più della vecchia tariffa OSC, **prima di considerare tempo del consulente**" | media sul dato UK, **bassa sulla trasferibilità diretta a ENAC** (UK SORA è un framework post-Brexit distinto) |
| Alternativa: PDRA predefinito vs SORA bespoke | Casi reali italiani: **E-Distribuzione/Enel** (PDRA-01, BVLOS <25kg, area non popolata, ≤2km dal pilota) e **Telespazio/Leonardo** (piattaforma T-DROMES®, PDRA, 2024) | Due precedenti italiani reali di autorizzazione BVLOS **via PDRA**, non SORA custom — percorso potenzialmente più rapido/economico se lo scenario Pentema è riconducibile a un PDRA esistente (es. IT-PDRA-01) | media — **da verificare con aviation-regulatory-counsel** se applicabile a un VTOL >25kg (JOUAV CW-30E è 38kg, sopra il limite PDRA-01) |

### 5.2 Stima finale best-effort (triangolata)

- **Onere ENAC certo**: €355 (fonte ufficiale diretta).
- **Consulenza esterna per un dossier SORA SAIL II-III completo**: nessuna cifra pubblica diretta reperita in Italia/UE dopo ricerca estesa su 7+ operatori. Triangolando il proxy UK CAA (£3.806-10.380 ≈ €4.400-12.000 di sola fee regolatoria) con l'osservazione di settore che il costo del consulente eccede tipicamente quello della fee regolatoria, **stima plausibile (non verificata) €10.000-30.000** per un dossier SAIL II-III completo. **Da verificare con RFI diretta a D-Flight, EuroUSC Italia, DL Droni prima del gate M+6** — nessun'altra via per ottenere un numero reale.
- **Tempo totale end-to-end**: 15-45 gg lavorativi di sola istruttoria formale (dossier pronto) + tempo di preparazione dossier non quantificato pubblicamente (proxy internazionale: Germania/Olanda 3-6 mesi, UK 6-12 mesi alla prima domanda) → **stima ragionevole 4-8 mesi** dalla kick-off all'autorizzazione, se il dossier non richiede iterazioni.
- **Percorso da esplorare prioritariamente**: verificare se un PDRA esistente (probabilmente non IT-PDRA-01 stesso, che è limitato a <25kg — JOUAV CW-30E è 38kg — ma un PDRA-G01/G02/G03 di più recente pubblicazione) copre lo scenario Pentema, il che ridurrebbe sensibilmente sia costo sia tempo rispetto a un SORA bespoke.

---

## 6. Azioni raccomandate (procurement / RFQ)

1. **RFQ formale a JOUAV** (tramite reseller EU, es. MARIDS Spagna) e **Threod Systems** — unico modo per ottenere un prezzo reale per la fascia T2; nessuna fonte pubblica disponibile dopo ricerca estesa.
2. **Segnalare a `regulatory-adversary` e `aviation-regulatory-counsel`** il nuovo rischio JOUAV/DOD 1260H (ban procurement USA da dic-2025, interrogazione Europarlamento in corso) come rischio attivo per il Percorso 6A se la piattaforma baseline resta JOUAV in un contesto di cliente pubblico italiano (PA, Protezione Civile).
3. **Richiedere 3 preventivi comparativi reali** per il dossier SORA (D-Flight, EuroUSC Italia/Terra Drone, DL Droni) prima del gate M+6 — nessuna cifra pubblica esiste, va commissionata.
4. **Verificare applicabilità di un PDRA esistente** (non IT-PDRA-01, limitato <25kg) allo scenario Pentema con JOUAV CW-30E (38kg) — potenziale risparmio di costo/tempo rispetto a SORA bespoke.
5. **Correggere 3 numeri nei report interni**: (a) `05-piattaforme-costi.md` §6, contratto EMSA da "€30-35M" a "€30M, tetto massimo, 2+2 anni opzionali"; (b) `21-boxy-prodotto-strategia.md` riga 190, C-marking da `[fatto]` a `[stima single-source EU Drone Port, media]`; (c) `05-piattaforme-costi.md` §3.1, Trinity F90+ da "$18.300" a "Trinity Pro (successore) $23.800-28.550".
6. **Richiedere quotation diretta a un Notified Body** (TÜV SÜD, DEKRA o TÜV Rheinland) per il costo reale di assessment C1-C3 — il numero "€9-25k" trovato è single-source e ottimistico.

---

## Elenco fonti salvate (pertinenti a questo report)

**Prezzi COTS (topic 1):** `wingtraone-gen2-pricing-2026.md`, `wingtraone-genii-uk-tender-korec-2025.md`, `quantum-trinity-f90-pricing-variance-2026.md`, `quantum-systems-trinity-pricing-retail-2026.md`, `quantum-systems-trinity-pro-successore-2026.md`, `jouav-threod-delair-no-public-price-confirmed.md`, `jouav-nessun-prezzo-pubblico-dod-1260h-2026.md`, `threod-stream-c-nessun-prezzo-pubblico-2026.md`, `delair-francia-tender-ministero-interno-2020-2021.md`, `delair-dt18-dt26-prezzi-2013-datati.md`

**Contratto EMSA-Tekever (topic 2):** `emsa-tekever-contract-2025-value-30M.md`, `tekever-emsa-contract-history-2018-2021-2025.md`, `uasvision-usd-eur-conversion-35m.md`, `emsa-rpas-service-model-crew-contractor.md`, `emsa-parallel-rpas-contracts-schiebel-airbus-nordic.md`, `ted-emsa-access-limitation.md`

**Costo sviluppo UAV (topic 3):** `cordis-wingtraone-industrializzazione-grant.md`, `scaneagle-cost-3.2m-2006-comparabile.md`, `watchkeeper-patroller-male-cost-benchmark-non-comparabile.md`, `nao-watchkeeper-cost-programma-non-comparabile.md`, `navair-stuas-integrator-emd-contract.md`

**Certificazione prodotto (topic 4):** `notified-body-easa-fees-no-public-price.md`, `notified-body-c-class-cost-eudroneport.md`, `easa-design-verification-report-cost.md`, `easa-certified-category-status-no-tc-issued.md`, `easa-sora-2.5-easy-access-rules-e-tariffa-dvr.md`

**SORA/BVLOS Italia (topic 5):** `uk-caa-sora-fee-schedule-2026-27-proxy-utile.md`, `uk-caa-sora-tariffe-ufficiali-sail-2026-27.md`, `enac-tariffe-ufficiali-reali-2025.md`, `enac-autorizzazione-operativa-costi-documentazione.md`, `enac-tempistiche-istruttoria-15-45-giorni.md`, `sora-consulenza-italia-nomi-reali-no-prezzo.md`, `consulenze-italia-sora-nessun-listino-pubblico.md`, `pdra-vs-sora-bespoke-e-distribuzione-telespazio.md`

**Limite di sessione documentato in:** `ted-emsa-access-limitation.md` (WebFetch/curl bloccati per l'intera sessione da policy di rete — dato confermato indipendentemente da tutti e 5 gli agenti e dalla ricerca diretta).
