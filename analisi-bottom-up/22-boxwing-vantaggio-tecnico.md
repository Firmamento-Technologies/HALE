# BOXY — Il box-wing dà un vantaggio tecnico REALE per un VTOL cargo C3? Analisi di prima approssimazione

> **Volume:** Analisi bottom-up pre-Studio — approfondimento tecnico su richiesta, di seguito a `10-fasce-engineering.md` §3 (fascia T1 "BOXY")
> **Data:** 8 luglio 2026
> **Autore:** Aerodynamics & Structures Engineer
> **Livello di fidelity:** **L0 (back-of-envelope) + L1 parziale (VLM/Prandtl analitico)**. Nessun CFD, nessuna galleria, nessun prototipo. Tutti i numeri sono stime ingegneristiche di primo ordine con bande dichiarate.
> **Mandato:** stabilire se la configurazione box-wing (closed-wing / joined-wing / boxplane) offra un vantaggio tecnico tale da giustificare un **prodotto proprietario** invece di adattare un fixed-wing VTOL COTS, per la nicchia delivery C3 (telemedicina/farmaci/sangue/AED/pacchi aree montane).

---

## 0. Caveat epistemico e chiarimento terminologico preliminare (Regola provenienza)

**Confidence aggregata del documento: LOW-MEDIUM**, dichiarata riga per riga. Metodologia: teoria consolidata (Prandtl 1924, best wing system) + letteratura box-wing/UAV rivista + stime ingegneristiche di primo ordine calibrate sui vincoli C3. **Distinguo esplicitamente "calcolo" (formula chiusa applicata) da "stima" (analogia/giudizio ingegneristico).**

**Tre precisazioni che cambiano l'inquadramento:**

1. **Nel repository NON esiste un box-wing.** Ho ispezionato `cad/`: i modelli presenti (`HALE.png`, `HALE2.png`, `WhatsApp Image 2026-01-18…`) sono un **monoplano convenzionale high-AR** con T-tail e trave di coda + elica traente (il concept HALE stratosferico). L'unica configurazione non-convenzionale documentata nel repository è la **three-lifting-surface (canard + ala + T-tail)** analizzata in XFLR5 nel `Progetto concettuale struttura HALE.md`. **Un box-wing (ala chiusa ad anello) non è mai stato disegnato né modellato in Firmamento.** Questo documento valuta quindi un'ipotesi *nuova*, non un design esistente. `[confidence: alta — verifica diretta dei file]`

2. **Box-wing ≠ three-lifting-surface ≠ tandem.** Sono tre famiglie diverse. Il box-wing (PrandtlPlane) ha ala anteriore e posteriore **connesse alle estremità da paratie verticali**, formando un anello chiuso. La three-lifting-surface del concept ha superfici **separate** (canard + ala + coda) e NON è un box-wing. I vantaggi di Prandtl valgono **solo** per il sistema chiuso. Il mandato usa "box-wing" in senso letterale: lo tratto come tale.

3. **Firmamento è operatore di servizi, non OEM** (`CLAUDE.md`). Un prodotto airframe proprietario è già di per sé una deviazione dal modello di business inderogabile; il box-wing la accentua. Questo pesa sul verdetto finale a prescindere dall'aerodinamica.

---

## 1. Vantaggio aerodinamico — quantificazione

### 1.1 La teoria: Prandtl Best Wing System (1924) — cosa promette davvero

