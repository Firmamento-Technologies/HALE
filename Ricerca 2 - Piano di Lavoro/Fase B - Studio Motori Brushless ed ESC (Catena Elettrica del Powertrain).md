# Fase B — Studio Motori Brushless, ESC e Gestione Termica (Catena Elettrica del Powertrain)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Selezione e dimensionamento della **catena elettrica a valle del bus DC**: motori brushless (4 lift VTOL + 1 crociera), ESC professionali, BEC/alimentazione ausiliaria e **gestione termica**, per il powertrain **genset (ibrido-serie, config A2)** già scelto dal team |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Input** | `Trade Propulsione` (§4 dimensionamento potenze, §8 scelta A2 genset), `Bilancio di Massa ed Energia` (CFG-A, voci powertrain elettrico), concept CAD nel branch |
| **Metodo** | Ripartizione energetica/temporale della missione → due filosofie di progetto distinte (lift vs crociera) + benchmark commerciali reali + fisica delle perdite (conduzione/commutazione) + onestà tecnica sui claim di efficienza |
| **Scopo** | Rispondere ai quesiti del team: **(1)** quali motori brushless in commercio danno il miglior rapporto **efficienza/spinta** per i rotori VTOL; **(2)** dato che il VTOL (decollo/atterraggio/transizione — "opening") pesa pochissimo sulla missione, **quanto ha senso spingere la capacità di spinta**; **(3)** quali **ESC professionali** massimizzano l'efficienza (RDS(on) basso, GaN, ZVS) e **riducono il calore**; **(4)** il ruolo di BEC e alimentazioni ausiliarie |
| **Powertrain di riferimento** | **Genset (ibrido-serie, A2)** — ICE al punto ottimo → alternatore/PMSG → **bus DC 48–58 V + batteria buffer** → 1 motore crociera + 4 lift VTOL |

> ⚠️ **Onestà tecnica (coerente col Dossier di Verifica):** i numeri di spinta, g/W ed efficienza dei vendor sono quasi sempre **valori di picco/best-case** (banco, prop e tensione specifici, spesso prima del soak termico). **Nessun costruttore di ESC pubblica l'RDS(on) o una curva efficienza-vs-carico.** I dati sono raccolti da datasheet/estratti di ricerca e vanno **confermati via RFQ e banco** prima dello Studio. Dove un numero è marketing lo segnalo.

---

## 0. Executive summary — la tesi in una riga

> **La missione è ~20 h di crociera con pochi minuti di VTOL. Quindi i 4 motori lift vanno ottimizzati per SPINTA/PESO (non per efficienza), il motore di crociera e il suo ESC vanno ottimizzati per EFFICIENZA CONTINUA, e la caccia a RDS(on)/GaN/ZVS va indirizzata dove serve davvero — non nell'ESC di crociera.**

Le tre risposte ai quesiti del team:

1. **Miglior rapporto efficienza/spinta per i lift (§3):** per un 25 kg su 4 rotori il candidato "best-in-class" per **spinta-per-grammo** è il **MAD Antimatter M6C12 EEE** (~0,26 kg, ~10,8 kgf di picco); il **T-Motor U11 II** (0,77 kg, 14,2 kgf) è l'alternativa matura con più margine. L'efficienza di hover realistica è **~7–10 g/W** (non i 10–14 g/W di targa). Ma — punto chiave — **l'efficienza dei lift conta pochissimo sul bilancio di missione** (§2).

