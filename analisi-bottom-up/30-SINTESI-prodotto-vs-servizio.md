# 30 — Sintesi: BOXY prodotto vs MALE/HALE servizio, e piano di capitale

> **Cosa è.** Chiusura della terza tornata (raffinamento utente: *vendere* BOXY come prodotto di nicchia; *operare* MALE/HALE come servizio; massimizzare profitto e non spaventare gli investitori). Incrocia: strategia prodotto (`21`), vantaggio tecnico box-wing (`22`), economia integrata + capitale (`23`), sulla base delle tornate 1–2 (`00`–`20`). Supporto alla decisione; la scelta finale (§4, §8) è dell'utente. **Confidenza complessiva media-bassa** sui numeri (nessun prezzo/volume è dato reale: gli scenari divergono ~10× sull'NPV).

---

## 1. La risposta in una riga

> **Vendere un prodotto può essere profittevole** — ma il prodotto profittevole è un **VTOL snello per operatori professionali** (dev ≤€2,5M, prezzo ≥€120k), **non** un box-wing certificato per la consegna. Il **box-wing** e la **consegna medicale** sono, ciascuno per motivi diversi, i punti più deboli della combinazione. Il servizio grande (MALE/HALE) **non è il premio facile**: è zavorra opex finché non è ancorato a un contratto firmato.

---

## 2. I tre responsi

