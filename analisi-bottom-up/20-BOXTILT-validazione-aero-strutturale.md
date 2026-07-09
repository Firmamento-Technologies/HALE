# 20 — Validazione aero-strutturale del concept box-wing + 4 tilt-rotor (BOXTILT)

> **Cosa è.** Validazione critica (o falsificazione) del concept dell'utente — box-wing alla Prandtl con **4 tilt-rotor** (2 anteriori traenti + 2 posteriori spingenti in crociera, tutti e 4 verticali in hover) — e revisione delle assunzioni della simulazione L0/L1 `sim_boxwing_tiltrotor.py`. Aggiunge la parte **strutturale / aeroelastica / di controllo di transizione** che il modello di sola polare non copre.
> **Autore:** Aerodynamics & Structures Engineer
> **Data:** 9 luglio 2026
> **Livello di fidelity:** **L0/L1** (back-of-envelope + Prandtl analitico + component drag build-up). Nessun VLM validato, nessun RANS, nessuna galleria, nessun volo. Ogni numero ha assunzione, banda e confidence.
> **Ancore interne:** `18-boxwing-tiltrotor-rivalutazione.md`, `22-boxwing-vantaggio-tecnico.md`, `ricerca-approfondita/R6-boxwing-aerodinamica.md`, `14-vtol-config-tradestudy-C3.md`.
> **Vincolo di coerenza (rispettato):** NON contraddico i verdetti fisici consolidati — vantaggio d'ala netto ≈0% a scala C3 (regime attrito-dominato, crossover Re≈4×10⁵) e CD0 dominato dall'hardware VTOL. Verifico però onestamente l'unica novità genuina del BOXTILT: **qui nessun disco rotore è morto in crociera**, e questo merita di essere pesato, non liquidato.

---

## 0. Sintesi in una riga

Le assunzioni della simulazione **non sono eque: prendono il corner ottimistico su due leve contemporaneamente** (span efficiency alta *e* CD0 basso *e* penalità di massa VTOL bassa), e confrontano il BOXTILT con il peggior VTOL possibile (lift+cruise a dischi morti) invece che con il benchmark corretto (lift+cruise retrattile, anch'esso pulito in crociera). Corretto il tiro, il **+44% di range** collassa a **≈+10÷15% base** e **≤0% contro il retrattile**, con una coda negativa. Ma — punto onesto a favore dell'utente — **il verdetto aero non è "il box perde": qui, senza dischi morti, l'aerodinamica è un vero pareggio, non una penalità.** Il collo di bottiglia del concept **non è l'aerodinamica: è il controllo di transizione, i modi di guasto dell'attuazione di tilt e la massa dei 4 meccanismi.**

---

## 1. Le assunzioni della simulazione sono eque? (giudizio voce per voce)

### 1.1 CD0 = 0.034 per il BOXTILT — **ottimistico, ma per la ragione giusta** `[STIMA, confidence media]`

Qui il mandato coglie un punto reale: il CD0 = 0.040 "sporco" di `22`/`R6` derivava in larga parte dai **dischi rotore fermi (bluff bodies) esposti in crociera** di un lift+cruise. **Nel BOXTILT quei dischi non esistono**: tutti e 4 i rotori tiltano e diventano propulsivi. Quindi **è scorretto applicare al BOXTILT il CD0 0.040 del lift+cruise** — e su questo la simulazione ha ragione a scendere.

Ma 0.034 (solo +0.006 sul monoplano pulito 0.028) **sottostima ciò che resta**. Build-up incrementale rispetto al monoplano (riferito a S = 0.692 m²) `[STIMA]`:

| Voce aggiunta dal BOXTILT vs monoplano pulito | ΔCD0 stimato | Note |
|---|---|---|
| **2ª ala (box)** — superficie bagnata ~raddoppiata, ma soprattutto **Re dimezzato** (corda per ala ~0.11–0.12 m → Re≈2×10⁵) → drag di profilo peggiore, bolle di separazione low-Re | +0.002 ÷ +0.004 | il single-CD0 della sim non cattura il degrado di Re per-ala |
| **2 paratie verticali di estremità** (gap 0.4 m × corda ~0.2 m) — superficie bagnata pura, nessuna portanza utile | +0.003 ÷ +0.005 | driver spesso sottovalutato; a S piccola pesa |
| **4 nacelle di tilt** (motore + attuatore + pivot + carenatura) | +0.002 ÷ +0.004 (netto del pusher che anche il mono ha) | frontale + bagnata non trascurabili a questa scala |
| **4 giunzioni d'angolo + interferenza + fessure del pivot di tilt** | +0.002 ÷ +0.004 | drag di interferenza notoriamente alto low-Re |
| **Totale incrementale** | **+0.009 ÷ +0.017** | → **CD0_box ≈ 0.037 ÷ 0.045** |

**Verdetto:** CD0 realistico del BOXTILT ≈ **0.038–0.040 (base)**, **0.034 (best, airframe estremamente pulito)**, **0.045 (worst)**. Il valore 0.034 della sim è il **fondo della banda**, non la mediana. `[STIMA, confidence media]`

### 1.2 e = 1.05 (span efficiency) — **difendibile come base, ma è la leva sbagliata su cui contare** `[STIMA, confidence media]`

Con gap 0.4 m su b = 3 m si ha **h/b ≈ 0.13**. Il Prandtl *ideale* dà e_box ≈ 1.30–1.33 a questo h/b (`22` §1.1). Scalando l'efficienza reale del monoplano (e_mono = 0.80, cioè 80% dell'ideale) allo stesso rapporto: 0.80 × 1.33 ≈ **1.06**. Quindi **e = 1.05 è coerente con Prandtl reale a h/b = 0.13** — non è gonfiato in sé.

