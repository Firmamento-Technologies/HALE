# T-SORV — Aerostruttura preliminare di un MALE fixed-wing ad alta endurance (>10 m di apertura) con valutazione di integrazione solare sull'ala

> **Volume:** Analisi bottom-up pre-Studio — di seguito a `14-vtol-config-tradestudy-C3.md` (§4.8, baseline non-VTOL a catapulta = configurazione qui prescelta) e a `10-fasce-engineering.md` §5 (fascia T3 MALE).
> **Data:** 13 luglio 2026
> **Autore:** Aerodynamics & Structures Engineer
> **Livello di fidelity:** **L0 (back-of-envelope) + L1 parziale (buildup parassita, Prandtl-lifting-line analitico)**. Nessun CFD, nessuna galleria, nessun GVT, nessun prototipo. Ogni numero è una stima ingegneristica di primo ordine con banda e confidence dichiarate riga per riga.
> **Mandato:** dimensionare l'aerostruttura preliminare di un UAV ad ala fissa, apertura > 10 m, alta endurance (10-20 h), lancio a catapulta/traino (NON VTOL), per sorveglianza EO ad area vasta delle Aree Interne liguri; e quantificare l'area alare realisticamente disponibile per pannelli solari con la relativa penalità di massa/aerodinamica/aeroelastica — **senza** eseguire il bilancio energetico (compito del `propulsion-energy-engineer`).

---

## 0. Caveat epistemico e inquadramento — il trade-off inverso rispetto al caso C3

**Confidence aggregata del documento: MEDIA**, dichiarata riga per riga. Metodologia identica a `22-boxwing-vantaggio-tecnico.md`: teoria consolidata (lifting-line di Prandtl, buildup parassita per componenti, criterio di crossover indotta/attrito) + benchmark reali della fascia (`10-fasce-engineering.md` §5) + giudizio ingegneristico calibrato sui vincoli del mandato. Distinguo esplicitamente **[FATTO]** (dato verificato o formula chiusa applicata) da **[STIMA]** (analogia/giudizio con banda).

**Precisazione che cambia l'inquadramento rispetto a tutta l'analisi C3 precedente.** Il caso C3 (`22`, `14`) e questo caso T-SORV vivono in **due regimi opposti**, e il rischio si sposta di conseguenza:

| Dimensione | C3 (b ≈ 3 m, 25 kg) | T-SORV (b ≈ 14 m, ~180 kg) | Conseguenza |
|---|---|---|---|
| **Numero di Reynolds crociera** | ~4,7·10⁵ (transizionale, bolle laminari, drag di profilo instabile) | **~1,0-1,7·10⁶ (turbolento pulito, prevedibile)** | **Aerodinamica QUI più facile** |
| **L/D atteso** | ~12 (VTOL sporco) / ~16 (ala pulita) | **~21 (base)** | Migliore |
| **Momento flettente radicale** | ~0,3 kN·m | **~10 kN·m limite (≈30-35×)** | Struttura più impegnata |
| **Rischio aeroelastico** | Vf ≫ Vd probabile — **NON showstopper** (`22` §3) | **Flutter/divergenza da dimostrare esplicitamente — potenziale driver di progetto** | **Aeroelasticità QUI molto più critica** |

> **Tesi del documento:** rispetto al C3, qui **l'aerodinamica è "facile"** (Reynolds favorevole, nessuna transizione critica, L/D alto e robusto) **mentre l'aeroelasticità è "difficile"** (apertura 4,7× maggiore ⇒ ala molto più flessibile, flutter e divergenza diventano vincoli di progetto, non note a piè di pagina). È il **trade-off inverso** rispetto a `22`. Chi legge questo documento dopo la serie C3 deve ribaltare l'intuizione: là il collo di bottiglia era il profilo a basso Re, qui è la scatola strutturale/torsionale dell'ala lunga.

Coerentemente con `10-fasce-engineering.md` §5 e con i verdetti consolidati del repository, il materiale primario è **CFRP standard**; la fibra di lino resta confinata a parti secondarie / carenature / narrativa ESG (nessun uso in longherone o percorsi di carico primari — vedi caveat di dominio persistente nel progetto). Questo documento **non** riapre quel trade.

---

## 1. Punto di progetto aerostrutturale

Benchmark di riferimento (`10-fasce-engineering.md` §5, **[FATTO]** — dati vendor pubblici): Tekever AR5 (≤180 kg, 16-20 h), Elbit Hermes 450 (~450 kg, 17-20 h), Schiebel S-100 (200 kg). Il mandato colloca il velivolo nella fascia **T2/T3, 30-450 kg**, apertura > 10 m. Il "punto dolce" per bilanciare endurance / apertura / area solare / costo / carico gust è nella fascia **150-220 kg**, con apertura **12-16 m**. Propongo il seguente punto di progetto base, con banda:

| Parametro | Simbolo | **Base** | Banda | Livello | Note / motivazione |
|---|---|---|---|---|---|
| Apertura | b | **14,0 m** | 12-16 m | Progetto | > 10 m come richiesto; coerente con T3 (8-17 m). 14 m dà AR alto senza esplodere massa/flutter |
| Allungamento | AR | **17** | 15-20 | Progetto | Compromesso L/D↑ vs area solare/rigidezza. AR>20 aggrava il flutter e riduce l'area disponibile per pannelli |
| Superficie alare | S | **11,5 m²** | 9,8-13,7 m² | Derivato | S = b²/AR |
| MTOM | m | **180 kg** | 150-220 kg | Progetto | Al vertice della fascia AR5 (180 kg) ma con ala più grande ⇒ carico alare più basso |
| Carico alare | W/S | **~154 N/m² (15,7 kg/m²)** | 12-20 kg/m² | Derivato | **Basso** per la categoria (MALE tattici stanno a 30-60 kg/m²): scelta deliberata per endurance, bassa Vstall, area solare, dolcezza al lancio — a costo di **maggiore sensibilità alle raffiche** (vedi §4) |
| Corda media | c̄ | **0,82 m** | — | Derivato | c̄ = S/b — chiave per il Reynolds (§2) |
| Velocità di stallo (SL, CLmax 1,4) | Vs | **~13,4 m/s** | — | [STIMA] conf. media | Bassa ⇒ lancio e recupero benigni (§6) |
| Velocità di loiter | Vloiter | **20-25 m/s (72-90 km/h)** | — | [STIMA] conf. media | Prossima a L/Dmax |
| Velocità di crociera/trasferimento | Vc | **30-38 m/s (108-137 km/h)** | — | [STIMA] conf. media | Coerente coi benchmark 110-220 km/h della fascia |
| Payload EO | — | **10-25 kg** | — | [STIMA] | Gimbal EO/IR + eventuale relay; alimenta ConOps del collega |
| Materiale primario | — | **CFRP standard** | — | Verdetto consolidato | Longherone UD CFRP, pelle sandwich CFRP/schiuma o Nomex. Lino solo secondarie/ESG |

**Configurazione geometrica** (coerente col concept interno e col §4.8 di `14`): monoplano alto-AR ala dritta con lieve rastremazione (taper ~0,6) e svergolamento geometrico di lavaggio (-2°/-3° alle estremità per stallo progressivo dal centro), **fusoliera low-drag pod** + **tail boom** + **T-tail**, **elica traente in prua**. È esattamente la configurazione che `14` §4.8 indica come "la migliore delle 7 alternative in crociera e frazione payload" una volta rimosso il vincolo confined-space di Pentema — qui **prescelta**, non squalificata, perché i siti d'impiego ipotizzati sono su crinale/altopiano (ConOps del collega).

---

## 2. Regime di Reynolds — perché qui l'aerodinamica è "facile"

Numero di Reynolds sulla corda media, **[FATTO]** (formula chiusa Re = V·c̄/ν):

| Condizione | Quota | ρ [kg/m³] | ν [m²/s] | V [m/s] | c̄ [m] | **Re** |
|---|---|---|---|---|---|---|
| Loiter, quota media | 3.000 m | 0,909 | 1,86·10⁻⁵ | 20 | 0,82 | **~0,88·10⁶** |
| Crociera, quota media | 3.000 m | 0,909 | 1,86·10⁻⁵ | 30 | 0,82 | **~1,32·10⁶** |
| Crociera, livello del mare | 0 m | 1,225 | 1,46·10⁻⁵ | 30 | 0,82 | **~1,68·10⁶** |
| Lancio/decollo (SL) | 0 m | 1,225 | 1,46·10⁻⁵ | 18-20 | 0,82 | **~1,0-1,1·10⁶** |

