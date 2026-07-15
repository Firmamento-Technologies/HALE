# Fase B — Telemetria, Data Link e Stazione di Terra (GCS)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio preliminare di **telemetria, collegamento di comando/controllo (C2), downlink del payload e stazione di terra (GCS)** per operazioni BVLOS in Italia. |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Perimetro** | **Solo** telemetria e link/GCS. L'avionica di bordo è in `Avionica ed Elettronica di Bordo`; i sensori di missione in `Componenti di Payload per Applicazione`. |
| **Impostazione** | Tecnica + normativa (spettro, SORA). Considerato il **budget cap**: qui la voce critica è l'**OPEX del SATCOM**, non solo il CAPEX delle radio. |

> ⚠️ **Onestà tecnica:** i fatti su spettro UE, SORA, Remote ID e legalità delle bande sono ben corroborati (fonti in §7). Alcune cifre di targa delle singole radio (peso/prezzo di SkyLink 5060, Silvus, MPU5) vengono da snippet di datasheet fornitore → **da confermare a datasheet** prima di usarle come numeri "duri".

---

## Sigle usate in questo documento

*Le sigle comuni — **ENAC, EASA, SORA, ConOps, SAIL, OSO, BVLOS, C2, U-space, Remote ID, MANET** — sono spiegate nel Glossario della `Guida ENAC-SORA`. Qui sotto solo quelle proprie di telemetria e link.*

