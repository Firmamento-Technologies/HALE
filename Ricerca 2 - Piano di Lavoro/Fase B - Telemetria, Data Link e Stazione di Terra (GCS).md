# Fase B — Telemetria, Data Link e Stazione di Terra (GCS)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio preliminare di **telemetria, collegamento di comando/controllo (C2/radiocomando), downlink payload e stazione di terra (GCS)** per operazioni BVLOS in Italia (ENAC/EASA, SORA) |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Perimetro** | **Solo** telemetria e link/GCS (file separato per scelta operativa). L'avionica di bordo è in `Avionica ed Elettronica di Bordo`; i sensori di missione in `Componenti di Payload per Applicazione`. |
| **Impostazione** | Tecnica + **normativa** (spettro, SORA); **budget cap** considerato — qui la voce critica è l'**OPEX SATCOM**, non solo il CAPEX radio. |

> ⚠️ **Onestà tecnica:** i fatti su **spettro UE, SORA/RLP, Remote ID e legalità delle bande** sono ben corroborati (fonti §6). Alcune cifre di targa di singole radio (peso/prezzo SkyLink 5060, Silvus/MPU5) vengono da snippet di datasheet (PDF fornitore bot-bloccati) → **confermare a datasheet** prima di numeri "duri".

---

## 0. Executive summary

1. **La banda C2 aeronautica 5030–5091 MHz NON è oggi utilizzabile in UE** per il C2 civile: è allocata a livello internazionale (ITU/ICAO) come banda protetta UAS, ma **non esiste ancora un accesso civile armonizzato in Europa** (mandato CE→CEPT **ECC-24-014**, in corso, orizzonte pluriennale). L'equipaggiamento per questa banda (es. **uAvionix SkyLink**) è oggi una soluzione **USA/FAA**, **non** operabile in Italia. **È il fatto normativo più importante del documento.**
2. **In Italia si vola sulle bande esenti da licenza (ISM/SRD):** **2,4 GHz** (100 mW EIRP), **5,8 GHz** (sotto-bande), **868 MHz** (SRD) — **autorizzazione generale**, nessuna licenza per apparato. **868 MHz, NON 915 MHz** (la banda USA 902–928 è **illegale** in UE): ogni radio va nella **variante UE** (es. **RFD868x**, non RFD900x; SKU UE per Doodle/Silvus/Microhard).
3. **Architettura C2 raccomandata:** **link primario LOS MANET mesh** (Silvus / Persistent MPU5 / Doodle low-SWaP in banda UE) **+ backup SATCOM Iridium Certus 100**. Soddisfa la **continuità/disponibilità dell'OSO#06** e riduce la probabilità di lost-link; è anche la fascia **OPEX-efficiente** (~€60–200/mese vs ~€1.000+/mese di SwiftBroadband/Certus 700).
4. **GCS: dimostratore su QGroundControl/Mission Planner; prodotto BVLOS su stack certificabile** (Embention **Veronte Pipe/PCS**, DO-178C/DO-254; oppure Auterion). La **GCS è parte del "UAS"** ai sensi del Reg. 2019/945/947 → **dentro il perimetro SORA** (affidabilità, HMI, lost-link, prestazione C2 valutate).
5. **Obblighi adiacenti:** **Remote ID diretto (DRI)** obbligatorio dal **1/1/2024**; **Network RID** se dentro **U-space**; comportamento di **lost-link deterministico** sotto OSO#14/#15.

---

## 1. Spettro e normativa

### 1.1 Banda C2 aeronautica 5030–5091 MHz — stato UE (fatto critico)
- **Base di allocazione:** 5030–5091 MHz è allocata AM(R)S/AMS(R)S e identificata a livello internazionale (ITU WRC-2012, ICAO) come spettro **protetto** per il C2 (CNPC) degli UAS. È la banda "protetta" globalmente riconosciuta.
- **Realtà UE — non ancora disponibile per l'UAS civile:** in Europa è orientata alla **categoria Certified** ed era **fuori dallo scope** del lavoro CEPT (ECC Report 268, 2018) che ha armonizzato lo spettro droni per **Open e Specific**. **Non c'è una ECC Decision** che dia accesso civile armonizzato, né un percorso di licenza pronto in Italia.
- **In corso:** la CE ha dato **mandato alla CEPT (ECC-24-014, 2024)** per le condizioni tecniche armonizzate → è il veicolo con cui l'accesso potrebbe essere definito. **Trattarla come capacità futura (pluriennale), non opzione 2026.**
- **Conseguenza pratica:** **uAvionix SkyLink** (5030–5091) è oggi certificabile in **contesto USA** (bozza TSO-C213a, RTCA DO-362A, FCC Part 88, ago 2024); in UE **non operabile** perché lo spettro non è rilasciato al civile.

