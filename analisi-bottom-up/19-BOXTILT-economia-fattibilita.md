# 19 — BOXTILT (box-wing 4 tilt-rotor): fattibilità ECONOMICA nel modello-servizio

> **Progetto HALE — Firmamento Technologies · Analisi economico-finanziaria critica**
> **Autore:** Financial Analyst / Fractional CFO · **Data:** 2026-07-09
> **Mandato:** stabilire se il concept dell'utente — **box-wing (ala anteriore + posteriore chiuse alla Prandtl) con 4 tilt-rotor** (2 anteriori traenti + 2 posteriori spingenti in crociera, tutti verticali in hover, nessun rotore "morto") — ha senso **ECONOMICO** in uno studio di fattibilità, non solo aerodinamico. Il filtro economico è **decisivo**: un vantaggio tecnico che non ripaga il capitale che costa non è una feature, è una passività.
> **Base tecnica:** simulazione bottom-up L0/L1 `sim_boxwing_tiltrotor.py` (BOXTILT L/D 16,6; **+44% range** e **−23% potenza di crociera** vs COTS lift+cruise; **+8% potenza in hover** per download su due ali).
> **Base costi/finanza/mercato:** `10-fasce-engineering.md` §3, `22-boxwing-vantaggio-tecnico.md`, `18-boxwing-tiltrotor-rivalutazione.md`, `06-finanziabilita.md`, `23-economia-integrata-capitale.md`, `R2-competitor.md`, `R1-mercato-delivery-medicale.md`, `R5-finanziamenti.md`.
> **Confidenza aggregata: MEDIO-BASSA.** Alta sui benchmark di costo/finanziamento/competitor ereditati (già triangolati); **bassa** sui ricavi di servizio e sul valore assoluto del +44% (fedeltà L0/L1). **Nessuna cifra è una quotation reale né un ricavo contrattualizzato.**

---

## 0. Regola di lettura e la domanda che governa il capitolo

`[FATTO]` = dato da fonte ufficiale / benchmark verificato nei report a monte. `[STIMA]` = elaborazione del CFO, confidenza dichiarata inline. Scale sempre esplicite (**€k** vs **€M**). WACC **nominale, post-imposte, blended** (grant 0% + equity aerospace seed 25-35% + debito agevolato 0-6%) ⇒ **WACC base 12%** (sensibilità 10%/15%), coerente con `23`.

**La domanda del capitolo NON è "il box-wing vola meglio?" (sì, di poco, secondo la sim). È:**

> Firmamento è **operatore di servizi, non OEM** (`CLAUDE.md`). Nel modello-servizio la piattaforma è un **asset di flotta** che genera OpEx e produce ricavi ricorrenti. La domanda è quindi: **il risparmio OpEx ricorrente prodotto dal +44% di autonomia ripaga il costo di SVILUPPARE una piattaforma bespoke, invece di COMPRARE COTS o PARTNERSHIP con chi il problema l'ha già risolto (e brevettato)?**

Anticipo il metodo del verdetto: quantifico prima **il valore € del +44%** (§1), poi il **costo delle tre strade** (§2), poi **NPV/IRR/payback** (§3), il **nodo IP** (§4), il **verdetto condizionato** (§5) e i **kill-criteria** (§6). La conclusione attesa — e confermata dai numeri — è che **BUILD ha senso solo come R&D/IP finanziato da grant, mai come asset di servizio autofinanziato.**

---

## 1. Quanto vale DAVVERO il +44% di autonomia in un modello-servizio?

### 1.1 Il chiarimento che dimezza il valore percepito: il +44% NON viene dal box-wing

Prima di attribuire un euro al concept, va isolato **da dove** arriva il vantaggio nella simulazione. Leggendo `sim_boxwing_tiltrotor.py` (righe 47-60), il delta di BOXTILT su LIFTCRUISE si compone di due leve:

| Leva | Parametro sim | Effetto | Chi altro la cattura |
|---|---|---|---|
| **Nessun rotore morto in crociera** (CD0 0,034 vs 0,044 del COTS) | `CD0` | la maggior parte del −23% di potenza di crociera | **RETRACT** (pod retrattili, +25% range) la cattura quasi tutta con un solo meccanismo |
| **Guadagno Prandtl su drag indotto** (e 1,05 vs 0,80) | `e` (Oswald) | la parte residua | esclusivo del box-wing, ma **piccolo**: `22` §1.3 dimostra che a scala C3 la crociera è **attrito-dominata** (crossover CL≈1,03), quindi il guadagno sull'indotta pesa poco sul drag totale |

**Conseguenza economica dirimente `[FATTO, da sim + doc 22]`:** il grosso del +44% è "**eliminare i rotori di sostentamento morti in crociera**", **non** "avere l'ala chiusa". La configurazione RETRACT (rotori retrattili) — **più semplice, un meccanismo invece di quattro** — ottiene **+25%** con la stessa logica. Il box-wing con 4 tilt aggiunge, sopra RETRACT, solo **~+19 punti percentuali di range** (44 − 25), pagati con **quattro meccanismi di tilt** anziché uno e con tutta l'aeroelasticità/certificazione dell'ala chiusa. **Il valore incrementale attribuibile alla scelta "box-wing 4-tilt" rispetto alla migliore alternativa acquistabile/licenziabile è quindi molto minore del +44% nominale.**

> Questo è il primo colpo economico: **si sta confrontando BOXTILT con il COTS lift+cruise "sporco" (il riferimento più debole)**. Il confronto onesto è con la **migliore alternativa disponibile senza sviluppo** (RETRACT/SUPAIR o un COTS a maggiore endurance), e lì il margine crolla.

### 1.2 Quantificazione del beneficio OpEx per uno scenario di flotta plausibile

Modello uno scenario **flotta di proprietà** (coerente col modello-servizio) su due orizzonti: **Pentema pilota** (1 piattaforma) e **scale-up SNAI** (3 piattaforme a regime, `23` §2). Il +44% di autonomia si traduce in OpEx risparmiato attraverso **tre canali**, tutti ricorrenti:

**Assunzioni `[STIMA]`** (flotta 3 piattaforme a regime, ~400 h volo/anno cad. → ~1.200 h/anno flotta, `23` §2.1):

| Canale di risparmio | Meccanismo | €/anno flotta (3 pf) | Confidenza |
|---|---|---|---|
| **(a) Meno sortite per pari copertura** | +44% endurance → per missioni di persistenza/copertura ~20-30% sortite in meno → meno lavoro di lancio/recupero (≈0,5 h uomo/sortita @ €40/h loaded) | **€8-18k** | bassa |
| **(b) Meno cicli batteria** | ~30% cicli in meno su pacchi da €4-8k, vita ~500-800 cicli → estensione vita utile pacco | **€6-15k** | bassa |
| **(c) Meno ferry/overhead + energia** | più tempo utile per transito, meno voli di trasferimento, meno energia/connettività per sortita | **€5-12k** | bassa |
| **Subtotale non-persistenza** (EO/mapping tipico) | | **€19-45k/anno** | **bassa** |
| **(d) *Condizionale*: 1 piattaforma in meno** | **solo se** il servizio è **endurance-binding** (copertura continua/relay): +44% può far coprire con 2 pf ciò che ne richiederebbe 3 → si evita ~0,3-0,5 pf-equivalente | **+€25-60k** (CapEx amm. €0,8M + OpEx €0,32M pro-quota) | molto bassa |
| **Totale (banda)** | | **€20-70k/anno** | **bassa** |

**Punto centrale `[STIMA, confidenza bassa]`:** il beneficio OpEx ricorrente del +44% per una flotta di 3 piattaforme è dell'ordine di **€20-70k/anno**, centrale **~€40k/anno**. Su 5 anni, **€100-350k** attualizzato. Il beneficio è **reale e ricorrente**, ma:

1. **È il beneficio della *maggiore endurance*, non del *box-wing* né dei *4 tilt*.** La stessa endurance si compra con un **COTS più capace/ibrido** (JOUAV CW-30E: 6-10 h già di serie, `10` §4.1) — che ha endurance **superiore** al C3 elettrico bespoke — senza sviluppare nulla. *Il canale (d), quello grosso, si ottiene comprando la piattaforma giusta, non costruendola.*
2. **È attribuibile a BOXTILT solo per il suo margine su RETRACT/SUPAIR (+19pp), non sui +44pp pieni.** Riproporzionando (§1.1), il beneficio **incrementale di BOXTILT vs la migliore alternativa acquistabile** scende a **~€10-30k/anno**.

> **Verdetto §1 — la domanda-chiave del mandato ha risposta netta e negativa.** *Quel risparmio OpEx (€20-70k/anno lordo, €10-30k/anno incrementale su alternativa acquistabile) NON ripaga lo sviluppo bespoke.* Anche nell'ipotesi generosa €70k/anno × 5 = €350k, resta **1-2 ordini di grandezza sotto** il costo di sviluppo di un box-wing 4-tilt bespoke (§2). Nel modello-servizio, dove il moat è il servizio/dato/operazioni (`CLAUDE.md`), pagare milioni di R&D per raschiare €10-30k/anno incrementali di OpEx è **distruzione di capitale**.

---

## 2. Costo del possesso di ciascuna strada (TCO 5 anni)

Scenario di servizio comune per il confronto: **flotta 3 piattaforme, servizio EO/monitoraggio SNAI, orizzonte 5 anni**. Tutte le cifre `[STIMA]` salvo dove marcato `[FATTO]`.

### 2.1 (A) BUY COTS lift+cruise — comprare ora, TRL 9

- **Cosa:** 3× piattaforma classe JOUAV CW-30E / Quantum, sistema pronto. CapEx sistema **€0,58-0,82M/pf** `[FATTO, 10 §4.1]`; uso €0,80M/pf.
- **OpEx:** €0,32M/pf/anno (2 FTE + manut. + assicuraz. BVLOS + energia/SW, `23` §2.1) `[FATTO parziale]`.
- **Dev:** €0. **TRL 9, disponibile subito, supporto vendor, ricambi a catalogo.**

### 2.2 (B) BUILD bespoke BOXTILT — sviluppare la piattaforma dell'utente

- **Cosa:** dimostratore box-wing 4-tilt → prodotto utilizzabile in servizio. **Dimostratore €0,5-1,5M `[FATTO, 10 §3.3 + 22 §5]`**; **prodotto certificato/serie €3-10M+ `[FATTO, 10 §3]`**. Il box-wing **aggiunge €0,5-1,5M e 6-18 mesi** rispetto a un VTOL convenzionale (interferenza giunzioni, buckling membratura compressa, flutter accoppiato, penalità di novità in certificazione, `22` §3/§5).
- **Timeline:** 24-48 mesi da TRL 3-4 → **nessun ricavo di servizio prima di Y3-Y4** (revenue persa nel frattempo).
- **OpEx:** **superiore** al COTS: 4 meccanismi di tilt = più manutenzione, nessun supporto vendor, ricambi custom, penalità download in hover (+8% potenza hover, sim) sul bilancio energetico. Uso €0,36M/pf/anno.
- **Beneficio OpEx range:** −€20-70k/anno flotta (§1.2), che **non compensa** l'extra-manutenzione bespoke.

### 2.3 (C) PARTNER/LICENSE SUPAIR (o co-sviluppo Polito)

- **Cosa `[FATTO]`:** **SUPAIR** è spinoff **Politecnico di Torino** (nov 2024, incubatore **I3P**), con tecnologia **brevettata "ThrustPod"** (pod VTOL retrattile) per delivery/sorveglianza/rescue, in **design phase, target estate 2026** (fonte: supair.it, Politecnico di Torino, I3P). L'approccio **retrattile** è quello che la sim mostra a **+25% range** — cioè cattura **la maggior parte** del beneficio, con **un meccanismo** invece di quattro, ed è **già finanziato e brevettato**.
- **Cosa comporta:** licenza/royalty o co-sviluppo su airframe altrui. Evita di reinventare + evita di sviluppare l'IP da zero. **Ma** SUPAIR è un **concorrente italiano nella stessa nicchia** (partnership strategicamente delicata) ed è **pre-prodotto** (rischio timeline).
- **Costi `[STIMA, bassa]`:** ingresso partnership/licenza €0,3-1,0M + royalty €5-15k/unità; nessun dev airframe da zero.