**Implicazione [FATTO/STIMA, confidence alta].** Tutto il campo di missione sta a **Re ≈ 0,9-1,7·10⁶**, cioè **2-3,5× il Reynolds del caso C3** (4,7·10⁵). Questo colloca l'ala nettamente **sopra la soglia critica** dei profili a basso Reynolds: la bolla di separazione laminare, che a C3 rendeva il drag di profilo instabile e sensibile alla rugosità, qui è molto più piccola o assente (transizione anticipata e controllabile). Conseguenze pratiche:
- Si possono usare profili **consolidati e ben caratterizzati** in questa fascia di Re (es. famiglia NACA 43xx/23xxx modificati, Wortmann FX 63-137, Eppler E-series alto-Re, o profili laminari moderati tipo NLF): esiste letteratura sperimentale abbondante, **niente estrapolazioni ardite**.
- **Non è indispensabile** un modello di transizione γ-Reθ in CFD per una stima L1 attendibile (a differenza dell'HALE a 20 km o del C3): un semplice buildup parassita + polare di profilo da database è già affidabile a questo Re.
- Il drag di profilo previsto è **basso e prevedibile** ⇒ L/D alto e robusto (§3).

> Questo è il senso della tesi "**aerodinamica facile**": il rischio tecnico dominante di questa piattaforma **non** è aerodinamico. È strutturale/aeroelastico (§4-5) e — a monte — regolatorio (MTOM > 150 kg, vedi `10-fasce` §5.3, fuori scope qui).

---

## 3. Polare di crociera preliminare (L0/L1) e drag breakdown

### 3.1 CD0 — buildup parassita per componenti [STIMA, confidence media]

Airframe **pulito** (fixed-wing non-VTOL: nessuna nacelle/boom di sostentamento esposti, nessuna massa morta VTOL — il vantaggio strutturale/aerodinamico che `14` §4.8 attribuisce alla baseline A7). Riferimento: `22` mostrava CD0 ≈ 0,040 per un VTOL C3 "sporco" e ~0,011 per la sola ala pulita; qui siamo in mezzo, dominati da fusoliera pod + boom + coda + torretta EO.

| Componente | ΔCD0 (rif. S) | % di CD0 | Note |
|---|---|---|---|
| Ala (profilo, Re ~1,3·10⁶) | 0,0090 | 36% | Cf turbolento ~0,0045 × form factor × Swet/S |
| Fusoliera low-drag pod | 0,0045 | 18% | Corpo affusolato, fineness ratio favorevole |
| Tail boom | 0,0020 | 8% | Sezione tubolare snella |
| Impennaggio a T (HTP+VTP) | 0,0035 | 14% | Include ~2-3% di **trim drag** a CL di loiter |
| Torretta EO/IR + antenne + prese | 0,0040 | 16% | La "sporcizia" residua di un MALE ISR; retrattile ⇒ meno |
| Interferenza + gap/rugosità | 0,0020 | 8% | Giunzioni ala-fusoliera, boom-coda |
| **CD0 totale (base)** | **0,0250** | 100% | — |

Banda: **worst 0,032** (torretta grande, molte antenne, finitura industriale), **best 0,020** (torretta retratta, airframe molto pulito). **[STIMA, confidence media].**

### 3.2 Efficienza di Oswald e polare [FATTO per la formula, STIMA per i valori]

Ala alto-AR, rastremata, pulita, con eventuali winglet: **e = 0,82 (base)**, banda 0,75-0,88. Fattore indotto k = 1/(π·AR·e) = **0,0228**.

Polare: **CD = CD0 + k·CL²**. Prestazioni chiave (formule chiuse):

| Grandezza | Worst | **Base** | Best | Formula |
|---|---|---|---|---|
| CD0 | 0,032 | **0,025** | 0,020 | buildup §3.1 |
| e | 0,75 | **0,82** | 0,88 | [STIMA] |
| **L/D max** | 17,7 | **~21** | 24,2 | ½·√(π·AR·e/CD0) |
| CL @ L/Dmax | 1,00 | **1,05** | 1,08 | √(CD0·π·AR·e) |
| **L/D @ loiter (CL 0,9)** | ~17,5 | **~20,7** | ~23 | CL/CD |
| **L/D @ crociera (CL 0,5)** | ~14 | **~16,3** | ~18 | CL/CD |

> **Confronto col C3 [FATTO]:** L/D max ~21 contro ~12 (VTOL C3) / ~16 (ala pulita C3). Il salto è dovuto a (a) AR molto più alto (17 vs 10), (b) CD0 più basso (airframe non-VTOL pulito), (c) Reynolds favorevole. **Il numero L/D ≈ 20-21 è quello che il `propulsion-energy-engineer` deve usare** per il calcolo di endurance a questa scala (banda 18-24).

### 3.3 Drag breakdown percentuale per condizione [STIMA, confidence media]

| Componente di resistenza | Loiter (CL 0,9) | Crociera/dash (CL 0,5) |
|---|---|---|
| **Indotta** (CDi = k·CL²) | **42,5%** | **18,5%** |
| Profilo ala | 20,7% | 29,3% |
| Fusoliera pod | 10,3% | 14,7% |
| Impennaggio + trim | 8,0% | 11,4% |
| Torretta EO + protuberanze | 9,2% | 13,0% |
| Boom | 4,6% | 6,5% |
| Interferenza | 4,6% | 6,5% |
| **CD totale** | **0,0435** | **0,0307** |

**Lettura:** al loiter (missione principale) la resistenza è **indotta-dominata (~42%)**, il che è tipico e favorevole per un endurance-UAV alto-AR — è proprio dove l'alto allungamento paga. Diversamente dal C3 (dove `22` mostrava che il regime di crociera era attrito-dominato e penalizzava le config non-planari), qui l'alto AR lavora nel suo punto forte. Riducibile ulteriormente solo con AR ancora maggiore (ma peggiora il flutter, §5) o winglet (già inclusi in e = 0,82).

---

## 4. Analisi strutturale preliminare — carichi di longherone e V-n

### 4.1 Inviluppo di volo (V-n) [STIMA, confidence media-alta sul metodo]

Categoria operativa di riferimento: **CS-23 normal-like / CS-LURS esteso** per un UAV di sorveglianza a manovra dolce (loiter, non acrobazie). Fattori di carico di progetto proposti:

| Grandezza | Valore | Note |
|---|---|---|
| n limite manovra positivo | **+3,8** | CS-23 normal category; conservativo per un loiter-UAV |
| n limite manovra negativo | **−1,5** | — |
| Fattore ultimate | **1,5** (⇒ n_ult = +5,7 / −2,25) | **CS-23; NON confondere limit e ultimate** |
| Raffica di progetto | 15,2 / 7,6 m/s EAS (§341 CS-23) | **Può eccedere il carico di manovra** dato il basso W/S (§4.3) |

### 4.2 Momento flettente radicale del longherone [FATTO per la formula, STIMA per i numeri]

Al fattore di carico limite n = 3,8, distribuzione di portanza ~ellittica, centroide della semiala a 4·(b/2)/(3π) = 2,97 m dalla radice:

- Portanza per semiala: L_semi = n·W/2 = 3,8 × 1765/2 = **3.354 N**
- **Momento flettente radicale limite: M_root ≈ 3.354 × 2,97 ≈ 10,0 kN·m**
- **Momento flettente radicale ultimate: ×1,5 ≈ 15,0 kN·m**

> **Confronto col C3 [FATTO]:** lo stesso conto a C3 (25 kg, b 3 m) dà M_root ≈ 0,30 kN·m. **Qui il momento radicale è ~30-35× maggiore.** Questo è il "salto di scala" strutturale: non è l'aerodinamica a cambiare regime tra C3 e T-SORV, è la **scatola alare**.

**Dimensionamento indicativo dei correnti (spar caps) [STIMA]:** con spessore d'ala radicale t ≈ 0,13 m (corda radice ~1,0 m, t/c ~13%) e braccio efficace ~0,8·t, la forza assiale in ciascun corrente è ≈ M_ult/(0,8·t) ≈ 15.000/0,104 ≈ **144 kN**. Con CFRP UD ammissibile di progetto ~700 MPa (dopo knock-down per fori/ambiente/BVID), area corrente ≈ 2,1 cm². **Un longherone CFRP UD di pochi cm² di sezione di corrente per lato è sufficiente** — struttura del tutto realizzabile, margine ≥1,5 sul limite rispettabile senza acrobazie di layup. **[STIMA, confidence media]**

### 4.3 Sensibilità alle raffiche — il rovescio del basso carico alare [STIMA, confidence media]

L'incremento di fattore di carico per raffica scala come Δn ∝ (ρ·V·a·U)/(2·W/S): il **basso W/S (15,7 kg/m²)** scelto per l'endurance **aumenta la risposta alle raffiche**. In area appenninica ligure (orografia, venti di crinale, rotori sottovento) questo è un vincolo reale: è plausibile che **la raffica, non la manovra, dimensioni il longherone** e imponga limitazioni operative di vento al lancio/recupero. Da verificare con analisi di gust response (L1, §7). Margini strutturali qualitativi: **adeguati con margine ≥1,5 sul limite** per i carichi di manovra; **da confermare** per l'inviluppo di raffica combinato.

### 4.4 Buckling della pelle e deflessione [STIMA, confidence media]

- **Buckling dei pannelli**: con pelle sandwich (schiuma/Nomex) i pannelli del dorso in compressione a n alto vanno verificati; a questo carico alare e con sandwich, il buckling **non è previsto dimensionante** ma richiede verifica L1.
- **Deflessione di punta**: attesa **~5-10% della semiala** al carico limite [STIMA]. È **molto più del C3** (rigido) ma **molto meno dell'HALE stratosferico** (AR 25+, flessione >20% dell'apertura, che impone aeroelasticità geometricamente nonlineare). A AR 17 la flessione è **moderata**: analisi lineare/moderatamente nonlineare adeguata, non serve il framework geometricamente esatto dell'HALE. Un punto intermedio, coerente col posizionamento intermedio della piattaforma.

