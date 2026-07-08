# 06 — Analisi di Finanziabilità (bottom-up)

> **Progetto HALE — Firmamento Technologies**
> Analisi CFO / financial analyst. Pivot strategico: dal "costruire un HALE" al "servizio alle Aree Interne" (connettività + osservazione), con la **finanziabilità** come criterio primario di selezione della piattaforma.
> **Domanda centrale:** cosa può REALMENTE essere finanziato da questo ecosistema (Regione Liguria + Legacoop + rete cooperative + CDP/Coopfond), e qual è la **taglia massima di investimento** sostenibile mantenendo alta probabilità di finanziamento?
> **Data:** 2026-07-08 · **Confidenza aggregata:** MEDIA (strumenti = dato alto; capacità del veicolo cooperativo = stima medio-bassa)
> **Metodo:** riparto da zero. Il piano CapEx pregresso (`cap-08`, `financial-model/`) è letto solo criticamente, non assunto.

---

## 0. Sintesi del metodo e regola di lettura

Questo capitolo NON stima i costi della piattaforma (lo fanno le analisi 01-05). Stima **il tetto di capitale che il veicolo — un consorzio di cooperative di comunità Legacoop + Firmamento Technologies come operatore — può realisticamente mobilitare**, strumento per strumento, e verifica le soglie del pivot:

| Soglia pivot | Ipotesi di partenza | Esito dell'analisi |
|---|---|---|
| **< €1M** = "facilmente finanziabile" | Taglia A (drone COTS / VTOL + ground segment) | Finanziabile ma **NON "facile"**: richiede stacking di 4-6 strumenti e la copertura del cofinanziamento, che è il vero collo di bottiglia |
| **decine di M€** = "difficile ma possibile" | Taglia B (flotta MALE/VTOL servizio continuo, €3-8M) | Possibile solo con **equity di rischio esterno** (€1-3M) che il consorzio non ha; probabilità 30-50% |
| **centinaia di M€** = "impossibile per questo veicolo" | Taglia C (HALE, €50-100M+) | **Confermato fuori portata**: incompatibile con la natura mutualistica del veicolo |

**Distinzione epistemica applicata in tutto il capitolo:** [DATO CERTO] = documento firmato / fonte ufficiale; [DATO ALTO] = bando/norma verificata via web; [STIMA] = elaborazione dell'analista, con confidenza dichiarata.

---

## 1. Il punto di partenza certo (e ciò che NON copre)

**[DATO CERTO]** Coopfond S.p.A. (CdA 20/10/2025) ha deliberato **€50.000** a favore del progetto "H.A.L.E. – Cooding II – Prototype", a valere sul **Fondo Servizi Reali – Programma Cooding II**, a beneficio della rete (capofila **Fabrica Soc. Coop.**).
*Fonte: `bando/[Reg.Uff.CoopFond 2025U0001593-24-10-2025]…-signed.md` (lettera firmata Andrea Passoni, DG Coopfond).*