### 2.4 Tabella TCO 5 anni — flotta 3 piattaforme (€M)

| Voce | **(A) BUY COTS** | **(B) BUILD BOXTILT** | **(C) PARTNER SUPAIR** |
|---|---|---|---|
| Dev / licenza ingresso | 0 | **3,0 → 6,0** (base→worst) | 0,3 → 1,0 |
| CapEx flotta (3 pf) | 2,4 | 1,8 (BOM bassa a volume minimo, ma dev sopra) | 2,1 |
| OpEx 5 anni (ramping) | 4,0 | 4,3 (manut. bespoke) | 4,1 |
| Beneficio OpEx range (−) | 0 (baseline) | −0,2 | −0,15 |
| Ritardo a ricavo | nessuno (Y1) | **Y3-Y4** (revenue persa Y1-Y3) | Y2-Y3 |
| **TCO 5y (base)** | **~€6,4M** | **~€8,9M** | **~€6,3M** |
| **TCO 5y (worst)** | ~€7,0M | **~€12M+** (dev €6M, cert. Certified) | ~€7,5M |
| **TRL / rischio tecnico** | **9 / basso** | **3-4 / alto** (aeroelastico, 4 tilt, cert.) | 5-6 / medio |
| **Disponibilità** | **subito** | 24-48 mesi | 2026+ (pre-prodotto) |

> **Verdetto §2:** BUILD è la strada **più cara di €2,5-5M+** e la **più lenta**, con il rischio tecnico più alto. BUY e PARTNER si equivalgono sul TCO, ma BUY è **disponibile ora e a TRL 9**. Il beneficio OpEx del range (−€0,2M su 5 anni) **non sposta la classifica di un millimetro**. Coerente con `10` §4.3 e `23` §7: nel modello-servizio, **Buy COTS batte Build su costo, tempo, rischio e time-to-market**.

---

## 3. NPV / IRR / payback delle tre strade nel modello-servizio

**Contesto di ricavo `[FATTO/STIMA]`:** mercato pagante **reale e piccolo** — Pentema **€40-150k/anno** (`10` §0), scale-up SNAI a €0,5M/pf/anno **solo con utilization >60%** (`23` §2, la linea servizio ha NPV project **−€1,88M** già di suo). Il mercato delivery medicale EU è **$0,5-1,2B al 2035, pilot-stage** (`R1`), con **Zipline non profittevole** dopo $600M e **Wingcopter a $1,73M di ricavi 2024** (`R2`). **Tetto finanziabile all'ingresso ~€1M** (`06`/`R5`).

### 3.1 KPI per strada (vista equity con grant, WACC 12%, orizzonte Y0-Y7) `[STIMA]`

| Strada | NPV@12% | IRR | Payback | Picco cassa | Commento |
|---|---|---|---|---|---|
| **(A) BUY COTS** | **−€1,9M** (≈ linea servizio `23`) | ~9% (con grant) | ~6 anni | −€3,3M | il meno peggio; cassa-positiva Y5; è già il caso-base di `23` |
| **(B) BUILD BOXTILT** | **−€4,5 → −€8M** | **n.d. (negativo)** | **mai (in 8 anni)** | **−€6 → −€9M** | dev €3-6M su mercato <€0,5M/anno → **non recupera**; è lo scenario *worst* di `23` §1.3 aggravato |
| **(C) PARTNER SUPAIR** | −€2,2 → −€3M | ~6-8% | ~7 anni | −€3,8M | vicino a BUY, ma dipende da un pre-prodotto di un concorrente |