Prandtl (1924, *Induced Drag of Multiplanes*) dimostrò che, **a parità di apertura `b` e di portanza totale `L`**, un sistema alare chiuso (box-wing con paratie verticali di estremità) ha la **minima resistenza indotta possibile** tra tutti i sistemi non-planari di data apertura e altezza. Il guadagno cresce col rapporto **altezza/apertura `h/b`** (gap verticale tra le due ali diviso l'apertura).

Valori teorici di riferimento (distribuzione di portanza ottima, ala ideale) — `[calcolo/letteratura, teoria dei vortici a ferro di cavallo]`:

| h/b | Resistenza indotta box / monoplano (pari `b`, pari `L`) | Riduzione D_i | Fattore di efficienza `e` (mono ≈ 0.85→1.0 ideale) | Confidence |
|---|---|---|---|---|
| 0.10 | ≈ 0.78 | **~22%** | e_box ≈ 1.28 | media (interpolazione Prandtl) |
| 0.15 | ≈ 0.71 | **~29%** | e_box ≈ 1.41 | media |
| 0.20 | ≈ 0.66 | **~34%** | e_box ≈ 1.46 | media |
| 0.30 | ≈ 0.60 | **~40%** | e_box ≈ 1.67 | media-alta (valore classico citato) |

Fonte primaria del dato h/b=0.3 → D_i al 60% del monoplano: confermato da più review (ScienceDirect box-wing review 2025; ERAU IJAAA; Purdue JATE). Range di validità dichiarato da Prandtl: **1/15 < h/b < 1/2** (0.067–0.5).

**Attenzione — cosa NON dice il teorema:**
- È una riduzione **solo della componente indotta**, e **solo a parità di apertura**. Non è una riduzione del drag totale.
- Assume distribuzione di portanza ottima (a "farfalla" sulle due ali) e **ignora completamente** la resistenza viscosa/di profilo delle ali aggiuntive, delle paratie verticali e delle quattro giunzioni.
- A basso Reynolds (droni piccoli) l'ipotesi di ala ideale è ottimistica: le giunzioni generano bolle di separazione e drag di interferenza sproporzionato.

### 1.2 Il vincolo che rende il box-wing *potenzialmente* sensato: il cap C3 di 3 m

La classe **C3** (Reg. UE 2019/945) impone MTOM < 25 kg **e una dimensione caratteristica ≤ 3 m**. Per un'ala fissa questo è di fatto un **tetto rigido all'apertura**. Il box-wing brilla proprio quando **l'apertura è vincolata** e si vuole più "allungamento efficace" di quanto un monoplano da 3 m possa dare — esattamente la stessa ragione per cui è studiato per gli airliner al gate ICAO da 80 m.

**Riformulazione in "apertura equivalente"** `[calcolo]`: un box con h/b=0.13 (gap 0.4 m su 3 m) ha D_i pari a un monoplano di apertura `b_eq = b·√(e_box/e_mono) = 3·√(1.28/0.85) ≈ 3·1.23 = 3.7 m`. Il box "compra" ~0.7 m di apertura equivalente **dentro** il cap di 3 m. Questo è il **solo** argomento aerodinamico legittimo e forte a favore del box-wing per il C3.

**Contro-argomento immediato:** lo stesso effetto (più AR entro 3 m) si ottiene, più semplicemente, con un **monoplano a corda più sottile / AR più alto** entro i 3 m — pagando in numero di Reynolds e rigidezza, ma senza giunzioni chiuse. Il box-wing va confrontato con QUESTO monoplano ottimizzato, non con un monoplano tozzo.

### 1.3 Il conto che conta: drag totale, non indotto — quando il box vince e quando perde

Il risultato chiave della letteratura UAV (arXiv 2112.02872 / AIAA SciTech 2025, "Investigation of Flight Conditions where Box-Wing Outperforms Mono-Wing for Small UAVs") è netto e coincide con la fisica:

> **Il box-wing conviene SOLO quando la resistenza indotta supera la resistenza d'attrito** (alto CL, bassa velocità, alto carico), perché è lì che il suo risparmio sull'indotta pesa più della penalità di superficie bagnata. In crociera efficiente (basso CL, attrito-dominato) **il monoplano vince.**

Applico il criterio al caso BOXY con un **conto di primo ordine** `[calcolo, L0]`:

**Baseline monoplano di riferimento (VTOL delivery C3):**
| Parametro | Valore | Nota |
|---|---|---|
| MTOM / peso | 25 kg / W = 245 N | vincolo C3 |
| Apertura b | 3.0 m | cap C3 |
| Superficie S | 0.90 m² (corda media 0.30 m) | AR = b²/S = **10** |
| Densità ρ | 1.11 kg/m³ | ≈ 1500 m ISA (quota tipica missione montana) |
| CD0 (parassita totale) | **0.040** | VTOL: ala ~0.011 + fusoliera/booms/**nacelle rotori esposti** ~0.029. Un delivery VTOL è "sporco", non un aliante. `[stima]` |
| e (monoplano) | 0.85 | tipico ala rastremata |

**Numero di Reynolds crociera** `[calcolo]`: Re = ρ·V·c/μ. A V=25 m/s, c=0.30 m, ν=1.58e-5 → **Re ≈ 4.7·10⁵**. Basso-Re: profili tipo SD7037/E387, transizione critica, drag di profilo elevato. Un box-wing con due ali a corda ridotta (per pari superficie) lavora a Re ancora più basso (~2.5·10⁵), **peggiorando** la penalità di profilo.

**CL di crossover indotta = attrito** `[calcolo]`:
`CL_x = √(CD0·π·AR·e) = √(0.040·π·10·0.85) = √1.068 ≈ 1.03`

→ L'indotta supera l'attrito **solo per CL > ~1.03**, cioè volo lento/pesante/salita/raffica, **NON in crociera**. In crociera (CL ~0.5–0.8) il regime è **attrito-dominato = territorio sfavorevole al box-wing.** Questo, da solo, è quasi il verdetto.

**Confronto L/D nei due regimi** `[calcolo]` (box: h/b=0.13, riduzione D_i 22%, penalità profilo ΔCD0 = +0.008 per paratie verticali + seconda giunzione + Re più basso):

| Regime | V | CL | L/D monoplano | L/D box-wing | Δ box vs mono |
|---|---|---|---|---|---|
| **Crociera** (attrito-dom.) | 25 m/s (90 km/h) | 0.79 | **12.4** | 11.9 | **−4%** (box peggiore) |
| **Alto CL** (indotta-dom.: salita/pesante/lento) | 20 m/s (72 km/h) | 1.23 | 12.7 | **13.3** | **+5%** (box migliore) |

**Sintesi aerodinamica onesta:**
- Il guadagno teorico Prandtl (22–40% sull'**indotta**) è reale ma si scarica su una componente che in crociera vale poco. Netto sul **drag totale in crociera: da −5% a +5%, stima centrale ≈ 0% (sostanzialmente pari), con probabile leggera penalità** per un VTOL ad alto CD0. `[calcolo L0, confidence media]`
- Il box vince **solo** nella finestra alto-CL (~+5%), che per una missione delivery (dominata dalla crociera punto-punto) è marginale sul **range**.
- Il guadagno positivo si materializza **se e solo se**: (a) CD0 è basso (airframe pulito, rotori retrattili/carenati — improbabile su un VTOL C3 economico), **e/o** (b) la missione è loiter/persistenza a basso CL alto — ma allora non è più "delivery".
- **Il range/endurance a MTOM 25 kg NON migliora in modo apprezzabile** rispetto a un buon monoplano da 3 m. Nella migliore delle ipotesi realistiche: +3–8% di L/D di crociera **solo** se l'airframe è aerodinamicamente pulito; nella peggiore, −5%.

> **Verdetto §1:** il vantaggio aerodinamico netto del box-wing per un VTOL cargo C3 è **marginale e condizionato** (banda −5%…+8% su L/D di crociera, centrale ~0). Il 20–40% "da brochure Prandtl" è vero solo sull'indotta e a pari apertura, e **non sopravvive** al conto del drag totale a basso Re con un airframe VTOL sporco. `[confidence: media]`

---

## 2. Vantaggio strutturale — quantificazione

### 2.1 Bracing e massa strutturale: reale ma piccolo a questa scala

Il claim classico (PrandtlPlane, joined-wing Wolkovitch): le due ali si controventano → l'anello chiuso ha maggiore rigidezza flessionale a parità di massa → risparmio di massa strutturale dell'ala (letteratura: 10–30% *in alcuni casi*, ma **conteso** — Livne, Demasi mostrano che le giunzioni e il carico di compressione dell'ala posteriore erodono il vantaggio).

**Perché a scala C3 il beneficio è piccolo** `[stima]`:
- La massa strutturale dell'ala per un drone da 25 kg è **~8–12% del MTOM = 2–3 kg** (composito). I carichi di flessione (25 kg, 3 m) sono modesti.
- Un risparmio del 10–25% sulla struttura alare = **0.2–0.75 kg**. Ma le 4 giunzioni di estremità (strutturalmente critiche) **ri-aggiungono massa**. Netto realistico a questa scala: **≈ 0…+0.5 kg**, cioè **1–2% del MTOM al massimo**. Non decisivo: la massa di un VTOL C3 è dominata da motori/ESC/batterie/booms, non dall'ala.
- Payload utile: il guadagno di frazione di payload da bracing strutturale è **entro il rumore** (≤2%). Non giustifica la configurazione.

### 2.2 La VERA sinergia strutturale: il telaio del box come struttura VTOL

Questo è l'argomento ingegneristico più interessante e va isolato: un lift+cruise VTOL convenzionale richiede **4 booms cantilever** per portare i rotori di sostentamento. Un box-wing **ha già un telaio rettangolare rigido chiuso**; i 4 rotori di sostentamento possono essere montati ai **4 spigoli** (estremità ala anteriore + posteriore) su una base larga e rigida, **eliminando i booms dedicati** e ottenendo un'ampia base motrice (buona autorità di controllo in hover).

- Risparmio potenziale: la massa dei booms VTOL (**~0.5–1.2 kg** su un C3) più il loro drag in crociera. `[stima, confidence media]`
- **Questa è la sola ragione strutturale per cui un box-wing VTOL cargo ha senso di esistere** rispetto a un fixed-wing VTOL convenzionale. Non l'aerodinamica: l'**integrazione strutturale della propulsione VTOL**.

### 2.3 Compattezza (hangar-in-a-box / trasporto)

Il box-wing realizza una data superficie alare con **~30–40% di apertura in meno** di un monoplano → più compatto per stoccaggio/trasporto in furgone/valigia. Beneficio operativo **reale ma modesto**, e **facilmente pareggiato** da un monoplano ad **ala ripiegabile** (soluzione molto più semplice e senza penalità aerodinamica/strutturale). Inoltre il box aggiunge un ingombro verticale (il gap ~0.4 m). Netto: la compattezza **non è un differenziatore esclusivo del box-wing.**

> **Verdetto §2:** il vantaggio strutturale "bracing → più payload" è **entro il 2% del MTOM = trascurabile** a scala C3. L'**unico** argomento strutturale forte è usare il telaio chiuso come **struttura portante dei 4 rotori VTOL** (risparmio booms ~0.5–1.2 kg). La compattezza è reale ma la batte un'ala ripiegabile. `[confidence: media]`

---

## 3. Costi e rischi del box-wing vs fixed-wing VTOL convenzionale

| Voce | Impatto box-wing | Note tecniche | Confidence |
|---|---|---|---|
| **Fabbricazione** | **+40–80%** effort ala | 2 ali + 2 paratie verticali + 4 giunzioni ⇒ più stampi, più maschere di assemblaggio, allineamento critico dell'anello chiuso | media |
| **Giunzioni di estremità** | Rischio strutturale/fatica alto | Trasferimento di carico attraverso 4 nodi; punti di ispezione difficili; fatica sensibile — nodo di certificazione | media |
| **Buckling** | Rischio specifico | L'ala posteriore/inferiore lavora in **compressione + flessione**: instabilità (buckling) e comportamento non-lineare "snap" documentati (Wolkovitch, Demasi, Livne). Richiede analisi + test di compressione dedicati | media |
| **Aeroelasticità** | Accoppiamento tra le due ali | Flutter modes accoppiati, possibile body-freedom flutter. **A scala C3 (piccola, rigida, bassa V)** la Vf è probabilmente ben sopra Vd ⇒ **verosimilmente NON showstopper**, MA va dimostrato con GVT + analisi flutter (margine ≥20%). Non si dichiara "no flutter" senza envelope. | media |
| **Download in hover (VTOL)** | Penalità energetica | La scia dei rotori di sostentamento impatta **due** ali invece di una ⇒ perdita di spinta in hover maggiore (monoplano ~5–10%, box ~10–18% a seconda del posizionamento rotori). **Peggiora il bilancio energetico VTOL** (fase più critica per un C3 elettrico) | bassa-media `[stima]` |
| **Integrazione VTOL** | Tilt complesso; lift+cruise pulito | Tilt-rotor su box è complicato (dove ruota?). Lift+cruise ai 4 spigoli è la scelta naturale (vedi §2.2) ma introduce la penalità di download sopra | media |
| **Δ costo dimostratore** | **+€0.3–0.8M**, **+6–12 mesi** | vs fixed-wing VTOL convenzionale: extra aero/strutturale/aeroelastico + sviluppo giunzioni | bassa `[stima]` |
| **Δ costo → prodotto certificato** | **+€0.5–1.5M**, **+6–18 mesi** | penalità di **novità**: config non-standard, nessun precedente per il Notified Body C3 e per il valutatore SORA ⇒ più burden analitico | bassa `[stima]` |

> **Verdetto §3:** il box-wing **aggiunge costo e rischio non banali**. I rischi aeroelastici (flutter accoppiato, buckling della membratura compressa) sono gestibili a scala C3 ma **richiedono test dedicati** (non sono gratis). La penalità di **download in hover** lavora **contro** il caso d'uso VTOL. Delta realistico: **+€0.3–0.8M dimostratore, +€0.5–1.5M al prodotto certificato**, +6–18 mesi. `[confidence: bassa-media]`

---

## 4. IP difendibile — c'è un moat?

### 4.1 Il box-wing è arte nota, e abbondante

- **Prandtl 1924** (best wing system): fondamento **pubblico da 100 anni**.
- **US 3,834,654 A "Boxplane wing and aircraft"** (Miranda, Lockheed, 1974): brevetto fondativo del boxplane — **scaduto**, quindi dominio pubblico.
- **PrandtlPlane** (Frediani, Università di Pisa): brevetti su *specifiche* implementazioni, ma il concetto è pubblico; progetto **IDINTOS** (idrovolante PrandtlPlane leggero) già realizzato.
- **Box-wing VTOL UAV già esistenti in letteratura**: "Preliminary design of a box-wing VTOL UAV" (ResearchGate), "Design of UAV VTOL Box Wing Aircraft" (Academia), **TiltOne** (box-wing tiltwing UAV), "Preliminary design of a Tiltwing UAV with a box wing configuration" (Springer, Aerotecnica Missili & Spazio). La delivery è **esplicitamente citata** come applicazione target in questi lavori.
- **Wingcopter** (benchmark delivery C3): **NON è un box-wing** — è un tilt-rotor convenzionale ad ala dritta con winglet e tilt-rotor brevettato. Il suo IP è nel **meccanismo tilt-rotor e nell'operatività**, non nella configurazione alare.

**Conclusione arte nota:** la configurazione box-wing **non è brevettabile** — è prior art profonda e diffusa, inclusa la variante box-wing VTOL UAV per delivery. `[confidence: alta]`

### 4.2 Cosa resterebbe di potenzialmente proprietario (e quanto vale)

- **Il "vano cargo modulare integrato nel box-wing"** come tale: **debole**. Meccanismi di sgancio/rilascio cargo per droni sono ampiamente brevettati (es. US 10,035,623 "Package for drone delivery" e famiglia). Un vano generico nel box non supera l'arte nota.
- **Ciò che *potrebbe* reggere** come brevetto **per modello di utilità** (IT — economico, veloce, ma IP debole): una combinazione **specifica e non ovvia** di (i) telaio box come struttura portante dei 4 rotori lift+cruise, (ii) pod cargo alloggiato **nella cella centrale del box sull'asse** con gestione attiva del CG durante il rilascio, (iii) percorso di carico strutturale dedicato. È una **rivendicazione stretta**, facilmente aggirabile riposizionando rotori/pod. **Non crea un moat durevole.**
- **IP di processo/dati**: il vero asset difendibile non è la configurazione ma il **pacchetto dati di qualifica** (polare validata, test strutturali, clearance flutter, accettazione SORA, affidabilità provata in volo) — che **non è configuration-specific** e vale per qualsiasi airframe.

> **Verdetto §4:** **NESSUN moat IP forte.** Box-wing = arte nota (Prandtl 1924, boxplane Lockheed 1974, molteplici box-wing VTOL UAV per delivery in letteratura). Il vano cargo nel box è, al massimo, un **modello di utilità debole e aggirabile**. Coerente con `CLAUDE.md`: per un **operatore di servizi** il moat sta nel servizio/dati/operazioni, non nell'airframe. `[confidence: alta]`

---

## 5. Dimostratore → prodotto: cosa serve tecnicamente, costo/tempo

Scala di fedeltà per portare un box-wing C3 da concept a prodotto vendibile/conforme:

| Livello | Attività | Scopo | Costo/tempo `[stima]` |
|---|---|---|---|
| **L0** ✔ | Back-of-envelope (questo documento) | Screening | fatto |
| **L1** | XFLR5/AVL + **VLM** del box (il VLM cattura bene l'indotta non-planare); polare preliminare, stabilità statica, margine statico, V-n diagram (CS-LURS/PDRA), stima flutter analitica | Confermare (o falsificare) il ~0% netto di crociera | €10–30k, 1–2 mesi |
| **L2** | CFD **RANS con transizione γ-Reθ** (obbligatorio a Re ~2–5·10⁵); drag breakdown box vs monoplano; download in hover (attuatore-disco/URANS) | Quantificare drag di interferenza delle giunzioni e penalità hover | €50–150k, 3–6 mesi |
| **L3** | **Galleria del vento** (polare + interferenza giunzioni); **GVT** (ground vibration test) + analisi flutter con margine ≥20%; **prova statica** telaio + **test di buckling** della membratura compressa; prova di fatica delle 4 giunzioni | Validare aeroelasticità e struttura — i rischi specifici del box | €150–350k, 6–12 mesi |
| **L4** | Campagna di **volo**: espansione envelope, clearance flutter in volo, caratterizzazione transizione VTOL e download, reliability growth | Prova operativa | €150–400k, 12–24 mesi |
| **Conformità** | **Classe C3: NO self-declaration** (Modulo A non disponibile) ⇒ **EU-type examination via Notified Body** o quality assurance completa, per una **config non-standard** | Marcatura C3 vendibile | €100–300k, 12–18 mesi |

**Totale dimostratore→prodotto certificato: ordine di €2–6M e 3–5 anni** (coerente con `10-fasce-engineering.md` §3.3, "prodotto certificato €3–10M+"). Di cui il box-wing **aggiunge ~€0.5–1.5M e 6–18 mesi** rispetto a un fixed-wing VTOL convenzionale, concentrati in L2/L3 (interferenza, buckling, flutter accoppiato) e nella penalità di novità in certificazione.

---

## 6. Lista showstopper / condizioni al contorno (sintesi rischi)

| # | Rischio | Impatto | Gestibile? |
|---|---|---|---|
| S1 | Guadagno aero netto ≈ 0 in crociera ⇒ **il box non migliora il range delivery** | Erode la ragion d'essere del prodotto | Sì, ma allora **perché il box?** |
| S2 | Penalità **download in hover** peggiora il bilancio energetico VTOL | Riduce endurance/payload nella fase critica | Mitigabile con posizionamento rotori; costa analisi |
| S3 | **Buckling** membratura compressa + fatica 4 giunzioni | Strutturale/certificazione | Sì, con test L3 dedicati |
| S4 | **Flutter accoppiato** delle due ali | Aeroelastico | Probab. Vf >> Vd a scala C3, ma **da dimostrare** (GVT) |
| S5 | **Nessun moat IP** + penalità novità in certificazione C3 | Business/regolatorio | Non mitigabile: è intrinseco |
| S6 | Deviazione dal modello **operatore-non-OEM** | Strategico | Decisione di governance |

Nessuno showstopper è "fisico-fatale" a scala C3 (a differenza dell'HALE high-AR dove il flutter è dominante); ma **il cumulo di costi/rischi non è ripagato da un vantaggio prestazionale decisivo.**

---

## 7. VERDETTO

**Il box-wing NON è un differenziatore tecnico decisivo per un VTOL cargo C3 delivery, nel caso generale.** Il guadagno di Prandtl (22–40% sull'indotta) è reale ma **a pari apertura e solo sull'indotta**; sul **drag totale di crociera** a basso Re con un airframe VTOL sporco si riduce a **≈ 0% netto (banda −5%…+8%)**. Il vantaggio strutturale di bracing è **≤2% del MTOM = trascurabile**. Non c'è **moat IP** (arte nota da Prandtl 1924 e boxplane Lockheed 1974; box-wing VTOL UAV per delivery già in letteratura). In compenso il box **aggiunge** ~€0.5–1.5M e 6–18 mesi, rischi di buckling/flutter da testare, e una **penalità di download in hover** che lavora contro il caso VTOL.

**La bilancia pende verso "complessità che non ripaga" — SALVO** una congiunzione specifica di condizioni in cui pende verso "differenziatore reale":

1. **L'apertura di 3 m è un vincolo binding e sfruttato** (si vuole davvero l'AR-efficace di ~3.7 m equivalenti entro il cap C3), **E**
2. **Si fa del "telaio box = struttura dei 4 rotori VTOL" la tesi ingegneristica** (eliminare i booms: l'unica sinergia forte, §2.2), **E**
3. **L'airframe è tenuto aerodinamicamente pulito** (rotori carenati/retrattili) così che la crociera cada in regime meno attrito-dominato, **E**
4. **Il valore per il cliente è "compattezza + integrazione elegante", non "range imbattibile"** — perché il range non migliora.

Anche soddisfatte tutte e quattro, il risultato è **eleganza tecnica, non un edge prestazionale decisivo né IP difendibile.** Per un'azienda che è **operatore di servizi** (`CLAUDE.md`), sviluppare un airframe box-wing proprietario significa **bruciare capitale R&D su novità di configurazione che il cliente-servizio non paga a premio.**

**Raccomandazione ingegneristica:** per la nicchia delivery C3, **adattare un fixed-wing VTOL COTS** (Wingcopter-class) batte lo sviluppo box-wing proprietario su costo, tempo, rischio e time-to-market. Il box-wing va tenuto **solo** come eventuale **dimostratore tecnologico/vetrina IP** (coerente con `10-fasce-engineering.md` §3.3: BOXY ha senso come "banco di prova", non come prodotto operativo), **non** come base di un prodotto vendibile a breve. Se si vuole comunque perseguirlo, la porta d'ingresso obbligata è **L1 (VLM) → L2 (RANS transizionale)** per falsificare o confermare il "~0% netto di crociera" **prima** di ogni impegno di capitale su L3/L4.

---

## 8. Fonti e confidence

**Verifica interna (confidence alta per il dato Firmamento):**
- `cad/` — ispezione diretta: **nessun box-wing**, solo monoplano HALE + three-lifting-surface. Confermato che BOXY-box-wing è ipotesi nuova, non design esistente.
- `Progetto concettuale struttura HALE.md` — three-lifting-surface (canard) in XFLR5, ≠ box-wing.
- `analisi-bottom-up/10-fasce-engineering.md` §3 — fascia T1 BOXY, target €300k = dimostratore, non prodotto (coerente col verdetto).
- `CLAUDE.md` — modello operatore-non-OEM (pesa sul verdetto strategico).

**Fonti esterne (web, luglio 2026):**
- Prandtl best wing system / h/b: [ScienceDirect box-wing review 2025](https://www.sciencedirect.com/science/article/pii/S037604212500034X); [Waeterschoot – HAW Hamburg, effect of h/b ratio](https://www.fzt.haw-hamburg.de/pers/Scholz/arbeiten/TextWaeterschoot.pdf); [Purdue JATE, box-wing design issues](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1253&context=jate); [ERAU IJAAA box-wing optimization](https://commons.erau.edu/cgi/viewcontent.cgi?article=1034&context=ijaaa). Dato h/b=0.3 → D_i al 60% del monoplano confermato.
- Crossover box vs mono per UAV: [arXiv 2112.02872 / AIAA SciTech 2025, "Investigation of Flight Conditions where Box-Wing Outperforms Mono-Wing for Small UAVs"](https://arxiv.org/abs/2112.02872) — box vince **solo** quando indotta > attrito.
- Box-wing VTOL UAV / prior art: [Preliminary design of a box-wing VTOL UAV (ResearchGate)](https://www.researchgate.net/publication/337700902_Preliminary_design_of_a_box-wing_VTOL_UAV); [Preliminary design of a Tiltwing UAV with box wing (Springer)](https://link.springer.com/article/10.1007/BF03406054); [Design of UAV VTOL Box Wing Aircraft (Academia)](https://www.academia.edu/31370723/Design_of_UAV_VTOL_Box_Wing_Aircraft).
- Prior art brevettuale: [US 3,834,654 A Boxplane wing and aircraft (Lockheed/Miranda, 1974)](https://patents.google.com/patent/US3834654A); [US 10,035,623 Package for drone delivery](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10035623).
- Wingcopter (benchmark, NON box-wing): [Wingcopter 198](https://wingcopter.com/wingcopter-198); [Wikipedia Wingcopter](https://en.wikipedia.org/wiki/Wingcopter).

**Limiti dichiarati:**
- Tutti i valori di L/D, CD0, ΔCD0, masse strutturali e download in hover sono **stime L0/L1 non validate** (né CFD né galleria né volo). Il conto di crossover CL e apertura equivalente è **calcolo chiuso** su assunzioni dichiarate; la sua conclusione (crociera attrito-dominata) è **robusta al variare delle assunzioni entro banda ragionevole**, ma il segno esatto del Δ crociera (−5%…+8%) dipende da CD0 e ΔCD0, entrambi da misurare.
- La penalità di download in hover per box-wing è la stima a confidence più bassa: richiede URANS/attuatore-disco (L2) per essere quantificata.
- Nessuna ricerca brevettuale professionale (freedom-to-operate) è stata condotta: l'affermazione "nessun moat" è a livello di screening, non di parere IP legale.
</content>
</invoke>
