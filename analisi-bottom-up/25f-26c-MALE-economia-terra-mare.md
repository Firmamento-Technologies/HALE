# 25f/26c — T-SORV (fixed-wing endurance sorveglianza): economia dei due business case TERRA e MARE

> **Progetto HALE — Firmamento Technologies · Analisi economico-finanziaria critica**
> **Autore:** Financial Analyst / Fractional CFO · **Data:** 2026-07-13
> **Piattaforma oggetto:** **T-SORV** — UAV ad ala fissa, endurance **10-20 h**, apertura **>10 m**, MTOM **100-250 kg**, lancio a **catapulta/traino** (no VTOL), recupero a rete/skyhook o pista corta, certificazione ENAC **Specific (SAIL alto) / Certified**. Payload di sorveglianza EO/IR ± SAR/AIS.
> **Mandato:** costruire l'analisi economica di **due business case separati** — **(A)** sorveglianza terrestre delle Aree Interne liguri, **(B)** sorveglianza marittima costiera — mantenendo i capisaldi di progetto: Firmamento **operatore di servizi, non OEM** (`CLAUDE.md`); tetto finanziabile all'ingresso **~€1M** (`06`, `R5`); nicchia MALE/ISR presidiata da giganti (`R2`).
> **Metodo:** riuso della metodologia TCO 5 anni + NPV/IRR/payback + scenari worst/base/best + sensitivity già in uso nel repo (`19-BOXTILT-economia-fattibilita.md`, `23-economia-integrata-capitale.md`). WACC **nominale, post-imposte, blended = 12%** (sensibilità 10%/15%).
> **Confidenza aggregata: MEDIO-BASSA.** Alta sui benchmark di costo/finanziamento/regolatori ereditati (già triangolati in `10`/`16`/`06`/`R5`); bassa sui ricavi di servizio (nessun capitolato firmato). **Nessuna cifra è una quotation vendor reale né un ricavo contrattualizzato.**

---

## 0. Regola di lettura e collocazione della piattaforma nelle fasce

**[FATTO]** = dato da fonte ufficiale / benchmark verificato nei report a monte. **[STIMA]** = elaborazione del CFO, confidenza dichiarata inline (high/medium/low). Scale sempre esplicite (**€k** vs **€M**). Tassi sempre dichiarati.

**Dove si colloca T-SORV nella famiglia T0-T4 (`10-fasce-engineering.md`).** Le specifiche del mandato (ala fissa, 100-250 kg, apertura >10 m, endurance 10-20 h, lancio a catapulta) collocano T-SORV **a cavallo tra il tetto di T2 e il fondo di T3a** ("MALE tattico piccolo", 150-220 kg, apertura 8-13 m, endurance 12-20 h, ICE heavy-fuel, lancio catapulta — archetipo **Tekever AR5 / Insitu Integrator / Schiebel S-100** in `16` §2.1). **[FATTO, confidence high]**

Due precisazioni dirimenti, entrambe con conseguenze economiche di primo ordine:

1. **T-SORV NON è VTOL.** Il lancio a catapulta/traino elimina il gruppo di sostentamento verticale: è una scelta **economicamente favorevole** (nessuna penalità hover −15/30% di massa-potenza, `16` §2.2) ma **impone un sito attrezzato** (catapulta + area di recupero) — vincolo forte in orografia appenninica (valli strette, cfr. Pentema in `13`). Si compra endurance a prezzo di infrastruttura di lancio. **[FATTO]**

2. **MTOM 100-250 kg attraversa lo spartiacque regolatorio dei 150 kg.** Sotto i 150 kg si resta in **Specific Category** (SAIL IV-VI, mitigabile con Design Verification Report, ~€250/h EASA ≈ €45k/anno di engagement, `16` §2.7 **[FATTO]**). Sopra i 150 kg si scivola verso la **Certified Category**, per la quale **nessun UAS ha mai ottenuto un Type Certificate EASA pieno** (luglio 2026) → costo certificazione €5-15M+, 5-8 anni, nessun precedente italiano (`16` §2.7 **[FATTO]**). **Questo non è un dettaglio: è la variabile che, da sola, può spostare il CapEx di un ordine di grandezza e va risolta PRIMA di qualsiasi impegno.** Raccomandazione trasversale: **dimensionare T-SORV a MTOM ≤150 kg** salvo che un requisito di payload/endurance inderogabile giustifichi il salto in Certified (e il suo costo).

> **Impostazione del capitolo.** Per coerenza con il verdetto Buy-vs-Build già consolidato (`10` §4.3, `19` §5, `23` §7) valuto **due strade di CapEx**: **(a) acquisto/adattamento COTS** (comprare una piattaforma ala-fissa endurance civile-adjacente esistente e operarla) e **(b) sviluppo semi-custom** (airframe nuovo o profondamente adattato). Anticipo il metodo del verdetto: la strada COTS domina, e la domanda decisiva non è "quanto costa" ma **"esiste un anchor pubblico pluriennale che copre gli OpEx prima di impegnare il CapEx?"** — perché questa fascia di piattaforma è, per benchmark (EMSA €7,5-15M/anno, `16` §2.6), **strutturalmente OpEx-intensiva e non si autofinanzia dal mercato**.