**Il problema non è il valore di e, è il suo peso.** In crociera C3 il CDi vale ~0.016–0.021 su un CD totale ~0.050–0.065: la componente indotta è **minoritaria** (regime attrito-dominato, `R6` §2). L'intero guadagno di e (1.05 vs 0.80) vale ΔCDi ≈ **−0.005** sul drag totale; ma il CD0 realistico è **+0.004 ÷ +0.011 più alto** dell'assunto 0.034. **I due effetti si elidono** — che è esattamente il verdetto consolidato "vantaggio d'ala netto ≈0% a C3", qui **né confermato come penalità né ribaltato come vantaggio: è un pareggio genuino**, perché l'assenza di dischi morti toglie la penalità che rendeva il box *sfavorevole* nel caso lift+cruise. Inoltre, usare **AR = 13 *e* e = 1.05** rischia un lieve doppio conteggio del beneficio d'apertura non-planare.

### 1.3 Download in hover 0.14 — **plausibile, lievemente ottimistico, poco influente** `[STIMA, confidence bassa-media]`

Due ali nella scia dei rotori: 0.14 vs 0.08 del monoplano è ragionevole se i 4 rotori stanno ai **4 spigoli** (ali largamente fuori dal nucleo di scia). Banda realistica **0.14–0.20**. Impatto sul risultato: **piccolo**, perché per un delivery C3 l'hover è solo decollo/atterraggio (frazione di missione minima); il +8% di potenza hover incide sul range di pochi punti. Non è qui il problema.

### 1.4 Penalità di massa VTOL 15% MTOM — **ottimistica e probabilmente al contrario** `[STIMA, confidence media]`

La sim assegna al BOXTILT **15%** contro il **18%** del lift+cruise. Questo è discutibile: **un tilt-rotor è più pesante per-rotore di un lift-rotor fisso**, non più leggero. Il BOXTILT aggiunge **4 attuatori di tilt + 4 cuscinetti di pivot + rinforzo strutturale ai 4 nodi + elettronica/logica di tilt**, e i 4 motori devono essere dimensionati per il **massimo tra spinta di hover e spinta di crociera**. Il risparmio reale (niente booms dedicati — il telaio box porta i rotori agli spigoli, `22` §2.2 — e niente motore pusher separato) è **compensato o superato** dai 4 attuatori e dai rinforzi.