### 1.2 Bande ISM/SRD esenti da licenza — su queste si vola in Italia oggi

| Banda | Base UE | Limite potenza (UE) | Licenza in Italia | Uso C2/telemetria |
|---|---|---|---|---|
| **2,4 GHz** (2400–2483,5) | ERC 70-03 / EN 300 328 | 100 mW EIRP | **No licenza** (autorizzazione generale) | C2 + video più comune; congestionata |
| **5,8 GHz** (5725–5875) | ERC 70-03 / EN 302 502 | ~25 mW–1 W EIRP secondo sotto-banda | **No licenza** | downlink video + C2 secondario; più banda, meno raggio |
| **868 MHz** (863–870 SRD) | ERC 70-03 / EN 300 220 | ~25 mW e.r.p. (alcune sotto-bande 500 mW con duty) | **No licenza** | telemetria long-range low-rate; **NON 915** |

> ⚠️ **868 UE, non 915 USA:** la 902–928 MHz ("915") **non è legale in UE**. Ogni radio deve essere la variante **UE/868** (**RFD868x** non RFD900x, SKU UE per Doodle/Silvus/Microhard). Comprare la variante 915 per operare in Italia è un errore **illegale** ricorrente.

**Italia:** l'uso ISM/SRD è in **autorizzazione generale** (Ministero delle Imprese e del Made in Italy) — nessuna licenza per apparato, ma equipaggiamento **CE/RED** entro i limiti EN. In più l'**ENAC**, nell'autorizzazione operativa, richiede che il **data link usi frequenze scelte per minimizzare le interferenze** che possano compromettere la sicurezza: l'onere è **giustificare la robustezza del link nel SORA**, non ottenere una licenza di spettro.

### 1.3 SATCOM per il BLOS
Sotto l'orizzonte LOS/mesh, il C2 BLOS richiede SATCOM: **Iridium Certus (L-band, globale)** o **Inmarsat/Viasat SwiftBroadband (L-band)** — §3. La licenza di spettro MSS è del **provider di airtime** → nessuna licenza operatore in Italia, ma è una **voce OPEX ricorrente**.

### 1.4 Prestazione del link C2 (RLP) nel SORA
- **SORA 2.5** è l'AMC adottata da EASA (ED Decision 2025/018/R), che sostituisce la 2.0.
- L'integrità C2 si dimostra sotto **OSO#06 ("C2 Link")**: descrivere e analizzare **copertura/raggio, latenza, continuità, disponibilità, integrità e protezione (sicurezza)**.
- **RLP = Required C2 Link Performance** (framework JARUS). Benchmark quantitativo: per **SAIL III**, latenza del comando **≤ 5 s per il 99% del tempo**; ai SAIL più alti si stringe.
- **Integrità/sicurezza:** CRC (es. CRC-32) per l'integrità dati; protezione link per **ASD-STAN prEN 4709-001 / EUROCAE ED-325**. SAIL alto → protezione crittografica attesa.

### 1.5 Remote ID (UE)
- **DRI (Direct Remote ID)** obbligatorio dal **1/1/2024** (Reg. 2019/945): il drone trasmette **localmente** (Wi-Fi/Bluetooth) ID operatore, posizione e posizione pilota. Standard **ASD-STAN prEN 4709-002**. Nessuna infrastruttura a terra.
- **NRI (Network Remote ID)** richiesto **dentro uno U-space** (Reg. 2021/664): ID/telemetria pubblicati in rete per la durata del volo. Distinto da DRI e dal C2.
- Per un BVLOS Specific: **DRI a bordo di serie** + **capacità NRI** se si opera in volume U-space.