---

# PARTE A — Business case TERRESTRE (sorveglianza Aree Interne liguri)

## A.1 CapEx per 1 unità T-SORV

### A.1.a Strada COTS/adattamento (raccomandata)

**Esiste una piattaforma civile europea simile?** Parzialmente. La fascia ala-fissa 100-250 kg endurance con catapulta è **presidiata da prodotti militari/dual-use** (Tekever AR5, Insitu Integrator/RQ-21, Schiebel S-100 rotary) più che da COTS civili puri: è un **gap di mercato civile** (`R2` §B punto 4: ISR/EO-persistenza sovrana presidiata da Quantum/Tekever/JOUAV). Di conseguenza "COTS" qui significa **acquistare una piattaforma dual-use e adattarla al ConOps civile**, non prendere un prodotto civile a catalogo. Bracket di costo per **sistema completo, 1 unità** [STIMA, confidence medium, ancorata a `10` §5.1 bracket T3a €2-5M e a `16` §2.1]:

| Voce CapEx (sistema, 1 unità) | Range €k | Assunzione / fonte | Confidence |
|---|---|---|---|
| Airframe ala-fissa 100-150 kg + integrazione | 700-1.600 | fondo fascia T3a (`10` §5.1: €2-5M/unità *fully equipped* militare-grade → si scende al fondo perché sorveglianza "semplice" civile, non SIGINT/SAR pieno) | medium |
| Payload EO/IR gimbal MWIR (giorno/notte, 30× zoom) | 150-350 | payload maturo COTS (`16` §2.4) | medium |
| Catapulta di lancio + sistema di recupero (rete/skyhook) | 100-300 | analogia RQ-21 launch/recovery (`10` §4.1) | low-medium |
| Ground Control Station (fissa Pentema + mobile) | 150-350 | analogia `cap-08`/`19` ground segment | medium |
| Hangar/sito attrezzato + infrastruttura di terra | 50-200 | affitto/costruzione lieve, area interna | low-medium |
| Certificazione SORA/Specific + DPIA privacy + training + ricambi iniziali | 150-400 | `16` §2.7 (DVR ~€45k/anno) + formazione + spare | medium |
| **Totale CapEx sistema COTS-adattato (1 unità)** | **1.250-3.200** | base **~€1,8M** | **medium** |

**Osservazione dirimente [FATTO]:** già la sola strada COTS, base ~€1,8M, **eccede il tetto finanziabile "comodo" ~€1M** (`06` §6) e sfiora il CapEx Y1 realistico del Percorso 6A "sliding" (€2,5-3,5M, `05` §4). Con MTOM >150 kg (Certified) si aggiungono €5-15M di certificazione: la voce salta fuori scala.

### A.1.b Strada semi-custom (sconsigliata come asset di servizio)

Sviluppo di un airframe nuovo/profondamente adattato: **€3-10M+ solo di sviluppo** verso un prodotto certificato/serie (`10` §3 e §5.2 **[FATTO bracket]**), 24-48 mesi, TRL 3-5 di partenza. Per la **stessa logica economica del verdetto BOXTILT** (`19` §5): su un mercato pagante <€1M/anno, €3-10M di sviluppo espensato **non rientra su nessun orizzonte ragionevole** ed è incompatibile col tetto finanziabile. **La strada semi-custom ha senso solo come linea R&D/IP finanziata ≥70% da grant a fondo perduto** (dimostratore/vetrina, non asset di servizio autofinanziato). Nel resto della Parte A si usa la strada **COTS-adattata**.

## A.2 OpEx annuo per erogare il servizio (1 piattaforma, servizio persistente)

Benchmark di ancoraggio [FATTO]: OpEx/h fascia T3 = **€800-3.000/h** (`10` §5); OpEx flotta T2 = **€0,32M/pf/anno** (`23` §2.1). Per T-SORV ala-fissa ICE heavy-fuel, servizio persistente **single-platform**, ~300-450 h volo/anno:

| Voce OpEx | Range €k/anno | Assunzione | Confidence |
|---|---|---|---|
| Personale operativo (2-3 FTE: pilota remoto + operatore + analyst pro-quota) | 120-200 | servizio persistente richiede turnazione | medium |
| Manutenzione airframe + motore ICE heavy-fuel (8-12% CapEx rilevante) | 100-250 | motore a combustione = manut. maggiore vs elettrico | medium |
| Assicurazione aviation BVLOS (RC + casco) | 40-100 | RC BVLOS su area montana abitata | low-medium |
| Sito di lancio + hangar + utilities | 25-60 | area interna Pentema/Torriglia | low-medium |
| Ground segment / connettività / canoni SW (GIS, processing, anonimizzazione) | 25-60 | | medium |
| Carburante / energia | 10-30 | heavy-fuel | medium |
| Compliance ricorrente (rinnovo SORA, DVR EASA, registri privacy) | 20-80 | DVR ~€45k/anno se Certified-adjacent (`16` §2.7) | medium |
| **Totale OpEx/anno (1 piattaforma)** | **340-780** | base **~€0,6M/anno** | **medium** |

