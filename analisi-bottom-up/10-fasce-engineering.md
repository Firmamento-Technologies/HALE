# Fasce Engineering di Famiglia — T0-T4, Costi Realistici e Architettura Modulare

> **Volume:** Analisi bottom-up pre-Studio — documento di seguito a `05-piattaforme-costi.md` e `00-SINTESI-strategica.md`
> **Data:** 8 luglio 2026
> **Autore:** VTOL/MALE UAS Specialist
> **Mandato:** riframing strategico — Firmamento non cerca "la piattaforma minima per un servizio" ma una **famiglia di piattaforme modulari a fasce crescenti** (T0-T4), con Pentema come trampolino di lancio e non come fine. Il presente documento definisce 4-5 punti di progetto concreti, con numeri realistici di CapEx/OpEx/prestazioni, e valuta onestamente quanto un'architettura comune (avionica, GCS, vano payload) sia davvero condivisibile tra fasce.

---

## 0. Caveat epistemico e riconciliazione con la ricerca precedente

**Confidence aggregata: LOW-MEDIUM**, eterogenea per fascia (dichiarata riga per riga). Metodologia: benchmark vendor pubblici + triangolazione con i dati già raccolti nel repository (`05-piattaforme-costi.md`, vendor-RFQ JOUAV/Tekever) + stime ingegneristiche per analogia dove non esiste prezzo pubblico. **Nessun numero di questo documento è una quotation vendor reale per Firmamento.**

**Riconciliazione esplicita.** Il verdetto di `00-SINTESI-strategica.md` ("non volare, torri fisse battono l'aereo") **vale solo per la persistenza su un punto fisso per la connettività** — il caso specifico analizzato in quella ricerca (hotspot Pentema, copertura banda larga di un borgo). Non si applica automaticamente a:
- **missioni di trasporto** (consegna farmaci/pacchi punto-punto, intrinsecamente mobili — una torre fissa non trasporta nulla);
- **sensing di area vasta o multi-sito** (mapping, monitoraggio ambientale su più versanti, non un singolo punto);
- **relay mobile** (nodo di comunicazione che segue un evento, es. un incendio che si sposta).

Queste missioni sono **il cuore della nuova cornice** di questo documento e non erano l'oggetto della falsificazione precedente. Restano validi, e vanno tenuti in mente come vincolo esterno: (a) il mercato pagante non-grant a Pentema è piccolo (`03-mercato.md`, `00-SINTESI`, ~€40-150k/anno), (b) il tetto di finanziabilità "comodo" resta ~€1M (`06-finanziabilita.md`), (c) il "moltiplicatore della persistenza" (`05-piattaforme-costi.md` §8) si applica a qualunque fascia se si vuole continuità H24, non solo alla connettività.

---

## 1. Tabella comparativa sintetica — T0-T4

| | **T0 — COTS EO** | **T1 — BOXY (box-wing C3)** | **T2 — MID** | **T3 — MALE civile** | **T4 — HALE stratosferico** |
|---|---|---|---|---|---|
| **Rif. mercato** | DJI M350 RTK / WingtraOne GEN II | Concept Firmamento (three-lifting-surface C3, [`Progetto concettuale struttura HALE.md`](../Progetto%20concettuale%20struttura%20HALE.md)); bracket COTS Quantum Trinity F90+ / JOUAV CW-15 | JOUAV CW-30E, Threod Stream C, Eule MH675 (bracket) | Tekever AR3/AR5, Elbit Hermes 450/900, Schiebel S-100 | Airbus Zephyr, BAE PHASA-35, Skydweller, EuroHAPS |
| **MTOM** | 4,8-9,2 kg | **≤25 kg** (vincolo C3 dichiarato) | 30-150 kg | 150-450 kg | 20-150+ kg (ma quota 20 km cambia tutto) |
| **Apertura** | n/a (multirotore) / ~1-2 m | **~3 m** (vincolo dichiarato) | 3-6 m `[stima]` | 8-17 m `[stima/bracket]` | 20-25+ m (high-AR) |
| **Payload utile** | 2,7 kg, no vano interno | 3-5 kg `[stima]`, vano ~4-6 L | 10-20 kg `[stima]`, vano ~15-25 L | 4-6 kg (ISR compatto) → 50-150 kg (multi-sensore) fortemente ruolo-dipendente | pochi kg (relay/EO leggero) |
| **Endurance** | 40-60 min | 90 min-3h elettrico `[stima]`; 4-5h se ibrido (rischio TRL) | 10-16h ibrido `[stima/bracket]`; **"giorni" NON realistico a questa taglia in VTOL compatto** | 16-24h | settimane-mesi nominali (mai dimostrato in inverno UE) |
| **Quota operativa** | <120 m AGL operativo (limite reg. tipico) | fino 3.000-4.000 m `[stima]` | fino 4.000-5.000 m `[stima]` | 4.000-9.000 m | 18-24 km |
| **Range/C2** | 15-20 km O3/LOS | 40-80 km `[stima]` | 100-200 km (+SATCOM opz.) `[stima]` | 100-230 km tattico (+SATCOM BLOS) | globale (satellite) |
| **Velocità cruise** | ~50-60 km/h | 90-120 km/h `[stima]` | 100-150 km/h `[stima]` | 110-220 km/h | 20-30 m/s (~72-108 km/h) |
| **CapEx sviluppo/acquisto (1 unità/sistema)** | **€40-120k** (sistema completo) | Dimostratore: **€150-400k**. Prodotto certificato/serie: **€3-10M+** | **€0,8-1,8M** (sistema completo, no IVA) `[stima]` | **€2-10M** per unità fully equipped `[bracket Hermes/Schiebel]` | **$50M-1B per programma** (nessun listino) |
| **Costo-programma servizio (TCO/anno)** | n/a (spot, no persistenza) | n/a dimostratore; se prodotto: come sopra | TCO 5 anni **€1,3-2,5M** `[stima]` | benchmark EMSA reale: **€7,5-8,75M/anno** (4 velivoli, equipaggio incl.) | impossibile stimare: nessun operatore commerciale esiste |
| **OpEx/h** | €15-40 `[stima]` | n/a / €30-60 se COTS equiv. | €150-400 `[stima]` | €800-3.000 `[stima]` | n/a |
| **TRL** | **9** | **3-4** (dimostratore) / 9 (COTS equiv.) | 7-9 (COTS/semi-custom) / 3-4 (custom da zero) | 8-9 (vendor, non EASA-validated) | 3-5 (nessuno operativo commerciale) |
| **Lead time** | settimane | 12-24 mesi (sviluppo) | 6-12 mesi (COTS) / 24-36 (custom) | 12-24 mesi (backlog difesa alto) | anni (nessun prodotto in serie) |
| **Classe regolatoria** | Open A1/A2/A3, C0-C2 | Open A3 VLOS o Specific SAIL II BVLOS (PDRA-S01) | Specific SAIL II-III BVLOS | Certified Category probabile (MTOM>150kg) o Specific SAIL IV-VI — **nodo regolatorio non risolto in Italia** | Certified, nessun framework HAPS dedicato |