**[DATO CERTO]** Il Business Plan del bando dimensiona lo **Studio di Fattibilità a €100.350** (oltre l'80% personale/consulenze), coperto da **€70.000 di contributi Anno 1** (di cui i €50k Coopfond) + il resto. Anni 2-3: solo €30.000/anno di contributi ipotizzati; ricavi vendite €61k (Anno 2) e €157k (Anno 3).
*Fonte: `bando/Business Plan.docx (1).md`, righe 445-489.*

> **Implicazione critica n.1 — il €50k finanzia lo STUDIO, non la flotta.** Il capitale già in cassa copre un'attività *intellettuale* (dossier, simulazioni, pre-verifica regolatoria). Non esiste, ad oggi, alcun finanziamento deliberato per l'hardware. Il salto dallo studio (€100k) alla prima flotta operativa (Taglia A, €0,5-1M) è un salto di **scala 5-10x** che richiede strumenti completamente diversi da quelli usati finora.

> **Implicazione critica n.2 — asimmetria soggetto ammissibile / soggetto capital-intensive.** I grant Coopfond/Marcora sono destinati alle **cooperative**; l'operatore che sostiene il CapEx della piattaforma è **Firmamento Technologies** (società tecnologica, non cooperativa). I fondi che arrivano alle coop non possono essere semplicemente "girati" a Firmamento: devono finanziare asset/servizi *a beneficio delle cooperative*. Questo **restringe la quota di ciascuno strumento effettivamente spendibile sul CapEx della piattaforma** e impone una struttura contrattuale attenta (es. asset di proprietà della coop/consorzio, servizio erogato da Firmamento).

---

## 2. Tabella strumenti di finanziamento

Legenda natura: **G** = grant a fondo perduto (no rimborso, no diluizione) · **D** = debito · **E** = equity/capitale di rischio · **Gar** = garanzia · **CF** = credito fiscale.
Ammissibilità: valutata per il **veicolo = rete 10 coop Legacoop (capofila Fabrica) + Firmamento operatore**, focus Liguria/Pentema.

| # | Strumento | Natura | Ticket tipico | Cofinanziamento richiesto | Tempi (domanda→cassa) | Ammissibilità del veicolo coop | Confidenza |
|---|---|---|---|---|---|---|---|
| 1 | **Coopfond — Cooding II Prototypes** | G | **max €50k** (50% spese) | 50% | 1-3 mesi (rapidissimo, **già ottenuto**) | ✅ Alta: pensato per reti ≥10 coop Legacoop | [DATO CERTO]+[ALTO] |
| 2 | **Coopfond — Cooding Invest** | G/quasi-E | **max €250k**/coop (pool €2,5M) | quota spese ammissibili | 2-6 mesi | ✅ per coop dedicata a digital transformation/innovazione | [ALTO] |
| 3 | **Coopfond — partecipazione al capitale** | E | €50-500k tipico | n/a (è capitale) | 3-9 mesi | 🟡 entra nel capitale di coop Legacoop "meritevoli" | [STIMA-MEDIA] |
| 4 | **FESR Liguria OS 1.1.1 — innovazione MPMI** | G | **max €150k** (50% fondo perduto) | 50% | 6-12 mesi | ✅ MPMI ligure; ambito S3 "Sicurezza e qualità della vita nel territorio" calzante | [ALTO] |
| 5 | **FESR Liguria — Poli di Ricerca e Innovazione** | G | progetti €0,3-2M (bando €25M) | 25-50% | 9-18 mesi | 🟡 richiede aggregazione a Polo di R&I | [ALTO]/[MEDIA] |
| 6 | **Quota SNAI area (FESR+FSE+FEASR+naz.)** | G indiretto | €4M naz. + ~€10,9M tot **per Area** | programmato via ApQ | 12-36 mesi | 🟠 **INDIRETTO**: la coop è beneficiaria/fornitore di un intervento, non grantee del fondo | [ALTO dato]/[BASSA accesso] |
| 7 | **Nuova Marcora (CFI/MIMIT)** | D agevolato 0% + E CFI | **fino €1M** (4× partecip. CFI; max 2× capitale versato) | capitale proprio proporzionale | 3-9 mesi | 🟡 **solo cooperative** (Firmamento SRL esclusa); leva limitata dal capitale delle coop | [ALTO] |
| 8 | **CFI/Cooperfidi + sezione CDP (garanzia)** | Gar su debito bancario | plafond FEI €25M; copertura costo ≤3,5% | richiede debito bancario rimborsabile | 1-3 mesi | ✅ per coop bancabili | [ALTO] |
| 9 | **CDP Venture Capital / Fondo Impresa Sociale** | E/D | €0,5-5M+ equity deep-tech | n/a / diluizione | 6-18 mesi | 🟠 VC competitivo, **mal compatibile con governance mutualistica** | [MEDIA-BASSA] |
| 10 | **PNRR — Fondo Naz. Connettività / BUL** | G a operatori TLC via gara | pool €712M (fino €2,8Mld BUL) | via gara Infratel/MIMIT | via gara | 🔴 **NO diretto**: aggiudicato a operatori TLC; solo come subfornitore/partner | [ALTO dato]/[BASSA accesso] |
| 11 | **PNRR Aerospazio / MIMIT / ASI** | G/cofin. R&D | €0,5-3M | 20-50% | 12-24 mesi | 🟡 possibile via partnership (Polito IS4Aerospace, prime) | [MEDIA-BASSA] |
| 12 | **Horizon Europe Cluster 4/5** | G (RIA 100% / IA 70%) | progetto €1-10M (quota Firmamento €0,3-2M) | 0% (RIA) / 30% (IA) | 12-18 mesi | 🟡 come partner di consorzio transnazionale | [MEDIA] |
| 13 | **European Defence Fund (EDF)** | G R&D difesa | progetti €5-30M+ (fondo €8Mld 21-27) | cofin. per development actions | 18-30 mesi | 🟠 solo consorzio 3+ Stati membri, dual-use; fase R&D avanzata | [BASSA per questo veicolo] |
| 14 | **EUSPA — CASSINI** | premi/accelerator/E | premi €100k; facility seed €0,5-2,5M | variabile | 6-12 mesi | 🟡 startup spaziali | [MEDIA] |
| 15 | **Credito d'imposta R&S (L.160/2019)** | CF | ~10% costi R&S ammissibili | post-spesa | recupero su ~3 anni | 🟡 richiede capienza fiscale (utile/IRES) | [MEDIA] |
| 16 | **Capitale proprio 10 coop + founder** | E | **€20-100k realistico** (floor) | n/a | immediato | ✅ ma **capacità limitatissima** (vedi §3) | [STIMA-MEDIA] |

**Osservazioni trasversali sulla tabella:**
- Gli strumenti **rapidi e ad alta ammissibilità** (1, 2, 4, 8) sono anche quelli con **ticket più piccolo** (€50-250k) e **cofinanziamento 50%**. La somma dei "facili" plafona intorno a **€400-600k lordi**, di cui metà è cofinanziamento da trovare.
- Gli strumenti **grandi** (6, 9, 10, 12, 13) sono o **indiretti** (SNAI, BUL: la coop non è il grantee), o **equity competitivo poco compatibile** con la cooperativa (CDP VC), o **R&D transnazionale** non adatto all'acquisto di una flotta COTS.
- Il **debito** (Marcora, CDP/Cooperfidi) è disponibile ma **proporzionale al capitale proprio** delle coop: piccolo capitale → piccola leva. E va **rimborsato**, quindi presuppone ricavi che oggi non esistono.

---

## 3. Capacità reale del veicolo cooperativo (il vincolo che tutti sottovalutano)

**[DATO ALTO]** Fotografia delle cooperative di comunità Legacoop (AICCON 2025): **106 cooperative**, in media **51 soci**, fatturato **complessivo €33,5M**, patrimonio **complessivo €7,8M**. Il 65% è in aree interne, il 69% in Comuni < 5.000 abitanti.
*Fonte: AICCON, "Economie di luogo — cooperative di comunità 2025".*

Ne deriva, **[STIMA]**:
- Patrimonio **medio** ≈ €7,8M / 106 = **~€74k per cooperativa**; la **mediana** è nettamente inferiore (distribuzione asimmetrica, poche coop grandi trainano la media). Le 10 del nostro consorzio sono piccole coop di comunità di aree interne liguri → verosimilmente **sotto la media**.
- Il patrimonio è **in larga parte illiquido** (immobilizzato nelle attività della coop): non è cassa disponibile per un investimento aerospaziale ad alto rischio.
- **Cassa fresca realisticamente conferibile** da ciascuna coop in un veicolo di rischio: dell'ordine di **€2-10k** (aumento simbolico di quota sociale). Per 10 coop: **€20-100k** di equity "proprio" del consorzio.

> **Implicazione critica n.3 — il floor di equity è €20-100k, non €0,5M.** Questo è il numero che disinnesca l'ottimismo. Ogni grant al 50% (Cooding, FESR) richiede di mettere sul piatto l'altro 50%; ogni euro di Marcora richiede capitale proprio proporzionale. Con €20-100k di equity conferibile, la capacità di **attivare cofinanziamento** e di **fare leva sul debito** è strutturalmente bassa. Il gap deve essere colmato da **Firmamento** (equity founder/seed) o da **capitale esterno** — non dalle cooperative.

---

## 4. Scenari di funding-mix per le 3 taglie

### 4.1 — Taglia A (~€0,5-1M): flotta COTS / VTOL + ground segment

*Perimetro fisico indicativo (da `cap-08`, [MEDIA]): 1-2 piattaforme VTOL classe JOUAV CW-15/CW-30E (€250-400k cad.), payload EO RGB+IR, ground station fissa+mobile, hangar leggero, setup SW, certificazioni SORA. Ipotesi centrale CapEx+IVA ≈ €0,8M.*

| Fonte | Natura | Importo target | Note di fattibilità |
|---|---|---|---|
| Coopfond Cooding Prototypes (nuova call pilota) | G | €50k | 50% cofin.; il €50k già speso è per lo studio |
| Coopfond Cooding Invest (coop dedicata) | G/qE | €100-200k | serve coop veicolo dedicata |
| FESR Liguria OS 1.1.1 | G | €100-150k | 50% cofin., ~6-12 mesi |
| Nuova Marcora (CFI) — debito 0% | D | €100-250k | limitato dal capitale coop; da rimborsare |
| Equity Firmamento (founder/seed) + coop | E | €150-350k | **il founder deve mettere la parte grossa** |
| Credito d'imposta R&S | CF | €30-60k | post-spesa, cash lag |
| **Totale attivabile** | | **~€530-1.060k** | ✅ raggiungibile **su 18-24 mesi** |

**Verdetto Taglia A:** finanziabile con **probabilità alta (60-75%)**, MA:
1. **non è "facile"**: richiede lo stacking di 5-6 strumenti, ciascuno con istruttoria, rendicontazione e cofinanziamento;
2. il **cofinanziamento e l'equity founder** (€150-350k) sono la condizione binding, non la disponibilità dei bandi;
3. la cassa non arriva a M+0: si compone su **18-24 mesi**, con gap di tesoreria da coprire (bridge €50-150k).
> **Falsifying observation A:** se al M+9 l'equity founder + cofinanziamento *committed* è < €150k, la Taglia A slitta e va ridotta a un "MVP super-lean" (1 piattaforma a noleggio, no payload telecom, ground segment minimo) da €300-500k.

### 4.2 — Taglia B (~€3-8M): flotta MALE/VTOL per servizio continuo

*Perimetro: 3-5 piattaforme con ridondanza, ops multi-sito, ground segment robusto, team operativo, primo scale-up SNAI multi-area.*

| Fonte | Natura | Importo target | Note di fattibilità |
|---|---|---|---|
| FESR Poli R&I / PNRR Aerospazio | G | €0,5-1,5M | via aggregazione/partnership, 25-50% cofin. |
| Horizon Europe IA (consorzio) | G | €0,5-1,5M | 70%, competitivo, 12-18 mesi |
| CFI/Marcora + debito CDP/Cooperfidi | D+Gar | €0,5-1,5M | richiede ricavi per servizio debito |
| **Equity di rischio esterno** (CDP VC / seed-Series A / patient capital) | **E** | **€1-3M** | 🔴 **il vero collo di bottiglia** |
| Coopfond capitale + coop | E | €0,1-0,5M | insufficiente da solo |
| Credito R&S + Patent Box | CF | €0,2-0,5M | |
| **Totale** | | **~€2,8-8,5M** | 🟡 possibile **solo se l'equity esterno chiude** |

**Verdetto Taglia B:** "**difficile ma possibile**", probabilità **30-50% [STIMA]**. Il mix regge **solo con €1-3M di equity di rischio esterno** (CDP Venture, deep-tech VC, capitale paziente). Problemi:
- il **modello cooperativo mutualistico** (voto capitario, non lucratività, porta aperta) è **poco compatibile** con l'ingresso di VC che pretende governance e ritorno — richiede uno spin-off/società di capitali affiancata alla rete coop (cambia il "veicolo");
- il debito è servibile **solo con ricavi dimostrati**, che a questa fase sono ancora in rampa (Business Plan: €157k Anno 3);
- timeline realistica **24-40 mesi** per comporre il mix.
> **Falsifying observation B:** se entro M+24 non c'è un term sheet equity esterno ≥ €1M, la Taglia B non è finanziabile da questo veicolo e va ricondotta alla Taglia A estesa.

### 4.3 — Taglia C (~€50-100M+): HALE stratosferico

*Perimetro: programma HALE solare proprietario fino a operatività.*

**Capacità massima dei grant (best case, cumulati su più anni):**
- EDF (development, cofin. richiesto): €10-30M netti su più call;
- Horizon Europe: €5-10M;
- PNRR/ASI nazionale: €5-15M;
- → **grant "tetto" plausibile ~€30-50M**, e comunque **soggetto a regole di cumulazione e intensità d'aiuto** (de minimis, GBER) che impediscono di sommare liberamente.

**Il residuo €50M+ è capitale di rischio privato/istituzionale.** Benchmark [ALTO/MEDIA] (da `cap-08` §8.3.3 DR-014): capital intensity programma HALE **$50M-1B** (Zephyr/Airbus cumulato pluriennale; **Skydweller Series A $40M** *solo round iniziale*; PHASA-35/BAE multi-round; **Sunglider/SoftBank ~$200M+**).

**Verdetto Taglia C:** **fuori portata, strutturalmente [confidenza ALTA]**. Ragioni:
1. **Scala**: nessuna combinazione di grant + debito + capitale cooperativo raggiunge €50-100M+; servono Series B/C da €15-50M+ per round, ripetute;
2. **Incompatibilità di veicolo**: il capitale che finanzia gli HALE (VC deep-tech, fondi sovrani, prime aerospaziali, programmi tipo IRIS²) esige governance societaria e ritorni che una rete di cooperative di comunità **non può offrire**;
3. **Rischio/tempo**: 8-12 anni a operatività, TRL basso, nessun ricavo intermedio → profilo che il capitale mutualistico non può assorbire.
> Il percorso HALE resta praticabile **solo** come nodo italiano di un **consorzio EU prime-led** (Firmamento operatore di servizi, non finanziatore) — cioè cambiando veicolo, come già riconosce `cap-08` §8.3.3.

---

## 5. Falsificazione obbligatoria: qual è il FLOOR reale al Year-1?

**Domanda pre-mortem:** e se anche €1M fosse difficile da mobilitare senza ricavi dimostrati?

Verifica del floor **[STIMA, confidenza MEDIA]**:

| Componente Year-1 | Importo realistico | Certezza |
|---|---|---|
| Coopfond Cooding II (già deliberato, per lo studio) | €50k | [CERTO] |
| Equity conferibile dalle 10 coop (cassa fresca) | €20-100k | [STIMA] |
| Equity founder Firmamento (seed) | €50-150k | [STIMA/incognita] |
| Grant "veloci" *incassati entro 12 mesi* (Cooding Invest + FESR, al netto dei lag) | €50-150k | [STIMA] |
| **Floor mobilitabile "in proprio" a M+12** | **~€120-300k** | |
| **Tetto deployable Year-1 (se tutti i bandi veloci vanno a segno)** | **~€300-600k** | |

**Conclusioni della falsificazione:**
- Il consorzio, **con risorse proprie**, mobilita al Year-1 **~€120-300k** — sufficiente per lo **studio + un anticipo su MVP molto lean**, **non** per una flotta da €1M.
- Il **€1M pieno** richiede che l'**intero stack** (Cooding, FESR, Marcora, credito R&S, + equity founder) vada a segno; realisticamente **si compone sul Year-2**, non sul Year-1.
- Il **fattore critico non sono i bandi**, ma (a) l'**equity founder di Firmamento** e (b) la **capacità di anticipare il cofinanziamento** in attesa delle tranche grant (che arrivano con 3-6 mesi di ritardo).
- **Rischio "cofinanziamento che il consorzio non copre" = reale.** Con equity coop €20-100k, ogni grant al 50% è un vincolo, non un regalo.

---

## 6. Verdetto: tetto di finanziabilità e taglia massima "sicura"

| Orizzonte | Tetto realistico [STIMA] | Composizione |
|---|---|---|
| **Year-1** | **€0,3-0,6M** deployable (floor "in proprio" €0,12-0,3M) | €50k Coopfond + equity founder/coop + primi grant veloci |
| **A 3 anni (cumulato)** | **€1,5-3M** | stack completo grant liguri/coop + Marcora + credito R&S + modesta equity; entra nella **fascia bassa della Taglia B solo se** si aggiunge equity esterno €0,5-1,5M |
| **Oltre** | richiede **cambio di veicolo** (spin-off SpA + capitale VC/istituzionale o consorzio EU) | — |

**VERDETTO sulla taglia massima "sicura":**

- ✅ **Taglia A (~€1M) = tetto sicuro con alta probabilità**, a due condizioni non negoziabili: (1) Firmamento porta l'**equity founder** (€150-350k); (2) il CapEx si distribuisce su **18-24 mesi** con bridge di tesoreria. Anche così, "sicuro" ≠ "facile": è uno stacking di 5-6 strumenti.
- 🟡 **Taglia B (€3-8M) = possibile ma condizionata** all'ingresso di **€1-3M di equity di rischio esterno** e, con esso, a un **adeguamento del veicolo** (società di capitali affiancata alla rete coop). Probabilità 30-50%. La fascia bassa (€3M) è al limite del raggiungibile in 3 anni; €8M richiede un round Series A vero.
- 🔴 **Taglia C (€50-100M+, HALE) = fuori portata** per questo veicolo. Praticabile solo come operatore in un consorzio EU prime-led, cioè non più "questo veicolo".

**Coerenza con le soglie del pivot:** confermate, con una precisazione. Il "< €1M facilmente finanziabile" è vero sulla *disponibilità dei bandi* ma **sovrastima la facilità**: il collo di bottiglia è il **cofinanziamento + equity founder + tesoreria**, non l'esistenza degli strumenti. Il "decine di M€ difficile ma possibile" vale **solo per la fascia €3-8M e solo con equity esterno**; oltre i €10M il veicolo cooperativo non arriva. Il "centinaia di M€ impossibile" è **confermato senza riserve**.

**Raccomandazione operativa per la selezione della piattaforma:** dimensionare la piattaforma-target entro un **CapEx ≤ €1M spendibile su 18-24 mesi** (Taglia A), trattando la Taglia B come opzione Year-2/3 subordinata a un term sheet equity esterno. Questo tetto è il vincolo che, a valle, seleziona la piattaforma: **COTS/VTOL sì, MALE-fleet solo con equity esterna, HALE no.**

---

## 7. Fonti e livelli di confidenza

**Documenti di progetto (locali):**
- `bando/[Reg.Uff.CoopFond 2025U0001593-24-10-2025]…-signed.md` — delibera €50k Coopfond [CERTO]
- `bando/Business Plan.docx (1).md` (righe 445-489) — studio €100.350, contributi €70k/€30k/€30k, ricavi €61k/€157k [CERTO come dato di piano]
- `bando/Elenco Cooperative.md` — 10 coop rete + capofila Fabrica [CERTO]
- `bando/piano economico prototype cooding.md`, `bando/Sintesi/progetto prototype cooding.md` — struttura studio [CERTO]
- `studio-di-fattibilita/cap-08-economico-finanziario.md` + `allegati/financial-model/README.md` — benchmark CapEx piattaforma e capital intensity HALE [MEDIA, letto criticamente]

**Fonti web (verificate luglio 2026):**
- Coopfond/Legacoop — Cooding II: pool €500k Prototypes, €50k max/50%, ≥10 coop; Cooding Invest €2,5M/€250k max [ALTO]
- Regione Liguria PR FESR 2021-2027 — OS 1.1.1 innovazione MPMI: 50% fondo perduto max €150k; bando Poli R&I €25M [ALTO]
- MIMIT/CFI — Nuova Marcora: fino €1M, 0%, 3-10 anni, 4× partecipazione CFI / max 2× capitale versato [ALTO]
- Agenzia Coesione/OpenCoesione — SNAI 2021-2027: €4M naz. + ~€10,9M tot per Area; 72 ApQ, ~€1,18Mld [ALTO]
- AICCON 2025 — cooperative di comunità: 106 coop, 51 soci medi, €33,5M fatturato tot, €7,8M patrimonio tot [ALTO]
- Cooperfidi Italia — plafond FEI €25M, sezione CDP, costo garanzia ≤3,5% [ALTO]
- MIMIT/Infratel — PNRR Fondo Naz. Connettività ~€712M (BUL fino €2,8Mld), assegnato a operatori TLC via gara [ALTO dato / BASSA accessibilità diretta]
- CINEA/EUSPA — Horizon Europe progetti €1-10M (RIA 100%/IA 70%); EDF €8Mld 2021-27; CASSINI premi €100k [ALTO/MEDIA]

**Confidenza aggregata del capitolo: MEDIA.** Alta sull'esistenza e sui parametri degli strumenti; **medio-bassa** sulla capacità effettiva del veicolo cooperativo di attivare cofinanziamento ed equity (il dato più incerto e più decisivo, formalizzato come `floor €20-100k` da validare con i bilanci reali delle 10 coop).

**Azioni di validazione prima del gate:** (1) acquisire i **bilanci 2024-2025 delle 10 coop** per sostituire lo `[STIMA]` del floor con dato certo; (2) **LoI Regione Liguria** su FESR OS 1.1.1 + calendario bandi 2026; (3) verifica apertura **nuova call Cooding Prototypes/Invest 2026**; (4) definire l'**impegno di equity founder Firmamento** (numero oggi assente dai documenti).