**Lettura [STIMA, confidence medium].** L'OpEx base ~€0,6M/anno è **coerente per scala** con il benchmark EMSA riparametrato: EMSA = €7,5-15M/anno per **4 velivoli + equipaggio + operazioni multi-sito** (`16` §2.6) ≈ **€1,9-3,75M per velivolo-anno** *all-in con ridondanza e multi-sito*. Un servizio ligure **single-platform, mono-regione, con quota stagionale** (l'antincendio boschivo è concentrato in estate) sta correttamente **al di sotto** del per-velivolo EMSA (meno turni H24, meno ridondanza, meno siti). Se il servizio fosse H24 tutto l'anno con ridondanza, l'OpEx salirebbe verso €0,9-1,2M/anno (scenario worst).

## A.3 Chi paga — domanda pagante terrestre

| Cliente / capitolo di spesa | Missione | Base giuridica / capitolo | Confidence sull'esistenza del capitolo |
|---|---|---|---|
| **Regione Liguria — Protezione Civile / AIB** (antincendio boschivo) | sorveglianza e allerta incendi boschivi, loiter su evento | **L. 353/2000** (legge quadro incendi boschivi) impone alle Regioni un **Piano AIB** con risorse dedicate; Liguria ha Piano AIB regionale | medium (esistenza capitolo AIB regionale) / low (importo spendibile su UAV) |
| **Consorzi Forestali / Comunità montane** | monitoraggio patrimonio boschivo, tagli abusivi | fondi forestazione regionali/PSR | low-medium |
| **ANAS / Città Metropolitana di Genova** | monitoraggio viabilità, frane su strade | manutenzione infrastrutture viarie | low-medium |
| **PNRR M2C4 / FESR dissesto idrogeologico** | monitoraggio versanti, frane, rischio idrogeologico | PNRR Missione 2 Componente 4 (dissesto idrogeologico ~€2,49 mld nazionali) + FESR Liguria | medium (fondo esiste) / low (accesso diretto coop) |
| **Protezione Civile regionale — emergenze** | ripresa on-event (alluvioni, frane) | fondo emergenze regionale | low-medium |

**Prezzo di servizio plausibile [STIMA, confidence low].** Per analogia con i benchmark T3/EMSA **scalati alla realtà ligure** (molto più piccola): un contratto-quadro di sorveglianza regionale plurimissione (AIB estivo + frane/viabilità nelle mezze stagioni) è collocabile in **€0,3-0,8M/anno** come **anchor**, integrabile con committenze accessorie (forestali, ANAS) per **+€0,1-0,2M/anno**. In €/ora di volo, a 300-450 h/anno, ciò corrisponde a **€900-2.400/h** — dentro il bracket OpEx/h T3 (€800-3.000/h, `10` §5), cioè **prezzo che copre l'OpEx ma lascia margine sottile o nullo sul CapEx**. Questo è il punto: il modello è **servizio pubblico a copertura costi (mini-EMSA regionale)**, non un business a ritorno di mercato.

## A.4 TCO 5 anni + NPV/IRR/payback — scenari worst/base/best

**Impostazione DCF.** Vista di progetto (asset), WACC 12%, orizzonte Y0-Y5. CapEx a Y0. Ricavi in rampa (utilization che sale). Scenari:

| Parametro | **WORST** | **BASE** | **BEST** |
|---|---|---|---|
| CapEx sistema (Y0) | €3,2M (MTOM>150kg, Certified-adjacent) | €1,8M | €1,25M (MTOM≤150kg, lean) |
| OpEx annuo (Y1-5) | €0,85M | €0,60M | €0,45M |
| Ricavo anchor a regime | €0,25M/anno (solo Pentema-scale, no anchor regionale) | €0,60M/anno (anchor AIB + accessori) | €0,90M/anno (multi-cliente + co-fin. PNRR dissesto) |
| Rampa ricavo | 0,10 / 0,15 / 0,20 / 0,25 / 0,25 | 0,30 / 0,50 / 0,60 / 0,60 / 0,60 | 0,50 / 0,80 / 0,90 / 0,90 / 0,90 |
| Utilization implicita | <30% | 50-60% | 65-75% |

**TCO 5 anni (CapEx + Σ OpEx 5 anni), €M:**

| | WORST | BASE | BEST |
|---|---|---|---|
| CapEx | 3,20 | 1,80 | 1,25 |
| OpEx × 5 | 4,25 | 3,00 | 2,25 |
| **TCO 5y** | **~€7,45M** | **~€4,80M** | **~€3,50M** |