*Fonti dettagliate e confidence per riga nelle sezioni 2-6. Dati T0 e T4 già triangolati in `05-piattaforme-costi.md` (confidence media-alta); T1-T3 comprendono ricerca nuova per questo documento (confidence dichiarata inline).*

---

## 2. T0 — Multirotore/VTOL COTS EO (riferimento economico)

Riferimento invariato rispetto a `05-piattaforme-costi.md` §2 (DJI M350 RTK, WingtraOne GEN II): CapEx €40-120k, endurance 40-60 min, TRL 9, nessuna persistenza. Funziona come **baseline di costo/prestazioni** per giudicare se le fasce superiori valgono l'investimento incrementale — non come piattaforma di famiglia modulare (architettura chiusa proprietaria DJI/Wingtra, nessuna possibilità di payload custom Firmamento).

---

## 3. T1 — "BOXY": VTOL C3 box-wing custom (≤25 kg, ~3 m)

### 3.1 Cosa dice il concept interno

Il documento concettuale Firmamento (`Progetto concettuale struttura HALE.md`) descrive due configurazioni: (a) l'ala high-AR a diedro poliedrico per l'HALE (T4, fuori scope qui) e (b) un'**analisi preliminare in XFLR5 di una configurazione a tre superfici portanti (three-lifting-surface, canard + ala + T-tail) ispirata al Piaggio P180 Avanti, categoria C3 (apertura <3m)**, esplicitamente indicata come "potenziale per una futura integrazione ibrida VTOL". 

**Nota terminologica:** il mandato di questo documento chiama questa fascia "box-wing"; il documento concettuale interno la descrive come *three-lifting-surface* (canard+ala+coda), non un box-wing in senso stretto (ala chiusa ad anello). Sono famiglie aerodinamiche diverse — entrambe C3, entrambe a canard/superfici multiple, ma **BOXY nel senso letterale (ala chiusa) non è ancora stato modellato nel repository**; quanto segue vale per la configurazione three-lifting-surface effettivamente disegnata, che è la più vicina a un dato reale disponibile.

### 3.2 Prestazioni stimate (nessun prototipo volato, quindi tutte stime per analogia)

| Parametro | Stima | Base dell'analogia | Confidence |
|---|---|---|---|
| MTOM | ≤25 kg | vincolo di categoria C3 dichiarato | alta (è un vincolo, non una previsione) |
| Payload utile | 3-5 kg | bracket Quantum Trinity F90+ (1 kg, 5,5 kg MTOW) → JOUAV CW-15 (3 kg, 14 kg MTOW); a 25 kg MTOM con propulsione elettrica un carico utile 3-5 kg è coerente | media |
| Vano payload | ~4-6 L indicativi | dimensionamento gondola centrale (fusoliera "low-drag pod" citata nel concept) per alloggiare gimbal EO/IR o piccolo pod cargo | bassa (nessun disegno meccanico dettagliato disponibile) |
| Endurance | 90 min-3h elettrico puro | bracket Trinity F90+ (90 min) — CW-15 (3-5h, ma CW-15 non è confermato elettrico puro, probabile ibrido) | bassa-media |
| Quota operativa | fino 3.000-4.000 m | limite tipico small VTOL a propulsione elettrica (densità aria, autonomia motore) | bassa (stima ingegneristica, non validata in galleria/volo) |
| Range C2 | 40-80 km | tipico small VTOL con datalink LOS/leggero SATCOM | bassa |
| Velocità cruise | 90-120 km/h | efficienza aerodinamica attesa da configurazione high-AR/three-lifting-surface (il canard riduce il carico deportante di coda, vedi concept doc §"Analisi Configurazioni Alternative") | media (qualitativo, non quantificato in CFD completo) |

