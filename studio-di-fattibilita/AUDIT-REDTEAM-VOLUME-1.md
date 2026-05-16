# Audit Red Team — Volume 1 Studio di Fattibilità

> **Autore:** agente `red-team-skeptic`
> **Data:** 16 maggio 2026 (M+3)
> **Scope:** stress-test avversariale globale del Volume 1 (Cap. 0-11)
> **Boundary conditions non attaccate:** B1 (cooperative + service-only), B2 (vettore EU sovereign)
> **Disciplina applicata:** Regole 1-7 di `epistemic-rigor` + 4 tecniche di `red-team-skeptic` (pre-mortem, falsificazione popperiana, base-rate, steel-manning)
> **Stile:** brutale, fattuale, niente diplomazia

---

## 0. Verdetto sintetico

**Il documento regge con caveat strutturali pesanti.** Il Volume 1 è metodologicamente onesto su confidence levels, falsifying observations e capital intensity (raro per documenti aerospace early-stage). Ha 4 difetti strutturali che lo rendono **non investment-grade** al M+11 nello stato attuale:

1. **Il verdetto "Go Condizionato 6A" è una postura, non una decisione**: AND di 5 hard conditions con P~50-70% ognuna → P(tutte) realistica 15-35%. Il documento ammette il problema (Cap. 10 §10.6 Critica 1) ma lo classifica come feature, non come bug.
2. **Tre claim cifrati critici sono single-source commerciali declassificati a "low" — eppure tutto il business case Y3-Y5 si appoggia su di essi** (TAM/SAM, pricing PA, willingness-to-pay).
3. **La separazione "decisione Y1-Y3" vs "vettore strategico Y4-Y10" è dichiarata ma non operativa**: il documento mescola continuamente capital intensity Y1 (€0.7-1.2M) con scenari €10-30B Fase 5, creando confusione narrativa e regalando munizioni a chi vuole rigettare lo Studio "perché parla di €30B".
4. **L'esecuzione M+0-M+3 mostra debito di rigore non chiuso**: gli stessi capitoli citano DR-002, DR-004, DR-007, DR-012 ancora aperti, ma il verdetto Cap. 10 viene proiettato come Go Cond. La proiezione è basata su action items che la storia aerospace dice non si chiudono nei tempi.

Il documento non è "non regge" perché ha un livello di onestà metodologica superiore a 90% degli studi di fattibilità aerospace early-stage italiani. Ma non è ancora "regge" perché le critiche sopra non sono affrontate, sono **dichiarate e accettate**.

---

## 1. Critiche GLOBALI al Volume 1 (top 10 lacune trasversali)

### Critica G-01 — Proiezione M+11 da M+3: il verdetto del Cap. 10 è scritto come se le evidenze fossero acquisite
**Razionale:** Cap. 0, 10, 11 sono datati "bozza M+11 proiezione" mentre Cap. 1-9 sono "bozza M+3". Il verdetto **Go Condizionato 6A** è formulato come decisione, ma le evidenze chiave (LoI Regione, SORA feedback, mix funding 60% committed, 8/10 cooperative formali) non sono raccolte. Si sta votando il risultato di un esame che non si è ancora dato.
**Risposta attesa:** "È una proiezione metodologica, non un verdetto effettivo". Allora il documento dovrebbe essere **rietichettato come 'piano di lavoro per il gate M+11'**, non 'Studio di Fattibilità completo'.
**Action item:** Distinguere visivamente nei file tra "stato evidenziale M+3" e "verdetto target M+11 sotto condizioni". Aggiungere a Cap. 0 una tabella "evidenze attuali M+3 vs evidenze necessarie M+11".

### Critica G-02 — Mancata triangolazione su numeri di mercato (single-source commerciale)
**Razionale:** TAM HAPS €99-240M (Cap. 7.3.1) viene da MarkNtel + Coherent + Grand View — tutti report commerciali, nessuno triangolato con AIAD, Eurospace, EUSPA, ITU. Il documento lo dichiara confidence "low" (audit-rigore-epistemico.md DR-007/012), ma poi costruisce SAM/SOM/ARR/NPV Y3-Y5 derivando da questo TAM "low".
**Risposta attesa:** "Confidence è dichiarato basso". Sì, ma il piano economico e la decisione Go Cond. dipendono da queste cifre.
**Action item:** Triangolare TAM-IT con AIAD Annual Report + Eurospace Facts & Figures + ITU 2024 prima del M+10. Senza, declassificare il Cap. 7 a "preliminary indicative" e il Cap. 8 NPV/IRR a "scenario qualitativo".

### Critica G-03 — Survivorship bias dichiarato ma non quantificato
**Razionale:** Cap. 7.1.2 cita correttamente Helios, Aalto HAWK30, Solara 50, Sanswire come programmi falliti. Cap. 10.6 critica 4 lo richiama. Ma in **nessun punto del documento** si applica una base rate aggiustata ai planning. Esempio: se il base rate "HALE solare → operativo commerciale" è <30%, perché lo Studio approva Phase B €5.5-13.5M con confidence medium come se fosse 70%?
**Risposta attesa:** "Phase B è R&D, non operativo commerciale". Errato: i €5.5-13.5M sono soldi reali bruciati se la base rate ci colpisce.
**Action item:** Per ogni gate (M+12, M+24, M+36, M+48), dichiarare probabilità Bayesian condizionata alla base rate aerospace (es. P(go al M+48 | go al M+24) = base_rate × evidence_update). Aggiungere a Cap. 9 + Cap. 11.

### Critica G-04 — Assenza di "kill criteria" formali per ciascun gate
**Razionale:** Il documento usa diffusamente "Go / Go Cond. / Hold / No-Go", ma i **No-Go criteria** sono vaghi ("showstopper insuperabili"). Cap. 3.2 falsifying observation: "≥30% criteri non soddisfatti = HOLD; No-Go solo per showstopper insuperabili". Cosa è "insuperabile"? Quanto tempo di Hold prima del No-Go automatico? Senza kill criteria duri, il progetto rischia di restare in zombie state per anni (esattamente come Helios, Solara, Sanswire).
**Risposta attesa:** "Hold significa re-review 30-60 giorni". OK, ma quante Hold prima di chiamare il No-Go?
**Action item:** Aggiungere a Cap. 9 una **escalation matrix**: dopo X Hold consecutivi su criterio Y → No-Go automatico. Esempio: "3 Hold consecutivi su LoI Regione = No-Go scale-up Liguria, pivot Piemonte". Senza, il documento è troppo morbido.

### Critica G-05 — Confusione concettuale "feasibile / fattibile / operativo" (Errore 6 della skill epistemic-rigor)
**Razionale:** Cap. 10 §10.3.1 dice "tecnicamente, regolatoriamente, di mercato e finanziariamente fattibile". Cap. 5 §5.4.2 dice "operazioni civili continuative non esiste alternativa alla Certified Category". Cap. 6 §6.0.1 dice "GO tecnicamente". Il termine **"fattibile"** è usato per "il design lo permette" (Cap. 6), "il regolatore lo autorizzerà se gli chiediamo bene" (Cap. 5), "il NPV è positivo nel scenario base" (Cap. 8) — tre cose diverse. Conseguenza: la conclusione "6A pienamente fattibile" maschera che è "feasibile + tecnicamente fattibile + non ancora regolatoriamente autorizzato + non ancora economicamente sostenibile".
**Risposta attesa:** "Il documento dichiara le condizioni del Go Cond.". Sì, ma il linguaggio del verdetto sintetico è imprecise.
**Action item:** Riformulare Cap. 0 e Cap. 10 con le 6 categorie distinte (feasibile, tecnicamente fattibile, operativamente fattibile, regolatoriamente autorizzabile, economicamente sostenibile, operativo). Esempio: "6A è tecnicamente e regolatoriamente plausibile, economicamente sostenibile in scenario base, ma operativamente fattibile solo se LoI Regione + SORA approvato; non operativo fino M+12".