**Verdetto:** penalità realistica **18% (base) ÷ 21% (worst)**, non 15%. Conseguenza diretta entro il tetto duro 25 kg: m_batt scende da 7.75 kg (sim) a **7.0 ÷ 6.25 kg**. La sim "nasconde" questo fissando il payload a 3.5 kg e scaricando tutto sulla batteria; nella realtà i 4 meccanismi erodono **payload *o* batteria** — e quindi il range stesso che il concept rivendica.

---

## 2. Banda onesta worst / base / best (rifatto il conto)

Rifatti i conti con CL crociera = 0.829 (fissato da W, S, V, ρ), AR = 13, range = 1.82 · m_batt · (L/D) — costante validata contro la sim.

| Scenario | CD0 | e | m_batt [kg] | CDi | CD | **L/D** | **Range [km]** | vs LIFTCRUISE | vs RETRACT |
|---|---|---|---|---|---|---|---|---|---|
| **BEST** (= assunzioni sim) | 0.034 | 1.05 | 7.75 (15%) | 0.0160 | 0.0500 | **16.6** | **234** | **+44%** | **+15%** |
| **BASE** (realistico) | 0.040 | 0.95 | 7.00 (18%) | 0.0177 | 0.0577 | **14.4** | **183** | **+13%** | **−10%** |
| **WORST** (conservativo) | 0.045 | 0.88 | 6.25 (21%) | 0.0191 | 0.0641 | **12.9** | **147** | **−9%** | **−28%** |
| *Rif. LIFTCRUISE COTS* | 0.044 | 0.80 | 7.00 | 0.0210 | 0.0650 | 12.75 | 162 | — | — |
| *Rif. RETRACT (SUPAIR-like)* | 0.031 | 0.80 | 7.00 | 0.0210 | 0.0520 | 15.93 | 203 | — | — |

**Letture chiave:**

1. **Il "+44% range" è il corner ottimistico, non il valore atteso.** La banda realistica di range vs lift+cruise COTS è **−9% ÷ +44%, centrale ≈ +10÷15%**.
2. **Il benchmark corretto non è il lift+cruise a dischi morti, è il RETRACT.** Entrambi (BOXTILT e RETRACT) hanno la crociera *pulita* senza dischi morti; ma il RETRACT è **meccanicamente molto più semplice** (pod retrattili + 1 pusher, nessuna transizione di tilt, `18`). Contro il RETRACT, il BOXTILT è **+15% solo nel best case** e **perde (−10÷−28%) nel base/worst**. **L'edge del BOXTILT esiste solo nel corner ottimistico e solo contro un avversario scelto male.**
3. Il segno positivo residuo nel base case (+13% vs lift+cruise) è **reale e attribuibile all'unica cosa vera del concept: niente dischi morti in crociera** — ma è lo stesso beneficio che il RETRACT ottiene con un decimo della complessità.

**Falsifying observation #1** `[FATTO su richiesta]`: se un RANS γ-Reθ a Re≈2–4×10⁵ del box completo (2 ali + 2 paratie + 4 nacelle + giunzioni) restituisce **CD0 ≥ 0.040**, la L/D di crociera scende a ≤14 e **il +44% collassa a ≤+15% vs lift+cruise e a ≤0% vs RETRACT** → l'edge aerodinamico è falsificato.

**Falsifying observation #2**: se la span efficiency **realmente conseguita e ≤ 0.90** (ala posteriore nella downwash dell'anteriore + effetti viscosi low-Re), il risparmio indotto che regge il risultato evapora e il BASE scivola verso il WORST.

---

