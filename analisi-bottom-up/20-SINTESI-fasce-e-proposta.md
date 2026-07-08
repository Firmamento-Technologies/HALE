# 20 — Sintesi a fasce & proposta a menu per i finanziatori

> **Cosa è.** Chiusura della seconda tornata di ricerca (riframing "piattaforma modulare multi-missione / trampolino di lancio"). Incrocia quattro flussi: ingegneria fasce (`10`), mercato multi-missione (`11`), modularità & business (`12`), regolatorio per missione (`13`), sulla base della prima tornata (`00`–`07`). Restando **realistici**. È supporto alla decisione: la scelta finale (§7) è dell'utente.

---

## 1. La matrice a fasce (unificata)

| | **T0 — COTS** | **T1 — BOXY** (VTOL C3 box-wing) | **T2 — MID** (mid-VTOL ibrido) | **T3 — MALE** civile | **T4 — HALE** |
|---|---|---|---|---|---|
| MTOM | 5–9 kg | **≤25 kg** | 30–150 kg | 150–450 kg | 20–150 kg @20 km |
| Autonomia | 40–60 min | 1,5–3 h (elettrico) | **10–16 h** (ibrido) | 16–24 h | settimane *(mai dimostrato civ.)* |
| Quota | <150 m | fino ~3–4 km | 3–5 km | 5–9 km | 20 km |
| Payload utile | 1–3 kg | ~2–5 kg | **5–30 kg + pod cargo** | decine di kg | pochi kg |
| CapEx | €40–120k | **dimostratore €150–400k** / prodotto certificato €3–10M+ | €0,8–1,8M (buy/config COTS) / build nuovo €5–15M+ | €2–10M/unità | $50M–1B (programma) |
| Costo-programma servizio | <€150k | *(dimostratore, non servizio)* | €2–5M (servizio continuo) | decine M€ cumulati | centinaia M€ |
| TRL | 9 | **3–4** | 7–9 (COTS) | 8–9 (vendor) | 3–5 |
| Categoria reg. | Open A3 | Specific SAIL II | Specific SAIL II–IV | Certified / Specific alto | Certified (**no framework HAPS**) |
| Missioni ottimali | EO spot, AED urbano | EO BVLOS di valle, relay leggero | **logistica medicale, EO-persistenza, sorveglianza — 4/6 missioni civili** | area vasta, dual-use difesa | copertura regionale persistente |
| Buy / Build | Buy | **Build** (è l'IP) | **Buy COTS** (avionica chiusa) | Buy (prime) | Build R&D |
| Finanziabilità | Pool A (facile) | Pool A (demo) / Pool B (R&D) | Pool A alta + Pool B | Pool B / difesa | fuori portata del veicolo |

*(Pool A = fondi territoriali B2G: Coopfond/FESR/convenzioni PA. Pool B = fondi R&D aerospazio/dual-use: PNRR-Aero/Horizon/EDF/CDP Venture. Numeri completi e fonti nei report `10`–`13`.)*

---

## 2. Dove converge il mercato: tutto su **T2**

Le tre missioni civili a valore reale — **logistica medicale** (sangue/campioni/farmaci/defibrillatori; unica dove *volare serve davvero* e il sostituto non è gratis: elisoccorso ~€2.000/h), **EO-persistenza in finestra** (incendi/overwatch PC), **sorveglianza ambientale** — convergono **tutte su T2 (mid-VTOL con payload intercambiabile)**. Non su T1 box-wing, non su T4 HALE. Difesa e sorveglianza coste valgono ma sono presidiate dai prime (Leonardo/Eurodrone). Pacchi = vetrina (Amazon Prime Air **fuori dall'Italia da dic. 2025**).

**T2 è dunque il cuore corretto dell'idea modulare.** Ma con un problema.

---

## 3. La contraddizione centrale (ingegneria ⟷ mercato)

> **Il mercato premia T2; T2 conviene comprarlo COTS (buy batte build di 1–2 ordini di grandezza); ma i sistemi COTS (JOUAV/Threod/Tekever) hanno avioniche proprietarie chiuse → il "bus comune" non si può costruire sopra di essi → la famiglia modulare si dissolve.**

In altre parole, le due cose che vuoi non stanno insieme *dentro la stessa gamba*:

| Vuoi… | Lo ottieni da… | Ma perdi… |
|---|---|---|
| **Servire le missioni reali al miglior costo** | comprare/leasing **T2 COTS**, scambiando i payload | il **bus proprietario / l'IP**: diventi un *operatore di COTS*, la credibilità ingegneristica non si costruisce |
| **Costruire il bus proprietario (IP, credibilità, strada verso l'HALE)** | **costruire in-house** T1 (e deliberatamente T2) | l'**economia del servizio**: il custom costa €3–15M+ e perde contro il COTS |

La modularità *vera con architettura condivisa* si riduce, se compri COTS, a **T1 da solo con i suoi 3 moduli payload**. Per avere una famiglia con bus comune su 2–3 taglie devi **decidere di costruirla** — non è una proprietà che emerge dal linguaggio "piattaforma modulare".

---

## 4. Le tre verità sui costi (correzioni ai target, restando realistici)

1. **BOXY a €300k** — realistico **solo come dimostratore non certificato**. Come *prodotto pronto a erogare un servizio autorizzato* costa €3–10M+ (benchmark Wingtra/Quantum). *Va dichiarato quale dei due è.*
2. **MID a €1,5M** — raggiungibile **comprando/configurando** un sistema COTS/semi-custom esistente (classe JOUAV CW-30E/Threod) con payload avanzato, **non** sviluppando un airframe nuovo (€5–15M+). E **"giorni" di autonomia a 30–150 kg con solare parziale non esiste** sul mercato: tetto reale 10–16 h ibrido.
3. **MALE a €50–100M** — quella forbice è **territorio militare esquisito (MQ-9-class) o programma di servizio pluriennale cumulato**, non l'acquisto di un MALE civile: il dato solido è **€2–10M/unità** (Hermes/Schiebel; EMSA-Tekever €7,5–8,75M/anno).

---

## 5. La risoluzione: **barbell a due gambe, reso concreto**

Non "scegliere una fascia", ma **separare due gambe con P&L distinti**, unite solo dal *bus* e dalla narrativa (come Anduril/GA-ASI):

### Gamba A — **OPERATORE** (cassa, Pool A, oggi)
- **Compra/leasing T2 COTS** (+ T0 per lo spot) e **opera** con payload intercambiabili: gimbal EO, relay/IoT, **pod cargo medicale**.
- Missioni: logistica medicale su anchor firmato (ASL/118) + EO-persistenza (incendi/PC) + sorveglianza ambientale.
- Regolatorio: sequenza a minimo attrito **S0 Open A3 → S1 EO Specific SAIL II (base madre) → S3 consegna medicale**; il **LUC** solo in fase di scala (Y3+).
- Tetto CapEx **≤€1M su 18–24 mesi**, grant-prevalente. È la parte che **sopravvive alla falsificazione**.

### Gamba B — **COSTRUTTORE del bus** (IP, Pool B, scorporata)
- **BOXY come dimostratore** dell'**IP che conta**: autopilota/autonomia proprietari, **interfaccia payload standard (ICD)**, ground station comune, e — soprattutto — le **autorizzazioni BVLOS** (asset scarsissimo: 23 operatori in Italia nel 2023) e il **track record di volo**.
- Finanziata **come R&D** (PNRR-Aero/Horizon/EDF), **fuori dal P&L del servizio**.
- Obiettivo esplicito: **produrre asset trasferibili** (IP, autorizzazioni, partner prime/ASI) → è *questo*, non i ricavi del servizio, che costruisce il trampolino verso T2-in-house, dual-use e infine HALE.

> Il collante è il **bus**: se BOXY nasce con un'interfaccia payload e un'avionica che *domani* possono equipaggiare un T2 costruito in casa, la gamba B ha un senso industriale. Se BOXY è solo "un altro drone", la gamba B è un hobby costoso.

---

## 6. La proposta a menu per i finanziatori

Da mettere sul tavolo di ciascun ente **la fascia + la narrazione giusta per lui** (due pitch, non uno):

| Ente | Fascia/oggetto da proporre | Narrazione | Taglia |
|---|---|---|---|
| **Coopfond / FESR Liguria** | Gamba A: servizio EO+resilienza (T0/T2 COTS), pilota Pentema | "Asset pubblico multi-funzione, servizio mutualistico **focalizzato** per le Aree Interne" (modularità *sotto traccia*: sbandierarla = red flag di focus) | €0,3–1M |
| **ASL / 118 / Regione-Sanità** | Gamba A: logistica medicale (pod cargo su T2), su convenzione | "Riduzione tempi/costi vs elisoccorso; evidenza clinica AED 50–70%" (serve un **anchor firmato**, altrimenti dispersione) | pilota grant |
| **PNRR-Aerospazio / Horizon / EDF** | Gamba B: BOXY + bus proprietario + roadmap dual-use | "Famiglia **dual-use** su bus proprietario + track record BVLOS — *platform play*" (la modularità qui è **il** valore) | €1–15M |
| **CDP / Legacoop / coop** | co-finanziamento Gamba A + equity founder | veicolo mutualistico + radicamento SNAI | debito/equity |
| **ASI / prime (Leonardo/TAS)** | Gamba B: partnership su IP/HALE Y6+ | nodo italiano infrastruttura HAPS (vettore strategico) | partnership |

---

## 7. La decisione che resta a te (esplicita, non aggirabile)

Tutta la ricerca converge su **una** domanda che il linguaggio "piattaforma modulare" nasconde:

> **BOXY è un DIMOSTRATORE (Gamba B, R&D, IP verso l'HALE) o un PRODOTTO-SERVIZIO (Gamba A, cassa)?**

- Se **dimostratore**: giusto costruirlo in-house a €150–400k, finanziato come R&D, progettato attorno al **bus/ICD**; il *servizio* di cassa lo eroghi in parallelo comprando **T2 COTS**. → **coerente, questa è la raccomandazione.**
- Se lo si vuole come **prodotto-servizio economico**: allora costa €3–10M+ e **perde contro il COTS** — non farlo, compra.
- Ciò che **non** funziona è la via di mezzo implicita ("costruiamo BOXY a €300k e sarà anche il nostro prodotto di servizio"): è il punto falsificato dall'ingegneria (`10`).

E, a monte, il bivio di posizionamento del cap. §8 di `00` resta il vero interruttore: **Servizio puro / R&D-first / Barbell**. La matrice a fasce dice che **solo il Barbell** usa T1 (build/IP) e T2 (buy/servizio) *ciascuno per ciò in cui è forte*, senza chiedere a una fascia sola di fare tutto.

---

## 8. Roadmap e kill-criteria aggiornati

**Sequenza (demand-first, come `00` §6):**
- **G0 (<€30k, subito):** EO Open A3 + Copernicus; obiettivo **commerciale**: 1 LoI Regione + 1 convenzione ASL/Ente Parco. Nessun CapEx di piattaforma prima della firma.
- **G1 (≤€1M, dopo la firma):** Gamba A operativa su **T2 COTS**, payload EO/relay/cargo; SAIL II. In parallelo, **se** si sceglie Gamba B: avvio BOXY-dimostratore su bando R&D **separato**.
- **G2 (Pool B, con IP + autorizzazioni maturate):** T2-in-house / dual-use; candidatura EDF/PNRR-Aero.
- **G3 (Y6+):** HALE come nodo di consorzio, non OEM.

**Kill-criteria (oltre a quelli di `00` §7):**
- **Logistica medicale:** nessun anchor ASL/118 firmato entro G1 → la missione più forte cade; il pod cargo non entra.
- **Gamba B:** se BOXY **non è progettato attorno a un bus/ICD riusabile** (cioè non produce asset trasferibili), va **cancellata** — è spesa R&D senza ritorno strategico.
- **Buy-vs-build:** se un T2 COTS copre le missioni a 1/2 del costo del custom **e** non serve l'IP, il build di T2 non si fa.
- **Dispersione:** se a G1 si inseguono >2 missioni contemporaneamente senza un anchor ciascuna → *morte per mille nicchie*; ridurre a una.

---

### Riga di fondo

> La finestra di opportunità **non** è coperta da un'unica piattaforma: è coperta da **un'unica architettura (bus + ICD + autorizzazioni)** declinata su **due gambe** — un **operatore** che *compra* T2 COTS e fa cassa sulle missioni reali (logistica medicale in testa), e un **costruttore** che *edifica* il bus proprietario partendo da BOXY-dimostratore, finanziato come R&D, come strada verso il dual-use e l'HALE. La domanda operativa n.1 resta *"chi firma per la persistenza / la consegna?"*; la domanda strategica n.1 è *"BOXY è dimostratore o prodotto?"*. Rispondendo a queste due, la piattaforma — e il suo costo — si scelgono da sé.
