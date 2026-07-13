# 25e — Payload EO/IR per piattaforma T-SORV di sola sorveglianza terrestre (Aree Interne liguri)

> **Volume:** Analisi bottom-up pre-Studio — approfondimento payload di `02-osservazione-terra.md` (fascia VTOL/C3) portato alla scala **T3a/T-SORV** definita in `10-fasce-engineering.md` §5 e `16-fasce-MALE-HALE-espanse.md` §2.
> **Data:** 13 luglio 2026
> **Autore:** Earth Observation Payload Expert
> **Mandato:** definire il **payload EO/IR** (nessun trasporto/consegna — solo sensori di osservazione) di una piattaforma fixed-wing endurance 10-20 h, apertura >10 m, MTOM 100-250 kg, quota di crociera 2.000-5.000 m AMSL, dedicata a due missioni terrestri sulle Aree Interne liguri: **(1) controllo aree boschive** (antincendio + salute vegetazione) e **(2) controllo viabilità** (frane, dissesto idrogeologico, infrastrutture stradali/ponti). Calcolo GSD alla quota assunta con sensitivity, frequenza/copertura, confronto satellite, downlink, falsifying observations.

---

## 0. Caveat epistemico e ancoraggio ai verdetti esistenti

**Confidence aggregata: MEDIUM**, dichiarata riga per riga. Marcatura: **[FATTO]** = specifica sensore/normativa verificabile con fonte pubblica o calcolo deterministico; **[STIMA]** = valutazione ingegneristica per analogia con banda dichiarata.

**Tre ancoraggi non negoziabili ereditati dal repository, che questo documento rispetta e non ribalta:**

1. **Il verdetto EO di `02-osservazione-terra.md` §7 resta valido.** La maggioranza dei servizi EO delle Aree Interne è **già coperta gratis da Copernicus** (frane wide-area via EGMS, post-incendio via Sentinel-2 NBR, agricoltura/foreste via Sentinel-2) **o, per il dettaglio puntuale, da un drone COTS a noleggio** (ispezione ponti/corridoi, fronte-frana). L'**unico** fattore che giustifica una piattaforma aerea dedicata è la **PERSISTENZA** (loitering continuo + bassa latenza), che abilita solo **early-detection incendi** e **overwatch di emergenza Protezione Civile**. Questo documento **non** riapre la questione "vale la pena una piattaforma dedicata?" (risposta: stretta e contesa da torri fisse e drone tattico); **assume** che la piattaforma T-SORV esista per decisione a monte e ne progetta il payload nel modo più difendibile.
2. **La quota cambia tutto rispetto all'HALE.** A 2.000-5.000 m (non 20 km) il sistema ottico è **largamente resolution-limited** in tutte le bande, incluso il LWIR: la diffrazione non è più il collo di bottiglia dominante che era per l'HALE (`02` §2). Questo è il vantaggio fisico decisivo di questa fascia sull'HALE per l'EO terrestre.
3. **Fixed-wing >10 m di apertura a 100-250 kg richiede infrastruttura di lancio/recupero** (pista ≥300-500 m o catapulta+skyhook). Coerente con `16` §2.2: **incompatibile con l'orografia appenninica senza un sito attrezzato dedicato** — non decolla da Pentema. Questo è un vincolo operativo di sistema, non di payload, ma va dichiarato perché condiziona la frequenza di rivisitazione reale (§6). [FATTO — vincolo fisico noto]

---

## 1. Piattaforma assunta e budget payload disponibile

| Parametro | Valore assunto | Fonte/base |
|---|---|---|
| Classe | T3a "MALE tattico piccolo" / T-SORV | `10` §5, `16` §2.1 (Tekever AR5, Schiebel S-100 come archetipi) |
| MTOM | 100-250 kg | mandato |
| Apertura | >10 m | mandato |
| Endurance | 10-20 h | mandato (coerente EMSA AR5 16-20 h [FATTO]) |
| Quota crociera | 2.000-5.000 m AMSL | mandato (assunto) |
| Velocità crociera | 110-150 km/h (≈30-42 m/s) | `10` §5 bracket T3 [STIMA] |
| **Payload utile** | **4-40 kg** (ISR compatto → multi-sensore) | `10` §5.1, `16` §2.1 [FATTO bracket] |
| Potenza payload disponibile | 200-600 W [STIMA] | scalabile da ICE heavy-fuel + generatore di bordo T3 |
| Downlink | 100-230 km LOS tattico (+SATCOM BLOS opz.) | `10` §1 riga Range/C2 |

**Implicazione:** con 4-40 kg e 200-600 W a disposizione, **non c'è vincolo di massa/potenza stringente** sul payload EO/IR (a differenza dell'HALE, dove ogni kg è critico). Si può imbarcare un **gimbal EO/IR stabilizzato multi-sensore** (5-15 kg) **e**, in alternanza o in parallelo, una **camera cartografica large-format** (2-4 kg) e/o un **sensore multispettrale** (0,5-1 kg). Il LiDAR (§4) è il solo payload che mette pressione al budget e va giustificato caso per caso.

---

## 2. Framework GSD, swath e note fisiche alla quota T-SORV

