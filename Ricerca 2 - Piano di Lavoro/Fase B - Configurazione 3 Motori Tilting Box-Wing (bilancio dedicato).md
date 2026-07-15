# Fase B — Configurazione "3 Motori Tilting" su Box-Wing (bilancio dedicato)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio dedicato di una configurazione **finora non contemplata**: cellula **box-wing** con **3 rotori tutti tiltanti** — **2 traenti + 1 spingente** — che fanno sia il decollo verticale (VTOL) sia la crociera. Rifà, **solo per questa configurazione**, il **bilancio energetico, di massa, l'elettronica necessaria, il peso dei supporti/meccanismi di tilt e gli ESC** |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Input** | `Trade Propulsione` (§2–§4 tassonomia, §4.2 potenza VTOL, §7.5 tilt-rotor), `Bilancio di Massa ed Energia` (CFG-A/CFG-B, metodo), `Studio Motori Brushless ed ESC` (catena elettrica), `WP-B5` (box-wing TRL 4–5, simulazioni interne promettenti) |
| **Scopo** | Contemplare, **senza modificare i documenti esistenti**, il caso a **3 rotori tutti in assetto tiltante (2 traenti + 1 spingente) su box-wing**, con i suoi bilanci dedicati. È un **documento additivo**: non ridiscute né sostituisce le configurazioni A1/A2/A3 già studiate — le affianca. |
| **Powertrain** | **Genset (ibrido-serie) obbligato** — vedi §2 (un termico non può azionare in asse 3 rotori basculanti). |

> ⚠️ **Onestà tecnica (coerente col Dossier di Verifica):** tutti i pesi/energie sono **stime parametriche first-order** con banda esplicita, calcolate qui. Il **box-wing è a TRL 4–5** e il **tilt-rotor ibrido a 25 kg non esiste in commercio** (`Trade Propulsione` §7.5): questa configurazione **cumula** entrambe le immaturità → i numeri sono da validare con CFD, banco e dimostratore, non da consolidare. Nessun numero è misurato sul nostro sistema.

> 📌 **Nota di ambito (non tocca gli altri file):** questo studio introduce una configurazione che chiamiamo internamente **"3-TILT box-wing"**. Non rinumera né modifica A1/A2/A3 del `Trade Propulsione` né le CFG-0/A/B del `Bilancio di Massa`. Dove serve un confronto, li **cita in sola lettura**.

---

## 0. Executive summary

1. **Cos'è:** un **box-wing** (ala anteriore + ala posteriore chiuse) con **3 gruppi motopropulsori tutti basculanti**: **2 traenti** (sull'ala anteriore) + **1 spingente** (posteriore). In hover i 3 rotori puntano in alto; dopo la transizione basculano in orizzontale e diventano i propulsori di crociera. **Nessun rotore "morto" in crociera** e **nessun motore di crociera dedicato** (i 3 tilt fanno tutto).

2. **È serie obbligato (genset):** come per il tilt-rotor a 4 motori (A3), un termico **non può** azionare in asse 3 rotori che basculano → **ICE→alternatore/PMSG→bus DC+buffer→3 ESC→3 motori**. Eredita quindi la penalità di doppia conversione (~5–12%).

3. **Il numero dimensionante (24 kg MTOM):** hover **8,0 kgf/rotore** (contro 6,0 kgf a 4 rotori). Per **pareggiare** la potenza di hover del 4-rotori servono **eliche più grandi (Ø~0,66–0,71 m)**; a parità di diametro il 3-rotori paga **~15% di potenza di hover in più** (disk loading 330 vs 248 N/m²).

4. **La penalità che conta è in CROCIERA, non in hover.** I 3 motori sono dimensionati per l'**hover** (~2–3 kW ciascuno); in crociera servono **~400 W totali** → ogni motore girerebbe a una frazione minima del suo punto ottimo → **efficienza di crociera scadente**. Poiché la crociera è **~98% della missione** (`Studio Motori Brushless` §2), questa è la vera minaccia all'endurance. Mitigazione: **crociera su 1 solo rotore** (lo spingente) con i 2 traenti **in bandiera/fermi** — ma richiede **eliche a passo variabile/feathering**, che aggiungono massa e complessità.