### 1.6 Lost-link (perdita del C2)
- Gestito nel SORA sotto **OSO#14 (procedure di contingenza, incl. perdita C2)** e **OSO#15 (risposta emergenza)**; dimostrazione tecnica del link sotto OSO#06.
- Requisito: comportamento di lost-link **predefinito e deterministico** (hold → return-to-home nel volume operativo → land, o terminazione), che tenga il velivolo **dentro il volume operativo/adiacente** e il ground-risk buffer.
- Per il BVLOS è il motivo per cui i **link ridondanti (LOS mesh + backup SATCOM)** riducono la probabilità di lost-link e **facilitano l'argomento OSO#06 / un SAIL più basso**.

---

## 2. Radio C2 / mesh (COTS)

> **Caveat legalità UE** trasversale: solo 2,4 GHz (100 mW EIRP), sotto-bande 5,8 GHz e 868 MHz sono esenti in Italia. Molte di queste radio si vendono a **potenze/bande USA (915 MHz, alta potenza, bande militari L/S)** **non** esenti in UE → serve la **SKU UE** e spesso un'autorizzazione individuale/sperimentale.

| Radio | Banda(e) | Raggio LOS | Throughput | TX | Peso | Potenza | Cifra | Note UE |
|---|---|---|---|---|---|---|---|---|
| **uAvionix SkyLink 5060 / micro** (+ **skyStation** a terra) | **5030–5091** (protetta) | C2 BVLOS | C2/CNPC (comando, non video) | 10 W / 100 mW | micro ~decine g | bassa (avionica) | quote | **Banda non civile in UE (§1.1).** Certificabile in **USA** |
| **Silvus StreamCaster SC4200 EP** | 300 MHz–6 GHz sintonizzabile | ~100+ km con relay | fino **100 Mbps** | 1 mW–10 W (20 W EIRP beamform.) | modulo low-SWaP | ~10–30 W | ~$8–15k+/nodo | **AES-256**; scegliere **SKU UE**; IP68 |
| **Persistent MPU5 (Wave Relay)** | moduli 2,4 GHz / L/S/C | fino ~130 mi con gain; multi-hop | alto (video/dati/voce) | 6–10 W | **~391 g** | rilevante | ~$10–15k+ | MANET self-healing; **EAR/ITAR**; modulo UE + autorizz. |
| **Doodle Labs Mesh Rider (Nano/Mini/OEM)** | sub-GHz + 2,4 + 6 GHz; **SKU UE 868/2,4** | multi-km, mesh | decine Mbps | ~1,6 W (32 dBm) | **25 / 34 / 102 g** | 4–14 W | ~$1,5–3k | **miglior low-SWaP**; specificare variante UE |
| **Microhard pMDDL2450** | **2,4 GHz** 2×2 MIMO | multi-km | fino 25 Mbps | fino 1 W | decine g | bassa | ~$300–900 | 2,4 GHz esente UE a 100 mW EIRP |
| **Trellisware TW-950** | 225–2600 MHz militari | tattico multi-hop | fino 16 Mbps | 100 mW–2 W | **~320 g** | 8 h/32 Wh | ~$10k+ | bande militari → **uso civile UE molto vincolato** |
| **RFD868x** (telemetria, non mesh) | **863–870 (UE)** | fino **40 km+** | fino 500 kbps | fino 1 W | **14 g** | ~1–3 W | ~$200–300/coppia | **usare 868x in Italia**; MAVLink classico |

> **Scelta baseline:** C2 primario **MANET mesh in banda UE** (Doodle low-SWaP per il dimostratore/leggero; Silvus/MPU5 per capacità/portata e cifra difesa), **telemetria MAVLink su RFD868x** come canale semplice, **backup SATCOM** (§3). Video payload sul mesh o su 5,8 GHz.

---

## 3. SATCOM BLOS (la voce OPEX)

| Sistema | Data rate | Peso | Potenza | Airtime (OPEX indic.) | Note |
|---|---|---|---|---|---|
| **Iridium Certus 9770** (transceiver) | 22 kbps up / 88 kbps down | **185 g** | ~5 W | dipende dal piano | globale (poli incl.); SWaP ideale per C2/backup |
| **Iridium Certus 100** (servizio) ★ | 22/88 kbps | terminale piccolo | bassa | **~$62–580/mese** (0–100 MB) | giusto per **backup C2** (comando/telemetria low-rate) |
| **Iridium Certus 700** | fino 700 kbps | maggiore | maggiore | da ~$79/mese in su | rate alto; antenna più pesante |
| **Inmarsat/Viasat SwiftBroadband SB-UAV** | 200–432 kbps (fino ~650) | L-band low-SWaP | media | **~$4–6/MB, ~$1.000+/mese** | C2 BLOS dedicato LALE; L-band (no poli) |