Formula: **GSD [m] = (h × pixel_size) / focal_length**, con **h = quota AGL** (Above Ground Level), **non** AMSL.

### 2.1 La complessità operativa dell'orografia ligure: h non è costante

**Questo è il punto metodologicamente più importante del documento.** La quota è data in AMSL (sul livello del mare), ma il GSD dipende dalla quota **AGL = AMSL − quota del terreno sorvolato**. In Appennino ligure il terreno sotto la stessa rotta varia enormemente:

- fondovalle (es. torrente Scrivia/Trebbia): ~300-500 m s.l.m.;
- crinali e vette (Monte Antola **1.597 m** [FATTO], Monte Aiona ~1.700 m nel Parco Aveto): ~1.500-1.700 m s.l.m.

Con la piattaforma a **4.000 m AMSL** costante, l'AGL passa da **~3.600 m sul fondovalle** a **~2.400 m sopra il crinale dell'Antola** — un **rapporto 1,5×** lungo la stessa passata. Poiché GSD ∝ AGL, **il GSD si degrada del ~50% dal fondovalle al crinale** a quota barometrica costante. Conseguenze operative dichiarate:

1. Il GSD **non è un numero unico** ma un **intervallo lungo la rotta**; ogni specifica di prodotto deve dichiarare "GSD ≤ X su tutto l'inviluppo di quota-terreno atteso", dimensionando sul **caso peggiore (fondovalle, AGL massima)**.
2. Il volo a **AGL costante** (terrain-following, quota barometrica variabile) uniforma il GSD ma è più esigente per GNC/DAA in valle stretta e alza il consumo; il volo a **AMSL costante** è più semplice e sicuro ma lascia il GSD variabile. È un trade GNC-payload da chiudere con `avionics-gnc-engineer`.
3. Per la fotogrammetria/orthomosaico la quota-terreno variabile impone **GSD di progetto sul punto più alto del blocco** e ricampionamento — o strisciate a quota adattata per fascia altimetrica.

### 2.2 Calcolo GSD e swath — RGB large-format

Assunzioni sensore RGB: **Phase One iXM-100** (100 MP, sensore 43,9×32,9 mm, **pixel 3,76 µm**) o **Sony α7R V** (61 MP, pixel 3,76 µm) [FATTO — datasheet vendor]. GSD e swath a tre quote AGL rappresentative (2.000 / 3.000 / 5.000 m) e due focali:

| Ottica | Grandezza | AGL 2.000 m | AGL 3.000 m | AGL 5.000 m |
|---|---|---|---|---|
| **f = 100 mm** | GSD RGB | 7,5 cm | 11,3 cm | 18,8 cm |
| | Swath (sensore 43,9 mm) | 0,88 km | 1,32 km | 2,20 km |
| **f = 200 mm** | GSD RGB | 3,8 cm | 5,6 cm | 9,4 cm |
| | Swath | 0,44 km | 0,66 km | 1,10 km |
| **f = 300 mm** | GSD RGB | 2,5 cm | 3,8 cm | 6,3 cm |
| | Swath | 0,29 km | 0,44 km | 0,73 km |

**Lettura:** con una focale media (100 mm) si ottiene **GSD 7-19 cm su swath 0,9-2,2 km** — il miglior compromesso copertura/dettaglio; con teleobiettivo (300 mm) si scende a **2,5-6 cm** ma con swath 0,3-0,7 km. Entrambi soddisfano i target ottici di §4-5 (≤0,1 m infrastrutture; ≤0,2 m frane) su gran parte dell'inviluppo, con il caso 5.000 m/f=100 mm (18,8 cm) al limite superiore per le infrastrutture — da coprire scendendo di quota o allungando la focale.

**Nota diffrazione (favorevole):** nel visibile (λ=0,5 µm) con f=300 mm a f/4 (apertura 75 mm), il limite di Rayleigh angolare è 1,22·λ/D = 8,1 µrad → a 3.000 m ≈ **2,4 cm a terra**, comparabile al GSD del sensore. Il sistema è **resolution-limited**, la GSD calcolata è realizzabile. [FATTO — calcolo]

### 2.3 Calcolo GSD — termico LWIR

Assunzioni: microbolometro non raffreddato **640×512, pixel 12 µm** (es. Teledyne FLIR Boson/Hadron; Workswell WIRIS) [FATTO]. Opzione high-end **1024×768, pixel 12 µm**.

| Ottica LWIR | AGL 2.000 m | AGL 3.000 m | AGL 5.000 m |
|---|---|---|---|
| **f = 25 mm** | GSD 0,96 m · swath 0,61 km | GSD 1,44 m · swath 0,92 km | GSD 2,40 m · swath 1,54 km |
| **f = 50 mm** | GSD 0,48 m | GSD 0,72 m | GSD 1,20 m |
| **f = 100 mm** | GSD 0,24 m | GSD 0,36 m | GSD 0,60 m |

**Lettura:** il GSD termico è **0,24-2,4 m** — **ampiamente sotto il target ≤5 m per hotspot detection** (`02` §3 riga 2b) a tutte le quote e focali. La focale corta (25 mm) massimizza lo swath (fino 1,5 km) mantenendo GSD < 2,5 m, ideale per la scansione antincendio d'area.