### 3.3 Verifica del target €300k — FALSIFICATO se inteso come "prodotto operativo"

Riprendendo `05-piattaforme-costi.md` §3.2 (nessuna ricerca nuova necessaria, il dato regge):

- **Come dimostratore sperimentale non certificato** (1 esemplare, no serie, no declaration of conformity EASA): **€150-400k, 12-24 mesi**. Il target €300k **sta dentro questo range** — è un numero plausibile per arrivare a un primo volo di un dimostratore. Confidence: **low** (stima per analogia con costing di progetti universitari/startup pre-seed di categoria simile in composito, nessun dato diretto pubblico).
- **Come prodotto certificato, industrializzato, supportabile in serie** (il livello a cui operano oggi Quantum Systems, Wingtra, JOUAV): **€3-10M+**. Il target €300k **è sotto di 1-2 ordini di grandezza** rispetto a un prodotto realmente commerciabile per un servizio operativo autorizzato PA/Protezione Civile. Benchmark: Wingtra (~8 anni, oltre $60M cumulati, TechCrunch/DroneXL/Tracxn) e Quantum Systems (valutazione $8 mld dopo Series D, ma include vendita/marketing globale — limite superiore, non costo di sviluppo puro).

**Verdetto: il target €300k è REALISTICO SOLO se il mandato di BOXY è esplicitamente "dimostratore tecnologico/banco di prova IP", NON "prodotto pronto per erogare servizio autorizzato a Pentema o altrove".** Va dichiarato esplicitamente nella governance del progetto quale dei due obiettivi BOXY persegue, perché cambiano di un ordine di grandezza il budget necessario e il tipo di autorizzazione ENAC richiesta.

### 3.4 Classe regolatoria

Senza declaration of conformity C3 (Modulo A **non disponibile** per C1-C3 — serve EU-type examination o quality assurance tramite Notified Body, vedi `05-piattaforme-costi.md` §3.2 fonte EASA/EU Drone Port), BOXY può operare solo: (a) **Open A3 VLOS** come dimostratore non certificato con operazioni lontano da persone, oppure (b) **Specific Category, PDRA-S01/SAIL II BVLOS** con autorizzazione ENAC caso per caso. Nessuna delle due consente un servizio commerciale ripetibile scalabile senza ulteriore iter di certificazione.

---

## 4. T2 — "MID": VTOL/fixed-wing più capace e persistente (30-150 kg)

### 4.1 Benchmark di mercato raccolti per questa fascia

