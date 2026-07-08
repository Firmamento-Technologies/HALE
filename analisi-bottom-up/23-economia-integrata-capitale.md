# 23 — Economia integrata (PRODOTTO + SERVIZIO) e piano di capitale scaglionato

> **Progetto HALE — Firmamento Technologies · Terza tornata**
> **Autore:** Financial Analyst / Fractional CFO · **Data:** 2026-07-08
> **Mandato (raffinamento utente):** architettura a **due linee** — **BOXY (box-wing C3 ≤25 kg) = PRODOTTO da vendere** (dimostratore → prodotto finito; nicchie telemedicina/consegna medicale, AED, pacchi aree isolate); **MALE/HALE = SERVIZIO** (operato, mercato più grande, opex-intensivo, personale dedicato). Vincoli: **massimizzare profittabilità e sensatezza** e **non spaventare gli investitori con cifre enormi** (capitale scaglionato, ingresso modesto, milestone-gated).
> **Base:** `10-fasce-engineering.md` (costi piattaforma), `11-fasce-mercato-multimissione.md` (nicchie/pagatori/WTP), `06-finanziabilita.md` (strumenti e tetti), `12`/`13` (business/regolatorio), `20-SINTESI-fasce-e-proposta.md` (barbell).
> **Confidenza aggregata: MEDIO-BASSA.** Alta sui benchmark di costo/finanziamento ereditati (già triangolati); **bassa** su prezzi di vendita, volumi e ricavi/piattaforma (nessun prototipo venduto, nessun capitolato firmato). **Nessuna cifra qui è una quotation reale né un ricavo contrattualizzato.**

---

## 0. Metodo, regola di lettura e caveat che cambiano il verdetto

**Regola epistemica.** `[DATO]` = fonte ufficiale/benchmark verificato nei report `05`/`06`/`10`/`11`. `[STIMA]` = elaborazione del CFO, confidenza dichiarata. Scale sempre esplicite (**€k** vs **€M**). Tassi: WACC **nominale, post-imposte, blended** (grant a costo 0% + equity aerospace seed 25-35% + debito agevolato Marcora/CDP 0-6%) ⇒ **WACC base 12%** (sensibilità 10%/15%). Orizzonte **Y0-Y7** (8 anni). Modello a `scratchpad/model.py` + `model2.py`.

**Tre caveat che condizionano tutto il capitolo — da leggere PRIMA dei numeri:**

1. **[CAVEAT-DEV] Il costo di sviluppo di BOXY dipende dalla base di certificazione.** `10` §3.3 falsifica il target €300k *se* BOXY è "prodotto certificato per servizio autorizzato" → **€3-10M+**. Il modello base qui usa **€2,5M di dev** (`[STIMA]`), che è una **via di mezzo esplicita**: prodotto in **piccola serie, minimamente industrializzato, venduto a operatori in Specific Category che ottengono la *propria* SORA** — NON un prodotto type-certificato "chiavi in mano". **Se serve piena certificazione (Certified/type-cert per uso medicale seriale), il dev sale a €4-8M e la linea prodotto va in perdita** (è la direzione dello scenario *worst*). Questo è il singolo rischio più grande. Confidenza sul dev: **bassa**.

2. **[CAVEAT-AIRFRAME] Tensione airframe↔missione (da `11` §1).** Un box-wing high-AR è **ottimizzato per loiter/EO**, non per la **consegna VTOL punto-punto**. Le nicchie che l'utente cita (medicale/AED/pacchi) sono **delivery-centriche** e premiano un **cargo-VTOL** (Wingcopter/ABzero), non un box-wing. ⇒ Il **mercato primario difendibile per BOXY-prodotto è EO/ISR/mapping** (dove l'airframe calza e la persistenza differenzia); la **variante consegna** richiede una configurazione diversa ed entra su un terreno **già presidiato** (ABzero incumbent italiano). Il benchmark prezzo €120k (Wingcopter, delivery) è usato come **ancora di fascia**, non come promessa di battere l'incumbent sul suo airframe.

3. **[CAVEAT-SERVIZIO] "MALE/HALE = servizio" va servito, near-term, con T2 (mid-VTOL), non con MALE/HALE.** `06`/`11` sono netti: il **MALE (T3)** è presidiato dai prime e richiede equity esterno (Taglia B, prob. 30-50%); l'**HALE (T4)** è fuori portata (Taglia C). La **linea servizio finanziabile oggi è T2 mid-VTOL operato as-a-service**; MALE è il **tier di scala Y3-5 (equity-gated)**, HALE resta **vettore strategico Y6+ fuori P&L**. Modello la linea servizio come **T2**, con MALE come opzione di scala dichiarata.