**Nota diffrazione LWIR (il contrasto con l'HALE):** a λ=10 µm con f=100 mm a f/1,2 (apertura 83 mm), il limite di Rayleigh è 1,22·10µm/0,083 = 147 µrad → a 3.000 m ≈ **0,44 m** a terra, **comparabile** al GSD del sensore (0,36 m). Il sistema è **prossimo ma non oltre** il limite di diffrazione. **Contrasto decisivo con l'HALE**: a 20 km lo stesso LWIR era **diffraction-limited a 2,4 m** (`02` §2); a 2-5 km il collo di bottiglia si sposta sul sensore e il termico diventa **10× più fine**. È la ragione fisica per cui questa fascia batte l'HALE sull'EO terrestre. [FATTO — calcolo]

**Detection ≠ risoluzione (information resolution).** Un focolaio incipiente di 1 m² resta sub-pixel a 0,5-1,5 m di GSD, ma la sua radianza satura l'intero pixel (stesso principio di VIIRS che rileva a 375 m incendi molto più piccoli): la **rilevabilità dell'hotspot non richiede che il fuoco riempia il pixel**. Distinguere "rilevo la sorgente calda" (facile, sub-pixel) da "misuro l'area bruciata" (richiede GSD ≤ dimensione target). [FATTO — fisica radiometrica]

### 2.4 Calcolo GSD — multispettrale (NDVI/salute vegetazione)

Sensore multispettrale a più bande discrete (es. **AgEagle/MicaSense Altum-PT** o **RedEdge-P**: bande blue/green/red/red-edge/NIR + termico integrato) [FATTO]. Nota: questi sensori sono ottimizzati per volo basso (<120 m AGL) con focali corte (~8 mm) → a quota T-SORV il GSD è metrico. Con pixel multispettrale ~3,45 µm, f=8 mm: GSD ≈ **0,86 m/1.000 m di AGL** → **1,7-4,3 m** a 2.000-5.000 m. Adeguato per NDVI/NDRE di stand forestale, **grossolano per il singolo albero**. Per NDVI a GSD decimetrico servirebbe un multispettrale con ottica lunga custom (non COTS agricolo) — non giustificato a questa scala. **NDVI a 2-4 m è comunque 3-10× più fine di Sentinel-2 (10-20 m)** (§7). [STIMA — GSD; FATTO — specifiche COTS]

---

## 3. Complessità dichiarate e limiti fisici (onestà preventiva)

- **GSD variabile con l'orografia** (§2.1): il numero di GSD è un intervallo, non un punto. Dimensionare sul caso peggiore.
- **Occlusione forestale:** le Aree Interne liguri sono forestate al 77-90% (`02` §1 [FATTO]). L'ottico/termico **vede la chioma, non il suolo sotto** — critico per le frane in bosco (il movimento del terreno sotto copertura resta invisibile all'EO passivo; serve LiDAR con penetrazione tra le fronde o SAR/DInSAR, §4).
- **Nuvolosità invernale elevata** (`02` §1): l'EO ottico/IR è **cieco sotto le nuvole**. La finestra utile per il monitoraggio frane in stagione piovosa (quando le frane sono più probabili) è proprio quella più penalizzata dalle nubi. È un limite strutturale dell'EO passivo a 2-5 km (a differenza del SAR, che però è pesante — §4).
- **Termico e vegetazione:** l'irraggiamento solare riscalda rocce/suolo esposto creando falsi hotspot diurni; la finestra migliore per il termico antincendio è **alba/tramonto/notte** (contrasto termico massimo, minimo disturbo solare).

---

## 4. Payload missione 1 — controllo aree boschive (antincendio + salute vegetazione)

### 4.1 Requisiti derivati

| Sotto-servizio | GSD target | Bande | Persistenza | Latenza alert |
|---|---|---|---|---|
| Early-detection incendi | ≤5 m termico (soddisfatto: 0,24-2,4 m) | **LWIR** (+ RGB per conferma) | continua finestra estiva/red-flag | ≤5 min (`02` §3) |
| Mappatura fronte attivo | 1-5 m | RGB + LWIR live | continua durante evento | quasi-real-time |
| Salute vegetazione / stress idrico | 1-4 m | **Multispettrale (NDVI/NDRE) + termico** | periodica (quindicinale) | ore |

### 4.2 Payload raccomandato

- **Gimbal EO/IR stabilizzato multi-sensore** — l'elemento primario. Archetipi COTS maturi in fascia T3: **Teledyne FLIR StormCaster/Star SAFIRE**, **L3Harris WESCAM MX-10/MX-15**, **Next Vision Colibri2/Raptor**, **Trillium HD55** [FATTO — prodotti esistenti]. Contiene: canale **LWIR** (640×512 o 1024×768, radiometrico, **NEdT ≤ 50 mK** tipico degli uncooled di fascia; opzione **MWIR raffreddato NEdT ≤ 20-30 mK** per sensibilità termica superiore, a costo di massa/potenza/€ maggiori) + canale **EO diurno** (zoom continuo 30-60×) + telemetro laser + geo-pointing. Massa 5-15 kg, potenza 50-150 W [FATTO — bracket categoria].
  - **Soglia NEdT antincendio:** per discriminare un hotspot incipiente dal fondo servono ΔT rilevabili di pochi K; una **NEdT ≤ 50 mK** (uncooled buono) è ampiamente sufficiente, poiché il ΔT di un focolaio vs bosco è di decine-centinaia di K. Il MWIR raffreddato (NEdT ≤ 30 mK) si giustifica **solo** per detection a lunga gittata obliqua o in presenza di forte foschia, non per il nadir a 2-5 km. [STIMA — soglia; FATTO — NEdT di categoria]