| Flusso | Verdetto | Confidenza |
|---|---|---|
| **Strategia prodotto (`21`)** | Hardware nudo = **me-too senza moat**; il fossato "europeo/dual-use" è **già preso da Quantum Systems** ($8B, lug-2026). L'incumbent IT **ABzero non produce droni** (moat = capsula+servizio). Le **ASL comprano servizi con SLA, non unità**. Mercato-unità: poche decine/anno UE. "Prodotto" regge solo come **bundle hardware+servizio** (razor-and-blades). | Media |
| **Tecnico box-wing (`22`)** | Nessun vantaggio: crociera delivery **netto ≈ 0%** (regime attrito-dominato); risparmio strutturale **≲2% MTOM**. **Nessuna IP** (arte nota Prandtl 1924…). Aggiunge **+€0,5–1,5M e 6–18 mesi** + rischi flutter/buckling. *(Nota: in `cad/` non esiste un box-wing — è un'ipotesi, non un design esistente.)* Tenere **solo come dimostratore/vetrina**. | Media (aero/IP), bassa-media (costi) |
| **Economia (`23`)** | Linea prodotto **profittevole SE** prezzo ≥€120k e dev ≤€2,5M: margine ~€65k/unità (54%), break-even operativo **~9–10 unità/anno**, recupero dev a **~38 unità (~Y5-6)**, **IRR ~22%** base (best >100%; worst non recupera mai). **Prodotto = motore di valore; servizio = zavorra** (NPV servizio −€1,9M, ok solo ≥3 piattaforme e utilizzo >60%). Se serve **piena certificazione, dev €4–8M → salta**. | Bassa (nessun dato reale) |

---

## 3. Il verdetto integrato — cosa è vero

1. **"Vendi il piccolo, opera il grande" è sano come istinto**, ma con due rettifiche forti:
   - il *piccolo* che si vende con profitto è un **VTOL per operatori Specific** (non type-certificato), venduto **in bundle con servizio ricorrente** — non hardware nudo (che perde contro Quantum/DJI);
   - il *grande* (MALE/HALE) **non è il premio automatico**: è **opex-intensivo e in perdita** finché non ha un **anchor contrattuale**. Il "mercato più grande" c'è, ma costa gestione e capitale, e va scalato **lean e solo su contratto firmato**.
2. **Il box-wing non è ciò che rende profittevole il prodotto.** Non dà edge di prestazione né IP; aggiunge costo, tempo e rischio. Se l'obiettivo è un prodotto vendibile, un **fixed-wing VTOL convenzionale** è più economico, veloce e sicuro. Il box-wing sopravvive **solo** come **dimostratore/vetrina IP** o in una nicchia sovrana ISR molto stretta.
3. **La consegna medicale è l'anchor narrativo più forte ma il fit-prodotto più debole:** l'airframe box-wing è da *loiter/EO*, non da *consegna*; la nicchia AED/medicale premia un **cargo-VTOL** ed è presidiata da **ABzero**; e il cliente (ASL) **compra servizio, non droni**. Va perseguita **come servizio in bundle**, non come vendita di box-wing.
4. **Il capitale può restare "non spaventoso":** picco di esposizione **~€3,3M (Y3)**, un ordine di grandezza sotto i €5–11M dell'HALE del Briefing — e l'investitore **non vede mai la cifra grande prima del de-risk**.

---

## 4. La contraddizione da sciogliere (decisione utente n.1)

Tu vuoi che **BOXY (box-wing) sia il prodotto**. La ricerca dice: il prodotto *profittevole* è un VTOL snello, e il *box-wing* specifico aggiunge costo/rischio senza edge. Quindi:

| Opzione | Cosa comporta |
|---|---|
| **(A) Prodotto = VTOL convenzionale**; box-wing come **dimostratore R&D a parte** | Prodotto più economico/veloce/profittevole (dev ≤€2,5M). Il box-wing resta la **vetrina IP/sovranità** verso l'HALE, finanziata come ricerca. **Massimizza profitto e finanziabilità.** ⟵ *raccomandata dai numeri* |
| **(B) Prodotto = box-wing** (identità/IP di Firmamento) | Accetti +€0,5–1,5M, +6–18 mesi, nessun edge prestazionale né IP: lo giustifichi **solo** con la narrativa sovrana/vetrina o con l'impegno "è ciò che sviluppiamo". Profitto più basso, rischio più alto. |

Non è una scelta tecnica: è **quanto Firmamento è legata al box-wing come identità** vs pragmatica sul prodotto. La ricerca raccomanda **(A)**; se vuoi **(B)**, va fatto a occhi aperti e col box-wing scorporato come R&D, non appeso al P&L del prodotto.

**Prima di qualunque capitale** sul box-wing: 2 simulazioni (VLM → RANS transizionale) per **falsificare il "~0% crociera"**. Se confermato, (B) perde la sua unica giustificazione tecnica.

---

## 5. Il piano di capitale a stage (che non spaventa)

| Stage | Cifra (netto grant) | Sblocca / milestone | Fondi | Cosa si costruisce |
|---|---|---|---|---|
| **0** | **€150–500k** (quasi tutto grant + €50k Coopfond già deliberati) | dimostratore volato + **1 LoI Regione + 1 anchor ASL/Parco** | Coopfond, FESR, SNAI | dimostratore (box-wing come vetrina) + servizio EO Open A3 |
| **1** | **€1,5–2,5M** in **2 tranche gated** | tranche 2 sbloccata dalla **1ª vendita/anchor**; BVLOS SAIL II | FESR/Coopfond/Nuova Marcora + prima cassa | prodotto VTOL snello per operatori + servizio T2 COTS |
| **2** | **€1,5–3M** | **contratto servizio firmato** | CDP Venture / EDF / PNRR-Aero | linea servizio "grande" lean + linea IP dual-use |
| **3 (Y6+)** | capitale istituzionale/consorzio | prodotto cassa-positivo + IP maturata | ASI/prime/EU | HALE come nodo di consorzio, non OEM |

**Picco esposizione ~€3,3M (Y3).** MALE/HALE **fuori dal conto** finché il prodotto non è cassa-positivo.

---

## 6. La struttura a tre gambe (evoluzione del barbell)

1. **Motore di cassa — Prodotto+bundle:** VTOL snello per operatori Specific, venduto con servizio ricorrente (razor-and-blades). *Profittevole a ~10 unità/anno.* Pool A + vendite operatori.
2. **Gamba IP/credibilità — Box-wing dimostratore:** R&D scorporata (Pool B), vetrina sovrana verso il dual-use e l'HALE. Produce **asset trasferibili** (IP, autorizzazioni BVLOS, partner), **non** cassa.
3. **Gamba servizio grande — MALE/HALE operato:** premio di lungo periodo ma **opex-zavorra**: scalare **lean, solo su anchor firmato**, personale dedicato solo quando il contratto lo paga.

P&L separati; condivisi **bus + autorizzazioni + brand + narrativa** (sovranità + Aree Interne).

---

## 7. Caveat e kill-criteria

- **Dato debole:** nessun prezzo/volume/ricavo è reale → prima di Stage 1, **validare prezzo e volume** con 3–5 lettere d'intenzione da operatori/ASL. Se il prezzo realizzabile < €100k o i volumi < ~9/anno, **la linea prodotto non recupera**: fermarsi al bundle-servizio.
- **Box-wing:** se le simulazioni confermano ~0% di guadagno in crociera, **cancellare l'opzione (B)**; box-wing resta solo vetrina.
- **Certificazione:** se la nicchia scelta impone type-cert (dev €4–8M), la linea prodotto salta → **restare su servizio**.
- **Servizio grande:** nessun anchor firmato → **non** assumere personale né scalare piattaforme; resta un business plan, non un centro di costo.
- **Dispersione:** >2 nicchie inseguite insieme senza anchor ciascuna → ridurre a una.

---

### Riga di fondo

> Sì al "vendi il piccolo, opera il grande" — ma il piccolo che vende con profitto è un **VTOL snello in bundle con servizio**, non un box-wing certificato per la consegna; e il grande è **zavorra finché non è ancorato**. Il **box-wing va tenuto come dimostratore/vetrina IP** (decisione (A)), non come il prodotto — a meno che tu non scelga consapevolmente di pagarne il premio per ragioni di identità/sovranità (decisione (B)), scorporandolo come R&D. Il capitale resta **scaglionato e modesto** (picco ~€3,3M, mai la cifra HALE prima del de-risk). Le due prove che sbloccano tutto: **un anchor firmato** (chi paga il servizio/il primo prodotto) e **le simulazioni box-wing** (il vantaggio esiste o no). Nessuna delle due costa quasi nulla — ed è da lì che si parte.
