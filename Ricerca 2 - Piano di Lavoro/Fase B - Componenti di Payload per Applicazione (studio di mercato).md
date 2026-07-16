# Fase B — Componenti di Payload per Applicazione (studio di mercato)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio di mercato dei **componenti di payload reali** per riempire il "parco payload": per **ogni applicazione contemplata**, i sensori/telecamere/radar/relay disponibili in commercio, con peso, potenza, prezzo indicativo e vincoli export |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Relazione con** | `Studio Pesi Payload` (che fissa il **payload di progetto a 4 kg**); qui si verifica **con prodotti reali** che ogni applicazione ci stia dentro e **con quali componenti** |
| **Perimetro** | **Solo payload.** L'avionica di bordo è in `Avionica ed Elettronica di Bordo`; telemetria/link/GCS in `Telemetria, Data Link e Stazione di Terra`. |
| **Impostazione** | Tecnica/di mercato; **budget cap** considerato (i payload sono la voce di costo più variabile). |

> ⚠️ **Onestà tecnica:** pesi/potenze sono dati di targa (solo sensore/turret, salvo diverso avviso); prezzi **indicativi/quote-based**. Le note **export** (ITAR/EAR/lista UE dual-use/NDAA) sono una **lettura di esposizione**, non consulenza legale: confermare ECCN/numero lista UE col fornitore. Fonti in §7.

---

## 0. Executive summary

1. **Il budget payload di 4 kg è generoso per quasi tutte le applicazioni.** Le missioni tipiche stanno **≤ 2 kg**; l'unica applicazione che lo mette in tensione è il **radar/SAR marittimo di imaging** (§4).
2. **Regola di progetto per app:** EO/IR fuoco/rischio ~1–1,2 kg; LiDAR ispezione **stare ≤ 2 kg** (evitare i survey-LiDAR più pesanti); multi/iperspettrale agricoltura ~0,5–1,5 kg; marittimo **solo** radar ESA leggero (EchoGuard 1,25 kg) o SAR NSP-3 (3,04 kg) + AIS; gateway/relay <1 kg.
3. **App 4 (imaging-SAR marittimo) è il vincolo:** i veri SAR (PicoSAR ~10 kg, Gabbiano <24 kg, IMSAR NSP-5 ~11 kg) **eccedono** i 4 kg → richiedono una piattaforma più grande. Entro 4 kg passano **solo** IMSAR **NSP-3 (3,04 kg)** o radar ESA non-imaging **Echodyne EchoGuard (1,25 kg)** + AIS.
4. **AI a bordo** (NVIDIA Jetson Orin) è trasversale e leggera (~0,1–0,16 kg + enclosure) → abilita detection on-board per fuoco/ISR.
5. **Disponibilità UE forte** (NextVision integrata UE, Octopus 🇱🇻, DST 🇸🇪, RIEGL 🇦🇹, YellowScan 🇫🇷, Workswell 🇨🇿, Cubert 🇩🇪, AIS Comar/Digital Yacht 🇬🇧, HENSOLDT 🇩🇪). **Attrito export massimo** su Trillium, IMSAR, radar Leonardo, HENSOLDT ARGOS, Persistent MPU5; **dual-use EAR** (procurabile ma licenziato) su FLIR Boson/Hadron, Echodyne, Silvus, Doodle, Jetson alto, Headwall, MagArrow; **caveat NDAA/origine cinese** su Hesai e DJI.

---

## 1. Fuoco / rischio (incendi, dissesto) — EO/IR stabilizzato + AI a bordo

*Fit tecnico migliore per il C3 ad alta persistenza (`Downstream Civile` §tab).*

