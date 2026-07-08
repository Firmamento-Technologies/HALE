# 03 — Mercato bottom-up: chi paga davvero per connettività + Earth Observation nelle Aree Interne

**Progetto HALE / Firmamento Technologies — analisi ripartita da zero (pivot "operatore di servizi")**
**Data:** 2026-07-08 · **Autore:** aerospace-market-analyst · **Confidenza complessiva:** medium sui fatti di budget PA, low-medium sulle stime SOM.

> **Mandato.** Rispondere a UNA domanda: quanto vale *realisticamente* il mercato indirizzabile **pagante** per servizi ricorrenti di connettività + EO alle Aree Interne italiane (da Liguria/Pentema, scalabile a SNAI Italia), erogati da un operatore cooperativo? Il numero che conta non è il TAM teorico: è il **tetto di ricavo plausibile**, perché quello determina quanto è razionale investire.
>
> **Metodo.** Bottom-up: si parte dai **pagatori reali** e dalle **linee di budget esistenti**, non da CAGR di report commerciali. Le stime TAM/SAM/SOM già nel repo (`cap-07`: SOM Y3 €1,5-3,5M; SAM 2030 €40-100M) sono lette **criticamente e NON assunte**. La classe di piattaforma (VTOL/MALE/HALE) è trattata come variabile aperta: il mercato è indifferente a *come* si eroga il dato, paga solo per l'output.
>
> **Regola epistemica.** Ogni cifra è marcata `[fatto|stima; fonte; confidence]`. Fatto = dato verificabile da fonte terza. Stima = elaborazione dell'analista, dichiarata.

---

## 0. Sintesi dei risultati (il resto del documento la argomenta)

| Metrica | Worst (2028-30) | Base (2028-30) | Best (2028-30) | Fonte-ancora |
|---|---|---|---|---|
| **SOM Firmamento a 5 anni — ricavo TOTALE annuo (grant+commerciale)** | **€80-150k** | **€250-500k** | **€0,9-1,8M** | triangolazione §5-6 |
| di cui **ricorrente commerciale genuino** (non-grant) | €30-70k | €120-280k | €0,4-0,9M | §6 |
| **Tetto d'investimento razionale** (giustificato dal mercato) | ~€0,3M | **~€0,8-1,2M** | ~€2-3M | §7 |

**Confronto di realtà (fatto):** il *business plan del progetto stesso* (bando Cooding) proietta ricavi da vendite di **€0 (Y1) → €61.414 (Y2, 10 contratti) → €156.606 (Y3, 20 contratti)** `[fatto; bando/Business Plan.md righe 445-472; confidence: high]`. È tra il mio scenario worst e base. La stima cap-07 di €1,5-3,5M Y3 è **10-20× superiore** al piano economico interno e non è supportata bottom-up.

**Verdetto sintetico:** il mercato pagante esiste ma è **piccolo, frammentato e grant-dipendente**. Non giustifica un HALE dedicato (R&D €5,5-11M). Giustifica al massimo un **pilota VTOL/drone commerciale largamente finanziato da bandi** (Percorso 6A). Il segmento più solido è **B2G ancorato a grant SNAI/FESR/PNRR per monitoraggio del territorio** (EO), non la connettività (uccisa da Starlink) e non l'utility (porta chiusa da in-house).

---

## 1. Perché "bottom-up" cambia la risposta

Il TAM top-down HAPS/droni è ingannevole perché mescola R&D pubblica, difesa e hardware. Bottom-up si chiede: *esiste una riga di bilancio, oggi, da cui un ente stacca un assegno ricorrente a Firmamento per un servizio EO/connettività?* La risposta determina tutto. Le Aree Interne sono, per definizione istituzionale, **territori a domanda debole e budget pubblico sottile**: la SNAI nasce proprio perché il mercato lì non arriva. Vendere un servizio *a pagamento* dentro un'area definita dalla sua incapacità di sostenere servizi è strutturalmente difficile — il finanziatore quasi sempre è lo Stato/UE via grant, non l'utente.