**Lettura.** Nel modello-servizio **nessuna strada è brillante** (il mercato pagante è troppo piccolo, `23` lo dimostra), ma **BUILD è l'unica strutturalmente NPV-negativa senza via d'uscita**: aggiunge €3-6M di dev espensato a una linea di servizio già in perdita nel near-term, contro un beneficio OpEx da €10-70k/anno. **Il dev bespoke è un buco che il servizio, a queste dimensioni di mercato, non riempie mai.**

### 3.2 Sensitivity sui driver dominanti (NPV@12%, strada BUILD)

Base BUILD ≈ **−€6M**. Variazione di un driver alla volta `[STIMA]`:

| Driver | Δ NPV | Sensibilità |
|---|---|---|
| **Costo dev bespoke** (€3M → €6M) | **−€3M** | 🔴 massima — la variabile che affonda o "solo" peggiora |
| **Prezzo/ricavo servizio** (±25%) | ±€1,1M | 🔴 alta |
| **Dimensione flotta** (2 → 4 pf) | ±€1,0M (più flotta = più perdita se utilization bassa) | 🟠 alta |
| **Valore del +44%** (OpEx range €20k → €70k/anno) | **±€0,2M** | 🟢 **trascurabile** |
| **WACC** (10% → 15%) | ∓€0,4M | 🟡 media |

> **Il risultato più importante della sensitivity:** il **"valore del +44%"** — cioè la ragion d'essere tecnica del concept — è il driver **meno sensibile** (±€0,2M), **dominato di 15× dal costo di sviluppo** (±€3M). *In un'analisi economica, il vantaggio aerodinamico dell'idea è rumore; il suo costo di sviluppo è il segnale.* Questo, da solo, è quasi il verdetto.

---

## 4. Il nodo brevetto / IP: il concept è libero? Vale come moat?

### 4.1 Il 4-tilt su box-wing è arte nota — nessun moat difendibile `[FATTO, alta confidenza]`

Da `22` §4 e `18` §1.2:
- **Box-wing / PrandtlPlane:** Prandtl 1924 (best wing system), **pubblico da 100 anni**; **US 3.834.654 A "Boxplane wing"** (Lockheed/Miranda, 1974) **scaduto** = dominio pubblico.
- **Box-wing + eliche tiltanti a scala UAV:** **TiltOne** (box-wing tilt-wing, 4 eliche su 2 ali basculanti, SUPAERO/Prandtl), "Preliminary design of a Tiltwing UAV with a box wing configuration" (Springer), Elytron/Converticopter — **prior art accademica esplicita**, con delivery come applicazione citata.
- **Tilt-rotor:** arte nota profonda (Wingcopter ha brevettato il *proprio meccanismo*, non la configurazione).

**Conseguenza:** il concept "box-wing + 4 tilt-rotor" **non è brevettabile come tale**. Al massimo un **modello di utilità italiano debole e aggirabile** (es. combinazione specifica telaio-box/pod cargo), che non crea un moat durevole (`22` §4.2). **Per un operatore di servizi, il moat è nel servizio/dati/operazioni/autorizzazioni, non nell'airframe** — coerente con ABzero (5 brevetti sulla *capsula*, non sull'airframe; 90% COTS-compatibile; `R2`).

### 4.2 È libero dal brevetto SUPAIR? Sì — ma è un'arma a doppio taglio

- **SUPAIR brevetta il "ThrustPod" — un pod VTOL *retrattile*.** Il concept dell'utente usa il **tilt** (rotazione), un **meccanismo diverso**: **verosimilmente libero dalla rivendicazione specifica di SUPAIR** (freedom-to-operate plausibile, **da confermare con parere IP professionale — non fatto**).
- **Ma il taglio economico è netto:** la via **retrattile** (semplice, +25%, che cattura la maggior parte del beneficio) è **presidiata dal brevetto SUPAIR**; per **aggirarla** si sceglie il 4-tilt, **più complesso**, per un **+19pp marginale** di range e **senza ottenere IP propria difendibile** (§4.1). Si paga di più (4 meccanismi, aeroelasticità box) per **evitare un brevetto altrui** e **non costruirne uno proprio**. Economicamente è il peggiore dei mondi.