**NPV / IRR / payback (vista progetto, WACC 12%), €M:**

| KPI | WORST | BASE | BEST |
|---|---|---|---|
| Flusso netto operativo cumulato 5y (ricavo − OpEx) | −3,20 | −0,55 | +1,60 |
| **NPV@12% (progetto, pre-grant)** | **−€5,4M** | **−€2,3M** | **+€0,1M** |
| IRR | n.d. (negativo) | n.d. (negativo) | ~12-13% |
| Payback (semplice) | mai | mai (senza grant su CapEx) | ~Y5-6 |
| Picco cassa | −€6,5M | −€2,9M | −€1,6M |

**Sensitivity (NPV base ≈ −€2,3M, un driver alla volta) [STIMA]:**

| Driver | Δ NPV | Sensibilità |
|---|---|---|
| **Ricavo/anchor** (±25%) | ±€0,9M | 🔴 alta |
| **CapEx** (€1,25M ↔ €3,2M) | ∓€1,95M | 🔴 massima |
| **Utilization / tasso occupazione** (30%↔75%) | ±€1,1M | 🔴 alta |
| **OpEx** (±25%) | ∓€1,0M | 🔴 alta |
| **WACC** (10%↔15%) | ±€0,3M | 🟡 media |

> **La domanda decisiva del mandato — risposta netta [STIMA, confidence medium-high].** **T-SORV terrestre NON è finanziabile da Firmamento standalone entro il tetto ~€1M.** Due ragioni cumulative e indipendenti: (1) il **solo CapEx** (base €1,8M) eccede già il tetto ~€1M; (2) l'**NPV di progetto è negativo in worst e base** e break-even solo in best, e **anche in best il ritorno è marginale** (IRR ~12-13%, appena sopra il WACC) e condizionato a multi-cliente + utilization >65% + CapEx coperto da grant. **La piattaforma richiede necessariamente un anchor pubblico pluriennale (mini-EMSA regionale) che copra gli OpEx PRIMA di ogni impegno di CapEx**, esattamente come il benchmark EMSA-Tekever (`16` §2.6: "serve l'anchor prima dell'asset, non dopo"). Senza contratto firmato che copra ≥ l'OpEx (~€0,6M/anno), ogni euro di CapEx è capitale a rischio non recuperabile.

> **Falsifying observation A [FATTO negativo al 2026]:** *nessuna PA ligure ha firmato un contratto di servizio di sorveglianza pluriennale.* Finché questo resta vero, T-SORV terrestre **non è attivabile** — non c'è business case standalone (coerente con `16` §6 osservazione 1).

## A.5 Confronto e sequenza con il Percorso 6A (T2 VTOL COTS)

Il Percorso 6A raccomandato nello Studio (`10` §4, `05` §11) è un **VTOL COTS classe JOUAV CW-30E** (T2, 38 kg, 6-10 h, TRL 9), CapEx sistema **€0,58-0,82M/unità** (`10` §4.1 **[FATTO]**), dentro/vicino al tetto €1M.

| Dimensione | **6A — T2 VTOL COTS** | **T-SORV — ala fissa endurance** |
|---|---|---|
| CapEx sistema (1 unità) | €0,58-0,82M | **€1,25-3,2M** (2-4× superiore) |
| Endurance | 6-10 h | 10-20 h |
| Area coperta per sortita | media (VTOL, raggio ridotto) | **ampia (endurance lunga, loiter)** |
| Infrastruttura di lancio | nessuna (VTOL, spazi ridotti Pentema) | **catapulta + sito attrezzato (vincolo orografico)** |
| TRL / rischio | 9 / basso | 8-9 (COTS) / **medio** (adattamento, cert. SAIL alto) |
| Tetto finanziabile ~€1M | ✅ dentro | 🔴 **fuori** senza anchor |
| Nodo regolatorio | SAIL II-III (mappato) | **SAIL IV-VI / Certified se >150 kg (non risolto)** |

**Complementari o in competizione di budget? Entrambe le cose.** Sul piano della **missione** sono **complementari**: 6A (VTOL, spazi ridotti, missione locale/on-event) e T-SORV (ala fissa, area vasta, endurance lunga, loiter persistente) coprono esigenze diverse. Ma sul piano del **capitale**, con un tetto finanziabile ~€1M e un floor equity coop €20-100k (`06` §3), **sono in diretta competizione di budget**: un solo T-SORV assorbe da solo l'intero tetto e oltre, precludendo il 6A.