### Critica G-06 — Le boundary conditions B1+B2 sono usate come scudo contro la critica
**Razionale:** Cap. 1.0bis, Cap. 2.0bis, ... Cap. 11.0bis — tutti ripetono "B1 e B2 non sono soggette a stress-test epistemico". Esatto, ma:
1. Le critiche legittime su "come si argomenta B1+B2" sono confinate al `RESERVED-rischi-geopolitici.md`, fuori dello Studio pubblico.
2. Cap. 7.13 Critica 2 sul "modello cooperativo come limitazione" viene affrontata con difese tautologiche ("è scelta strutturale del progetto, non in discussione"). Steel-manning vero? No.
3. Il framing "complementare a IRIS²" è ripetuto compulsivamente (~25 occorrenze nel Vol. 1) come mantra. Mantra non sono argomenti.
**Risposta attesa:** "Le boundary sono input strategici, non output da validare". Vero per il **se** B1+B2; falso per il **come**.
**Action item:** Aggiungere a Cap. 1 e Cap. 7 una sezione **"Limiti delle boundary conditions"** che esplicita: in quale scenario futuro B1+B2 andrebbero rivisitate (es. "se al gate M+36 il modello cooperativo non riesce ad attrarre Series A perché VC chiedono ownership > 51%, B1 va rinegoziato").

### Critica G-07 — Capital intensity €10-30B nello stesso documento del CapEx Y1 €0.7-1.2M
**Razionale:** Cap. 0.4, Cap. 0.11, Cap. 7.10, Cap. 8.0.3, Cap. 11.6.4 — tutti citano €500M-2B (small fleet) o €10-30B (full scale EU sovereign). Anche con tutte le dichiarazioni di "precondizione esterna", **il primo grafico/tabella che un lettore poco attento vede è la cifra €30B**. Il lettore VC chiude lo Studio. Il lettore PA pensa "questi sognano". Cap. 10.6 Critica 3 lo dichiara ma la risposta è insufficiente.
**Risposta attesa:** "Il rigore epistemico richiede onestà". Vero. Ma onestà ≠ pessima comunicazione strategica.
**Action item:** **Spostare** capital intensity Y8-Y10 dal Volume 1 al Volume 2 Allegato "Vettore strategico". Cap. 0, 7, 8, 11 citano capital intensity Y1-Y5 con ARR cumulato Y5 (€3-8M). Sezione "Visione 10 anni" del Cap. 11 fa riferimento a un allegato separato per scale future. Disaccoppia narrativamente decisione attuale (Y1-Y3) da vettore (Y4-Y10).

### Critica G-08 — Mancanza di benchmark "do nothing" / "wait and see"
**Razionale:** L'art. 41 D.Lgs. 36/2023 richiede esplicitamente confronto con **ipotesi di non realizzazione**. Cap. 1.4 lo cita una volta. Cap. 6.3 (trade study) confronta solo alternative architetturali. **Nessuna sezione confronta seriamente "Firmamento avvia 6A ora vs Firmamento aspetta 12 mesi e impara da pilot competitor"**. La pressione narrativa è "go now". È un caso classico di sunk-cost (i 10 mesi di Studio investiti) che spinge verso Go.
**Risposta attesa:** "Cap. 7.13 dichiara competitor reale". Vero, ma non c'è un'alternativa "do nothing M+12" valutata.
**Action item:** Aggiungere a Cap. 10 una **opzione "Defer 6A 12 mesi"** con razionale (vedere primo cliente JOUAV in Europa muoversi, vedere Aalto JV-Leonardo, vedere quale Regione tra Liguria/Piemonte/Marche apre prima bando FESR rilevante). Comparare onestamente "Go ora" vs "Defer 12 mesi".

### Critica G-09 — Trade study chiave (TS-PLATFORM-6A) declassificato a "preliminary" ma è la decisione strutturale
**Razionale:** Cap. 6 §6.0.2 dichiara TS-PLATFORM-6A con confidence "medium" e raccomandazione JOUAV CW-30E. Cap. 8 dimensiona CapEx su JOUAV (€280-460k). Cap. 0.2 cita "JOUAV CW-30E baseline con Plan B Tekever AR3". La scelta è **già nel verdetto** ma il trade study è **preliminare**. Questo è un caso di **decisione data per fatta che pretende di essere trade study**.
**Risposta attesa:** "JOUAV è benchmark, scelta finale è M+10". OK, ma allora perché Cap. 0 e Cap. 10 (M+11 proiezione) hanno JOUAV come baseline?
**Action item:** Esplicitare in Cap. 6 §6.0.2 che la scelta JOUAV è **provvisoria e che il vero gate sarà M+10 dopo quotation Tekever**. Senza, il trade study è teatro.

### Critica G-10 — Engagement EASA HAPS è "in dialogo informale" — tutto il Percorso 6B dipende da questo
**Razionale:** Cap. 5 §5.4.2 + Cap. 10 §10.2.1 dichiarano RSK-REG-001 (mancanza framework HAPS EU) come **showstopper rosso**. Cap. 11 §11.9.1 dice "engagement EuroHAPS + ASD-Eurospace". Cap. 9.2.x dice "engagement EASA Innovation Network M+6-9". Lo stato evidenziale attuale (M+3): **zero contatti formali EASA**. Eppure il gate G3 (M+10/M+11) deve dare un verdetto "Hold/Go Cond. Estremo R&D" su 6B basato su che cosa? La speranza che dialogue informale produca apertura RMT entro M+24?
**Risposta attesa:** "Hold significa esattamente questo: aspetta evidenze". Vero, ma allora Phase B 6B M+24-48 (€5.5-13.5M) è un Hold subordinato a una condizione esterna (RMT EASA) totalmente fuori dal controllo Firmamento.
**Action item:** Cap. 5 + Cap. 10 + Cap. 11 devono dichiarare **timeline realistica EASA RMT HAPS**: base rate apertura RMT EASA in domini novel = 3-7 anni dalla prima proposta industriale. Probabilità RMT aperto entro 2030 = stimata, con fonte. Se < 50%, il Percorso 6B è di fatto **post-2030**, non M+24-48.

---

## 2. Critiche PER CAPITOLO

### Cap. 0 — Sintesi Esecutiva

- **Critica 2.0.1:** §0.11 dichiara "Falsifying observations dichiarate: ~40 (totale Volume 1)" senza link a registro tracciabile. Affermazione non verificabile.
- **Critica 2.0.2:** §0.11 dichiara "Citazioni autoritative: ~200" — numero senza tipologia/distribuzione. Quante sono peer-reviewed vs vendor vs press? Senza breakdown, è metric vanity.
- **Critica 2.0.3:** §0.4 cita "€500M-€2B scenario small fleet / €10-30B EU sovereign full scale" nella Sintesi Esecutiva di 5-8 pagine. Decisione strategica errata di comunicazione (vedi Critica G-07).
- **Critica 2.0.4:** §0.3 verdetto 6A elenca 5 hard conditions tutte al M+9-10. Se ognuna ha P~70%, P(tutte)~17%. Lo Studio sostanzialmente sta dicendo "abbiamo 17% di chance di arrivare a Go al M+11" senza ammetterlo apertamente.
- **Critica 2.0.5:** §0.7 stakeholder critici elenca CIRA con "LoI entro M+9-12" — al M+3 zero contatti formali risultano. Optimism on naked schedule.
- **Critica 2.0.6:** §0.14 verdetto in una riga preserve "complementare a IRIS²" come slogan. Nessun documento Commissione UE / DG CNECT / DG DEFIS ha mai usato HAPS come "complementare IRIS²". È auto-narrativa.

### Cap. 1 — Inquadramento (Quadro Esigenziale)

- **Critica 2.1.1:** §1.1.1 dichiara "PMI italiana early-stage" + "nessuna piattaforma in volo operativo, nessun servizio ricorrente in essere". Onestà OK. Ma il resto del capitolo presenta engagement Regione, ENAC, Coopfond, 10 cooperative come fait accompli. **Status reale al M+3: 10 cooperative identificate, LoI in raccolta** (§1.1.2 caveat). Gap tra "early-stage senza track record" e "rete istituzionale consolidata" è troppo largo.
- **Critica 2.1.2:** §1.1.2 "l'identità nominale delle 10 cooperative è dato sensibile commerciale" — gli stakeholder di gate (Coopfond CdA) vorranno vedere i nomi prima di approvare €50-300k. Senza nomi, è "cooperative anonime".
- **Critica 2.1.3:** §1.2.3 Pentema "rappresentatività generalizzabile per analogia alle altre 7 aree SNAI Liguria e alle 71 aree SNAI nazionali" — analogia debole. Pentema 1100 m s.l.m., orografia appenninica. Aree SNAI Calabria/Basilicata sono diverse. La pretesa di generalizzazione è speculativa.
- **Critica 2.1.4:** §1.2.4 criticità C-2 "Digital divide" è seriamente sfidata dal PNRR 1 Giga (€6.7B) + 5G PNRR (€2B). Cap. 1 falsifying obs §1.2.4 lo ammette. Ma poi tutta la value proposition Cap. 7 si appoggia ancora su digital divide. Coerenza interna debole.
- **Critica 2.1.5:** §1.3.2 tabella comparativa HAPS vs LEO vs GEO è **wishful thinking sui costi**: "€5-50M/HAPS (stima)" — la stima Airbus interna Zephyr era €15M/unità nel 2018, scaled-up con inflazione + complexity Italia: €25-60M realistici. Sottostima 2-3×.
- **Critica 2.1.6:** §1.7 "Coerenza con cornice ENAC AAM" — il Piano AAM ENAC NON include HAPS (lo Studio lo ammette). La pretesa "convergenza istituzionale rilevante" è argument by association.