---

## 5. Aeroelasticità — il rischio dominante, e perché il salto rispetto al C3 è grande

**Questo è il capitolo dove la piattaforma T-SORV è più esposta e dove la mia raccomandazione è più forte.**

### 5.1 Il salto di rischio rispetto al C3 — quantificazione qualitativa

La velocità di flutter di un'ala a sbalzo scala, a parità di forma e materiali, **grosso modo con la rigidezza torsionale e con l'inverso dell'apertura**: allungando l'ala e mantenendo proporzioni simili, **Vf tende a scendere e le frequenze proprie si abbassano** (≈ ∝ 1/b² per la flessione fondamentale). Passando da b = 3 m (C3) a b = 14 m (T-SORV), **a parità di architettura la frequenza flessionale fondamentale cala di un ordine di grandezza** e i modi flesso-torsionali si infittiscono e si accoppiano nell'inviluppo di velocità operativo.

| | C3 (b 3 m) | **T-SORV (b 14 m)** |
|---|---|---|
| Verdetto flutter tipico | "Vf ≫ Vd probabile, **non showstopper**" (`22` §3, §6) | **"Vf da dimostrare esplicitamente; possibile driver di progetto"** |
| Frequenza flessionale 1° modo | Alta (ala corta rigida) | **Bassa** (~1 ordine di grandezza sotto) |
| Necessità GVT + analisi flutter formale | Consigliata | **Obbligatoria e potenzialmente dimensionante** |

### 5.2 Fenomeni da clearare (nessuna dichiarazione di "stabile" senza inviluppo) [STIMA]

