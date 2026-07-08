# Benchmark Costi/Prestazioni delle Classi di Piattaforma Aerea — Analisi Bottom-Up

> **Volume:** Analisi bottom-up pre-Studio (ripartenza dalla variabile "classe di piattaforma")
> **Data:** 8 luglio 2026
> **Autore:** VTOL/MALE UAS Specialist (su mandato pivot strategico Firmamento Technologies)
> **Scopo:** benchmark REALE di mercato su TUTTO lo spettro di piattaforme aeree, dal multirotore COTS all'HALE stratosferico, per abilitare la scelta costi/benefici della CLASSE di piattaforma — variabile NON assunta a priori.
> **Metodologia:** ricerca di mercato (vendor pricing pubblico + benchmark analoghi) + triangolazione con i dati vendor-RFQ e financial model già raccolti nel repository per il Percorso 6A (JOUAV CW-30E / Tekever AR3).

---

## 0. Caveat epistemico prioritario

**Confidence aggregata: LOW-MEDIUM.** Questo documento riparte da zero sulla scelta di classe, quindi mescola fonti eterogenee per affidabilità:

- **Alta confidenza**: dati da contratti pubblici europei (EMSA, EDF/EuroHAPS), da modelli finanziari e vendor-RFQ già raccolti internamente da Firmamento (JOUAV CW-30E, Tekever AR3), da fonti governative USA (GAO/USAF su MQ-9).
- **Media confidenza**: listini vendor pubblici (DJI Store, Wingtra, Quantum Systems) — prezzi reali ma spesso riferiti al mercato USA, IVA/dazi UE esclusi, "starting at" non full-kit.
- **Bassa confidenza**: stime per analogia di categoria (aerostati tattici Hemeria, JOUAV CW-15, sviluppo custom box-wing) dove il prezzo non è pubblico e viene triangolato da classi di peso/mercato comparabili.
- **Valuta**: molte fonti sono in USD. Conversione indicativa 1 USD ≈ 0,92 EUR (luglio 2026, non verificata in tempo reale — usare solo come ordine di grandezza). Tutti i prezzi UE sono **DDP-escluso IVA** salvo indicato.
- **Nessun prezzo di questo documento è una quotation vendor reale per Firmamento.** Per numeri investment-grade serve RFQ formale (processo 3-6 mesi, vedi `studio-di-fattibilita/allegati/vendor-rfq/`).

---

## 1. Tabella comparativa sintetica — le 6 classi

| Classe | Esempio piattaforma | CapEx unità | OpEx/h volo | Endurance | Quota op. | Payload utile (EO+telecom) | TRL | Costo-programma servizio operativo (incl. GS, ridondanza, personale) | Soglia budget |
|---|---|---|---|---|---|---|---|---|---|
| **1. Multirotore/VTOL COTS spot** | DJI Matrice 350 RTK / WingtraOne GEN II | €11k-45k (fully equipped) | ~€15-40 (batteria+usura) | 40-60 min | <500 m AGL tipico | EO+IR 2.7 kg; **no telecom relay realistico** | **9** | €40k-120k (1 unità+payload+training+assicurazione) | **<€1M — comodo** |
| **2. Box-wing/fixed-wing C3 custom** | Concept Firmamento (three-lifting-surface, <25kg, <3m) vs COTS Quantum Trinity F90+/JOUAV CW-15 | Custom: €150k-400k *(demonstrator non certificato)* / €3-10M+ *(prodotto certificato serie)*. COTS: €17k-95k | n/d (demonstrator) / ~€30-60 (COTS) | 90 min (Trinity) – 3-5h (CW-15) | <4.500 m | 1-3 kg | **Custom: 3-4** / COTS: **9** | Demonstrator non operativo: €150-400k. Prodotto certificato serie: **€3-10M+** | **Demonstrator <€1M, ma NON eroga servizio autorizzato**; prodotto reale >€10M |
| **3. VTOL commerciale TRL 8-9 (heavy)** | JOUAV CW-30E (CN) / Tekever AR3 (PT) | €80k-450k piattaforma | stimato €150-400/h (fuel+manut.+ammortamento) | 6-16h | 3.500-4.500 m | 8 kg (JOUAV) / 4 kg (Tekever) EO+IR+LTE relay | **8-9** | TCO 5 anni 1 unità: **€745k-1.640k** (no IVA); CapEx Y1 realistico con contingency: **€975k-1.960k** (sliding: €2,5-3,5M) | **<€1M marginale/superato**; **<decine di M€ con ridondanza** |
| **4. Aerostato tethered/free-flying** | Elistair (tethered drone) / Hemeria White Hawk (LTA tattico) | €20k-130k (tethered drone) / stima €150k-500k (aerostato LTA 20kg payload) | ~€10-30 (genset+usura tether) | **teorica illimitata** (alim. da terra); pratica 5-24h continui/ciclo | 100-1.000 m AGL (limite tether) | fino 20 kg (White Hawk): EO+IR+**relay 4G realistico** | **8-9** | 1 unità + genset + winch + spare: **€150k-700k** | **<€1M per singolo sito fisso** |
| **5. MALE (classe Tekever AR5)** | Tekever AR5 (PT) / Hermes 900 (IL, benchmark) | €2-8M+ (stima, no listino pubblico) | stimato €800-3.000/h | 16-20h | ~4.000-9.000 m | 6 kg; SAR/EO/IR/relay modulare | **8-9** (Tekever, battle-proven) | Benchmark reale: **contratto EMSA €30-35M / 4 anni / 4 velivoli "as-a-service"** ≈ €7,5-8,75M/anno | **>€1M sempre; ordine "decine di M€"** |
| **6. HALE stratosferico** | Zephyr (Airbus), PHASA-35 (BAE), Skydweller | n/a (non in produzione seriale) | n/a | settimane-mesi (mai dimostrato in inverno UE) | 18-24 km | modulare (relay 3GPP + EO) | **3-5** (nessuno operativo commerciale) | **$50M-1B+ per programma** (min $50-150M lean militare; median $200-400M; max $500M-1B+) | **Centinaia di M€ — impossibile per Firmamento standalone** |