- **Camera multispettrale** (AgEagle Altum-PT / RedEdge-P o MicaSense-class) per NDVI/NDRE/GNDVI di salute forestale — 0,5-1 kg, 5-10 W [FATTO]. Missione non urgente, alternabile con il gimbal.
- **Camera RGB large-format** (iXM-100 / α7R V) per conferma visiva ad alta risoluzione dell'hotspot e mappatura post-evento severità.

**Modalità operativa antincendio:** scansione LWIR a focale corta (25 mm, swath ~1 km, GSD ≤2,4 m) in pattern di loiter sopra la valle a rischio; su rilevamento di anomalia termica, **cue automatico** del canale EO zoom per conferma e geolocalizzazione; alert + thumbnail in downlink a bassa banda entro secondi. Finestra: **persistent surveillance estiva** (giugno-settembre, giornate red-flag) — è **il** caso d'uso che giustifica la persistenza (`02` verdetto).

---

## 5. Payload missione 2 — controllo viabilità e dissesto idrogeologico

### 5.1 Requisiti derivati

| Sotto-servizio | GSD target | Bande | Frequenza | Note |
|---|---|---|---|---|
| Rilevamento frane (fronte attivo/nuovo) | ≤0,2 m + change-detection | RGB stereo + LWIR | settimanale (stagione piovosa) / mensile (secca) | multi-passaggio per change detection |
| Deformazione lenta (mm-cm/anno) | — | **SAR DInSAR** | 6-12 gg | **dominato da EGMS Copernicus gratuito** (`02` 1a) — NON replicare |
| Ispezione strade/corridoi | ≤0,1 m | RGB + (LiDAR) | trimestrale + post-evento | |
| Ispezione ponti/viadotti (dettaglio strutturale) | ≤0,01 m | close-range | on-demand | **dominato da drone COTS ravvicinato** (`02` 4a) — NON replicare |

### 5.2 Payload raccomandato e trade LiDAR