2. **Quanto spingere la spinta (§3.2):** **fino al margine di autorità di controllo (~1,7–2,0× l'hover), non oltre.** Ogni kgf di spinta in più impone un motore più pesante, e **ogni grammo di motore lift è massa morta trasportata per 20 h di crociera** → penalità di resistenza ed endurance. Sovradimensionare la spinta "per sicurezza" è controproducente su una piattaforma di endurance.

3. **ESC ad alta efficienza e meno calore (§5–§9):** a ~400 W di crociera il bus tira solo **~7–9 A** → la perdita di conduzione (I²·RDS) è di **frazioni di watt**: in crociera l'RDS(on) basso è quasi irrilevante e **domina l'efficienza del motore, non dell'ESC**. L'**RDS(on) basso e il GaN servono sugli ESC dei LIFT** (60–100 A, dove il calore del picco è il problema), non in crociera. Lo **ZVS non esiste negli ESC trifase** (sono hard-switched): va messo nel **DC-DC/BEC** e nel raddrizzatore del genset, dove è la norma. La leva reale e "bancabile" nell'ESC è la **rettificazione sincrona (active freewheeling)**.

**Debunk onesto (§6):** l'idea che "APD usi GaN" è **falsa** — gli ESC di serie APD (F/HV Pro/UHV) sono **MOSFET al silicio** con rettificazione sincrona; l'unico wide-bandgap di APD è un **progetto SiC su commessa per eVTOL (200–500 V)**, non un prodotto a catalogo. **Nessun ESC UAV di serie sul mercato usa GaN o ZVS oggi.**

---

## 1. Il quadro: dove si colloca questo studio

Il `Trade Propulsione` ha scelto l'architettura (**genset serie A2**) e dimensionato le **potenze**; il `Bilancio di Massa` ha allocato le **masse** (CFG-A). Restava aperto **quali componenti elettrici reali** mettere nella catena a valle del bus DC. Questo documento chiude quella lacuna. Non ridiscute l'architettura: la dà per assunta.

**Ancoraggi numerici ereditati (non li rifacciamo, li usiamo):**

| Grandezza | Valore | Fonte |
|---|---|---|
| Bus DC | **48–58 V** (≈12–14S) | `Trade Propulsione` §4.3 |
| Potenza **crociera** (elettrica) | **~400 W** (banda 350–500 W); albero ~300–380 W | `Trade Propulsione` §4.1 |
| Corrente bus in crociera | **~7–9 A** (400 W ÷ 55 V) | derivata |
| Picco **VTOL** (elettrico, 4 rotori) | **~4–7 kW** per **~2–4 min** | `Trade Propulsione` §4.2 |
| Hover per rotore | **25 kg / 4 = 6,25 kgf** | derivata |
| Batteria buffer | ~0,4–0,6 kWh utili, ~2,1–3,0 kg | `Trade Propulsione` §4.3, `Bilancio di Massa` CFG-A |
| Voci di massa da specificare | 4 lift+ESC+booms **3,8 kg**; crociera+ESC **0,6 kg**; BEC nell'avionica | `Bilancio di Massa` CFG-0/CFG-A |

---

## 2. Il fatto dimensionante: la ripartizione della missione

La chiave dell'intero documento — e la risposta al quesito dell'utente sul "10%".

### 2.1 Ripartizione del TEMPO

Il VTOL non è il 10% della missione: è **molto meno**. Decollo+transizione e transizione+atterraggio durano **~1–2 min per lato**; anche mettendo una riserva di hover, il totale VTOL sta **sotto i ~10 min** su una missione di 20+ h.

| Fase | Durata tipica | % del tempo di missione (20 h) |
|---|---|---|
| Decollo verticale + transizione | ~1–2 min | ~0,1–0,2% |
| Crociera (ala/box-wing) | ~20 h | **~98–99%** |
| Transizione + atterraggio verticale | ~1–2 min | ~0,1–0,2% |
| (Riserva hover/riposizionamento) | ~0–5 min | ~0–0,4% |
| **VTOL totale** | **≤ ~10 min** | **≤ ~1% (il "10%" è un tetto ampiamente prudenziale)** |

### 2.2 Ripartizione dell'ENERGIA

| Voce | Stima | Note |
|---|---|---|
| Energia di crociera | **~9,6 kWh/giorno** (banda 8,4–12) | `Bilancio di Massa` §3.1 |
| Energia VTOL | **~0,5 kWh** (≈5 kW × ~6 min) | dal buffer, poi ripristinato dal genset |
| **Quota VTOL sull'energia** | **~5%** | e per giunta **bufferata** dalla batteria |

### 2.3 La conseguenza (perché due filosofie di progetto)

Un punto percentuale di efficienza vale in modo **completamente diverso** sui due rami:

- **+1 pp sull'efficienza della catena di CROCIERA** agisce su **~9,6 kWh** → meno carico sul genset → **meno carburante** su tutte le 20 h. Un miglioramento realistico motore+ESC del **~3%** (es. 88%→91%) vale **~3% di energia di crociera**, cioè **~0,1 kg di carburante ≈ decine di minuti di endurance**. **Reale.**
- **+1 pp (o +3%) sull'efficienza dei LIFT** agisce su **~0,5 kWh** → risparmio ~0,015 kWh → **trascurabile**, e nemmeno tutto (è bufferato).

> **Regola di progetto che ne discende:**
> - **Lift → ottimizzare SPINTA/PESO e tenuta termica del picco.** L'efficienza è secondaria; la **massa** è il nemico (viaggia per 20 h).
> - **Crociera (motore + ESC + BEC) → ottimizzare l'EFFICIENZA CONTINUA.** Qui si spende in poli/laminazioni/rettificazione sincrona.

---

## 3. I motori di sollevamento (VTOL) — spinta/peso, non efficienza

### 3.1 Dimensionamento

- Hover: **6,25 kgf/rotore**. Per **autorità di controllo** (assetto in hover, raffiche in transizione) serve un picco di **~1,7–2,0× l'hover ≈ 10–13 kgf/rotore**.
- Motori la cui **spinta massima è ~6,5–7,3 kgf** (T-Motor MN6007, U8/U8 Lite) farebbero hover all'**85–95% di gas** → caldi, g/W pessimo, margine ~0. **Sono la classe di un ~16–20 kg, non di un 25 kg con margine.**
- La "classe giusta" per un quad-lift da 25 kg ha **~10–15 kgf di picco**, tipicamente **255–800 g**, 12S, prop **21–28″**.

### 3.2 Quanto spingere la spinta — la risposta diretta

> **Si dimensiona la spinta al margine di controllo (~1,8× hover), non al massimo assoluto.** Spinta extra = motore più grande = **più massa morta** che la crociera trascina per 20 h → **più resistenza indotta e parassita, meno endurance**. Su una piattaforma il cui KPI è l'endurance, sovradimensionare i lift è una **perdita netta**. Il picco serve solo a (a) sollevare con margine di assetto e (b) reggere una raffica in transizione — non a "avere tanta spinta".

Questo spiega anche perché la metrica dei lift è la **spinta-per-grammo**, non i g/W:

| Motore | Picco (kgf) | Peso (g) | **Spinta/peso (kgf/kg motore)** |
|---|---|---|---|
| MAD M6C12 EEE | ~10,8 | ~260 | **~41** ← migliore |
| MAD M10 IPE | ~16,2 | ~400+ | ~40 |
| T-Motor U11 II | ~14,2 | 772 | ~18 |
| KDE7215XF-135 | ~14,5 | ~405–460* | ~32 |

### 3.3 Tabella motori lift candidati

*Peso per motore. "g/W @ max" = spinta max ÷ potenza max = **pavimento** di efficienza (100% gas, worst-case); l'hover reale a carico moderato è **~1,6–2,2× migliore** — vedi §3.4.*

| Mfr / Modello | KV | Peso | Potenza max | Spinta max (prop / V) | g/W @ max (pavimento) | Prezzo ~USD | Idoneità 25 kg |
|---|---|---|---|---|---|---|---|
| **MAD Antimatter M6C12 EEE** | 150–400 | **255–268 g** | — | **10,8 kgf** / 6–12S | — | ~130–170 | ✅ **miglior spinta/peso** |
| **T-Motor U11 II** | 120 | 772 g | 2783 W | **14,16 kgf** / 26″ / 12S | ~5,1 | ~260–320 | ✅ maturo, gran margine |
| **KDE7215XF-135** | 135 | ~405–460 g* | 4405 W (58,8 V, 85 A) | **14,5 kgf** / 27,5″ dual / 14S | ~3,3 | **440** | ✅ premium heavy-lift, >93% η motore |
| **MAD M10 IPE** | 100–180 | ~400+ g | 3422 W | **16,2 kgf** | ~4,7 | ~200+ | ✅ margine ampio |
| **MAD V8010 EEE** | 120/150 | — | — | 12,6–14 kgf / 12S | — | ~180+ | ✅ candidato solido |
| T-Motor MN6007 II | 160/320 | ~155–161 g | 1120 W | 6,5 kgf / 22″ / 12S | ~5,8 | ~60–75 | ⚠️ **sotto-dimensionato** |
| T-Motor U8 II | 85–190 | 277 g | 1200 W | 7,3 kgf / ~28″ / 12S | ~6,1 | ~180–210 | ⚠️ marginale |

*KDE non pubblica un peso singolo chiaro: ~405–460 g **da confermare** sul datasheet prestazionale.

**Shortlist lift:** **(1) MAD M6C12 EEE** (spinta/peso), **(2) T-Motor U11 II** (maturità + ecosistema ESC), **(3) KDE7215XF-135** (qualità/supporto, se il budget lo consente).

### 3.4 Efficienza (g/W) — banda realistica

| Regime | g/W tipico | Note |
|---|---|---|
| Leggero (25–40% gas, prop grande) | **10–14** | il numero "di targa" dei vendor |
| Hover su motore ben-margine (~50–65%) | **7–10** | **il punto realistico del nostro VTOL** |
| Hover su motore sotto-dimensionato (80–95%) | **4–6** | dove starebbero MN6007/U8 a 25 kg |
| Spinta max (100%) | **3–6** | la colonna "pavimento" §3.3 |

Regola: massimizzare i g/W di hover ⇒ **prop più grande possibile, KV/tensione più bassi** che tengano il motore nel 50–65%. **Ma** (vedi §2) questo conta poco sul bilancio: non si sacrifica massa per inseguire i g/W dei lift.

> ⚠️ **Qualità del dato:** spinta max e "efficienza" sono di picco (banco, burst, pre-soak). La spinta sostenuta reale è tipicamente **10–20% sotto** il max di targa. Il **g/W @ max** è il pavimento, **non** il numero di hover: per l'energetica usare la banda 7–10 g/W. I datasheet PDF (KDE/T-Motor/MAD pubblicano tabelle complete spinta/corrente/potenza/g-W per prop+V) e il **database indipendente Tyto Robotics** vanno consultati prima di congelare il progetto.

---

## 4. Il motore di crociera — efficienza continua

Gira **il 100% della missione** → la sua efficienza si moltiplica per 20 h. **Qui si investe.**

### 4.1 Perché un motore di crociera è "efficiency-optimized" (vs un lift "thrust-optimized")

| Leva | Motore crociera (efficienza) | Motore lift (spinta) |
|---|---|---|
| **KV** | **basso** → più coppia/A → meno corrente → meno I²R | alto per RPM/densità |
| **Numero poli** | **alto** → meno flusso/polo, meno perdite nel ferro | moderato |
| **Statore** | **grande diametro (pancake)** → coppia a bassa corrente, buona dissipazione | piccolo/denso per peso |
| **Laminazioni** | **sottili (0,20–0,35 mm)** → meno correnti parassite/isteresi (perdita che domina in continuo) | più spesse OK (burst brevi) |
| **Riempimento rame** | **alto slot fill** → bassa resistenza avvolgimento | densità di corrente da burst |
| **Punto di lavoro** | dimensionato perché **la crociera cada sul picco della curva η** | dimensionato perché il picco di spinta sia raggiungibile |
| **Perdita nemica** | **ferro** (continua, ∝ frequenza/flusso) | **I²R / limite termico** (burst) |

**La fisica in una riga:** un lift sta secondi ad alta spinta → tollera perdite nel ferro. Un motore di crociera sta **~72.000 secondi** su un punto → ogni frazione di percento di perdita è moltiplicata per 20 h → deve stare **sul picco della curva di efficienza**.

### 4.2 Tabella motori di crociera candidati

| Marca / Modello | KV | Peso | η di picco (claim vendor) | Potenza continua | Cel. | Prezzo ~USD | Note |
|---|---|---|---|---|---|---|---|
| **Scorpion HKIV-40** | 400–520 (e più bassi) | ~280–340 g | **>90% (vendor)** | ~400–1500 W | ≤12S | ~150–250 | Elica/UAV, avvolgimento single-strand, efficiency-tuned. **Candidato forte diretto.** |
| **Plettenberg (Orbit / HP-220/30)** | basso, custom | ~200–500 g | **~90–93%** | 300–1000 W | ≤14S+ | $$$ (quote) | Inrunner di precisione, **ottimo match a 14S**, alta η ad alta tensione |
| **Neu Motors (1509/1521 + riduttore)** | custom basso | ~200–400 g | **~91–93% (misurata)** | 300–1000+ W | flessibile | 300–600+ | **Massima efficienza**, inrunner + planetario; peggiore integrazione/costo |
| **T-Motor MN605-S / MN701-S** | 170–320 | 230–480 g | ~88–90% (inferita) | 300–800 W | ≤12S | ~150–350 | Buon match 12S, direct-drive |
| **KDE 3510XF/4213XF** | 187–515 | 100–300 g | tabelle g/W (η% non pubbl.) | 250–800 W | ≤12S | ~80–200 | Multirotor-optimized, datasheet per prop |
| T-Motor Antigravity **MN5006** | 300/450 | **108 g** | ~85–88% (inferita) | 500 W picco | **4–6S** | ~100–130 | ⚠️ **6S: NON gira a 48–58 V** — non progettare il bus attorno a questo |

**Letture:**
- **Non progettare un bus 14S attorno all'MN5006** (6S). Per **400 W a 48–58 V** la shortlist è **Plettenberg/Neu (inrunner + riduttore)** per la massima η, oppure **Scorpion HKIV / grande T-Motor MN** (outrunner basso-KV) per la semplicità direct-drive.
- **Assunzione di progetto: ~89–91% di η motore al punto di crociera** (non il picco di targa). Il "meglio in classe" ~92–93% richiede inrunner+riduttore o motori Halbach (Launchpoint, solo OEM).

---

## 5. Gli ESC professionali — dove l'efficienza conta e dove no

**Framing dalle correnti:** crociera **~7–9 A** (qualsiasi ESC 40–120 A è "a vuoto" → I²R trascurabile, domina il motore) vs lift **~60–100 A** (dove il **calore del picco** è il problema termico). Quindi **due ESC con criteri opposti**, come i motori.

### 5.1 Tabella ESC professionali

*Nessun vendor pubblica RDS(on) o curve η. **Nessun prodotto di serie qui usa GaN**: sono tutti MOSFET Si, hard-switched. L'efficienza viene da (1) Si a basso RDS(on), (2) **rettificazione sincrona / active freewheeling**, (3) progetto termico.*

| Marca / Serie | Cont./picco A | Cel. (V) | Peso | Tecnologia stadio di potenza (verificato vs claim) |
|---|---|---|---|---|
| **T-Motor ALPHA 60/80/120A HV** | 60–120 | ≤**14S** | ~85–170 g | Si MOSFET, **sine/FOC** → più liscio e freddo a carico parziale. **La linea T-Motor giusta per la crociera.** |
| **T-Motor FLAME 60/80/100/180A HV** | 60–180 | ≤12S | 73,5–210 g | Si MOSFET, **onda quadra (trapezoidale)**, ~600 Hz refresh, no BEC. Robusto, non sine. |
| **KDE UAS (KDEXF-UAS35…125)** | 35–125 | ≤12S | ~30–140 g | Si MOSFET, opto-isolato, **rettificazione sincrona a controllo di temperatura + active freewheeling** (feature reale, utile a carico parziale) |
| **APD F-series (80/120/200F3)** | 80–200 | ≤14S | ~10–36 g | **Si MOSFET (NON GaN)**, MCU 32-bit, dithering PWM, **APCD** + rettificazione sincrona, BLHeli_32/DShot |
| **APD HV Pro / UHV** | fino ~45 kW | ≤**28S** | HV Pro ~227 g | **Si MOSFET**, FW 180 MHz custom, **rettificazione sincrona dinamica + APCD** |
| **Currawong Velocity (XS/HC/HS)** | ~80–300+ | ≤18S / 75 V | XS **75 g** | Si MOSFET low-impedance, **rettificazione sincrona**, CAN, aero-Al, HW interlock. Adottato da AeroVironment. |
| **Hobbywing XRotor Pro H80A (BLDC/FOC)** | 40/80 | 6–14S | 87 g | Si MOSFET, sine o quadra, "DEO" (label proprietaria) |
| **mGm COMPRO (TMM/HBC)** | decine–centinaia | fino a HV | variabile | Si MOSFET (IGBT nei più grandi), **PWM sincrona + rigenerativo**; "98–99%" è **best-case marketing** |

### 5.2 Letture

- **ESC di crociera → sine/FOC right-sized.** A ~7 A un **T-Motor ALPHA HV / Currawong Velocity / KDE UAS** (sine + rettificazione sincrona) batte un FLAME a onda quadra: il drive sinusoidale riduce le armoniche → **meno perdite nel ferro del motore** e meno calore dell'ESC a carico parziale (conta **più per il motore che per l'ESC**).
- **Non sovradimensionare la corrente in crociera:** un ESC da 120 A a 7 A può essere **meno** efficiente di uno da 40–60 A ben dimensionato, perché l'overhead fisso (gate drive, MCU, condensatori) pesa di più a carico leggero. L'efficienza è una **curva vs carico** e la crociera sta all'estremo basso.
- **ESC dei lift → corrente/termico.** Qui contano **RDS(on) basso** e **progetto termico** per sopravvivere ai 60–100 A del burst; l'efficienza di picco è secondaria (dura minuti).
- **La rettificazione sincrona (active freewheeling) è l'unica feature ESC davvero rilevante per l'efficienza** ed è reale in **KDE, APD, Currawong, mGm**: sostituisce la conduzione del diodo di corpo (lossy) con il canale a basso RDS(on).