### Cap. 2 — Stakeholder e SMART

- **Critica 2.2.1:** §2.4.5 obiettivi V10-* sono "direzionali", dichiarato esplicitamente. OK metodologicamente, ma li si lascia comunque nel capitolo. Effetto: il lettore VC vede V10-04 ARR €30-80M Y8 e o ci crede (sopravvaluta) o non ci crede (sottovaluta tutto il documento). Better: spostarli a Cap. 11.
- **Critica 2.2.2:** Stakeholder S-23 (Leonardo/TAS/Telespazio) classificato "Manage Closely" con "Power High, Interest Medium (ambiguo)". Più realistico: "Power High, Interest **High** (hanno tutto da perdere se Firmamento riesce su layer stratosferico italiano)". L'ambiguità è ottimismo.
- **Critica 2.2.3:** Top-5 stakeholder (§2.2.3) include "ASL3 Genovese" come cliente telemedicina. Telemedicina UAV in Italia ha base rate di adozione **molto bassa** (zero contratti operativi paganti documentati 2025-2026). Sovrastima dell'interest.
- **Critica 2.2.4:** Obiettivo 6A-04 "≥ 5 contratti pluriennali firmati M+24" con soglia minima 3. La storia delle aerospace startup italiane (Sky-Tech, AVIORS, etc.) mostra che ottenere 5 contratti pluriennali PA in Y1 è raro. Soglia minima 3 più realistica, ma anche 3 contratti pluriennali in 12 mesi è ambizioso. Confronto con base rate aerospace IT mancante.
- **Critica 2.2.5:** §2.5.2 vincoli finanziari ripetono "€500M-€2B (small fleet) → €10-30B (EU sovereign)" anche nel capitolo stakeholder. Reiterazione non necessaria, amplifica il problema G-07.
- **Critica 2.2.6:** §2.6 critica Red Team 4 ammette che AS-001 (Regione Liguria fino M+24) è wishful thinking. Risposta cita "elezioni regionali 2025 effettive". Liguria ha avuto elezioni regionali ottobre 2024 (Bucci presidente). La Giunta attuale ha priorità diverse da Bucci (centrodestra vs Toti centrosinistra ex). Il capitolo non aggancia mai esplicitamente "il nuovo Presidente Liguria conosce SNAI e PSNAI?". Lacuna fattuale.

### Cap. 3 — Requisiti e RTM

- **Critica 2.3.1:** §3.1.2 "Subsystem Requirements (SsR): ~80 (sample, ~200 in v1.0)". 200 SsR per uno Studio di Fattibilità M+11 è **troppo dettagliato per Phase A**. NASA SE Handbook §6.7 colloca SsR a Phase B-C, non Phase A. Sovrascopo metodologico.
- **Critica 2.3.2:** §3.2 criteri Go/No-Go sono ben articolati, ma falsifying observation Gate M+10 dice "No-Go solo per showstopper insuperabili". Non c'è kill criterion quantitativo (vedi Critica G-04).
- **Critica 2.3.3:** §3.3.1 stakeholder map ha 26 stakeholder (Cap. 3) vs 30 (Cap. 2). Cap. 2 estende; OK come metodologia, ma il documento ha **due tabelle stakeholder leggermente diverse**, source of confusion.
- **Critica 2.3.4:** SyR-Cost-003 (Revenue Y1 ≥ €200k) è citato in 8 punti del Volume 1 come "minimum viable threshold". Ma non è triangolato con willingness-to-pay reale di Regione Liguria. Single-point requirement.
- **Critica 2.3.5:** RTM v0.5 baseline (§3.0) è dichiarato. Quanti orfani? Quanti SyR senza SsR? Senza dato, "RTM completa" è opinione.

### Cap. 4 — Scope e ICD

- **Critica 2.4.1:** §4.2.1 dominio C-02 (SORA application formale completa SAIL III) è OUT. Coerente con scope PFTE M+11. **Ma** Cap. 9 G3 entry criterion include "Autorizzazione SORA ENAC operativa entro M+9". Contraddizione interna: lo Studio dichiara SORA OUT, poi la rende prerequisito Go.
- **Critica 2.4.2:** §4.3.1 17 deliverable PFTE per €150-300k budget Coopfond + 11 mesi = ~€8-18k per deliverable medio. Ridicolmente sottostimato per deliverable come DEL-PFTE-12 (Quadro Economico + Computo Metrico Estimativo + Piano Finanziario completo) che industria standard costa €30-60k.
- **Critica 2.4.3:** §4.3.2 deliverable Fase 1 include "SORA application formale ENAC (SAIL III)" come DEL-F1-04 M+18-22. **Ma** Cap. 10 hard condition C2 dice "SORA ENAC operativa entro M+9". Inconsistenza temporale.
- **Critica 2.4.4:** §4.1.5 lista "cosa NON è fattibilità" è lunga e onesta. Bene. Ma poi §4.5 (criteri scope acceptance) e Cap. 9 reintroducono LoI Regione Y1 + SORA approvato M+9 come if-then per Go. Scope creep nascosto.
- **Critica 2.4.5:** §4.4 ICD a 20 interfacce è dichiarato "preliminare". OK. Ma alcune sono critiche (es. INT-ENAV per integrazione U-Space) — il documento non chiarisce se l'ICD preliminare ha avuto **input da ENAV** (probabilmente no al M+3).

### Cap. 5 — Quadro Normativo

- **Critica 2.5.1:** §5.4.1 Percorso 6A SAIL II-III stima. Falsifying obs (§5.1.5) dice "se ENAC valuta GRC ≥ 6, SAIL salta a IV o V, costi × 3-5, tempi raddoppiati. Probabilità: M". Lo Studio accetta P=M (medium = ~30-50%) di failure mode che fa fallire l'intero CapEx 6A. **Eppure il verdetto è Go Cond.** Non si fa Go Cond. su uno scenario con 30-50% di chance di blow-up del piano.
- **Critica 2.5.2:** §5.4.2 Percorso 6B "Special Condition negoziata caso per caso". Storia EASA: nessuna Special Condition HALE solare civile è mai stata negoziata. PHASA-35 (UK) è gestita in test campaign con MAA UK, non EASA. Zephyr è gestita in Australia/Kenya. **Nessun precedente civile EU**. La "negoziazione" è quindi pioneering — base rate di successo per pioneering certification path = molto bassa, tempi 7-10 anni storici.
- **Critica 2.5.3:** §5.2.3 stato U-Space Italia: prima area U-Space attiva R100 San Salvo (Abruzzo) 28 novembre 2025. Pentema (Liguria) non è in lista. Lo Studio cita questo come "framework esistente"; in realtà l'U-Space su Pentema è da **istituire ex novo** se serve. Cap. 5 non esplicita timeline + costi di istituzione.
- **Critica 2.5.4:** §5.1.5 SAIL atteso II-III "stima preliminare, basata su analogia con autorizzazioni precedenti italiane, non validata da ENAC". Quale analogia? Quale operatore italiano ha già SAIL II-III BVLOS in zona simile a Pentema? Senza precedente, l'analogia è ipotesi.
- **Critica 2.5.5:** Cap. 5 ha confidence "high" su tutte le norme. Vero per il testo della norma; **falso** sull'interpretazione applicativa che ENAC darà a Pentema. Confondere "conosciamo il testo del regolamento" con "sappiamo come ENAC lo applicherà al nostro caso" è errore epistemico.

### Cap. 6 — Analisi Tecnica