| Sigla | Significato | In parole semplici |
|---|---|---|
| **GCS** | *Ground Control Station* | La **stazione di terra**: computer, software, radio e antenne con cui si pilota e si monitora il drone. |
| **GDT** | *Ground Data Terminal* | La **radio della GCS**, cioè il terminale radio a terra del link C2. |
| **C2** | *Command & Control link* | Il **collegamento radio** che porta i comandi al drone e la telemetria a terra. |
| **CNPC** | *Control and Non-Payload Communications* | Tutto il traffico radio "di pilotaggio" (comando + telemetria), **escluso** il video/dati del payload. |
| **LOS / BLOS** | *Line of Sight / Beyond LOS* | Link **in vista diretta** dell'antenna / link **oltre l'orizzonte** (che deve passare per un satellite). |
| **SATCOM** | *Satellite Communications* | Collegamento **via satellite**, l'unico modo di mantenere il C2 quando il drone è oltre l'orizzonte. |
| **MSS** | *Mobile Satellite Service* | Il **servizio satellitare mobile** (es. Iridium, Inmarsat) su cui viaggia il SATCOM. |
| **ISM / SRD** | *Industrial-Scientific-Medical / Short Range Devices* | Le **bande radio libere**, usabili **senza licenza** entro limiti di potenza (2,4 GHz, 5,8 GHz, 868 MHz). |
| **EIRP / e.r.p.** | *Equivalent Isotropically Radiated Power* / potenza efficace irradiata | Due modi di misurare la **potenza effettivamente emessa** dall'antenna: sono i tetti da rispettare per legge. |
| **RLP** | *Required C2 Link Performance* | Il **livello di prestazione del link C2** (raggio, latenza, continuità…) che il SORA chiede di dimostrare. |
| **RCP** | *Required Communication Performance* | Framework "gemello" dell'RLP, sul lato comunicazione. |
| **DRI** | *Direct Remote ID* | La "**targa elettronica**" che il drone trasmette localmente (Wi-Fi/Bluetooth) a chi è nei paraggi. |
| **NRI** | *Network Remote ID* | La stessa identità/telemetria ma **pubblicata in rete**, richiesta solo dentro uno U-space. |
| **SWaP** | *Size, Weight and Power* | **Ingombro, peso e consumo** di un apparato: il criterio con cui si sceglie l'hardware di bordo. |
| **COTS** | *Commercial Off-The-Shelf* | Prodotto **commerciale già pronto**, non sviluppato su misura. |
| **SKU (variante UE)** | *Stock Keeping Unit* | La **versione commerciale** di un prodotto: la stessa radio ha una SKU per l'UE (868 MHz) e una per gli USA (915 MHz). |
| **OPEX / CAPEX** | *Operating / Capital Expenditure* | **Costo ricorrente** (es. l'abbonamento SATCOM) vs **costo una-tantum** d'acquisto. |
| **MAVLink** | *Micro Air Vehicle Link* | Il **protocollo standard** di telemetria/comando usato da PX4/ArduPilot, QGroundControl e Mission Planner. |
| **AES-256 / CRC** | *Advanced Encryption Standard / Cyclic Redundancy Check* | **Cifratura** del link e **controllo d'integrità** dei dati (rileva i pacchetti corrotti). |
| **HMI** | *Human-Machine Interface* | L'**interfaccia uomo-macchina**: schermate e comandi con cui il pilota interagisce con la GCS. |

---

## Come sono richiamate le normative

Questo documento incrocia **quattro mondi normativi** (spettro, aviazione, standard di prodotto, export). Per evitare che le sigle compaiano "a sorpresa", ecco **chi emette cosa e dove morde** in questo studio. Ogni riferimento inline (es. *EN 300 328*, *Reg. 2019/945*, *OSO#06*) rientra in una di queste famiglie.

| Chi lo emette | Cosa regola | Riferimenti citati qui |
|---|---|---|
| **ITU / ICAO** (internazionale) | Allocazione **globale** dello spettro e bande aeronautiche protette | Banda C2 5030–5091 MHz (AM(R)S), WRC-2012 |
| **CEPT / ECC** (Europa, tecnico) | **Armonizzazione** dell'uso dello spettro in Europa | ECC Report 268, mandato **ECC-24-014**, **ERC 70-03** |
| **Commissione UE** (legislatore) | **Regolamenti** UE su droni e spettro (validi in Italia) | Reg. **2019/945** e **2019/947** (UAS), Reg. **2021/664** (U-space), Dec. 2019/1345 |
| **ETSI → norme EN** (prodotto) | **Limiti tecnici** degli apparati radio sotto la direttiva RED | **EN 300 328** (2,4 GHz), **EN 302 502** (5,8 GHz), **EN 300 220** (868 MHz) |
| **EASA** (autorità UE aviazione) | **Metodo di rischio** e obiettivi di sicurezza | **SORA 2.5** (ED Decision 2025/018/R), **OSO#06/#14/#15** |
| **JARUS** (gruppo tecnico) | Framework tecnici ripresi da EASA | **RLP / RCP** del C2 link |
| **ASD-STAN / EUROCAE** (standard di dettaglio) | Standard tecnici **richiamati** dai regolamenti UE | prEN **4709-002** (Remote ID), prEN 4709-001 / ED-325 (protezione link) |
| **ENAC** (autorità italiana) | **Applica** in Italia e autorizza la singola operazione | Autorizzazione operativa; scelta frequenze anti-interferenza |
| **MIMIT** (Italia) | **Autorizzazione generale** all'uso delle bande ISM/SRD | Nessuna licenza per apparato entro i limiti EN |
| **FAA / FCC / RTCA** (USA — **fuori UE**) | Quadro americano, **non** valido in Italia | TSO-C213a, DO-362A, FCC Part 88 (per uAvionix SkyLink) |
| **RTCA / EUROCAE** (assurance avionica) | Sviluppo di SW/HW critici | **DO-178C / DO-254** (GCS certificabile) |

> **Come leggere:** una banda o una radio è **usabile in Italia** solo se rispetta insieme (1) l'**allocazione** ITU/CEPT, (2) i **limiti EN** di potenza e (3) l'**autorizzazione generale** MIMIT. I riferimenti FAA/FCC/RTCA descrivono il caso **USA** e servono solo a spiegare perché certi prodotti **non** sono operabili qui.

---

## 0. Executive summary

1. **La banda C2 aeronautica 5030–5091 MHz oggi in UE non si può usare.** A livello internazionale (ITU/ICAO) è una banda protetta per il C2 dei droni, ma **in Europa non esiste ancora un accesso civile armonizzato**: il percorso è aperto (mandato CE→CEPT **ECC-24-014**, in corso, orizzonte pluriennale) ma non pronto. Gli apparati per questa banda (es. **uAvionix SkyLink**) sono soluzioni **USA/FAA, non operabili in Italia**. È il fatto normativo più importante del documento.
2. **In Italia si vola sulle bande libere (ISM/SRD):** **2,4 GHz**, **5,8 GHz** e **868 MHz**, in **autorizzazione generale** e senza licenza per apparato. Attenzione: **868 MHz, non 915 MHz** — la banda USA 902–928 MHz è **illegale in UE**. Ogni radio va comprata nella **variante UE** (es. **RFD868x**, non RFD900x).
3. **Architettura C2 raccomandata:** **link primario LOS a maglia (MANET mesh)** in banda UE (Doodle, Silvus o Persistent MPU5) **+ backup SATCOM Iridium Certus 100**. La ridondanza soddisfa la continuità richiesta dall'**OSO#06**, riduce il rischio di lost-link ed è la scelta più efficiente sull'OPEX (~€60–200/mese contro ~€1.000+/mese delle alternative ad alto rate).
4. **GCS: dimostratore su software open-source, prodotto BVLOS su stack certificabile.** Per R&D bastano **QGroundControl / Mission Planner**; per l'autorizzazione BVLOS ai SAIL alti serve uno stack **certificabile** (Embention **Veronte Pipe/PCS**, DO-178C/DO-254, oppure Auterion). La GCS è **parte del "UAS"** ai sensi dei Reg. 2019/945-947 → rientra nel perimetro SORA.
5. **Obblighi collegati:** **Remote ID diretto (DRI)** obbligatorio dal **1/1/2024**; **Network RID (NRI)** solo se si opera dentro uno **U-space**; comportamento di **lost-link deterministico** sotto OSO#14/#15.

---

## 1. Spettro e normativa

### 1.1 Banda C2 aeronautica 5030–5091 MHz — perché in UE non è un'opzione (2026)

- **A livello internazionale è la banda "giusta".** La 5030–5091 MHz è allocata AM(R)S/AMS(R)S e identificata da ITU (WRC-2012) e ICAO come spettro **protetto** per il comando e controllo dei droni.
- **In Europa, però, non è ancora aperta al civile.** Il lavoro CEPT (ECC Report 268, 2018) ha armonizzato lo spettro droni per le categorie **Open e Specific**, ma **non** questa banda, che resta orientata alla categoria **Certified**. Non esiste una ECC Decision che dia accesso civile armonizzato, né un percorso di licenza pronto in Italia.
- **È in corso un percorso.** La Commissione UE ha dato **mandato alla CEPT (ECC-24-014, 2024)** per definire le condizioni tecniche. Va trattata come **capacità futura pluriennale**, non come opzione 2026.
- **Conseguenza pratica.** **uAvionix SkyLink** (5030–5091 MHz) è certificabile solo in **contesto USA** (bozza TSO-C213a, RTCA DO-362A, FCC Part 88, ago 2024). In UE **non è operabile**, perché lo spettro non è rilasciato al civile.

### 1.2 Bande libere ISM/SRD — è su queste che si vola in Italia oggi

| Banda | Norma di prodotto | Limite di potenza (UE) | Licenza in Italia | Uso tipico |
|---|---|---|---|---|
| **2,4 GHz** (2400–2483,5) | EN 300 328 | 100 mW EIRP | **No** (autorizzazione generale) | C2 + video, la più diffusa; ma congestionata |
| **5,8 GHz** (5725–5875) | EN 302 502 | ~25 mW–1 W EIRP secondo sotto-banda | **No** | downlink video + C2 secondario; più banda, meno raggio |
| **868 MHz** (863–870 SRD) | EN 300 220 | ~25 mW e.r.p. (alcune sotto-bande 500 mW con duty cycle) | **No** | telemetria a lungo raggio e basso rate; **non 915** |

> ⚠️ **868 UE, non 915 USA.** La banda 902–928 MHz ("915") **non è legale in UE**. Ogni radio va nella variante **UE/868** (**RFD868x** non RFD900x; SKU UE anche per Doodle, Silvus, Microhard). Comprare la variante 915 per operare in Italia è un errore **illegale** ricorrente.

**Il caso Italia.** L'uso delle bande ISM/SRD è in **autorizzazione generale** (MIMIT): nessuna licenza per apparato, purché l'equipaggiamento sia **CE/RED** e rientri nei limiti delle norme EN. In più, in sede di autorizzazione operativa, l'**ENAC** chiede che il data link usi frequenze scelte **per minimizzare le interferenze** che possano compromettere la sicurezza. L'onere quindi non è ottenere una licenza di spettro, ma **giustificare la robustezza del link nel SORA**.

### 1.3 SATCOM per il volo oltre l'orizzonte (BLOS)

Quando il drone esce dalla portata LOS/mesh, il C2 può proseguire solo via satellite: **Iridium Certus** (banda L, copertura globale) o **Inmarsat/Viasat SwiftBroadband** (banda L) — dettagli in §3. La licenza di spettro è del **provider di airtime**, quindi in Italia non serve alcuna licenza all'operatore. Il costo, però, è una **voce OPEX ricorrente**.

### 1.4 Prestazione del link C2 (RLP) nel SORA

- Il metodo di rischio di riferimento è **SORA 2.5**, adottato da EASA con ED Decision 2025/018/R (sostituisce la 2.0).
- L'integrità del C2 si dimostra sotto l'**OSO#06 ("C2 Link")**: vanno descritti e analizzati **copertura/raggio, latenza, continuità, disponibilità, integrità e protezione** del collegamento.
- Il framework quantitativo è l'**RLP (Required C2 Link Performance)**, di JARUS. Benchmark: per **SAIL III**, latenza del comando **≤ 5 s nel 99% del tempo**; ai SAIL più alti i requisiti si stringono.
- **Integrità e sicurezza:** controllo d'integrità con **CRC** (es. CRC-32); protezione del link secondo **ASD-STAN prEN 4709-001 / EUROCAE ED-325**. Ai SAIL alti è attesa la **protezione crittografica**.

### 1.5 Remote ID (DRI e NRI)

- **DRI (Direct Remote ID)** — obbligatorio dal **1/1/2024** (Reg. 2019/945). Il drone trasmette **localmente** (Wi-Fi/Bluetooth) ID operatore, propria posizione e posizione del pilota. Standard **ASD-STAN prEN 4709-002**. Non richiede infrastruttura a terra.
- **NRI (Network Remote ID)** — richiesto **solo dentro uno U-space** (Reg. 2021/664): ID e telemetria pubblicati in rete per tutta la durata del volo. È cosa distinta sia dal DRI sia dal C2.
- **Per un BVLOS Specific:** **DRI di serie** a bordo, **più** la capacità NRI se si opera in un volume U-space.

### 1.6 Lost-link (perdita del C2)

- Nel SORA la gestione della perdita del C2 ricade sotto **OSO#14** (procedure di contingenza) e **OSO#15** (risposta all'emergenza); la dimostrazione tecnica del link resta sotto l'OSO#06.
- Requisito: comportamento di lost-link **predefinito e deterministico** (hold → rientro nel volume operativo → atterraggio, oppure terminazione), che tenga il velivolo **dentro il volume operativo** e il relativo buffer di rischio a terra.
- È il motivo per cui, nel BVLOS, i **link ridondanti (LOS mesh + backup SATCOM)** convengono: riducono la probabilità di lost-link e **rendono più facile l'argomento OSO#06**, con effetto favorevole sul SAIL.

---

## 2. Radio C2 / mesh (COTS)

> **Caveat legalità UE (trasversale):** in Italia sono libere solo 2,4 GHz (100 mW EIRP), le sotto-bande 5,8 GHz e 868 MHz. Molte di queste radio si vendono con **potenze/bande USA** (915 MHz, alta potenza, bande militari L/S) **non** esenti in UE → serve la **SKU UE** e spesso un'autorizzazione individuale/sperimentale.

| Radio | Banda(e) | Raggio LOS | Throughput | TX | Peso | Note UE |
|---|---|---|---|---|---|---|
| **uAvionix SkyLink 5060 / micro** (+ **skyStation** a terra) | 5030–5091 (protetta) | C2 BVLOS | solo C2/CNPC (comando, non video) | 10 W / 100 mW | micro ~decine di g | **banda non civile in UE (§1.1)**; certificabile in USA |
| **Silvus StreamCaster SC4200 EP** | 300 MHz–6 GHz sintonizzabile | ~100+ km con relay | fino a **100 Mbps** | 1 mW–10 W (20 W EIRP beamforming) | modulo low-SWaP | **AES-256**; scegliere **SKU UE**; IP68 · ~$8–15k+/nodo |
| **Persistent MPU5 (Wave Relay)** | moduli 2,4 GHz / L / S / C | fino a ~130 mi con antenna direttiva | alto (video/dati/voce) | 6–10 W | **~391 g** | MANET auto-riparante; **EAR/ITAR**; serve modulo UE · ~$10–15k+ |
| **Doodle Labs Mesh Rider (Nano/Mini/OEM)** | sub-GHz + 2,4 + 6 GHz; **SKU UE 868/2,4** | multi-km, mesh | decine di Mbps | ~1,6 W (32 dBm) | **25 / 34 / 102 g** | **miglior rapporto low-SWaP**; specificare variante UE · ~$1,5–3k |
| **Microhard pMDDL2450** | 2,4 GHz 2×2 MIMO | multi-km | fino a 25 Mbps | fino a 1 W | decine di g | 2,4 GHz esente UE a 100 mW EIRP · ~$300–900 |
| **Trellisware TW-950** | 225–2600 MHz (militari) | tattico multi-hop | fino a 16 Mbps | 100 mW–2 W | **~320 g** | bande militari → **uso civile UE molto vincolato** · ~$10k+ |
| **RFD868x** (telemetria, non mesh) | **863–870 (UE)** | fino a **40 km+** | fino a 500 kbps | fino a 1 W | **14 g** | **la variante da usare in Italia**; MAVLink classico · ~$200–300/coppia |

> **Scelta baseline:** C2 primario **MANET mesh in banda UE** (Doodle low-SWaP per il dimostratore leggero; Silvus o MPU5 per capacità/portata), **telemetria MAVLink su RFD868x** come canale semplice, **backup SATCOM** (§3). Il video del payload viaggia sul mesh o su 5,8 GHz.

---

## 3. SATCOM per il BLOS (la voce OPEX)

| Sistema | Data rate | Peso | Potenza | Airtime (OPEX indicativo) | Note |
|---|---|---|---|---|---|
| **Iridium Certus 9770** (transceiver) | 22 kbps up / 88 kbps down | **185 g** | ~5 W | dipende dal piano | globale (poli inclusi); SWaP ideale per C2/backup |
| **Iridium Certus 100** (servizio) ★ | 22/88 kbps | terminale piccolo | bassa | **~$62–580/mese** (0–100 MB) | giusto per il **backup C2** (comando/telemetria a basso rate) |
| **Iridium Certus 700** | fino a 700 kbps | maggiore | maggiore | da ~$79/mese in su | rate alto; antenna più pesante |
| **Inmarsat/Viasat SwiftBroadband SB-UAV** | 200–432 kbps (fino a ~650) | banda L, low-SWaP | media | **~$4–6/MB, ~$1.000+/mese** | C2 BLOS dedicato; banda L (esclusi i poli) |

> **Impatto sul budget cap:** il SATCOM è l'**OPEX dominante**. Se serve **solo come backup C2** (comando/telemetria a basso rate, non video), **Iridium Certus 100** (~€60–200/mese) è la scelta razionale; SwiftBroadband/Certus 700 (~€1.000+/mese) solo se serve BLOS ad alto rate. Va modellato come **linea mensile per velivolo**, non come costo una-tantum.

---

## 4. Stazione di terra (GCS)

### 4.1 Blocchi hardware

- **Unità di controllo ruggedizzata:** laptop/tablet MIL-STD-810/IP (classe Getac/Toughbook) con il software GCS.
- **Ground Data Terminal (GDT):** la radio C2 lato terra — **uAvionix skyStation** (IP67, PoE, backhaul LTE) nel caso banda C, oppure il nodo a terra del mesh scelto (Silvus/MPU5/Doodle) per il LOS.
- **Antenna direzionale / tracking:** antenna auto-tracking pan-tilt o **palo elevato** (es. Embention Veronte PCS, palo 3 m) per estendere il raggio LOS e migliorare il margine di link (argomento RLP).
- **Radiocomando manuale:** trasmettitore dedicato per **decollo/atterraggio e override manuale** (safety pilot), separato dal link BVLOS autonomo — spesso richiesto nel ConOps SORA per le fasi di lancio e recupero.
- **Ridondanza:** **link primario LOS mesh + backup SATCOM** (Iridium Certus 100) → sostiene la continuità dell'OSO#06 e riduce il lost-link (§1.6).

### 4.2 Software — dimostratore vs certificabile (la distinzione chiave)

| Livello | Prodotti | Ruolo | Postura di certificazione |
|---|---|---|---|
| **Open-source / dimostratore** | **QGroundControl**, **Mission Planner** (MAVLink; PX4/ArduPilot) | controllo volo, pianificazione, telemetria; ottimi per R&D e BVLOS dimostrativo | **Non certificati.** Accettabili in Specific se il SORA argomenta l'integrità di sistema, ma **senza DO-178C** → più difficili ai SAIL alti |
| **Prodotto / certificabile** | **Embention Veronte Pipe** (SW) + **Veronte PCS** (HW, **DO-178C/DO-254 certificabile**); **Auterion Mission Control**; **UgCS** | stesse funzioni + assurance di sviluppo, configuration control ed evidenze per gli OSO | **Veronte** è esplicitamente **DO-178C/DO-254 certificabile** → miglior fit per BVLOS SAIL III+ |

> **Logica:** **QGroundControl/Mission Planner nel dimostratore** (rapidi, MAVLink-nativi, licenza zero); per l'autorizzazione **BVLOS SAIL III+** si migra a uno **stack certificabile** (Veronte Pipe/PCS o Auterion), così l'**OSO#06** e gli OSO di software-assurance sono difendibili con **evidenza del fornitore**, non auto-dichiarati. Coerente con la scelta autopilota di `Avionica ed Elettronica di Bordo` §2.

### 4.3 Ruolo normativo della GCS

In Specific/BVLOS la **GCS è parte del "UAS"** (Reg. 2019/945-947: *UAS* = aeromobile **più** l'equipaggiamento per controllarlo da remoto). Quindi la GCS — hardware, software, antenna, link — è **dentro il perimetro SORA**: affidabilità, HMI, lost-link e prestazione C2 vengono **valutati**, non trattati come accessori. La ridondanza (primario LOS mesh + backup SATCOM) e un **percorso di override manuale** chiaro sono le leve pratiche per il contenimento e per l'OSO#06.

---

## 5. Sintesi e budget cap

| Elemento | Scelta baseline | Impatto sul budget |
|---|---|---|
| C2 primario | MANET mesh **banda UE** (Doodle → Silvus/MPU5) | CAPEX ~€1,5–15k/nodo (×2: bordo + terra) |
| Telemetria | **RFD868x** MAVLink | CAPEX ~€200–300 |
| Backup BLOS | **Iridium Certus 100** | **OPEX ~€60–200/mese** (dominante) |
| Remote ID | **DRI** a bordo (+ NRI se U-space) | CAPEX basso |
| GCS software | QGC/Mission Planner → **Veronte Pipe/Auterion** | licenza zero (demo) → quote (prodotto) |
| GCS hardware | unità rugged + antenna tracking + RC manuale | CAPEX medio |

> **Consuntivo cap:** il CAPEX del link è modesto; i veri driver economici sono l'**OPEX SATCOM** (per velivolo, mensile) e il **CAPEX della migrazione a stack certificabile** per il BVLOS. Entrambi vanno riflessi in `WP-B5`.

---

## 6. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Cifre esatte SkyLink/Silvus/MPU5 (da snippet) | Richiedere datasheet e RFQ diretti |
| Scelta banda/potenza per il SORA specifico | Link budget + giustificazione RLP nel ConOps |
| Evoluzione della 5030–5091 in UE | Monitorare il mandato CEPT **ECC-24-014** (capacità futura) |
| Autorizzazione individuale per radio non-esenti | Verifica con MIMIT se si usano bande/potenze fuori ISM |
| Integrazione DRI/NRI e U-space | Verifica dei volumi U-space applicabili (San Salvo e futuri) |

---

*Analisi first-order, adeguata allo stadio di fattibilità. Fatti normativi/spettro corroborati; alcune cifre radio da confermare a datasheet. Baseline: **C2 MANET mesh in banda UE + backup Iridium Certus 100**, telemetria **RFD868x**, **DRI** obbligatorio, GCS **dimostratore→certificabile**. Vincolo chiave: la **banda C2 5030–5091 MHz non è un'opzione UE nel 2026**.*

## 7. Fonti principali

- **Spettro/normativa:** FCC 5030–5091 (ago 2024) https://www.fcc.gov/document/fcc-report-supports-use-5030-5091-mhz-band-uas-operations · ECC Report 268 https://www.bakom.admin.ch/dam/bakom/de/dokumente/frequenzen/Drohnen/ecc_report_268.pdf.download.pdf/ECC_Report_268.pdf · mandato CE→CEPT ECC-24-014 https://cept.org/documents/ecc/81470/ecc-24-014_mandate-to-the-cept-on-uas · ERC 70-03 https://docdb.cept.org/download/3700 · Impl. Decision (UE) 2019/1345 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32019D1345 · ENAC UAS https://www.enac.gov.it/en/safety-security/uas-drones
- **SORA/RLP:** EASA ED Decision 2025/018/R (SORA 2.5) https://www.easa.europa.eu/en/document-library/agency-decisions/ed-decision-2025018r · EASA MOC OSO#6 (SAIL III) https://www.easa.europa.eu/en/downloads/139100/en · JARUS C2 Link RCP/RLP http://jarus-rpas.org/wp-content/uploads/2023/06/jar_02_doc_rpas_c2_link_rcp.pdf
- **Remote ID:** EASA https://www.easa.europa.eu/en/document-library/general-publications/remote-identification-will-become-mandatory-drones-across · ASD-STAN DRI https://cms.stan-shop.org/uploads/2024/01/ASD-STAN_DRI_Introduction_to_the_European_digital_RID_UAS_Standard.pdf
- **Radio:** uAvionix skyStation https://uavionix.com/uncrewed-aircraft-systems/skystation/ · Silvus SC4200 https://silvustechnologies.com/products/streamcaster-radios/ · Persistent MPU5 https://persistentsystems.com/mpu5-specs/ · Doodle Labs https://doodlelabs.com/products/ · Microhard pMDDL2450 https://www.microhardcorp.com/pMDDL2450.php · RFD900x/868x https://files.rfdesign.com.au/Files/documents/RFD900x%20DataSheet%20V1.2.pdf
- **SATCOM:** Iridium Certus 9770 https://www.iridium.com/products/iridium-certus-9770 · Certus 100 https://www.groundcontrol.com/products/iridium/iridium-certus-100-range/iridium-certus-100-plans/ · Inmarsat SB-UAV https://www.inmarsatgov.com/mission/applications/uas/
- **GCS:** Embention Veronte Control Stations https://www.embention.com/veronte/control-stations/ · Auterion Mission Control https://auterion.com/product/mission-control/ · QGroundControl https://qgroundcontrol.com/