---

## 6. MOSFET / RDS(on) / GaN — onestà tecnica

### 6.1 Perdita di conduzione e RDS(on)
Per MOSFET: **P_cond ≈ I_rms² × RDS(on) × D**.
- **Crociera (7 A, FET 1 mΩ):** P_cond ≈ 7² × 0,001 ≈ **0,05 W/FET** → **trascurabile**. Inseguire FET esotici per l'ESC di crociera è **fatica sprecata**.
- **Lift (60–100 A):** I²R scala col quadrato → qui **RDS(on) basso è decisivo** (sopravvivenza termica del burst). **È lì che vanno i MOSFET a bassissimo RDS(on).**

### 6.2 Perdita di commutazione e GaN
Per fronte: **P_sw ≈ ½·V_bus·I·(t_r+t_f)·f_sw** + recupero inverso **≈ Q_rr·V_bus·f_sw**. Il **GaN** ha **Q_rr ≈ 0**, basso gate charge, fronti veloci → taglia commutazione + recupero inverso e consente **>100 kHz** con meno calore. **Ma** P_sw ∝ corrente e tensione: **il vantaggio GaN è sui rami di alta potenza (lift), non su un inverter di crociera a 7 A.**

### 6.3 Debunk onesto
- **Nessun ESC UAV di serie usa GaN** (né SiC) nei prodotti a catalogo di APD, Hobbywing, Currawong, mGm, KDE, T-Motor.
- **APD ≠ GaN:** F/HV Pro/UHV sono **MOSFET Si** con rettificazione sincrona. L'unico wide-bandgap di APD è un **progetto SiC su commessa per eVTOL (200–500 V, >50 kW, 60 W/g)** — bespoke, non a catalogo. Da qui la confusione "APD 500 / GaN".
- **Dove va l'RDS(on) basso:** **sugli ESC dei lift** (calore del picco). In crociera non muove l'ago.