## 3. Transizione e controllo — dove il concept si gioca davvero (non coperto dall'L0)

Il concept specifico è **4 tilt-rotor con tilt opposto anteriore/posteriore**. Chiarimento cinematico preliminare: "traente" (elica avanti al pivot) e "spingente" (elica dietro al pivot) sono una distinzione **di packaging del disco**, non di verso della spinta — in crociera **entrambe le coppie producono spinta in avanti** e in transizione **entrambe le coppie spazzano il vettore spinta da "su" a "avanti"** nella stessa direzione angolare. Questo è un bene: se front e rear sono sincronizzati, l'equilibrio di beccheggio in transizione **è gestibile**. Ma restano quattro problemi reali che la polare non vede.

### 3.1 Autorità e momento di beccheggio in transizione `[STIMA, confidence media]`
Durante la transizione la componente verticale di spinta decade e il peso deve trasferirsi sull'ala. I 4 vettori di spinta (2 avanti-CG, 2 dietro-CG) generano momenti di beccheggio il cui **braccio è fissato dalla geometria chiusa del box** — meno libertà di trimmatura di una configurazione a superfici separate. Il **differenziale di tilt front/rear** è simultaneamente **autorità di controllo di pitch** e **sorgente di disturbo**: richiede una legge di tilt-schedule coordinata con l'elevatore e con la spinta differenziale. Fattibile, ma è **la regione di volo più difficile** — la stessa già segnalata come punto debole della famiglia tilt in `14` §4.5.

### 3.2 Rotori posteriori spingenti nella scia — efficienza propulsiva degradata `[STIMA, confidence media]`
I 2 pusher posteriori operano **nella scia dell'ala posteriore (e in parte dell'ala/rotori anteriori)**: flusso disturbato → **η_p reale della coppia posteriore verosimilmente 0.65 anziché 0.72**, più carichi non stazionari (vibrazione, rumore, fatica sul pivot di tilt). Il mandato lo segnala esplicitamente ("propeller in scia coda: attenzione"). **Falsifying observation #3**: se η_p dei pusher misura ≤0.65, la potenza di crociera sale ~10% e il **−23% Pcruise** si riduce a ~−13%.