| Prodotto | Specs | Peso | Potenza | Prezzo indic. | Export |
|---|---|---|---|---|---|
| **NextVision Colibri2** 🇮🇱 | EO+LWIR 640, ×20 ottico, micro-stab. | **0,18 kg** | pochi W | ~€12–18k | MoD IL (non-ITAR); molto integrato in UE |
| **NextVision Raptor** 🇮🇱 | EO/LWIR, 80× EO, laser opz., AI tracking | **0,64 kg** | decine W | ~€30–45k | come sopra |
| **Octopus ISR Epsilon 140LC** 🇱🇻 | EO 30× + LWIR | **1,3–1,7 kg** | decine W | quote | **UE** (Lettonia); dual-use Wassenaar |
| **Octopus ISR Epsilon 175** 🇱🇻 | 4 sensori **MWIR** (il più piccolo al mondo) | **2,6 kg** | alta | quote | **MWIR raffreddato = 6A003 controllato** |
| **DST Control OTUS-U135** 🇸🇪 | micro-gimbal EO/IR + LRF + geolocation | **~1,0 kg** | decine W | quote | **UE** (Svezia); dual-use |
| **Trillium HD25 / HD40** 🇺🇸 | gimbal 2,5"/4" EO/IR, INS | ~0,4–0,5 / ~1,0–1,5 kg | 10–35 W | quote | **ITAR/EAR** — licenza import UE |
| **Teledyne FLIR Hadron 640R** 🇺🇸 | 64 MP visibile + 640×512 radiometrico | **0,056 kg** | 1,8–2,9 W | ~$3–5k | **EAR 6A003** |
| **HENSOLDT ARGOS-8** 🇩🇪 | EOS 8", IR raffreddato + laser designator | **<6 kg** | alta | quote (militare) | Lista militare UE; **eccede 4 kg** |
| **NVIDIA Jetson Orin NX 8/16 GB** 🇺🇸 | fino 157 TOPS | **~0,09–0,16 kg** (+ enclosure) | 10–40 W | ~$400–700 | **EAR dual-use** (UE libero) |

**Peso di missione realistico:** Raptor/Colibri2 + Jetson Orin (+ enclosure) → **~1,0–1,2 kg**. Anche Epsilon 175 (2,6) + compute (~0,5) = **~3,1 kg**, dentro i 4 kg. Solo ARGOS-8 sfora.

---

## 2. Ispezione lineare (linee elettriche, ferrovie, condotte)

### 2.1 LiDAR di rilievo

| Prodotto | Specs | Peso | Potenza | Prezzo indic. | Export |
|---|---|---|---|---|---|
| **YellowScan Mapper+** 🇫🇷 | integrato, 100 m AGL, ~1 h | **1,1 kg** (no batt.) | decine W | ~€50–70k | **UE** commerciale |
| **RIEGL miniVUX-3UAV** 🇦🇹 | 300 kHz, 360° FOV | **1,55–1,6 kg** (sensore) | 18 W | ~€80–110k | **UE**; controllo minimo |
| **RIEGL miniVUX-SYS** 🇦🇹 | sistema completo con IMU/GNSS | **2,0–3,3 kg** | 18–43 W | ~€120k+ | **UE** |
| **Hesai XT32M2X** (kit) 🇨🇳 | 32 linee, kit integrati | **0,49 kg** / kit ~1,0–1,26 kg | decine W | ~$25–45k (kit) | **origine cinese — caveat NDAA**; UE commerciale ok |
| **YellowScan Voyager** 🇫🇷 | lungo raggio, 440 m AGL | **3,5 kg** (no batt.) | alta | ~€120k+ | **UE** — **è il tetto dei 4 kg** |

### 2.2 RGB + termografico

| Prodotto | Specs | Peso | Prezzo | Note |
|---|---|---|---|---|
| **Workswell WIRIS Pro** 🇨🇿 | termico + RGB radiometrico | **<0,43 kg** | ~€8–15k | **UE**; core termico può essere controllato |
| **DJI Zenmuse H20T** 🇨🇳 (solo benchmark) | 640×512 termico + 20 MP 23× + LRF 1200 m | **0,83 kg** | ~$3,8–7,8k | **ecosistema DJI/Matrice** — non integrabile su UAS generico; caveat NDAA |