---

## 7. Zero-Voltage Switching (ZVS) e soft-switching — dove serve davvero

### 7.1 Cos'è
**ZVS:** accendere il MOSFET quando la sua V_DS è ≈0 (risuonando la Coss e lasciando che il diodo di corpo clampi a zero) → elimina la perdita capacitiva di accensione (½·Coss·V²·f) e lo spike di sovrapposizione. Recupera energia invece di dissiparla → **meno calore** e permette **frequenze più alte** (magnetici e condensatori più piccoli), oltre a ridurre l'EMI.

### 7.2 Dove vive davvero (conversione DC-DC / DC-AC, non motor drive)
- **LLC risonante** (mezzo/pieno ponte) — il cavallo di battaglia.
- **Phase-Shifted Full-Bridge (PSFB)** — ZVS usando l'induttanza di dispersione per scaricare la Coss.
- Alcuni inverter/convertitori GaN ad alta frequenza.

### 7.3 La parte onesta: gli ESC dei droni NON fanno ZVS
- Un ESC BLDC/PMSM trifase è un **inverter a sorgente di tensione (VSI) a due livelli, hard-switched**: nessun serbatoio risonante, i FET commutano contro l'intera tensione di bus → **hard-switching per costruzione** (sia trapezoidale sia FOC/sine). **Nessuno ZVS nativo.**
- Gli inverter soft-switched **esistono** (**ARCP** — Auxiliary Resonant Commutated Pole) ma per un UAV sono **impraticabili**: aggiungono per-ramo induttore + condensatori + interruttori ausiliari + controllo dipendente dalla corrente → **massa, volume, complessità, fragilità** che superano il beneficio.
- Ciò che i migliori ESC fanno **al posto** dello ZVS: **rettificazione sincrona/active freewheeling** (complementary PWM), **dead-time ottimizzato**, tuning del gate-drive, **GaN** (Q_rr≈0). Tagliano la conduzione del diodo di corpo e il recupero inverso — **ma non sono ZVS**; l'accensione/spegnimento del FET principale resta hard.