- **Critica 2.6.1:** §6.0.2 trade study TS-PLATFORM-6A confidence "medium" + raccomandazione JOUAV (vedi Critica G-09).
- **Critica 2.6.2:** §6.0.2 TS-PROP-6B confidence "medium-low" per architettura energetica HALE. Eppure questo trade study definisce se Percorso 6B può esistere o no. Confidence medium-low ≠ base sufficiente per "Hold con commitment Phase B €5.5-13.5M".
- **Critica 2.6.3:** §6.1.1 piattaforma JOUAV CW-30E "TRL 8-9 (commerciale)" — **TRL secondo vendor cinese**. NASA TRL ≠ EASA TRL ≠ CAAC TRL. Cap. 5 stesso dice che JOUAV è categorizzato cinese, non EASA. L'analogia 8-9 EASA è speculativa.
- **Critica 2.6.4:** §6.1.2 HALE TRL attuale 3-4, target Phase B = 5-6. Passare da TRL 3-4 a TRL 6 in 24 mesi con €5.5-13.5M è ottimistico. Base rate aerospace passaggio TRL 4→6: 3-5 anni, €15-50M. Lo Studio sta proponendo half of typical budget in half of typical time.
- **Critica 2.6.5:** §6.1.3 "Riuso medio asset 6A → 6B: ~60%". Stima dichiarata "Y3+ asset riusabili". La tabella mostra **brand 100%, cloud 100%, autorizzazioni 70%, payload 30%, avionica 0%, piattaforma 0%**. Media ponderata reale (su CapEx €): probabilmente 25-35%, non 60%. Sovrastima del riuso.
- **Critica 2.6.6:** §6.2.2.2 energy balance estate 44°N margine 370% suspicious. Il calcolo usa 25 m² pannelli × 12 kWh/m²/giorno × η 30% = 90 kWh/giorno vs consumo 19.2 kWh/giorno. **Ma**: η 30% è cella, non sistema (cabling, MPPT, temperature derating riducono 15-25%). Consumo P_cruise stimato 0.5-1.0 kW è ottimistico per HALE 80-150 kg (più realistico 0.8-1.5 kW). Energy balance estate corretta probabilmente 200-280%, non 370%. Ancora positiva, ma il margine dichiarato è inflated.
- **Critica 2.6.7:** §6.2.2.2 energy balance inverno è troncato nella lettura ma RSK-TEC-001 "margin 0-15%" è dichiarato. **0% margin** significa **non vola** in inverno con tech 2026. Il "fallback seasonal-only marzo-ottobre" funziona per casi d'uso italiani (antincendio è giugno-settembre), **non** per casi d'uso continuativi (sovranità, NTN backhaul). Quindi il vettore B2 EU sovereign **non è raggiungibile** con tech 2026 senza breakthrough batterie Li-S 350 Wh/kg. Cap. 11 §11.9.3 lo dichiara come dipendenza, ma la probabilità di breakthrough Li-S aerospace-qualified entro 2028 è **bassa** (Solid Power non ha qualificato, QuantumScape è automotive, gli aerospace operator ASM nessuno).

### Cap. 7 — Mercato e Business Case

- **Critica 2.7.1:** §7.3.1 TAM HAPS strict $99M-$240M. Single source commerciale (vedi Critica G-02).
- **Critica 2.7.2:** §7.3.2 TAM-IT = "3-5% del mercato aerospace globale". Approssimazione lecita ma applicata a un mercato che **non esiste ancora** (HAPS service revenue, non R&D investment). 3-5% di zero è zero.
- **Critica 2.7.3:** §7.3.4 SOM Firmamento Y3 "€1.5-3.5M ARR (3 regioni)". Implica €500k-€1.2M ARR per regione. Nessuna regione italiana ha mai pagato €500k+/anno per servizio UAS persistente. Benchmark e-GEOS ha contratti Regioni a €50-200k. Sovrastima 3-5×.
- **Critica 2.7.4:** §7.8.2 pricing baseline Y1 €355-405k = somma di 5 contratti tra €30-150k ciascuno. Buon dettaglio. **Ma:** nessuno di questi 5 è validato da LoI. Action item M+6 esiste ma è ancora aperto. Pricing è ipotetico.
- **Critica 2.7.5:** §7.4.1 competitor Tier 1 globale. La tabella è onesta ("Firmamento NON può competere head-to-head"). Ma poi §7.5 differenziazione "4 pilastri" include "sostenibilità + ESG narrativa" come pilastro. **ESG è igiene, non vantaggio**. Tutti i competitor (Airbus, Skydweller, BAE) hanno ESG narrative. Non è differenziatore.
- **Critica 2.7.6:** §7.4.3 critica "Starlink a €50/mese è già lì". Risposta cita "sovranità dati italiana = argomento decisivo per PA". Ma **nessuna PA italiana ha mai pagato premium per "sovranità dati"** quando Starlink funziona. Argomento ipotetico, non validato.
- **Critica 2.7.7:** §7.6.1 BMC Customer Segments include "ASL3 (telemedicina)" e "Enti Parco Antola/Aveto". Entrambi sono customer ipotetici con willingness-to-pay non validata. Realismo dei segments medio-basso.
- **Critica 2.7.8:** §7.13 Red Team Check è onesto (6 critiche accettate). Ma le risposte sono tutte "action item M+6". Cosa succede se al M+6 le LoI non arrivano? Il documento non lo dice.

### Cap. 8 — Economico-Finanziario

- **Critica 2.8.1:** §8.3.1 Quadro Economico Y1 range €975k-1.96M (incluse IVA + contingency 15%). Il Briefing originale citava €600-900k. Differenza 2×. Lo Studio onestamente lo ammette (§8.3.1 caveat). **Ma:** mai chiamato esplicitamente "Briefing iniziale sottostimava CapEx 2×". Esecuzione narrativa morbida.
- **Critica 2.8.2:** §8.5.1 OpEx run-rate Y2 €260-480k. Personale: "3 FTE (pilota+ing+analyst) + 0.5 FTE PM". Costo onnicomprensivo €150-220k = €37-55k/FTE. Per profili aerospace IT con BVLOS skill, mercato 2026 = €60-100k/FTE annual loaded (lordo). Sottostima personale 30-50%.
- **Critica 2.8.3:** §8.6.1 modello cash flow Y1 NetIncome -€190k, Y2 +€53k, Y3 +€912k, Y4 +€1.9M. **CAGR revenue Y1-Y3: 156%**. **CAGR Y3-Y5: 60%**. Base rate aerospace service startup CAGR Y1-Y3: tipicamente 30-50% (vedi e-GEOS, NHazca, Planetek). Sovrastima 2-3×.
- **Critica 2.8.4:** §8.6.1 WACC 12% blended. Critica 3 Red Team lo solleva. Risposta cita "blended con 40-50% grant". Vero, ma se grant slittano (base rate aerospace: alta), WACC effettivo sale a 18-25%, NPV diventa negativo. Sensitivity §8.6.3 lo mostra ma non lo cita come risk.
- **Critica 2.8.5:** §8.6.2 scenario Worst Revenue Y3 €1.0M, Y5 €2.5M, NPV negativo. **Lo Studio non discute la probabilità del Worst scenario.** Senza probabilità, scenarios sono decorativi.
- **Critica 2.8.6:** §8.7 mix finanziamenti raccomandato Y1 cita "Coopfond Cooding Prototypes 2026: €50k". Audit-rigore-epistemico.md DR-002 dice "verifica bando Cooding 2026 disponibilità — chiusura M+1". Al M+3 chiuso o no? Se no, il piano fund mix Y1 è basato su grant non confermato.
- **Critica 2.8.7:** §8.6.4 ROI sociale "vite salvate da antincendio precoce: 1-3 vite/decennio per area servita". **Senza fonte**. Quante vite morte per incendi in zone SNAI Liguria? Senza dato base, l'attribuzione è ipotetica.

### Cap. 9 — Cronoprogramma e Gate

- **Critica 2.9.1:** §9.0.1 Gantt: 11 mesi Studio fattibilità + 12 mesi pilota = "aggressivo ma fattibile". Aerospace base rate: Phase A→B 18-30 mesi, non 11. Pilota commerciale 18-36 mesi, non 12. Sovraottimismo schedule.
- **Critica 2.9.2:** §9.1.2 Gantt schematico mostra Vol.1 + Vol.2 + Vol.3 in parallelo M+0-M+11. 3 volumi totali ~250-350 pagine + allegati. Con 3-4 FTE interni + 2-3 consulenti, sono ~80-120 pp/persona in 11 mesi. Faceabile ma significa **zero tempo per validazione esterna** (peer review indipendente, audit).
- **Critica 2.9.3:** G2 entry criteria M+6 include "Pre-application meeting ENAC condotto + feedback documentato". Tempi reali pre-application meeting ENAC = scheduling + paperwork ~4-6 mesi. Avviato M+0 = realisticamente feedback M+5-7. Compatibile, ma tight, e nessuna buffer.
- **Critica 2.9.4:** G3 entry criteria M+10 include "Mix funding ≥ 60% committed". Coopfond decisione = mesi. Regione FESR DGR = mesi. Mix funding 60% committed M+10 implica decisioni board Coopfond + Giunta Regione Liguria entro M+10. Politically unrealistic per timing.
- **Critica 2.9.5:** Sebbene il documento citi "kill criteria" come "showstopper insuperabili", la struttura Hold→Re-review è soggetta a deriva temporale (vedi Critica G-04).