---

## 1. LINEA PRODOTTO — BOXY venduto (hardware + ricorrente)

### 1.1 Assunzioni unit-economics `[STIMA salvo dove segnato]`

| Voce | Base | Range worst→best | Fonte/ragionamento |
|---|---|---|---|
| **Costo dev-a-prodotto** (Y0-Y2) | **€2,5M** | €3,85M → €1,85M | via di mezzo tra demo €150-400k `[10 §3.3 DATO]` e certificato €3-10M `[10 DATO]`; vedi CAVEAT-DEV |
| **Prezzo di vendita/unità** | **€120k** | €95k → €150k | ancora Wingcopter ~€120k `[utente/DATO]`; JOUAV/ALTI/Latitude HQ €55-180k `[10 §4.1 DATO]` |
| **BOM + costo diretto/unità** (a regime) | **€55-70k** | €72-80k → €42-55k | scomposizione: airframe lino/CFRP €8-15k, propulsione €5-10k, batterie €4-8k, avionica €5-12k, payload/interfaccia €3-6k, datalink €4-8k, GS pro-quota €5-10k, assemblaggio/test €10-20k `[STIMA ingegneristica]` |
| **Margine lordo/unità** (a regime) | **€65k (54%)** | €23k (24%) → €108k (72%) | prezzo − BOM; curva di apprendimento sul BOM |
| **Ricavo ricorrente/unità/anno** (manut+spare+SW) | **€30k** (GM 60%) | €22k → €40k | ~20-25% del prezzo/anno, modello ibrido hardware+servizi |
| **OpEx fisso di linea** (vendite/support/G&A) | €0,35→0,60M/anno | — | struttura commerciale minima + supporto prodotto |

### 1.2 P&L linea PRODOTTO — scenario BASE (cassa, €M)

| | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 |
|---|---|---|---|---|---|---|---|---|
| **Unità vendute** | 0 | 0 | 4 | 8 | 12 | 16 | 20 | 22 |
| Ricavo hardware | 0 | 0 | 0,48 | 0,96 | 1,44 | 1,92 | 2,40 | 2,64 |
| Ricavo ricorrente (base installata) | 0 | 0 | 0 | 0,12 | 0,36 | 0,72 | 1,20 | 1,80 |
| Margine lordo (HW+ricorr.) | 0 | 0 | 0,20 | 0,57 | 0,91 | 1,42 | 2,00 | 2,51 |
| Dev (R&D) | −0,30 | −0,90 | −1,30 | 0 | 0 | 0 | 0 | 0 |
| OpEx fisso linea | −0,10 | −0,15 | −0,35 | −0,42 | −0,48 | −0,54 | −0,58 | −0,60 |
| **Cash flow netto** | **−0,40** | **−1,05** | **−1,45** | **+0,08** | **+0,43** | **+0,88** | **+1,42** | **+1,91** |

### 1.3 Break-even e profittabilità

- **Break-even OPERATIVO annuo:** costi fissi di linea a regime €0,55M / margine €60k per unità ⇒ **~9-10 unità/anno** coprono i costi fissi (prima del recupero dev). `[STIMA]`
- **Break-even sul DEV (cumulato):** €2,5M / €65k margine ⇒ **~38 unità cumulate**, raggiunte a ritmo base intorno a **Y5-Y6**. `[STIMA]`
- **KPI linea prodotto (equity view, con grant 40%+credito 10% sul dev):** NPV@12% **+€0,88M**, **IRR ~22%**, **payback ~5,2 anni**, picco cassa **−€2,3M**. `[STIMA]`
- **Worst (prezzo €95k, margine €23k/unità, dev €3,85M):** break-even dev **167 unità** → irraggiungibile; NPV **−€3,4M**, **non recupera**. La **compressione di prezzo è fatale** (margine sottile → nessun volume realistico ripaga il dev).
- **Best (prezzo €150k, margine €108k/unità, volumi 10→55/anno):** NPV **+€14M**, IRR **>100%**, payback **~2,3 anni**.