5. **Bilancio di massa (24 kg target, payload 4 kg, VTOL integrato):** **≈ 27–28 kg** con ambizione piena → **sfonda C3 di ~3 kg**, come già la CFG-B a 4-lift+1-cruise. Per rientrare valgono le stesse leve del `Bilancio di Massa` (payload e/o carburante). Il **meccanismo di tilt (×3) aggiunge ~1,2–1,6 kg** che le configurazioni a rotori fissi non hanno (§7).

6. **Elettronica (§8):** **3 ESC** classe 80–120 A (niente ESC di crociera dedicato) + **3 servoattuatori di tilt ad alta coppia** + **BEC servi robusto e ridondante** + **flight controller con legge di transizione/vettorizzazione**. Più complessa (software e failure modes) di un lift+cruise.

7. **I due rischi esistenziali:** **(a)** con 3 rotori **non c'è ridondanza di hover** — la perdita di un rotore/ESC in hover **non è recuperabile** (un tri-rotore non regge l'assetto su 2); **(b)** ogni **attuatore di tilt è un guasto a punto singolo in transizione** (×3). Sommati al **TRL più basso del corpus** (box-wing 4–5 **+** tilt-rotor ibrido inesistente in classe), fanno di questa la configurazione **più affascinante e più rischiosa**.

