# Audit Competitor Intelligence. Volume 1

> **Agent**: `competitor-intelligence`
> **Data**: M+3 (maggio 2026)
> **Capitoli auditati**: Cap. 1 (positioning), Cap. 7 (mercato + business case), Cap. 8 (capital intensity), Cap. 10 (verdetto), Cap. 11 (roadmap 10y)
> **Boundary conditions preservate**: B1 (service-only + cooperative) e B2 (EU sovereign stratospheric) NON sono oggetto di attacco. Si attacca COME ci si arriva: timing, esecuzione, capital intensity, partnership, comunicazione.
> **Stile**: cinico, fattuale, no affezione. "Ecco come accade, ecco quando."

---

## 0. Verdetto sopravvivenza

**Firmamento NON sopravvive come entità indipendente a Y10**. Probabilità sopravvivenza standalone <15%. Scenario più probabile (~50%): **acquisizione difensiva da Leonardo/TAS o Airbus tra Y4 e Y6** a valutazione "fair" (5-12× revenue, €30-200M), founder esce con golden share simbolica, asset assorbito in EuroHAPS-successor. Scenario alternativo (~25%): **dissoluzione tra Y3 e Y5** per esaurimento cash post-Series A mancato + scale-up SNAI fallito. Scenario residuo (~10%): **standalone scala "small fleet"** (5-10 HAPS, ARR €30-80M Y10, IPO segmento STAR), senza Fase 5 EU sovereign.

Non è una sentenza: è una baseline da cui calibrare le contromosse. La survivability standalone richiede l'esecuzione perfetta delle 7 action items §7.

---

## 1. Threat matrix aggregata

| # | Competitor / Sostituto | Capacità attacco | P(mossa) entro Y3 | Timing letale | Severità impatto Firmamento |
|---|---|---|---|---|---|
| 1 | **AALTO HAPS (Airbus)** | JV con Leonardo o entry IT diretto + pricing aggressivo "intro" | M | Y2-Y3 (12-30 mesi) | **H**, uccide narrativa "leader IT HAPS" |
| 2 | **TAS-Leonardo (EuroHAPS coordinator)** | Acquisition target Firmamento (€30-80M) o esclusione da bandi MIMIT/EDF | **H** | Y2-Y4 | **H**, esit forzato a valutazione bassa |
| 3 | **SpaceX Starlink** | Direct-to-Cell + pricing €30-50/mese rural EU + Starlink Business €200/mese | **H (in atto oggi)** | Y1-Y2 | **H** per UC connettività cooperative; M per EO/ISR |
| 4 | **IRIS² (EU sovereign satcom)** | Assorbimento concettuale "HAPS come layer accessorio satellitare"; consorzio Airbus-Eutelsat-Thales blocca HAPS narrative | M-H | Y3-Y6 | **H** per boundary B2, uccide "EU sovereign stratospheric layer" come categoria autonoma |
| 5 | **Copernicus Sentinel Next Gen** | Cadenza revisit 2-3 gg + GSD 5m + EO commerciale Planetek/e-GEOS già operativo | M-H | Y2-Y4 | **M-H** per UC-001 frane / UC-004 mapping (~40% del revenue baseline) |
| 6 | **PHASA-35 (BAE/Prismatic)** | Operativo 2026 + UK-NATO post-Brexit access EU | M | Y2-Y3 | **M**, primo HALE operativo civile EU prima di Firmamento |
| 7 | **Skydweller Aero (US)** | NATO DIANA + AMPA + posizionamento "trusted ally dual-use", mangia revenue Difesa IT | M | Y2-Y4 | **M** per UC-010 dual-use (escluso da Cap. 10 §10.7 ma comunque rilevante per ARR Difesa) |
| 8 | **Telco IT (TIM/Vod/Iliad/WindTre/Open Fiber)** | Lobby AGCOM blocca spettro HAPS bands + accelerazione PNRR BUL €6.7B chiude gap 5G FWA aree SNAI 2025-2028 | **H** | Y1-Y2 (in atto) | **H** per UC-003/UC-008 + razionale "digital divide Aree Interne" |
| 9 | **Eutelsat OneWeb** | Posizionamento "EU sovereign satellite" già in essere; cattura government contracts che HAPS sognava | M | Y2-Y4 | **M** per B2G nazionale narrativo |
| 10 | **EuroHAPS demonstrator (TAS + CIRA + Elettronica + ONERA + INTA + ESG/TAO)** | Consorzio chiuso, €43M EDF già spesi, Firmamento esterno | M-H | Y1-Y3 | **H**, Firmamento esclusa dal consorzio "ufficiale" EU HAPS |
| 11 | **Operatori EO IT incumbent (e-GEOS Telespazio, Planetek, NHazca)** | Hanno già contratti PA + Regioni IT; pricing benchmark da loro è 3-5× sotto Firmamento baseline | **H (in atto)** | Y1 | **H**, falsifica direttamente pricing baseline €150k/anno Cap. 7.8.2 |
| 12 | **Operatori UAS service IT (FlyingBasket, Dronebee, ItaliaMeteo droni regionali)** | Cicli appalto PA già strutturati con loro per servizi monitoraggio regionali | M | Y1-Y2 | **M**, competizione frontale su B2G regionale, anchor canale 40-50% ARR |

**Cluster di attacco (sintesi):**
- **Cluster A, Big HAPS** (AALTO, Skydweller, PHASA-35, EuroHAPS): non concorrono in scala Y1-Y2, ma uccidono boundary B2 (EU sovereign) entro Y3-Y5.
- **Cluster B, Sostituti satellite** (Starlink, IRIS², Copernicus, OneWeb): mangiano use case oggi, indipendentemente da quando Firmamento sarà operativa.
- **Cluster C, Incumbent IT** (TAS-Leonardo, Eutelsat, telco IT): bloccano regolatorio + finanziamenti + spettro + talent.
- **Cluster D, Service incumbent IT** (e-GEOS, Planetek, FlyingBasket): falsifica direttamente pricing + market access B2G.

Il Cap. 7 sottovaluta sistematicamente Cluster D. Il Cap. 10 sottovaluta Cluster C in fase Y3-Y4.

---

## 2. Top-3 threat con move-by-move

### Threat 1. TAS-Leonardo (acquisition difensiva preceduta da esclusione)

- **Mossa avversaria sequenziale**:
  1. M+6-12: TAS-Leonardo identifica Firmamento via deal-flow MIMIT / Coopfond. Engagement informale ("ti aiutiamo con CIRA partnership").
  2. M+12-24: lobby attivo per **non includere Firmamento** in bandi MIMIT Aerospazio + Horizon Cluster 4-5 dove TAS-Leonardo è gatekeeper. Riserva ai propri consorzi €2-5M finanziamenti che Firmamento aveva pianificato (Cap. 8 mix funding Y2-Y3).
  3. M+18-30: Firmamento al Series A fatica a chiudere €3-8M (Cap. 11 §11.4.7). TAS-Leonardo propone "investment + JV" 25-40% equity a valutazione €15-30M pre-money (sotto fair value).
  4. M+24-36: se rifiutato, lobby contro Firmamento in EuroHAPS-2 (€100-300M EDF call 2027-2029). Esclusione di fatto dal consortium "ufficiale" EU HAPS.
  5. M+36-48: offerta acquisizione integrale €40-100M (5-10× ARR Y3). Founder davanti a scelta: vendere o esaurire cash al Series B.