> **Sequenza raccomandata [STIMA, confidence medium-high].** **6A prima, T-SORV dopo e solo condizionatamente.** (1) **Y1-Y2: Percorso 6A VTOL COTS** — dentro il tetto, TRL 9, genera il **track-record operativo, il dato e le relazioni PA** che sono l'unico moat di un operatore di servizi (`CLAUDE.md`). (2) **Il pilota 6A è lo strumento commerciale per conquistare l'anchor**: si usano i risultati Pentema per negoziare con Regione Liguria/Protezione Civile un **contratto-quadro di sorveglianza pluriennale**. (3) **Solo a valle di un anchor firmato che copra gli OpEx** si attiva T-SORV (Y2-Y3+) per la sorveglianza di **area vasta** che il VTOL non fa. T-SORV **non è un investimento parallelo Y1**: è un'estensione **anchor-gated** del servizio dopo che il 6A ha dimostrato valore. Coerente con la gate-logic di `16` §5 (T3a attivabile Y3-Y4 "solo con anchor PA/agenzia firmato che copre OpEx").

---

# PARTE B — Business case MARITTIMO (sorveglianza costiera)

## B.1 CapEx incrementale della variante marittima (delta su airframe condiviso)

**Impostazione [FATTO metodologico].** Se l'airframe T-SORV è **condiviso** con la variante terrestre e il payload è **intercambiabile** (il livello di modularità più solido e difendibile, `10` §7.3), il costo della variante marittima è un **delta di payload + hardening**, non un secondo CapEx completo. Stimo il **delta** [STIMA, confidence medium-low]:

| Voce delta marittima | Range €k | Assunzione / fonte | Confidence |
|---|---|---|---|
| Ricevitore **AIS** (correlazione tracce navali) | 20-60 | payload maturo (`16` §2.4, "AIS receiver EMSA-like") | medium |
| **Radar** di sorveglianza marittima (surface-search / SAR leggero-GMTI) | 150-500 | il delta dominante; radar navale-grade è costoso (`16` §2.4) | low-medium |
| EO/IR marittimo long-range + hardening anti-salino | 50-150 | ottica marinizzata, portata su specchio d'acqua | low-medium |
| **SATCOM BLOS** (BVLOS su mare = no LOS costiero continuo) | 50-150 | link satellitare obbligatorio over-sea (`avionics-gnc` framework) | medium |
| Hardening anticorrosione airframe/celle (ambiente salino) | 30-100 | trattamento superfici, guarnizioni | low |
| **Totale delta CapEx marittimo (su airframe condiviso)** | **300-960** | base **~€0,55M** | **medium-low** |