**Peso di missione realistico:** LiDAR **1,1–3,5 kg**. **Sweet spot ≤ 2 kg** (Mapper+/miniVUX/Hesai) → lascia margine; **Voyager (3,5 kg) = soffitto**. RGB+termo (<0,9 kg) → banale entro budget.

---

## 3. Agricoltura / forestale — multi/iperspettrale

| Prodotto | Specs | Peso | Prezzo indic. | Export |
|---|---|---|---|---|
| **MicaSense RedEdge-P** 🇺🇸 | 5 bande + pancro, DLS2 | **0,30 kg** (0,745 kit) | ~$8k | EAR99 (basso) |
| **MicaSense Altum-PT** 🇺🇸 | 5 bande + pancro + **termico** | **0,46 kg** (0,577 kit) | ~$15–20k | banda termica può alzare l'ECCN |
| **Sentera 6X** 🇺🇸 | 6 bande, 3 cm GSD | **0,52–0,59 kg** | quote | commerciale US |
| **Cubert ULTRIS X20 Plus** 🇩🇪 | iperspettrale snapshot; sistema <1,5 kg | **0,35–0,69 kg** | ~€40–60k | **UE**; dual-use possibile |
| **Cubert ULTRIS 5** 🇩🇪 | iperspettrale miniatura | **0,12 kg** | quote | **UE** |
| **Headwall Nano-Hyperspec** 🇺🇸 | VNIR 270 bande, processore a bordo | **~0,6 kg** | ~$40–80k | **EAR**, dual-use 6A003 |

**Peso di missione realistico:** multispettrale **~0,5–0,75 kg**; iperspettrale **~0,6–1,5 kg** (compute incl.). **<40% del budget** → è l'applicazione **meno vincolata**; c'è spazio per co-imbarcare RGB o sensore di luce.

---

## 4. ISR marittimo — radar/SAR + AIS (il vincolo del budget)

| Prodotto | Specs | Peso | Potenza | Prezzo | Export |
|---|---|---|---|---|---|
| **Echodyne EchoGuard** 🇺🇸 | radar ESA metamateriale (sorveglianza/C-UAS) | **1,25 kg** | 50 W (op)/<10 W (idle) | ~$25–40k | **EAR** (procurabile, licenziato) |
| **IMSAR NSP-3** 🇺🇸 | SAR/GMTI Ku multi-modo | **3,04 kg** | 81 W | quote (militare) | **ITAR** — forte controllo |
| **IMSAR NSP-5 ER** 🇺🇸 | SAR/MTI multi-modo | **~10,9 kg** | <275 W | quote | ITAR; **~3× il budget** |
| **Leonardo PicoSAR** 🇮🇹 | SAR X-band AESA, 20 km | **~10 kg** | alta | quote (militare) | lista militare UE; **eccede** |
| **Leonardo Gabbiano TS UL** 🇮🇹 | radar sorveglianza X multi-modo | **<24 kg** | 450 W | quote | lista militare UE; **eccede molto** |
| **AIS RX — Comar COM100 / Digital Yacht** 🇬🇧 | ricevitore AIS dual-channel OEM | **0,021–0,1 kg** | <2 W | ~€150–400 | **UE** commerciale, libero |

**Peso di missione realistico:** **è l'applicazione che rompe il budget.** I SAR di imaging (3–24 kg) per lo più **eccedono o consumano tutto** il budget. Entro 4 kg chiudono **solo**:
- **IMSAR NSP-3 (3,04) + AIS (~0,1) ≈ 3,14 kg**, oppure
- **EchoGuard (1,25) + AIS (~0,1) + EO/IR condiviso dall'App 1 (Raptor 0,64) ≈ 2,0 kg** (con margine).

> **Conclusione:** l'**ISR marittimo a SAR di imaging pieno richiede una piattaforma più grande del C3**. Nella nostra classe si fa **radar ESA leggero (rilevamento/tracking) + AIS + EO/IR**, non imaging-SAR. Da riflettere nel posizionamento marittimo (`Market`, `Subacquea`).