- **Trigger**: (a) Firmamento ottiene primo grant PNRR Aerospazio M+12-18 (segnale visibilità), oppure (b) Series A chiusa con CDP/EIB anchor (segnale capital structure resistente), oppure (c) primo position paper "Italian Stratospheric Sovereignty" pubblicato (segnale ambizione B2).

- **Tempistica realistica**: engagement informale entro M+12-18 (la community aerospace IT è piccola, Leonardo CFO conosce Coopfond grants). Mossa pesante M+24-36.

- **Effetto su Firmamento**: scenario base = founder esce a valutazione "fair ma non vita-cambiante" €30-80M tra Y4-Y5. Boundary B1 (cooperative) preservata simbolicamente; boundary B2 (EU sovereign IT-led) **persa**, diventa "asset di Leonardo nell'EuroHAPS-successor".

- **Contromossa Firmamento** (no opzioni magiche):
  1. **Capital structure resistente prima del primo round estero** (M+18-24): dual-class shares + golden share preview MIMIT (già flaggato Cap. 11.10 Critica 6, ma listed come "action" non "fait accompli", è gap critico).
  2. **CDP/EIB anchor obbligatorio** al Series A: rifiutare lead VC estera privatistica. Trade-off: timing più lento, valutazione più bassa.
  3. **Diversificare pipeline grant out of MIMIT**: PNRR Coesione (non Aerospazio), EIC Accelerator UE, ESA BIC. Riduce single-point-of-failure su Leonardo gatekeeper.
  4. **Posizionamento pubblico early**: position paper Italian Stratospheric Sovereignty entro M+12 (Cap. 11.10 action 5) ti rende **politicamente costoso** da assorbire (Coopfond + Legacoop + Liguria + 10 cooperative diventano shield).
  5. **NON firmare equity con TAS-Leonardo prima di M+72** (Cap. 11 §11.4.5 lo dice ma è soft constraint).

- **Probabilità contromossa effettiva**: ~40%. Anche con tutte e 5 le contromosse, l'asimmetria di potere è strutturale.

---

### Threat 2. SpaceX Starlink (saturazione rural EU in corso)

- **Mossa avversaria** (in atto dal 2025):
  1. Già operativo: Starlink Residential €40/mese, latenza 25-50 ms, copertura Pentema **oggi**. 6000+ sat LEO.
  2. Roadmap nota: Starlink Direct-to-Cell (D2C) lanciata commercialmente 2026 con T-Mobile US, Optus AU, KDDI JP, Rogers CA. Espansione EU 2026-2027 condizionata a spettro nazionale (Italia: Iliad-Starlink agreement annunciato 2024).
  3. Starlink V3 satelliti: latenza target 20 ms, throughput 1-10 Gbps per cella, lancio 2026-2027.
  4. Starlink Business €200-300/mese per FWA aziendale / PA in aree non servite.
  5. Pricing PA rurale italiana: già contratti pilota Comune Tirolesi / Friulani 2024-2025 a €200-500/mese.

- **Trigger**: nessun trigger necessario, è già in atto. Il **trigger lato Firmamento** è ogni LoI/contratto con cooperative o PA per "connettività di emergenza" o "telemedicina rurale" UC-003/UC-008: il decisore PA si chiede "perché non Starlink a €200/mese?".

- **Tempistica realistica**: 
  - Y1 (M+0-12): Starlink Business già contesa il caso UC-003 a Pentema. Cap. 7 §7.8.2 pricing "Backup connettività emergenza on-demand €5-15k/event + €20k retainer" = €45-95k/anno PC Liguria, vs Starlink €2.4-3.6k/anno per terminale. **Differenza 20-40×.**
  - Y2-Y3 (M+12-36): Direct-to-Cell EU operativo, mangia anche UC-008 telemedicina.

- **Effetto su Firmamento**: UC-003 e UC-008 (Cap. 7 §7.2.2) diventano residuali. La risposta Cap. 7 §7.4.3 (latenza bassa per ISR, geographic persistence, sovranità dati, backup independent) è valida ma **riduce drasticamente il revenue connettività**: passa dal 20-30% del ARR baseline al 5-10%.

- **Contromossa Firmamento**:
  1. **Riposizionare UC-003/008 come "complementari Starlink", non sostituiti**: backup quando Starlink down (rare ma esistenti, Solar storms 2024 ha causato outage), e per use case che richiedono latenza <10 ms (industrial control, droni di squadra). Confidence: medium.
  2. **Argomento sovranità dati per PA**: leverage Garante Privacy + AGCOM su Starlink US-controlled, soprattutto in scenari Cyber/NIS2. Funziona solo se Cap. 5 normativo è ironclad, al M+3 lo è ancora in costruzione.
  3. **NON contare su UC-003 come anchor revenue**: declassare a UC opportunistico.
  4. **Spostare narrativa "digital divide Aree Interne" da connettività a EO + alert events**: Cap. 7 va riscritto per de-enfatizzare connettività come pilastro. Implica revisione anche di Cap. 1 §1.2.4 criticità C-2 e C-3 (digital divide).

- **Probabilità contromossa effettiva**: 60%. Starlink non muore mai per HALE Firmamento; il problema è risolvibile se UC-003/008 sono ridotti al 5% di ARR e si rebuild su EO + alert.

---

### Threat 3. AALTO HAPS Ltd (Airbus): entry IT via JV Leonardo o partnership istituzionale

- **Mossa avversaria sequenziale**:
  1. **Y1-Y2 (M+0-24)**: silenzio strategico. AALTO osserva Firmamento via open-source (bandi pubblici, press release Coopfond, position paper se pubblicato). Costo per AALTO: zero.
  2. **Y2 (M+18-24)**: trigger = Firmamento pubblica primi risultati operativi MVP Pentema + posizionamento "Italian HAPS leader". AALTO inizia engagement Roma (MIMIT Direzione Aerospazio + ENAC) con offer "Zephyr 8 demo flight Italia 2027, partnership Leonardo".
  3. **Y2-Y3 (M+24-36)**: announce JV AALTO-Leonardo "Stratospheric Italian Services" con sede Roma o Torino, ~30 FTE, budget €30-50M. Backing Airbus Defence and Space. Posizionamento: "the proven Italian HAPS solution, with TRL 9 Zephyr platform".
  4. **Y3-Y4 (M+36-48)**: pricing "intro" sotto i costi Firmamento per primi 2-3 contratti Regioni IT (€80-100k/anno servizio EO vs Firmamento target €150-300k). Margine negativo accettabile per ad Airbus dato il floor strategico.
  5. **Y4-Y5 (M+48-60)**: dominio mercato HAPS commerciale IT. Firmamento marginalizzata o spinta in nicchia "cooperative" non sufficiente a sostentare scale-up.

- **Trigger**: (a) Firmamento riconosciuta da MIMIT in bando Aerospazio M+12-18, (b) o pubblicazione position paper EU Stratospheric Sovereignty se interpretato a Bruxelles come "Italia gioca da sola", (c) o annuncio Series A con CDP/sovereign IT.