*Fonti dettagliate e confidence per riga nelle sezioni 2-7. Righe 3 e 6 sono ancorate a dati già raccolti nel repository (vendor-RFQ M+3, DR-014 chiuso); righe 1-2-4-5 sono ricerca nuova per questo documento.*

---

## 2. Classe 1 — Multirotore/VTOL COTS per EO spot

**Esempi:** DJI Matrice 350 RTK, WingtraOne GEN II (WingtraRAY 2026 anche disponibile).

| Parametro | Valore | Fonte | Confidence |
|---|---|---|---|
| DJI M350 RTK — solo piattaforma | $11.129-14.814 (Worry-Free Combo) | [DJI Store](https://store.dji.com/product/m350-rtk-and-dji-care-enterprise-basic), [Alibaba pricing guide](https://electronics.alibaba.com/question/dji-matrice-350-rtk-price-guide-what-you-really-pay-in-2024) | medium (listino USA, no IVA UE) |
| DJI M350 — sistema completo EO+termico (H20T/H30T + accessori) | $25.000-45.000 | Ricerca aggregata vendor USA | medium |
| WingtraOne GEN II — kit base | $29.000 (~€27k) | [Robotomated ROI calc 2026](https://robotomated.com/explore/drone/wingtra-one-gen2) | medium |
| WingtraOne — costo di proprietà annuo | 8-12% del prezzo d'acquisto ($2.320-3.480/anno) | stessa fonte | medium |
| Endurance | 40-60 min (M350: 55 min max; Wingtra: 59 min) | vendor | high |
| Payload | M350: 2,7 kg (fino 3 sensori Zenmuse simultanei) | [DJI specs](https://enterprise.dji.com/matrice-350-rtk/specs) | high |
| TRL | 9 (migliaia di unità in campo, mercato PA maturo in Italia) | osservazione diretta mercato | high |

**Lettura:** questa classe è **il servizio "spot" più economico in assoluto**. Un CapEx totale (piattaforma + payload EO/IR + assicurazione + formazione 1 pilota) resta **comodamente sotto €80-120k**. L'OpEx è quasi trascurabile (usura batterie ~$90/volo secondo un case study citato, nessuna GCS fissa necessaria).

**Limite strutturale:** endurance 40-60 minuti e range LOS/O3 limitato (15-20 km tipico) rendono **impossibile qualunque forma di persistenza o connettività continua**. È lo strumento giusto per mapping periodico, sopralluoghi post-evento, monitoraggio agricolo/forestale a cadenza settimanale — **non** per "il mestiere di un satellite anche se limitato". Non trasporta payload telecom relay realistico (peso/energia insufficienti per un nodo NTN utile).

---

## 3. Classe 2 — Fixed-wing/box-wing C3 custom vs COTS equivalente

Questo è il cuore della domanda di falsificazione del pivot: **l'idea box-wing di Firmamento** (concept in `Progetto concettuale struttura HALE.md`, configurazione three-lifting-surface ispirata al Piaggio P180, categoria C3 EASA: MTOM <25 kg, apertura <3 m) può stare sotto €1M come sviluppo custom, o conviene un COTS equivalente?

### 3.1 COTS equivalenti di classe C3

| Piattaforma | Prezzo | Specifiche | Fonte | Confidence |
|---|---|---|---|---|
| **Quantum Trinity F90+** (DE) | ~$18.300 (~€17k) kit base | 8 kg MTOW, 90+ min endurance, payload modulare | [Quantum Systems](https://quantum-systems.com/wp-content/uploads/2023/01/QS_TrinityF90_Overview_220912.pdf), ricerca web | medium |
| **JOUAV CW-15** (CN) | non pubblico; stima $35-100k (~€33-93k) per analogia scalata da CW-30E ($50-150k base) | 14 kg MTOW, 3-5h endurance (vendor), 3 kg payload | [JOUAV](https://www.jouav.com/products/cw-15.html) + triangolazione interna | **low** (nessun prezzo pubblico) |
| **WingtraOne GEN II** | $29.000 | vedi Classe 1 (al margine tra le due classi) | vedi sopra | medium |

### 3.2 Costo di sviluppo custom (box-wing Firmamento)

Non esiste un prezzo di mercato diretto: va costruito per analogia. Due scenari radicalmente diversi:

**(a) Dimostratore sperimentale non certificato** (1 esemplare, no serie, no declaration of conformity EASA):
- Ingegneria (aerodinamica, strutture, avionica integrata da COTS), fabbricazione in composito, banco prova, primi voli sperimentali: stima **€150k-400k**, 12-24 mesi, team piccolo (2-4 persone + consulenza esterna).
- **Confidence: low** — nessun dato pubblico diretto; stima per analogia con progetti universitari/startup pre-seed di categoria simile (letteratura tecnica su UAV a basso costo conferma che la fabbricazione di un singolo esemplare in composito è dell'ordine delle decine-centinaia di k€, non milioni — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2090447922004051), [MATEC](https://www.matec-conferences.org/articles/matecconf/pdf/2018/18/matecconf_ijcaet-isampe2018_02045.pdf)).
- **Ma questo dimostratore NON è un "servizio"**: senza declaration of conformity C3 (Modulo A **non disponibile** per C1-C3, serve EU-type examination o quality assurance totale tramite Notified Body — [EASA/EU Drone Port](https://eudroneport.com/blog/certification-requirements-class-c3-drones/)) non può operare in Specific Category in modo ripetibile e assicurabile per conto terzi (PA, cooperative) senza un'autorizzazione ENAC ad hoc caso per caso.

**(b) Prodotto certificato, industrializzato, supportabile in serie** (il livello a cui operano oggi Quantum Systems, Wingtra, JOUAV):
- Benchmark indiretto: **Wingtra** (spin-off ETH Zurigo 2016) ha impiegato ~8 anni e **oltre $60M cumulati** in funding ([TechCrunch](https://techcrunch.com/2023/03/21/wingtra/), [DroneXL](https://dronexl.co/2024/08/19/swiss-drone-startup-wingtra-secures-23-million/), [Tracxn](https://tracxn.com/d/companies/wingtra/__79a4sNNtPI_WTjMVwCJkuIhHaVtAptaRnbziH-AUyhU)) per arrivare da prototipo a leader di mercato C3-class globalmente supportato. **Quantum Systems** (fondata 2015, oggi valutata $8 mld dopo Series D $1,2 mld) ha impiegato anni e decine di milioni pre-scale-up solo per il primo prodotto commerciale maturo (Trinity F90) prima del pivot verso il mercato difesa ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-02/quantum-systems-more-than-doubles-valuation-to-8-billion-in-new-round), [Quantum Systems Series B](https://quantum-systems.com/us/news/series-b-funding-round/)).
- Anche scontando pesantemente questi benchmark per un "minimo vitale IT-only" (niente scale-up internazionale, niente rete vendita globale), un percorso realistico per arrivare a un box-wing C3 **certificato e supportabile** resta dell'ordine di **€3-10M+** (ingegneria, certificazione Notified Body, industrializzazione, prove di volo estese, supporto post-vendita).
- **Confidence: low-medium** — proxy da funding VC, non da costing diretto di programma; il funding VC include anche vendite/marketing, quindi è un limite superiore, non un costo di sviluppo puro. Ma anche dimezzando la stima resta **un ordine di grandezza sopra €1M**.

### 3.3 Verdetto Classe 2

**FALSIFICATO: un box-wing C3 custom NON sta sotto €1M se si intende "prodotto in grado di erogare un servizio operativo autorizzato".** Sta sotto €1M (anzi sotto €400k) **solo** come dimostratore sperimentale non certificato — utile come banco di prova tecnologico/IP per la visione HALE a lungo termine, **non** come piattaforma per il pilota Pentema Y1. Per il servizio comparabile, un COTS equivalente (Quantum Trinity F90+ o JOUAV CW-15, €17-95k) costa **1-2 ordini di grandezza meno** e arriva subito a TRL 9.

---

## 4. Classe 3 — VTOL commerciale TRL 8-9 (heavy)

Questa classe è già stata oggetto di lavoro RFQ preliminare nel repository (`studio-di-fattibilita/allegati/vendor-rfq/VENDOR-QUOTATION-ANALYSIS-JOUAV-TEKEVER.md`, M+3, confidence low-medium). Riprendo qui i dati già raccolti perché restano il riferimento più solido del dataset:

| Voce | JOUAV CW-30E (CN) | Tekever AR3 (PT) | Confidence |
|---|---|---|---|
| Piattaforma base | €80-180k | €250-450k | medium |
| CapEx Y1 completo (piattaforma+GS+payload+training+spare, no IVA) | **€580-820k** | **€850-1.250k** | low-medium |
| TCO 5 anni (no IVA) | **€745-1.120k** | **€1.065-1.640k** | low |
| Lead time | 6-9 mesi (best) / 9-14 (worst, rischio geopolitico CN) | 8-12 mesi (best) / 12-16 (worst, backlog NATO) | medium |
| Endurance (datasheet vendor) | 6-10h | 8h VTOL / 16h fixed-wing | medium (non validato operatori EU indipendenti) |
| Payload | 8 kg | 4 kg | high |

**Cross-check con il modello finanziario Firmamento** (`studio-di-fattibilita/allegati/financial-model/README.md`): il CapEx Y1 baseline del Percorso 6A completo (non solo piattaforma, ma intero pilota con contingency) è **€1,4M (range €0,97-1,96M)**, e lo stesso modello segnala che il **CapEx Y1 realistico "sliding timeline" è €2,5-3,5M** — quasi il **triplo** della stima nominale iniziale di €0,7-2M. Questo è un dato interno importante: **anche la piattaforma "a basso rischio" del Percorso 6A, se costata con rigore (redundancy, GS, formazione, contingency, sliding), supera già €1M**, e con margine.

**Lettura:** una singola unità VTOL heavy per missioni **schedulate non persistenti** (2-4 uscite/settimana, poche ore ciascuna) può stare nell'intorno di **€600k-1,6M TCO 5 anni** — al margine superiore della soglia "ideale <€1M", dentro la soglia "accettabile <decine di M€". Con ridondanza minima (2-3 unità, necessaria per qualunque forma di continuità di servizio, vedi §8) il costo sale a **€2-5M**, ben dentro la fascia "decine di milioni" ma lontano da "centinaia".

---

## 5. Classe 4 — Aerostato tethered o free-flying

Classe poco esplorata nel repository esistente ma potenzialmente rilevante per Pentema: offre **persistenza h24 nativa** (alimentazione da terra via tether) senza il moltiplicatore di flotta richiesto da VTOL/MALE (vedi §8).

| Piattaforma | Tipo | Prezzo | Specifiche | Fonte | Confidence |
|---|---|---|---|---|---|
| **Elistair** (varie: Safe-T2, Ligh-T, Khronos) | Tethered multirotore su tether (non aerostato LTA) | **€20.000-130.000** sistema completo (no payload) | Endurance teorica illimitata (alim. da terra); pratica 5-8h standard, >24h rinforzati; quota ~100-150m AGL | [Elistair](https://elistair.com/), ricerca web aggregata | medium |
| **Hemeria White Hawk** (tactical) | Aerostato LTA (elio) tattico | non pubblico; stima **€150k-500k** per classe/categoria mercato | Diametro min. 4,4m, payload fino **20 kg** (gimbal EO/IR + **relay 4G**) | [Hemeria](https://www.hemeria-group.com/en/product/tactical-tethered-aerostat-systems/) | **low** (nessun prezzo pubblico, stima per analogia di categoria) |
| **Hemeria Eagle Owl** (strategic) | Aerostato LTA maggiore | non pubblico, ordine di grandezza superiore | 19m+, payload fino 120 kg | Hemeria | low |
| **TCOM PSS-T** (benchmark scala militare) | Grande flotta persistente USA | **$978.946.631** contratto supporto pluriennale flotta | Riferimento "top of range", fuori scala per Pentema | [Army Technology](https://www.army-technology.com/news/us-dod-awards-tethered-aerostat-support-contract-to-tcom/) | high (ma non applicabile) |

**Vantaggio strutturale:** un'unica unità tethered fornisce **presenza quasi continua su un punto fisso** senza bisogno di rotazione di flotta — il tether alimenta il sistema da terra, eliminando il vincolo "batteria/carburante" che impone soste a VTOL e multirotori. Il payload di classe Hemeria White Hawk (20 kg) è **fisicamente compatibile con EO+IR+relay 4G/LTE simultanei**, l'unica classe sotto €1M in cui questo è vero.

**Rischio critico per Pentema:** i sistemi tethered hanno limiti operativi di vento tipicamente **~15-20 m/s sostenuti**. Il CLAUDE.md di progetto e il contesto Pentema descrivono esplicitamente **vento canalizzato e wind shear in valle stretta** — condizione sfavorevole per un asset ancorato a un punto fisso. L'uptime reale in inverno a Pentema potrebbe scendere significativamente sotto la disponibilità nominale dichiarata dai vendor (che è tipicamente per siti pianeggianti/costieri, non orografia alpina). **Nessun dato indipendente conferma le prestazioni di un aerostato tattico in una valle ligure a 1.100-1.300 m s.l.m.: verifica sul campo necessaria prima di ogni impegno di budget.**

**Verdetto:** questa è, sui dati raccolti, **la piattaforma con il miglior rapporto persistenza/costo sotto €1M** — ma solo se il vincolo del vento in valle è gestibile (da verificare con anemometria locale prima di qualunque commitment) e solo per copertura di **un singolo punto fisso**, non dell'intera vallata.

---

## 6. Classe 5 — MALE (classe Tekever AR5)

| Parametro | Valore | Fonte | Confidence |
|---|---|---|---|
| **Tekever AR5** — MTOW | fino 180 kg (una fonte cita 500 kg come massimo assoluto in altra configurazione) | [militaryfactory.com](https://www.militaryfactory.com/aircraft/detail.php?aircraft_id=1457), [Tekever](https://www.tekever.com/ar5/) | medium |
| Endurance | fino 20h (alcune fonti: >12h operativo) | stesse | medium |
| Range C2 | fino 230 km | stesse | medium |
| Payload | 6 kg (EO/IR/SAR modulare) | stesse | medium |
| **Prezzo unitario** | **non pubblico** | — | — |
| **Contratto EMSA 2025/2026** | **€30-35M / fino 4 anni / 2 sistemi × 2 UAS (4 velivoli totali)**, modello "RPAS-as-a-Service" (Tekever fornisce anche equipaggio/operazioni, non solo hardware) | [UST](https://www.unmannedsystemstechnology.com/2025/11/tekever-secures-emsa-agreement-for-ar5-fixed-wing-uas-deployment/), [UAS Vision](https://www.uasvision.com/2026/03/05/tekever-gets-35m-emsa-contract-for-ar5-fixed-wing-uas-deployment/), [defence-industry.eu](https://defence-industry.eu/emsa-awards-tekever-new-e30-million-contract-to-expand-ar5-fixed-wing-uas-operations-in-europe/) | **high** (contratto pubblico UE) |
| **Hermes 900** (Elbit, benchmark generale MALE) | $6,85-30M/unità (range ampio, dipende da configurazione/contratto) | [ricerca stampa aggregata](https://top10express.com/top-10-military-drones-price/), [X/Elbit](https://x.com/unityoffields/status/1935351508364579110) | low-medium (range troppo ampio per essere affidabile puntualmente) |
| **MQ-9 Reaper** (benchmark top-of-range, non comparabile 1:1 civile) | $16,9-30M/unità flyaway; CPFH $3.000-4.000 diretto, fino **$12.000 fully-loaded** (GAO) | [GAO/USAF via ricerca aggregata](https://www.cbo.gov/publication/57260) | medium-high (fonte governativa, ma esemplare militare non paragonabile) |

**Lettura chiave:** il dato più solido e utilizzabile per Firmamento è il **benchmark EMSA**: **€30-35M per 4 anni per un servizio ISR quasi-continuo multi-sito europeo, equipaggio incluso** ≈ **€7,5-8,75M/anno**. Questo conferma empiricamente perché la classe MALE serva quando il requisito è "**davvero** >€1M e verso la decina di milioni": non è il prezzo del velivolo da solo a spingere il costo in questa fascia, è il **modello operativo persistente con equipaggio dedicato** (si veda §8).

Per il caso Pentema, il MALE è quasi certamente **sovradimensionato**: progettato per missioni marittime/ISR su area vasta (100-230 km di raggio), non per un singolo borgo di poche migliaia di abitanti. Resta utile come benchmark di "quanto costa un vero servizio aereo persistente multi-anno con un solo aeromobile long-endurance e crew dedicato" — la risposta è **ordine di grandezza €10-40M**, non €1-5M.

---

## 7. Classe 6 — HALE stratosferico

Questa sezione **non richiede nuova ricerca**: il repository ha già chiuso (parzialmente) il DR-014 "Capital intensity HAPS perennial" con fonti istituzionali di alta confidenza (`riferimenti/DR-research-closure-M3.md`, righe 253-294). Riporto qui la sintesi perché è il termine di paragone "impossibile" richiesto dal mandato:

| Programma | Costo cumulato stimato | Fonte | Confidence |
|---|---|---|---|
| **BAE PHASA-35 / Prismatic** | $50-150M (2018-2024, programma "snello" militare UK MoD) | [Wikipedia](https://en.wikipedia.org/wiki/BAE_Systems_PHASA-35), [Aviation Week](https://aviationweek.com/defense/aircraft-propulsion/bae-built-stratospheric-aircraft-wins-five-year-afrl-contract) | medium-high |
| **Skydweller Aero** | $48M raised (Series A $40M 2021, Leonardo lead investor) | [PR Newswire](https://www.prnewswire.com/news-releases/skydweller-aero-inc-raises-40m-in-oversubscribed-series-a-funding-round-to-continue-rapid-technological-development-to-meet-demand-for-persistent-flight-301371942.html), [CB Insights](https://www.cbinsights.com/company/skydweller-aero) | high |
| **EuroHAPS** (EDF, consorzio TAS/CIRA/Leonardo) | €63,5M (di cui €43M EU), 38 mesi, 21 partner — solo **dimostrazione MVP scala ridotta**, non prodotto operativo | [EU funding page](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/projects-details/44181033/101103150/EDF) | very high |
| **SoftBank Sunglider/HAPSMobile** | stima industry $200-500M cumulati 2017-2024 | ricerca interna repo | medium |
| **Airbus Zephyr** | $200-400M+ cumulati su 20+ anni di programma | ricerca interna repo | medium |
| **Sceye** (privato US) | stima industry $100-200M cumulati 2013-2025 | ricerca interna repo | low-medium |

**Benchmark consolidato (dal repo, DR-014):** minimo **$50-150M**, mediana **$200-400M**, massimo **$500M-1B+**. **Nessuno dei 12 programmi HALE solari avviati globalmente dal 2003 è oggi operativo commercialmente con revenue >$1M** (DR-013, chiuso: 42% cancellati, 42% slittati permanentemente, 17% solo dimostrazione governativa, 0% operativo commerciale). Questo colloca la classe HALE **inequivocabilmente nella fascia "centinaia di milioni di euro — impossibile"** per un attore come Firmamento in autonomia; l'unico percorso realistico è la partnership di minoranza con un prime contractor (Aalto/Skydweller/TAS-Leonardo/CIRA), non lo sviluppo in-house.

---

## 8. Il moltiplicatore della persistenza: perché "un velivolo" non basta per un servizio h24

Il mandato segnala correttamente che per connettività/EO **persistente** su un'area non basta un velivolo: servono N unità in rotazione per coprire 24h, più equipaggio su turni, più manutenzione programmata. Questo moltiplica i costi in modo non lineare e va tenuto esplicito in ogni confronto tra classi:

| Classe | Meccanismo del moltiplicatore | N unità stimate per continuità reale | Impatto |
|---|---|---|---|
| **1. Multirotore/VTOL COTS** | Endurance 40-60 min: impossibile qualunque persistenza; non ha senso "moltiplicare", va accettato come servizio spot | n/a (non persistente per design) | resta sotto €1M **solo se si rinuncia alla persistenza** |
| **2. Box-wing C3** | Endurance 90 min-5h: persistenza solo con più unità in staffetta ravvicinata | 4-6+ per coprire 24h con margini di turnaround | il custom certificato passa da €3-10M a decine di M€ |
| **3. VTOL heavy (JOUAV/Tekever)** | Endurance 6-16h + turnaround batteria/carburante + turni piloti (BVLOS in Italia oggi vincolato prevalentemente a operazioni diurne/VFR-adjacent) | tipicamente **2-3 velivoli** (1-2 attivi + 1 riserva/manutenzione) + più piloti in turno | CapEx piattaforme ×2-3 **e** OpEx piloti/manutenzione cresce più che proporzionalmente (regole di turno) → sposta la classe da "€1M marginale" a "**€2-5M** realistico per continuità" |
| **4. Aerostato tethered** | Alimentazione da terra: nessun turnaround energetico; il vincolo è manutenzione programmata e meteo (vento) | **1 unità operativa + eventuale unità di riserva/parti** (N≈1,5-2) | moltiplicatore **minimo** tra tutte le classi — è il vero vantaggio strutturale di questa classe per un singolo sito |
| **5. MALE (Tekever AR5)** | Endurance 16-20h riduce il numero di cambi/giorno, ma restano necessarie ridondanza tecnica e turni di equipaggio dedicato H24 | **2+ velivoli** per un'orbita quasi-continua + crew multipla | il benchmark EMSA (€7,5-8,75M/anno per 4 velivoli multi-sito con equipaggio) **è già** il costo di un servizio persistente reale — conferma che questa classe vive strutturalmente sopra €1M |
| **6. HALE** | Endurance nominale settimane/mesi **elimina in teoria** il moltiplicatore giornaliero, ma (a) il bilancio energetico invernale a 44°N non è risolto secondo la stessa analisi Firmamento (Cap. 6 §6.2.2.3 / A.3.4: E5 Seasonal-only, no perennial), e (b) anche i pochi operatori HAPS al mondo pianificano **costellazioni**, non singoli assetti, per guasti/manutenzione | flotta multi-unità anche a regime | irrilevante come discriminante: la classe è già fuori scala per altri motivi (§7) |

**Regola pratica desunta (letteratura ISR generale, non dato Firmamento):** per un'unica "orbita" ISR realmente 24/7 con piattaforme ad autonomia medio-lunga, la prassi consolidata nel settore difesa/ISR converge tipicamente su **3-4 assetti per orbita** (mix volo attivo + turnaround/manutenzione + riserva). Questo è un fattore, non un dato puntuale Firmamento: va validato con un CONOPS dedicato prima di ogni commitment di budget.

**Implicazione diretta per Pentema:** se l'obiettivo Y1 è "presenza quasi-continua su un punto" (es. hotspot connettività + monitoraggio ambientale del borgo), **l'aerostato tethered è l'unica classe che risolve il problema della persistenza senza moltiplicare il numero di velivoli**. Se l'obiettivo è "missioni programmate ripetute" (mapping periodico, sopralluoghi Protezione Civile su innesco evento), **il VTOL COTS heavy a singola unità (JOUAV/Tekever classe) resta la scelta più equilibrata**, accettando che non è persistenza reale.

---

## 9. Mappatura contro le soglie di finanziabilità

| Soglia | Classi che rientrano | Condizioni |
|---|---|---|
| **Ideale <€1M** | **Classe 1** (sempre, ma solo servizio spot). **Classe 4** (aerostato tethered singolo sito, 1 unità, CapEx+alcuni anni OpEx). **Classe 3** al margine (1 unità JOUAV, missioni schedulate non persistenti, TCO 5 anni €745k-1,1M) — ma il modello finanziario interno Firmamento stesso segnala sliding a €2,5-3,5M se costato con rigore pieno. **Classe 2** solo come demonstrator non certificato (non eroga servizio autorizzato) | Nessuna persistenza reale, o persistenza solo su singolo punto fisso |
| **Accettabile <decine di M€** | **Classe 3** con ridondanza (2-3 unità, €2-5M). **Classe 4** multi-sito o con piena ridondanza. **Classe 5** MALE (benchmark EMSA reale: €30-35M/4 anni per 4 velivoli con equipaggio, ≈€7,5-8,75M/anno) | Copertura area più ampia, persistenza parziale/multi-sito |
| **>€10M difficile** | Classe 5 MALE con flotta ridondante multi-sito estesa; Classe 2 "prodotto certificato da zero" (€3-10M+, al margine di questa soglia) | Servizio persistente su larga scala regionale |
| **Centinaia di M€ impossibile** | **Classe 6 HALE** ($50M-1B per programma, confermato da fonti istituzionali già triangolate nel repo) | Fuori portata per Firmamento standalone; solo partnership di minoranza |

---

## 10. Punto chiave e falsificazione

**Domanda:** qual è la piattaforma MINIMA che eroga un servizio utile stando sotto €1M?

**Risposta articolata su due letture del requisito:**

1. **Se "servizio utile" = missioni spot non persistenti** (mapping periodico, monitoraggio ambientale a cadenza settimanale/mensile, sopralluoghi Protezione Civile su innesco): la **Classe 1 (DJI M350/WingtraOne)** eroga valore reale a **€40-120k**, un ordine di grandezza sotto la soglia. Non fa "il mestiere di un satellite" in alcun senso di persistenza, ma è economicamente il punto di ingresso più basso con TRL 9 comprovato.

2. **Se "servizio utile" = una qualche forma di presenza/connettività persistente** (anche solo su un hotspot, anche solo diurna): la **Classe 4 (aerostato tethered piccolo, tipo Elistair o Hemeria White Hawk)** è l'unica piattaforma che risolve il problema della persistenza **senza moltiplicatore di flotta**, restando **sotto €1M** (CapEx €150-700k + OpEx contenuto). Il vincolo critico non testato è il **vento canalizzato di valle a Pentema** — nessun dato indipendente conferma le prestazioni reali in questa orografia specifica, verifica anemometrica sul campo è prerequisito prima di ogni commitment.

**Sulla domanda specifica del box-wing custom C3:** **FALSIFICATO che un box-wing custom <25kg possa stare sotto €1M come prodotto capace di erogare un servizio operativo autorizzato**. Sta sotto €1M (anzi sotto €400k) **solo** come dimostratore sperimentale non certificato — utile eventualmente come banco di prova IP/tecnologico per la traiettoria HALE a lungo termine, non come piattaforma del pilota Pentema. Portarlo a "prodotto certificato e supportabile" costa, per analogia con i percorsi reali di Wingtra e Quantum Systems, **€3-10M+** — lo stesso ordine di grandezza di una piccola flotta di VTOL COTS ridondante (Classe 3).

---

## 11. Verdetto: build custom vs buy COTS

**BUY COTS vince nettamente per l'orizzonte 0-24 mesi del pilota Pentema.**

- Il costo di sviluppo di un velivolo custom certificato (anche piccolo, categoria C3) è **dello stesso ordine di grandezza** (milioni-decine di milioni) del costo di acquisto di una **intera piccola flotta ridondante** di VTOL COTS (Classe 3) o di più unità di Classe 4.
- Il mercato COTS copre già lo spettro di payload/endurance rilevante per Pentema: da 40 min/2,7kg (Classe 1) a 8-16h/8kg (Classe 3), passando per la persistenza nativa dell'aerostato (Classe 4). **Non emerge, da questa ricerca, un gap di requisito che solo un box-wing custom potrebbe colmare.**
- Costruire da zero ha senso **solo** se l'obiettivo dichiarato è diverso da "minimizzare il costo del servizio Pentema": ad esempio se il box-wing è concepito esplicitamente come **banco di prova tecnologico/IP** in vista della traiettoria HALE (Percorso 6B), separando così l'investimento in R&D dalla decisione di procurement per il servizio Y1.
- Se questa distinzione non viene fatta esplicitamente nella governance del progetto, il rischio è di spendere risorse paragonabili a quelle di un COTS heavy ridondante (Classe 3, €2-5M) per ottenere un **singolo dimostratore non certificabile in tempi brevi**, senza guadagnare nulla in termini di servizio operativo a Pentema.

---

## 12. Fonti e confidence complessiva

**Fonti interne al repository (alta confidence per il dato Firmamento, ma già dichiarate low-medium alla fonte):**
- `studio-di-fattibilita/allegati/vendor-rfq/VENDOR-QUOTATION-ANALYSIS-JOUAV-TEKEVER.md` — Classe 3
- `studio-di-fattibilita/allegati/vendor-rfq/vendor_comparison_matrix.csv` — Classe 3
- `studio-di-fattibilita/allegati/financial-model/README.md` — Classe 3, cross-check CapEx Y1
- `riferimenti/DR-research-closure-M3.md` (DR-013, DR-014) — Classe 6
- `Progetto concettuale struttura HALE.md` — concept box-wing Classe 2
- `da revisionare/Briefing_...md`, `da revisionare/Relazione Tecnica Comparativa...md` — contesto strategico Percorso 6A/6B (letti criticamente, non assunti)

**Fonti web nuove per questo documento (Classi 1, 2, 4, 5; confidence dichiarata per riga nelle sezioni 2-7):** DJI Store/Enterprise, Wingtra/Robotomated, Quantum Systems, JOUAV, Elistair, Hemeria, Tekever AR5 (UST/UAS Vision/defence-industry.eu), EMSA press, GAO/CBO su MQ-9, TechCrunch/Bloomberg/CB Insights su funding Wingtra/Quantum Systems/Skydweller.

**Limiti dichiarati:**
- Nessuna quotation reale ricevuta da vendor per questo documento — tutti i numeri sono stime pubbliche o benchmark analoghi.
- I prezzi USD non sono stati verificati con tasso di cambio in tempo reale.
- La regola "3-4 assetti per orbita 24/7" (§8) è una prassi di settore ISR generale, non un dato calcolato per Pentema — richiede CONOPS dedicato.
- Le prestazioni di aerostati tethered in valle stretta con vento canalizzato (Pentema) non sono documentate da alcuna fonte: è un gap di conoscenza esplicito, non un'assunzione.