- **RGB large-format stereo/nadir (iXM-100 / α7R V, f=200-300 mm)** — GSD **2,5-9,4 cm** (§2.2): soddisfa ≤0,2 m per le frane e ≤0,1 m per i corridoi stradali su gran parte dell'inviluppo. È il **cavallo di battaglia** della missione viabilità.
- **Change-detection multi-passaggio:** il valore aggiunto della piattaforma dedicata è la **rivisitazione frequente e georeferenziata dello stesso versante** (settimanale in stagione piovosa) → confronto orthomosaico t vs t+1 per individuare nuove nicchie di distacco, coronamenti, deformazioni del piano stradale, colamenti. La persistenza/frequenza è qui il differenziante rispetto a Sentinel-2 (5 gg, 10 m) e al drone-spot (dispiegato solo dopo l'allarme).
- **LWIR** come canale complementare: le venute d'acqua/zone sature a monte di un dissesto hanno firma termica distinta (umidità → inerzia termica diversa) — utile ma secondario.

**Trade LiDAR — [STIMA, confidence media]:** un LiDAR aviotrasportato (**RIEGL VUX-1/miniVUX**, **YellowScan Voyager/Explorer**; 3-15 kg, 50-200 W) darebbe DTM 3D sotto-chioma (penetrazione tra le fronde) e struttura dei corridoi lineari. **Ma:**
1. **Rientra nel budget massa/potenza T3** (3-15 kg su 4-40 kg disponibili) — fattibile, a differenza dell'HALE.
2. **Efficienza a 2-5 km AGL discutibile:** i LiDAR topografici UAV sono ottimizzati per 50-500 m AGL; a 2.000-5.000 m la densità di punti crolla e serve un sensore long-range dedicato (classe airborne survey, non UAV), più pesante e costoso. **La quota T-SORV è ai limiti superiori dell'utilità LiDAR compatto.**
3. **Sostituto dominante:** per il DTM/LiDAR di dettaglio su sito noto, il **drone COTS a 120 m AGL** (Zenmuse L2, YellowScan Mapper) domina in densità di punti e costo (`02` 1b, 4b) — la frana è un fenomeno **lento e localizzato**, l'ispezione è point-in-time programmabile, la persistenza è irrilevante.

**Verdetto LiDAR [STIMA]:** **NON integrare LiDAR di serie** su T-SORV per la missione viabilità. Il DTM di dettaglio è più efficiente ed economico con drone COTS on-demand a bassa quota; a 2-5 km AGL il LiDAR compatto rende poco. Riservare il LiDAR a un **modulo opzionale** solo se emerge un requisito di DTM ripetuto su area vasta non copribile a bassa quota — improbabile a questa scala. La **SAR/DInSAR per frane lente resta esclusa** (dominata da EGMS gratuito **e** troppo pesante: 25-50 kg, 200-500 W — al limite/oltre il budget T3, coerente con `10` tabella sensori).

---

## 6. Frequenza di rilevamento e copertura d'area

### 6.1 Estensione del territorio-obiettivo

| Ambito | Estensione | Fonte | Conf. |
|---|---|---|---|
| Area pilota **Antola-Tigullio** (16 comuni, incl. Torriglia/Pentema, Valle Scrivia+Trebbia) | ~300-500 km² [STIMA su analogia aree SNAI Liguria 185-442 km²] | `02` §1; `rapporto-istruttoria_regione-liguria.md` | media |
| Singola area SNAI Liguria | 185-442 km² | `02` §1 [FATTO] | alta |
| Totale Aree Interne Liguria (8 aree) | ~3.050 km² | `02` §1 [FATTO] | alta |

### 6.2 Copertura oraria (calcolo)

Tasso di copertura di strisciata = **swath × velocità al suolo**. Con RGB f=100 mm a 3.000 m AGL (swath **1,32 km**, GSD 11 cm) e crociera **130 km/h**:

- Copertura lorda di strisciata = 1,32 km × 130 km/h = **~172 km²/h**.
- Applicando fattori realistici — sovrapposizione laterale 30% per mosaicatura, virate di fine strisciata, riposizionamento (fattore ~0,6) — **copertura netta ≈ 80-120 km²/h** [STIMA].
- Per pura **sorveglianza a scansione** (non fotogrammetria, overlap minimo) la copertura sale verso **150-170 km²/h**; per **mappatura orthomosaico** (overlap 70/60%) scende verso **50-80 km²/h**.

### 6.3 Cicli di monitoraggio

| Scenario | Calcolo | Risultato |
|---|---|---|
| Sweep completo area pilota (~400 km²) a 100 km²/h netti | 400/100 | **~4 ore di volo** |
| Sortite necessarie con endurance 12 h (dedotto transito/loiter, ~8 h utili) | 400 km² / (8 h × 100) | **1 sortita copre l'area pilota ~2 volte** |
| Rivisitazione area pilota per sortita | — | **fino a 2-3 passaggi/giorno** |
| Ciclo completo Aree Interne Liguria (~3.050 km²) a 100 km²/h | 3.050/100 = ~30,5 h di volo | **~2-3 sortite (2-3 giorni)** per una copertura wall-to-wall |

**Lettura:** con endurance 10-20 h la piattaforma **rivisita l'area pilota più volte al giorno** (contro i 5 giorni di Sentinel-2) e **copre l'intera Liguria interna in 2-3 giorni**. Il vincolo reale **non è la copertura oraria** ma **(a)** la disponibilità del sito di lancio/recupero attrezzato (§0 punto 3), **(b)** la nuvolosità (§3), **(c)** l'economicità di volare per una copertura così frequente su un territorio dove il fenomeno da monitorare (frana lenta, fenologia) è più lento della rivisitazione ottenibile — cioè **la persistenza è tecnicamente facile ma spesso sovrabbondante** rispetto al bisogno, tranne nelle due finestre (antincendio estivo, emergenza PC) in cui la bassa latenza conta davvero (`02` §4).

---

## 7. Confronto con satellite (Copernicus / Sentinel-2)

Replica del ragionamento HALE-vs-satellite di `02`, ma per una piattaforma **più economica e già disponibile oggi** (TRL 8-9 vendor, non subordinata alla maturazione tecnologica HALE):

| Parametro | **T-SORV @ 2-5 km** | **Sentinel-2 (Copernicus)** | **Sentinel-3 SLSTR / VIIRS (fire)** | **Pléiades Neo (commerciale)** |
|---|---|---|---|---|
| GSD ottico | **2,5-19 cm** | 10 m (10/20/60 m per banda) | — | 0,30 m |
| GSD termico | **0,24-2,4 m** | — (S2 non ha termico) | 1 km (SLSTR) / 375 m (VIIRS) | — |
| Rivisitazione | **più volte/giorno → continua in loiter** | 5 giorni (S2A+S2B) | ~2×/giorno (VIIRS) | 1-2 gg (tasking) |
| Latenza dato | **minuti** (downlink diretto) | ore-giorni | ~3 h (FIRMS) | ore (tasking) |
| Swath | 0,3-2,2 km | 290 km | 1.270-3.000 km | 14 km |
| Vincolo nuvole | sotto le nubi alte, **cieco sotto nubi basse** | sopra le nubi (limitato) | sopra (limitato) | sopra (limitato) |
| Costo | asset dedicato (OpEx alto) | **gratuito** | gratuito | €5-20/km² tasking |
| Disponibilità | **oggi (COTS TRL 8-9)** | oggi | oggi | oggi |

**Dove T-SORV vince nettamente:** **risoluzione** (2-3 ordini di grandezza sul termico vs VIIRS/SLSTR; 40-400× sull'ottico vs Sentinel-2) **+ latenza** (minuti vs ore-giorni) **+ rivisitazione on-demand persistente** su un versante specifico. Un focolaio incipiente rilevato a 0,5-2 m di GSD con alert in ≤5 min è **irraggiungibile** da VIIRS (375 m, latenza ~3 h) e da Sentinel-2 (nessun canale fire, 5 gg). Per l'**early-detection incendi** e l'**overwatch di emergenza** il vantaggio è reale e strutturale.

**Dove il satellite resta dominante (onestà):** **deformazione frane lenta wide-area** → **EGMS Copernicus gratuito** (mm/anno, 100 m, Sentinel-1 DInSAR) non è battibile da EO passivo (`02` 1a); **severità post-incendio** (dNBR) → **Sentinel-2 NBR gratuito** a 10-20 m è sufficiente (`02` 2a); **copertura wall-to-wall di migliaia di km²** → lo swath satellitare (290 km) vs 1-2 km del T-SORV rende il satellite imbattibile in produttività d'area a bassa risoluzione. **La regola di `02` regge: il satellite gratuito domina il "wide-area lento"; il T-SORV vince solo dove servono insieme alta risoluzione + bassa latenza + persistenza su area ristretta.**

**Rispetto all'HALE:** T-SORV offre lo **stesso vantaggio di persistenza/latenza** dell'HALE per l'EO terrestre locale, con **GSD migliore** (più vicino al terreno) e a **1-2 ordini di grandezza di costo/rischio in meno**, **disponibile oggi** senza attendere la maturazione (energy balance invernale, aeroelasticità, framework HAPS) che blocca l'HALE (`16` §3). Per la **sola sorveglianza terrestre delle Aree Interne**, T-SORV **domina l'HALE** — lo swath da 3 km dell'HALE è capacità sprecata su valli di 300-500 km² (`02` §5).

---

## 8. Downlink dati

**Requisito:** trasmettere EO/IR in **quasi-real-time** durante 10-20 h di missione, coerente con il link C2/dati mappato per T3 (`10` §1: 100-230 km LOS tattico + SATCOM BLOS opzionale) e con `01-connettivita.md` (il downlink da quota "non è un problema a nessuna quota", SNR ≥ 13 dB, capacità 20-100 Mbps/settore [FATTO]).

| Flusso | Banda richiesta | Note |
|---|---|---|
| **Alert antincendio (hotspot + thumbnail + coord)** | **< 0,5 Mbps** | il flusso critico a bassa latenza; passa su qualsiasi datalink, anche SATCOM stretto |
| **Video EO/IR compresso live (H.265, HD/4K)** | **5-20 Mbps** | streaming gimbal per overwatch/PC; standard ISR [FATTO] |
| **Multi-sensore live (EO+IR+chip full-res selettivi)** | **10-50 Mbps** | ampiamente entro i 20-100 Mbps/settore di `01` |
| **Orthomosaico full-res 100 MP (bulk)** | non in real-time | archiviato a bordo (SSD), scaricato in burst LOS ad alta capacità vicino base o via rimozione fisica del supporto |

**Architettura raccomandata:**
- **Datalink direzionale LOS** (banda C/S/Ku, 10-50 Mbps) come primario entro 100-230 km dalla stazione di terra — sufficiente per video EO/IR live e alert. A 2-5 km AMSL la LOS scavalca i crinali locali meglio che da terra (vantaggio di quota di `01` §4).
- **SATCOM BLOS di back-up** (Iridium Certus a bassa banda per C2/alert sempre-attivo; **Starlink/OneWeb** se serve alta banda oltre-LOS, a costo di massa/potenza payload aggiuntivi) — per copertura oltre l'orizzonte radio o quando l'orografia interrompe la LOS.
- **Alert su canale prioritario a bassa banda** disaccoppiato dal video: garantisce la latenza ≤5 min anche se il video ad alta banda è degradato.

**Verdetto downlink:** **non è un vincolo dimensionante.** Il flusso critico (alert) è minuscolo; il video live (5-20 Mbps) sta comodamente nella capacità già dimostrata in `01`; il bulk full-res non è real-time e non compete per la banda. Coerente con T2/T3 senza necessità di link esotici.

---

## 9. Compliance (sintesi)

- **GDPR** (Reg. UE 2016/679 + D.Lgs. 196/2003): sorveglianza EO ricorrente su territorio che include abitato (borghi, viabilità) → serve **base giuridica** (interesse pubblico/PA titolare — Regione Liguria è già Titolare dei dati SNAI, `02` §6), **minimizzazione** (risoluzione volti/targhe evitabile a GSD ≥ 5-10 cm se non necessaria; mascheramento), **DPIA preliminare** per EO ricorrente su abitato. Rimando a `data-privacy-counsel`. Conf. alta.
- **Riprese aeree cartografiche:** acquisizioni sistematiche georeferenziate ad alta risoluzione possono ricadere nella normativa sulla **fotografia aerea/cartografia** (nulla-osta per uso commerciale in aree sensibili — infrastrutture, siti militari). Da verificare per acquisizioni ricorrenti. Conf. media.
- **ENAC/EASA:** MTOM 100-250 kg fixed-wing BVLOS su area montana → **Specific Category SAIL alto** (probabile SAIL IV-VI) o **Certified** oltre 150 kg — **nodo regolatorio non risolto** (0 Type Certificate EASA mai emessi; via praticabile DVR + regime agenzia, `16` §2.7). Rimando a `aviation-regulatory-counsel`/`regulatory-adversary`. Conf. alta sul rischio.

---

## 10. Falsifying observations

Osservazioni che, se occorressero, **falsificherebbero** il valore del payload T-SORV qui proposto o ne cambierebbero il dimensionamento:

1. **[Persistenza sovrabbondante]** Se un pilota reale su Antola-Tigullio mostra che **la frequenza di monitoraggio utile è settimanale/mensile** (fenomeni lenti: frane, fenologia) e che le finestre a vera bassa-latenza (incendio attivo, alluvione) sono **poche giornate/anno**, allora la persistenza multi-oraria del T-SORV è **capacità sprecata** e il servizio è meglio erogato da **drone COTS on-demand + Copernicus**, coerentemente con `02` §7. *Stato 2026: nessun pilota ha misurato la domanda reale → ipotesi non confermata.* [STIMA]

2. **[Occlusione forestale distrugge il caso frane]** Se su copertura forestale 77-90% l'EO passivo **non vede il suolo** e le frane rilevanti avvengono **sotto chioma**, allora RGB+LWIR sono ciechi sul fenomeno-bersaglio e servirebbe LiDAR penetrante o SAR (entrambi problematici: LiDAR poco efficiente a 2-5 km, SAR troppo pesante). *Verificabile con un test su un versante boscato noto instabile.* [FATTO — fisica dell'occlusione; STIMA — impatto operativo]

3. **[Nuvolosità azzera la finestra utile]** Se nella stagione piovosa ligure la copertura nuvolosa bassa rende l'EO ottico/IR inutilizzabile **proprio quando le frane sono più attive**, il valore del monitoraggio frane crolla e il satellite SAR (Sentinel-1/EGMS, all-weather) resta l'unica opzione — gratuita. *Quantificabile con statistica di cloud-cover ARPAL sui mesi ottobre-marzo.* [FATTO — limite EO passivo]

4. **[Termico batte l'HALE ma non le torri fisse]** Se una **rete di torri camera termiche su crinale** (già benchmark di `02` §5, €10-50k/torre, h24, latenza nulla) copre l'early-detection incendi a costo inferiore, il payload antincendio T-SORV è **dominato al suolo** per la sola detection statica; il T-SORV mantiene vantaggio solo per l'**overwatch mobile del fronte attivo** (che la torre fissa non fa). *Confrontabile con un TCO torri vs ore-volo su una stagione.* [STIMA]

5. **[GSD reale peggiore del calcolato]** Se in volo reale il GSD sul crinale (AGL minima 2.400 m ma turbolenza orografica, vibrazione gimbal, foschia di valle) risulta **>50% peggiore** del calcolo geometrico di §2, allora i target ≤0,1 m (infrastrutture) e ≤0,2 m (frane) **non sono raggiunti a 5.000 m AMSL** e la piattaforma deve scendere di quota (riducendo copertura/sicurezza) o rinunciare a quei target. *Verificabile con una campagna di calibrazione GSD su target noti a diverse quote-terreno.* [STIMA]

6. **[LiDAR necessario dopo tutto]** Se il DTM sotto-chioma richiesto dal PAI per il monitoraggio frane **non è ottenibile** con drone COTS a bassa quota (accesso negato, area troppo vasta) e serve LiDAR aviotrasportato d'area, il verdetto "no LiDAR di serie" (§5.2) cade e il budget massa/potenza va rivisto. *Stato: nessun requisito PAI verificato in dettaglio in questo documento.* [STIMA]

7. **[Il satellite migliora e chiude la nicchia]** Se costellazioni EO commerciali ad alta rivisitazione (Planet, ICEYE SAR sub-daily, futuri Sentinel Next-Gen) portano la **rivisitazione sub-giornaliera a risoluzione metrica** su tasking economico, la finestra di persistenza/latenza del T-SORV si restringe. *Stato 2026: ancora latenza di ore e costo €5-50/km² → finestra aperta.* [FATTO]

---

## 11. Riga di fondo

Per la **sola sorveglianza terrestre** delle Aree Interne liguri, la piattaforma **T-SORV (fixed-wing, 100-250 kg, 10-20 h, 2-5 km AMSL)** ha un vantaggio EO fisico decisivo sull'HALE: a bassa quota il sistema è **resolution-limited anche nel LWIR** (a 20 km era diffraction-limited), quindi il termico è ~10× più fine. **Payload raccomandato: gimbal EO/IR stabilizzato multi-sensore** (LWIR 640-1024 px NEdT ≤50 mK + EO zoom, classe WESCAM/Star SAFIRE/Trillium, 5-15 kg) come primario, **+ camera RGB large-format** (iXM-100/α7R V, 2-4 kg) per il dettaglio ottico e la change-detection frane, **+ multispettrale** (Altum-PT/RedEdge-P, <1 kg) per NDVI salute boschiva. **No LiDAR di serie** (poco efficiente a 2-5 km, dominato dal drone COTS a bassa quota); **no SAR** (troppo pesante per T3 e comunque dominato da EGMS gratuito). GSD attesi: **RGB 2,5-19 cm, termico 0,24-2,4 m, NDVI 1,7-4,3 m** — tutti dentro i target, con il **caveat orografico** che il GSD varia ~1,5× lungo la stessa rotta (fondovalle vs crinale) e va dimensionato sul caso peggiore. Copertura **~80-120 km²/h netti** → **rivisitazione multi-giornaliera dell'area pilota (~400 km²)** e **ciclo Liguria interna (~3.050 km²) in 2-3 giorni**. Downlink **non dimensionante**: alert <0,5 Mbps, video live 5-20 Mbps entro la capacità già dimostrata in `01`. Rispetto a **Sentinel-2** il vantaggio è netto su risoluzione (40-400×) e latenza (minuti vs giorni), **ma solo per early-detection incendi ed emergenza PC**: sul wide-area lento (frane mm/anno, dNBR) **Copernicus gratuito resta dominante** e va orchestrato, non replicato. Valore vs HALE: **stesso beneficio di persistenza, GSD migliore, 1-2 ordini di grandezza meno costo/rischio, disponibile oggi**.

---

## 12. Fonti e confidence

| Elemento | Confidence | Fonte |
|---|---|---|
| Verdetto EO base (persistenza = unico differenziante; satellite domina wide-area) | alta [FATTO] | `analisi-bottom-up/02-osservazione-terra.md` §4, §7 |
| Fascia T3a/T-SORV (MTOM, endurance, payload 4-40 kg, quota, range C2) | media-alta [FATTO bracket] | `10-fasce-engineering.md` §5; `16-fasce-MALE-HALE-espanse.md` §2.1 |
| Estensione territoriale (aree SNAI Liguria 185-442 km², totale ~3.050 km², Antola-Tigullio 16 comuni) | alta [FATTO] / media [STIMA area pilota] | `Aree interne/rapporto-istruttoria_regione-liguria.md`; `02` §1 |
| Calcolo GSD/swath RGB, LWIR, multispettrale a 2/3/5 km AGL | alta [FATTO — deterministico date le assunzioni] | calcolo proprio, formule e pixel/focali dichiarati (§2) |
| Note diffrazione (resolution- vs diffraction-limited a bassa quota) | alta [FATTO — calcolo Rayleigh] | calcolo proprio (§2.2-2.3), coerente con `02` §2 |
| Specifiche sensori RGB (iXM-100 3,76 µm; α7R V 61 MP) | alta [FATTO] | Phase One (phaseone.com), Sony — datasheet vendor |
| Specifiche LWIR (640×512/1024×768, 12 µm, NEdT ≤50 mK) | alta [FATTO] | Teledyne FLIR (flir.com), Workswell (workswell.eu) — datasheet |
| Gimbal EO/IR di categoria (WESCAM MX-10/15, Star SAFIRE, Trillium HD55, Next Vision) | alta [FATTO — prodotti esistenti] | L3Harris, Teledyne FLIR, Trillium Engineering, Next Vision |
| Multispettrale (AgEagle/MicaSense Altum-PT, RedEdge-P) | alta [FATTO] | AgEagle (ageagle.com) — datasheet |
| LiDAR di categoria (RIEGL VUX/miniVUX, YellowScan) — trade | media [STIMA efficienza a 2-5 km] | RIEGL, YellowScan datasheet + scaling ingegneristico |
| Satellite: Sentinel-2 (10/20/60 m, 5 gg), VIIRS/SLSTR fire, EGMS | alta [FATTO] | Copernicus/ESA; già triangolato in `02` §Fonti |
| Copertura oraria e cicli (80-120 km²/h netti) | media [STIMA] | calcolo swath×velocità con fattori operativi dichiarati (§6.2) |
| Downlink (alert <0,5 Mbps, video 5-20 Mbps, capacità 20-100 Mbps/settore) | media-alta [FATTO capacità, STIMA flussi] | `01-connettivita.md` §4, §6; standard ISR H.265 |
| Compliance (GDPR/DPIA, cartografica, ENAC SAIL/Certified) | alta sul rischio [FATTO] | `02` §6; `16` §2.7; rimando `data-privacy-counsel`/`aviation-regulatory-counsel` |

**Limiti dichiarati:**
- Nessuna quotation vendor reale per i sensori qui citati — le specifiche sono da datasheet pubblici, i prezzi non sono trattati (rimando a `financial-cfo-analyst` per il costing payload).
- La quota operativa (2-5 km AMSL) è **assunta** dal mandato; il collega che finalizza il numero esatto potrà spostare i GSD linearmente con l'AGL (tutti i calcoli sono parametrici in h).
- L'estensione dell'area pilota Antola-Tigullio (~300-500 km²) è stima per analogia con le altre aree SNAI liguri; il perimetro esatto va estratto dal rapporto istruttoria per un dimensionamento preciso del ciclo di copertura.
- Il documento **non** ridiscute la giustificazione economica della piattaforma dedicata (ereditata da `02`, verdetto: nicchia stretta e contesa) né il nodo regolatorio/infrastruttura di lancio (ereditati da `16`): progetta il payload assumendo la piattaforma decisa a monte.