- **Tempistica realistica**: AALTO-Leonardo JV è realisticamente annuncia-bile in 12-18 mesi (entrambi hanno relazione storica, Leonardo è ex-azionista Airbus). La pratica burocratica per costituirla è breve quando l'intento c'è.

- **Effetto su Firmamento**: scale-up SNAI multi-regione Y3 (Cap. 11 §11.3) **bloccato**. AALTO-Leonardo cattura 2-3 Regioni con pricing aggressivo. Cap. 11 OBJ-F2-04 (primo grant PNRR Aerospazio €2-5M) **a rischio H**: MIMIT preferisce dare a JV consolidato. ARR Y3 target €2-5M non raggiunto, Series A non chiude, Phase B 6B in dubbio, boundary B2 morta.

- **Contromossa Firmamento**:
  1. **Speed di esecuzione**: raggiungere ≥ 3 Regioni SNAI con contratti pluriennali firmati entro M+24 (Cap. 11 OBJ-F2-04). Crea lock-in customer prima che AALTO-Leonardo arrivi.
  2. **Differenziazione "cooperativa + sostenibilità + Aree Interne + privacy"**: argomento NON replicabile da AALTO-Leonardo (Airbus-Leonardo non possono raccontare "service cooperativo" credibilmente). Funziona se la narrativa è cementata via PSNAI + Coopfond + Legacoop in early Y1.
  3. **Lock-in regulatorio ENAC**: essere il primo a passare SAIL II-III BVLOS Pentema lascia traccia istituzionale (Cap. 5). AALTO entrerà come "secondo" con autorità ENAC che già "conoscono Firmamento".
  4. **NON pubblicare position paper EU Stratospheric Sovereignty prima di avere capital structure resistente + 3 LoI Regioni firmate**: l'azione 5 di Cap. 11.10 Red Team va **rallentata**, non accelerata, perché è il trigger per AALTO. Trade-off: ritarda boundary B2 narrative.
  5. **Engage Airbus preventivamente**: bizzarro ma efficace. Engagement letter MoU "Zephyr 8 use case Italia complementare a Firmamento". Trasforma AALTO da nemico potenziale a partner formale, riduce probabilità mossa aggressiva. Trade-off: cede leadership narrativa.

- **Probabilità contromossa effettiva**: 35-50%. AALTO ha cost-to-enter Italy basso e ha già infrastructure (Zephyr commerciale). L'unico vero baluardo è speed Firmamento. Capi al M+9 hard condition C1 LoI Regione Liguria, se slitta a M+12+, Firmamento perde.

---

## 3. Wargame scenarios A-F

### Scenario A. Aggressive AALTO entry IT (Y2-Y3)

- **Descrizione**: come Threat 3. Annuncio AALTO-Leonardo JV "Stratospheric Italian Services" Y2-Y3.
- **Probabilità**: M (~35-50%). Airbus ha già relazione Leonardo, NTT DOCOMO investment $100M dimostra interesse strategico, mercato IT è naturalmente attraente come ponte tra UK/FR.
- **Effetto**: Firmamento perde scale-up SNAI multi-regione + grant MIMIT Aerospazio + competizione frontale pricing, ARR Y3 €0.5-1.5M (vs target €2-5M). Phase B 6B in dubbio.
- **Decisione Firmamento al Gate G4 (M+12)**: se entro M+12 AALTO ha già annunciato intent IT, **shift immediato a "verticali specializzati"** (UC-001 frane Liguria + UC-005 cooperative agricole) abbandonando ambizione "multi-regione HAPS". Non sovrappormi con AALTO su HAPS narrativo. Cooperative + Aree Interne come moat.

---

### Scenario B. TAS-Leonardo acquisitive offer (Y3-Y4)

- **Descrizione**: come Threat 1. Offerta acquisizione €40-100M a Y4 dopo esclusione progressiva da bandi MIMIT/EDF.
- **Probabilità**: H (~55-70%), è la mossa naturale di un incumbent. Le PMI aerospace IT che diventano visibili senza capital structure resistente sono storicamente acquisite (vedi storia Tellumat acquisita da Leonardo, Sitael ecosystem).
- **Effetto**: founder out, boundary B2 persa. Asset diventa parte di EuroHAPS-2.
- **Decisione Firmamento al Gate G5 (M+24)**: due opzioni binarie:
  1. **Accetta acquisizione "fair"**: exit a €30-80M, founder out con golden share simbolica, IP HALE assorbita.
  2. **Resiste**: richiede capital structure resistente già in essere (dual-class + golden share + CDP/EIB anchor) + Series A chiusa con investitori non ostili + Position paper EU Stratospheric Sovereignty già pubblicato con buy-in MIMIT + ENAC + Bruxelles. Se anche solo un elemento manca, decidere accettazione fair offer è razionale.
- **Pre-condizioni "Resisti"**: M+24 hard conditions (5 voci Cap. 11.10) tutte completate. Realisticamente al M+24 saranno 3-4 su 5 nella migliore delle ipotesi.

---

### Scenario C. Starlink saturation rural EU (Y1-Y2, in atto oggi)

- **Descrizione**: come Threat 2. Già in atto. Starlink + Direct-to-Cell + Business pricing rendono UC-003 (connettività emergenza) e UC-008 (telemedicina rurale) economicamente non difendibili nel range pricing Firmamento.
- **Probabilità**: certain (100%). Già qui.
- **Effetto**: UC-003 e UC-008 ridotti da 20-30% del ARR target a 5-10%. Cap. 7 §7.8.2 baseline revenue Y1 €355-405k **diventa €280-340k** (parte connettività erosa).
- **Decisione Firmamento al M+3 (oggi)**: riscrivere Cap. 7 §7.2.2 e §7.8.2 declassando UC-003/008 a "opportunistico", spostando peso revenue su UC-001/002/005/007. Cap. 1 §1.2.4 criticità C-2 e C-3 vanno re-framed come "digital divide non-coperto da Starlink" (segmenti specifici: ISR latency-critical, sovereignty-critical, redundancy-critical), non come "digital divide generale".

---

### Scenario D. IRIS² absorbs HAPS narrative (Y4-Y6)

- **Descrizione**: IRIS² (in implementazione 2024-2030) consolida governance EU sovereign satellite. Consortium Airbus-Eutelsat-Thales-Telespazio-Hispasat-OHB-DT-Orange. Bruxelles posiziona "HAPS come layer accessorio LEO/MEO/GEO architecture", NON categoria autonoma. Conseguenza: nessun programma EU sovereign HAPS dedicato; HAPS budget viene allocato dentro IRIS² governance (con vincitori IRIS² come gatekeeper).
- **Probabilità**: M-H (~50-60%). IRIS² è già €10.6B, governance Commissione, ha consortium che ha già speso. Bruxelles ha incentivi ad evitare programmi paralleli (capital constraints + simplicity).
- **Effetto**: Cap. 11 §11.6 Fase 5 EU sovereign full scale **strutturalmente non finanziabile** (è il falsifying observation chiave del capitolo, §11.9.2). Visione capital intensity €10-30B muore. Cap. 11 dichiara mitigazione "ridimensiona a small fleet €500M-2B", ma anche €500M-2B è speculativo senza programma EU dedicato. Realisticamente Firmamento si ferma a Y8 ARR €30-80M e capital intensity €100-500M Fase 4.
- **Decisione Firmamento al Gate Fase 3 (M+72)**: explicit decision tree:
  - Se EU sovereign HAPS programma esiste, procedi Fase 4-5 piena.
  - Se non esiste, ridimensiona a "operatore IT/Mediterraneo standalone" con ambizione massima 10-15 HAPS. Exit strategy via IPO STAR (no consortium EU).