**CapEx sistema marittimo standalone** (se NON si condivide l'airframe) = CapEx terrestre + delta = **€2,1-4,1M** (base ~€2,35M). **CapEx incrementale su T-SORV già posseduto** = solo il delta **€0,3-0,96M**. La differenza è la misura della sinergia (§B.4).

**Nota "controllo fondali" [STIMA, confidence medium — da confermare col collega EO].** Il monitoraggio batimetrico/fondali da ala fissa a quota, su **acque costiere liguri torbide del Mediterraneo**, ha penetrazione ottica di pochi metri e resa marginale: il collega Earth-Observation ne ha valutato la fattibilità tecnica. **Se risulta non fattibile, NON va costato come flusso di ricavo** — e in questa analisi **non lo è**: nessun ricavo "fondali" è incluso. Il valore marittimo è AIS/radar/EO di superficie (traffico, SAR, inquinamento, immigrazione), non batimetria.

## B.2 Chi paga — domanda pagante marittima

| Cliente / capitolo di spesa | Missione | Precedente / nota | Confidence |
|---|---|---|---|
| **Guardia Costiera / Capitaneria di Porto** | SAR, controllo traffico, sorveglianza AMP | committente naturale RPAS-as-a-Service | medium |
| **Agenzia Dogane e Monopoli** | controllo traffico commerciale, contrabbando | controllo doganale marittimo | low-medium |
| **Regione Liguria — turismo / Aree Marine Protette** | vigilanza AMP (Portofino, Cinque Terre), balneazione | fondi regionali ambiente/turismo | low-medium |
| **EU — Frontex** (sorveglianza costiera) | sorveglianza frontiere marittime | **Frontex Aerial Surveillance Service (FASS)**: Frontex contrattualizza servizi di sorveglianza aerea con operatori terzi — **precedente rilevante e diretto** | medium |
| **EU — EMSA** (RPAS service) | monitoraggio inquinamento, traffico, pesca | **il precedente letterale del repo**: EMSA-Tekever, €30M/2-4 anni, €7,5-15M/anno (`16` §2.6) | high (esistenza del modello) |

**Il comparabile naturale [FATTO].** Il modello di ricavo marittimo **non è un mercato aperto**: è un **contratto-quadro pluriennale di agenzia** (Guardia Costiera / EMSA / Frontex), esattamente il caso EMSA-Tekever già nel repo. EMSA/Frontex operano in **regime di agenzia** (fuori Reg. 947 civile puro, `16` §2.7), il che **mitiga parte del nodo regolatorio Certified** — un vantaggio non trascurabile della variante marittima rispetto alla terrestre BVLOS su area abitata.

## B.3 TCO 5 anni + NPV — scenario marittimo

**Assunzioni [STIMA].** Poiché il valore marittimo emerge solo con un contratto di agenzia, modello il caso **marittimo come sistema dedicato** (airframe + payload marittimo) e, separatamente, l'**incremento su airframe condiviso** (§B.4). OpEx marittimo **superiore** al terrestre (BVLOS over-sea, SATCOM, manutenzione anticorrosione, turni SAR): base **~€0,75M/anno** (worst €1,0M, best €0,55M).

| Parametro | **WORST** | **BASE** | **BEST** |
|---|---|---|---|
| CapEx sistema marittimo (standalone) | €4,1M | €2,35M | €1,55M |
| OpEx annuo | €1,00M | €0,75M | €0,55M |
| Ricavo anchor (agenzia) a regime | €0,30M/anno | €0,70M/anno | €1,20M/anno |
| Rampa ricavo | 0,10/0,20/0,25/0,30/0,30 | 0,30/0,55/0,70/0,70/0,70 | 0,60/1,00/1,20/1,20/1,20 |

**TCO 5 anni (€M):** WORST **~€9,1M** · BASE **~€6,1M** · BEST **~€4,3M**.

**NPV / IRR / payback (vista progetto, WACC 12%, €M):**

| KPI | WORST | BASE | BEST |
|---|---|---|---|
| **NPV@12% (progetto, pre-grant)** | **−€6,8M** | **−€3,1M** | **+€0,3M** |
| IRR | n.d. (negativo) | n.d. (negativo) | ~13-14% |
| Payback | mai | mai (senza grant) | ~Y5 |

> **Finanziabile standalone o anchor-dipendente? [STIMA, confidence medium-high].** La variante marittima è **ancora più anchor-dipendente della terrestre**: CapEx più alto (radar + SATCOM), OpEx più alto (over-sea, SAR), e il cliente **è già strutturalmente un contratto pluriennale di agenzia** (Guardia Costiera / EMSA / Frontex). **NPV negativo in worst e base**, break-even marginale solo in best con anchor ≥€1,2M/anno. **Non finanziabile standalone entro ~€1M**; il comparabile naturale è un contratto EMSA/Frontex-style — che nel repo è già benchmark a **€7,5-15M/anno** per un lotto pieno (`16` §2.6). La buona notizia relativa: il regime di agenzia EMSA/Frontex **attenua il nodo Certified** che invece grava sulla variante terrestre BVLOS su area abitata.

## B.4 Sinergia terra/mare — quanto si risparmia con airframe condiviso

**Il livello di modularità che vale [FATTO, `10` §7.3].** La variante marittima è un **payload swap sullo stesso airframe T-SORV** (EO/IR terrestre ↔ AIS+radar+EO marittimo): è **modularità intra-fascia, stesso airframe, payload intercambiabile** — il livello più solido e difendibile della famiglia (contro l'illusione dell'"airframe morphabile" tra fasce, fisicamente impossibile, `10` §7.1).

**Quantificazione del risparmio [STIMA, confidence medium]:**

| Voce | Due piattaforme separate | Airframe condiviso + payload swap | Risparmio |
|---|---|---|---|
| Airframe + integrazione (×2 vs ×1) | €1,4-3,2M (2 airframe) | €0,7-1,6M (1 airframe) | **€0,7-1,6M** |
| Certificazione (SORA/DVR ×2 vs ×1 famiglia) | €0,3-0,8M | €0,15-0,4M | **€0,15-0,4M** |
| GCS + training + ricambi comuni | ×2 parziale | condivisi | **€0,2-0,5M** |
| Payload marittimo (delta) | incluso | €0,3-0,96M | (delta necessario in entrambi) |
| **Risparmio CapEx totale da condivisione** | | | **~€1,05-2,5M** |
| Risparmio OpEx (crew/GCS/hangar/spares comuni) | | | **~€0,2-0,4M/anno** |

**Caveat di concorrenza operativa [FATTO logico].** Un airframe condiviso **non può essere in due posti nello stesso momento**: se terra e mare richiedono **persistenza simultanea**, servono comunque **2 velivoli**. In quel caso la sinergia **non è dimezzare la flotta**, ma condividere **design, certificazione di famiglia, GCS, equipaggio, ricambi e vano payload standardizzato** — un risparmio di **~€0,8-1,5M sul programma** (sviluppo/cert. unico + logistica comune), non dell'intero secondo airframe. La sinergia piena (1 airframe, 2 missioni) vale solo se le due missioni sono **temporalmente sfasate** (es. AIB terrestre estivo ↔ sorveglianza costiera turistica estiva — **purtroppo sovrapposte in estate**: da verificare, il conflitto stagionale erode la sinergia proprio nel picco).

> **Verdetto sinergia [STIMA, confidence medium].** L'airframe condiviso con payload intercambiabile è **la scelta economicamente corretta** e vale **€1-2,5M di CapEx risparmiato + €0,2-0,4M/anno di OpEx** rispetto a due piattaforme separate. Ma **non trasforma il verdetto di finanziabilità**: due servizi anchor-dipendenti che condividono un airframe restano **due servizi anchor-dipendenti**. La sinergia riduce il costo, non rimuove la necessità del contratto pubblico pluriennale.

---

# TRASVERSALE

## T.1 Kill-criteria e falsifying observations economiche

Condizioni sotto le quali **nessuna** delle due varianti è finanziabile senza anchor pubblico pluriennale pregresso (ipotesi attesa — e, come si vedrà, **confermata**):

1. **[Anchor mancante — il killer principale]** Se **nessun contratto pubblico pluriennale** (AIB regionale / Guardia Costiera / EMSA-Frontex) che copra **≥ l'OpEx** (~€0,6M/anno terra, ~€0,75M/anno mare) è **firmato PRIMA** dell'impegno di CapEx, **nessuna delle due varianti è finanziabile**: CapEx €1,25-4,1M + OpEx senza ricavo committed → capitale a rischio non recuperabile, ben oltre il tetto ~€1M. **Al 2026: nessun anchor firmato → entrambe non attivabili.** [FATTO negativo, confidence high]

2. **[Spartiacque 150 kg]** Se il dimensionamento porta MTOM **>150 kg** (Certified Category), il costo di certificazione €5-15M + 5-8 anni + **0 Type Certificate EASA mai emessi** (`16` §2.7) **affonda l'economia standalone a prescindere dal ricavo**. Mitigazione: restare ≤150 kg (Specific SAIL) o operare in **regime di agenzia** (EMSA/Frontex) che aggira il Certified civile. [FATTO, confidence high]

3. **[Semi-custom su mercato sottile]** Se non esiste COTS civile ~questa classe e serve **sviluppo semi-custom** (€3-10M+), su un mercato pagante <€1M/anno **l'NPV non torna su nessun orizzonte** (identico al verdetto BOXTILT, `19` §5). BUILD ammissibile solo come R&D grant-funded ≥70%, mai come asset di servizio. [STIMA, confidence high]

4. **[Contratto < OpEx run-rate]** Se il valore annuo del contratto anchor è **< OpEx** (~€0,6M terra / €0,75M mare), il servizio è **cash-flow negativo ogni anno** → non serve alcun debito contratto per il CapEx → morto su base cassa. [STIMA, confidence high]

5. **[Utilization bassa]** Se il tasso di occupazione (ore fatturate / ore disponibili) è **<50-60%** — tipico aerospace civile 50-70% (`19` warning) — i costi fissi (crew, sito, compliance) non sono coperti e l'NPV peggiora di €1,1M (sensitivity §A.4). Non assumere mai 100% utilization. [STIMA, confidence high]

6. **[Delta marittimo senza anchor di agenzia]** Se il delta radar/SATCOM porta il CapEx marittimo **>€2,5M senza** un anchor Guardia Costiera/EMSA/Frontex firmato, la variante marittima è **morta standalone** (NPV base −€3,1M). [STIMA, confidence medium-high]

7. **[Fondali non fattibili]** Se il monitoraggio fondali/batimetria risulta **tecnicamente non fattibile** (acque torbide liguri — valutazione EO), quel ricavo è **zero** e **non va costato**: in questa analisi è già escluso. Contarlo sarebbe sovrastima. [STIMA, confidence medium — da confermare EO]

**Verifica dell'ipotesi attesa.** L'ipotesi del mandato — *"questa fascia di piattaforma è strutturalmente OpEx-intensiva e non si autofinanzia senza contratto firmato"* — **si conferma per entrambe le varianti**. NPV di progetto negativo in worst e base per terra e mare; break-even solo in best e solo con anchor pluriennale + utilization alta + CapEx coperto da grant. È lo stesso risultato del benchmark EMSA/T3 (`16` §2.6) e coerente con il verdetto generale del repo: **nel modello-servizio la fascia MALE/ISR non si autofinanzia dal mercato civile — serve l'anchor prima dell'asset.**

## Riga di fondo

> **T-SORV** (ala fissa, 100-250 kg, endurance 10-20 h, catapulta) siede **a cavallo T2-alto/T3a-basso**, archetipo **Tekever AR5 / Insitu Integrator** in fascia civile. **Parte A (terra):** CapEx sistema COTS-adattato **€1,25-3,2M** (base ~€1,8M, già oltre il tetto ~€1M), OpEx **~€0,6M/anno**; NPV@12% di progetto **−€5,4M (worst) / −€2,3M (base) / +€0,1M (best marginale)**. **Parte B (mare):** delta payload marittimo su airframe condiviso **€0,3-0,96M** (base ~€0,55M; standalone €2,1-4,1M), OpEx **~€0,75M/anno**; NPV **−€6,8M / −€3,1M / +€0,3M**. **Verdetto di finanziabilità: NESSUNA delle due è finanziabile da Firmamento standalone entro il tetto ~€1M** — il solo CapEx lo eccede e l'NPV è negativo senza ricavo committed. **Entrambe richiedono un anchor pubblico pluriennale (mini-EMSA regionale per la terra; contratto Guardia Costiera/EMSA/Frontex per il mare) che copra gli OpEx PRIMA di ogni impegno di CapEx** — l'ipotesi attesa è **confermata**, coerente col benchmark EMSA €7,5-15M/anno. **Sinergia terra/mare:** airframe condiviso + payload intercambiabile (il livello di modularità difendibile) vale **€1-2,5M di CapEx + €0,2-0,4M/anno di OpEx** risparmiati vs due piattaforme separate, **ma non rimuove l'anchor-dipendenza** (due servizi anchor-dipendenti che condividono un airframe restano tali; e in caso di persistenza simultanea servono comunque 2 velivoli). **Sequenza raccomandata:** **Percorso 6A VTOL COTS prima** (dentro il tetto, TRL 9, genera il track-record per conquistare l'anchor), **T-SORV dopo e solo anchor-gated** — complementare per missione (area vasta, loiter lungo), ma in **competizione di budget** con 6A finché il tetto resta ~€1M. Il filtro economico, che è il filtro decisivo, **respinge T-SORV come asset di servizio autofinanziato e lo ammette solo a valle di un contratto pubblico pluriennale firmato.**