> **Impatto budget cap:** il SATCOM è l'**OPEX dominante**. Se usato **solo come backup C2** (comando/telemetria low-rate, non video), **Iridium Certus 100** (~€60–200/mese) è la scelta razionale; SwiftBroadband/Certus 700 (~€1.000+/mese) solo se serve BLOS ad alto rate. Modellare come **linea mensile per velivolo**, non one-off.

---

## 4. Stazione di terra (GCS)

### 4.1 Blocchi hardware
- **Unità di controllo ruggedizzata:** laptop/tablet MIL-STD-810/IP (classe Getac/Toughbook) con il software GCS.
- **Ground Data Terminal (GDT):** la radio C2 lato terra — **uAvionix skyStation** (IP67, PoE, backhaul LTE) per il caso C-band, oppure il nodo a terra del mesh scelto (Silvus/MPU5/Doodle) per il LOS.
- **Antenna direzionale / tracking:** antenna auto-tracking pan-tilt o **palo elevato** (es. Embention Veronte PCS, palo 3 m) per estendere il raggio LOS e migliorare il margine di link (argomento RLP).
- **Radiocomando manuale:** trasmettitore dedicato per **decollo/atterraggio e override manuale** (safety pilot), separato dal link BVLOS autonomo — spesso richiesto nel ConOps SORA per le fasi di lancio/recupero.
- **Ridondanza:** **link primario LOS mesh + backup SATCOM** (Iridium Certus 100) → supporta continuità/disponibilità OSO#06 e riduce il lost-link (§1.6).

### 4.2 Software — dimostratore vs certificabile (distinzione chiave)

| Livello | Prodotti | Ruolo | Postura di certificazione |
|---|---|---|---|
| **Open-source / dimostratore** | **QGroundControl**, **Mission Planner** (MAVLink; PX4/ArduPilot) | controllo volo, pianificazione, telemetria; ottimo per R&D e BVLOS dimostrativo | **Non certificato.** Accettabile in Specific se il SORA argomenta l'integrità di sistema, ma **nessuna DO-178C** → più difficile ai SAIL alti |
| **Prodotto / certificabile** | **Embention Veronte Pipe** (SW) + **Veronte PCS** (HW, Veronte 1x embedded, **DO-178C/DO-254 certificabile**); **Auterion Mission Control**; **UgCS** (SPH Engineering) | stesse funzioni + assurance di sviluppo, configuration control, evidenze per l'OSO | **Veronte** esplicitamente **DO-178C/DO-254 certificabile** → miglior fit BVLOS SAIL III+ |

> **Logica:** **QGroundControl/Mission Planner nel dimostratore** (rapido, MAVLink-nativo, licenza zero); per l'autorizzazione **BVLOS SAIL III+**, migrare a **stack certificabile** (Veronte Pipe/PCS o Auterion) così **OSO#06** e gli OSO di software-assurance sono difendibili con **evidenza del fornitore**, non auto-dichiarati. Coerente con la scelta autopilota di `Avionica ed Elettronica di Bordo` §2.