> **Verdetto:** per un ESC UAV **inseguire lo ZVS è la leva sbagliata**. Lo ZVS va messo **dove è già la norma**: nei **DC-DC/BEC** (58 V→12 V con LLC/PSFB, §8) e nell'**elettronica di raddrizzamento/carica del genset**. Nell'ESC le leve vere sono RDS(on) basso (sui lift) + rettificazione sincrona + dead-time + progetto termico.

---

## 8. BEC / alimentazione ausiliaria — 58 V→5 V è il vero problema di efficienza

Il velivolo deve alimentare **avionica (5 V/12 V), servi (molti, transitori forti), gimbal/payload, datalink**, scendendo da un bus **48–58 V**. Qui — non nell'ESC — l'efficienza di conversione è **realmente difficile**.

### 8.1 Perché 58 V→5 V è duro (fisica)
- **Duty estremo:** D ≈ V_out/V_in ≈ 5/58 ≈ **8,6%**. L'high-side conduce ~9%, il **low-side conduce ~91%** del periodo → il low-side domina le perdite.
- **Buck a diodo (non sincrono) è brutale qui:** uno Schottky di ricircolo cade ~0,35–0,4 V per il **91%** del ciclo → contro 5 V d'uscita, **~8% di efficienza persa** solo lì.
- **Perdita di commutazione ∝ V_in:** a 58 V ogni fronte dissipa molto, e i FET HV hanno più gate charge/Coss → f limitata.
- **Soluzione pratica: due stadi.** 58 V→**~12 V** intermedio, poi 12 V→5 V POL. Ogni convertitore lavora a duty sano. (È perché i moduli industriali regolano a 12 V, non a 5 V.)