---

## Fonti e confidenza

| Fonte | Tipo | Uso in questo capitolo | Confidenza |
|---|---|---|---|
| `10-fasce-engineering.md` §4-5 | Costi interni (benchmark) | bracket T3a €2-5M/unità, T2 COTS €0,58-0,82M, OpEx/h €800-3.000, modularità §7 | media |
| `16-fasce-MALE-HALE-espanse.md` §2 | Ingegneria di sistema T3 | segmentazione T3a, EMSA €7,5-15M/anno, spartiacque 150 kg / 0 TC EASA, payload EO+SAR+AIS, regime agenzia | media-alta (benchmark) |
| `06-finanziabilita.md` | Analisi CFO finanziabilità | tetto ~€1M, floor equity coop €20-100k, stacking strumenti, anchor prima dell'asset | media-alta (strumenti) |
| `R5-finanziamenti.md` | Finanziamenti ancorati | Coop2050 €500k, Galaxia €1M, FESR €150k, EDF/Horizon/EIC, cumulazione | media-alta (strumenti) |
| `19-BOXTILT-economia-fattibilita.md` | Metodologia CFO | metodo TCO 5y / NPV / sensitivity / kill-criteria; verdetto BUILD morto su mercato <€1M/anno | media (metodo) |
| `23-economia-integrata-capitale.md` | Modello CFO interno | WACC 12%, OpEx €0,32M/pf/anno, NPV linea servizio | medio-bassa |
| `R2-competitor.md` | Competitor verificati | nicchia ISR/sovrana presidiata da Quantum/Tekever/Helsing; gap COTS civile fascia T3a | alta |
| `05-piattaforme-costi.md` §4/§11 | Costi/verdetto Buy-vs-Build | CapEx Y1 6A €2,5-3,5M; "Buy COTS vince" | media |
| EMSA-Tekever / Frontex FASS | Esterna (via `16`/`R2`) | comparabile servizio marittimo (contratto agenzia pluriennale) | media (da riverificare su fonte primaria) |
| L. 353/2000 (AIB) / PNRR M2C4 dissesto | Norma / fondo pubblico | esistenza capitoli di spesa AIB regionale e dissesto idrogeologico | media (esistenza) / bassa (importo su UAV) |

**Limiti dichiarati:** (1) **nessuna quotation vendor reale** per T-SORV — tutti i CapEx sono bracket pubblici o stime per analogia con la fascia T3a (`10`/`16`), confidenza medium-low; (2) i **ricavi di servizio** (anchor €0,3-1,2M/anno terra e mare) sono `[STIMA]` a confidenza **low**, nessun capitolato firmato; (3) gli **importi dei capitoli di spesa pubblici** (AIB Liguria, PNRR dissesto, Guardia Costiera/Frontex) esistono come strumenti ma **l'importo effettivamente spendibile su un servizio UAV va verificato** su bando/atto reale prima di qualunque pianificazione vincolante; (4) il **delta CapEx marittimo** (radar navale) è la voce a maggior incertezza (confidenza low-medium); (5) la **fattibilità del monitoraggio fondali** è demandata al collega EO — qui esclusa prudenzialmente dai ricavi; (6) lo **spartiacque regolatorio 150 kg** (Specific vs Certified) è la variabile che può spostare il CapEx di un ordine di grandezza e **va risolta con `aviation-regulatory-counsel`/`regulatory-adversary` prima di ogni commitment**.