> **Verdetto sintetico:** il **3-TILT box-wing** è la variante **più compatta e "da vetrina"** (allineata al binario MAKE box-wing di `WP-B5`, con bonus normativo dell'apertura ≤ 3 m → C3), ma **paga la stessa penalità di crociera del tilt-rotor** su ciò che conta di più (endurance) e **peggiora la ridondanza**. Ha senso **solo** come **traccia R&D finanziata** (EDF/PNRM/DIANA) o se la validazione box-wing conferma un guadagno aerodinamico tale da **compensare** la penalità di propulsione. Per il **prodotto certificabile a breve** resta preferibile il genset a 5 motori (A2) del corpus.

---

## 1. Definizione della configurazione

### 1.1 Geometria
- **Cellula:** box-wing (ala anteriore bassa + ala posteriore alta, unite alle estremità). Compatta a parità di prestazione (simulazioni interne `WP-B5`) → **apertura potenzialmente ≤ 3 m** (bonus classe C3).
- **3 gruppi motopropulsori, tutti basculanti:**
  - **2 traenti** alle estremità/gondole dell'**ala anteriore**;
  - **1 spingente** posteriore (in coda/sull'ala posteriore, sull'asse di simmetria).
- **VTOL:** i 3 rotori ruotano a puntare in alto → tri-rotore in hover (triangolo: 2 avanti + 1 dietro).
- **Crociera:** i 3 rotori basculano in orizzontale → 2 traenti + 1 spingente spingono in avanti.

### 1.2 Cosa la distingue dalle configurazioni già studiate
| | A1/A2 (5 motori) | A3 (4 tilt-rotor) | **3-TILT box-wing (questo doc)** |
|---|---|---|---|
| Cellula | ala fissa | ala fissa | **box-wing** |
| N. rotori | 5 (4 lift + 1 cruise) | 4 (tutti tilt) | **3 (tutti tilt)** |
| Rotori "morti" in crociera | 4 (A1) / 0 (A2 elettrico) | 0 | **0** |
| Motore crociera dedicato | sì | no | **no** |
| Meccanismo di tilt | no | ×4 | **×3** |
| Ridondanza hover | ✅ (4 rotori) | ⚠️ (4 rotori, limite) | ❌ **(3 rotori, nessuna)** |
| Powertrain | serie o diretto | **serie obbligato** | **serie obbligato** |

---

## 2. Perché è "serie obbligato" (genset)

Identico al ragionamento del `Trade Propulsione` §2.4 per il tilt-rotor: per avere la spinta "in asse al termico" l'albero motore dovrebbe azionare **meccanicamente** i rotori; ma qui i rotori **basculano** e sono distribuiti (2 avanti + 1 dietro) → **un solo termico non può azionarli** (servirebbero 3 alberi cardanici basculanti, assurdo), e **3 termici basculanti** sono improponibili (massa, vibrazioni, sincronizzazione). **Unica opzione sensata: un solo genset che alimenta i 3 motori elettrici via bus DC + buffer.** → Il 3-TILT **impone l'architettura serie** e ne eredita la **penalità di doppia conversione (~5–12%)** e i suoi vantaggi (regime ottimale, modo silenzioso, ridondanza a batteria per il **rientro** — ma **non** per l'hover, vedi §3.4).

---

## 3. Dimensionamento hover e controllo

### 3.1 Spinta e potenza di hover (24 kg MTOM)
| Config | kgf/rotore (hover) | Elica | Area disco tot | Disk loading | **P_elettrica hover** (FoM 0,62; η_mot+ESC 0,85) |
|---|---|---|---|---|---|
| 4 rotori (rif. A-series) | 6,0 | Ø0,55 | 0,95 m² | 248 N/m² | **~4,5 kW** |
| **3 rotori — stesse eliche** | **8,0** | Ø0,55 | 0,71 m² | **330 N/m²** | **~5,2 kW (+15%)** |
| **3 rotori — eliche grandi** | 8,0 | Ø0,66 | 1,03 m² | 229 N/m² | **~4,3 kW (≈ pari)** |
| 3 rotori — eliche molto grandi | 8,0 | Ø0,71 | 1,19 m² | 198 N/m² | ~4,0 kW (meglio) |

> **Lettura:** per non pagare potenza di hover, il 3-TILT **deve** montare eliche più grandi (Ø~0,66–0,71 m). Su una cellula **box-wing compatta** questo è un **vincolo geometrico stretto** (ingombro elica vs corda/apertura ridotte) → probabile compromesso verso dischi più piccoli → **~+15% di potenza di hover** rispetto al 4-rotori. Il picco resta **coperto dalla batteria buffer** (peak-shaving), quindi non ridimensiona il genset (`Trade Propulsione` §4.3), ma **aumenta l'energia del buffer** e lo stress termico degli ESC lift.

### 3.2 Margine e picco per rotore
Hover 8,0 kgf; per autorità di controllo (assetto + raffiche in transizione) **~1,6–1,8×** → **~13–14 kgf/rotore di picco**. Motori classe **T-Motor U11/U13, MAD M10/V8010** (vedi `Studio Motori Brushless` §3.3). Nota: 8 kgf di hover per rotore è **il punto di lavoro continuo del VTOL** → serve un motore che lo regga **freddo per 2–4 min**, non solo un picco di targa.

### 3.3 Controllo in hover (tri-rotore vettorizzato)
- **Rollio/beccheggio:** spinta differenziale tra i 3 rotori.
- **Imbardata:** **vettorizzazione** — inclinazione differenziale dei rotori basculanti (un tri-copter classico imbarda inclinando il rotore di coda; qui **tutti e 3** basculano → autorità d'imbardata ampia). **Vantaggio** del "tutti tiltanti": l'imbardata in hover è forte e diretta.
- **Costo:** i servoattuatori di tilt diventano **attuatori di volo primari anche in hover** (non solo per la transizione) → devono essere **veloci, precisi e ridondanti** (§8).

### 3.4 Il limite di sicurezza: nessuna ridondanza di hover
> ⚠️ Con **3 rotori** la perdita di **un** rotore/ESC/motore in hover **non è recuperabile**: un tri-rotore non può bilanciare assetto e portanza su **2** rotori (a differenza di un quad, che in alcuni casi degrada a discesa controllata). Questo è un **downgrade di sicurezza reale** rispetto alle configurazioni a 4+ rotori. La **ridondanza a batteria del genset** copre l'**avaria del termico in crociera** (rientro), **non** la perdita di un rotore in hover. → In termini di *safety case* SORA/ENAC, il 3-TILT parte **svantaggiato** in decollo/atterraggio.

---

## 4. Crociera: la penalità di carico parziale (il vero costo)

I 3 motori sono dimensionati per l'**hover** (~2–3 kW/rotore di picco). In crociera il velivolo chiede **~400 W totali** (banda 350–500 W; il box-wing *potrebbe* abbassarla se le simulazioni interne di miglior L/D si confermano — **da validare**). Due strategie:

| Strategia di crociera | Come | Efficienza propulsiva | Complessità |
|---|---|---|---|
| **(a) Tutti e 3 a basso carico** | ~130 W/motore | ❌ **Scadente**: motore da 2–3 kW a ~130 W è ben sotto il picco della sua curva η → **η ~75–82%** invece di 89–91% | bassa (nessun feathering) |
| **(b) Crociera su 1 (spingente), 2 traenti in bandiera** | il pusher fa i ~400 W; i 2 traenti fermi/feathered | ✅ **Migliore**: 1 motore più vicino a un punto sensato; niente drag di windmilling **se** le eliche vanno in bandiera | ⚠️ richiede **eliche a passo variabile/feathering** o stop-fold → **+massa, +complessità, +failure modes** |

> **Il nodo:** la strategia (a) ripropone in pieno la **penalità di carico parziale del tilt-rotor** (`Trade Propulsione` §2.3/§6, "eliche di compromesso") su **tutta** la crociera. La strategia (b) la mitiga ma **compra complessità** (feathering ×2) che erode il vantaggio di "meno parti" del 3-rotori. **In entrambi i casi la crociera del 3-TILT è, sul piano propulsivo, meno efficiente del motore di crociera dedicato di A2** (basso-KV, alto numero poli, ottimizzato per i 400 W — `Studio Motori Brushless` §4). Questa penalità agisce sul **98% della missione**.

---

## 5. Bilancio ENERGETICO dedicato

**Assunzioni:** MTOM 24 kg, crociera ~400 W (banda 350–500 W; potenziale sconto box-wing **non** contabilizzato finché non validato), endurance obiettivo ~20 h, genset serie.

| Voce energetica | Stima | Note |
|---|---|---|
| Fabbisogno crociera (albero) | ~350–400 W | come corpus; box-wing potrebbe ridurlo (da validare) |
| **η catena propulsiva crociera** | **(a) ~0,80–0,86** / (b) ~0,86–0,90 | (a) 3 motori a carico parziale; (b) 1 motore + feathering |
| Confronto con A2 (motore crociera dedicato) | A2 ~0,89–0,91 | **il 3-TILT perde ~3–9 punti** in (a), ~1–5 in (b) |
| Penalità serie (doppia conversione) | +5–12% carburante | ereditata (§2), **già** in tutte le config serie |
| Energia crociera/24 h | ~9,6 kWh (banda 8,4–12) | `Bilancio di Massa` §3.1 |
| **Extra-consumo di crociera del 3-TILT vs A2** | **+3–9% (strategia a) / +1–5% (strategia b)** sull'energia di crociera | **~0,1–0,4 kg di carburante/giorno** in più → **~0,5–2 h di endurance** in meno a parità di serbatoio |
| Energia VTOL | ~0,5–0,6 kWh (3 rotori, +15% se dischi piccoli) | dal buffer, poi ripristinata |
| **Quota VTOL sull'energia** | ~5–6% | bufferata; **non** è il driver |

> **Conclusione energetica:** il 3-TILT **non** ha un problema di hover (bufferato, ~5% dell'energia); ha un problema di **crociera** (~98% della missione), dove la propulsione tiltante è **strutturalmente meno efficiente** del motore dedicato di A2. Il **potenziale guadagno aerodinamico del box-wing** (miglior L/D) è l'**unica leva** che potrebbe **compensare** questa penalità — ma è a **TRL 4–5 e non validato**, quindi **non lo si mette a bilancio** finché CFD/galleria/dimostratore non lo confermano.

---

## 6. Bilancio di MASSA dedicato

Metodo e bande coerenti col `Bilancio di Massa` (CFG-0/CFG-B), ricalcolati per il 3-TILT. **Ambizione piena** (payload 4 kg, VTOL integrato, niente solare — già escluso dal corpus):

| Voce | Peso (kg) | Note |
|---|---|---|
| Struttura/cellula **box-wing** (2 ali + giunzioni d'estremità + fusoliera + coda) | **6,5–7,5** (design **7,0**) | box-wing più rigido ma **2 superfici + giunzioni**; compatto |
| **Rinforzi + supporti di tilt** (×3 gondole) | **1,2–1,6** (design **1,4**) | **voce nuova** — vedi §7 |
| Avionica **certificabile** + **legge di transizione/tilt** | **1,3–1,6** (design **1,45**) | +sensori posizione tilt, controllo vettorizzato |
| Datalink LOS + BLOS + antenne | **0,8** | REQ-05 |
| Genset (ICE + alternatore/PMSG + elettronica di potenza) | **3,2–4,3** (design **3,4**) | serie obbligato |
| **3 motori** (classe hover 8 kgf → U11/U13/M10) | **1,8–2,4** (design **2,1**) | 3 × ~0,6–0,8 kg |
| **3 ESC** (80–120 A) | **0,15–0,30** (design **0,22**) | niente ESC crociera dedicato |
| **3 servoattuatori tilt** (alta coppia) | **0,45–0,9** (design **0,6**) | +driver; **primari anche in hover** |
| (Feathering/passo variabile ×2, se strategia crociera b) | **+0,3–0,6** (opzionale) | costo della mitigazione §4 |
| Batteria buffer (picco VTOL 3 rotori) | **2,2–3,0** (design **2,6**) | +energia se dischi piccoli |
| Carburante (~20 h + penalità serie) | **3,8–4,6** (design **4,2**) | include extra-consumo §5 |
| Serbatoio + impianto | **0,5** | |
| Payload di progetto | **4,0** | `Studio Pesi Payload` |
| Recupero (paracadute/skid) | **0,4** | REQ-06 |
| Minuteria/margine hardware | **0,4** | |
| **TOTALE (senza feathering)** | **≈ 27,3** (banda 26–30) | **⊗ sfonda C3 di ~2,3 kg** |
| **TOTALE (con feathering, strategia b)** | **≈ 27,9** | ⊗ peggio di ~0,6 kg |

> **Lettura:** come per la **CFG-B** del corpus (~27 kg col VTOL installato), il 3-TILT **non chiude a 24 kg con payload 4 kg e VTOL integrato**. Per rientrare in C3 valgono **le stesse leve** del `Bilancio di Massa` §2.2 — **senza modificarlo**: payload 4→~1,5–2 kg **e/o** carburante −~2 kg (endurance ~20 h → ~12–14 h). Il 3-TILT **non** offre una scorciatoia di massa: i **3 motori grandi + 3 meccanismi di tilt (+feathering opzionale)** **compensano** il risparmio del "meno rotori / niente cruise dedicato".

### 6.1 Confronto di massa "propulsione" (solo le voci che cambiano)
| Blocco propulsivo | A1/A2 (4 lift + 1 cruise) | **3-TILT box-wing** |
|---|---|---|
| Motori | 4 lift + 1 cruise ≈ **2,9–4,6 kg** | 3 tilt ≈ **1,8–2,4 kg** |
| ESC | 5 ESC ≈ 0,2–0,4 kg | 3 ESC ≈ **0,15–0,30 kg** |
| Booms / supporti | booms fissi ≈ **incl. struttura** | **meccanismi tilt ×3 ≈ 1,2–1,6 kg + servi 0,45–0,9** |
| Feathering | — | opzionale **+0,3–0,6** |
| **Somma indicativa** | **~3,3–5,4 kg** | **~3,6–5,8 kg** |

> **Il 3-TILT è alla pari o leggermente più pesante sul blocco propulsivo**, nonostante "un motore in meno e nessun cruise dedicato", perché il **tilt (×3) + servi + eventuale feathering** riportano su la massa. **Non è la configurazione leggera** che l'intuizione "meno rotori" suggerirebbe.

---

## 7. Peso dei supporti / meccanismi di TILT (sezione dedicata)

Voce **assente** nelle configurazioni a rotori fissi (A1/A2) e **critica** qui, richiesta esplicitamente. Ogni gondola basculante è un sotto-sistema:

| Componente per gondola | Funzione | Massa stimata |
|---|---|---|
| **Attuatore di tilt** (servo/gearmotor alta coppia) | Ruota e **tiene** il rotore contro spinta (~8 kgf), momenti aerodinamici di transizione e **precessione giroscopica** | **0,15–0,30 kg** |
| **Albero/cuscinetti di basculamento + fine-corsa** | Asse di rotazione, rigidità, arresti | **0,10–0,25 kg** |
| **Rinforzo strutturale locale** dell'ala/gondola | Reagire carichi concentrati e momenti di transizione | **0,08–0,20 kg** |
| **Cablaggio flessibile + sensore di posizione** | Potenza motore + feedback angolo | **0,03–0,08 kg** |
| **Per gondola** | | **≈ 0,36–0,83 kg** |
| **× 3 gondole** | | **≈ 1,1–2,5 kg → design ~1,2–1,6 kg** |

**Note ingegneristiche:**
- L'attuatore deve **tenere la posizione sotto spinta** (non solo slew): dimensionamento sul **momento peggiore** (transizione con raffica), non sulla coppia statica. Sottodimensionarlo = **stallo dell'attuatore in transizione = perdita di controllo**.
- **Guasto a punto singolo:** un attuatore/albero che si **blocca o cede in transizione** è **catastrofico** (asimmetria di spinta non compensabile). ×3 gondole → **3 SPOF** in transizione. Mitigazioni (attuatori ridondanti, fail-safe verso posizione sicura) **aggiungono massa** e vanno messe a budget in Fase C.
- Rispetto ai **booms fissi** di A1/A2 (nessuna parte in movimento, integrabili nella struttura), il tilt è **massa + rischio** aggiuntivi. È il prezzo del "nessun rotore morto in crociera".

---

## 8. Elettronica necessaria

| Blocco | Cosa serve | Note (vs corpus) |
|---|---|---|
| **ESC di potenza** | **3× ESC 80–120 A HV** (12–14S), **sine/FOC** per transizione liscia e crociera a carico parziale | **niente ESC crociera dedicato**; candidati: APD 120F3 / T-Motor ALPHA 120A HV / KDE UAS95-125 (`Studio Motori Brushless` §5) |
| **Rettificazione sincrona** | su tutti e 3 gli ESC | leva di efficienza reale; utile a carico parziale (crociera) |
| **RDS(on) basso + termico** | sugli ESC (picco hover 80–100 A) | calore del burst; `Studio Motori Brushless` §6/§9 |
| **Attuatori di tilt** | **3× servoattuatori alta coppia** + driver + **encoder di posizione** | **attuatori di volo primari anche in hover** (imbardata) → banda passante e affidabilità elevate |
| **BEC servi** | **BEC dedicato ad alta corrente, ridondante**, separato dall'avionica | i servi tilt hanno transitori forti; `Studio Motori Brushless` §8 |
| **Flight controller** | FC ridondante con **legge di transizione/vettorizzazione a 3 rotori** | software più complesso; scheduling tilt, mixing non lineare nel regime a tilt parziale |
| **Genset control + buffer mgmt** | come corpus (bus DC, BMS buffer, peak-shaving) | invariato |
| **DC-DC/BEC principale** | 58→12→5 V sincrono, dual-ridondante | `Studio Motori Brushless` §8; **ZVS qui**, non negli ESC (§7 di quel doc) |

> **Sintesi elettronica:** rispetto a un lift+cruise, il 3-TILT **toglie** 1 ESC e il motore/ESC di crociera dedicato, ma **aggiunge** 3 attuatori di tilt di qualità "volo primario", il loro BEC robusto e una **legge di controllo di transizione** più complessa. Il conto **componenti** è simile; il conto **rischio software/attuatori** è **più alto**.

---

## 9. Confronto sintetico (solo per collocare la variante)

| Criterio | A2 (5 mot., serie) | A3 (4 tilt) | **3-TILT box-wing** |
|---|---|---|---|
| Endurance/η crociera | ✅ motore dedicato | ⚠️ tilt (compromesso) | ⚠️ **tilt (compromesso), su cellula da validare** |
| Ridondanza hover | ✅ 4 rotori | ⚠️ 4 rotori | ❌ **3 rotori (nessuna)** |
| Rischio meccanismo | ✅ nessun tilt | ⚠️ tilt ×4 | ⚠️ **tilt ×3 (SPOF in transizione)** |
| Massa propulsione | media | media | **pari/leggermente peggiore** (§6.1) |
| Compattezza / C3 (≤3 m) | dipende dall'ala | dipende dall'ala | ✅ **box-wing compatto (bonus)** |
| Appeal/innovazione, accesso bandi | media | media | ✅✅ **massimo (vetrina MAKE, WP-B5)** |
| TRL | alto (serie multirotor maturo) | basso (no tilt ibrido 25 kg) | ❌ **il più basso (box-wing 4–5 + tilt ibrido inesistente)** |

> Il 3-TILT **non** compete con A2 sull'endurance-a-breve; compete sul **posizionamento** (compattezza + innovazione + IP + bandi difesa), esattamente il **binario MAKE box-wing** di `WP-B5`.

**Analogo commerciale più vicino:** **Quantum Systems Vector** (tri-tilt-rotor), ma **tutto elettrico** (~2 h, batteria) e **non** ibrido/box-wing — conferma che il **tri-tilt esiste**, ma **non** in versione **ibrida-genset a lunga endurance**, che resta territorio inesplorato (`Trade Propulsione` §7.5).

---

## 10. Rischi principali

| Rischio | Impatto | Mitigazione |
|---|---|---|
| **Nessuna ridondanza di hover** (perdita di 1 rotore = non recuperabile) | **Alto (safety/SORA)** | Aumentare affidabilità motori/ESC; profilo di decollo che minimizza il tempo in hover; considerare 4+ rotori se il safety case non regge |
| **Tilt = SPOF in transizione (×3)** | Alto | Attuatori ridondanti/fail-safe; fine-corsa robusti; test di transizione estensivi |
| **Penalità di crociera (carico parziale / eliche di compromesso)** | Alto (endurance) | Strategia (b) crociera-su-1 con feathering; validare guadagno aero box-wing che compensi |
| **TRL cumulato più basso del corpus** (box-wing 4–5 + tilt ibrido inesistente) | Alto (tempo/costo) | Finanziamento R&D dual-use (EDF/PNRM/DIANA, `WP-B5`); dimostratore in scala |
| **Vincolo geometrico eliche su box-wing compatto** (dischi piccoli → +15% hover) | Medio | Trade elica/gondola; accettare +buffer; verificare clearance |
| **Sfondamento di massa (≈27–28 kg)** | Medio | Stesse leve del `Bilancio di Massa` (payload/carburante), **senza** modificarlo |

---

## 11. Raccomandazione (quando ha senso)

**Il 3-TILT box-wing è una configurazione da traccia R&D/vetrina, non la baseline certificabile a breve.**

- **Adottalo** se: (a) l'obiettivo primario è **innovazione/IP/accesso ai bandi difesa** (binario MAKE box-wing, `WP-B5`); (b) la **validazione box-wing** (CFD/galleria/dimostratore) conferma un guadagno aerodinamico che **compensa** la penalità di propulsione tiltante; (c) esiste **finanziamento dual-use** che paga il premio di rischio/TRL.
- **Non adottarlo** come prodotto certificabile a breve termine: la **mancanza di ridondanza di hover**, i **3 SPOF di tilt** e il **TRL cumulato** lo rendono più rischioso di A2 senza un vantaggio di endurance dimostrato. Per il time-to-market resta preferibile il **genset a 5 motori (A2)**.
- **Se si vuole un tilt-rotor**, valutare **4 rotori** (A3) invece di 3: recupera **un minimo di ridondanza di hover** al costo di +1 gondola.

---

## 12. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Guadagno aerodinamico reale del box-wing (compensa la penalità?) | CFD estesa + galleria + dimostratore in scala (`WP-B5`) |
| Potenza di hover reale a 3 rotori (FoM, dischi, clearance su box-wing) | Trade elica/gondola + prove di hover |
| η di crociera reale: 3 a carico parziale **vs** 1 + feathering | Banco propulsivo sui due schemi; decidere se serve il passo variabile |
| Massa/coppia reali dei meccanismi di tilt + strategia di ridondanza | Progetto di dettaglio gondola + prova attuatori (tenuta sotto spinta) |
| Legge di transizione/vettorizzazione a 3 rotori | Modello 6-DoF + SIL/HIL + volo dimostrativo |
| Safety case hover senza ridondanza (SORA/ENAC) | Analisi affidabilità + confronto con opzione 4 rotori |
| Chiusura di massa in C3 (payload/carburante) | Ri-taratura con le leve del `Bilancio di Massa` (senza modificarlo) |

---

## 13. Fonti

> Questo documento è una **sintesi ingegneristica** basata sui numeri già stabiliti nel corpus + fisica del tilt-rotor. Le fonti primarie di prodotto/architettura sono nei documenti citati e nelle loro bibliografie.

**Corpus interno (sola lettura, non modificati):**
- `Fase B - Trade Propulsione Dettagliato (Powertrain Ibrido).md` — §2.4 (tilt ⟹ serie), §4.2 (potenza VTOL), §6 (matrice), §7.5 (tilt-rotor ibrido inesistente a 25 kg), §10 (fonti tilt-rotor/serie)
- `Fase B - Bilancio di Massa ed Energia (preliminare).md` — CFG-B (~27 kg col VTOL), §2.2 (leve di riduzione), §3.1 (energia crociera)
- `Fase B - Studio Motori Brushless ed ESC (Catena Elettrica del Powertrain).md` — §2 (ripartizione missione), §3–§5 (motori/ESC), §6–§9 (RDS(on)/GaN/ZVS/BEC/termico)
- `Fase B - WP-B5 Costi TRL Make-vs-Buy.md` — box-wing TRL 4–5, simulazioni interne promettenti, binario MAKE finanziato
- `Fase B - Studio Pesi Payload (applicativi contemplati).md` — payload di progetto 4 kg

**Esterne (tilt-rotor, box-wing, tri-tilt):**
- MDPI *Aerospace* 2023, 10(2):105 — box-wing/tandem-wing solare ≤25 kg (beneficio strutturale-aeroelastico, TRL basso): https://www.mdpi.com/2226-4310/10/2/105
- Misra et al. — Review VTOL Tilt-Rotor & Tilt-Wing UAVs (Wiley 2022): https://onlinelibrary.wiley.com/doi/10.1155/2022/1803638
- Hybrid VTOL Tilt-Rotor for increased endurance (PMC8468980, solo accademico): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8468980/
- Impatto del drag delle eliche di lift su lift+cruise/tilt eVTOL (ScienceDirect): https://www.sciencedirect.com/science/article/abs/pii/S1270963820311111
- Quantum Systems **Vector** (tri-tilt-rotor, solo elettrico — analogo più vicino): https://quantum-systems.com/vector-ai/

---

*Analisi first-order stage-appropriate. Pesi/energie parametrici con banda esplicita, da validare con CFD, banco e dimostratore. Conclusione: il **3-TILT box-wing** è **compatto e ad alto appeal** ma **eredita la penalità di crociera del tilt-rotor** (sul 98% della missione), **peggiora la ridondanza** (nessun recupero in hover), **aggiunge ~1,2–1,6 kg di meccanismi di tilt** e ha il **TRL cumulato più basso** del corpus. Baseline certificabile a breve → resta il genset a 5 motori (A2); il 3-TILT è una **traccia R&D/vetrina finanziata**. Questo documento è **additivo** e non modifica i file esistenti.*
