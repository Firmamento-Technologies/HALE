# 40 — Revisione evidence-graded: cosa regge alla verifica con fonti reali

> **Cosa è.** Consolidamento della ricerca iper-approfondita (7 flussi R1–R7, **102 fonti scaricate** con provenienza in `fonti/`). Verifica avversariale di tutte le cifre-chiave delle tre tornate precedenti (`analisi-bottom-up/`): ciascun claim è marcato **✅ confermato / ✏️ corretto / ❌ smentito**, con fonte e confidenza aggiornata.
>
> **⚠️ Caveat metodologico (vale per tutti i flussi).** L'egress policy dell'ambiente ha bloccato con **HTTP 403** il download integrale (WebFetch/curl) di quasi tutti gli host esterni (TED, EASA, ENAC, editori, perfino Wikipedia). La ricerca è stata condotta via **WebSearch con triangolazione** su fonti multiple; ogni cifra ha l'URL della fonte primaria ma **va riverificata sul PDF/bando ufficiale prima dell'uso in documenti per finanziatori o regolatori**. I link sono nei file `fonti/`.

---

## 1. Il quadro complessivo: le conclusioni strategiche REGGONO

La ricerca con fonti reali **non ribalta** nessuna delle conclusioni delle tre tornate. Le **rafforza** e ne **corregge i numeri**. In sintesi:

- **Nessun velivolo dedicato chiude il business case dentro il budget finanziabile** → confermato e rafforzato.
- **Il valore è nel servizio / bundle verticale, mai nell'OEM di airframe** → confermato da 3 casi indipendenti.
- **HALE = centinaia di M€, fuori portata standalone** → confermato con fonti esterne.
- **Il box-wing non dà vantaggio a scala C3** → confermato con letteratura peer-reviewed.
- **La connettività broadband è dominata da Starlink** → rafforzato (prezzi scesi).
- **€0,5–1M è finanziabile; €1,5–3M solo con SpA+equity esterna** → confermato con strumenti reali.

---

## 2. Tabella evidence-graded (claim → verdetto → fonte → confidenza)

### Mercato & business (R1, R2)
| Claim precedente | Verdetto | Evidenza reale | Confidenza |
|---|---|---|---|
| Mercato medical-delivery "$5,5B EU 2035" | ❌ **corretto (3–5× più piccolo)** | GM Insights è **globale**: $166M(2025)→**$2,1B(2035)**; EU ≈ **$0,5–1,2B** | LOW→ MEDIA (endpoint corretto, single-source) |
| Wingcopter "~€120k/unità" | ✏️ **corretto** | airframe base **$80–100k**; €120k solo come **sistema integrato** (airframe+capsula+GCS) | MEDIA |
| "airframe €20k" (report 21) | ❌ **smentito** | nessun delivery-drane serio a quel prezzo | ALTA |
| Elisoccorso "~€2.000/h" | ✅ **confermato (conservativo)** | reale **€2.000–7.200/h** (HEMS IT) → value-prop medicale *rafforzata* | ALTA |
| AED "sopravvivenza 50–70%" | ✏️ **confermato ma ri-attribuito** | Karolinska/Lancet prova il **tempo** (−3 min); il 50–70% è letteratura clinica separata | ALTA |
| Quantum Systems "$8B, ITAR-free, 19.000 missioni" | ✏️ **2 su 3 confermati** | $8B Series D (Airbus co-lead) ✅; ITAR-free ✅; **"19.000 missioni" ritirato** (non verificabile) | ALTA |
| ABzero "non-OEM, capsula brevettata, round €190k" | ✅ **confermato e rafforzato** | 5 brevetti, spin-off Sant'Anna, €190k@€4,6M pre-money | ALTA |
| "Valore = bundle verticale, non OEM" | ✅ **confermato ×3** | Zipline **non profittevole** ($600M, 2M consegne); Wingcopter **ricavi 2024 $1,73M**; Matternet monetizza rete+cert | ALTA |