> **Verdetto linea prodotto:** **profittevole a bassi/medi volumi — a due condizioni**: (1) **prezzo ≥€120k** difeso da differenziazione (persistenza EO / integrazione AED-medicale), NON in gara sul prezzo contro COTS; (2) **dev tenuto ≤€2,5M** con base "Specific-operator", non piena certificazione. Sotto queste condizioni la linea è **operativamente in utile a ~9-10 unità/anno** e ripaga il dev a ~38 unità (~Y5-6). L'asimmetria (worst −€3,4M / best +€14M) è un **profilo venture puro**: la leva è **prezzo × volume**, non i costi.

---

## 2. LINEA SERVIZIO — MALE/HALE operato (near-term: T2 mid-VTOL)

### 2.1 Assunzioni per-piattaforma `[STIMA salvo dove segnato]`

| Voce | Base | Range | Fonte/ragionamento |
|---|---|---|---|
| **CapEx/piattaforma** (T2 COTS) | **€0,80M** | €0,75-0,90M | JOUAV CW-30E sistema €580-820k `[10 §4.1 DATO]` |
| **Ricavo/piattaforma/anno** (a regime) | **€0,50M** | €0,35-0,65M | ~350-500 h fatturabili × €1.000-1.400/h, o 1-2 convenzioni; ancora superiore EMSA €1,9-2,2M/velivolo `[05 DATO]` è tier MALE, non T2 |
| **OpEx/piattaforma/anno** | **€0,32M** | €0,30-0,36M | personale dedicato ~2 FTE €120-200k + manut. €30-60k + assicuraz. BVLOS €15-40k + carburante/connett./SW €20-40k `[briefing/05 DATO parziale]` |
| **Overhead centrale/anno** (mgmt, LUC, ops center, autorizzazioni) | €0,30→0,44M | — | costo fisso indipendente dalla flotta |
| **Organico linea servizio** | 4-8 FTE | — | piloti BVLOS, operatori, manutentore, analyst, PM/accountable manager (LUC) |

### 2.2 P&L linea SERVIZIO — scenario BASE (cassa, €M)

| | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 |
|---|---|---|---|---|---|---|---|---|
| **Piattaforme attive** | 0 | 1 | 1 | 2 | 3 | 3 | 3 | 3 |
| Ricavo servizio | 0 | 0,25 | 0,50 | 1,00 | 1,50 | 1,50 | 1,50 | 1,50 |
| OpEx (piattaforme + centrale) | 0 | −0,62 | −0,64 | −0,98 | −1,32 | −1,34 | −1,36 | −1,36 |
| CapEx (nuove piattaforme) | 0 | −0,80 | 0 | −0,80 | −0,80 | 0 | 0 | 0 |
| **Cash flow netto** | **0** | **−1,17** | **−0,14** | **−0,78** | **−0,62** | **+0,16** | **+0,14** | **+0,14** |

### 2.3 Break-even e scala

- **Contribuzione/piattaforma a regime:** €0,50M − €0,32M = **€0,18M**. **Break-even flotta:** overhead centrale €0,38M / €0,18M ⇒ **~2,1 piattaforme** solo per coprire il fisso centrale; **utile operativo a 3 piattaforme**. `[STIMA]`
- **KPI linea servizio (project, 8 anni):** NPV@12% **−€1,88M**, cassa-positiva **solo da Y5**. **È la linea che frena** l'insieme: capex-intensiva, ritorno lento.
- **Worst (ricavo €0,35M, opex €0,36M/pf):** **contribuzione NEGATIVA per piattaforma** (−€10k) → si **perde su ogni ora di volo**. È la traduzione concreta dell'avvertimento "non assumere 100% utilization": con utilization bassa il servizio è **strutturalmente in perdita**.
- **Best (ricavo €0,65M, flotta 5):** NPV **+€0,61M**, IRR **23%**.

> **Verdetto linea servizio:** **opex-intensiva, marginale, e profittevole solo a scala ≥3 piattaforme** con **utilization difesa (>60%)** e **overhead centrale ammortizzato**. Diventa cassa-positiva a Y5 nel base; richiede **CapEx €2,4M (flotta 3) + capitale circolante + equity esterno** (Taglia B, `06` §4.2). Il **tier MALE (T3)** moltiplica ricavo (€1,5-2M/pf, ancora EMSA) **e** capex (€2-10M/pf) e va attivato solo Y3-5 con equity Series A. **HALE resta fuori dal P&L.**

---

## 3. PIANO DI CAPITALE SCAGLIONATO — "non spaventoso", milestone-gated