---

## 5. Subacqueo / dual-use gateway — relay/mesh, magnetometro

*(La piattaforma è un **nodo aereo**, non subacqueo — `Subacquea` §137. Le boe **non** sono a bordo: il payload è il relay.)*

| Prodotto | Specs | Peso | Potenza | Prezzo | Export |
|---|---|---|---|---|---|
| **Doodle Labs Mesh Rider (Nano/Mini/OEM)** 🇺🇸🇸🇬 | MANET auto-guarente; **SKU UE 868/2,4 GHz** | **0,025–0,10 kg** | 4–14 W | ~$1,5–4k | **EAR** (encryption); il più accessibile |
| **Silvus StreamCaster SL4200** 🇺🇸 | MANET 2×2 MIMO | **0,295 kg** | 4,8–17 W | ~$5–10k | **EAR**; scegliere banda/potenza UE |
| **Persistent Systems MPU5** 🇺🇸 | Wave Relay MANET, video | ~0,2–0,4 kg | decine W | ~$10k+ | **EAR/ITAR** |
| **Geometrics MagArrow II** 🇺🇸 | magnetometro cesio ottico, GPS/storage a bordo | **1,0–1,2 kg** | pochi W | ~$45–60k | commerciale; sensore cesio con controllo dual-use |
| **Gateway LoRaWAN** (OEM RAKwireless/Multitech) | gateway IoT aereo (concept) | **<0,3 kg** | pochi W | ~€100–500 | commerciale, libero |
| **Nodo relay acustico / sonobuoy-relay** (concept) | relay verso nodi acustici (via radio MANET) | = radio mesh | = radio mesh | — | radio controllate come sopra |

**Peso di missione realistico:** relay comms **<0,6 kg**; magnetometro ~**1,5 kg**; gateway dual-use combinato **<1 kg**. **Ampio margine** → spazio per co-imbarcare EO/IR.

> **Nota (coerente con `Studio Pesi Payload`):** LoRaWAN-gateway e sonobuoy-relay **non hanno una SKU "payload drone" unica** in commercio → vanno **integrati** montando un modulo OEM sulla dorsale radio MANET. Concept-level, da prototipare.

---

## 6. Sintesi vs budget 4 kg e note trasversali

| Applicazione | Payload di missione tipico | Entro 4 kg? |
|---|---|---|
| 1. Fuoco/rischio (EO/IR + AI) | ~1,0–1,2 kg (fino ~3,1 con Epsilon 175) | ✅ (tranne ARGOS-8) |
| 2. Ispezione lineare (LiDAR) | 1,1–3,5 kg; sweet spot ≤ 2 kg | ✅ (Voyager = tetto) |
| 3. Agricoltura (multi/iper) | 0,5–1,5 kg | ✅ ampio margine |
| 4. ISR marittimo (radar/SAR) | EchoGuard+AIS ~1,4 kg ✅ / **imaging-SAR 3–24 kg ✗** | ⚠️ parziale |
| 5. Gateway dual-use | <0,6 kg (relay) … ~1,5 kg (magnet.) | ✅ ampio margine |

**Conferma per `Studio Pesi Payload`:** i dati di mercato **confermano il payload di progetto a 4 kg** (nessuna app tipica raggiunge 6 kg; solo l'imaging-SAR marittimo, che comunque eccede e va su piattaforma maggiore). **Note potenza:** i payload più energivori sono SAR (~80–275 W) e Jetson AGX (~15–60 W): il budget di **potenza** payload va sommato in `Bilancio di Massa`/`Avionica` §7 (qui il vincolo può essere l'energia, non il peso).