### 8.2 Perché il buck a rettificazione sincrona ≫ buck a diodo
Sostituisce il **diodo** low-side con un **MOSFET a basso RDS(on)** pilotato in complementare: la caduta ~0,35–0,4 V diventa I·RDS ≈ **0,05–0,1 V** → conduzione low-side ridotta di più volte. **Il beneficio è massimo proprio ad alto rapporto di step-down/basso duty (il nostro caso).** Costo: gestire il **dead-time** (no shoot-through). **È la singola leva di efficienza più grande sulle alimentazioni.**

### 8.3 Tabella BEC / DC-DC candidati

| Prodotto | Ingresso | Uscita | Cont./picco | Sincrono? | Peso | Note |
|---|---|---|---|---|---|---|
| **Mauch 090 HYB-BEC 12 V** | 4–14S, **60 V max** | 12,0 V | 3 A | buck + LDO post-reg | ~16 g | Uscita pulitissima (avionica), bassa corrente |
| **Mauch 021/084 HYB-BEC 5,3 V** | 4–14S, 60 V | 5,3 V | ~3 A | buck + LDO | ~16 g | Rail avionica |
| **Mauch Power-Cube HV** | 4–14S | 2–3× 5,3 V + 12 V | 10 A tot | buck + LDO, **ridondante** | — | **Dual-BEC** per Cube/Pixhawk |
| **Castle CC BEC 2.0** | **2–14S, 6–58,8 V** | 4,75–12 V | 10 A / **15 A picco** | buck sincrono | brick | ⚠️ **soffitto 58,8 V = zero margine a 58 V** |
| **CUAV HV PM** | 3–14S, **10–60 V** | 5,3 V | 3 A (+ sensing) | buck | — | Modulo di potenza (avionica + telemetria) |
| **Vicor DCM (V48C12C150BL)** | **40–60 V** | 12 V | 150–240 W | soft-switched HF | — | ~**93% pubblicato**, densità altissima. **Tier certificabile.** |
| **RECOM RMD** | 14,4–170 V | 24/36/48 V | 40–500 W | sì | — | **EN 50155 ferroviario** (argomento di power-quality) |
| **TRACO (isolati)** | 6–160 V | vari | fino a centinaia W | sì | — | OVP/OCP/OTP, wide-temp, isolati |

### 8.4 Regole di progetto BEC
1. **Rettificazione sincrona obbligatoria** (§8.2).
2. **Due stadi** 58→12→5 (§8.1).
3. **BEC dedicato per i servi** (10–15 A, es. Castle CC BEC 2.0 o rail Vicor/RECOM) con bulk-cap vicino, **separato** dal rail avionica pulito (Mauch/LDO). I gimbal/payload spesso un terzo rail. Contiene il guasto: un corto sul rail servi non fa il brown-out del flight controller.
4. **BEC ridondante/dual** con ORing: un BEC che cade **spegne silenziosamente il FC** → single point of failure inaccettabile su velivolo certificabile (Cube/Pixhawk espongono Power1/Power2 apposta).
5. **Margine di tensione:** il soffitto **58,8 V (14S)** di Castle & simili è **a filo** col bus a 58 V → specificare ingressi **≥60 V (idealmente ≥75 V)**, cioè il tier Vicor/RECOM o il bus intermedio 12 V. **I vendor hobby non pubblicano curve η → misurare a banco.**

---

## 9. Gestione termica — ridurre il calore (la richiesta dell'utente)

Le fonti di calore e la loro leva, **ordinate per efficacia reale**:

| Fonte di calore | Quando | Leva primaria | Note |
|---|---|---|---|
| **ESC lift** (60–100 A) | burst VTOL **2–4 min** | **RDS(on) basso + massa termica/heatsink + flusso d'aria del rotore** | È il picco termico più duro; sfrutta il transitorio (2–4 min → massa termica assorbe) |
| **Motori lift** (rame/ferro) | burst VTOL | statore grande + prop grande (meno gas) | secondario sull'energia, primario sul termico del burst |
| **Catena crociera** (motore+ESC) | **continuo 20 h** | **η motore + sine/FOC + rettificazione sincrona + right-sizing ESC** | basso in assoluto (~7–9 A) ma continuo → progetto per il regime, non per il picco |
| **BEC** (58→5 V) | continuo | **rettificazione sincrona + due stadi** | §8; il diodo è il nemico |
| **Raddrizzatore/carica genset** | continuo | **ZVS/soft-switching (LLC/PSFB)** | §7: **qui** lo ZVS paga |