### Il territorio-ancora in cifre (fatti)
- **Liguria aree interne:** 8 aree di progetto SNAI, **118 comuni, 203.367 ab, densità 66,7 ab/km²** `[fatto; rapporto-istruttoria_regione-liguria.md; confidence: high]`.
- **Area pilota Antola-Tigullio** (dove sta Pentema, frazione di Torriglia): **16 comuni, 16.710 ab, 592 km²**; Torriglia **2.198 ab, -8,1%** demografico `[fatto; Dossier SNAI.md; confidence: high]`.
- **Pentema:** frazione di poche decine di residenti. È un *caso dimostrativo*, non un mercato.
- **SNAI Italia (scala massima):** 124 aree, **1.904 comuni, 4,57M ab** `[fatto; politichecoesione.governo.it; confidence: high]`.

Implicazione: anche catturando *tutta* la Liguria interna, la base-clienti finale sono ~200k abitanti sparsi e ~118 micro-comuni. Lo scale-up nazionale moltiplica per ~22 il numero di aree, ma con gli stessi vincoli di budget.

---

## 2. Chi paga davvero — mappa pagatore → budget reale → cattura plausibile

Tabella-cardine. "ACV" = Annual Contract Value plausibile per Firmamento. "Prob." = probabilità di cattura entro 5 anni (giudizio dell'analista).

| # | Pagatore | Riga di budget REALE che esiste | Natura | ACV plausibile Firmamento | Prob. | Confidence |
|---|---|---|---|---|---|---|
| 1 | **Regione Liguria (SNAI/FESR)** | FESR 21-27 **€630M** tot; digitale solo **€10M** (90% a imprese); energia €57M `[fatto; regione.liguria.it]`. SNAI Liguria ~€30M ma per **salute/scuola/mobilità** | Grant/convenzione R&D-pilota | €50-200k/anno (a bando vinto) | Media | medium |
| 2 | **Protezione Civile reg. / ARPAL** | AIB Liguria elicotteri **€248.530** (290h × €857/h, 2021) `[fatto; Regione Liguria]`; ARPAL ha **team droni interno** (4 piloti) `[fatto; SNPA/ARPAL]` | Servizio / pilota | €0-100k/anno | Bassa | medium |
| 3 | **Singoli Comuni montani** | Bilanci €1-4M quasi interamente vincolati; L.bilancio 2025 stanzia **solo €5M/anno per TUTTI** i comuni <3.000 ab totalmente montani (servizi sociali) `[fatto; camera.it/RGS]` | Spesa discrezionale ~€0 | €0-5k/anno cad. | Molto bassa | medium |
| 4 | **Unioni di Comuni** | Veicolo di aggregazione SNAI (Antola, Scrivia…); spendono da fondi SNAI/FESR | Grant aggregato | €10-50k/anno per Unione | Bassa-media | low |
| 5 | **Utility (Terna/Enel/Iren/RFI)** | Terna **~€50M/anno** ispezioni ma con **flotta interna 34 droni + 7 elicotteri**, e ha **finanziato Wesii (startup droni di Chiavari, €2,8M)** `[fatto; Terna/Industria Italiana]` | Appalto quadro | €0-100k niche subcontract | Molto bassa | high (porta chiusa) |
| 6 | **Consorzi agricoli/forestali** | Coop agricole del network (Monte di Capenardo, olivicoltori): micro-budget; NDVI drone commoditizzato €350-1.000/job | Servizio spot | €5-20k/anno aggreg. | Bassa | low |
| 7 | **Cooperative di comunità (le 10 pilota)** | Micro-entità; sono **utenti-partner, non clienti paganti**. Il BP stesso implica ~€6k/coop `[fatto; bando/BP]` | Bundle sovvenzionato | €5-10k/anno cad. | Media (ma grant) | medium |
| 8 | **Telco (wholesale NTN)** | Backhaul rurale via NTN è **post-3GPP Rel.18/19**, non commerciale a 3-5 anni | Futuro | ~€0 a 5 anni | Nulla (near-term) | medium |
| 9 | **Enti Parco / ARPA ambiente** | Parco Antola/Aveto: budget €1-3M, monitoraggio a progetto | Grant/pilota | €5-30k/anno | Bassa | low |

**Lettura trasversale:** i due pagatori con budget "vero e grande" — **Regione** (FESR €630M) e **utility** (Terna €50M/anno) — sono i due dove Firmamento cattura meno: il FESR digitale è 90% a imprese e minuscolo (€10M), Terna fa tutto in-house e ha già la *sua* startup ligure. I pagatori "accessibili" (comuni, coop) **non hanno budget**. Questa è la tenaglia strutturale del mercato Aree Interne.

---

## 3. Willingness-to-pay per caso d'uso (evidenza, non asserzione)

### 3.1 Connettività aree bianche — WTP quasi nulla
- Digital divide Antola-Tigullio: **25,35% pop. mobile <30 Mbit/s**; ma fisso VHCN 100 Mbit/s "passed" al **92,31%**, e il **Piano BUL Liguria vale €43,1M** (Infratel/Open Fiber, terrestre) `[fatto; Dossier SNAI.md d.1-d.6; OpenCoesione]`. La white-zone residua **si sta chiudendo con fibra pubblica**.
- **Sostituto letale:** Starlink Italia **€29-40/mese** residenziale, hardware €299-349 `[fatto; Corriere Comunicazioni; SOStariffe; confidence: high]`. Un servizio HAPS/aereo di connettività *all'utente finale* è fuori mercato sul prezzo. L'unico valore difendibile è **connettività d'emergenza/backhaul temporaneo** — episodica, piccola, difficile da contrattualizzare come ricorrente.
- **Verdetto WTP connettività:** near-zero per il ricorrente. Il claim "5G ovunque dall'alto" non ha un pagatore.

### 3.2 Monitoraggio dissesto idrogeologico — budget grande, ma non per il monitoraggio-servizio
- Nazionale: **€19,2 mld** stanziati in 25 anni (26.000 interventi), spesa media **~€280-329M/anno**, ma **solo il 27% effettivamente speso** e quasi tutto in **opere civili**, non in monitoraggio EO `[fatto; ISPRA ReNDiS; OCPI Cattolica; confidence: high]`. Il monitoraggio è una frazione marginale, spesso interna (ARPAL, piezometri/inclinometri).
- **Sostituto:** ARPAL fa già rilievi con droni propri; Copernicus EGMS (subsidenza) è gratuito. WTP per un servizio esterno persistente: bassa, *salvo* progetto grant-finanziato.

### 3.3 Antincendio boschivo — budget reale ma presidiato
- Liguria: elicotteri AIB **€248,5k (2021)**; flotta Canadair statale **€59M/estate** `[fatto; Regione Liguria; Panorama]`. Esiste un capitolo di spesa, ma è **contrattualizzato con operatori consolidati** (Heliwest, Babcock). Un servizio di *early-detection* persistente potrebbe integrarsi, ma la WTP è per il **spegnimento**, non per l'osservazione (che oggi è a costo quasi zero via avvistamento + Copernicus EFFIS).

### 3.4 Ispezione infrastrutture — chiuso dagli incumbent
- §2 riga 5: Terna in-house + Wesii. Il mercato droni-servizi professionale italiano vale **€160M (2024), 657 imprese**, di cui il **96% operazioni aeree tradizionali** (rilievi 67%, riprese 64%, ispezioni 61%); solo **23 autorizzazioni BVLOS nel 2023** `[fatto; Osservatorio Droni Polimi; confidence: high]`. Firmamento entrerebbe come **una delle 657**, non come categoria nuova. Pricing di riferimento: **€350-3.000 per lavoro**; rilievo 3 ha €345-875 `[fatto; edilnet/archeodigital; confidence: medium]`. Sono ricavi da micro-commessa, non da abbonamento.

---

## 4. Falsificazione: e se il mercato non giustificasse nemmeno €1M?

Questo scenario **non è un'ipotesi remota, è plausibile**. Costruiamolo onestamente.

**Catena di sostituzione che erode la domanda pagante:**
1. **Connettività** → Starlink €40/mese + BUL fibra pubblica. Firmamento non ha un cliente disposto a pagare di più per meno. `[fatto]`
2. **EO ordinario** → Copernicus Sentinel gratis (10 m, revisita 5 gg) + commerciale VHR economico + droni €350/job. `[fatto]`
3. **EO d'emergenza/ispezione** → ARPAL/Terna/VVF hanno flotte proprie; il resto è coperto da 657 operatori droni esistenti. `[fatto]`
4. **Pagatori accessibili** (comuni montani, coop) → **budget discrezionale ≈ €0** (L.bilancio 2025: €5M per *tutti* i mini-comuni montani d'Italia). `[fatto]`
5. **Grant near-term** → il bando Cooding Prototypes dà **max €50k, ≤50% dei costi** `[fatto; cooding.it; confidence: high]`. La benzina iniziale è €50k, non milioni.

**Scenario worst quantificato:** se la Regione non firma una convenzione pluriennale, se ARPAL/utility restano in-house e se i comuni non aggregano domanda, il ricavo ricorrente **commerciale** a 5 anni è **€30-70k**, con ricavo totale (incl. code di grant) **€80-150k**. A quel punto un investimento >€0,3M **distrugge valore**: si costruisce capacità per un mercato che non stacca assegni. Questo scenario ha, a mio giudizio, **probabilità 30-40%** — non è la coda, è un esito centrale plausibile. È coerente con la base-rate delle startup aerospace (10-20% arrivano a revenue operativa).

**Falsifying observation esplicita:** se entro M+24 Firmamento non ha **≥€150k di ricavi ricorrenti da contratti firmati non-grant** (o ≥1 convenzione regionale pluriennale ≥€100k/anno), lo scenario base è falsificato e va derubricato al worst; l'investimento in qualsiasi piattaforma dedicata va congelato.

---

## 5. Costruzione bottom-up del SOM (somma dei pagatori, non % di un TAM)

Non stimo il SOM come "5% del SAM". Lo **sommo dai pagatori** del §2, con tasso di cattura per scenario.

| Fonte di ricavo | Worst | Base | Best | Note |
|---|---|---|---|---|
| Convenzione Regione Liguria (EO territorio, grant-anchored) | €0 | €80-150k | €300-500k | richiede LoI + bando vinto |
| Protezione Civile / AIB early-warning pilota | €0 | €30-60k | €100-200k | integrazione, non sostituzione |
| Unioni di Comuni / SNAI (bundle EO+dati) | €20-40k | €40-90k | €120-250k | aggregazione domanda |
| Enti Parco / ARPA progetti | €10-20k | €20-50k | €60-120k | a progetto |
| Utility niche subcontract | €0 | €0-30k | €80-200k | bassa prob. anche in best |
| Coop agri/forestali (NDVI, telemetria) | €10-20k | €20-40k | €60-120k | micro-commesse |
| 10 coop di comunità (bundle dati/conness.) | €30-50k | €40-80k | €80-150k | grant-dipendente |
| Telco wholesale NTN | €0 | €0 | €0-100k | solo se Rel.18/19 accelera |
| **TOTALE ricavo annuo Y5 (grant+comm.)** | **€80-150k** | **€250-500k** | **€0,9-1,8M** | |
| **di cui ricorrente commerciale non-grant** | €30-70k | €120-280k | €0,4-0,9M | metrica di sopravvivenza |

**Assunzioni dichiarate:**
- Ogni riga è capped dal budget reale del §2, non da un CAGR.
- Il *best* assume: LoI Regione convertita in convenzione, scale-up a 2-3 aree SNAI extra-Liguria, 1 slot utility, pilota HAPS/NTN grant-finanziato. È ottimistico ma non impossibile; resta **sotto** il €3-8M del cap-07.
- Erogazione via **piattaforma commerciale VTOL/drone** (TRL 8-9), non HALE: il mercato non paga il layer stratosferico di più.
- Traiettoria coerente col BP interno (Y3 €157k) collocandolo tra worst e base.

**Cross-check di sanità:** €250-500k Y5 base ÷ ~€10-30k ACV medio ⇒ **15-40 contratti attivi**. Plausibile per una cooperativa radicata in Liguria con rete Legacoop. €3-8M (cap-07) richiederebbe 150-400 contratti o poche mega-commesse utility/telco: **non supportato** dai budget del §2.

---

## 6. Il tetto d'investimento derivato dal mercato

Il punto vero del mandato. Quanto è **razionale investire**, dato che il mercato è quello del §5?

**Logica.** Il tetto d'investimento *puramente commerciale* è il valore attuale dei margini che il servizio può generare. Base case: ricavo ~€300-500k con margine EBITDA realistico 20-30% ⇒ cash flow **€60-150k/anno**; NPV su 7 anni @ WACC 12% ⇒ **~€0,4-0,8M**. Il tetto *puramente commerciale* è quindi **sotto €1M**.

| Voce di investimento | Costo tipico | Giustificato dal mercato Aree Interne? |
|---|---|---|
| **Studio di fattibilità** | €100k (di cui €50k grant Cooding) | **Sì** — riduce incertezza, costo basso `[fatto; bando]` |
| **Pilota VTOL/drone (Percorso 6A)** | €600-900k | **Solo se ≥70-80% grant** (PNRR/FESR/EDF) e se conta l'opzione strategica | 
| **HALE dedicato (Percorso 6B)** | €5,5-11M R&D | **No.** Il mercato-servizio non lo ripaga di 1-2 ordini di grandezza |

**Conclusione sul tetto.** Se si conta **solo** il ritorno commerciale del mercato Aree Interne: **investimento razionale ≤ €0,3-0,8M**, quasi tutto in forma non-dilutiva (grant). Un impegno fino a **~€1-1,2M** è difendibile *solo* aggiungendo: (a) prevalenza di denaro grant non-dilutivo (SNAI/FESR/Coopfond/PNRR), e (b) **valore-opzione strategico** (posizionamento verso futura infrastruttura HAPS EU) contabilizzato a parte, come R&D di opzione, **non** come VAN di mercato. Qualunque cifra oltre ~€2-3M non trova copertura nel mercato indirizzabile qui analizzato e va giustificata su basi extra-mercato (industriale/sovranità), con l'onere della prova a chi la propone.

---

## 7. Verdetto sul segmento pagante più solido

Ranking dei segmenti per **solidità del pagatore** (esiste il budget? è accessibile? c'è WTP? regge la sostituzione?):

1. **🥇 B2G territorio — EO monitoraggio grant-anchored (Regione + Unioni SNAI + Enti Parco).** È "solido" non per grande WTP, ma perché **allineato a fondi che esistono e a una missione pubblica** (dissesto, AIB, spopolamento), con Firmamento come operatore cooperativo credibile. Rischio: è **grant-dipendente**, quindi ciclico e a lead-time lungo. Metrica di verità: **LoI Regione + convenzione pluriennale entro M+12**.
2. **🥈 B2B rete cooperativa (le 10 coop + agri/forestale).** Solido come *canale di aggregazione e legittimazione*, debole come *cassa* (micro-budget, sovvenzionato). Utile per volume-community e per de-risk del bando, non per ARR.
3. **🥉 B2G emergenza (Protezione Civile/AIB).** Budget reale ma presidiato da incumbent; ingresso solo come integrazione early-detection, non sostituzione.
4. **❌ Utility (Terna/Enel):** porta chiusa (in-house + Wesii). Non inseguire near-term.
5. **❌ Connettività retail / telco wholesale:** uccisa da Starlink/BUL (retail) e prematura (wholesale NTN). **Non** costruire la value proposition sulla connettività.

**Raccomandazione operativa:** posizionare Firmamento come **operatore cooperativo di dati EO per la PA delle Aree Interne, finanziato da fondi di coesione**, erogando con **piattaforma commerciale** (VTOL/drone) nel Percorso 6A. Trattare l'HALE come opzione strategica di lungo periodo, **non** come investimento ripagato da questo mercato. Il tetto prudente d'investimento pre-ricavi è **~€0,8-1,2M, in prevalenza grant**.

---

## 8. Confidenza, limiti e falsificazioni

- **Fatti (confidence high):** budget FESR/SNAI, Terna in-house, Starlink pricing, mercato droni €160M, Cooding €50k, digital divide Antola. Fonti terze verificabili.
- **Stime (confidence low-medium):** tassi di cattura per segmento, SOM worst/base/best, tetto d'investimento. Sono giudizi dell'analista, dichiarati come tali.
- **Non triangolato / da validare sul campo:** WTP *reale* firmata (serve ≥3 LoI); esistenza di una linea FESR/SNAI Liguria specificamente aggredibile per EO-servizio; disponibilità Unioni ad aggregare domanda.
- **Falsifying observations:**
  - Se M+24 senza **≥€150k ricorrente non-grant** o convenzione regionale ≥€100k/anno ⇒ scenario base falsificato.
  - Se Cooding/FESR non finanziano il pilota ≥50% ⇒ tetto d'investimento crolla a ~€0,3M.
  - Se ARPAL/utility confermano piena internalizzazione ⇒ EO-ispezione esce dal SOM.

---

## Fonti principali

**Repository (fatti locali):**
- `Aree interne/rapporto-istruttoria_regione-liguria.md` — aree SNAI Liguria, OpenCoesione €74M, BUL €43,1M.
- `Aree interne/Dossier SNAI.md` — Antola-Tigullio, Torriglia, digital divide d.1-d.6.
- `bando/Business Plan.docx (1).md` — proiezione ricavi Y1-Y3 (€0/€61k/€157k), 10-20 contratti.
- `bando/Elenco Cooperative.md` — le 10 coop (Val Pentemina, Fabrica capofila, Monte di Capenardo…).
- `studio-di-fattibilita/cap-07-mercato-e-business-case.md` — stime top-down criticate (SOM Y3 €1,5-3,5M).

**Web (fatti esterni):**
- SNAI risorse per area / 124 aree — politichecoesione.governo.it; camera.it (temi.camera.it/leg19).
- FESR Liguria €630M / digitale €10M — regione.liguria.it (via ricerca).
- Dissesto ReNDiS €19,2mld/25 anni, ~€280-329M/anno — ISPRA; osservatoriocpi.unicatt.it; greenreport.it.
- AIB Liguria €248,5k / Canadair €59M — regione.liguria.it; panorama.it.
- ARPAL team droni interno — snpambiente.it/arpal.liguria.it.
- Mercato droni €160M 2024, 657 imprese, 23 BVLOS — osservatori.net (Polimi); innovationpost.it; ilsole24ore.com.
- Prezzi rilievo drone €350-3.000 — edilnet.it; archeodigital.it.
- Starlink €29-40/mese — corrierecomunicazioni.it; sostariffe.it.
- Terna €50M/anno, 34 droni+7 elicotteri, Wesii €2,8M — industriaitaliana.it; quadricottero.com.
- Cooding Prototypes max €50k, ≤50% — cooding.it/prototypes; coopfond.it; ilmessaggero.it.