### Cap. 10 — Raccomandazione di Gate

- **Critica 2.10.1:** §10.1.1 verdetto "Go Cond. 6A confidence medium-high". Confidence medium-high basato su evidenze M+3 = wishful. Realistica al M+3: confidence medium (LoI Regione non firmata, SORA non valutato, mix funding non committed).
- **Critica 2.10.2:** §10.3.1 argomento 1 "Tecnicamente fattibile con piattaforma TRL 8-9". JOUAV TRL secondo vendor cinese (Critica G-09 + 2.6.3).
- **Critica 2.10.3:** §10.3.1 argomento 5 "Asset riusabili 6A → 6B: ~30-40% del CapEx Y1 in valore". Cap. 6 §6.1.3 dice "~60%". Inconsistenza interna 30-40% vs 60%.
- **Critica 2.10.4:** §10.3.2 5 hard conditions C1-C5 = 5 cose che devono andare tutte bene per Go. Cap. 10.6 Critica 1 ammette P(tutte)~25-60%. Non è "Go Condizionato", è "Likely Hold camuffato da Go Cond.".
- **Critica 2.10.5:** §10.4.1 argomento 1 a supporto Hold 6B: "Concept tecnicamente plausibile". "Plausibile" ≠ fattibile. Cap. 6 §6.0.2 confidence medium-low. Concept plausibile + showstopper aperti = non base per spend Phase B €5.5-13.5M.
- **Critica 2.10.6:** §10.4.3 hard conditions Phase B M+24 include "C-6B-2: Funding mix Phase B ≥ 50% committed al M+24". Committed da chi? EDF call HAPS chiusa al M+24 e Firmamento è vincitrice? PNRR Aerospazio? Nessun calendar bandi specifici è citato.
- **Critica 2.10.7:** §10.5 verdetto aggregato visione: lo Studio "preserva come vettore strategico" Fase 4 (M+72-96) e Fase 5 (M+96-120). Decisioni gate G6, G futuri "out of scope". **Lo Studio sta scrivendo un assegno in bianco con i propri verdetti futuri.**
- **Critica 2.10.8:** §10.6 Red Team Combinato ha 6 critiche con risposte. **Tutte le risposte concludono in difesa del verdetto.** Nessuna critica ha provocato modifica del verdetto. Pattern "red team theater" — il red team valida, non sfida.
- **Critica 2.10.9:** §10.7 "Cosa esplicitamente NON facciamo" è eccellente. Mantenere e rafforzare.
- **Critica 2.10.10:** §10.9 livelli di successo: micro (M+12) €200k ARR, meso (M+36) €1.5-3.5M, macro (M+120) "principal Italian node consorzio EU". Salto micro→macro di **100-400×** in 10 anni. Base rate aerospace startup: ~10% raggiunge €10M ARR Y7. Lo Studio sta posizionando Firmamento nel top 1-2% di startup aerospace.

### Cap. 11 — Roadmap Post-Fattibilità

- **Critica 2.11.1:** §11.1.2 confidence per fase: Fase 1 high → Fase 2 medium → Fase 3 medium-low → Fase 4 low → Fase 5 speculative. Lecito. Ma poi il capitolo dedica **uguale densità di pianificazione** a ciascuna fase. Sproporzione tra rigore confidence e dettaglio descrittivo.
- **Critica 2.11.2:** §11.4.6 budget Fase 3 cumulato €17.8-35.5M vs visione-10-anni §4 €15-50M. "Più alto della stima" ammesso. Cap. 11 stesso amplifica capital intensity oltre la visione documentata. Inconsistenza interna del progetto.
- **Critica 2.11.3:** §11.5 Fase 4 ARR target €30-80M Y8 + "3-10 HAPS perennial operativi". 10 HAPS perennial in 8 anni con tech 2026? Nessun programma globale HAPS solare ha mai raggiunto 10 unità operative perennial. Zephyr massima fleet 2-3 unità.
- **Critica 2.11.4:** §11.6 Fase 5 "consorzio EU stratosferico" con 10-30 HAPS. Programma EU equivalente IRIS² su HAPS non esiste. Lo Studio lo dichiara (§11.9.2) come dipendenza, ma la roadmap ci si appoggia.
- **Critica 2.11.5:** §11.6.3 consorzio EU target con TAS-Leonardo "Co-lead consortium". Cap. 11 stesso (§11.4.5, §11.5.5) avverte che TAS-Leonardo è rischio di acquisizione difensiva. Stesso entity è top-1 partner E top-1 rischio. Contraddizione strategica.
- **Critica 2.11.6:** §11.7 gate decisionali post-Studio M+12 → M+120. Ogni gate ha criteri Go/Hold/No-Go. **Ma:** la probabilità composta di passare tutti 9 gate sequenziali = base rate aerospace startup ~5-15%. Lo Studio non lo dichiara.
- **Critica 2.11.7:** §11.8 showstopper per fase: ottima sezione. **Ma:** gli showstopper Fase 3-5 includono RSK-GEO-001 (geopolitica EU-US) e RSK-GEO-005 (acquisizione difensiva). Questi sono fuori dal controllo Firmamento. Mitigation strategy esiste ma success rate ignoto.
- **Critica 2.11.8:** §11.10 Red Team Check ha 6 critiche. Critica 3 (capital intensity €10-30B "catastrofico per narrativa VC") riceve risposta "stratificazione di tipi di capitale per fase". Non risolve il problema (vedi Critica G-07).
- **Critica 2.11.9:** §11.13 disclaimer epistemico finale: "La probabilità che il vettore venga eseguito esattamente come descritto è bassa (base rate aerospace startup: ~10% per Y8 ARR €10M+)". **Onestà eccellente.** Mantenere.

---

## 3. Falsifying observations MANCANTI

I seguenti claim importanti del Volume 1 NON hanno falsifying observation dichiarata o ne hanno una troppo morbida:

| # | Claim | Localizzazione | Falsifying observation mancante |
|---|---|---|---|
| FO-MISS-01 | "Modello service-only + cooperative dà vantaggio competitivo difendibile vs Aalto/Skydweller" | Cap. 7 §7.5 | Quale evento dimostrerebbe che il modello cooperativo è **svantaggio** competitivo (non vantaggio)? Es: "Se al M+18 Aalto annuncia JV con Leonardo + servizio servizi a Liguria/Calabria a €50k/anno, modello cooperativo è handicap." |
| FO-MISS-02 | "Linguaggio 'complementare a IRIS²' protegge da reazione US" | Cap. 0, 1, 5, 7, 11 (~25 occorrenze) | Quale evento dimostrerebbe che il linguaggio non funziona? Es: "Se entro Y3 il Dipartimento di Stato US emette communiqué su HAPS EU come 'EU sovereign challenge', linguaggio fallito." |
| FO-MISS-03 | "Asset riusabili 6A → 6B ~30-60% del CapEx" | Cap. 0, 6, 10 | Quale misurazione concreta valida o invalida il riuso? Es: "Al gate M+24 audit CapEx Phase B che riusa effettivamente >40% asset Y1 (cloud, ground segment, autorizzazioni, brand) ≥ €0.4M valore." |
| FO-MISS-04 | "Firmamento è candidato a nodo italiano di consorzio EU sovereign HAPS" | Cap. 0, 1, 2, 7, 11 | Quale evento dimostrerebbe Firmamento non è candidato? Es: "Se al M+36 EuroHAPS-2 (call EDF 2027) si chiude senza Firmamento come partner, posizionamento candidato è fallito." |
| FO-MISS-05 | "Pricing PA italiana €100-300k/anno per servizio EO Regione è sostenibile" | Cap. 7 §7.8 | Quale evento concreto invalida il pricing? Es: "Se entro M+6 e-GEOS / Planetek confermano che contratti Regione 2024-2025 sono in fascia €30-80k, pricing baseline da rivedere -40%/-60%." |
| FO-MISS-06 | "NPV positivo Y4-Y5 scenario base" | Cap. 8 §8.6 | Quale evento attiva re-baseline NPV? Es: "Se Y2 cum FCF < -€2M (worse than worst case), NPV 10y diventa negativo strutturalmente." (Cap. 8.6.2 cita questo, ma soglia €-2.5M; coerenza). |
| FO-MISS-07 | "Capital structure dual-class shares + golden share preservano founder maggioranza fino M+72" | Cap. 11 §11.4.7 | Quale evento dimostra fallimento difesa? Es: "Se al Series A (M+24-36) lead investor richiede unanimous voting >50% per blocco strategic, e Firmamento accetta, founder maggioranza persa." |
| FO-MISS-08 | "Pentema rappresentativo aree SNAI italiane" | Cap. 1 §1.2.3 | Quale evento invalida la rappresentatività? Es: "Se al M+24 tentativo replica in 2nda area SNAI (Piemonte/Calabria) fallisce per ragioni strutturali (orografia troppo diversa, popolazione troppo diversa, willingness-to-pay troppo bassa), rappresentatività falsata." |
| FO-MISS-09 | "TAS-Leonardo coopereranno (non antagonizzeranno) fino M+72" | Cap. 11 §11.9.4 (RSK-GEO-005 riferimento riservato) | Quale evento dichiarato? Es: "Se entro M+24 TAS-Leonardo apre proposta MoU subordinato a equity stake ≥ 25% Firmamento, cooperazione mascherata di acquisizione." |
| FO-MISS-10 | "Energy balance HALE inverno chiudibile con tech 2028 batterie Li-S 350 Wh/kg" | Cap. 6 §6.2.2.2 + Cap. 11 §11.9.3 | Quale evento concreto invalida? Es: "Se al M+36 nessun fornitore aerospace (Maxwell, Northvolt, Solid Power, ACC) ha qualificato cella ≥ 320 Wh/kg pack, breakthrough atteso 2028 non è in arrivo." |