Principio: **nessuno stage chiede una cifra enorme; ogni stage è derisckato dal precedente prima di partire.** Cifre **nette di grant** (i grant sono a fondo perduto, non diluiscono). Picco di esposizione equity+debito **base ~€3,3M** (Y3); grant totali attivati **~€2,2M**; fabbisogno lordo di progetto **~€5,1M** (Y4).

| Stage | Finestra | **Cifra da mostrare** (equity+debito, netto grant) | Milestone di sblocco (gate) | Fondi mappati | Cosa deriscka |
|---|---|---|---|---|---|
| **Stage 0 — Ingresso** | Y0 (M0-12) | **€150-500k** | dimostratore BOXY **volato** (VLOS/Open A3) + **1 LoI** Regione/ASL su servizio EO | Coopfond €50k `[DATO, già deliberato]` + FESR OS1.1.1 + equity founder modesto + credito R&S | rischio tecnico base + domanda |
| **Stage 1 — Prodotto + primo servizio** | Y1-Y2 (M12-30) | **€1,5-2,5M** (in 2 tranche gated) | **1ª vendita/LoI d'ordine BOXY** + **autorizzazione BVLOS** (SAIL II) + 1ª piattaforma servizio operativa | Coopfond Invest + Nuova Marcora + FESR Poli R&I + **PNRR-Aero/Horizon** (dev IP) + credito R&S + equity founder €150-350k `[06 §5, condizione binding]` | industrializzazione prodotto + moat BVLOS |
| **Stage 2 — Scala servizio** | Y3-Y4 (M30-54) | **€1,5-3M** | **1° contratto servizio pluriennale** firmato (utilization provata) + flotta a 3 piattaforme | **CDP Venture / EDF / PNRR-Aero** + debito CDP/Cooperfidi + ricavi ricorrenti | opex-intensità servizio + scala flotta |
| **Stage 3 — Autofinanziamento / MALE** | Y5+ (M54+) | **autofinanziato**; MALE-tier = Series A dedicata | linea prodotto cassa-positiva; se MALE: term-sheet equity ≥€1M | ricavi + Series A / consorzio EU (MALE/HALE = veicolo separato) | — |