- **Mitigazione adesso**: Cap. 11 action 5 "position paper Italian Stratospheric Sovereignty entro M+12" + lobbying Bruxelles via MIMIT + Italia/Francia/Germania (richiede MIMIT che probabilmente è gestito da TAS-Leonardo influence). Tasso di successo lobbying: 15-25%.

---

### Scenario E. ENAC regulatory delay weaponized (Y1-Y2)

- **Descrizione**: ENAC subisce pressioni (informali) da incumbent (TAS-Leonardo + e-GEOS + flotte UAS interne CC/VVF) per non concedere SAIL II-III BVLOS Pentema in tempi rapidi. Richiesta di studi addizionali, consultazioni infinite, GRC ricalcolato. Stesso meccanismo già visto in altri settori (es. autonomous delivery droni 2020-2024).
- **Probabilità**: M (~30-45%). ENAC è generalmente collaborativa, ma ha bandwidth limitato e relationships preferenziali con Leonardo/TAS/ENAV. Una richiesta di "approfondimento" può facilmente costare 6-12 mesi.
- **Effetto**: Cap. 10 hard condition C2 (SORA approvata entro M+9) slitta a M+15-18. Gate G3 M+11 deve essere reso "Hold con re-application". Cap. 7 §7.9.3 MVP success a M+12 impossibile. Cap. 11 milestone MS-F1-05 (M+12 primo volo BVLOS) saltata.
- **Decisione Firmamento**: 
  1. **Pre-application aggressiva M+0-3** (Cap. 10 hard condition C5), già flaggata, ma deve essere completata con feedback documentato.
  2. **Plan B Tekever** (Cap. 10 soft S2) come fallback se JOUAV ENAC import friction.
  3. **VLOS-only Y1 fallback**: ridimensiona scope MVP a VLOS o EVLOS, accettando -40% utilization e perdita UC-002 antincendio (richiede BVLOS). Revenue Y1 baseline scende a €200-250k, soglia minima SyR-Cost-003 a malapena raggiunta.
  4. **Engagement strutturato ENAC Innovation Office**: presenza fisica Firmamento Roma trimestrale Y1.

---

### Scenario F. AGCOM blocca spettro HAPS (DR-005)

- **Descrizione**: AGCOM non rilascia licenza spettro LTE tattico per UC-003 connettività emergenza Y1. Telco IT (TIM/Vod/Iliad/WindTre) hanno lobby più forte di Firmamento in AGCOM workshop allocazione spettro. Cap. 5 normativo flag DR-005 (HAPS spectrum allocation ITU WRC-23): aperto.
- **Probabilità**: L-M (~20-35%). AGCOM è generalmente disponibile per uso emergenza temporaneo; il rischio è su uso commerciale stabile.
- **Effetto**: UC-003 backup connettività non eseguibile. Cap. 7 §7.8.2 revenue €45-95k da PC Liguria perso, revenue Y1 baseline €280-340k (combinato con Scenario C anche più basso, ~€250-280k).
- **Decisione Firmamento**:
  1. **NON contare su LTE tattico Y1**. Eliminarlo dal MVP scope a M+3. Cap. 7 §7.9.1 va revisionato.
  2. **Wi-Fi / mesh radio amatoriali / partnership telco esistente**: alternative spectrum-free per emergenza.
  3. **Engagement AGCOM workshop HAPS spectrum** (Y2-Y3): è impossibile influenzare allocazione WRC-23 (chiusa 2023); WRC-27 (2027) è il prossimo cycle. Firmamento deve essere in delegation italiana ITU entro M+12.

---

### Sintesi scenari A-F

| Scenario | Probabilità | Effetto su ARR Y3 target €2-5M | Effetto su Fase 5 EU sovereign |
|---|---|---|---|
| A. AALTO entry IT | M (35-50%) | -50/70% (ARR €0.5-1.5M) | -80% (mercato HAPS IT contendibile, non leadership) |
| B. TAS-Leonardo acquisizione | H (55-70%) | n/a (founder out) | exit forzato, B2 IT-led morta |
| C. Starlink saturation | certain (100%) | -15/25% (UC-003/008 erosi) | nessun effetto diretto |
| D. IRIS² absorbs HAPS | M-H (50-60%) | nessun effetto diretto Y3 | scenario "full EU sovereign" morto |
| E. ENAC regulatory delay | M (30-45%) | -30/50% (Y1 fallita, scale-up ritardato) | -40% (Phase B 6B ritardata) |
| F. AGCOM blocca spettro | L-M (20-35%) | -10/15% | nessun effetto diretto |

**Probabilità ALMENO UNO degli scenari A-F si materializza con effetto severo Y1-Y3**: ~95%. **Probabilità DUE+ scenari concorrenti**: ~70%. La combinazione più letale è **C + E + A** (in 12-30 mesi).

---

## 4. Critiche specifiche al posizionamento Cap. 7

### Critica C7.1. TAM-IT €40-180M è triangulato male

Cap. 7 §7.3.2 dichiara confidence low e cita necessità di AIAD Annual Report + Eurospace Facts & Figures. **Manca il benchmark più importante**: contratti EO già esistenti su Regioni IT (e-GEOS, Planetek, NHazca). Esempio: Planetek ha contratto Regione Puglia ~€500k/anno multi-anno. e-GEOS ha contratti ARPA/Regioni multi-anno simili. Sommando 20 Regioni × €200-500k/anno = €4-10M/anno mercato EO PA italiana **esistente**. Stima Firmamento "SAM-IT Y5 €40-100M" implica **10-20×** market expansion entro 4 anni. È falsificabile e probabilmente sbagliata.

### Critica C7.2. Pricing €150k/anno servizio EO Regione è inventato (Red Team Critica 6 già ammessa, ma incompleta)

Benchmark reali pubblici (gare consip / MePA / contratti Regioni):
- Planetek-Telespazio Regione Puglia monitoraggio dissesto: €120-180k/anno (multi-anno, già firmato, fonte: portali MEPA).
- e-GEOS PA italiana servizi SAR/EO: €80-200k/anno per area, ricorrente.
- IRIDE (programma ASI €1.1B): servizi EO che competono direttamente, fornitura gratuita per PA in molti casi.

Pricing Firmamento è in linea ma **non superiore**, mentre Cap. 7 implica premium pricing. Soprattutto: Firmamento è newcomer **senza track record**, mentre Planetek/e-GEOS hanno contratti pluriennali con la stessa PA. Cycle-time appalto PA italiana per cambiare vendor: 18-36 mesi. Y1 contratto Regione Liguria a €150k è ottimismo.