### Costi & piattaforme (R3)
| Claim precedente | Verdetto | Evidenza reale | Confidenza |
|---|---|---|---|
| COTS T0 "€40–120k" | ✅ **confermato** | WingtraOne GEN II **€35–37k** (tender pubblici UK) | ALTA |
| COTS T2 "€0,8–1,8M" | ⚠️ **non verificato** | JOUAV/Threod **senza prezzo pubblico** → resta stima | BASSA |
| MALE-service "EMSA-Tekever €7,5–8,75M/anno" | ✏️ **corretto** | contratto **€30M** (2 anni+opzioni) → **€7,5–15M/anno** | MEDIA-ALTA |
| Box-wing custom certificato "€3–10M+" | ✅ **corroborato** | CORDIS **€3,54M** solo per industrializzare il WingtraOne | MEDIA |
| Certificazione prodotto "€9–25k" | ✏️ **ottimistico** | EASA Design Verification **€250/h, ~€45k/anno**; **nessun UAS ha un Type Certificate EASA pieno** | MEDIA |

### Regolatorio (R4)
| Claim precedente | Verdetto | Evidenza reale | Confidenza |
|---|---|---|---|
| Consegna medicale "sempre Specific, SAIL II–IV" | ✅ **confermato** | art. 4 Reg. 947; DG fuori scope SORA 2.5; **precedente ABzero Eolie lug-2024** | ALTA |
| Esiste percorso cargo semplificato | ✅ **nuovo, positivo** | **PDRA-G01 "long-range cargo"** (BVLOS poco popolata, **SAIL II**) | ALTA |
| "23 operatori BVLOS Italia 2023" | ✏️ **corretto** | **23 *autorizzazioni* BVLOS Specific** nel 2023 (Osservatorio PoliMi) | ALTA |
| LUC "€150–400k, Y3+" | ✅ **confermato** | fee €3.220 ma build org. pesante; **Amazon ha rinunciato al LUC italiano** (dic-2025) | MEDIA-ALTA |

### Connettività & HAPS (R7)
| Claim precedente | Verdetto | Evidenza reale | Confidenza |
|---|---|---|---|
| "Starlink batte l'aereo per broadband" | ✅ **rafforzato** | Italia **29/39/59 €/mese, antenna gratis**, 25–40 ms | ALTA |
| Starlink Direct-to-Cell minaccia il D2D | ◐ **parziale** | commerciale USA; UE dal 2026–28; **nessun MNO IT a metà 2026**; ancora narrowband | ALTA |
| "HALE centinaia di M€, impossibile standalone" | ✅ **confermato** | Loon ~$1B bruciati, HAPSMobile sciolta, **0 HALE solari commerciali in 20+ anni**; dimostratore **$10–25M** | ALTA |

### Box-wing (R6)
| Claim precedente | Verdetto | Evidenza reale | Confidenza |
|---|---|---|---|
| "Box-wing nessun vantaggio netto a C3" | ✅ **confermato e rafforzato** | crossover a **Re≈4×10⁵** ≈ crociera C3 → pareggio CD0-sensibile; VTOL "sporco" → mono avanti | MEDIA-ALTA |
| "Nessuna IP difendibile" | ✅ **confermato** | arte nota (Lockheed US3834654 scaduto, Prandtl 1924) | ALTA |
| Aeroelasticità joined-wing = showstopper | ✏️ **ridimensionato** | rischio **basso su C3 rigido**, **primo ordine su ala HALE** | MEDIA-ALTA |

### Finanziamenti (R5)
| Claim precedente | Verdetto | Evidenza reale | Confidenza |
|---|---|---|---|
| "€0,5–1M finanziabile" | ✅ **confermato e meglio ancorato** | **Coop2050** prestito 0% ≤€500k; **Galaxia** seed ~€1M; FESR Liguria 1.1.1 ≤€150k | MEDIA-ALTA |
| "€1,5–3M solo con equity esterna+SpA" | ✅ **confermato** | EIC Accelerator (≤€2,5M+equity), CASSINI (≤€2,5M+€15M) | MEDIA |
| Nuova Marcora "€1M, leva 4×" | ✏️ **corretto (meglio)** | fino **€2M, leva 5×, 0%, 3–10 anni** (ma ∝ capitale coop) | MEDIA |
| ">€3M HALE fuori portata" | ✅ **confermato** | EDF/ESA/ASI indiretti, prime-led | ALTA |

---

## 3. Rischi e scoperte nuove (non presenti nei report precedenti)