**Perché non spaventa (lettura per l'investitore):**
- Lo **Stage 0 (€150-500k)** è quasi interamente **grant + €50k già in cassa**: l'ingresso privato è **simbolico**.
- Lo **Stage 1 (€1,5-2,5M)** arriva **in due tranche gated** (dev prodotto industrializzazione ~€0,9-1,3M sbloccata dalla 1ª vendita; primo servizio ~€0,75M largamente coperto FESR/Coopfond) — **mai un lump da €2,5M**.
- Il **picco di esposizione equity+debito è ~€3,3M** (Y3), non i €5-11M del percorso HALE del Briefing: la **linea prodotto+servizio T2** vive **un ordine di grandezza sotto** l'R&D HALE.
- **MALE/HALE non entrano nel conto** finché la linea prodotto non è cassa-positiva → l'investitore **non vede mai la cifra grande** finché il rischio non è già ripagato.

### 3.1 Fabbisogno netto per finestra (base, grant-adjusted) `[STIMA]`

| Stage | Cash flow netto di periodo | Uscite lorde nel periodo |
|---|---|---|
| Stage 0 (Y0) | −€0,40M | −€0,40M |
| Stage 1 (Y1-Y2) | −€2,89M | −€2,89M |
| Stage 2 (Y3-Y4) | ~pari (−€0,05M) | −€0,05M |
| Stage 3 (Y5-Y7) | **+€4,97M** | 0 |

---

## 4. Sintesi finanziaria — NPV / IRR / payback (combinato)

WACC base **12%** (nominale, post-imposte). Due viste: **PROJECT** (unlevered, senza grant, la più prudente) ed **EQUITY** (grant a fondo perduto ~€2,2M che coprono ~40% dev + ~40% capex servizio + credito R&S 10%, con lag 1 anno).

| Scenario | Vista | NPV@10% | NPV@12% | NPV@15% | IRR | Payback | Picco cassa |
|---|---|---|---|---|---|---|---|
| **WORST** | Project | −€8,6M | **−€8,2M** | −€7,6M | n.d. | mai | −€11,1M (Y7) |
| | Equity (grant) | — | **−€6,3M** | — | n.d. | mai | −€8,4M |
| **BASE** | Project | −€1,8M | **−€1,95M** | −€2,1M | −2% | mai (8 anni) | −€5,1M (Y4) |
| | **Equity (grant)** | — | **−€0,36M** | — | **~9%** | **~6,1 anni** | **−€3,3M (Y3)** |
| **BEST** | Project | +€15,5M | **+€13,9M** | +€11,7M | **80%** | 3,2 anni | −€2,5M (Y2) |
| | Equity (grant) | — | **+€15,5M** | — | **97%** | 2,6 anni | −€1,8M |

**Lettura.**
- **Base combinato ≈ break-even** su 8 anni (equity NPV −€0,36M, IRR ~9% ≈ WACC): l'insieme **non distrugge valore ma non lo crea granché entro Y7**, perché la **linea servizio (NPV −€1,9M project) trascina** la linea prodotto (~break-even project, +€0,88M equity da sola). Il **cumulato equity diventa positivo a Y7** (+€1,8M): un DCF a 10 anni sarebbe nettamente positivo (le due linee sono cassa-positive da Y5).
- **La linea PRODOTTO da sola batte il combinato** (equity NPV +€0,88M vs −€0,36M): la coda opex del servizio è la zavorra. **Implicazione:** il servizio va tenuto **lean e grant/equity-funded**, non caricato come flotta capex sullo stesso P&L finché non raggiunge ≥3 piattaforme con utilization provata.
- **Il grant sposta il verdetto**: da project −€1,95M a equity −€0,36M (base), e **dimezza il picco di cassa** (−€5,1M → −€3,3M). I grant sono la **leva di de-risk n.1**, non un extra.

### 4.1 Sensitivity — NPV@12% base combinato (project, tornado top-driver)

Base = **−€1,95M**. Variazione di un driver alla volta:

| Driver | Δ NPV | Sensibilità |
|---|---|---|
| **Volumi prodotto ±30%** | **±€1,22M** | 🔴 massima |
| **Ricavo/piattaforma servizio ±25%** | **±€1,14M** | 🔴 massima |
| **Prezzo prodotto ±20%** | **±€1,10M** | 🔴 alta |
| **Costo dev +50% / −30%** | −€1,07M / +€0,64M | 🟠 alta (asimmetrica) |
| **OpEx servizio +25% / −15%** | −€0,77M / +€0,46M | 🟡 media |

**Le 3 variabili che decidono il progetto:** **(1) volumi di vendita BOXY**, **(2) ricavo/utilization della piattaforma servizio**, **(3) prezzo di vendita BOXY** — tutte ~±€1,1-1,2M sull'NPV. Poi il **costo di sviluppo** (rischio CAVEAT-DEV, asimmetrico verso il basso). L'**opex del servizio** è meno sensibile del suo **ricavo**: il problema del servizio è la **domanda/utilization**, non il costo unitario.

---

## 5. Quadro Economico sintetico (art. 41, Stage 0-1 — asset capitalizzabili) `[STIMA]`

Solo per le componenti **infrastrutturali/asset** (non R&D espensata). Scala **€k**.

```
A) Importo investimenti (asset)
   A.1 Dimostratore BOXY (materiali, propulsione, avionica)      150–300
   A.2 1ª piattaforma servizio T2 (COTS) + payload               600–800
   A.3 Ground segment (GS fissa+mobile, hangar leggero)          120–250
                                              Totale A            870–1.350
B) Somme a disposizione
   B.1 Spese tecniche (progettaz., SORA, DL, RUP)                 80–160
   B.2 Imprevisti (10–15% di A) [base-rate aerospace: alzare]     90–200
   B.3 IVA su A (22%, se non recuperabile nel regime)             190–300
   B.4 Certificazioni/autorizzazioni (BVLOS, DG, DPIA)            40–110
   B.5 Formazione team + collaudo/verifica                        40–90
                                              Totale B            440–860
   TOTALE GENERALE (A+B)                                          1.310–2.210
```
> Nota base-rate: per l'imprevisti aerospace usare **+30% minimo, +50% prudente** (GAO-20-195G); il dev R&D (BOXY dev €2,5M) è **espensato**, non nel Quadro asset.

---

## 6. Kill-criteria e falsificazione (coerenti con `06`/`11`/`12`)

- **Prodotto — prezzo:** se a Stage 1 le LoI d'ordine arrivano solo **<€100k/unità**, il margine crolla sotto €40k → break-even dev >80 unità → **linea non profittevole** → ridurre a demo-IP (Gamba B di `20`) o cambiare nicchia.
- **Prodotto — dev:** se la base di certificazione impone **Certified/type-cert** (dev >€4M), la linea prodotto va **NPV-negativa** → vendere solo a operatori Specific o non industrializzare.
- **Prodotto — airframe:** se la nicchia pagante è **solo consegna** (non EO), il box-wing è l'airframe sbagliato (`11`) e si compete con ABzero sul suo terreno → **ripiegare su EO/ISR come mercato primario del prodotto**.
- **Servizio — utilization:** se a Y2 l'utilization <50% (ricavo/pf <€0,35M) → **contribuzione negativa** → non aggiungere piattaforme, non scalare la flotta.
- **Servizio — anchor:** nessun **contratto pluriennale** (non-pilota) firmato entro Stage 2 → il servizio resta grant-pilota (`11` §6) → congelare a 1 piattaforma.
- **Capitale:** se l'**equity founder ≥€150k** non è deliberato entro M+9 (`06` §5), Stage 1 non parte e il piano resta al floor €300-600k.

---

## 7. Verdetto sintetico

1. **La linea PRODOTTO (BOXY venduto) è la fonte di valore e di ritorno**, ma **solo** con prezzo ≥€120k e dev ≤€2,5M (Specific-operator, non Certified): profittevole a **~9-10 unità/anno** operativamente, ripaga il dev a **~38 unità (~Y5-6)**, equity IRR ~22% base, upside venture nel best (IRR >100%). **Fragile** a prezzo/volumi e al rischio-certificazione.
2. **La linea SERVIZIO (T2 operato) è il mercato più grande ma la zavorra finanziaria**: profittevole **solo ≥3 piattaforme** con utilization >60%, cassa-positiva da Y5, capex-intensiva, equity-esterno-dipendente. MALE = scala Y3-5; HALE = fuori P&L.
3. **Combinazione più sensata:** **prodotto come motore near-term di cassa/valore; servizio T2 lean, grant/equity-funded, come generatore di domanda e track-record BVLOS, scalato solo su anchor firmato.** Le due linee condividono **bus, autorizzazioni e brand** (barbell di `20`/`12`), ma con **P&L separati e servizio non caricato di capex-flotta** finché non prova l'utilization.
4. **Il piano di capitale non spaventa**: ingresso €150-500k (quasi tutto grant), Stage 1 €1,5-2,5M in tranche gated, picco esposizione equity+debito **~€3,3M** — **un ordine di grandezza sotto** il percorso HALE. I grant (~€2,2M) sono la leva di de-risk n.1.

---

## 8. Fonti e limiti

**Interne (già triangolate):** `05`/`10` (costi piattaforma, demo €150-400k, cert. €3-10M, JOUAV CW-30E, EMSA €7,5-8,75M/anno), `06` (strumenti, Taglie A/B/C, floor equity €20-100k, €50k Coopfond `[DATO CERTO]`), `11` (nicchie/pagatori/WTP, ABzero incumbent, airframe loiter≠consegna), `12`/`13` (barbell, bus, LUC, trigger DG consegna), `20` (sintesi barbell). Vincolo `CLAUDE.md`.

**Limiti dichiarati (da chiudere prima del gate):**
- **Nessun prezzo di vendita né volume reale**: prezzo €120k e volumi 4-55/anno sono **`[STIMA]` a confidenza bassa** — il best/worst diverge di 10× sull'NPV.
- **Costo dev €2,5M**: stima **bassa confidenza**, dipende dalla base di certificazione (CAVEAT-DEV) — è la variabile che può ribaltare la linea prodotto.
- **Ricavo/piattaforma servizio €0,5M**: nessun capitolato firmato; l'utilization è l'incognita che rende il servizio profittevole o strutturalmente in perdita.
- **BOM/unità**: scomposizione ingegneristica, non una distinta base reale.
- I grant sono **cumulabili solo entro le regole di intensità d'aiuto** (de minimis/GBER, `06`): il €2,2M assunto va verificato per non violare massimali per singolo strumento/beneficiario.

**Azioni di validazione:** (1) RFQ reale su BOM BOXY e su 1 piattaforma T2; (2) pre-application ENAC per costo/base di certificazione del prodotto (CAVEAT-DEV); (3) LoI prezzo/volumi da ≥2 clienti prodotto; (4) 1 convenzione servizio con utilization stimata; (5) delibera equity founder ≥€150k.