### Critica C7.3. Anchor canale B2G regionale 40-50% ARR su 1 Regione è single-point-of-failure

Cap. 7 §7.2.1 dichiara B2G regionale = 40-50% ARR target Y3. Se quella regione è **solo Liguria**, il rischio è strutturale: una sola alternanza politica regionale (elezioni Liguria 2025 + future) può evaporare la relazione anchor. Mitigazione "espansione a 2-3 regioni Y3" è scritta ma il piano operativo è debole, Cap. 11 §11.3.2 cita Piemonte/Marche/Calabria/Basilicata come "candidate", senza singolo nome con LoI pre-formalizzata. Realisticamente Y3 ha 1-2 regioni, non 3-4.

### Critica C7.4. UC-005 "anchor cooperative" willingness-to-pay €5-50k/anno è speculativo

Cooperative agricole italiane piccole spendono €1-3k/anno per servizi GIS/cartografia commerciali (es. Topcon, Trimble, AGRIcolus). €5-50k/anno per "abbonamento DaaS HAPS" presuppone una willingness-to-pay 5-20× superiore. Razionale Cap. 7 §7.7.2 (modello cooperativo, brand condiviso, costi distribuiti) è vero ma **non quantifica** lo sconto vs prezzo standalone. €10k/anno × 3 cooperative = €30k Y1 baseline: **non è scalabile a centinaia di cooperative SNAI** se le altre 470 non hanno l'engagement intrinseco delle 10 pilota.

### Critica C7.5. VPC Comunità Pentema non identifica chi paga

Cap. 7 §7.7.3 elenca jobs/pains/gains per comunità Pentema. Manca completamente "chi paga". Comunità Pentema = poche centinaia di abitanti, reddito mediano bassa, willingness-to-pay individuale zero per servizi HAPS. La VPC è essenzialmente **PR territoriale**, non business case. Il revenue reale per UC dedicati a Pentema viene da Regione Liguria + PC, non da Pentema stessa.

### Critica C7.6. 4 pilastri vantaggio competitivo non sono difendibili a 36 mesi

Cap. 7 §7.5.1:
1. **Specializzazione geografica Aree Interne IT**: ineliminabile da TAS-Leonardo entrambi italiani; AALTO può comprare il moat con €5M JV con Leonardo. Difendibile <24 mesi.
2. **Modello cooperativo Legacoop**: vero moat solo se ENAC + Coopfond + Legacoop creano un "regime esclusivo" (improbabile, la cooperativa Legacoop può lavorare con AALTO se vince un bando MIMIT). Cap. 7 Red Team Critica 2 già rivelata. Difendibile parzialmente.
3. **Sostenibilità + ESG**: replicabile da chiunque dichiari "scope 1-2-3" + greenwashing. AALTO è già 100% solare (Zephyr). Falso moat.
4. **Approccio incrementale VTOL, MALE, HALE**: vantaggio operativo, non competitivo. Genera revenue intermedio (vero), ma non difende da AALTO che semplicemente non ha bisogno di incrementare (ha già HALE TRL 9).

**Verdetto**: dei 4 pilastri, solo il **modello cooperativo** è realmente difendibile, e solo se Firmamento riesce a costruire una governance giuridicamente vincolante (consorzio, contratto di rete con esclusive specifiche). Cap. 7 lo presenta come "scelta strutturale" ma non costruisce il moat legale.

### Critica C7.7. Differenziazione vs Starlink (§7.4.3 verdetto) è argomento PA, non commerciale

I 4 argomenti citati (latenza, persistenza, sovranità, backup) sono **veri** ma solo il punto 3 (sovranità) è argomento PA decisivo, e solo per certi UC (Difesa, intelligence, infrastrutture critiche). Latenza è irrilevante per ~90% degli use case servizi territoriali (EO, monitoraggio non real-time). Persistence è argomento secondario (vs revisit migliorato Sentinel/Capella). Backup independent è argomento di nicchia.

**Implicazione**: il vero moat vs Starlink è **un singolo argomento** (sovranità dati PA) che vale per **una sottocategoria** di clienti (Difesa + alcune Regioni privacy-aware). Non vale per cooperative agricole né per generico PA. Cap. 7 va riscritto per essere onesto su questo.

### Critica C7.8. Cap. 7 §7.10 Fase 5 ARR €100-500M Y10 è incompatibile con base rate

Cap. 7 §7.10 cita "ARR target Fase 5 €100-500M (potenziale)". Cap. 11 Red Team Critica 5 (business-model-strategist) già confessa "100-400× in 7 anni è inverosimile". La risposta "scenario consolidamento standalone Y8 ARR €10-30M" è onesta ma **dovrebbe diventare baseline**, non scenario alternativo. La narrativa €100-500M è dannosa per la credibilità del documento verso investitori VC (paradossalmente, il rigore epistemico in §7.10 caveat protegge ma sottoutilizza).

### Critica C7.9. Mancanza analisi competitor Tier 3 operatori UAS-as-a-Service IT

Cap. 7 §7.4.4 elenca "Tier 3" con superficialità (FlyingBasket, Dronebee, ItaliaMeteo). In realtà:
- **FlyingBasket** (Bolzano) ha 100+ FTE, contratti pluriennali con Comuni e infrastructure manager, oltre €10M revenue annuo, opera già BVLOS in Alto Adige.
- **Dronebee + Globaldrone + Skygenetics** sono cluster operativi che concorrono frontalmente su contratti Regioni e PA su pricing 30-50% sotto Firmamento target.
- **e-GEOS (Telespazio + ASI)** è quasi un mostro: contratti decennali con tutte le Regioni IT, fornitura EO satellitare + analytics. Mappa l'intera Italia revisit settimanale.

Questi non sono "minaccia bassa". Sono il **competitor primario Y1** per qualunque contratto B2G regionale Firmamento provi a vincere. Il Cap. 7 li sottovaluta sistematicamente.

### Critica C7.10. Revenue Y1 €355-405k è top-down wishful, non bottom-up dei sales

Cap. 7 §7.8.2 dichiara "preliminare con confidence low" 6 linee servizio. Manca completamente:
- **Sales pipeline funnel**: quanti contatti, quante demo, quanti negoziazioni, quanti close attesi. Aerospace B2G ha conversion rates 5-15% lead-to-close. Per 5 contratti Y1, servono 30-100 lead qualificati.
- **Sales effort**: il team Firmamento ha 1 PM, no sales dedicato (vedi Cap. 7 §7.9.1 MVP scope). 1 persona part-time genererà 20-30 lead/anno realistici.
- **Cycle time**: gare PA IT 6-18 mesi tra avvio e firma contratto. Per chiudere 5 contratti Y1, devono essere avviati a M+0-3 minimo, idealmente già aperti.

Revenue Y1 €200k (soglia SyR-Cost-003) è raggiungibile con sforzo. €355-405k è ambizione. La differenza è critica per la viability.

---

## 5. Critiche al verdetto Cap. 10

### Critica C10.1. Hard conditions Go Condizionato 6A sono AND di probabilità basse