> **Verdetto §4:** **nessun moat IP forte** dal concept; il valore d'impresa aggiunto dall'"IP airframe" è **~zero** per un operatore di servizi. La libertà dal brevetto SUPAIR esiste ma **spinge verso la variante più costosa e meno difendibile**. L'unico IP che vale (pacchetto dati di qualifica: polare validata, clearance flutter, accettazione SORA, affidabilità provata) **non è configuration-specific** e si accumula anche operando COTS.

---

## 5. Verdetto di fattibilità economica netto

**BUILD BOXTILT come asset di servizio autofinanziato: NO, senza riserve.** Ragioni, tutte economiche:

1. Il **servizio si eroga meglio, prima e a minor rischio con COTS** (§2, §3) — il +44% si compra come endurance in un COTS più capace, non si costruisce.
2. Il **beneficio OpEx del +44% (€10-70k/anno) non ripaga** €3-10M+ di dev bespoke (§1, §3.2) — è il driver meno sensibile dell'NPV.
3. C'è un **concorrente italiano finanziato e brevettato (SUPAIR)** nella stessa nicchia con l'approccio più semplice (`R2`, §4).
4. Il **mercato pagante è piccolo** (Pentema €40-150k/anno; delivery EU pilot-stage; Zipline non-profit; Wingcopter $1,73M) e il **tetto finanziabile è ~€1M**: **€3-10M di dev è strutturalmente non autofinanziabile** (`06`/`R5`).
5. **Nessun moat IP** giustifica lo sviluppo (§4).

**La UNICA condizione sotto cui BUILD ha senso economico: come linea R&D/IP finanziata (≥70%) da grant a fondo perduto, con valore strategico indipendente dal servizio** — cioè **dimostratore tecnologico / vetrina di sovranità** e **trasferimento tecnologico verso l'HALE** (tilt, propulsione distribuita, aeroelasticità di ala non-convenzionale), **non** un prodotto/asset che deve ripagarsi dal mercato. In questa veste il costo è **coperto da denaro che non chiede ritorno né diluizione**, e il "ritorno" è apprendimento + posizionamento, non NPV di flotta. È esattamente il ruolo assegnato a BOXY in `10` §3.3 ("banco di prova IP, non prodotto operativo") e `18` §5 ("linea R&D/dimostratore, non prodotto").

### 5.1 Quali grant lo finanziano, e a quali condizioni `[FATTO, da R5/06]`

| Grant | Ticket / intensità | Condizione binding | Fit come R&D-BOXTILT |
|---|---|---|---|
| **Coopfond Cooding Prototypes** | €50k, ≤50% | rete ≥10 coop; finanzia **studio/prototipo**, non flotta | ✅ ingresso demo, già €50k deliberati per lo studio |
| **Coopfond Cooding Invest** | €250k, ≤70% | coop veicolo dedicata | 🟡 parte del dimostratore |
| **FESR Liguria Poli di R&I** | €0,3-2M/progetto, 25-50% cofin. | aggregazione a Polo (ATS) | 🟡 il canale più adatto per R&D airframe |
| **PNRR Aerospazio (ASI/ESA) / IS4Aerospace-Polito** | bandi PMI downstream | partnership prime/Polito | 🟡 possibile via Politecnico (dove nasce SUPAIR — attenzione conflitto) |
| **Horizon Europe / EIC Accelerator** | grant ≤€2,5M (+equity) | consorzio o spin-off SpA, TRL≥6 | 🟠 competitivo, richiede maturità |
| **EDF (post-EuroHAPS)** | €5-30M+ | consorzio 3 SM, dual-use, prime-led | 🔴 per 6B/HALE, non per un C3 |

