# Fase B — Avionica ed Elettronica di Bordo (studio tecnico)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio tecnico dell'elettronica di bordo (non-payload, non-telemetria) del velivolo: flight controller, GNSS/RTK, sensori aggiuntivi, elettronica di potenza dei motori, I/O — con vincolo di **certificabilità ENAC/EASA** |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Perimetro** | **Solo** l'avionica/elettronica di bordo che **non** è payload (→ `Componenti di Payload per Applicazione`) né telemetria/link/GCS (→ `Telemetria, Data Link e Stazione di Terra`). |
| **Impostazione** | **Tecnica prima di tutto:** si sceglie il componente per funzione e certificabilità; **i consumi sono trattati come conseguenza** della scelta (non come driver). Il **budget cap** è considerato ovunque. |
| **Contesto di sistema** | Powertrain **genset (ibrido-serie A2)**: 4 motori lift elettrici + 1 motore elettrico di crociera, alimentati da bus DC (alternatore + batteria buffer); motore termico a regime ottimale (`Trade Propulsione` §8). Baseline di massa: avionica certificabile ~1,0–1,6 kg (`Bilancio di Massa` §2.3). |

> ⚠️ **Onestà tecnica (coerente col Dossier di Verifica):** prodotti e prezzi sono **indicativi** e in gran parte **quote-based** (listini non pubblici per l'avionica certificabile). I claim di certificazione (DO-178C/DO-254/DO-160G, DAL) vanno **verificati sul data-package del fornitore** prima di fondarci la safety-case. Fonti in §9.

---

## 0. Executive summary

1. **"Certificabile" ha un significato preciso:** il fornitore deve consegnare un **pacchetto di certificazione** — **DO-178C** (software), **DO-254** (hardware complesso), **DO-160G** (ambientale) a un **DAL** (Design Assurance Level) dichiarato. **ArduPilot/PX4 non hanno DAL né pacchetto** → sono **solo da dimostratore**. Questo è il discrimine dell'intero documento (e il motivo per cui stimare l'avionica con elettronica hobbistica falserebbe peso, costo e certificabilità — `Bilancio di Massa` §4).
2. **Flight controller — baseline raccomandata: Embention Veronte 1x** (OEM 🇪🇸, DO-178C/DO-254 **DAL B**, ~198 g, ridondanza interna IMU/GNSS/baro, supporto transizione VTOL+ala fissa). Alternativa: **uAvionix George** (derivato dal Cube, HW **DO-254 DAL-C** + SW **DO-178C** via Hionos 🇫🇷). **Cube Orange+/Pixhawk + ArduPilot/PX4 solo per il dimostratore**, non nella base di certificazione. **Veronte 4x** (fail-operational) solo se richiesto "continua-dopo-il-guasto".
3. **GNSS + RTK — l'RTK NON serve per navigare** (in rotta basta **GNSS + SBAS/EGNOS**, che dà anche l'**integrità**). L'RTK (cm) serve **solo** per: **atterraggio di precisione shipborne** (in modalità **moving-base**, base sulla nave), e **payload georeferenziati** (LiDAR/fotogrammetria — dove va bene anche il **PPK** in post-processing). Prioritaria la **resilienza jam/spoofing** (Septentrio **AIM+/OSNMA** o NovAtel **GRIT**), ormai attesa nella safety-case.
4. **Altimetro AGL distanziometrico — sì, è necessario** per lo scenario "decollo in avvallamento → salita": il barometrico è riferito alla quota di decollo, la **distanza reale dal suolo** la danno **radar/LiDAR**. Baseline: **radar altimeter Ainstein US-D1** (all-weather, sopra acqua/nave) come primario + **LiDAR LightWare** per il flare su superficie dura; **baro + database del terreno (SRTM/DTED)** in rotta.
5. **Sensori carburante (non critici, niente certificazione):** **sonda di livello capacitiva** (ottimale: stato solido, insensibile all'assetto/sloshing) + **portata dedotta dall'ECU EFI** → fusione dei due per la miglior stima di autonomia/riserva.
6. **Elettronica di potenza dei 4 lift — valutata la "board unica a 4 inverter": sconsigliata.** Per un VTOL con motori all'estremità dei booms conviene **4 ESC separati (HV, con telemetria CAN) + power-distribution board**, non un 4-in-1 (che è un **single point of failure** e allunga i cablaggi di potenza). I/O insufficienti del FC → **nodi CAN (DroneCAN)**, restando **nell'ecosistema del fornitore certificato**.
7. **Consumi (conseguenza delle scelte):** l'avionica "core" (FC + GNSS + altimetri + sensori + nodi) sta in **~15–30 W**, dentro la voce "avionica/payload ~45 W" del `Trade Study`. Dettaglio in §7.

---

## 1. Cosa vuol dire "certificabile" (e perché esclude ArduPilot)

Per ENAC/EASA un componente è **davvero certificabile** solo se il fornitore fornisce le **evidenze di assurance**:

| Standard | Copre | Cosa serve |
|---|---|---|
| **DO-178C** (ED-12C) | Software | Sviluppato a un **DAL** (A/B/C/D) con tracciabilità requisiti→codice→test |
| **DO-254** (ED-80) | Hardware complesso (FPGA/ASIC/PCBA) | Assurance di progetto hardware al DAL |
| **DO-160G** | Ambiente | Prove EMC, vibrazioni, temperatura, potenza |

- **ArduPilot / PX4** (su Cube Orange+, Pixhawk 6X, Auterion Skynode): **nessun DAL, nessun pacchetto**. Ridondanza hardware reale (utile), ma il **software non può formare la base di certificazione EASA**. → **Ottimi per il dimostratore/collaudo, non per il prodotto certificato.**
- Nel SORA questo tocca gli **OSO di progetto/produzione** (OSO#01–#05, #24) e l'**OSO#06 sul C2**: al salire del SAIL (III+), l'ENAC chiede prove di robustezza di progetto **vicine a quelle di un aeromobile** (`Guida ENAC-SORA` §7–§8).

> **Percorso pratico:** volare il **dimostratore su Cube+PX4** (rapido, economico), ma impostare la **base di certificazione su un autopilota con pacchetto DAL** (Veronte/George). Il George nasce proprio come "un Cube reso certificabile" → migrazione naturale dal dimostratore.

---

## 2. Flight controller / autopilota

### 2.1 Opzioni certificabili (il fornitore consegna il DAL)

| Prodotto | Peso | Certificazione | Interfacce | Prezzo indic. | Note / EU |
|---|---|---|---|---|---|
| **Embention Veronte 1x** ★ baseline | ~198 g | **DO-178C + DO-254 DAL B** (DAL A in corso), DO-160G, MIL-STD-810; MoC per SORA/SAIL I–V | CAN (ecosistema Veronte), seriale, PWM, DroneCAN via nodi | ~€10–20k+ (quote) | **OEM 🇪🇸** — opzione sovrana UE più forte |
| **uAvionix George (G2/G3)** ★ alternativa | ~80 g | HW **DO-254 DAL-C** + DO-160G + MIL-STD-810H; SW **DO-178C** via **Hionos 🇫🇷** | Ecosistema Cube: PWM, CAN/DroneCAN, seriale | 4 cifre basse-medie USD (quote) | Baro **TSO-C88b**; GPS **truFYX TSO**; "il più economico certificabile" |
| **Embention Veronte 4x** | maggiore | DO-178C/DO-254 DAL B; **3(+1) core, arbiter, fail-operational** | come 1x | maggiore (quote) | Solo se serve **continua-dopo-il-guasto** (probabile over-spec a 25 kg) |
| **MicroPilot MP2x28** | ~24–28 g (core) | Professionale, **non-ITAR** 🇨🇦; servizi DO-178 ma **DAL da verificare** | seriale, PWM, CAN | quote | Vantaggio **non-ITAR**; chiedere evidenza DAL |
| **Collins Piccolo** | — | Pedigree militare/NAVAIR (no pacchetto civile EASA pubblico) | FMS integrato | quote | **ITAR/US** → attrito export UE |
| **Honeywell cFBW** | — | Pedigree civile fortissimo (Part 23/SC-VTOL) | triplex lockstep | alto | Dimensionato per eVTOL → **over-SWaP/over-budget a 25 kg** |

**Sensore INS di supporto (non è un autopilota):** **VectorNav VN-300** (GNSS/INS **doppia antenna** → heading da GNSS-compass, <1,25 W) come **fonte ridondante di assetto/heading** verso il FC — critico in un VTOL dove i **forti campi magnetici** dei motori disturbano il magnetometro. Grado industriale (no DAL): vale come **aiuto**, non come base di certificazione.

### 2.2 Opzioni da dimostratore (non nella base di certificazione)
- **Cube Orange+ / Pixhawk 6X + ArduPilot/PX4**: tripla IMU isolata, doppio baro, ~300–500 USD, ottimi per collaudo. **Nessun DAL.**
- **Auterion Skynode**: PX4 enterprise, **NDAA-compliant** (≠ airworthiness EASA), forte integrazione/compute. Dimostratore/enterprise/difesa.

### 2.3 Ridondanza-obiettivo (per la classe)
**Tripla IMU · doppio GNSS (meglio doppia antenna per heading) · doppio ingresso di potenza · terminazione di volo indipendente (FTS).** Veronte 1x e George danno la tripla IMU internamente; si sale a Veronte 4x solo se serve il **fail-operational** invece del **fail-safe**.

---

## 3. GNSS e valutazione della necessità di RTK

### 3.1 Ricevitori candidati

| Prodotto | Specs | Resilienza | Interfaccia | Prezzo | EU |
|---|---|---|---|---|---|
| **u-blox ZED-F9P** | L1/L2 RTK, 0,01 m + 1 ppm | **nessun anti-spoof** | UART/SPI/USB, DroneCAN via carrier | ~200 USD modulo | diffuso — **solo dimostratore** |
| **Septentrio mosaic-X5** ★ | tripla banda, tutte le costellazioni | **AIM+ / OSNMA** anti-jam+spoof | UART/USB/Ethernet | ~800–1.200 USD | **Milexia FR/IT, SACA** |
| **Septentrio AsteRx-m3 Pro** | multi-freq | **AIM+** | seriale/USB | ~2–3k USD | EU |
| **NovAtel OEM7700** | 555 canali, SPAN INS, ALIGN heading | **GRIT** anti-jam/spoof | seriale/USB/**CAN**/Eth | ~1–3k+ USD | via Hexagon |

### 3.2 Quando serve davvero l'RTK (cm)?

| Funzione | RTK necessario? | Perché / alternativa |
|---|---|---|
| **Navigazione in rotta (ala fissa)** | **NO** | **SBAS/EGNOS** (~1–3 m) con **integrità** (limiti d'allarme) è preferibile: l'RTK grezzo **non dà integrità** |
| **Atterraggio di precisione shipborne (ponte 5×5 m)** | **SÌ, ma moving-base** | Il ponte si muove → RTK assoluto verso base fissa **inutile**. Serve **RTK relativo** (base sulla nave, rover sul velivolo). mosaic-X5/OEM7700 supportano moving-base/heading |
| **Payload georeferenziati (LiDAR/fotogrammetria)** | **SÌ (o PPK)** | Direct georeferencing; in alternativa **PPK** in post-processing (nessun datalink RTK, più robusto alla perdita di link) — ideale per il survey, **non** per la guida real-time all'atterraggio |

> **Raccomandazione GNSS:** ricevitore **anti-jam/anti-spoof** (Septentrio AIM+/OSNMA o NovAtel GRIT), **doppia antenna** per l'heading, **EGNOS in rotta**, **moving-base RTK** per l'atterraggio navale, **PPK** per i payload di rilievo. ZED-F9P **solo** sul dimostratore. La resilienza GNSS è sempre più un'aspettativa esplicita della safety-case (dual-use/marittimo).

---

## 4. Altimetro AGL distanziometrico (lo scenario "avvallamento")

**Il problema posto:** quota di decollo bassa in un avvallamento; la missione richiede di salire; la quota **barometrica** è riferita al punto di decollo → serve la **distanza reale drone-suolo (AGL)** rispetto alla posizione attuale, non alla pressione di partenza.

### 4.1 Radar altimeter (primario — all-weather, sopra acqua/vegetazione/nave)

| Prodotto | Range | Peso | Potenza | Interfaccia | Prezzo |
|---|---|---|---|---|---|
| **Ainstein US-D1** ★ | 0,5–50 m, 24 GHz, ±4–6 cm | **110 g** | **2 W** | UART + **CAN**, IP67 | **~499 USD** |
| **Ainstein LR-D1 / US-D1 Pro** | >50 m (lungo raggio) | ~simile | ~2 W | UART/CAN | quote |
| **Smartmicro (automotive-grade)** | lungo raggio robusto | vario | basso | CAN/seriale | quote (OEM 🇩🇪) |

### 4.2 LiDAR altimeter (flare/atterraggio su superficie dura, alta precisione)

| Prodotto | Range | Peso | Potenza | Interfaccia | Prezzo |
|---|---|---|---|---|---|
| **LightWare SF45/B** (scanning) | 0,2–50 m, 388 Hz | **59 g** | ~0,5 W | seriale/I²C/USB | 449 USD |
| **LightWare SF20/C** | 100 m, 500 Hz | **10 g** | basso | seriale/I²C | 279 USD |
| **Benewake TF03** | 100/180/350 m | 89 g | **<1 W** | UART/**CAN**/485, IP67 | ~130–250 USD |

### 4.3 Architettura raccomandata (per fase di volo)
- **Decollo/salita in avvallamento e ostacoli bassi:** **radar 50 m (US-D1)** → AGL reale nella fase bassa.
- **In rotta / AGL sul terreno:** i sensori corti saturano → **baro + database terreno (SRTM/DTED)**; radar lungo raggio (LR-D1 / TF03-180/350) solo se serve **terrain-following** real-time.
- **Atterraggio di precisione / ponte nave:** **radar preferito** (funziona sopra acqua e ponte bagnato); **LiDAR** per il **flare** cm-level su superficie preparata.
- **Nessun problema di peso/consumo:** tutti <150 g e <2 W. **Non richiedono certificazione** a meno di usarli per una funzione critica (terrain-following/geofencing di sicurezza).

---

## 5. Sensori dell'impianto carburante (genset) — non critici, no certificazione

### 5.1 Livello serbatoio → ottimale la sonda **capacitiva**

| Tecnologia | Comportamento con assetto/sloshing | Verdetto |
|---|---|---|
| **Capacitiva** ★ | Stato solido, **insensibile all'orientamento**, alta risoluzione anche con slosh | **Ottimale** (Reventec, Gill Sensors 🇬🇧 — distrib. EU UAV Propulsion Tech) |
| Ultrasonica | **Dead-band** vicino e **errore con lo sloshing** | No |
| Galleggiante/resistiva | Usura meccanica, sensibile all'assetto | Economica ma no |

### 5.2 Portata carburante → **derivata dall'ECU EFI** (o flussometro dedicato)
- Se il motore genset è **EFI** (scelto anche per le emissioni — `Bilancio di Massa` §4), l'**ECU calcola già la portata** dal duty degli iniettori → **gratis** e sufficiente per la stima autonomia.
- Flussometro dedicato (turbina/volumetrico o ultrasonico Sentronics FlowSonic) **solo** se la stima ECU risultasse insufficiente.

> **Architettura di stato-carburante raccomandata:** **livello capacitivo (quantità residua, robusta all'assetto) + portata da ECU (rateo/consumo)**, **fusi** → miglior stima di autonomia e **riserva di rientro** (che nel genset alimenta anche la logica di ridondanza, `Trade Propulsione` §8).

---

## 6. Elettronica di potenza dei motori e I/O

### 6.1 Dimensionamento
Con **~1–2 kW per motore lift** a ~44–50 V (12–14S) la corrente per ESC è **~25–45 A continui** → i 200 A sono overkill; il punto giusto è **ESC HV 80–120 A** con margine.

| Prodotto | Rating | Telemetria | Note | EU |
|---|---|---|---|---|
| **APD 120F3[X]** ★ | 12S/120 A, picco ~18 kW | **CAN** + DShot/PWM, RPM | STM32F3, ottima qualità (OEM 🇦🇺) | via distributori |
| **T-Motor FLAME 60–100 A HV** | fino 14S | CAN (nuovi)/PWM | linea industriale UAV matura | diffuso |
| **Hobbywing XRotor X-series** | motore+ESC+elica integrati | **CAN** (V/I/RPM/T), IPX7 | semplifica l'integrazione ma **accoppia** motore+ESC | diffuso |

### 6.2 La domanda posta: "una board unica con 4 inverter/ESC"? → **sconsigliata**
Valutazione: per **questo** velivolo (VTOL con motori all'estremità dei booms) conviene **4 ESC separati (vicini a ciascun motore) + power-distribution board**, non un **4-in-1**, perché:
1. Gli ESC vicini al motore **accorciano i tratti di potenza** e **distribuiscono il calore**.
2. Un **4-in-1 è un single point of failure**: perderlo = perdere più lift → inaccettabile per la certificabilità.
3. La **telemetria CAN per-ESC** (V/I/RPM/T) è essenziale per il **monitoraggio del bus del genset** e l'isolamento guasti.

Il 4-in-1 vince **solo** su micro-multirotori compatti — non è il nostro caso.

### 6.3 I/O aggiuntivi (se il FC non ha abbastanza uscite servo / ingressi sensori)
Un VTOL+ala fissa ha molte uscite (4 lift + pusher + alettoni/equilibratore/timone + gas/starter/choke del genset + payload) → possono eccedere le PWM di un FC compatto. Soluzione: **nodi CAN (DroneCAN/UAVCAN)** che convertono CAN→PWM/servo e portano sensori sul bus (mRo CAN Node, RaccoonLab, CUAV, ARK).

> **Per la build certificata:** restare **nell'ecosistema CAN del fornitore dell'autopilota** (nodi **Veronte** o **uAvionix/Cube**), così la catena I/O è **coperta dallo stesso data-package** invece di mischiare nodi open non certificati.

---

## 7. Consumi (come conseguenza delle scelte)

| Sottosistema (scelta baseline) | Potenza tipica |
|---|---|
| Flight controller certificabile (Veronte 1x/George) | ~5–10 W |
| GNSS anti-jam (mosaic-X5) + 2ª antenna | ~1,5–2,5 W |
| INS di supporto (VN-300), se adottato | ~1,3 W |
| Radar altimeter (US-D1) | ~2 W |
| LiDAR flare (SF20), se adottato | ~0,5 W |
| Sensori carburante (livello + ECU) | <1 W |
| Nodi CAN I/O | ~1–3 W |
| **Totale avionica "core"** | **~15–30 W** |

> Coerente con la voce **"avionica/payload ~45 W"** del `Trade Study` §3.1 (il resto va ai radio/telemetria — `Telemetria, Data Link e Stazione di Terra` — e al payload — `Componenti di Payload`). **I consumi non guidano la scelta**, ma confermano che l'elettronica certificabile **non fa saltare** il budget energetico.

---

## 8. Budget cap — impatto economico (indicativo)

| Voce | Fascia (quote-based) | Nota per il cap |
|---|---|---|
| Autopilota certificabile (Veronte 1x / George) | **€/USD 4k–20k+** | La voce che alza di più il costo vs hobby (~€300); ma è **imprescindibile** per la certificazione |
| GNSS anti-jam (mosaic-X5/OEM7700) | ~€0,8–3k | vs ~€200 ZED-F9P dimostratore |
| Radar/LiDAR altimeter | ~€0,1–0,6k | trascurabile |
| Sensori carburante (capacitivo + ECU) | ~€0,2–1k | ECU-derivato ≈ gratis |
| 4× ESC HV + PDB + nodi CAN | ~€1–3k | telemetria CAN inclusa |

> **Conseguenza sul cap:** la certificabilità sposta il costo dell'avionica di **~1–2 ordini di grandezza** rispetto all'hobby. Va riflesso in `WP-B5` (i prezzi "COTS estero €5–20k/unità" del solo motore vanno **rivisti verso l'alto** aggiungendo l'avionica certificabile).

---

## 9. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Evidenza DAL effettiva (Veronte/George/MicroPilot) | Richiedere il **data-package** e la mappatura OSO/SAIL al fornitore |
| Moving-base RTK sul ponte nave | Trade dedicato atterraggio shipborne (base GNSS a bordo nave) |
| Integrazione INS ridondante vs magnetometro nei campi motore | Prova EMC/heading in configurazione VTOL |
| Certificabilità della catena di potenza (ESC/inverter) | Verificare se il fornitore ESC offre evidenze; altrimenti area **make/adatta** |
| Prezzi reali (tutti quote-based) | RFQ ai fornitori shortlist (Embention, uAvionix, Septentrio, Ainstein, Reventec, APD) |

---

*Analisi first-order stage-appropriate per la fattibilità. Prodotti/prezzi indicativi da confermare via RFQ e data-package. Baseline: **Veronte 1x** (o **George**), **GNSS anti-jam + EGNOS/moving-base/PPK secondo funzione**, **radar US-D1 + LiDAR flare**, **livello capacitivo + portata ECU**, **4 ESC HV CAN + PDB + nodi CAN nell'ecosistema certificato**. Dimostratore su **Cube/PX4**, prodotto su avionica **con pacchetto DAL**.*

### Fonti principali
- Embention Veronte 1x/4x: https://www.embention.com/veronte-ecosystem/autopilots/1x-sensor-redundancy/ · https://www.embention.com/whitepaper/mocs-for-sail-iv-advanced-safety-through-veronte-autopilot/
- uAvionix George + Hionos (DO-178C): https://uavionix.com/products/george/ · https://uavionix.com/press/uavionix-and-hionos-team-introduce-do-178c-compliant-pulsar-autopilot-software-onto-george-autopilot/
- MicroPilot MP2x28: https://www.micropilot.com/products-mp2128g.htm · Collins Piccolo: https://www.collinsaerospace.com/what-we-do/Industries/military-and-defense/avionics/autopilot/piccolo-flight-management-systems/ · Honeywell cFBW: https://aerospace.honeywell.com/us/en/products-and-services/products/cabin-and-cockpit/avionics/flight-management-systems/compact-fly-by-wire-flight-control-system
- VectorNav VN-300: https://www.vectornav.com/products/detail/vn-300
- Septentrio mosaic-X5 (AIM+): https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-x5 · NovAtel OEM7700: https://novatel.com/products/receivers/gnss-gps-receiver-boards/oem7700 · u-blox ZED-F9P: https://www.u-blox.com/en/product/zed-f9p-module
- Ainstein US-D1 / LR-D1: https://ainstein.ai/us-d1-all-weather-radar-altimeter/ · https://ainstein.ai/lr-d1-uav-long-range-radar-altimeter/ · LightWare SF45/SF20: https://lightwarelidar.com/shop/sf45-b-50-m/ · https://lightwarelidar.com/shop/sf20-c-100-m/ · Benewake TF03: https://en.benewake.com/TF03/index.html
- Reventec (livello capacitivo UAV): https://www.reventec.com/qa-with-unmanned-systems-technology/ · Gill Sensors: https://www.gillsc.com/newsitem/38/miniature-liquid-level-sensors-uav-s
- APD F-Series: https://docs.powerdrives.net/products/f_series · T-Motor FLAME: https://uav-en.tmotor.com/Multirotor/ESC/flame/ · Hobbywing XRotor X: https://www.hobbywing.com/en/drone-propulsion/multirotor/integrated/x-series
- Nodi CAN/DroneCAN: https://ardupilot.org/plane/docs/common-dronecan-servos.html