Cap. 10 §10.6 Critica 1 (red-team-skeptic interno) già ammette: 5 hard conditions AND = P(tutte) ~25-60%. La risposta "il punto del Go Cond. è esattamente questo" è formalmente corretta ma **statisticamente** significa che il verdetto realistico atteso al M+12 è **Hold** ~40-50% delle volte, non Go.

Implicazione: il piano operativo M+12 deve avere **piano B esecutivo per Hold** (non solo re-review tra 30 gg). Cap. 10 §10.3.3 elenca scenari alternativi (HOLD se C1 mancante etc.) ma non quantifica costi/conseguenze. In particolare:
- Se C1 (LoI Regione) manca, Hold automatico. Cap. 10 dice "cercare anchor alternative (Piemonte, Calabria)". **Quanto costa**? Cycle time 6-12 mesi. Firmamento ha cash per attendere?
- Se C3 (funding <40%), bridge financing. **Da chi**? Founder family + angels non hanno €500k disponibili rapidamente.

### Critica C10.2. Cap. 10 §10.7 "cosa NON facciamo" è strategicamente debole

L'elenco è onesto ma "**non concorriamo con Tier 1 globale HAPS in scala assoluta**" è CONTRADDITTORIO con boundary B2 "diventare nodo EU sovereign stratospheric layer". Se Y10 vuoi essere parte del consorzio EU, ti scontri inevitabilmente con AALTO + PHASA-35 + Skydweller per "chi è il leader". Il Cap. 10 dovrebbe esplicitare: "non concorriamo Y1-Y5; Y6+ siamo competitor diretti come parte del consorzio EU".

### Critica C10.3. Verdetto 6B Hold non risolve la "morte per cash"

Cap. 10 §10.4 Hold 6B = OK strategicamente, ma economicamente Phase B 6B costa €5.5-13.5M Y3-Y5 anche solo R&D. Cap. 11 §11.2.5 budget Fase 1 include "R&D Percorso 6B preliminare €100-300k Y1 + €200-500k Y2". È ragionevole, **ma** il vero costo del 6B preparatorio è in **bandwidth manageriale**: il CTO di Firmamento sta dividendosi tra MVP VTOL operativo e R&D HALE. Nel pratico, questo significa **MVP soffre**. Cap. 10 non quantifica questo trade-off.

### Critica C10.4. Verdetto 6B non considera "se AALTO/PHASA-35 dimostrano HAPS perennial 2027-2028, perché Firmamento serve?"

Cap. 10 §10.4.2 Argomenti No-Go rigettati: assenti gli argomenti competitivi. Mancano:
- "AALTO Zephyr 8 ha già 64 giorni di volo dimostrato 2018 e versione successor 2026; PHASA-35 operativo 2026. Cosa porta Firmamento al 2030+ che AALTO/PHASA-35 non offrono?"
- Risposta onesta: niente di tecnico (siamo behind). Solo "italianità + cooperative + sovranità IT". Cap. 10 dovrebbe dirlo esplicitamente: 6B Firmamento NON è first-mover tecnico, è "second source EU sovereign for political/geographical diversification".

### Critica C10.5. Decisione M+24 Phase B richiede capital structure resistente NON ancora pianificato

Cap. 10 §10.4.3 hard condition C-6B-2 "funding mix ≥ 50% committed (EDF + Horizon + PNRR / equity Series B) al M+24". 
- EDF call HAPS €100-300M next: 2027-2029 (Y2-Y4). Pubblicazione call non implica vincita.
- Horizon Cluster 4-5 HAPS: bandi 1-2 anni con probabilità vittoria ~10-20% per newcomer.
- PNRR Aerospazio: finisce 2026. Successor (NextGen EU + cohesion post 2027) non ancora definita.
- Series B €15-50M con valuation €30-80M pre-money richiede Series A chiusa Y2 con valuation crescente. Series A €3-8M con CDP anchor a M+24 è già stretch.

**Realisticamente** al M+24 il funding mix Phase B sarà 20-35%, non 50%. Trigger automatico ha esito Defer 6B a M+36 (Cap. 10 §10.4.4 scenario). Il "Hold" diventa "Defer permanente di facto".

### Critica C10.6. Manca scenario "Firmamento acquisita prima del Gate G5"

Cap. 10 §10.4 Hold 6B presuppone Firmamento indipendente fino M+24. Scenario Threat 1 (TAS-Leonardo acquisitive offer) può essere triggered a M+18-24, **prima** del Gate G5. Cap. 10 non considera: "che fa il CdA se a M+18 arriva offerta Leonardo €40M, founder ha lavorato 2 anni, MVP Y1 fa €250k revenue, Series A a stento closes a €3M?"

Realisticamente: CdA + sponsor (Coopfond, Regione) valutano "esit fair" come razionale. Cap. 10 dovrebbe esplicitare scenario di esit precoce e dichiarare la **postura del founder** (continua resistere vs accetta). Mancanza è gap di governance.

---

## 6. Critiche alla roadmap Cap. 11

### Critica C11.1. Capital intensity €10-30B Fase 5 è onesta ma narrativamente kamikaze

Cap. 11 §11.10 Red Team Critica 3 già lo ammette parzialmente: "narrativamente disastroso". La risposta "stratificazione tipi capitale per fase" è elegante ma non risolve il problema:

- VC al Series A che leggono lo Studio (e lo leggeranno, se trasparente) vedono "questa azienda dice che il full success scenario richiede €30B e programma EU che oggi non esiste". Confidenza scende.
- MIMIT che legge §11.6 sente "ambizione fuori scala per PMI early-stage". Probabilità grant Y2-Y3 diminuisce.
- Coopfond che legge sente "non finanziamo un'avventura speculativa". 

**Mitigazione possibile** (no opzioni magiche):
1. Spostare scenari capital intensity €10-30B in `RESERVED-rischi-geopolitici.md` o "visione strategica internal-only".
2. Cap. 11 pubblico chiude a Fase 4 con €100-500M capital intensity "small-medium fleet". Fase 5 diventa "EU consortium leadership" senza capital intensity quantificato.
3. Trade-off: perdi la disciplina epistemica (boundary B2 dichiarata onestamente come "vettore"). Diventi più "vendibile" ma meno onesto.

**Verdetto**: Cap. 11 è epistemicamente corretto ma commercialmente nocivo. Dilemma irrisolvibile senza compromesso.

### Critica C11.2. Stakeholder TAS-Leonardo come "co-lead Fase 5" è ingenuo

Cap. 11 §11.6.3 dichiara: "consorzio EU richiede accettazione di TAS-Leonardo come co-lead, non solo partner subordinato. Trade-off strutturale per evitare acquisition difensiva precoce". Cap. 11 §11.10 Critica 4 ammette frizione USA.

Realisticamente: TAS-Leonardo accetta di essere "co-lead" di Firmamento solo se Firmamento ha già **massa critica autonoma** (Series B chiusa, 3+ HAPS operativi, EU government backing). Senza, "co-lead" significa "Leonardo lead, Firmamento subordinato come spinoff".

Cap. 11 deve essere onesto: la cooperazione con TAS-Leonardo è strumentale ma **destinata a evolvere in subordinazione** quando il rapporto di forze diventa marcato. Non c'è uscita strategica nel mantenere Leonardo come "partner" oltre Series A senza diluirsi.