### 4.3 Ruolo normativo della GCS
In Specific/BVLOS la **GCS è parte del "UAS"** (Reg. 2019/945/947: UAS = aeromobile **+** l'equipaggiamento per controllarlo da remoto). Quindi GCS — hardware, software, antenna, link — è **dentro il perimetro SORA**: affidabilità, HMI, lost-link e prestazione C2 sono **valutati**, non trattati come accessorio. Ridondanza (primario LOS mesh + backup SATCOM) e un **percorso di override manuale** chiaro sono le leve pratiche per contenimento e OSO#06.

---

## 5. Sintesi e budget cap

| Elemento | Scelta baseline | Impatto budget |
|---|---|---|
| C2 primario | MANET mesh **banda UE** (Doodle → Silvus/MPU5) | CAPEX ~€1,5–15k/nodo (×2: bordo+terra) |
| Telemetria | **RFD868x** MAVLink | CAPEX ~€200–300 |
| Backup BLOS | **Iridium Certus 100** | **OPEX ~€60–200/mese** (dominante) |
| Remote ID | **DRI** a bordo (+ NRI se U-space) | CAPEX basso |
| GCS SW | QGC/Mission Planner → **Veronte Pipe/Auterion** | licenza zero (demo) → quote (prodotto) |
| GCS HW | unità rugged + tracking antenna + RC manuale | CAPEX medio |

> **Consuntivo cap:** il CAPEX del link è modesto; il **driver economico è l'OPEX SATCOM** (per-velivolo, mensile) e il **CAPEX della migrazione a stack certificabile** per il BVLOS. Riflettere entrambi in `WP-B5`.

---

## 6. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Cifre esatte SkyLink/Silvus/MPU5 (snippet) | Datasheet/RFQ diretti |
| Scelta banda/potenza per SORA specifico | Analisi di link budget + giustificazione RLP nel ConOps |
| Evoluzione 5030–5091 in UE | Monitorare il mandato CEPT ECC-24-014 (capacità futura) |
| Autorizzazione individuale per radio non-esenti | Verifica con MIMIT se si usano bande/potenze fuori ISM |
| Integrazione DRI/NRI e U-space | Verifica volumi U-space applicabili (San Salvo e futuri) |

---

*Analisi first-order stage-appropriate per la fattibilità. Fatti normativi/spettro corroborati; alcune cifre radio da confermare a datasheet. Baseline: **C2 MANET mesh in banda UE + backup Iridium Certus 100**, telemetria **RFD868x**, **DRI** obbligatorio, GCS **dimostratore→certificabile**; la **banda C2 5030–5091 MHz non è un'opzione UE 2026**.*

### Fonti principali
- **Spettro/normativa:** FCC 5030–5091 (ago 2024) https://www.fcc.gov/document/fcc-report-supports-use-5030-5091-mhz-band-uas-operations · ECC Report 268 https://www.bakom.admin.ch/dam/bakom/de/dokumente/frequenzen/Drohnen/ecc_report_268.pdf.download.pdf/ECC_Report_268.pdf · mandato CE→CEPT ECC-24-014 https://cept.org/documents/ecc/81470/ecc-24-014_mandate-to-the-cept-on-uas · ERC 70-03 https://docdb.cept.org/download/3700 · Impl. Decision (UE) 2019/1345 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32019D1345 · ENAC UAS https://www.enac.gov.it/en/safety-security/uas-drones
- **SORA/RLP:** EASA ED Decision 2025/018/R (SORA 2.5) https://www.easa.europa.eu/en/document-library/agency-decisions/ed-decision-2025018r · EASA MOC OSO#6 (SAIL III) https://www.easa.europa.eu/en/downloads/139100/en · JARUS C2 Link RCP/RLP http://jarus-rpas.org/wp-content/uploads/2023/06/jar_02_doc_rpas_c2_link_rcp.pdf
- **Remote ID:** EASA https://www.easa.europa.eu/en/document-library/general-publications/remote-identification-will-become-mandatory-drones-across · ASD-STAN DRI https://cms.stan-shop.org/uploads/2024/01/ASD-STAN_DRI_Introduction_to_the_European_digital_RID_UAS_Standard.pdf
- **Radio:** uAvionix skyStation https://uavionix.com/uncrewed-aircraft-systems/skystation/ · Silvus SC4200 https://silvustechnologies.com/products/streamcaster-radios/ · Persistent MPU5 https://persistentsystems.com/mpu5-specs/ · Doodle Labs https://doodlelabs.com/products/ · Microhard pMDDL2450 https://www.microhardcorp.com/pMDDL2450.php · RFD900x/868x https://files.rfdesign.com.au/Files/documents/RFD900x%20DataSheet%20V1.2.pdf
- **SATCOM:** Iridium Certus 9770 https://www.iridium.com/products/iridium-certus-9770 · Certus 100 https://www.groundcontrol.com/products/iridium/iridium-certus-100-range/iridium-certus-100-plans/ · Inmarsat SB-UAV https://www.inmarsatgov.com/mission/applications/uas/
- **GCS:** Embention Veronte Control Stations https://www.embention.com/veronte/control-stations/ · Auterion Mission Control https://auterion.com/product/mission-control/ · QGroundControl https://qgroundcontrol.com/