---

## 4. Triangolazione INSUFFICIENTE (claim numerici single-source)

| # | Claim numerico | Localizzazione | Source | Triangulation status |
|---|---|---|---|---|
| TR-01 | TAM HAPS strict $99M (2024) / $240M (2030) / CAGR 16% | Cap. 7 §7.3.1 | MarkNtel Advisors 2025 (commerciale) | NON triangolato (Cap. 7 dichiara confidence low). Manca AIAD, Eurospace, ITU, EUSPA. |
| TR-02 | TAM HAP wide $1.54-1.73B (2024) / $2.66-3.10B (2030) / CAGR 7-8% | Cap. 7 §7.3.1 | Coherent Market Insights + Grand View (commerciali) | NON triangolato. |
| TR-03 | TAM-IT 3-5% del globale | Cap. 7 §7.3.2 | "AIAD annual reports + Aerospace Italia 2023" (citato senza ref. specifica) | Triangolazione superficiale. AIAD 2024 ha dati più recenti. |
| TR-04 | CapEx Zephyr "€15-50M (stima)" | Cap. 1 §1.3.2 | Stima Studio | NON triangolato. Airbus non pubblica costo unitario. Press: $20-30M Zephyr-S unit cost. |
| TR-05 | OpEx aviation insurance UAS BVLOS €15-40k/anno | Cap. 8 §8.5.1 | Stima Studio | NON triangolato. Aviation insurance market IT (Allianz, AIG) non consultato. |
| TR-06 | Pricing PA Regione Liguria €150k/anno per servizio EO | Cap. 7 §7.8.2 | Stima Studio | NON triangolato. e-GEOS / Planetek / NHazca contratti pubblici (CONSIP/MEPA) non consultati. |
| TR-07 | Mercato batterie Li-S "350 Wh/kg pack entro 2028" | Cap. 6 §6.0.2 + Cap. 11 §11.9.3 | Citazione QuantumScape / Solid Power / ACC | Triangulation superficiale. QS è automotive, SP non ha qualificato aerospace, ACC è ramping. Roadmap aerospace-specific manca. |
| TR-08 | Mercato HAPS UAV "60% market share globale" | Cap. 7 §7.3.1 | MarkNtel | NON triangolato. |
| TR-09 | Wave AAM ENAC Italia €1.86B 2021-2030 | Cap. 7 §7.3.5 + Cap. 8 §8.1.2 | ENAC AAM BP 2021-2030 | Source authoritative ma single. Nessun cross-check con MIMIT bandi effettivi 2021-2025 (per validare che la traiettoria di spesa sta materializzando). |
| TR-10 | Cooperative Legacoop 10 pilota (capofila Fabrica) | Cap. 1 §1.1.2 + Cap. 2 §2.2.1 | Briefing Firmamento M-3 | Single source (proponente). Lista nominale "dato sensibile". Coopfond non ha validato indipendentemente. |
| TR-11 | Population Pentema "~150 residenti" / "poche centinaia di abitanti" | Cap. 1 §1.1.3 + Cap. 2 §2.5.4 | Cap. 1 dice "poche centinaia", Cap. 2 dice "~150" | **Inconsistenza interna** sui dati base. ISTAT Pentema = 32 residenti (2023). Tutti gli altri dati sovrastimati. |
| TR-12 | "Lead time vendor cinese JOUAV" rischio RSK-SUP-001 | Cap. 10 §10.2.2 | Stima Studio | Non quantificato. JOUAV CW-30E lead time 2025 = 60-120 giorni standard, 6-12 mesi se tensioni tariffarie. Variabilità non triangolata. |
| TR-13 | "Vite salvate da antincendio precoce 1-3/decennio per area" | Cap. 8 §8.6.4 | Stima Studio | NON triangolato. Liguria antincendio fatalities 2015-2024 stats non consultate. |
| TR-14 | "Comunità Pentema ~150 residenti accetta sperimentazione" (assunzione AS-009) | Cap. 2 §2.5.5 + Cap. 1 §1.2.3 | Estensione di "presunzione di accettabilità" | NON validato. Workshop pubblico Pentema non ancora condotto al M+3. |
| TR-15 | "WACC 12% blended" | Cap. 8 §8.6.1 | Stima Studio basata su mix grant 40-50% | Non triangolato con benchmark VC aerospace IT 2025-2026 (Primomiglio, P101, LIFTT, CDP VC). |

---

## 5. Base rate ignorate

I seguenti claim "tutto va bene" del Volume 1 non sono confrontati con base rate documentate:

| # | Claim "tutto va bene" | Localizzazione | Base rate ignorata |
|---|---|---|---|
| BR-01 | "11 mesi Studio Fattibilità + 12 mesi pilota = aggressivo ma fattibile" | Cap. 9 §9.0.3 | Aerospace Phase A→B = 18-30 mesi mediano (NASA, ESA). Aerospace pilot 18-36 mesi. Lo Studio è 50% di mediano. Probabilità execution on-time: 20-35%. |
| BR-02 | "Cooperative Legacoop ≥ 8 su 10 confermano partecipazione formale M+6" | Cap. 0.3 + Cap. 10.3 | Base rate cooperative IT che firmano partecipazione formale a sperimentazioni tech entro 6 mesi: probabilmente 40-60% (su 10, 4-6 firmano). |
| BR-03 | "≥ 3 contratti pluriennali PA M+24" (soglia minima 6A-04) | Cap. 2 §2.4.3 + Cap. 7 §7.9.2 | Base rate aerospace startup IT che chiude 3 contratti PA pluriennali in Y1-Y2: <20%. Cicli appalti PA italiani 12-24 mesi. |
| BR-04 | "ARR Y3 €1.5-3.5M / Y5 €3-8M" | Cap. 0.11 + Cap. 7 §7.3.4 | Base rate aerospace startup IT con ARR Y3 €1.5M+: ~15%. ARR Y5 €3M+: ~10%. |
| BR-05 | "Mix funding 60% committed entro M+10" | Cap. 0.3 + Cap. 10.3 | Base rate aerospace early-stage che chiude 60% funding committed in 11 mesi: ~25% (Coopfond decisione + Regione FESR DGR + R&D credit + equity seed in <12 mesi è ambizioso). |
| BR-06 | "SORA ENAC SAIL II-III operativa entro M+9" | Cap. 0.3 + Cap. 10.3 | Base rate SORA submission → autorizzazione in Italia 2023-2025: 6-12 mesi mediano. SAIL II-III BVLOS in zona popolata (Pentema): 8-14 mesi più probabili. M+9 = aggressivo. |
| BR-07 | "TRL HALE subsystems critici da 3-4 a 5-6 in 24 mesi Phase B" | Cap. 6 §6.0.2 | Base rate aerospace R&D passaggio TRL 4→6: 3-5 anni, €15-50M. Lo Studio propone half time / half budget. |
| BR-08 | "Energy balance HALE inverno 44°N chiudibile con tech 2028 (Li-S 350 Wh/kg)" | Cap. 6 + Cap. 11 §11.9.3 | Base rate breakthrough batteria aerospace-qualified in 2-3 anni dall'annuncio: <30% (Solid Power 2018-2026 ancora non qualified). |
| BR-09 | "EASA Special Condition HAPS adopted entro M+60-72" | Cap. 11 §11.4.3 | Base rate apertura framework EASA novel: 5-10 anni dalla prima proposta industriale ufficiale. **Nessuna proposta ufficiale al maggio 2026**. M+60-72 = ottimistico. |
| BR-10 | "Programma EU sovereign HAPS analog IRIS² aperto entro Y4-Y5 (2030)" | Cap. 11 §11.9.2 | Base rate apertura programma EU multi-miliardario dedicato a tech nuova: 7-12 anni dalla prima study commissionata. **Nessuna study commissionata al maggio 2026**. <20% probabilità entro 2030. |
| BR-11 | "Y8 ARR €30-80M, costellazione 3-10 HAPS perennial" | Cap. 11 §11.5.2 | Base rate aerospace operator con flotta 5+ HAPS perennial: **zero al 2026 globale**. Aalto ha 1-2 unità, Skydweller 1, PHASA-35 ancora pre-operational. |
| BR-12 | "Capital intensity €500M-€2B per small fleet 5-10 HAPS Y10" | Cap. 0.11 + Cap. 8 + Cap. 11 §11.6.4 | Base rate aerospace startup che raggiunge €500M+ raised in 10 anni: <2% (top 1% di startup aerospace globali). Esempi: SpaceX (16 anni a $1B), Rocket Lab (10 anni a $500M). |