### 3.3 Guasto di un solo attuatore di tilt a metà transizione — **il modo di guasto critico** `[STIMA, confidence media-alta]`
Questo è il vero discriminante di sicurezza. Se **1 dei 4 attuatori si inceppa a ~30–60°**:
- il suo diagonale è già orizzontale → **asimmetria accoppiata roll + yaw + pitch**;
- il velivolo **non può completare la transizione** (un rotore bloccato a mezz'aria = grande drag + impossibile sostentamento wing-borne pulito);
- si crea uno stato **potenzialmente non recuperabile a bassa quota** (la transizione avviene vicino al suolo, sopra la valle di Pentema).

Confronto diretto del carico di controllo e dei modi di guasto:

| Architettura | Attuatori di transizione | Guasto tipico in transizione | Recuperabilità |
|---|---|---|---|
| **Lift+cruise COTS (A2)** | **0** (rotori a orientamento fisso) | motore lift ko → restano 3 + già wing-borne; motore cruise ko → plana | **Alta** (nessuno stato di transizione instabile) |
| **RETRACT (SUPAIR-like)** | 2–4 (retrazione pod) | pod non retrae → si vola wing-borne con extra drag, **controllabile** | **Alta** (guasto benigno = degrado di range, non perdita di controllo) |
| **BOXTILT (concept)** | **4 (tilt)** | jam a metà tilt → **asimmetria non trimmabile, stato non recuperabile** | **Bassa** |

**Ranking di robustezza di transizione: lift+cruise > RETRACT ≫ BOXTILT.** Il BOXTILT ha **la transizione più difficile e i modi di guasto peggiori**, e aggiunge **4 nuovi single-point failure critici** proprio nella fase a bassa quota su area popolata → impatto diretto su **SORA / ground risk** (rilevante per il pilota Pentema).

**Falsifying observation #4**: se una simulazione 6-DOF di transizione mostra che un jam di un attuatore a 30–60° diverge in modo accoppiato roll/yaw/pitch entro pochi secondi alla quota di transizione, il concept **non supera la barra SORA di rischio a terra** per il volo su Pentema — showstopper di sicurezza **indipendente dall'aerodinamica**.

### 3.4 Sincronizzazione e VRS
I 4 attuatori richiedono **sincronizzazione stretta di angolo e rate** (sensori di posizione ridondati + controllore di tilt dedicato) per evitare momenti asimmetrici transitori → **onere avionico e di V&V** (legge di controllo di tilt safety-critical). Il **vortex-ring-state** in discesa/transizione è un rischio comune a tutti i multirotore, qui reso più complesso dal flusso semi-confinato tra le due ali; mitigabile con escape laterale, ma è **ulteriore carico di controllo**. Netto: il carico di controllo del BOXTILT è **nettamente superiore** sia al lift+cruise sia al retrattile.

---

## 4. Strutture e aeroelasticità — il box C3 resta rigido, ma i 4 tilt cambiano il quadro

Il verdetto consolidato (`18`/`R6`/`22`) è corretto: un box C3 (b ≤ 3 m, V ~28 m/s, CFRP) è **rigido**, con Vf verosimilmente ≫ Vd e rischio flutter/buckling **basso** *per l'ala pulita*. Ma il BOXTILT non è un box pulito: mette **4 masse concentrate (motore + elica + attuatore, ~0.8–1.5 kg ciascuna) agli spigoli/estremità**, sui pivot di tilt. Questo introduce due elementi nuovi:

1. **Whirl flutter [STIMA, confidence media].** È **il** modo aeroelastico proprio dei tilt-rotor (gyroscopici dell'elica + flessibilità del pilone/pivot; eredità V-22). Il **pivot di tilt introduce esattamente il DOF rotazionale morbido dove vive il whirl flutter.** A scala C3 con CFRP rigido è **probabilmente OK**, ma è un **modo nuovo, non presente nel lift+cruise né nel box pulito**, e va verificato con margine dedicato — non si può ereditare il "no flutter" del box pulito.
2. **Riduzione dei margini di flutter bending-torsion.** Masse agli spigoli/punte **abbassano** Vf. A V = 28 m/s resta verosimilmente Vf > Vd, ma **il margine si assottiglia** rispetto al box pulito → va dimostrato, non assunto.

**Buckling:** invariato dal caso box (membratura posteriore/inferiore in compressione, `22` §3), **ma** i nodi d'angolo ora incanalano anche spinta e carichi gyroscopici del rotore attraverso il cuscinetto di tilt → **percorso di carico più complesso e fatica al pivot**.

**Massa dei meccanismi e frazione payload:** vedi §1.4. La penalità 15% è ottimistica; realistico 18–21%. Entro il tetto duro 25 kg, **i 4 tilt erodono direttamente payload + batteria** → la frazione payload "14% costante" della sim è un artefatto di modellazione.

**Falsifying observation #5**: se l'analisi di whirl flutter con le 4 masse d'angolo sui pivot dà **Vf < 1.2·Vd**, l'assunto "box C3 rigido → niente flutter" è falsificato e serve irrigidimento (massa aggiuntiva), che erode ulteriormente il payload.

**Falsifying observation #6**: se il download in hover sulle due ali misura **≥ 0.20** (vs 0.14), la potenza di hover supera il lift+cruise di >15% e la fase energeticamente critica (decollo/atterraggio) è penalizzata oltre l'assunto.

**Falsifying observation #7**: se la massa reale dei 4 meccanismi di tilt supera **18% MTOM**, m_batt scende ≤ 7.0 kg e la **parità di range col lift+cruise si perde anche con L/D ottimistica** → il concept perde la sua unica giustificazione prestazionale.

---

## 5. "Aerodinamicamente funziona" è difendibile?

**Dove regge** `[FATTO/STIMA, confidence media]`:
- La configurazione **è volabile**: box-wing tilt esistono come dimostratori (TiltOne, `18`).
- **Assenza di dischi morti in crociera è un vantaggio reale** rispetto a un lift+cruise naïf, e il beneficio di drag indotto del box (e più alto) è fisico.
- A scala C3 l'ala è **abbastanza rigida** perché il flutter sia probabilmente (non certamente) gestibile.
→ "Vola e cruise-a in modo ragionevole" **è difendibile**.

**Dove si rompe** `[STIMA, confidence media-alta]`:
- Il **vantaggio aerodinamico *netto*** su un benchmark equo (monoplano pulito, o RETRACT) è **≈0% ÷ leggermente negativo** in crociera — stesso verdetto di `R6`/`22`, perché il risparmio indotto è mangiato da 2 ali + 2 paratie + 4 nacelle + giunzioni a basso Re. Il +44% è un artefatto di (a) corner ottimistico su due leve e (b) benchmark scelto male.
- **"Aerodinamicamente funziona" è la domanda sbagliata.** Il vero collo di bottiglia **non è l'aerodinamica** — che è un pareggio — ma il **controllo di transizione, i modi di guasto dell'attuazione di tilt (jam = perdita di controllo a bassa quota), il whirl flutter nuovo e la massa dei 4 meccanismi**. Dichiarare "aerodinamicamente funziona" come se chiudesse la questione è un **errore di categoria**: l'aerodinamica è il *minore* dei problemi del concept.

**Il vero collo di bottiglia tecnico (in ordine):**
1. **Controllo di transizione + modi di guasto** (jam di un attuatore a metà tilt sopra area popolata) — rischio dominante, legato a **TRL 3–4** e a **SORA/ground risk**.
2. **Massa/affidabilità dei 4 meccanismi di tilt** entro il tetto 25 kg — erode il range stesso che il concept rivendica.
3. **TRL / build-not-buy:** nessun COTS box-tilt C3, nessun volo di riferimento → contraddice il modello **operatore-non-OEM** (`CLAUDE.md`).

Aerodinamica e struttura pura sono **né il vantaggio rivendicato né lo showstopper**: sono un wash. Il rischio è tutto in **controllo e massa**.

---

## 6. Cosa cambierebbe con una vera L2 — piano minimo di 2 simulazioni

**Input incerti che dominano il risultato** (in ordine di leva sul verdetto):
- (a) **CD0 reale** del box con 4 nacelle + 2 paratie + giunzioni a Re≈2–4×10⁵ → decide se la crociera è +15% o −10%.
- (b) **e reale** conseguita sotto effetti viscosi low-Re (1.05 o 0.90?).
- (c) **η_p dei pusher posteriori** nella scia d'ala (0.72 o 0.65?).
- (d) **download in hover** con due ali (0.14 o 0.20?).
- (e) **controllabilità del corridoio di transizione** e recuperabilità del jam — **non affrontabile con nessuna polare**, serve 6-DOF.

**Piano minimo (2 simulazioni) per falsificare/confermare:**

| # | Simulazione | Metodo | Cosa falsifica/conferma | Costo/tempo `[STIMA]` |
|---|---|---|---|---|
| **Sim 1 — crociera** | VLM (AVL/XFLR5) della geometria box esatta (h/b=0.13, 2 ali, 2 paratie) per **e** e distribuzione di portanza → poi **RANS γ-Reθ** su box + 4 corpi-nacelle a Re di crociera per il **CD0 breakdown** (attrito + interferenza + nacelle) e la L/D netta; include disco attuatore del **pusher in scia** per η_p reale | VLM → RANS transizionale L1→L2 | Falsifica/conferma il +44% (atteso: collasso verso ≈0% vs benchmark pulito). Risolve (a)(b)(c) | €50–120k, 3–5 mesi |
| **Sim 2 — transizione + hover** | **URANS / disco attuatore** in hover per il download sulle due ali; **6-DOF transizione** (blade-element + corpo rigido) sweeping del tilt-schedule, **incluso il caso jam di un singolo attuatore** a 30–60° | URANS + 6-DOF flight dynamics | Testa il **vero collo di bottiglia** (controllo): margini di autorità in transizione e **recuperabilità del jam** → risolve (d)(e); nessuna polare può farlo | €40–100k, 3–5 mesi |

Ordine imposto: **Sim 2 pesa più di Sim 1 per la decisione**, perché anche un esito aero favorevole (Sim 1) non salva il concept se Sim 2 mostra il jam non recuperabile alla quota di transizione.

---

## Riga di fondo

> Le assunzioni della simulazione **non sono eque: sono il corner ottimistico** — e alta (difendibile ma non su cui contare), CD0 basso (fondo banda), penalità massa 15% (ottimistica e probabilmente al contrario, un tilt-rotor pesa *più* di un lift-rotor fisso) — e per giunta il BOXTILT è confrontato col peggior VTOL possibile (dischi morti) invece che col benchmark corretto (RETRACT, anch'esso pulito in crociera). Rifatto onestamente il conto, il **+44% di range diventa +10÷15% base (−9% worst) vs lift+cruise COTS**, e **≤0% contro il retrattile** — che è dieci volte più semplice. **L'unica cosa vera del concept è che nessun disco è morto in crociera**: questo rende l'aerodinamica un **pareggio genuino** (non la penalità del caso lift+cruise, né il vantaggio rivendicato) — coerente con il verdetto consolidato "ala ≈0% a C3". Ma **"aerodinamicamente funziona" è la domanda sbagliata**: l'aerodinamica è il *minore* dei problemi. Il **vero collo di bottiglia è il controllo di transizione** — 4 tilt opposti, sincronizzazione safety-critical, e soprattutto il **jam di un singolo attuatore a metà transizione = stato non recuperabile a bassa quota su Pentema (rischio SORA)** — seguito dalla **massa dei 4 meccanismi** (che erode il range rivendicato) e dal **whirl flutter**, un modo aeroelastico nuovo che il "box rigido C3" non copre. **Netto: il concept vola, ma non offre un edge prestazionale decisivo e importa il regime di controllo più difficile e i modi di guasto peggiori. Resta una linea dimostratore R&D, non un prodotto operativo** — e la prova che potrebbe (o dovrebbe) sbloccarlo è il piano da 2 simulazioni, con la Sim 2 (transizione + jam) che pesa più della polare. `[confidence aggregata: media]`

---

## Fonti e limiti

- **Interne:** `sim_boxwing_tiltrotor.py` (rieseguita e verificata), `18-boxwing-tiltrotor-rivalutazione.md`, `22-boxwing-vantaggio-tecnico.md`, `ricerca-approfondita/R6-boxwing-aerodinamica.md`, `14-vtol-config-tradestudy-C3.md`.
- **Metodo:** band worst/base/best su calcolo chiuso (CL fissato da W/S/V/ρ; range = 1.82·m_batt·L/D, costante validata contro la sim). Component drag build-up L0. Analisi di controllo/aeroelasticità **qualitativa L0/L1**.
- **Limiti dichiarati:** nessun VLM/RANS/URANS/6-DOF eseguito (è precisamente il piano §6); i valori di CD0 incrementale, e reale, η_p pusher, download, e masse dei tilt sono **stime ingegneristiche non validate**. La conclusione **robusta** è il **segno e l'ordine dei rischi** (controllo > massa > aerodinamica), non i valori assoluti. Il whirl flutter e la recuperabilità del jam sono i due punti a più alta incertezza e a più alta leva sul verdetto → priorità di L2.