**Condizioni trasversali non negoziabili `[FATTO, 06 §caveat / R5]`:**
- **Cofinanziamento 50%** (il collo di bottiglia reale, non la disponibilità del bando) — con floor equity coop €20-100k va coperto da equity founder Firmamento.
- **Regole di cumulazione e intensità d'aiuto** (de minimis / GBER): i grant **non si sommano liberamente**; il totale R&D-BOXTILT va verificato per non violare i massimali per beneficiario.
- **Asimmetria soggetto:** i grant Coopfond vanno alle **cooperative**, non a Firmamento SRL — l'asset R&D deve essere strutturato **a beneficio delle coop** (`06` implicazione n.2).
- **Un grant di R&D finanzia apprendimento/IP, non un prodotto vendibile:** rendicontabile come ricerca, non come acquisto di flotta operativa.

---

## 6. Kill-criteria e falsifying observations economiche

Osservazioni che, se verificate, rendono BUILD economicamente **insensato** (la maggior parte) o, all'opposto, **sensato** (la #7):

1. **[Marginalità del vantaggio]** Se **VLM/RANS** conferma che il range di BOXTILT supera la **migliore alternativa acquistabile/licenziabile** (RETRACT/SUPAIR, +25%) di **<15pp**, il valore incrementale è rumore → **BUILD economicamente morto** (il +44% nominale è un artefatto del confronto col COTS peggiore).

2. **[Costo di sviluppo]** Se la stima dev per una piattaforma bespoke **utilizzabile in servizio** supera **€2M** (altamente probabile, `10`/`22`) a fronte di un mercato pagante **<€200k/anno**, l'NPV non torna positivo su nessun orizzonte ragionevole → **BUILD morto come asset di servizio**.

3. **[Finanziabilità]** Se **non** si assicura un grant che copra **≥70% del dev come R&D a fondo perduto** (senza rimborso) **prima** di impegnare capitale, il dev €3-10M è **incompatibile col tetto finanziabile ~€1M** → **BUILD morto** (non autofinanziabile).

4. **[Beneficio OpEx]** Se il risparmio OpEx del +44% per la flotta realistica è **<€50k/anno** (probabile, §1.2), non riesce a **servire alcun debito** contratto per costruire → **BUILD morto** su base cash-flow.

5. **[Concorrenza brevettata]** Se **SUPAIR raggiunge il prodotto** (target estate 2026) e offre **licenza o COTS retrattile** a costo ragionevole, **PARTNER/BUY dominano BUILD** in modo assoluto → BUILD perde anche la ragione strategica.

6. **[Freedom-to-operate]** Se un **parere IP professionale** mostra che il 4-tilt-su-box è **bloccato** da SUPAIR o altri, BUILD non è nemmeno operabile senza licenza → **PARTNER domina** (e BUILD, senza IP propria, non ha upside).

