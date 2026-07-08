# R2 — Competitor Intelligence (ricerca approfondita con fonti verificate)

**Data:** luglio 2026
**Autore:** competitor-intelligence (vista avversariale)
**Mandato:** verificare con fonti reali i claim sui competitor dei report `21`, `11`, `12` di `analisi-bottom-up/`, che erano marcati "stima/confidenza bassa".
**Metodo:** WebSearch estensivo (WebFetch bloccato 403 lato-sito su quasi tutti i media/corporate — contenuto recuperato via motore di ricerca, URL primari sempre citati). Fonti salvate in `fonti/`.
**Regola:** nessuna affermazione su un competitor senza URL.

---

## A. Tabella di verifica — claim → fonte(URL) → verdetto → confidenza

| # | Claim (origine) | Fonte primaria (URL) | Verdetto | Confidenza prima → dopo |
|---|---|---|---|---|
| 1a | **Quantum Systems: $1,2B round @ $8B val., lug 2026** (rep. 21) | [CNBC](https://www.cnbc.com/2026/07/02/autonomous-defense-startup-quantum-systems.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-02/quantum-systems-more-than-doubles-valuation-to-8-billion-in-new-round), [Tech Startups](https://techstartups.com/2026/07/02/german-drone-startup-quantum-systems-raises-1-2b-at-8b-valuation-as-investors-pour-billions-into-ai-defense/) | ✅ **VERO** — Series D, $1,2B, post-money ~$8B, co-lead Blackstone/Airbus/Advent/Noteus, 2 lug 2026. Largest private defense-tech round europeo. | bassa → **alta** |
| 1b | **ITAR-free (MOSAIC)** (rep. 21) | [Militarnyi](https://militarnyi.com/en/news/quantum-systems-unveils-mosaic-uxs-system-in-ukraine/), [Quantum blog](https://quantum-systems.com/blog/2025/06/03/quantum-systems-launches-mosaic-uxs/) | ✅ **VERO** — MOSAIC UXS "explicitly designed to be ITAR-free", C2 multi-vendor. | bassa → **alta** |
| 1c | **19.000 missioni Ucraina '25** (rep. 21) | [Ukraine Arms Monitor](https://ukrainesarmsmonitor.substack.com/p/quantum-systems-and-recce-strike), [Wikipedia](https://en.wikipedia.org/wiki/Quantum-Systems) | ⚠️ **NON VERIFICATO** — nessuna fonte cita "19.000". Confermato invece: >700 Vector consegnati, 40–80/mese di produzione, "thousands of mission hours", 3° ISR "Army of Drones 2025". | bassa → **la cifra resta bassa/da ritirare; il fatto qualitativo (combat-proven) alto** |
| 2 | **ABzero: NON produce droni; COTS + capsula brevettata + software; €190k @ €4,6M pre-money (lug'25)** (rep. 11/21) | [ABzero FAQ](https://www.abzero.it/faq/?lang=en), [Sant'Anna](https://www.santannapisa.it/en/spin/abzero-srl), [Dealroom](https://app.dealroom.co/companies/abzero) | ✅ **VERO e rafforzato** — "does not produce drones, uses commercial drones"; **5 brevetti internazionali**; compatibile **90% multicotteri COTS**; round €190k @ €4,6M pre-money, 1 lug 2025. | media → **alta** |
| 3a | **Wingcopter: $16M Spright + $42M round; vende+DaaS** (rep. 11/21) | [MobiHealthNews](https://www.mobihealthnews.com/news/emea/german-drone-pioneer-wingcopter-snaps-16m-contract-spright), [DroneLife](https://dronelife.com/2022/06/22/wingcopter-funding-42-million-in-latest-round-over-60-million-total-for-drone-delivery/) | ✅ **VERO** — $16M Spright per flotta Wingcopter 198; $42M Series A ext (giu'22); modello ibrido confermato. | media → **alta** |
| 3b | **Wingcopter: $119M totale** (rep. 21) | [Tracxn](https://tracxn.com/d/companies/wingcopter/__Vg8hcC7zqUMDdA4fQsjeMuZfiFnejL9JIrsTYPyO8sQ/funding-and-investors) | 🟡 **QUASI — correggere a ~$110M** (8 round, ultimo Series B giu'25). **Nuovo dato debole:** revenue 2024 solo **$1,73M**. | media → **media (numero da correggere)** |
| 4 | **Zipline: $600M+ bruciati, non profittevole, $3–13/consegna** (rep. 11) | [TechCrunch](https://techcrunch.com/2026/01/21/zipline-charts-drone-delivery-expansion-with-600m-in-new-funding/), [Robot Report](https://www.therobotreport.com/zipline-raises-over-600m-in-funding-surpasses-2m-commercial-drone-deliveries/) | ✅ **VERO ma da aggiornare al rialzo** — val. **$7,6B**, **>$600M** (gen'26) **+$200M** (mar'26), **>2M consegne** cumulate. Non più "solo brucia": è il leader USA capitalizzato che scala. | media → **alta** |
| 5a | **Matternet: ibrido razor-and-blades, UPS/Swiss Post** (rep. 21) | [BusinessWire](https://www.businesswire.com/news/home/20260528964448/en/), [DroneLife](https://dronelife.com/2026/05/28/matternet-drone-delivery-raises-33m-and-goes-public-in-reverse-merger/) | ✅ **VERO + update** — **$33M** + **quotata** (reverse merger, mag'26), **unica FAA type-certified**, **>60k voli**, UPS/Swiss Post/NHS. | media → **alta** |
| 5b | **DJI FlyCart / Meituan (cargo cinese)** (rep. 11) | [DJI specs](https://www.dji.com/flycart-30/specs), [DroneDJ](https://dronedj.com/2024/11/25/dji-delivery-flycart-30-drone/) | ✅ **VERO** — FlyCart 30 payload 30 kg, TC CAAC; Meituan **>450k consegne** 2024, 53 rotte, co-leader con Wing. | bassa → **alta** |
| 5c | **Dronamics (cargo middle-mile): operativo** | [Autoevolution](https://www.autoevolution.com/news/the-real-cargo-drone-dronamics-black-swan-is-simple-capable-and-coming-soon-257766.html), [FlightGlobal](https://www.flightglobal.com/defence/dronamics-to-adapt-black-swan-cargo-drone-for-surveillance-tasks/166321.article) | 🟡 **PARZIALE/DEBOLE** — LUC EU + IATA/ICAO ottenuti, 350kg/2500km, ma **nessun servizio cargo a ricavo** a fine 2025; **pivot alla difesa** (Hensoldt ISR, feb'26). | n/a → **media** |
| 6 | **Moat "sovranità EU dual-use" già presidiato** (rep. 21) | [Helsing/TechCrunch](https://techcrunch.com/2026/05/11/daniel-ek-backed-defense-tech-helsing-to-raise-1-2b-at-18b-valuation/), [Tekever/Tech.eu](https://tech.eu/2025/05/06/tekever-becomes-the-latest-unicorn-in-europes-defencetech-industry/), [NIF](https://www.nif.fund/news/nato-innovation-fund-backed-tekever-becomes-europes-newest-unicorn/) | ✅ **VERO e più grave** — **3 giganti**: Helsing **€12B→$18B**, Quantum **$8B**, Tekever **$1,33B**. Backing NATO Innovation Fund + Airbus. | bassa → **alta** |

---

## B. Chi occupa già lo spazio che Firmamento vorrebbe

Mappa avversariale per segmento (tutto verificato con URL in `fonti/`):

**1. Sovranità EU / dual-use / non-cinese (l'unico moat concepibile per un Firmamento-prodotto):**
Già capitalizzato per **decine di miliardi** da **Helsing ($18B)**, **Quantum ($8B)**, **Tekever ($1,33B)**. Il capitale sovrano EU (NATO Innovation Fund, Airbus, Blackstone) si concentra sui pochi vincitori. **Airbus co-investe in Quantum** invece di difendersi — segnale che la finestra è chiusa per i newcomer. Firmamento qui non è competitor: è, al più, fornitore di nicchia o target di acquisizione difensiva.

**2. Logistica medicale (la nicchia più citata come "accessibile"):**
- **ABzero (IT)** — incumbent nazionale: 5 brevetti, 90% COTS-compatibile, track-record BVLOS, Sant'Anna. Occupa *esattamente* il pattern-moat (bundle IP+SW+servizio) indicato come unica via difendibile.
- **Wingcopter (DE)** — leader hardware EU (198), ~$110M, ma revenue 2024 solo $1,73M.
- **Matternet (US)** — FAA type-cert, quotata, Swiss Post/UPS/NHS.
- **Zipline (US)** — $7,6B, 2M consegne (extra-EU prevalente).

**3. Cargo / delivery di massa:**
- **DJI FlyCart 30 + Meituan** (muro-prezzo cinese, 450k consegne).
- **Dronamics** — cargo middle-mile che *non* ha trovato ricavi civili → pivot difesa.

**4. ISR/EO-persistenza sovrana (dove il box-wing loiter *sarebbe* l'airframe giusto):**
Presidiata da **Quantum**, **Tekever** (Intelligence-as-a-Service, EMSA), **JOUAV/Wingtra** (ereditati rep. 05/10). Moat contestato da un gigante.

**Pattern trasversale (nota avversariale forte):** *tutti* i player che partono civili gravitano verso il **dual-use/difesa** perché è lì che c'è capitale e WTP (Dronamics→Hensoldt; Quantum/Helsing/Tekever nati o pivotati sulla difesa). La logistica/EO civile pura non ripaga nemmeno i leader. Questo **conferma** e **irrigidisce** la tesi interna dei report 11/21: le nicchie civili accessibili sono sottili e contese; la scala è nel dual-use, dove però Firmamento (grant €150–400k) è irrilevante rispetto a incumbent multimiliardari.

---

## C. Verdetto sui due più citati

### Quantum Systems — competitor per la nicchia sovrana EU?
**Sì, in modo schiacciante — ma non è un competitor diretto di Firmamento: è la dimostrazione che la nicchia è già chiusa.** $8B, ITAR-free, combat-proven, co-finanziato da Airbus. Firmamento non può competere; può solo posizionarsi come fornitore/partner o accettare l'irrilevanza sul layer dual-use small-UAS. **Correzione obbligatoria:** ritirare o marcare "non verificato" la cifra "19.000 missioni" (nessuna fonte). Il resto è solido e **alto**.

### ABzero — incumbent italiano davanti a Firmamento?
**Sì, confermato in ogni dettaglio e rafforzato.** Non produce droni (COTS + capsula a 5 brevetti + software), €190k @ €4,6M pre-money (lug'25), 90% COTS-compatibile, Sant'Anna. Occupa già il pattern-moat che l'analisi interna indica come l'unica via prodotto difendibile per il medicale. Ingresso Firmamento = **follower puro**. Confidenza **alta**. *Nota:* il round minuscolo (€190k) conferma che è mercato grant/pilot-stage — reale ma piccolo, non una macchina da ricavi.

---

## D. Confidenza aggiornata (sintesi)

- **Da bassa → alta:** Quantum ($8B/ITAR-free), ABzero (modello/brevetti/round), Zipline ($7,6B/2M), Matternet (quotata/FAA), DJI-Meituan, panorama sovrano (Helsing/Tekever).
- **Da correggere:** Wingcopter totale **~$110M** (non $119M); Zipline non "solo brucia" ma leader a $7,6B.
- **Da ritirare:** "19.000 missioni Ucraina" (non corroborata).
- **Nuove aggiunte alla threat map:** **Helsing ($18B)** e **Tekever ($1,33B)** come co-occupanti dello spazio sovrano; **Dronamics** come case-study del cargo civile che non ripaga.

---

## E. Limiti metodologici (onestà)
- WebFetch è stato **bloccato 403** lato-sito su quasi tutti i domini (CNBC, TechCrunch, Wikipedia, corporate): gli estratti provengono dal recupero via WebSearch, non da fetch verbatim. Gli URL primari sono comunque citati e verificabili manualmente.
- Le valutazioni ($8B, $7,6B, $18B) sono post-money riportate dalla stampa finanziaria (CNBC/Bloomberg/TechCrunch), non bilanci auditati.
- Revenue Wingcopter ($1,73M 2024) da Tracxn/CBInsights (aggregatori): confidenza media.
- Volumi Meituan (450k) e consegne Zipline (2M) sono claim vendor/stampa, non certificati da terzi indipendenti.