**Principi:**
- **Il calore si riduce prima non generandolo:** right-sizing (niente ESC da 120 A per 7 A), sine vs trapezoidale a carico parziale, rettificazione sincrona ovunque (ESC e BEC).
- **Poi smaltendolo:** percorso termico (pad/heatsink verso struttura), **aria del rotore sugli ESC lift** durante il burst, aria di crociera costante sull'ESC di crociera. Il potting migliora la conduzione ma alza la massa termica: **valutarlo solo sugli ESC lift** (burst) dove aiuta ad assorbire il transitorio.
- **Lo ZVS** riduce calore **solo dove è applicabile** (DC-DC/BEC/genset), **non** nell'ESC.

---

## 10. Raccomandazione sintetica (shortlist)

| Blocco | Scelta primaria | Alternativa | Criterio |
|---|---|---|---|
| **4 motori lift** | **MAD M6C12 EEE** (spinta/peso) | T-Motor U11 II (maturità); KDE7215XF (premium) | spinta/peso + margine ~1,8× hover, **non oltre** |
| **ESC lift** | **APD F/HV** o **KDE UAS** (RDS(on) basso + rettificazione sincrona) | Currawong Velocity | **termico del burst**, non η di picco |
| **1 motore crociera** | **Scorpion HKIV basso-KV** (direct-drive) o **Plettenberg/Neu** (inrunner+riduttore, max η) | grande T-Motor MN basso-KV | **η al punto di crociera ~89–91%** |
| **ESC crociera** | **T-Motor ALPHA HV** (sine/FOC) | Currawong Velocity / KDE UAS | **sine + right-sized** (~40–60 A, non 120) + rettificazione sincrona |
| **BEC** | **buck sincrono a due stadi, dual ridondante**, rail servi dedicato | Vicor/RECOM per il tier certificabile | 58→12→5, ingresso ≥60 V |
| **ZVS/soft-switching** | **solo nel DC-DC/BEC e nel raddrizzatore genset** | — | non nell'ESC (hard-switched) |

---

## 11. Impatto sul bilancio di massa (aggancio a CFG-A, senza modificarlo)

Questo documento **non cambia i totali** del `Bilancio di Massa`: **specifica** cosa c'è dentro le voci già allocate.

| Voce CFG-A esistente | Massa allocata | Cosa specifica questo studio |
|---|---|---|
| 4 lift + ESC + booms | 3,8 kg | 4× (motore ~0,26–0,77 kg + ESC lift ~0,01–0,04 kg) + booms + supporti |
| Motore crociera + ESC | 0,6 kg | motore ~0,2–0,5 kg + ESC crociera sine ~0,07–0,15 kg |
| Avionica certificabile | 1,3 kg | include i **BEC dual + rail servi** (parte della distribuzione di potenza) |

> Le scelte qui (motori leggeri per i lift, ESC right-sized, niente GaN inutile in crociera) **aiutano a stare** dentro CFG-A; nessuna spinge oltre le allocazioni.

---

## 12. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| η reale della catena elettrica sul **nostro** punto (crociera 400 W) | Banco: misurare η motore+ESC a ~7 A e la curva η-vs-carico |
| RDS(on) e curve η degli ESC (non pubblicate) | RFQ datasheet + misura a banco (crociera **e** burst lift) |
| Spinta/g-W reali dei lift (targa = picco) | Datasheet prestazionali per prop+V + cross-check **Tyto Robotics** |
| Termico del burst ESC lift (2–4 min) | Prova termica del burst con massa termica/flusso reale |
| Curve η dei BEC (vendor hobby non pubblicano) | Banco 58→12→5; verificare margine di tensione ≥60 V |
| Scelta direct-drive vs inrunner+riduttore per la crociera | Trade dedicato η-vs-integrazione in Fase C |

---

## 13. Fonti

> ⚠️ **Qualità del dato:** molte specifiche sono di picco/marketing; parecchi domini vendor hanno bloccato il fetch automatico → numeri da estratti di ricerca/datasheet, **da confermare su datasheet primario/RFQ**. **Nessun vendor pubblica RDS(on) o curve η**; **nessun ESC UAV di serie usa GaN/ZVS**.

**Motori lift (VTOL):**
- T-Motor U11 II: https://store.tmotor.com/product/u11-v2-motor-u-power.html · U8 II: https://store.tmotor.com/product/u8-v2-u-efficiency-kv190.html · MN6007 II: https://uav-en.tmotor.com/2020/Antigravity_1211/384.html
- KDE7215XF-135: https://www.kdedirect.com/products/kde7215xf-135 · datasheet: https://www.verical.com/datasheet/kde-direct-brushless-dc-motors-kde7215xf-135-3236774.pdf · collection UAS: https://www.kdedirect.com/collections/uas-multi-rotor-brushless-motors
- MAD M6C12 EEE: https://mad-motor.com/products/mad-components-m6c12-eee-industrial-drone-motor · M10 IPE: https://rcdrone.top/products/mad-m10-ipe-brushless-drone-motor · V8010 EEE: https://mad-motor.com/products/mad-components-v8010-eee
- Tyto Robotics (test indipendenti): https://database.tytorobotics.com/ · metodo g/W: https://www.tytorobotics.com/blogs/articles/how-to-measure-brushless-motor-and-propeller-efficiency