---

## 6. Pre-mortem aggregato — "Il progetto è fallito tra 5 anni: perché?"

Top 5 driver di fallimento più probabili, in ordine di probabilità decrescente:

### Driver 1 — Regione Liguria non firma LoI o ritira commitment dopo Y1 (P: alta)
Storia: Bucci eletto Presidente Liguria ottobre 2024 (post-Toti). Centrodestra. Priorità diverse da centrosinistra. Aree Interne e SNAI sono priorità trasversali ma non bandiera. Cambio Assessorato (Innovazione, Aree Interne) probabile entro Y2. Senza anchor regionale, B2G regionale (40-50% ARR target Y3) collassa. Pivot Piemonte/Calabria implica 12-18 mesi riallocazione. **Early Warning Indicator (EWI):** se entro M+6 incontro tecnico ristretto con Giunta Liguria non avviato → red flag.

### Driver 2 — Cycle gap funding M+10 → M+18 esaurisce cash (P: alta)
Coopfond Cooding Prototypes 2025 €80-150k esauriti M+9-10. Cooding-Invest €150-300k non garantito (bando 2026 non confermato). Regione FESR DGR + erogazione = 6-12 mesi standard. R&D credit retroattivo (Q1 dell'anno successivo). Equity seed €200-500k da raised in 6-9 mesi con startup early-stage senza track record. Probabilità cash gap M+10-M+18 = alta. **EWI:** se al M+6 bridge financing buffer < €100k → red flag.

### Driver 3 — JOUAV CW-30E supply chain blocked + Plan B Tekever non ready (P: media-alta)
JOUAV cinese: tariffe USA-CN 2025+ + EU restrictions su dual-use cinese in escalation. Lead time potrebbe passare da 60-120 giorni a 12-18 mesi. Tekever AR3 (Plan B) ha lead time anch'esso non immediato, e con specifiche differenti (no VTOL pure, payload diverso). Pivot piattaforma in Y1 = 6-9 mesi delay + CapEx re-baselining. **EWI:** se al M+3 quotation JOUAV ritarda > 30 giorni → red flag.

### Driver 4 — Accettabilità sociale Pentema negata o controversa (P: media)
Comunità Pentema 32 residenti reali (ISTAT) — non 150 come sostenuto. Workshop pubblico non ancora condotto al M+3. Probabilità "single opponent vocale" su 32 abitanti = alta. Privacy concern + percezione sorveglianza + estetica + rumore = vulnerabili a 1 evento mediatico locale. Pivot ad altra frazione SNAI Liguria possibile ma implica re-engagement Comune + 6-9 mesi delay. **EWI:** se al M+6 workshop pubblico genera ≥ 3 vocali opposing → red flag.

### Driver 5 — Aalto HAPS apre operazioni Italia via JV Leonardo (P: media)
Aalto (Airbus subsidiary) + Leonardo (azionista Airbus 1.5%) hanno motivo strategico per chiudere "italian HAPS narrative" rapidamente. JV Aalto-Leonardo aprible in 6-12 mesi se Aalto vede mercato IT crescere. Aalto offre Zephyr 8/S a tariffe sotto i costi Firmamento (capital efficiency superior). Firmamento perde anchor narrative "sovranità italiana stratosferica". **EWI:** se al M+12 Aalto annuncia partnership IT (qualunque) → red flag.

**Bonus driver 6 — EASA HAPS framework non si apre entro M+48 (P: alta)**
Cap. 11 §11.9.1 lo dichiara. Base rate EASA novel framework apertura: 5-10 anni. Al M+48 (2030) nessuna probabilità ragionevole. Phase B 6B finisce essendo R&D senza commercial path. €5.5-13.5M Phase B = pre-burn pre-no-go. **EWI:** se al M+24 EuroHAPS-2 EDF call non include HAPS Special Condition framework workstream → red flag.

---

## 7. Scenari di morte del progetto (probabilità + trigger)

### Scenario A — ENAC nega SAIL II-III per Pentema (P: media, ~30-40%)
**Trigger osservabile:** ENAC pre-application meeting M+3-6 valuta GRC ≥ 6 (densità popolazione "moderate" non "sparse"), SAIL salta a IV-V, costi compliance × 3-5, tempi raddoppiati.
**Conseguenza:** Pilota Pentema inattuabile in budget Y1. Pivot ad altro sito SNAI Liguria (Beigua, Val di Vara, Fontanabuona) implica 6-12 mesi delay + perdita anchor narrative Pentema. Probabilità rilancio: 40-50%.

### Scenario B — Aalto entra in Italia con JV Leonardo (P: media, ~25-35% entro Y2)
**Trigger osservabile:** Aalto press release JV/partnership con Leonardo o TAS o servizio diretto Italia entro M+12-18.
**Conseguenza:** Firmamento perde "sovereign IT" pillar + perde Tier-1 customer (Regione, PC). Differenziazione "geografia + cooperative + sostenibilità" non basta da sola contro Tier-1 brand + Zephyr operational track record. Probabilità sopravvivenza: 30-50% (riposizionamento niche service operator senza HALE ambition).

### Scenario C — Coopfond Cooding 2026 non aperto + Regione FESR ritarda (P: alta, ~40-50%)
**Trigger osservabile:** M+6 Coopfond CdA non delibera bando Cooding 2026 + Regione Liguria FESR Bando R&I 2026 non aperto + Cooding-Invest in deferral.
**Conseguenza:** Cash gap M+10-M+18 = €200-400k missing. Bridge financing emergency: difficile per startup early-stage. Probabilità sopravvivenza: 30-50% (con drastico cost-cutting + Series Seed accelerato).

### Scenario D — Comunità Pentema oppone operazioni (P: bassa-media, ~15-25%)
**Trigger osservabile:** Workshop pubblico Pentema M+6-9 ha ≥ 3 voci pubbliche oppostie + stampa locale negativa + petition.
**Conseguenza:** Comune Torriglia ritira disponibilità. Pivot sito M+9-12 con delay 6-9 mesi. Probabilità rilancio: 60-70%.

### Scenario E — Energy balance HALE inverno conferma 0% margin + Li-S non disponibile entro 2028 (P: media-alta per 6B, ~40-50%)
**Trigger osservabile:** M+48 simulazioni completa energy balance inverno 44°N + nessun fornitore Li-S aerospace qualified ≥ 320 Wh/kg pack.
**Conseguenza:** Percorso 6B condannato a "seasonal-only" (marzo-ottobre). Vettore B2 EU sovereign perennial non raggiungibile con tech disponibile. Phase B €5.5-13.5M = R&D senza prospect commercial perennial. Probabilità Hold permanente 6B: 60-80%.

### Scenario F — Acquisizione difensiva TAS-Leonardo a "fair value" (P: media, ~20-30% entro Y4-Y6)
**Trigger osservabile:** Approccio informale TAS-Leonardo per equity stake ≥ 25% Firmamento entro M+24-36, con linguaggio "consortium leadership" / "Italian stratospheric coordination".
**Conseguenza:** Founder team perde maggioranza + traiettoria indipendente. Boundary B2 "nodo italiano" preservato narrativamente ma controllato da incumbent. Probabilità Firmamento standalone vivente Y10: 20-30%.

### Scenario G — Capital intensity Phase 4-5 non finanziabile (P: alta per Fase 4-5, ~70-80%)
**Trigger osservabile:** Roadmap CE 2030+ pubblicata senza programma HAPS sovereign multi-miliardario; Series B €10-30M non raised; EDF HAPS call < €100M.
**Conseguenza:** Roadmap ridimensionata a "small fleet" o "consolidamento standalone Italia". Boundary B2 "EU sovereign full scale" abbandonato (lo Studio già lo dichiara come precondizione esterna). Probabilità sopravvivenza company: 60-80% in modalità ridotta.

---

## 8. Action items prioritari da fissare prima di Gate G3 (M+10)

In ordine di priorità decrescente. Owner agent suggerito tra parentesi.

### Priorità 1 — Reality checks rapidi (M+3 → M+6)

1. **Verifica dato Pentema population** (snai-funding-expert + business-model-strategist) — **M+4**
   Risolvere inconsistenza interna Cap. 1 ("poche centinaia") vs Cap. 2 ("~150") vs ISTAT (32 residenti). Conseguenze su accettabilità sociale + scale narrativo.

2. **Verifica bando Coopfond Cooding 2026** (snai-funding-expert) — **M+4**
   Chiusura DR-002 (audit-rigore-epistemico.md). Se bando 2026 non aperto, mix funding Y1 va ricostruito + bridge financing strategy attivata.

3. **Verifica DGR e Giunta Regione Liguria post-Bucci 2024** (snai-funding-expert + sovereign-strategist) — **M+4**
   Mapping Assessorati attuali (Innovazione, Aree Interne, Protezione Civile, Trasporti). Identificare champion politici credibili. Senza, AS-001 wishful thinking.

4. **Triangolazione TAM-IT con AIAD + Eurospace + EUSPA** (business-model-strategist) — **M+5**
   Chiusura DR-007 + DR-012. Se TAM-IT realisticamente €30-60M (non €100-200M), SAM/SOM/ARR/NPV vanno re-baselinati.

5. **Benchmark pricing PA italiana e-GEOS / Planetek / NHazca via CONSIP/MEPA** (business-model-strategist + financial-cfo) — **M+5**
   Validare pricing baseline Y1. Se contratti reali sono €30-80k/anno (non €100-300k), MVP revenue Y1 €355-405k diventa €120-180k. SyR-Cost-003 (≥ €200k) potenzialmente fallisce.

### Priorità 2 — Decisioni stratoegiche (M+6 → M+8)

6. **Quotation contratti JOUAV + Tekever** (vtol-uas-specialist) — **M+6**
   Chiusura OQ-F03. Pre-finalize TS-PLATFORM-6A con cifre verificate, non datasheet.

7. **Pre-application meeting ENAC condotto + feedback documentato** (aviation-regulatory-counsel) — **M+6**
   Chiusura DR-004. Verifica realistica SAIL II-III vs IV-V. Senza, il verdetto Cap. 10 è speculation.

8. **Workshop pubblico Pentema condotto** (data-privacy-counsel + business-model-strategist) — **M+6**
   Validare AS-009 (accettabilità sociale). Senza, pilota a Pentema è speculation.

9. **LoI Regione Liguria firmata** (snai-funding-expert + sovereign-strategist) — **M+6**
   Chiusura OQ-010. Senza, anchor B2G regionale è ipotesi.

10. **MoU 8/10 cooperative pilota** (business-model-strategist) — **M+6**
    Chiusura OQ-011 (parziale). Validare formalmente la rete. Lista nominale, non più "dato sensibile".

### Priorità 3 — Riallineamento documentale (M+8 → M+10)

11. **Riformulare Cap. 0 e Cap. 10 con le 6 categorie distinte (feasibile/tecnicamente/operativamente fattibile, regolatoriamente autorizzabile, economicamente sostenibile, operativo)** (aerospace-SE + business-model-strategist) — **M+8**
    Chiudere Critica G-05.

12. **Spostare capital intensity Y8-Y10 (€500M-€2B / €10-30B) dal Volume 1 a Volume 2 Allegato "Vettore strategico"** (sovereign-strategist + communications-lead) — **M+8**
    Chiudere Critica G-07. Decoppiare narrativamente decisione Y1-Y3 da vettore Y4-Y10.

13. **Aggiungere a Cap. 10 opzione "Defer 6A 12 mesi" come do-nothing benchmark** (red-team-skeptic + business-model-strategist) — **M+9**
    Chiudere Critica G-08. Conforme art. 41 D.Lgs. 36/2023 + Allegato I.7 (ipotesi di non realizzazione).

14. **Aggiungere a Cap. 9 escalation matrix Hold→No-Go con kill criteria quantitativi** (gate-review-checklist skill + aerospace-SE) — **M+9**
    Chiudere Critica G-04. Esempio: 3 Hold consecutivi su LoI Regione = No-Go scale-up Liguria.

15. **Dichiarare timeline realistica EASA RMT HAPS con base rate 5-10 anni** (aviation-regulatory-counsel + sovereign-strategist) — **M+9**
    Chiudere Critica G-10. Onestà sul fatto che Phase B 6B M+24-48 si chiude prima dell'apertura RMT.

### Priorità 4 — Robustezza finanziaria (M+9 → M+10)

16. **Modello DCF completo Excel con scenarios + Monte Carlo + sensitivity** (financial-cfo-analyst) — **M+9**
    Chiusura OQ-F05, OQ-F06. Senza, NPV/IRR baseline è "suggestion", non analysis.

17. **Bridge financing strategy quantificata** (financial-cfo-analyst) — **M+9**
    Chiusura OQ-F04. €100-300k buffer richiesto. Identificare strumento concreto (linea CCB, anticipazione bandi, factoring).

18. **Sensitivity Y2 cum FCF + kill criterion** (financial-cfo-analyst) — **M+9**
    Cap. 8 §8.6.2 cita kill criterion Y2 < -€2.5M ma non lo aggancia a gate. Esplicitarlo come Hard No-Go trigger.

### Priorità 5 — Posizionamento difensivo (M+10 → M+11)

19. **Competitor monitoring Aalto/Skydweller/PHASA-35 con Early Warning Indicators trimestrali** (competitor-intelligence) — **M+10**
    Aggiungere a Cap. 2 §2.2 + Cap. 7 §7.4. Mappare 5-7 player globali HAPS con EWI per ciascuno.

20. **Falsifying Observations Tracker formale** (epistemic-rigor skill + risk-register-builder) — **M+10**
    Cap. 2.6 Critica 6 ha azione aperta. Implementare come allegato Vol. 2.

21. **Position paper "Italian Stratospheric Sovereignty" draft** (sovereign-strategist + communications-lead) — **M+10**
    Cap. 11 §11.10.6 + §11.13. Prima esposizione pubblica della visione, controllata, prima di gate G3.

---

## Nota di chiusura

Il Volume 1 dello Studio di Fattibilità è **superiore alla media degli studi aerospace early-stage italiani in disciplina epistemica** (dichiarazione confidence, falsifying observations, base rate awareness, red team automatic). Questo è merito.

Il problema **non è la qualità della disciplina**, è che la disciplina **è descrittiva, non prescrittiva**: il documento sa che ci sono debolezze, le elenca, ma non riformula le conclusioni di conseguenza. Il verdetto Go Cond. 6A + Hold 6B sopravvive ad ogni critica perché ogni risposta termina in "confidenza dichiarata, action item M+6/M+9/M+10". Action item su carta non sono evidenze.

Per essere **investment-grade al gate G3 M+10/M+11**, il documento deve:
1. Convertire ~50% degli action items in evidenze chiuse (LoI, contratti, feedback ENAC, quotation).
2. Riformulare verdetti con linguaggio più preciso (Critica G-05).
3. Disaccoppiare narrativamente Y1-Y3 da Y4-Y10 (Critica G-07).
4. Aggiungere kill criteria quantitativi (Critica G-04).
5. Triangolare i ~10 claim numerici cruciali (sezione 4).

Senza, il rischio è che il gate G3 produca un **Go Cond. teatrale** che il primo financiatore serio (Series Seed, banca, EIB due diligence) ribalterà in 4 ore di analisi.

---

**Fine audit Red Team Volume 1.**

> Brutality is mercy. Better critica oggi che no-go al primo Series Seed.