### Critica C11.3. Roadmap Fase 4 dipendenza EDF HAPS €50-200M è speculativa

Cap. 11 §11.5.4 EDF HAPS call 2030-2032 (Y6-Y8). EDF programma esiste, ma:
- EDF HAPS specifico **non è ancora annunciato** (M+0 maggio 2026).
- EuroHAPS (€43M EDF 2022-2024) era un demonstrator, non un programma operativo.
- Una hypothetical EDF HAPS €50-200M richiederebbe **lobbying paneuropeo** (IT + FR + DE + ES + PL) con buy-in MIMIT + ASI + Bruxelles. Firmamento non ha ancora questo network.
- Probabilità vittoria EDF call come lead per Firmamento (startup IT): ~5-15% (storia EDF: vincono prevalentemente Airbus, Leonardo, TAS, Indra, BAE, Saab).

Realisticamente: EDF HAPS Fase 4 vede participazione subordinata in consortium TAS-Leonardo-Airbus lead, con €5-15M (non €50-200M lead) per Firmamento. Non sufficiente a finanziare costellazione 3-10 HAPS.

### Critica C11.4. Roadmap Fase 1-2 milestone MS-F1-09 "Gate Fase 2" M+24 è troppo ottimistico

Cap. 11 §11.2.4 milestone MS-F1-09 = Gate Fase 2 al M+24 con criteri (Cap. 11 §11.3.5):
- ARR €1.0-1.5M Y2 (target medio del range)
- 2-3 UAS in fleet
- 10-15 FTE
- TRL HALE subsystems critici ≥ 5

Per arrivare a M+24 con questi numeri partendo da team 4 FTE M+3 e zero customers committed:
- Hiring 6-11 FTE in 21 mesi richiede compensation competitiva (aerospace senior IT €70-120k/anno) + ESOP. Cash burn implicato: €600k-1.5M solo personnel.
- 2-3 UAS in fleet richiede CapEx aggiuntivo €0.5-1M oltre MVP Y1.
- ARR €1.0-1.5M Y2 con 1 anno di operations + scaling significa 8-15 contratti firmati. Funnel sales ~80-200 lead. Capacity Firmamento Y1 senza sales team dedicato: ~30-50 lead. Gap factor 3-5×.

Realisticamente Y2 ARR €0.5-1M, fleet 1-2 UAS, team 8-12 FTE. Gate Fase 2 risulta parziale, Cap. 11 dice "KPI parziali = Hold scale-up". 

Cap. 11 dovrebbe scrivere il piano operativo Y1 backward dalla milestone M+24 e identificare le precondizioni Y1 "must achieve". Al momento Cap. 11 §11.2.4 è una lista aspirational, non un piano eseguibile.

### Critica C11.5. Fase 5 exit IPO Borsa Italiana STAR a €100-200M ARR Y10 è realistico solo se non sei stata acquisita prima

Cap. 11 §11.6.5 exit strategy IPO STAR come opzione 1. Pre-condizione "ARR ≥ €100-200M, ricorrente, multi-cliente, contratti pluriennali" è realistica se arrivi a Y10 con tutta la roadmap eseguita. **Ma** la roadmap Y1-Y9 ha 6 round di financing, ognuno con dilution. Founder ownership al M+96 Series C ~10-20% (anche con dual-class).

A quel punto, "IPO indipendente" è decisione del board (dominato da CDP + VC EU), non del founder. Probabilità IPO standalone vs strategic consolidation (opzione 2/3) sono 30/70 storicamente. Cap. 11 mette IPO come "preferred" ma in pratica il founder ha controllo limitato al M+96.

### Critica C11.6. Mancanza scenario "no boundary B2": cosa fa Firmamento se EU sovereign stratospheric NON si fa?

Cap. 11 dichiara boundary B2 non in discussione. **Ma** se EU sovereign HAPS programma non si materializza Y4-Y5 (Scenario D Wargame, P 50-60%), Cap. 11 non descrive la **traiettoria alternativa**: cosa fa Firmamento come operatore IT/Mediterraneo standalone, senza ambizione EU?

Risposta realistica probabile: Y8-Y10 sono 5-10 HAPS operativi cluster IT, ARR €30-80M, IPO STAR Milano. **Questa è una storia di successo onesta**, ma il Cap. 11 non la racconta, perché contraddice boundary B2. Risultato: lettori (investitori, sponsor) vedono solo la storia "EU sovereign €10-30B" che è speculativa, non la storia "Italian operator €30-80M ARR" che è realistica.

Mitigazione: Cap. 11 dovrebbe avere una sezione 11.X "Scenario B2-relaxed" che descrive la traiettoria standalone IT come outcome alternativo accettabile. Senza, lo Studio è binario: o boundary B2 si realizza, o tutto crolla.

---

## 7. Action items competitivi prioritari pre-Gate G3

In ordine di priorità competitiva (tutti vanno fatti tra M+3 e M+10):

1. **[M+3-6] Engagement Airbus AALTO preventivo**: MoU "Zephyr 8 use case Italia complementare". Trasforma threat 1 da nemico a partner formale. Trade-off: cede leadership narrativa. **NO regret** se eseguito intelligentemente.

2. **[M+3-6] Benchmark pricing PA italiana brutale**: Visit a e-GEOS, Planetek, NHazca per contratti reali Regioni IT (Puglia, Sardegna, Liguria). Riallinea Cap. 7 §7.8.2 a pricing reale. Probabile risultato: revenue Y1 baseline scende a €280-340k. **Necessario** per credibilità Cap. 7.

3. **[M+6-9] Capital structure resistente prima di Series A**: Dual-class shares + golden share preview Dipartimento Coordinamento Politiche Economiche. Cap. 11.10 action item, va elevato a "must have prima del primo equity". **Senza, Threat 1 vincoluto**.

4. **[M+6] LoI Regione Liguria hard binding**: Non solo "intent letter" ma "DGR formale con commitment budget FESR/FSE €200-400k Y1". Cap. 10 hard condition C1. **Senza, gioco finito**.

5. **[M+3-9] Eliminazione UC-003/008 connettività come anchor revenue**: Revisione Cap. 7 §7.2.2 e §7.8.2 per declassare connettività a "opportunistico". Cap. 1 §1.2.4 criticità C-2/C-3 ri-framed. Honesty win, immune to Threat 2 Starlink.

6. **[M+3-12] Pipeline funnel sales bottom-up**: Costruire CRM con 50-100 lead qualificati B2G/B2B entro M+6. Conversione 5-15% lead-to-close. Identificazione di 1 sales dedicato Y1 (anche part-time). **Senza, revenue Y1 fictional**.

7. **[M+3-9] Pre-application ENAC con feedback documentato**: Hard condition C5 Cap. 10. Riduce P(Scenario E) da 30-45% a 15-25%. **Necessario**.

8. **[M+6-12] Position paper "Italian Stratospheric Sovereignty" con timing accurato**: NON pubblicare prima di M+12 (Threat 3 trigger). Da redigere internamente entro M+9, pubblicazione M+12-15 con buy-in MIMIT preliminare. Apre Cap. 11 boundary B2 narrative responsabilmente.

