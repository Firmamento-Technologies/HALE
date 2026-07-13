# 25a — T-SORV: ConOps, morfologia del territorio e target di quota operativa per una piattaforma fixed-wing ad alta endurance per sorveglianza terrestre delle Aree Interne liguri

> **Volume:** Analisi bottom-up pre-Studio — nuova piattaforma di sorveglianza, derivata dalle analisi HALE/famiglia modulare ma **esplicitamente NON HALE stratosferico**
> **Data:** 13 luglio 2026
> **Autore:** Aerospace Systems Engineer (NASA SE Handbook)
> **ID piattaforma:** **T-SORV** (T2/T3 Sorveglianza) — fixed-wing ad alta endurance, sola Osservazione della Terra (EO/IR), decollo a catapulta/traino, NON-VTOL, NON stratosferico
> **Base documentale:** `10-fasce-engineering.md` §4-5 (T2/T3), `13-fasce-regolatorio-missione.md` (matrice missione×fascia; EO = minimo attrito), `14-vtol-config-tradestudy-C3.md` §4.8 e §10.4 (baseline non-VTOL A7), `CLAUDE.md` (contesto Pentema/Torriglia, modello operatore-di-servizio)
> **Gate associato:** input per M+3 Concept e M+6 Architettura (Percorso di sorveglianza EO)

---

## 0. Caveat epistemico, terminologico e di scope (leggere prima di tutto)

### 0.1 Convenzione epistemica
- **[FATTO]** = dato normativo, geografico o fisico verificabile, con fonte (repo o URL).
- **[STIMA]** = giudizio ingegneristico dell'autore, per calcolo di primo ordine o analogia; confidenza dichiarata riga per riga (high/medium/low).
- **Regola dura:** nessun numero di quota, prestazione o classificazione SORA è definitivo finché non validato da CONOPS di dettaglio, sopralluogo, e pre-application ENAC (art. 11 Reg. UE 2019/947). Tutti i valori sono *preliminary-grade*.

### 0.2 Caveat terminologico obbligatorio — "C3" è incompatibile con questi vincoli [FATTO]
Il committente ha usato l'espressione "classe C3", ma i vincoli imposti sono **tecnicamente e regolatoriamente incompatibili con la classe C3 EASA**:

| Vincolo committente | Classe C3 EASA (Reg. UE 2019/945) | Esito |
|---|---|---|
| Apertura alare **> 10 m** | dimensione caratteristica ≤ 3 m | **incompatibile** |
| Endurance **10-20 h** | tipica di piattaforme small elettriche (< 3 h) | **incompatibile** |
| Certificazione ENAC per servizio operativo | C3 abilita **solo Open A3 VLOS** | **incompatibile** — l'Open non consente il servizio BVLOS ad area vasta richiesto |
| MTOM implicita (span > 10 m, endurance 20 h) | C3 richiede MTOM ≤ 25 kg | **incompatibile** — MTOM realistica ≥ 60-150+ kg |

**Interpretazione adottata in questo documento:** la richiesta viene letta come una piattaforma nella fascia **T2/T3 "MID/MALE"** della tassonomia interna (`10-fasce-engineering.md` §4-5), categoria regolatoria **Specific (SAIL IV-VI) o Certified**, **non Open/C3**. La sigla usata in tutto il documento è **T-SORV** (T2/T3 Sorveglianza).

Poiché il vincolo di apertura è **> 10 m**, la piattaforma è in realtà **T3-leaning** (T3 MALE = 8-17 m apertura, `10-fasce-engineering.md` §5), con un'ambiguità di fascia che dipende dalla MTOM: se la cellula è un'ala ad alto allungamento leggera (< 150 kg, aliante-derivata), può restare al confine T2/T3 e in **Specific SAIL IV-VI**; se la MTOM supera 150 kg, ricade quasi certamente in **Certified Category** (nodo regolatorio segnalato in `10-fasce-engineering.md` §5.3 e `13-fasce-regolatorio-missione.md` §2). Questo documento **non risolve** quel nodo — lo eredita e lo rimanda a `aviation-regulatory-counsel`/`regulatory-adversary`.