1. **🔴 JOUAV bandita dal procurement federale USA** (lista DOD 1260H, dic-2025), l'UE valuta misure analoghe (R3). → **doppio effetto:** (a) rischio per la raccomandazione "compra JOUAV COTS" per il T2; (b) **rafforza** la tesi che serve un fornitore **europeo/non-cinese** — ma quel posizionamento è già affollato (punto 2).
2. **🔴 Il fossato "sovrano EU dual-use" è già capitalizzato da 3 giganti**, non da uno: **Helsing $18B, Quantum $8B (Airbus), Tekever $1,33B** (R2). Firmamento non può competere frontalmente come OEM di droni: deve essere **nodo/partner** o iper-verticale su una nicchia territoriale-pubblica.
3. **🟢 Precedente ABzero Eolie** (prima rotta biomedicale ENAC, lug-2024) → la consegna medicale in Specific **si fa davvero in Italia**, ma rotta-per-rotta e su **isole, non in Liguria** (R4, R1).
4. **🟡 Amazon ha rinunciato al LUC italiano** (dic-2025) → conferma "LUC solo in fase di scala" (R4).
5. **🟢 Il box-wing è studiato per HAPS/HALE dal CIRA italiano** (R6) → **la casa naturale del box-wing è il 6B/HALE come R&D, non il drone di consegna C3.** Riconcilia l'interesse per il box-wing con l'evidenza: non è il prodotto, è la ricerca di lungo periodo.

---

## 4. Cosa cambia (e cosa no) nelle raccomandazioni

**Non cambia** l'impianto: barbell a due/tre gambe (servizio-cassa / IP-dimostratore / servizio-grande ancorato), piano di capitale scaglionato ≤€1M all'ingresso, HALE come R&D di lungo periodo.

**Si affina così, alla luce delle fonti:**
- **Il mercato medicale è più piccolo del previsto** (EU $0,5–1,2B 2035, non $5,5B) e **pilot-stage su isole** → è un **anchor narrativo e di credibilità**, non un business autosufficiente. La value-prop (elisoccorso €2–7k/h) resta reale.
- **Il box-wing va spostato esplicitamente sull'HALE/6B come linea R&D** (dove è tecnicamente sensato e c'è il precedente CIRA), togliendolo dal ruolo di prodotto-consegna dove non ha né edge né IP.
- **La strategia "sovrana dual-use" — l'unica che i dati mostrano ripagare — è affollata da giganti** → Firmamento deve giocare da **nodo di consorzio / iper-verticale territoriale-pubblico**, non da OEM che compete con Helsing/Quantum/Tekever.
- **Attenzione al fornitore T2:** se si compra COTS per il servizio, **evitare JOUAV** (rischio ban EU) → orientarsi su europei (WingtraOne, Quantum, Threod), coerente con la narrativa sovrana.
- **Numeri da aggiornare nei documenti:** EMSA €7,5–15M/anno; "23 autorizzazioni" non "23 operatori"; Wingcopter sistema €80–120k; mercato medicale EU $0,5–1,2B; Marcora fino €2M.

---

## 5. Cosa resta da verificare (prima di andare dai finanziatori)

Il caveat 403 e le lacune residue impongono tre verifiche **su fonte primaria**, non delegabili al web:
1. **Bilanci reali delle 10 cooperative** → il fattore decisivo (capacità di cofinanziamento+equity) resta a confidenza medio-bassa finché non si leggono i bilanci.
2. **PDF ufficiali dei bandi** (Coopfond Cooding 2026, FESR Liguria 1.1.1, Coop2050, Galaxia) → riverificare ticket e scadenze; **contattare Coopfond** per il ciclo 2026.
3. **Prezzo reale T2** (JOUAV/Threod/equivalenti europei) → richiedere quotazioni (RFQ) dirette; la fascia €0,8–1,8M è l'unica ancora non ancorata.
4. **Pre-application ENAC** per il SAIL reale di una rotta Pentema e per il DG medicale.

---

### Riga di fondo

> La ricerca con fonti reali **conferma la direzione e corregge i numeri**. Le tre correzioni che contano: (1) il **mercato medicale è 3–5× più piccolo** e pilot-stage (anchor, non business); (2) il **box-wing appartiene all'HALE/R&D, non al drone di consegna**; (3) la **nicchia sovrana dual-use — l'unica che ripaga — è già dei giganti**, quindi Firmamento deve giocare da nodo/iper-verticale, non da OEM. Nessuna di queste ribalta la strategia: la rende **più difendibile davanti a un investitore**, perché ora ogni cifra ha una fonte (da riverificare sul primario) e ogni claim gonfiato è stato tarato. Le due decisioni restano tue: **posizionamento (servizio / R&D / barbell)** e **ruolo del box-wing (dimostratore-HALE vs prodotto)** — ora con l'evidenza sul tavolo.