**Export/sovranità (sintesi):**
- **UE-nativi (preferibili per sovranità):** Octopus 🇱🇻, DST 🇸🇪, RIEGL 🇦🇹, YellowScan 🇫🇷, Workswell 🇨🇿, Cubert 🇩🇪, AIS 🇬🇧, HENSOLDT 🇩🇪.
- **ITAR/lista militare UE (attrito alto):** Trillium, IMSAR, Leonardo radar, HENSOLDT ARGOS, Persistent MPU5.
- **EAR dual-use (procurabile, licenziato):** FLIR Boson/Hadron, Echodyne, Silvus, Doodle, Jetson alto, Headwall, MagArrow.
- **Origine cinese (caveat NDAA/procurement pubblico):** Hesai, DJI.

---

## 7. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Prezzi/pesi esatti (molti quote-only) | RFQ ai fornitori shortlist per nicchia (EO/IR, LiDAR, radar, relay) |
| Budget di **potenza** payload per missione | Tabella potenza payload → `Bilancio di Massa`/`Avionica` |
| LoRaWAN-gateway e sonobuoy-relay | Prototipo d'integrazione su dorsale MANET |
| Interfaccia bay modulare (REQ-04) | Envelope meccanico/elettrico sul payload dimensionante (~4 kg: SAR NSP-3 / EO-IR) |
| Classificazione export dei payload dual-use/difesa | Verifica ECCN/lista UE + eventuale consorzio per l'accesso |

---

*Analisi first-order stage-appropriate per la fattibilità. Prodotti/pesi/prezzi indicativi da confermare via RFQ e datasheet. Conclusione: il **payload di progetto 4 kg** è confermato dai prodotti reali; l'unica applicazione fuori portata è l'**imaging-SAR marittimo** (piattaforma più grande). Priorità di sovranità ai payload **UE-nativi**.*

### Fonti principali
- EO/IR: NextVision Raptor https://nextvision-sys.com/cameras-cpt/raptor/ · Colibri2 https://www.nextvision-sys.com/colibri-2-2/ · Trillium HD25 https://www.trilliumeng.com/gimbals/hd25 · Octopus Epsilon 140LC https://octopus.uavfactory.com/uav-payloads-equipment/epsilon-140lc · DST OTUS https://www.aeroexpo.online/prod/dst-control/product-175542-15398.html · FLIR Hadron 640R https://oem.flir.com/products/hadron-640 · HENSOLDT ARGOS-8 https://www.hensoldt.net/products/argos-8-compact-airborne-electro-optical-device · Jetson Orin https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/
- LiDAR/ispezione: RIEGL miniVUX-3UAV https://www.riegl.com/en-usa/products/detail/riegl-minivux-3uav · YellowScan Mapper+ https://www.yellowscan.com/products/mapper-plus/ · Voyager https://www.yellowscan.com/products/voyager/ · Hesai https://www.hesaitech.com/product/xt16-32-32m/ · Workswell WIRIS Pro https://workswell.eu/thermal-drone-camera-inspection-wiris-pro/
- Agricoltura: MicaSense RedEdge-P https://www.dslrpros.com/products/micasense-rededgep · Altum-PT https://www.dslrpros.com/products/micasense-altum-pt · Sentera 6X https://senterasensors.com/6x/ · Cubert ULTRIS X20 Plus https://cubert-hyperspectral.com/en/ultris-x20-plus/ · Headwall Nano-Hyperspec https://www.spectraresearch.com/wp-content/uploads/2016/01/Nano-Hyperspec.pdf
- Marittimo: IMSAR NSP-3 https://www.imsar.com/radar-systems/nsp-3/ · Leonardo PicoSAR https://www.leonardo.us/radar-picosar · Echodyne EchoGuard https://www.echodyne.com/radar-systems/echoguard · AIS Comar COM100 https://comarsystems.com/product/com100-ais-receiver-bundle-with-av30-antenna/
- Gateway/dual-use: Silvus SL4200 https://silvustechnologies.com/products/ · Persistent MPU5 https://persistentsystems.com/mpu5-specs/ · Doodle Labs https://doodlelabs.com/products/ · Geometrics MagArrow II https://www.geometrics.com/product/magarrow/