9. **[M+6-12] Mappa Early Warning Indicators competitivi attivata**: Monitor mensile: AALTO press releases, EuroHAPS-2 call, IRIS² consortium announcements, EU Stratospheric programma policy. Trigger automatico Red Team review se EWI scatta.

10. **[M+9-12] Decisione esplicita engagement TAS-Leonardo**: Timing, perimetro, line-in-the-sand su equity diretto. Cap. 11.10 action item, deve essere documento di governance approvato CdA. **Senza, exit forzato a Y3-Y4**.

---

## 8. Survivability final assessment

### Domanda: Firmamento sopravvive a Y10 come entità indipendente?

**Risposta cinica**: **No, salvo esecuzione eccezionale (probabilità <15%).**

Scenario probability tree:

| Outcome Y10 | Probabilità | Condizioni necessarie |
|---|---|---|
| **Standalone EU leader stratospheric** (boundary B2 piena, ARR €100-500M, consortium EU lead) | <5% | Tutti gli scenari A-F mitigati + programma EU sovereign aperto Y4-Y5 + Series A-B-C tutte chiuse a valutazioni crescenti + capital structure resistente preservata + IPO STAR Y10 |
| **Standalone IT operator** (boundary B2 ridimensionata, ARR €30-80M, 5-15 HAPS cluster IT, IPO STAR locale) | 10-15% | Mitigazione Scenari A, C, E + capital structure resistente + Series A-B chiuse + accettazione Fase 5 EU non realizzata |
| **Acquisita "fair value"** (founder out con golden share, asset in EuroHAPS-successor, boundary B1 simbolicamente preservata) | 45-55% | Threat 1 si materializza Y3-Y5 + offerta €30-100M + CdA + sponsor valutano razionale |
| **Acquisita "stress"** (founder out a valutazione bassa €10-30M, dopo Series A fallita o scale-up sotto target) | 15-25% | Combinazione Scenari A + E + Series A non chiusa → cash runway esaurito → exit obbligato |
| **Dissoluzione** (cash burnt out, asset liquidati, IP venduta a scrap) | 5-10% | Combinazione catastrofica: ENAC blocca SORA + Regione retreats + Starlink saturation totale + Coopfond non rinnova |

**Condizioni esplicite per scenario "Standalone IT operator" (l'outcome onesto migliore realistico):**

1. Eseguire le 10 action items §7 **integralmente** entro M+12.
2. Accettare boundary B2 ridimensionata: Fase 5 EU sovereign è vettore narrativo, non target operativo.
3. Capital structure resistente messa in piedi PRIMA del Series A (M+18-24): dual-class + golden share preview + CDP anchor.
4. Engagement Airbus AALTO preventivo per neutralizzare Threat 3 (trade-off accettato: cede leadership narrativa per acquisire safety).
5. Series A chiusa entro M+30 con valuation €15-25M pre-money. Investor mix: CDP Venture Capital + EIC Fund + LIFTT + 1-2 family office italiane. NO investitori esteri non-EU.
6. Y3 ARR €1.5-2.5M (realistico, sotto target Cap. 11 €2-5M). Cap. 11 va revisionato.
7. Y6-Y8 ARR €15-40M con 2-5 HAPS operativi cluster Mediterraneo (Sardegna + Sicilia + Puglia + Liguria). Series B chiusa €8-20M (non €15-50M Cap. 11).
8. Y10 IPO STAR a market cap €100-300M (founder ownership residua 8-15%, golden share italiana).
9. **NO** consortium EU lead. **NO** programma EU sovereign €10-30B. Accettazione che boundary B2 si realizza come "Italian leadership in EU stratospheric services within EU multi-orbit architecture" (narrativa, non infrastruttura €30B).

**Condizioni per "Standalone EU leader" (<5%):**
- Tutto quanto sopra, **più**
- Programma EU sovereign HAPS aperto Commissione UE 2030-2032 (P ~30-40%, fuori controllo Firmamento)
- Firmamento riconosciuta come lead italiano nel programma (richiede networking Bruxelles strutturato dal M+12, P ~30-50% se attivato)
- Series C €30-100M chiusa Y8 con sovereign EU + EIB anchor
- Founder team resiste 10 anni senza esit forzato

**Probabilità "Standalone EU leader"**: 0.4 × 0.4 × 0.6 × 0.6 ≈ 6% (e siamo generosi). Confidence: high sul calcolo, low sulle probabilità individuali.

---

## Final verdict

Lo Studio di Fattibilità è **strutturalmente solido** sul Percorso 6A pilota Pentema con verdetto Go Condizionato (Cap. 10), può funzionare e generare un'azienda di servizi onesta scala IT con ARR €30-80M a Y8-Y10. Le 7 action items prioritarie §7 sono **necessarie ma probabilmente non sufficienti** per il survival standalone.

Sul Percorso 6B HALE stratosferico e sulla boundary B2 EU sovereign (Cap. 11) lo Studio è **epistemicamente onesto ma operativamente fragile**: la roadmap dichiara le dipendenze esterne (EU programma sovrano, batterie 350 Wh/kg, EASA Special Condition) ma non offre piano credibile per realizzarle. Realisticamente Phase B 6B inizia con funding mix ~25-35% al M+24 (non 50% richiesto), gate G5 risulta Defer, Firmamento si attesta su scala "operator IT" senza scala EU.

L'output più probabile a Y10 è **acquisizione difensiva da TAS-Leonardo a Y3-Y5** (~50% probabilità). La contromossa principale è **capital structure resistente messa in piedi PRIMA del primo round equity esterno**, non dopo. Cap. 11.10 lo flag ma come "action item Y1", deve essere elevato a **precondizione assoluta del Series A**.

La boundary B2 EU sovereign è vettore strategico onesto. La traiettoria realistica per realizzarla passa attraverso (1) eccellenza esecutiva Y1-Y3 (improbabile ma non impossibile), (2) consolidamento standalone IT Y4-Y6 (probabile se Y1-Y3 OK), (3) leadership EU consortium Y7-Y10 (improbabile ma vivo solo se Y4-Y6 dato). La probabilità di completare tutti e 3 i passi: ~6%. La probabilità di completare i primi 2: ~15-20%.

**Raccomandazione operativa finale del Red Team competitivo**: 
- Approva Cap. 10 verdetto Go Condizionato 6A.
- Riconfigura Cap. 7 con pricing reale benchmark e UC-003/008 declassati (action items #2, #5).
- Riconfigura Cap. 11 con scenario "B2-relaxed" esplicito (critica C11.6).
- Eleva capital structure resistente a precondizione assoluta Series A (action item #3).
- Engagement Airbus AALTO preventivo entro M+6 (action item #1).
- Pre-application ENAC documentata entro M+6 (action item #7).
- Pipeline sales bottom-up entro M+6 (action item #6).

L'alternativa (status quo Cap. 7/11) ha probabilità sopravvivenza standalone <15%. Esecuzione delle 10 action items la porta a 20-30%. Boundary B2 EU sovereign rimane <10% probability di realizzazione, ma è OK dichiararlo come vettore.

Game on. Il timer è già partito.