7. **[Condizione di SENSATEZZA — l'unica]** BUILD diventa economicamente sensato **se e solo se, congiuntamente:** (a) un grant copre **≥70% del dev** come R&D puro; **E** (b) il dimostratore ha **valore strategico indipendente** (trasferimento tech verso HALE / vetrina di sovranità citabile per EDF/Horizon); **E** (c) VLM/RANS conferma un vantaggio **>20pp** su ciò che è acquistabile; **E** (d) la FTO è pulita. In quel caso **non è un asset di servizio**: è una **spesa di R&D/IP** giudicata su apprendimento e posizionamento, non su NPV di flotta.

---

## Riga di fondo

> Nel modello-servizio di Firmamento (flotta di proprietà, operatore non-OEM), il **+44% di autonomia** del box-wing 4-tilt vale, in OpEx ricorrente, **~€20-70k/anno lordi** per una flotta SNAI di 3 piattaforme — e **appena €10-30k/anno incrementali** rispetto alla migliore alternativa acquistabile, perché **il grosso del vantaggio non viene dall'ala chiusa ma dall'eliminazione dei rotori morti in crociera, che la variante retrattile (SUPAIR, brevettata, +25%) cattura con UN meccanismo invece di quattro.** Questo risparmio è **1-2 ordini di grandezza sotto** il costo di svilupparlo (**€3-10M+ bespoke, 24-48 mesi, TRL 3-4**), e la sensitivity lo conferma brutalmente: il "valore del +44%" muove l'NPV di **±€0,2M**, il **costo di sviluppo di ±€3M** (15×). Le tre strade nel modello-servizio: **(A) BUY COTS** — TCO 5y ~€6,4M, NPV@12% ~−€1,9M, disponibile subito, TRL 9 (**la strada di default**); **(B) BUILD BOXTILT** — TCO ~€9-12M, **NPV −€4,5/−€8M, payback mai**, alto rischio; **(C) PARTNER SUPAIR** — ~€6,3M, ma dipende da un pre-prodotto di un **concorrente italiano già brevettato nella nicchia**. Non c'è **moat IP** (arte nota da Prandtl 1924): l'airframe non aggiunge valore d'impresa a un operatore di servizi. **La condizione UNICA sotto cui BUILD ha senso economico è come linea R&D/IP finanziata ≥70% da grant a fondo perduto (Coopfond/FESR Poli/PNRR-Aero, con cofinanziamento e cumulazione verificati), con valore di vetrina-sovranità e trasferimento verso l'HALE — MAI come prodotto o asset di servizio autofinanziato,** perché il servizio si eroga meglio, prima e a minor rischio comprando COTS. Il filtro economico, che è il filtro decisivo della fattibilità, **respinge BOXTILT come asset di servizio e lo ammette solo come dimostratore grant-funded.**

---

## Fonti e confidenza

| Fonte | Tipo | Uso in questo capitolo | Confidenza |
|---|---|---|---|
| `sim_boxwing_tiltrotor.py` | Sim interna L0/L1 | +44% range, −23% Pcruise, +8% hover; scomposizione CD0/e | **segno alta, valore assoluto bassa** |
| `22-boxwing-vantaggio-tecnico.md` | Analisi aero interna | aero netto ~0% a C3, +€0,5-1,5M/6-18 mesi, no moat IP, prior art | media |
| `18-boxwing-tiltrotor-rivalutazione.md` | Rivalutazione interna | box-wing = dimostratore; tilt-wing vs 4-tilt indipendenti | media |
| `10-fasce-engineering.md` §3-4 | Costi interni | demo €150-400k; certificato €3-10M+; COTS T2 €0,58-0,82M | media (benchmark) |
| `23-economia-integrata-capitale.md` | Modello CFO interno | NPV/IRR linea servizio e prodotto, WACC, worst/best | medio-bassa |
| `06-finanziabilita.md` / `R5-finanziamenti.md` | Finanziamenti | tetto ~€1M, Coop2050 €500k, Galaxia €1M, FESR €150k, cumulazione | medio-alta (strumenti) |
| `R2-competitor.md` | Competitor verificati | Zipline non-profit, Wingcopter $1,73M, ABzero non-OEM 5 brevetti, giganti | alta |
| `R1-mercato-delivery-medicale.md` | Mercato verificato | EU medical delivery $0,5-1,2B 2035, pilot-stage; HEMS €2-7,2k/h | media (sizing low) |
| **SUPAIR** (supair.it, Politecnico di Torino, I3P) | Esterna | spinoff Polito nov 2024, ThrustPod brevettato retrattile, design phase estate 2026 | media (da riverificare su fonte primaria) |

**Limiti dichiarati:** (1) il **valore assoluto** del +44% è L0/L1, da riverificare con VLM/RANS — il segno è robusto, la magnitudine no; (2) i ricavi di servizio (€40-150k Pentema, €0,5M/pf SNAI) sono `[STIMA]` a confidenza bassa, nessun capitolato firmato; (3) il beneficio OpEx del range è una stima ingegneristico-finanziaria di primo ordine, non una distinta operativa reale; (4) **nessuna FTO professionale** è stata condotta sul concept vs SUPAIR — l'affermazione "libero dal brevetto" è a livello di screening; (5) i ticket dei grant vanno riverificati sui PDF di bando ufficiali prima di qualunque pianificazione vincolante (`R5` §0).