| Piattaforma | MTOM | Endurance | Payload | Prezzo | Fonte | Confidence |
|---|---|---|---|---|---|---|
| **JOUAV CW-30E** (CN) | 38 kg | 6-10h (480 min dichiarati) | 8 kg | Platform €80-180k `[stima triangolata]`; CapEx Y1 sistema completo **€580-820k**; TCO 5 anni **€745-1.120k** | [JOUAV product page](https://www.jouav.com/products/cw-30e.html); dato interno cross-checked con `studio-di-fattibilita/allegati/vendor-rfq/` | media (nessun listino pubblico diretto, ma cross-check con vendor-RFQ interno) |
| **Threod Systems Stream C** (EE, NATO-adjacent) | 38-45 kg | 5-6h | payload EO 30x zoom + gimbal MWIR | **prezzo non pubblico** — "il più grande UAS NATO Class I che eroga capacità Class II" implica sensoristica militare-grade, verosimilmente **€500k-1,5M+ per sistema equipaggiato** `[stima per analogia di categoria]` | [Threod datasheet](https://threod.com/wp-content/uploads/2020/07/Stream-C-VTOL-datasheet.pdf), [Dronelitic](https://dronelitic.com/threod-systems-stream-c-uas/) | **bassa** (nessun prezzo pubblico, estrapolazione da categoria) |
| **Eule MH675** (CN, heavy-lift) | 130 kg | 3-6h | fino 30 kg | non pubblico; per analogia di mercato cinese heavy-lift, verosimilmente sub-€150k platform `[stima]` | [MotioNew listing](https://www.motionew.com/shop/vtol-and-fixed-wing-drone/eule-mh675-30kg-hybrid-large-vtol/) | bassa |
| **Insitu Integrator / RQ-21A Blackjack** (US, benchmark endurance) | ~61 kg | fino 24h (16h a payload massimo) | modulare | contratti multi-unità $41-390M comprendono GCS/payload/supporto, **non isolabile il prezzo per singolo velivolo**; NON è VTOL (lancio a catapulta, recupero skyhook — richiede infrastruttura di lancio/recupero incompatibile col vincolo "aree ridotte in valle" di Pentema) | [Wikipedia RQ-21 Blackjack](https://en.wikipedia.org/wiki/Boeing_Insitu_RQ-21_Blackjack), [Defense Post](https://thedefensepost.com/2019/06/29/boeing-insitu-blackjack-scaneagle-drones-390-million/) | media (contratti pubblici, ma bundling rende difficile isolare unit cost) |
| **Latitude Engineering HQ-60** (US, hybrid quadrotor — diversa famiglia aerodinamica) | 27 kg | fino 15h | 3,6 kg | **~$60k** (~€55k) | [Latitude Engineering](https://www.latitudeengineering.com/products/hq/), [New Atlas](https://newatlas.com/hybrid-quadrotor-hq-uav/28767/) | media |

### 4.2 Lettura: "giorni di autonomia" per T2 è marketing, non ingegneria

Il mandato ipotizza T2 "eventualmente ibrido o parziale-solare per stare più su, più tempo" con orizzonte "giorni". **Nessun prodotto commerciale nella classe 30-150 kg dimostra endurance pluri-giornaliera.** Il record più vicino nel dataset raccolto è **Integrator/Blackjack, ~24h**, ottenuto con motore a combustione interna e frazione di carburante molto alta — non VTOL, lancio a catapulta. Il caso solare-assistito più vicino (Silent Falcon, US) mostra 14h di endurance ma a **5-10 kg di MTOM**, non 30-150 kg — l'assistenza solare in questa fascia richiede superficie alare molto estesa (per raccogliere energia sufficiente), il che è in **tensione diretta** con il requisito di VTOL compatto per "spazi di decollo ridotti a Pentema" del mandato originale. **Un parziale-solare a 30-150 kg che aggiunga giorni di endurance non esiste sul mercato oggi**; è più corretto parlare di **10-16h ibrido ICE-elettrico** come tetto realistico, con solare eventualmente come 15-25% di margine extra su una missione di 10-16h, non come salto di categoria verso "giorni".

Fonte Silent Falcon: [Defense Update](https://defense-update.com/20130814_slent_falcon.html), [sUAS News](https://www.suasnews.com/2019/06/silent-falcon-ee-extended-endurance/), [New Atlas](https://newatlas.com/silent-falcon-uav/23641/). Confidence: media (specifiche vendor, nessun prezzo pubblico).

### 4.3 Verifica del target €1,5M utente

- **Come sistema COTS/semi-custom "premium"** (1-2 unità JOUAV CW-30E-class con payload avanzato — SAR, relay telecom, ridondanza parziale — oppure 1 unità Threod Stream C-class NATO-adjacent): **€0,8-1,8M** `[stima]` è **realistico**. Cross-check interno: il modello finanziario Firmamento (`studio-di-fattibilita/allegati/financial-model/README.md`, citato in `05-piattaforme-costi.md` §4) segnala che il CapEx Y1 "sliding timeline" del Percorso 6A realistico è **€2,5-3,5M** — quindi €1,5M per un T2 "premium" con singola unità e payload avanzato è **compatibile in ordine di grandezza** con quanto già osservato per la Classe 3 del report precedente, se contenuto a 1 sola unità senza piena ridondanza.
- **Come sviluppo custom Firmamento da zero** (nuovo airframe 30-150 kg, non comprato COTS): per lo stesso principio della Classe 2 scalata (§3.3), un programma di sviluppo-certificazione-industrializzazione per questa taglia costerebbe verosimilmente **€5-15M+** — ben oltre €1,5M. Nessun dato diretto disponibile; stima per analogia con il gap dimostratore→prodotto osservato in T1 e con la scala di complessità maggiore (motore ibrido, certificazione MTOM>25 kg che esce dalla categoria Open, necessità di type-approval più stringente).

**Verdetto: il target €1,5M è raggiungibile SOLO comprando/configurando un sistema COTS o semi-custom esistente (JOUAV/Threod-class) con payload avanzato, NON sviluppando un nuovo airframe da zero.** Questo è coerente con il verdetto "Buy COTS vince" già raggiunto in `05-piattaforme-costi.md` §11 per il Percorso 6A.

### 4.4 Classe regolatoria

Specific Category, SAIL II-III BVLOS — stessa fascia già mappata per JOUAV CW-30E in `04-regolatorio.md`.

---

## 5. T3 — "MALE" civile (centinaia di kg, 10-40h)

### 5.1 Benchmark raccolti

| Piattaforma | MTOM | Endurance | Payload | Prezzo unitario | Costo-programma | Fonte | Confidence |
|---|---|---|---|---|---|---|---|
| **Tekever AR3/AR5** (PT) | fino 180 kg (AR5) | 16-20h | 4-6 kg | non pubblico | **benchmark EMSA reale: €30-35M/4 anni per 4 velivoli, equipaggio+operazioni incluse ≈ €7,5-8,75M/anno** | [UST](https://www.unmannedsystemstechnology.com/2025/11/tekever-secures-emsa-agreement-for-ar5-fixed-wing-uas-deployment/), [UAS Vision](https://www.uasvision.com/2026/03/05/tekever-gets-35m-emsa-contract-for-ar5-fixed-wing-uas-deployment/) | **alta** (contratto pubblico UE) — già triangolato in `05-piattaforme-costi.md` §6 |
| **Elbit Hermes 450** (IL) | ~450 kg | 17-20h | ~150 kg (multi-sensore) | **~$2M/unità** (~€1,85M) | n/d | [Wikipedia](https://en.wikipedia.org/wiki/Elbit_Hermes_450), [Globes](https://en.globes.co.il/en/article-elbit-systems-wins-contracts-worth-335m-in-europe-1001494253) | media (stampa aggregata, range stimato, non listino ufficiale) |
| **Elbit Hermes 900** (IL) | ~1.180 kg (classe superiore) | fino 36h | maggiore | **~$6-7M/unità** (~€5,5-6,5M) | n/d | stessa fonte aggregata | bassa-media (stima ampia) |
| **Schiebel Camcopter S-100** (AT) | 200 kg | 6h | non specificato qui | **£375k listino airframe** (~$470k) per singolo velivolo; **~$2M per sistema completo** (2 velivoli+GCS+training, dato storico 2005); contratti bulk recenti: **UAE 40 unità $170M (~$4,25M/unità)**, **Thailandia 2 unità $19,4M (~$9,7M/unità, verosimilmente incl. supporto/spare/training)** | n/d | [Wikipedia](https://en.wikipedia.org/wiki/Schiebel_Camcopter_S-100), [UK Defence Journal](https://ukdefencejournal.org.uk/royal-navy-gets-new-surveillance-drone/), [Shephard Media](https://www.shephardmedia.com/news/naval-warfare/thailand-confirms-additional-camcopter-s-100-procu/) | media (contratti pubblici, ma bundling eterogeneo tra fonti spiega la forbice ampia) |
| **MQ-9 Reaper** (US, benchmark top-of-range **militare esquisito**, non comparabile 1:1 civile) | ~4.760 kg | 27h | 1.700 kg | $16,9-30M/unità flyaway | CPFH $3.000-4.000 diretto, fino $12.000 fully-loaded (GAO) | fonte governativa già in `05-piattaforme-costi.md` §6 | media-alta ma non applicabile civile |

### 5.2 La forbice reale vs l'ipotesi utente €50-100M

**Il dato più solido è il civile/tattico non-esquisito: €2-10M per unità fully equipped** (Hermes 450/900, Schiebel S-100 su contratti bulk). Il benchmark EMSA (€7,5-8,75M/anno, 4 velivoli+equipaggio+operazioni multi-sito) è il riferimento più affidabile per **"quanto costa realmente un servizio MALE persistente in Europa"**, e conferma che l'ordine di grandezza corretto per un **programma pluriennale realistico è decine di milioni cumulati**, non centinaia.

**L'ipotesi utente €50-100M non è "sbagliata" in assoluto — descrive un territorio diverso.** Ciò che colloca un programma MALE in quella fascia:
1. **Piattaforme militari esquisite** (MQ-9 Reaper-class: $17-30M/unità × 3-5 velivoli + payload SIGINT/SAR avanzati + anni di sustainment) — è già il salto verso il militare puro, non un MALE "civile".
2. **Contratti "as-a-service" multi-anno multi-sito su scala molto più ampia** dell'EMSA (l'EMSA è già un benchmark generoso a €7,5-8,75M/anno; replicarlo su più aree geografiche/più anni con crescente ridondanza porta a cumulati €50-100M nell'arco di un decennio, ma è **costo cumulato di servizio**, non prezzo di un singolo velivolo).
3. **Sviluppo custom da zero di un nuovo MALE certificato EASA** (mai fatto per un civile puro in Europa — nessun type-certificate CS-UAS esiste oggi per questa classe): R&D + certificazione + industrializzazione + supporto per una nuova piattaforma MALE è **territorio HALE/sovranità**, non "acquisto di una piattaforma COTS".

**Verdetto: per Firmamento, un T3 realistico (acquisto/configurazione di una piattaforma MALE civile esistente, tipo Hermes 450 o Schiebel S-100 su contratto bulk) costa €2-10M per unità, non €50-100M.** €50-100M+ è il costo di un **programma di servizio pluriennale multi-unità** oppure il costo di uno **sviluppo custom certificato** — entrambi territorio strategico diverso da "comprare un MALE", e già ai confini della fascia T4/HALE per intensità di capitale.

### 5.3 Nodo regolatorio critico (non risolto)

MTOM 150-450 kg in EU tipicamente **esce dalla Specific Category "leggera"** e richiede o SAIL IV-VI (con requisiti tecnici e assicurativi molto più stringenti) o, più probabilmente, ricade nella **Certified Category** con obblighi di type-certificate quasi assimilabili all'aviazione con equipaggio. Nessun precedente italiano di autorizzazione ENAC per un MALE civile 150-450 kg in operazioni BVLOS su territorio SNAI è stato identificato in questa ricerca — **da verificare con `aviation-regulatory-counsel` e `regulatory-adversary` prima di ogni impegno su questa fascia**, è un rischio regolatorio potenzialmente showstopper indipendentemente dal costo.

---

## 6. T4 — "HALE" stratosferico solare (solo inquadramento)

Nessuna ricerca nuova: riuso integrale di `05-piattaforme-costi.md` §7 (già ancorato a DR-014, fonti istituzionali alta confidenza). **Perché $50M-1B**: R&D per bilancio energetico solare a 20 km (mai risolto per l'inverno a 44°N secondo l'analisi Firmamento stessa, Cap. 6 §6.2.2.3), batterie ad altissima densità energetica (LiS, non ancora maturo commercialmente), aeroelasticità di un'ala high-AR mai validata su scala di serie, e **nessuno dei 12 programmi HALE solari avviati globalmente dal 2003 è oggi operativo commercialmente** (DR-013: 42% cancellati, 42% slittati permanentemente, 17% solo dimostrazione governativa, 0% operativo commerciale). T4 resta **vettore strategico Y6+**, non procurement — coerente con `CLAUDE.md` e `riferimenti/visione-10-anni.md`.

---

## 7. Architettura modulare comune — cosa è davvero riusabile

### 7.1 I tre livelli di condivisione possibile

| Livello | Cosa significa | Fattibilità reale |
|---|---|---|
| **1. Airframe unico "morphabile"** | Stesso scafo/ala che cambia scala da 25 kg a 300+ kg | **NO — fisicamente impossibile.** Scaling laws: strutture, propulsione, aerodinamica cambiano qualitativamente tra un T1 da 25 kg e un T3 da 300 kg (numero di Reynolds diverso, materiali strutturali diversi, sistema propulsivo elettrico vs ibrido/ICE, requisiti di certificazione diversi). Nessun vendor del settore (JOUAV, Quantum, Tekever) offre una "famiglia" con lo stesso airframe scalato di 10x in massa. |
| **2. Sottosistemi/avionica condivisi tra 2-3 taglie adiacenti** | Stesso autopilota/FCC, stesso protocollo dati, stesso GCS software, tra le fasce **fisicamente vicine** (T1↔T2) | **SÌ, ma condizionato**: vedi §7.2 |
| **3. Payload intercambiabile dentro una fascia** | Stesso vano/interfaccia payload su un unico airframe, per scambiare gimbal EO/relay/cargo pod | **SÌ, il livello più solido e il più prezioso** — vedi §7.3 |

### 7.2 Avionica e GCS comuni — dove regge, dove no

**La condizione critica, spesso ignorata:** l'avionica/GCS è condivisibile **solo tra piattaforme sviluppate in-house da Firmamento**, non tra un T1 costruito internamente e un T2/T3 comprato COTS.

- Se BOXY (T1) è sviluppato da Firmamento su un'architettura avionica aperta (es. stack basato su PX4/MAVLink, tipo [Auterion Skynode](https://auterion.com/product/skynode-x/) o Pixhawk-class, che supporta nativamente multicottero/fixed-wing/VTOL — [PX4 docs](https://docs.px4.io/main/en/companion_computer/auterion_skynode)), quello stack **è genuinamente riusabile** su un eventuale futuro T2 "MID" **se e solo se anche T2 viene sviluppato in-house** con la stessa filosofia avionica.
- Ma il verdetto "Buy COTS vince" già raggiunto in `05-piattaforme-costi.md` §11 per il Percorso 6A implica che **T2 e T3 saranno più probabilmente comprati da JOUAV/Threod/Tekever**, che usano **avioniche e GCS proprietarie chiuse** (nessuno di questi vendor espone un'architettura avionica aperta a terzi per l'integrazione — la dicitura "payload interchangeable" nel marketing JOUAV [(fonte: JOUAV CW-30E product page)](https://www.jouav.com/products/cw-30e.html) si riferisce ai **payload del proprio catalogo**, non a un'interfaccia aperta per sviluppatori terzi).
- **Conseguenza onesta:** se la strategia resta "Buy COTS per T2/T3", l'avionica/GCS comune **non si estende oltre T1**. Un layer software di "single pane of glass" (dashboard di missione che aggrega dati da GCS vendor diverse via le rispettive API/export, dove disponibili) è tecnicamente possibile e ha valore operativo, ma **non è controllo di volo condiviso** — resta un livello di reportistica/coordinamento sopra sistemi di comando indipendenti e non intercambiabili.

**Verdetto:** l'avionica/GCS comune è **realistica solo per T1**, ed **eventualmente estendibile a un futuro T2 SE E SOLO SE Firmamento decide di costruirlo in-house** anziché comprarlo COTS — una scelta di make-vs-buy che ha conseguenze dirette sulla promessa di "famiglia modulare" e va decisa esplicitamente, non data per scontata.

### 7.3 Vano payload modulare standardizzato — il livello che vale davvero la pena progettare

Questo è il cuore realistico della modularità. Specifica proposta (da validare in ingegneria di dettaglio, oggi solo un framework):

**Interfaccia meccanica:**
- Rail/piastra di aggancio quick-release con pattern di foratura standard interno alla famiglia Firmamento, ispirato concettualmente ai kit di interfaccia payload modulare militari (es. [AeroVironment Modular Payload Interface Kits per RQ-20B Puma](https://www.suasnews.com/2021/08/aerovironment-introduces-standardized-modular-payload-interface-kits-for-rq-20b-puma-tactical-unmanned-aircraft-systems-kits-under-order-by-ussocom/), standard USSOCOM Modular Payload) e allo spirito di NATO STANAG 4586 (interoperabilità control-segment) / [STANAG 4671](https://en.wikipedia.org/wiki/STANAG_4586) (airworthiness UAS) — **non l'adozione letterale di questi standard militari** (fuori scope e costo per un operatore civile), ma l'ispirazione architetturale: un connettore meccanico+elettrico+dati unico che permette lo swap payload senza attrezzi speciali in campo.
- Involucro payload **dimensionato per fascia, NON identico tra fasce**: T1 vano ~4-6 L / 3-5 kg, T2 vano ~15-25 L / 10-20 kg. Un modulo payload progettato per il vano T1 **si inserisce fisicamente anche nel vano T2 più grande** (con piastra adattatrice), ma **non vale il contrario** — un payload T2 non entra nel vano T1 più piccolo. Questa è **compatibilità discendente**, non intercambiabilità piena.

**Interfaccia elettrica:**
- Bus di potenza comune (es. 24V/48V DC), connettore standard di famiglia, budget di potenza dichiarato per classe di payload: gimbal EO/IR ~50-150W, nodo relay/IoT ~30-100W, meccanismo di sgancio cargo ~20-50W di picco.

**Interfaccia dati:**
- Protocollo comune (Ethernet/CAN bus + MAVLink per telemetria/comando), formato video downlink comune per i payload EO.

**I tre moduli payload richiesti dal mandato:**

| Modulo | Riusabilità cross-tier | Nota |
|---|---|---|
| **(a) Gimbal EO/IR multispettrale** | **Alta**, se si sceglie un gimbal COTS di terze parti con mount standard (es. famiglie Gremsy/Workswell) invece di uno sviluppato ad-hoc — questi gimbal esistono già in più tagli di massa/potenza e sono pensati per essere montati su airframe diversi | il più maturo, minor rischio di sviluppo |
| **(b) Relay comunicazioni/IoT** | **Media** — nessun COTS esiste per questo caso d'uso specifico (nodo LoRa/cellulare aviotrasportato), sarebbe IP Firmamento; il modulo elettronico interno può essere lo stesso tra T1 e T2 (stesso PCB/radio), cambia solo l'alloggiamento meccanico e l'antenna | sviluppo custom ma a basso rischio ingegneristico (elettronica consumer-adjacent) |
| **(c) Pod di trasporto/cargo (medicale/pacchi)** | **Bassa** — la meno riusabile delle tre. Il meccanismo di sgancio, il bilanciamento del CG durante il rilascio, e la qualifica strutturale del punto di aggancio sono **specifici per ogni airframe** (non si può "bullonare" genericamente un pod cargo senza analisi strutturale dedicata). Riferimento di design: meccanismi di rilascio dei droni di consegna esistenti — [Wingcopter 198](https://wingcopter.com/wingcopter-198) (25 kg MTOW, payload 4,7-6 kg, sgancio triplo, ~$20k/unità, [specsheet](https://www.sisirl.com/wp-content/uploads/2018/01/Specsheet_Wingcopter-198.pdf)) è il benchmark di riferimento più vicino a T1/T2 per massa e concetto operativo, ma è un **prodotto integrato** (airframe+pod progettati insieme), non un pod separato intercambiabile su un airframe generico | massimo rischio di sviluppo/qualifica |

### 7.4 Onestà sui limiti — cosa NON si può fare

- **Non si può morphare un unico airframe da €300k (T1, 25 kg) a €50-100M (T3, 300+ kg).** È ovvio fisicamente, ma va detto esplicitamente perché il linguaggio "famiglia modulare" può far pensare il contrario a uno stakeholder non tecnico.
- **La modularità reale è a due livelli, non uno**: (i) payload intercambiabile **dentro** una fascia (stesso airframe, gimbal/relay/cargo a scelta) — questo è vero e vale la pena progettarlo bene; (ii) sottosistemi/avionica condivisi **tra 2-3 taglie di airframe**, ma **solo se quelle taglie sono tutte sviluppate in-house da Firmamento**, non se una fascia è comprata COTS.
- **Il vano payload è compatibile solo "verso l'alto"** (piccolo dentro grande con adattatore), non simmetricamente intercambiabile tra tutte le fasce.
- **Il modulo cargo è quello che richiede più lavoro di ingegneria dedicata per fascia** — non è un "accessorio" ma un sottosistema con la sua qualifica strutturale.

### 7.5 Verdetto: quali 2-3 taglie condividono davvero l'architettura

**Se Firmamento sviluppa T1 (BOXY) in-house e mantiene questa scelta anche per un eventuale T2 "MID" custom** (anziché comprarlo COTS): **T1 e T2 sono l'unica coppia dove la condivisione di avionica/GCS/filosofia del vano payload è ingegneristicamente vera.** Questo è il nucleo minimo credibile di "famiglia".

**Se invece T2 viene comprato COTS (JOUAV/Threod-class)** — scelta economicamente più difendibile secondo il verdetto Buy-vs-Build di `05-piattaforme-costi.md` §11 — **la famiglia con architettura condivisa si riduce al solo T1**, con la sua terna di payload intercambiabili (EO/relay/cargo). La "famiglia" a quel punto è una **famiglia di missioni su un unico airframe**, non una famiglia di airframe. T0 (COTS spot tool) e T3/T4 (COTS-bought o R&D separata) restano **fuori** dall'architettura condivisa in ogni scenario: sono acquisti/programmi indipendenti che condividono solo il brand e, nella migliore delle ipotesi, un layer software di coordinamento missioni non intrusivo sul volo.

---

## 8. Fonti e confidence complessiva

**Fonti interne al repository (già triangolate, confidence alta per il dato Firmamento):**
- `analisi-bottom-up/05-piattaforme-costi.md` — base per T0, T1 (§3.2-3.3), T3 (Tekever/EMSA), T4
- `analisi-bottom-up/00-SINTESI-strategica.md` — riconciliazione §0
- `Progetto concettuale struttura HALE.md` — concept aerodinamico T1 (three-lifting-surface)
- `analisi-bottom-up/04-regolatorio.md` — classi regolatorie
- `studio-di-fattibilita/allegati/vendor-rfq/`, `studio-di-fattibilita/allegati/financial-model/README.md` — cross-check CapEx JOUAV CW-30E

**Fonti web nuove per questo documento (T2, T3, architettura modulare):**
- Latitude Engineering HQ-60/HQ-40: [latitudeengineering.com](https://www.latitudeengineering.com/products/hq/), [New Atlas](https://newatlas.com/hybrid-quadrotor-hq-uav/28767/), [militaryfactory.com](https://www.militaryfactory.com/aircraft/detail.php?aircraft_id=1106)
- Threod Systems Stream C: [datasheet PDF](https://threod.com/wp-content/uploads/2020/07/Stream-C-VTOL-datasheet.pdf), [Dronelitic](https://dronelitic.com/threod-systems-stream-c-uas/)
- Eule MH675: [MotioNew](https://www.motionew.com/shop/vtol-and-fixed-wing-drone/eule-mh675-30kg-hybrid-large-vtol/)
- Insitu ScanEagle/Integrator/RQ-21 Blackjack: [Wikipedia MQ-27](https://en.wikipedia.org/wiki/Boeing_Insitu_MQ-27_ScanEagle), [Wikipedia RQ-21](https://en.wikipedia.org/wiki/Boeing_Insitu_RQ-21_Blackjack), [Defense Post](https://thedefensepost.com/2019/06/29/boeing-insitu-blackjack-scaneagle-drones-390-million/)
- Silent Falcon: [Defense Update](https://defense-update.com/20130814_slent_falcon.html), [sUAS News](https://www.suasnews.com/2019/06/silent-falcon-ee-extended-endurance/), [New Atlas](https://newatlas.com/silent-falcon-uav/23641/)
- Elbit Hermes 450/900: [Wikipedia](https://en.wikipedia.org/wiki/Elbit_Hermes_450), [Globes](https://en.globes.co.il/en/article-elbit-systems-wins-contracts-worth-335m-in-europe-1001494253)
- Schiebel Camcopter S-100: [Wikipedia](https://en.wikipedia.org/wiki/Schiebel_Camcopter_S-100), [UK Defence Journal](https://ukdefencejournal.org.uk/royal-navy-gets-new-surveillance-drone/), [Shephard Media](https://www.shephardmedia.com/news/naval-warfare/thailand-confirms-additional-camcopter-s-100-procu/)
- Wingcopter 198: [wingcopter.com](https://wingcopter.com/wingcopter-198), [specsheet PDF](https://www.sisirl.com/wp-content/uploads/2018/01/Specsheet_Wingcopter-198.pdf), [Jinghong Drone pricing survey](https://jinghongdrone.com/delivery-drone-cost-full-pricing-breakdown)
- JOUAV CW-30E payload/prezzo: [product page](https://www.jouav.com/products/cw-30e.html)
- Modularità/MOSA/STANAG: [STANAG 4586 Wikipedia](https://en.wikipedia.org/wiki/STANAG_4586), [AeroVironment Modular Payload Interface Kits](https://www.suasnews.com/2021/08/aerovironment-introduces-standardized-modular-payload-interface-kits-for-rq-20b-puma-tactical-unmanned-aircraft-systems-kits-under-order-by-ussocom/)
- Auterion Skynode/Mission Control (esempio di avionica/GCS aperta multi-piattaforma): [auterion.com/product/skynode-x](https://auterion.com/product/skynode-x/), [PX4 docs](https://docs.px4.io/main/en/companion_computer/auterion_skynode), [Auterion Mission Control docs](https://docs.auterion.com/vehicle-operation/auterion-mission-control)

**Limiti dichiarati:**
- Nessuna quotation reale ricevuta da vendor per T1/T2/T3 in questo documento — tutti i CapEx sono stime pubbliche, benchmark analoghi, o cross-check con dati vendor-RFQ interni già dichiarati low-medium confidence alla fonte.
- Le prestazioni di T1 (BOXY) sono **interamente stimate per analogia**: nessun prototipo esiste, nessuna prova in galleria del vento o volo è stata condotta.
- Il prezzo Threod Stream C e Eule MH675 non è pubblico: le stime sono per categoria di mercato, confidence bassa.
- Il nodo regolatorio T3 (Certified Category probabile per MTOM>150kg) è segnalato ma non risolto in questo documento — richiede lavoro dedicato di `aviation-regulatory-counsel`/`regulatory-adversary` prima di ogni commitment.
- L'architettura modulare §7 è un **framework concettuale**, non un progetto meccanico/elettrico di dettaglio — va sviluppata con `aerodynamics-structures-engineer` e `avionics-gnc-engineer` prima di essere considerata specificabile per un capitolato.