### 0.3 Scope e non-contraddizione con i verdetti HALE esistenti
T-SORV è una piattaforma **endurance-lunga ma a bassa quota** (target ~3.000 m AMSL, vedi §2), **non stratosferica**. Di conseguenza **NON è toccata** dagli showstopper del Percorso 6B/T4 e li lascia invariati:
- **[FATTO]** l'energy balance invernale solare a 20 km / 44°N (mai risolto, `10-fasce-engineering.md` §6, Studio Cap. 6) **non si applica**: T-SORV è a propulsione termica/ibrida convenzionale, quota di poche migliaia di metri, non dipende dal bilancio fotovoltaico stratosferico;
- **[FATTO]** l'assenza di framework HAPS civile EASA/ENAC (`13` §Fascia T4) **non si applica**: T-SORV opera in spazio aereo Classe G convenzionale, non attraversa FL195+ in salita/discesa, non richiede allocazione spettro HAPS;
- l'aeroelasticità dell'ala high-AR resta un **rischio da gestire** (l'apertura > 10 m è alta), ma di natura ordinaria per un MALE, non lo showstopper stratosferico.

**Il posizionamento è quindi netto:** T-SORV è la traduzione "a terra e a bassa quota" delle competenze maturate sul concept HALE — riusa l'IP aerodinamico high-AR e la logica di servizio-non-OEM (`CLAUDE.md`), ma non eredita il rischio stratosferico. È coerente con la strategia duale come **asset intermedio finanziabile** tra il pilota VTOL (6A) e l'HALE (6B).

---

## 1. Concept of Operations (ConOps)

### 1.1 Missione (invariante)
**Sola sorveglianza terrestre EO/IR.** Nessuna consegna, nessun trasporto, nessuno sgancio di materiale, nessun payload radio di servizio. Due famiglie di casi d'uso:

| Caso d'uso | Payload primario | Fenomeno osservato |
|---|---|---|
| **Controllo aree boschive** | IR/termico (LWIR/MWIR) + EO multispettrale | Rilevamento precoce di focolai d'incendio (hotspot termici), stato di salute della vegetazione (stress idrico, deperimenti, fitopatologie), monitoraggio post-evento |
| **Controllo viabilità e infrastrutture** | EO ad alta risoluzione (gimbal con zoom) + eventuale LiDAR | Frane e dissesto idrogeologico, monitoraggio ponti/viadotti/strade provinciali, sorveglianza di versanti instabili sopra la sede stradale |

**Rilievo regolatorio [FATTO]:** l'EO/sensing ambientale è la **missione a minimo attrito regolatorio** — non trasporta nulla, non sgancia, non riprende **sistematicamente** persone → **nessun trigger di missione** oltre a quello "di piattaforma" (BVLOS, scala, quota) (`13-fasce-regolatorio-missione.md` §1.4). L'onere aggiuntivo residuo è l'**overlay privacy** (DPIA, art. 34 ENAC APR Ed.3, Garante) **solo se** l'imagery cattura sistematicamente persone/targhe (`13` §1.2); per il monitoraggio boschivo/idrogeologico su versanti disabitati è tipicamente evitabile con un ConOps che esclude il sorvolo mirato del costruito abitato. **Da confermare con `data-privacy-counsel`.**

### 1.2 Chi opera e per chi (modello di servizio, non OEM) [coerente con `CLAUDE.md`]
- **Operatore:** Firmamento Technologies come **operatore di servizio ricorrente** (non vende la piattaforma; eroga un servizio di monitoraggio a canone/commessa). Modello identico a quello adottato per il resto della famiglia.
- **Committenti/utenti finali (B2G prevalente):**
  - **Protezione Civile** regionale e **Vigili del Fuoco** (antincendio boschivo — AIB; allertamento idrogeologico);
  - **Consorzi Forestali** e enti gestori dei Parchi (Parco dell'Antola, Parco dell'Aveto) — salute vegetazione, sorveglianza;
  - **Regione Liguria** e **Città Metropolitana di Genova** / **Province** (viabilità provinciale, ponti, versanti sopra strada);
  - reti di **cooperative Legacoop** (capofila Fabrica) come veicolo operativo/territoriale (`CLAUDE.md`).
- **Cadenza operativa [STIMA, confidence medium]:**
  - **Regime AIB (giugno-settembre, e ondate di calore):** pattugliamenti programmati quotidiani o bi-quotidiani nelle fasce orarie a massimo rischio (primo pomeriggio), più *surge on-demand* su allerta;
  - **Regime idrogeologico (autunno-inverno-primavera, eventi meteo):** attivazione *on-demand* post-evento (frane, dissesto) e campagne periodiche di baseline sui punti critici noti (ponti, versanti monitorati);
  - **Regime baseline (tutto l'anno):** una-due campagne/mese di aggiornamento cartografico/salute vegetazione.
  - La **lunga endurance (target 20 h)** è il differenziatore rispetto ai droni tattici a corto raggio: un singolo volo copre l'intero arco diurno + parte notturno (IR notturno per hotspot d'incendio è particolarmente prezioso), riducendo il numero di lanci/recuperi e il costo operativo per ora di copertura.

### 1.3 Pattern di missione — loiter/pattuglia su area vasta, NON punto-punto
- **Profilo:** **loiter e pattugliamento ad area vasta multi-versante** — orbite (racetrack/eight) e transetti programmati che spazzano più valli e versanti da una quota di osservazione unica, con re-tasking dinamico verso un punto d'interesse (hotspot, frana segnalata). **Non** è un profilo punto-punto in un borgo (quello era il caso della consegna a Pentema, `14` §2), ed è proprio questa differenza a ribaltare la scelta architetturale (vedi §1.5).
- **Copertura:** un'orbita a ~3.000 m AMSL con gimbal EO/IR brandeggiabile copre, per singola stazione di loiter, un'area con raggio utile di **[STIMA] 5-15 km** a seconda del sensore e della tolleranza di GSD (§2.4); rip-osizionando la stazione di loiter lungo un percorso pianificato, un volo da 10-20 h copre un'area di **centinaia di km²** — l'intera testata di una o più valli interne.
- **C2/BVLOS:** operazione **BVLOS** in Classe G, C2 in LOS radio dal sito di lancio o via ripetitore su crinale; SATCOM opzionale come ridondanza per la copertura oltre-orizzonte in terreno orograficamente complesso.

### 1.4 Siti di lancio (2-3 tipologie realistiche — NON necessariamente Pentema)
Il punto decisivo del ConOps: **il sito di lancio è disaccoppiato dall'area-bersaglio.** La piattaforma decolla da un sito scelto per lo spazio disponibile, transita all'area di pattuglia, e vi permane 10-20 h. Non serve che il sito di lancio sia dentro il borgo o la valle stretta da monitorare. Tre tipologie realistiche, tutte **fuori** dal confine spaziale di Pentema-borgo:

| # | Tipologia sito | Esempio ligure realistico | Idoneità catapulta/traino |
|---|---|---|---|
| **S1** | **Altopiano / sella di crinale** con strada o radura | Aree sommitali/selle del Parco dell'Antola; zone di passo (es. dorsali Torriglia-Antola, ~1.100-1.400 m) | Buona: corridoio di lancio libero verso valle, vento di crinale spesso favorevole al lancio controvento |
| **S2** | **Fondovalle agricolo pianeggiante** presso i centri delle Aree Interne | Piane alluvionali dell'alta Val Trebbia/Val d'Aveto presso Torriglia, Rovegno, Santo Stefano d'Aveto; aree agricole/prative di fondovalle (~500-850 m) | Buona per traino veicolo (pull) su strada/pista sterrata rettilinea; recupero a rete/paracadute su prato |
| **S3** | **Area logistica dedicata / eliporto-campo volo esistente** riconvertibile | Aviosuperfici e campi di volo dell'entroterra ligure/basso Piemonte prossimi all'area; piazzali di cantiere/AIB | Ottima: sito semi-preparato, ripetibile, base ricorrente per il servizio |

**Nota di coerenza [FATTO]:** Pentema-borgo (frazione di Torriglia a **839 m** sul fianco del Monte Prelà, [Wikipedia/topografia](https://it.wikipedia.org/wiki/Val_Trebbia)) resta **inadatta come sito di lancio** — è confinata, come già stabilito in `14` §4.8. Ma T-SORV **non ha bisogno di lanciare da Pentema**: lancia da S1/S2/S3 e **sorvola** Pentema e le altre frazioni come parte dell'area di pattuglia. Questo è esattamente il "ribaltamento della logica" richiesto (vedi §1.5).

### 1.5 Decisione VTOL vs NON-VTOL per questo caso d'uso — la logica si ribalta rispetto a `14`
`14-vtol-config-tradestudy-C3.md` §4.8/§7.2 aveva **squalificato** la baseline non-VTOL A7 (catapulta + recupero) per la missione **di consegna punto-punto a Pentema-borgo**, per un solo motivo: il vincolo di soglia C1 (idoneità confined-space) — non c'è spazio per una corsia di catapulta né per un'area di recupero a rete **dentro il borgo di destinazione**, perché nella consegna il punto di atterraggio/rilascio **coincide** con la destinazione confinata.

**Per T-SORV la premessa cade, e con essa il verdetto** [coerente con l'apertura esplicita di `14` §4.8 e §10.4]:
1. **La missione è ad AREA VASTA, non punto-punto.** Il punto di lancio/recupero **non coincide** con l'area osservata: è liberamente scelto su crinale/altopiano/piana (S1-S3, §1.4), dove lo spazio per catapulta/traino e per il recupero **esiste**. Il vincolo C1 che squalificava A7 a Pentema **non si applica** a un sito di lancio scelto per lo spazio.
2. **Il committente ha escluso il VTOL** come vincolo di progetto (catapulta o traino veicolo). Questo è **coerente e razionale** per questa fascia: un VTOL con apertura > 10 m e MTOM da MALE non esiste come prodotto COTS, la penalità di massa VTOL (15-22% MTOM per un lift+cruise, `14` §4.3) è **incompatibile con l'endurance target di 20 h**, e l'hover non serve a nulla in una missione di loiter d'alta quota. `14` §10.4 lo diceva già: *"per missioni EO/area-vasta su terreno diverso da Pentema, A7 (non-VTOL) resta l'opzione col miglior rapporto efficienza/costo/semplicità"*.
3. **La baseline non-VTOL è il vincitore "di merito"** anche nella matrice pesata pura di `14` §7.1 (score 7,65, il più alto in assoluto: massimi su crociera, frazione payload, semplicità) — era solo il gate confined-space a escluderla. Rimosso quel gate (missione ad area vasta), **A7 torna a vincere**.

**Verdetto VTOL per T-SORV: NON-VTOL confermato.** Decollo a **catapulta** (sito S1/S3 semi-preparato) o **traino/pull con veicolo terrestre** (sito S2 con corsia rettilinea), recupero a **rete/paracadute/skyhook** o **belly-landing** su striscia semipreparata. La scelta specifica del sistema di recupero è un trade study di secondo livello (TS separato, non in questo documento). L'apertura > 10 m e l'endurance 20 h **richiedono** questa architettura: è l'unica coerente con la fascia e con i vincoli del committente.

---

## 2. Morfologia del territorio interno ligure e target di quota operativa

### 2.1 Dati orografici verificati [FATTO — fonti web citate]
Regione operativa: Appennino ligure interno, area Torriglia/Pentema → Val Trebbia → Val d'Aveto (Parchi Antola e Aveto).

| Elemento orografico | Quota AMSL | Fonte |
|---|---|---|
| **Monte Maggiorasca** (vetta più alta dell'Appennino ligure) | **1.804 m** | [Wikipedia](https://en.wikipedia.org/wiki/Monte_Maggiorasca) |
| **Monte Penna** (Val d'Aveto) | **1.735 m** | [Wikipedia Appennino ligure](https://it.wikipedia.org/wiki/Appennino_ligure) |
| **Monte Aiona** (Val d'Aveto) | **1.701 m** | [appenninista.it](https://www.appenninista.it/appennino-ligure/gruppo-del-monte-maggiorasca/monte-aiona/) |
| **Monte Antola** (dorsale Torriglia, cuore del Parco) | **1.597 m** | [Wikipedia](https://en.wikipedia.org/wiki/Monte_Antola) |
| **Pentema** (frazione di Torriglia, fianco Monte Prelà) | **839 m** | [Val Trebbia / topografia](https://it.wikipedia.org/wiki/Val_Trebbia) |
| **Torriglia** (centro) | **769 m** | come sopra |
| **Sorgente del Trebbia** (fondovalle, piede Monte Prelà) | **~800 m** | come sopra |
| **Fondovalle Val Trebbia / Val d'Aveto** (piane e alvei tipici) | **~500-850 m** | [STIMA da profilo valle, medium] |

**Riconciliazione con `14` §2:** il documento `14` indicava Pentema "1100-1300 m s.l.m." — quel valore descrive il **contesto di versante/crinale circostante**, non il borgo, che sorge a **839 m** [FATTO]. Ai fini della quota operativa conta la **quota degli ostacoli orografici dominanti dell'area di pattuglia**, cioè i crinali/vette 1.600-1.804 m, non la quota del borgo.

**Sintesi morfologica [FATTO+STIMA]:**
- **Fondovalle e borghi:** ~500-900 m AMSL.
- **Versanti intermedi:** ~900-1.400 m.
- **Crinali e vette dominanti dell'area:** **1.600-1.804 m** (Antola 1.597, Aiona 1.701, Penna 1.735, Maggiorasca 1.804).
- **Dislivello tipico versante-crinale:** **800-1.300 m** su distanze orizzontali di pochi km → orografia ripida, **elevato mascheramento reciproco tra versanti opposti** (una missione multi-versante deve poter "guardare oltre" il crinale interposto).

### 2.2 Vincolo di spazio aereo [FATTO]
Lo spazio aereo italiano dal suolo fino a **FL195 (≈ 5.944 m / 19.500 ft) incluso è Classe G non controllata** ([ENAV/ANACNA/Wikipedia](https://it.wikipedia.org/wiki/Classificazione_dello_spazio_aereo)); in Classe G il VFR non richiede autorizzazione all'ingresso né contatto radio obbligatorio (fermi restando gli obblighi UAS BVLOS e il coordinamento ENAV/NOTAM per la specifica operazione). **Qualunque quota operativa ben sotto FL195 mantiene T-SORV in Classe G** — un margine ampio: anche a 3.500 m AMSL restano **~2.400 m** di margine sotto il tetto di Classe G. Questo è un **grado di libertà**, non un vincolo stringente: la quota può essere scelta sulla base di orografia e sensore, non sull'ingombro dello spazio controllato.

### 2.3 Requisito di linea di vista (LOS) su area di pattuglia multi-versante
Per pattugliare più versanti e vedere "oltre" i crinali interposti (1.600-1.804 m), la quota di osservazione deve dominare gli ostacoli con margine. Geometria di primo ordine [STIMA, medium]:
- Per avere **LOS ottica/sensoristica** su un versante rovescio protetto da un crinale a 1.804 m, la piattaforma deve stare **sopra** la quota del crinale con margine sufficiente a "affacciarsi" oltre la cresta entro il proprio cono di visione — in pratica **≥ 1.000-1.200 m sopra la vetta dominante** per coprire versanti rovesci a distanza utile senza doversi riposizionare in verticale sul crinale.
- Per la **LOS del datalink C2** in LOS radio, la stessa quota (o un ripetitore di crinale) garantisce collegamento sul sito di lancio e sull'area di pattuglia; SATCOM come ridondanza per i settori mascherati.

Vetta dominante 1.804 m + margine 1.000-1.200 m → **quota di lavoro dell'ordine di 2.800-3.000 m AMSL** per dominare l'intera regione operativa (compresa la Val d'Aveto, la più alta); per aree limitate al solo comprensorio Antola/Torriglia (dominante 1.597 m) sarebbe sufficiente **~2.600-2.800 m AMSL**.

### 2.4 Requisito di GSD del sensore EO/IR (vincolo verso il basso)
La quota alta favorisce copertura e LOS ma **degrada il GSD** (Ground Sample Distance). Ordine di grandezza [STIMA, medium — da validare con `earth-observation-expert`]:
- Un gimbal EO/IR di classe MALE (zoom EO + IR raffreddato MWIR/LWIR) opera utilmente a **slant range di 2-8 km**. A ~3.000 m AMSL su versanti a 800-1.400 m, gli slant range tipici di lavoro (off-nadir moderato) sono **2-5 km**, coerenti con **GSD sub-metrico** in EO e con la rivelabilità di hotspot termici in IR — adeguato sia per il rilevamento precoce d'incendio sia per il monitoraggio di frane/infrastrutture.
- Per **ispezioni di dettaglio** (fessurazione ponti, micro-movimenti di versante), la piattaforma **scende** temporaneamente a **2.000-2.500 m AMSL** (o si avvicina lateralmente riducendo lo slant range) per portare il GSD a pochi cm, poi risale in quota di loiter. La quota non è quindi un valore unico rigido ma una **banda operativa** con escursioni missione-dipendenti.

### 2.5 Target di quota raccomandato [STIMA, confidence medium — difendibile]
Sintesi dei tre vincoli (LOS multi-versante ↑, Classe G ↑↑ margine, GSD ↓):

| Parametro | Valore raccomandato | Margine/Motivazione |
|---|---|---|
| **Quota operativa nominale di loiter** | **3.000 m AMSL** | domina la vetta più alta (Maggiorasca 1.804 m) con **~1.200 m** di margine → LOS multi-versante sull'intera regione operativa; profondamente entro Classe G (margine ~2.900 m sotto FL195) |
| **Banda operativa nominale** | **2.500 - 3.500 m AMSL** | 2.500 m per comprensori a crinali più bassi (Antola, ~1.600 m) e miglior GSD; 3.500 m per massima copertura/LOS in campagne wide-area IR antincendio |
| **Escursioni di dettaglio (ispezione)** | **fino a ~2.000 m AMSL** | avvicinamento per GSD cm-metrico su ponti/frane; sempre in Classe G |
| **AGL equivalente** | **~1.200 m (sopra i crinali 1.800 m) → ~2.500 m (sopra i fondovalle 500-800 m)** | l'AGL varia con l'orografia sottostante; il riferimento operativo utile è l'**AMSL**, non l'AGL, data la forte variabilità del terreno |
| **Tetto di non-violazione spazio controllato** | **≤ FL195 (≈ 5.944 m AMSL)** | vincolo duro [FATTO] per restare in Classe G; il target 3.000 m lo rispetta con largo margine |

**Numero singolo difendibile: 3.000 m AMSL (≈ 9.850 ft) come quota nominale di loiter, banda 2.500-3.500 m.** La motivazione dominante è la **LOS su area di pattuglia multi-versante sopra i crinali 1.600-1.804 m**; il vincolo Classe G è largamente soddisfatto e non è stringente; il GSD è gestito con escursioni verso il basso. Questa quota è coerente con la fascia T2/T3 di `10-fasce-engineering.md` (T2 fino 4.000-5.000 m, T3 4.000-9.000 m: 3.000 m è al bordo inferiore, il che è **favorevole** — riduce i requisiti di pressurizzazione payload, densità aria, e potenza propulsiva rispetto a un MALE d'alta quota).

**Confidence:** **medium.** Regge sui fatti orografici (high) e sul vincolo Classe G (high); la traduzione in un numero singolo dipende da assunzioni [STIMA] su cono di visione del sensore e geometria di pattuglia, da validare con `earth-observation-expert` (GSD/slant range) e `avionics-gnc-engineer` (LOS C2, terrain masking).

---

## 3. Requisiti di sistema preliminari (estratto stile RTM)

Formato NASA RID (Req / Rationale / Verifica / Owner / Source). Requisiti *preliminary-grade*, da consolidare nella RTM del Capitolo 3 dello Studio.

| Req-ID | Requisito (VAFC) | Rationale | Verifica | Fonte |
|---|---|---|---|---|
| **SyR-SORV-01** | La piattaforma T-SORV deve operare a una quota nominale di loiter di **3.000 m AMSL (±500 m, banda 2.500-3.500 m)**, con escursioni di ispezione fino a **2.000 m AMSL** e tetto operativo **≤ FL195**. | Dominare i crinali 1.600-1.804 m dell'area (LOS multi-versante), restare in Classe G, gestire il GSD EO/IR. | Analysis (geometria LOS + link budget C2) + Test (voli di caratterizzazione a quota) | §2; `10-fasce` §5 |
| **SyR-SORV-02** | La piattaforma deve garantire un'**endurance ≥ 10 h, target 20 h**, a profilo di missione di loiter/pattuglia con payload EO/IR nominale. | Coprire l'intero arco diurno + finestra notturna IR con un solo lancio; ridurre il costo per ora di copertura. | Analysis (bilancio energetico/carburante) + Demonstration (volo di endurance) | Vincolo committente; `10-fasce` §5 (T3 10-40 h) |
| **SyR-SORV-03** | Il raggio d'azione di pattuglia dal sito di lancio deve essere **≥ 50 km** in LOS C2 (esteso via ripetitore/SATCOM), con copertura di più valli/versanti in un singolo volo. | Disaccoppiare sito di lancio e area-bersaglio; coprire un comprensorio SNAI, non un singolo punto. | Analysis (link budget) + Test | §1.3-1.4; `10-fasce` §5 (100-230 km tattico) |
| **SyR-SORV-04** | L'apertura alare deve essere **> 10 m**, con configurazione ad alto allungamento coerente con l'endurance target. | Efficienza aerodinamica per 20 h di loiter; vincolo committente. | Inspection (disegno) + Analysis (polare, aeroelasticità) | Vincolo committente; `Progetto concettuale struttura HALE.md` |
| **SyR-SORV-05** | Decollo mediante **catapulta o traino/pull con veicolo terrestre**; recupero mediante rete/paracadute/skyhook o belly-landing su striscia semipreparata. **NON-VTOL.** | Coerenza con missione area-vasta e siti di lancio S1-S3; incompatibilità del VTOL con span > 10 m ed endurance 20 h. | Demonstration (prove di lancio/recupero) | Vincolo committente; §1.5; `14` §4.8/§10.4 |
| **SyR-SORV-06** | Payload di missione **esclusivamente EO/IR** (gimbal EO ad alta risoluzione + IR MWIR/LWIR; opz. multispettrale/LiDAR). Nessun payload di trasporto/sgancio/relay di servizio. | Missione a minimo attrito regolatorio (nessun trigger di missione); confini di scope netti. | Inspection + Test (GSD, sensibilità termica) | §1.1; `13` §1.4 |
| **SsR-SORV-07** | La categoria regolatoria di riferimento è **Specific (SAIL IV-VI) o Certified** secondo la MTOM effettiva; l'operazione è **BVLOS in Classe G**. | Vincoli span/endurance/MTOM escludono l'Open/C3; MTOM > 150 kg → Certified probabile. | Analysis (SORA) + pre-application ENAC | §0.2; `10-fasce` §5.3; `13` §2 |

---

## 4. Falsifying observations (≥ 5)

Osservazioni che, se verificate, cambierebbero il target di quota o il ConOps:

1. **Sopralluogo sensoristico che mostri un terrain masking dei versanti rovesci non risolvibile a 3.000 m AMSL** (orografia più severa del previsto, con creste secondarie che schermano i settori d'interesse anche da 1.200 m sopra il crinale principale) → imporrebbe o una **quota superiore (3.500-4.000 m)**, o un profilo a **stazioni di loiter multiple** riposizionate sopra ciascun sub-comprensorio, o l'uso sistematico di ripetitori di crinale. Cambierebbe il numero singolo di §2.5.
2. **Requisito GSD di dettaglio più stringente del previsto** (es. rilevamento di fessurazioni sub-cm su ponti richiesto come standard di servizio, non come eccezione) → sposterebbe la **quota nominale verso il basso (2.000-2.500 m)** o imporrebbe un gimbal a focale molto lunga con costi/masse maggiori; ribilancerebbe il trade LOS↔GSD di §2.3-2.4.
3. **Designazione ENAC di un volume U-Space o di uno spazio a uso speciale sull'area** (es. per traffico AIB elicotteristico stagionale, o restrizioni sopra i Parchi) → potrebbe **imporre un tetto di quota inferiore a FL195** o finestre orarie, riconfigurando la banda operativa e il pattern di pattuglia. Il vincolo Classe G, oggi non stringente, diventerebbe dominante.
4. **MTOM effettiva > 150 kg confermata in fase di dimensionamento** → farebbe scattare la **Certified Category** (`10-fasce` §5.3), con requisiti di type-certificate e assicurativi che potrebbero rendere il servizio non finanziabile nell'orizzonte 6A — non cambia la quota, ma cambia la **fattibilità regolatoria/economica** del ConOps. Falsificherebbe l'ipotesi "Specific" di SsR-SORV-07.
5. **Interferenza operativa con il traffico AIB a bassa quota** (Canadair/elicotteri antincendio operano proprio nei versanti boschivi durante gli eventi, la finestra di massimo valore del servizio) → potrebbe imporre a T-SORV una **quota di segregazione più alta** o un ConOps di *deconfliction* temporale con la Protezione Civile, modificando pattern e quota nelle fasi di picco.
6. **Prova di volo che mostri un'aeroelasticità dell'ala > 10 m marginale alle raffiche di valle** (vento canalizzato/wind shear tipico dell'Appennino stretto, `14` §2) → non cambierebbe la quota target ma imporrebbe **vincoli di inviluppo (velocità/raffica) e di quota minima** per stare sopra lo strato di turbolenza orografica, spingendo la banda operativa verso l'alto (≥ 3.000 m) nelle giornate ventose.
7. **RFQ/dato vendor che dimostri l'inesistenza di una piattaforma T2/T3 non-VTOL con span > 10 m ed endurance 20 h acquistabile/configurabile** entro il budget di fascia (`10-fasce` §5: €2-10M/unità) → non cambierebbe quota né ConOps, ma sposterebbe la piattaforma da "buy/configure COTS" a "sviluppo custom", con impatto su costi e tempi (fuori scope di questo documento, rimando a `vtol-uas-specialist`/`financial-cfo-analyst`).

---

## Riga di fondo

**T-SORV** è una piattaforma fixed-wing ad alta endurance per **sola sorveglianza terrestre EO/IR** delle Aree Interne liguri — derivata dall'IP HALE ma **NON stratosferica**, quindi **immune** dagli showstopper del 6B (energy balance invernale, framework HAPS assente), che restano invariati. Il termine "C3" del committente è **respinto come incompatibile** (span > 10 m, endurance 20 h, certificazione ENAC → fascia **T2/T3 MID/MALE**, categoria **Specific SAIL IV-VI o Certified**, non Open). Il **ConOps** è un servizio B2G ricorrente (Protezione Civile, VVF, Consorzi Forestali, Regione Liguria) di **loiter/pattuglia su area vasta multi-versante**, con lancio a **catapulta o traino veicolo da siti scelti per lo spazio** (crinale/altopiano S1, fondovalle agricolo S2, campo-volo dedicato S3) — **disaccoppiati** dall'area osservata, così che Pentema si **sorvola** senza dover **lanciare** da Pentema. Su questa premessa, la **decisione VTOL si ribalta** rispetto a `14`: per una missione ad area vasta (non punto-punto in un borgo confinato) la baseline **NON-VTOL torna a vincere di merito**, coerentemente con `14` §10.4 e con il vincolo esplicito del committente — il VTOL è tecnicamente incoerente con span > 10 m ed endurance 20 h. Il **target di quota raccomandato è 3.000 m AMSL (≈ 9.850 ft) come loiter nominale, banda 2.500-3.500 m**, con escursioni a 2.000 m per l'ispezione di dettaglio: quota scelta per **dominare i crinali appenninici dominanti (Antola 1.597 m, Aiona 1.701 m, Penna 1.735 m, Maggiorasca 1.804 m) con ~1.200 m di margine di LOS multi-versante**, restando **profondamente entro la Classe G** (tetto FL195 ≈ 5.944 m, mai avvicinato) e mantenendo un **GSD EO/IR sub-metrico** utile alla missione. Confidence complessiva **medium**: fatti orografici e regolatori solidi (high), traduzione in numero singolo da validare con `earth-observation-expert` e `avionics-gnc-engineer`.