1. **Divergenza torsionale dell'ala** — l'ala alto-AR con longherone relativamente cedevole in torsione può divergere; Vdiv va tenuta ≥1,2·Vd. Driver: rigidezza torsionale GJ e posizione dell'asse elastico.
2. **Flutter flesso-torsionale (bending-torsion)** — il classico accoppiamento; frequenze ravvicinate a AR alto ⇒ margine da verificare con **margine flutter ≥ 20%** (Vf ≥ 1,2·Vd), soglia conservativa che adotto per una piattaforma "technology-stretched" in questa fascia.
3. **Flutter delle superfici di controllo (alettoni)** — bilanciamento di massa delle superfici obbligatorio; a corda alettone e sbalzo maggiori il rischio cresce.
4. **Torsione del tail boom + T-tail** — la rigidezza torsionale del boom è **critica** per stabilità longitudinale e per il flutter dell'impennaggio a T (accoppiamento boom-torsione/HTP). Sezione tubolare CFRP con GJ adeguato; il T-tail su boom lungo è una geometria notoriamente sensibile.
5. **Body-freedom flutter (BFF)** — meno probabile su config con boom+coda convenzionale che su ala volante, **ma non escludibile a priori** dato l'AR: da includere nel modello con i modi di corpo rigido liberi.

### 5.3 Raccomandazione aeroelastica

- **Non si dichiara l'ala "stabile" senza V-n + inviluppo di flutter completo** (regola di progetto). Allo stadio L0 odierno il flutter è **il rischio tecnico dominante identificato**, superiore all'aerodinamico.
- Priorità: portare presto la piattaforma a **L1 aeroelastico** (modello a travi + VLM/DLM, metodo p-k in NASTRAN-Aeroelastic / ZAERO), poi **GVT + flutter test** a L3. Il GJ del longherone e la posizione dell'asse elastico vanno **congelati come parametri di progetto guidati dal flutter**, non solo dalla resistenza statica.
- Buona notizia: a AR 17 (non 25+) e a bassa quota (densità alta ⇒ smorzamento aerodinamico maggiore che a 20 km), **il problema è gestibile con margini standard** — non è la frontiera irrisolta dell'HALE. È "difficile ma di ingegneria nota", non "speculativo".

---

## 6. Lancio a catapulta / traino — carichi e confronto con decollo su strip

### 6.1 Cinematica e carichi di lancio [FATTO per la formula, STIMA per i parametri]

Velocità di fine lancio per fly-away sicuro: V_lo ≈ 1,3·Vs ≈ 1,3 × 13,4 ≈ **17-20 m/s**.

Accelerazione di catapulta a = V_lo²/(2·L_stroke):

| Corsa catapulta L | Accelerazione | in g | Spinta shuttle (m·a) |
|---|---|---|---|
| 12 m | 16,7 m/s² | 1,7 g | ~3,0 kN |
| 8 m | 25,0 m/s² | 2,5 g | ~4,5 kN |
| 5 m (compatta) | 40,0 m/s² | 4,1 g | **~7,2 kN** |

**Carico longitudinale di progetto proposto: n_x = 4 g** (con margine sulla corsa più corta), ⇒ carico assiale d'aggancio ≈ 180 × 4 × 9,81 ≈ **7,1 kN**. **[STIMA, confidence media].**