**Motori crociera (efficienza):**
- Scorpion outrunner/η: https://www.scorpionsystem.com/info/brushless_outrunner_motors/ · HK-4540-400 (>90%): https://www.scorpionsystem.com/catalog/helicopter/motors_4/hk-45_1/hk-4540_400_8/
- T-Motor Antigravity MN5006 (6S): https://store.tmotor.com/product/mn5006-kv300-motor-antigravity-type.html · https://www.getfpv.com/t-motor-antigravity-mn5006-motor.html
- Overview costruttori (Plettenberg/Neu/Launchpoint): https://www.unmannedsystemstechnology.com/expo/drone-motors/

**ESC professionali:**
- T-Motor FLAME 60A 12S V2: https://store.tmotor.com/product/flame-60a-12s-V2-esc.html · serie FLAME: https://uav-en.tmotor.com/Multirotor/ESC/flame/
- KDE UAS (rettificazione sincrona): https://www.kdedirect.com/products/kdexf-uas55 · basi ESC/UBEC: https://www.kdedirect.com/blogs/news/esc-and-ubec-basics
- APD F-series: https://docs.powerdrives.net/products/f_series · HV Pro: https://docs.powerdrives.net/products/hv_pro · UHV: https://docs.powerdrives.net/products/uhv · **SiC custom (debunk GaN)**: https://powerdrives.net/projects/silicon-carbide-controller
- Currawong Velocity: https://www.currawongeng.com/velocity-esc/ · XS: https://www.unmannedsystemstechnology.com/company/currawong-engineering/currawong-velocity-xs-electronic-speed-controller-esc/ · selezione AeroVironment: https://www.suasnews.com/2023/07/aerovironment-selects-currawong-velocity-esc/
- Hobbywing XRotor Pro H80A: https://www.hobbywing.com/en/products/xrotorh80a14sbldc · FOC: https://www.hobbywingdirect.com/products/eps-esc-foc-h80
- mGm COMPRO HBC: https://www.mgm-compro.com/brushless-motor-controllers/ · HBC 50063: https://pdf.aeroexpo.online/pdf/mgm-compro/31-kw-motor-controller-hbc-50063/171210-21285.html

**BEC / DC-DC:**
- Mauch HYB-BEC 12V: https://mauch-electronic.com/products/090-4-14s-hyb-bec-12-0v · 5,3V: https://mauch-electronic.com/products/021-pl-4-14s-hyb-bec-1x-5-3v · ArduPilot: https://ardupilot.org/copter/docs/common-mauch-power-modules.html
- Castle CC BEC 2.0 (14S/58,8V): https://www.castlecreations.com/en/cc-bec-2-0-010-0154-00
- CUAV HV PM (10–60V): https://ardupilot.org/copter/docs/common-hv-pm.html
- Vicor DCM (40–60V, ~93%): https://www.vicorpower.com/dc-dc/non-isolated-regulated/dcm · RECOM ferroviario: https://recom-power.com/en/railway.html · TRACO: https://www.tracopower.com/dc-dc-converters
- Rohm — efficienza buck (sincrono vs diodo, alto step-down): https://fscdn.rohm.com/en/products/databook/applinote/ic/power/switching_regulator/buck_converter_efficiency_app-e.pdf

**MOSFET / RDS(on) / GaN / ZVS / soft-switching:**
- Calcolo perdite MOSFET BLDC/PMSM (P_cond=I²·Rds·D): https://calcengines.com/mosfet-loss-calculator-bldc-pmsm/ · selezione MOSFET BLDC: https://www.enrgtech.co.uk/blog/bldc-motors-power-loss-and-optimized-mosfet-selection/
- EPC — eGaN nei motor drive (>100 kHz): https://www.ednasia.com/epc-egan-fets-enhance-drive-performance-of-low-cost-motors/ · GaN drive UAV: https://eepower.com/technical-articles/wide-bandgap-advancements-in-gan-motor-drive-inverters-revolutionize-uav-drones-for-agricultural-applications/
- TI SLUA159 — ZVS resonant conversion: https://www.ti.com/lit/an/slua159/slua159.pdf · TI SLUA560 — PSFB ZVS+SR: https://www.ti.com/lit/slua560 · Infineon LLC (ZVS/ZCS): https://www.infineon.com/products/power/ac-dc-power-conversion/ac-dc-pwm-pfc-controller/llc-resonant-mode-controller
- ARCP per BLDC (accademico): https://www.sciencedirect.com/science/article/pii/S2352484722016407 · Resonant drive aeronautico (NASA NTRS): https://ntrs.nasa.gov/api/citations/20250002679/downloads/ITEC_Resonant_Algorithms_Paper_Final.pdf · IEEE — ridurre switching loss via body-diode: https://ieeexplore.ieee.org/document/6647273/

---

*Analisi first-order stage-appropriate per la fattibilità. Spinte, g/W ed efficienze sono bande di targa/parametriche, da raffinare con banco, RFQ e prova termica. Conclusione: **lift ottimizzati per spinta/peso (margine ~1,8× hover, non oltre); crociera+ESC ottimizzati per efficienza continua (sine/FOC, right-sized, rettificazione sincrona); RDS(on) basso e GaN sui rami lift ad alta corrente; ZVS/soft-switching nel DC-DC/BEC e nel genset, non nell'ESC; BEC sincrono a due stadi, dual-ridondante, con rail servi dedicato.***