**Impatto strutturale [STIMA]:**
- **Punto di aggancio**: hardpoint sul keel di fusoliera (baricentrico, sotto il CG), con percorso di carico dedicato verso i frame principali e verso la radice alare (che scarica l'inerzia dell'ala durante l'accelerazione). Non sull'ala direttamente.
- **Rinforzo locale**: keel beam + 2 frame rinforzati + fitting metallico (Ti o acciaio) incollato/bullonato. **Penalità di massa ~1-2% del MTOM (≈ 2-4 kg)** — modesta, e in gran parte non a sbalzo (vicino al CG, ininfluente sul flutter).
- La torretta EO e i sistemi devono reggere 4 g longitudinali una tantum: vincolo di qualifica del payload, non dell'airframe.

### 6.2 Catapulta vs traino vs decollo convenzionale su strip [STIMA, confidence media]

A differenza di Pentema (`14` §4.8: catapulta+recupero **squalificati** per mancanza di spazio in valle), qui i siti ipotizzati sono su **crinale/altopiano** (ConOps del collega), dove **può esistere una strip semi-preparata**. Confronto:

| Opzione | Spazio a terra | Complessità/logistica | Massa a bordo | Costo sistema di terra | Idoneità crinale |
|---|---|---|---|---|---|
| **Catapulta (idro-pneumatica)** | Corsia libera ~10-20 m + volo | Sistema pesante/ingombrante da trasportare e montare per un velivolo da 180 kg | +2-4 kg (hardpoint) | Alto (€100-300k, [STIMA]) | Buona (non serve strip) |
| **Traino con veicolo terrestre** | Corsia di traino ~100-200 m | Media (veicolo + cavo + sgancio) | +1-2 kg (gancio) | Basso-medio | Buona **se** c'è pista/strada di crinale rettilinea |
| **Decollo convenzionale (ROG) su strip corta** | Strip ~150-250 m | Bassa (carrello fisso o retrattile) | +3-6 kg (carrello) | Basso (solo la strip) | **Ottima se il sito ha 150-250 m preparabili** |

Corsa di decollo ROG stimata: ground roll ≈ V_lo²/(2·a_ground) ≈ 20²/(2·1,3) ≈ **~150 m** [STIMA, con T/W ~0,18]. Con un altopiano/crinale che offra 150-250 m, **il decollo convenzionale è la soluzione più semplice ed economica**; la **catapulta è il fallback** per i siti privi di strip; il **traino** è la via intermedia low-cost quando esiste una superficie lunga ma non un vero campo. Raccomando di **progettare l'airframe per accettare sia catapulta sia ROG** (hardpoint keel + predisposizione carrello leggero), lasciando la scelta al sito — costa poca massa e massimizza la flessibilità operativa multi-sito SNAI.

Recupero: rete/skyhook (come Insitu, `10-fasce` §4.1) o **belly-landing / paracadute-BRS** su superficie sgombra. Data la bassa Vs (13,4 m/s), il belly-landing su altopiano erboso è realistico; il BRS è comunque parte integrante del sistema di recupero (`14` §5, riga A7) e ne assorbe la penalità di massa (3-8% MTOM già contabilizzata come frazione payload in `14` §4.8).

---

## 7. Integrazione di pannelli solari sull'ala — area disponibile e penalità

**Compito circoscritto (per esplicito mandato):** fornire l'**area alare utile** e la **penalità di massa/aerodinamica/aeroelastica**; **NON** il bilancio energetico (che spetta al `propulsion-energy-engineer`, il quale userà i m² qui stimati con la sua densità di potenza).

### 7.1 Area alare realisticamente copribile [STIMA, confidence media]

Superficie alare in pianta (dorso, entrambe le semiali) ≈ S = **11,5 m²**. Frazione realisticamente copribile con celle (rigide o semi-flessibili incollate sul dorso), al netto di:

| Zona esclusa | Frazione persa | Motivo |
|---|---|---|
| Alettoni + eventuali flap | ~12% | Superfici mobili: no celle (deformazione, gap) |
| Bordo d'attacco + bordo d'uscita | ~30% della corda | Curvatura elevata al LE, TE troppo sottile ⇒ banda utile ~15-70% corda |
| Radice/raccordo fusoliera + estremità/winglet | ~8% | Ombreggiamento, curvatura, cablaggio |
| Zone sopra i correnti / accessi ispezione | ~5% | Vincoli strutturali/manutentivi |

**Frazione utile netta ≈ 45-55% della pianta ⇒ area celle ≈ 5,0-6,5 m², base ~5,5 m².**

> **Numero da consegnare al `propulsion-energy-engineer`: area solare utile sull'ala ≈ 5,5 m² (banda 5,0-6,5 m²).** Estendibile a **~6,0-7,5 m²** se si copre anche il dorso dell'HTP e una parte del dorso fusoliera, ma con celle a resa inferiore (curvatura/ombra della torretta) — sconsigliato come base, utile solo come upside.

### 7.2 Penalità di massa [STIMA, confidence media]

Il modello HALE (`energy_balance_simulation.py`) usa **~0,5 kg/m²** per la sola cella GaAs multigiunzione (grado spaziale, film sottile). Ma l'**integrazione su ala a bassa quota** aggiunge incapsulamento robusto, adesivo, irrigidimento locale della pelle, cablaggio e MPPT:

| Voce | Densità/massa | Note |
|---|---|---|
| Celle nude (GaAs MJ o Si ad alta η) | 0,5-1,0 kg/m² | come rif. HALE, o Si terrestre |
| Incapsulamento + adesivo + rinforzo pelle | +0,7-1,5 kg/m² | robustezza a bassa quota, flessione ala |
| **Densità installata (base)** | **~2,0 kg/m²** | banda 1,5-3,0 kg/m² |
| Massa celle su 5,5 m² | **~11 kg** | a 2,0 kg/m² |
| Cablaggio + MPPT + protezioni | +2-4 kg | — |
| **Massa aggiuntiva totale** | **~13-15 kg** | **≈ 7-8% del MTOM** |

**Non trascurabile:** 13-15 kg su 180 kg è massa che compete direttamente col payload o con l'endurance. È il primo elemento del giudizio di §7.4.

### 7.3 Impatto su CD0, rigidezza e frequenze di flutter [STIMA, confidence media]

- **CD0**: celle incollate a filo (semi-flessibili, sormonti minimi) aggiungono **ΔCD0 ≈ +0,001…+0,003** (base +0,0015) da rugosità/gradini. A Re ~1,3·10⁶ lo strato limite è già turbolento ⇒ effetto contenuto. **Penalità L/D ≈ 3-5%** (da ~21 a ~20). Rigide/mal integrate: fino a −8%.
- **Rigidezza**: l'incollaggio delle celle sul dorso **irrigidisce marginalmente** la pelle a torsione (piccolo beneficio), ma non è un contributo strutturale progettabile (le celle non sono un laminato portante).
- **Flutter/masse**: aggiungere ~11 kg **distribuiti sul dorso alare** (~10-15% della massa strutturale dell'ala) **abbassa le frequenze proprie di ~3-5%** e sposta la distribuzione di massa. Se le celle gravano **dietro l'asse elastico** (dorso posteriore), l'effetto sul flutter è **peggiorativo** (riduce Vf); se stanno attorno al mid-chord, è ~neutro. **Conclusione: la massa solare va inserita nel modello aeroelastico L1 fin dall'inizio** — non è un add-on trascurabile a questa apertura (§5). Non è uno showstopper, ma sposta il margine di flutter nella direzione sbagliata e va contabilizzata.

### 7.4 Giudizio onesto: bonus marginale o elemento abilitante?

A **bassa quota (3-5 km, non 20 km)** e con **propulsione primaria NON solare-pura** (endurance 10-20 h da combustibile/ibrido o batteria, non da solare 24h):

- Potenza di crociera dell'ordine di **~3-4 kW** [STIMA, da W·V/(L/D)/η_prop]; potenza solare di picco da 5,5 m² a bassa quota (η di sistema realistica ~18-20%, atmosfera piena sopra) dell'ordine di **~1 kW a mezzogiorno estivo**, **quasi nulla di notte/in inverno**.
- Ne segue che il solare copre **una frazione (≈20-30% di picco diurno estivo)** del fabbisogno di crociera per poche ore centrali, con contributo **medio giornaliero molto minore**. **È un bonus di endurance (ricarica/allungamento marginale, qualche punto percentuale di autonomia in più nelle missioni diurne estive), NON un elemento abilitante.** Il verdetto quantitativo definitivo spetta al `propulsion-energy-engineer` con i 5,5 m².

> **Contrasto con l'HALE [FATTO]:** per l'HALE a 20 km il solare è **l'unico** elemento abilitante (nessun'altra fonte per il volo perenne), e infatti l'intera piattaforma è progettata attorno ad esso. Qui, a bassa quota e con propulsione primaria convenzionale, **il solare è ESG-narrativa + margine marginale di autonomia**, che costa 13-15 kg e sposta il margine di flutter. **Raccomandazione: trattarlo come opzione (kit installabile), non come requisito di progetto dell'airframe.** L'ala va dimensionata bene comunque; le celle si aggiungono se e quando l'analisi energetica del collega dimostra un ritorno netto positivo su una missione tipo.

---

## 8. Falsifying observations

1. **Se l'analisi flutter L1 (p-k, modello a travi + DLM) dà Vf < 1,2·Vd** nell'inviluppo operativo con l'ala AR 17 e le masse solari incluse, allora l'apertura/AR va ridotta (o il GJ del longherone aumentato con penalità di massa), e il punto di progetto b = 14 m / AR 17 va rivisto verso il basso. **È l'osservazione più probabile a invalidare il design** (il flutter è il rischio dominante, §5).

2. **Se la gust response (CS-23 §341) mostra che la raffica dimensiona il longherone** oltre il carico di manovra n = 3,8 a causa del basso W/S (15,7 kg/m²), il carico alare va alzato (ala più piccola/pesante) o vanno imposti limiti operativi di vento stringenti — con impatto diretto sulla disponibilità operativa in area appenninica ventosa.

3. **Se la torretta EO e le protuberanze reali portano CD0 > 0,032** (worst case), L/D scende sotto ~18 e l'endurance stimata dal collega va rivista al ribasso; l'ipotesi "aerodinamica facile, L/D ~21" è ottimistica se l'airframe è più "sporco" del previsto.

4. **Se la densità installata dei pannelli supera 3 kg/m²** (incapsulamento robusto per bassa quota/impatti/umidità), la massa solare supera ~20 kg (>11% MTOM): a quel punto il solare **erode il payload EO** in modo non accettabile e va abbandonato anche come opzione. Test panel di caratterizzazione massa/robustezza a M+6.

5. **Se i siti d'impiego reali su crinale/altopiano NON offrono 150-250 m di strip** (verifica GIS/sopralluogo del collega territoriale), il decollo convenzionale ROG decade e resta solo la catapulta idro-pneumatica per 180 kg — sistema di terra pesante e costoso (€100-300k) che cambia l'economia operativa multi-sito e va confrontato esplicitamente col traino.

6. **Se il regime di Reynolds reale in loiter scende sotto ~7·10⁵** (loiter più lento del previsto, o quota più alta a bassa densità), riemergono effetti transizionali di basso Re sul profilo e la polare va rifatta con modello di transizione — l'assunzione "niente transizione critica" (§2) va falsificata con XFLR5/CFD.

---

## 9. Riga di fondo

**Punto di progetto:** monoplano alto-AR non-VTOL, **b = 14 m, AR 17, S = 11,5 m², MTOM 180 kg, W/S ~15,7 kg/m²**, CFRP standard, T-tail su tail boom, elica traente, lancio catapulta/ROG. **Polare L0/L1: CD0 ≈ 0,025 (0,020-0,032), e ≈ 0,82, L/D max ≈ 21 (banda 18-24), L/D di loiter ~20** — nettamente migliore del C3 perché il **Reynolds di crociera (~1,3·10⁶) è favorevole e non transizionale: l'aerodinamica qui è "facile"**. **Il rischio si è spostato all'aeroelasticità:** con apertura 4,7× il C3 e momento radicale ~30× (~10 kN·m limite, ~15 kN·m ultimate, longherone CFRP realizzabile con margine ≥1,5), **il flutter/divergenza diventa il driver di progetto** e **non si dichiara l'ala stabile senza inviluppo V-n + flutter con margine ≥20%** — è il trade-off inverso rispetto al C3 (là aerodinamica difficile, aeroelasticità facile; qui viceversa), ma resta **ingegneria nota e gestibile**, non la frontiera irrisolta dell'HALE. **Lancio:** carico d'aggancio ~7 kN a 4 g, rinforzo keel +2-4 kg (~1-2% MTOM, non a sbalzo ⇒ ininfluente sul flutter); su siti di crinale con 150-250 m di strip il **decollo convenzionale ROG è la via più semplice**, catapulta come fallback. **Solare sull'ala: area utile ≈ 5,5 m² (banda 5,0-6,5), massa aggiuntiva ~13-15 kg (7-8% MTOM), ΔCD0 +0,0015 (L/D −3-5%), frequenze di flutter −3-5% (da includere nel modello).** A bassa quota con propulsione primaria non-solare, **il solare è un bonus marginale/ESG, non un elemento abilitante** (opposto all'HALE): trattarlo come kit opzionale, non come requisito dell'airframe. Il numero **5,5 m²** è quanto il `propulsion-energy-engineer` deve usare per il bilancio energetico (che questo documento NON esegue).

**Prossimo livello di fedeltà:** L1 (XFLR5/AVL polare + stabilità + **NASTRAN/ZAERO flutter p-k** + gust response CS-23 §341) → L2 (RANS per drag breakdown e trim) → L3 (galleria + **GVT + flutter test** + prova statica longherone) → L4 (flight test, clearance flutter in volo). **Priorità assoluta: L1 aeroelastico**, perché è lì che vive il rischio dominante.

---

## 10. Fonti e confidence

| Fonte | Uso | Confidence |
|---|---|---|
| `10-fasce-engineering.md` §5 (Tekever AR5 180 kg/16-20h, Hermes 450, Schiebel S-100) | Bracket punto di progetto (MTOM, endurance, apertura) | **Alta** (contratti/vendor pubblici) |
| `14-vtol-config-tradestudy-C3.md` §4.8, §5 (baseline A7 non-VTOL a catapulta) | Config prescelta, penalità recupero/BRS, confronto lancio | **Alta** (interna) |
| `22-boxwing-vantaggio-tecnico.md` | Metodologia buildup CD0/e/drag breakdown, riferimento CD0 pulito vs sporco, criterio Re | **Alta** (metodo interno consolidato) |
| `energy_balance_simulation.py` (0,5 kg/m² cella, GaAs η 0,30) | Base densità pannello (poi maggiorata per integrazione bassa quota) | **Alta** (fonte interna) |
| Buildup parassita per componenti (Cf turbolento, form factor, Swet/S) | CD0 §3.1 | **Media** (L1 non validato) |
| Lifting-line Prandtl, e di Oswald, L/Dmax = ½√(πARe/CD0) | Polare §3.2 | **Alta** (formula) / Media (valori) |
| Root bending ellittico, centroide 4R/3π, n·W/2 | Carichi §4.2 | **Alta** (formula) / Media (n, distribuzione) |
| Scaling frequenza flessionale ∝ 1/b², Vf ∝ rigidezza | Salto di rischio aeroelastico §5.1 | **Media** (qualitativo, da confermare L1) |
| CS-23 §341 (raffica), fattore ultimate 1,5, n +3,8/−1,5 | Inviluppo V-n §4.1 | **Alta** (normativa) |
| Cinematica catapulta a = V²/2L | Carichi lancio §6.1 | **Alta** (formula) / Media (V_lo, corsa) |

**Confidence per area:** polare/L-D **media-alta** (regime di Re favorevole rende la stima robusta); carichi statici longherone **media** (formula solida, distribuzione da confermare); **aeroelasticità low-medium** (rischio dominante, richiede L1 dedicato prima di ogni verdetto di stabilità); area solare **media**; massa/penalità solare **media**; giudizio "solare = bonus, non abilitante" **alta** (coerente con fisica bassa quota + verdetto HALE per contrasto).

**Limiti dichiarati:** nessun CFD, nessun modello aeroelastico numerico, nessun GVT, nessun prototipo. Tutti i numeri sono L0/L1 con banda dichiarata. Il verdetto di stabilità aeroelastica **non è dato** (per progetto): è segnalato come rischio dominante da chiudere a L1/L3. La scelta del profilo alare specifico e il layup di dettaglio del longherone sono rimandati a L1. La stima di potenza solare in §7.4 è puramente indicativa per motivare il giudizio "bonus vs abilitante"; **il bilancio energetico ufficiale è del `propulsion-energy-engineer`** con l'area di 5,5 m² qui fornita.
