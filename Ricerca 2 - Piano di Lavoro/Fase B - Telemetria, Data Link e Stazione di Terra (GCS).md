# Fase B — Telemetria, Data Link e Stazione di Terra (GCS)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Studio preliminare di **telemetria, collegamento di comando/controllo (C2), downlink del payload e stazione di terra (GCS)** per operazioni BVLOS **in Italia (quadro UE)**. |
| **Versione** | 0.2 — bozza tecnica (revisione EU-only + processo per stadi) |
| **Data** | 2026-07-15 |
| **Perimetro** | **Solo** telemetria e link/GCS. L'avionica di bordo è in `Avionica ed Elettronica di Bordo`; i sensori di missione in `Componenti di Payload per Applicazione`. |
| **Ambito normativo** | **Esclusivamente UE/Italia.** Bande, potenze e prodotti non utilizzabili nell'UE civile (banda 915 MHz USA, bande militari, apparati in banda protetta non ancora aperta) sono **esclusi dall'analisi**, non solo sconsigliati. |
| **Impostazione** | Tecnica + normativa (spettro, SORA). L'analisi è organizzata come **processo per stadi** (§2): **(1) legale senza autorizzazioni → (2) legale con autorizzazione → (3) legale e certificabile**. Considerato il **budget cap**: la voce critica è l'**OPEX del SATCOM**, non il CAPEX delle radio. |

> ⚠️ **Onestà tecnica:** i fatti su spettro UE, SORA, Remote ID e legalità delle bande sono ben corroborati (fonti in §8). Alcune cifre di targa delle radio UE (peso/prezzo di Silvus, Doodle) vengono da snippet di datasheet fornitore → **da confermare a datasheet** prima di usarle come numeri "duri".

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
| **SKU (variante UE)** | *Stock Keeping Unit* | La **versione commerciale** di un prodotto: la stessa radio ha una SKU per l'UE (868 MHz) e una per gli USA (915 MHz) — a noi serve **solo** quella UE. |
| **OPEX / CAPEX** | *Operating / Capital Expenditure* | **Costo ricorrente** (es. l'abbonamento SATCOM) vs **costo una-tantum** d'acquisto. |
| **MAVLink** | *Micro Air Vehicle Link* | Il **protocollo standard** di telemetria/comando usato da PX4/ArduPilot, QGroundControl e Mission Planner. |
| **AES-256 / CRC** | *Advanced Encryption Standard / Cyclic Redundancy Check* | **Cifratura** del link e **controllo d'integrità** dei dati (rileva i pacchetti corrotti). |
| **OSNMA** | *Open Service Navigation Message Authentication* | L'**autenticazione anti-spoofing** del segnale Galileo (europeo): certifica che il GNSS non sia falsificato. |
| **HMI** | *Human-Machine Interface* | L'**interfaccia uomo-macchina**: schermate e comandi con cui il pilota interagisce con la GCS. |

---

## Come sono richiamate le normative

Questo documento incrocia **tre mondi normativi UE** (spettro, aviazione, standard di prodotto). Per evitare che le sigle compaiano "a sorpresa", ecco **chi emette cosa e dove morde** in questo studio. Ogni riferimento inline (es. *EN 300 328*, *Reg. 2019/945*, *OSO#06*) rientra in una di queste famiglie.

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
| **MIMIT** (Italia) | **Autorizzazione** all'uso dello spettro (generale o individuale) | Autorizzazione generale per ISM/SRD; individuale/sperimentale oltre i limiti |
| **RTCA / EUROCAE** (assurance avionica) | Sviluppo di software/hardware critici | **DO-178C / DO-254** (GCS certificabile) |

> **Come leggere:** una banda o una radio è **usabile in Italia** solo se rispetta insieme (1) l'**allocazione** ITU/CEPT, (2) i **limiti EN** di potenza e (3) l'**autorizzazione** MIMIT (generale o, oltre i limiti ISM, individuale). Il quadro USA (FCC/FAA/RTCA-DO-362A/TSO) **non vale in UE** ed è citato una sola volta (§1.4), solo per spiegare perché la banda 5030–5091 MHz non è ancora un'opzione europea.

---

## 0. Executive summary

1. **In Italia si vola sulle bande libere (ISM/SRD):** **2,4 GHz**, **5,8 GHz** e **868 MHz**, in **autorizzazione generale** e senza licenza per apparato. Regola d'oro: **868 MHz, non 915 MHz** — la banda USA 902–928 MHz è illegale in UE. Ogni radio va comprata nella **variante UE** (es. **RFD868x**, non RFD900x).
2. **La telemetria si affronta come processo per stadi** (§2), adottando il livello minimo che l'operazione richiede e salendo solo quando SAIL, portata o committente lo impongono:
   - **Stadio 1 — legale senza autorizzazioni:** solo bande ISM/SRD entro i limiti EN. Copre dimostratore e BVLOS a SAIL basso in LOS.
   - **Stadio 2 — legale con autorizzazione:** potenze/bande oltre l'ISM (autorizzazione individuale MIMIT) e/o **SATCOM** per il BLOS (legale via airtime del provider). Estende raggio e continuità.
   - **Stadio 3 — legale e certificabile:** link **cifrato (AES-256)** e **integro (CRC)**, navigazione **anti-spoofing (Galileo OSNMA)**, **RLP dimostrato** e stack GCS **DO-178C/254**. Richiesto ai SAIL alti (III+) e ai committenti istituzionali.
3. **Architettura raccomandata (baseline):** **link primario LOS a maglia (MANET mesh)** in banda UE (Doodle → Silvus) **+ telemetria MAVLink su RFD868x + backup SATCOM Iridium Certus 100**. La ridondanza soddisfa la continuità dell'**OSO#06**, riduce il lost-link ed è la scelta più efficiente sull'OPEX (~€60–200/mese contro ~€1.000+/mese delle alternative ad alto rate).
4. **GCS: dimostratore su software open-source, prodotto BVLOS su stack certificabile.** Per R&D bastano **QGroundControl / Mission Planner**; ai SAIL alti serve uno stack **certificabile** (Embention **Veronte Pipe/PCS**, DO-178C/254, oppure Auterion). La GCS è **parte del "UAS"** (Reg. 2019/945-947) → rientra nel perimetro SORA.
5. **Obblighi collegati:** **Remote ID diretto (DRI)** obbligatorio dal **1/1/2024**; **Network RID (NRI)** solo dentro uno **U-space**; comportamento di **lost-link deterministico** sotto OSO#14/#15.

---

## 1. Spettro e normativa (UE/Italia)

### 1.1 Bande libere ISM/SRD — è su queste che si vola in Italia oggi

| Banda | Norma di prodotto | Limite di potenza (UE) | Licenza in Italia | Uso tipico |
|---|---|---|---|---|
| **2,4 GHz** (2400–2483,5) | EN 300 328 | 100 mW EIRP | **No** (autorizzazione generale) | C2 + video, la più diffusa; ma congestionata |
| **5,8 GHz** (5725–5875) | EN 302 502 | ~25 mW–1 W EIRP secondo sotto-banda | **No** | downlink video + C2 secondario; più banda, meno raggio |
| **868 MHz** (863–870 SRD) | EN 300 220 | ~25 mW e.r.p. (alcune sotto-bande 500 mW con duty cycle) | **No** | telemetria a lungo raggio e basso rate; **non 915** |

> ⚠️ **868 UE, non 915 USA.** La banda 902–928 MHz ("915") **non è legale in UE**. Ogni radio va nella variante **UE/868** (**RFD868x** non RFD900x; SKU UE anche per Doodle e Silvus). Comprare la variante 915 per operare in Italia è un errore **illegale** ricorrente.

**Il caso Italia.** L'uso delle bande ISM/SRD è in **autorizzazione generale** (MIMIT): nessuna licenza per apparato, purché l'equipaggiamento sia **CE/RED** e rientri nei limiti delle norme EN. In più, in sede di autorizzazione operativa, l'**ENAC** chiede che il data link usi frequenze scelte **per minimizzare le interferenze** che possano compromettere la sicurezza. L'onere quindi non è ottenere una licenza di spettro, ma **giustificare la robustezza del link nel SORA**.

### 1.2 Oltre le bande libere — l'autorizzazione individuale (MIMIT)

Se servono **potenze o bande fuori dai limiti ISM** (per estendere il raggio o usare radio ad alta capacità), l'uso non è più coperto dall'autorizzazione generale: serve un'**autorizzazione individuale/sperimentale** presso il MIMIT per lo specifico apparato e la specifica frequenza. È il passaggio che segna il confine tra **Stadio 1 e Stadio 2** (§2).

### 1.3 SATCOM per il volo oltre l'orizzonte (BLOS)

Quando il drone esce dalla portata LOS/mesh, il C2 può proseguire solo via satellite: **Iridium Certus** (banda L, copertura globale) o **Inmarsat/Viasat SwiftBroadband** (banda L) — dettagli in §4. La licenza di spettro MSS è del **provider di airtime**, quindi in Italia non serve alcuna licenza all'operatore. Il costo, però, è una **voce OPEX ricorrente** (Stadio 2).

### 1.4 La banda C2 aeronautica 5030–5091 MHz — capacità futura, non opzione 2026

A livello internazionale (ITU WRC-2012, ICAO) la 5030–5091 MHz è la banda **protetta** dedicata al C2 dei droni. **In Europa, però, non è ancora aperta al civile:** il lavoro CEPT (ECC Report 268, 2018) ha armonizzato lo spettro droni per Open e Specific ma **non** questa banda, e non esiste una ECC Decision che ne dia accesso civile. La Commissione UE ha dato **mandato alla CEPT (ECC-24-014, 2024)** per definire le condizioni tecniche: va trattata come **capacità futura pluriennale**. Gli apparati che la usano oggi sono soluzioni certificate **solo negli USA** (quadro FCC/FAA), **non operabili in Italia**: per questo **non entrano nell'analisi** dei prodotti (§3).

### 1.5 Prestazione del link C2 (RLP) nel SORA

- Il metodo di rischio di riferimento è **SORA 2.5**, adottato da EASA con ED Decision 2025/018/R (sostituisce la 2.0).
- L'integrità del C2 si dimostra sotto l'**OSO#06 ("C2 Link")**: vanno descritti e analizzati **copertura/raggio, latenza, continuità, disponibilità, integrità e protezione** del collegamento.
- Il framework quantitativo è l'**RLP (Required C2 Link Performance)**, di JARUS. Benchmark: per **SAIL III**, latenza del comando **≤ 5 s nel 99% del tempo**; ai SAIL più alti i requisiti si stringono.
- **Integrità e sicurezza:** controllo d'integrità con **CRC** (es. CRC-32); protezione del link secondo **ASD-STAN prEN 4709-001 / EUROCAE ED-325**. Ai SAIL alti è attesa la **protezione crittografica** (Stadio 3).

### 1.6 Remote ID (DRI e NRI)

- **DRI (Direct Remote ID)** — obbligatorio dal **1/1/2024** (Reg. 2019/945). Il drone trasmette **localmente** (Wi-Fi/Bluetooth) ID operatore, propria posizione e posizione del pilota. Standard **ASD-STAN prEN 4709-002**. Non richiede infrastruttura a terra.
- **NRI (Network Remote ID)** — richiesto **solo dentro uno U-space** (Reg. 2021/664): ID e telemetria pubblicati in rete per tutta la durata del volo. È cosa distinta sia dal DRI sia dal C2.
- **Per un BVLOS Specific:** **DRI di serie** a bordo, **più** la capacità NRI se si opera in un volume U-space.

### 1.7 Lost-link (perdita del C2)

- Nel SORA la gestione della perdita del C2 ricade sotto **OSO#14** (procedure di contingenza) e **OSO#15** (risposta all'emergenza); la dimostrazione tecnica del link resta sotto l'OSO#06.
- Requisito: comportamento di lost-link **predefinito e deterministico** (hold → rientro nel volume operativo → atterraggio, oppure terminazione), che tenga il velivolo **dentro il volume operativo** e il relativo buffer di rischio a terra.
- È il motivo per cui, nel BVLOS, i **link ridondanti (LOS mesh + backup SATCOM)** convengono: riducono la probabilità di lost-link e **rendono più facile l'argomento OSO#06**, con effetto favorevole sul SAIL.

---

## 2. Il processo per stadi (la spina dorsale del documento)

La telemetria/link non è una scelta unica, ma un **percorso**: si adotta il **livello minimo** che l'operazione richiede e si sale di stadio **solo** quando SAIL, portata o committente lo impongono. **Tutti e tre gli stadi sono pienamente legali in Italia**; cambia solo l'onere normativo e il costo. Gli stadi sono **cumulativi** (lo Stadio 3 comprende e rafforza il 2 e l'1).

| Stadio | Cosa lo definisce | Onere normativo | Hardware/tecnologia tipica | Quando serve |
|---|---|---|---|---|
| **1 — Legale senza autorizzazioni** | Solo bande **ISM/SRD** entro i limiti EN (2,4 GHz 100 mW EIRP; 5,8 GHz; 868 MHz) | **Autorizzazione generale** MIMIT (nessuna licenza per apparato); equipaggiamento **CE/RED** | **RFD868x** (telemetria MAVLink), **Doodle**/**Microhard** mesh 2,4 GHz, video 5,8 GHz | Dimostratore e primi BVLOS a **SAIL basso**, raggio in LOS |
| **2 — Legale con autorizzazione** | Potenze/bande **oltre l'ISM**, oppure **BLOS satellitare** | **Autorizzazione individuale/sperimentale** MIMIT per lo spettro; SATCOM legale via **airtime del provider** (nessuna licenza operatore) | **Silvus** SKU UE (potenza/beamforming, ~100 km con relay); **SATCOM Iridium Certus 100** come backup C2 | Raggio esteso, **continuità/disponibilità (OSO#06)**, volo oltre l'orizzonte |
| **3 — Legale e certificabile** | Link **protetto e dimostrabile** ai SAIL alti | **RLP** dimostrato (OSO#06); protezione link **prEN 4709-001 / ED-325**; stack SW/HW **DO-178C/254** | **Cifratura AES-256** sul link, **integrità CRC-32**, **GNSS anti-spoofing Galileo OSNMA** (→ `Avionica`), **GCS Veronte Pipe/PCS** certificabile | **BVLOS SAIL III+** e committenti istituzionali/difesa |

> **Logica.** Lo **Stadio 1** basta per volare e dimostrare **subito**, senza pratiche di spettro. Lo **Stadio 2** si apre solo quando la missione chiede più portata o il volo oltre l'orizzonte: l'onere aggiuntivo è un'autorizzazione individuale MIMIT e/o l'abbonamento SATCOM (l'OPEX dominante). Lo **Stadio 3** è la postura da **prodotto certificato**: non aggiunge tanto hardware quanto **assurance ed evidenze** (cifratura, integrità, anti-spoofing, RLP, DO-178C/254) — è ciò che rende difendibile l'OSO#06 con prove del fornitore anziché auto-dichiarazioni.

---

## 3. Radio C2 / mesh utilizzabili in UE (COTS)

Elenco **filtrato all'utilizzabile in UE civile**: solo apparati con banda/potenza ammesse in Italia (2,4 GHz a 100 mW EIRP, sotto-bande 5,8 GHz, 868 MHz) **o** con SKU UE che, oltre i limiti ISM, sono percorribili via autorizzazione individuale (Stadio 2).

| Radio | Banda(e) UE | Raggio LOS | Throughput | Peso | Stadio | Note |
|---|---|---|---|---|---|---|
| **RFD868x** (telemetria, non mesh) | **863–870 (UE)** | fino a **40 km+** | fino a 500 kbps | **14 g** | 1 | **la variante da usare in Italia**; MAVLink classico · ~$200–300/coppia |
| **Microhard pMDDL2450** | 2,4 GHz 2×2 MIMO | multi-km | fino a 25 Mbps | decine di g | 1 | 2,4 GHz esente a 100 mW EIRP · ~$300–900 |
| **Doodle Labs Mesh Rider** (Nano/Mini/OEM) | **SKU UE 868 / 2,4** (+ 6 GHz) | multi-km, mesh | decine di Mbps | **25 / 34 / 102 g** | 1–2 | **miglior rapporto low-SWaP**; specificare variante UE · ~$1,5–3k |
| **Silvus StreamCaster SC4200 EP** | sintonizzabile, **SKU UE** | ~100+ km con relay | fino a **100 Mbps** | modulo low-SWaP | 2–3 | **AES-256** (→ Stadio 3), IP68; potenze elevate → **autorizzazione individuale** · ~$8–15k+/nodo |

> **Baseline consigliata.** C2 primario **MANET mesh in banda UE** (Doodle low-SWaP per il dimostratore; Silvus per capacità/portata), **telemetria MAVLink su RFD868x** come canale semplice, **backup SATCOM** (§4). Il video del payload viaggia sul mesh o su 5,8 GHz.
>
> **Escluse dall'analisi (non-UE):** apparati in banda **915 MHz/USA**, **bande militari** (es. Trellisware) e prodotti **ITAR in banda protetta** o soggetti a export USA — inclusi gli apparati per la 5030–5091 MHz, banda **non ancora aperta in UE** (§1.4). Non sono opzioni per questo progetto e non sono valutati.

---

## 4. SATCOM per il BLOS (Stadio 2 — la voce OPEX)

| Sistema | Data rate | Peso | Potenza | Airtime (OPEX indicativo) | Note |
|---|---|---|---|---|---|
| **Iridium Certus 9770** (transceiver) | 22 kbps up / 88 kbps down | **185 g** | ~5 W | dipende dal piano | globale (poli inclusi); SWaP ideale per C2/backup |
| **Iridium Certus 100** (servizio) ★ | 22/88 kbps | terminale piccolo | bassa | **~$62–580/mese** (0–100 MB) | giusto per il **backup C2** (comando/telemetria a basso rate) |
| **Iridium Certus 700** | fino a 700 kbps | maggiore | maggiore | da ~$79/mese in su | rate alto; antenna più pesante |
| **Inmarsat/Viasat SwiftBroadband SB-UAV** | 200–432 kbps (fino a ~650) | banda L, low-SWaP | media | **~$4–6/MB, ~$1.000+/mese** | C2 BLOS dedicato; banda L (esclusi i poli) |

> **Impatto sul budget cap:** il SATCOM è l'**OPEX dominante**. Se serve **solo come backup C2** (comando/telemetria a basso rate, non video), **Iridium Certus 100** (~€60–200/mese) è la scelta razionale; SwiftBroadband/Certus 700 (~€1.000+/mese) solo se serve BLOS ad alto rate. Va modellato come **linea mensile per velivolo**, non come costo una-tantum.

---

## 5. Stazione di terra (GCS)

### 5.1 Blocchi hardware

- **Unità di controllo ruggedizzata:** laptop/tablet MIL-STD-810/IP (classe Getac/Toughbook) con il software GCS.
- **Ground Data Terminal (GDT):** la radio C2 lato terra, cioè il nodo a terra del mesh scelto (Silvus/Doodle) per il LOS.
- **Antenna direzionale / tracking:** antenna auto-tracking pan-tilt o **palo elevato** (es. Embention Veronte PCS, palo 3 m) per estendere il raggio LOS e migliorare il margine di link (argomento RLP).
- **Radiocomando manuale:** trasmettitore dedicato per **decollo/atterraggio e override manuale** (safety pilot), separato dal link BVLOS autonomo — spesso richiesto nel ConOps SORA per le fasi di lancio e recupero.
- **Ridondanza:** **link primario LOS mesh + backup SATCOM** (Iridium Certus 100) → sostiene la continuità dell'OSO#06 e riduce il lost-link (§1.7).

### 5.2 Software — dimostratore vs certificabile (la distinzione chiave)

| Livello | Prodotti | Ruolo | Postura di certificazione | Stadio |
|---|---|---|---|---|
| **Open-source / dimostratore** | **QGroundControl**, **Mission Planner** (MAVLink; PX4/ArduPilot) | controllo volo, pianificazione, telemetria; ottimi per R&D e BVLOS dimostrativo | **Non certificati.** Accettabili in Specific se il SORA argomenta l'integrità di sistema, ma **senza DO-178C** → più difficili ai SAIL alti | 1–2 |
| **Prodotto / certificabile** | **Embention Veronte Pipe** (SW) + **Veronte PCS** (HW, **DO-178C/DO-254 certificabile**); **Auterion Mission Control**; **UgCS** | stesse funzioni + assurance di sviluppo, configuration control ed evidenze per gli OSO | **Veronte** è esplicitamente **DO-178C/DO-254 certificabile** → miglior fit per BVLOS SAIL III+ | 3 |

> **Logica:** **QGroundControl/Mission Planner nel dimostratore** (rapidi, MAVLink-nativi, licenza zero); per l'autorizzazione **BVLOS SAIL III+** si migra a uno **stack certificabile** (Veronte Pipe/PCS o Auterion), così l'**OSO#06** e gli OSO di software-assurance sono difendibili con **evidenza del fornitore**. Coerente con la scelta autopilota di `Avionica ed Elettronica di Bordo` §2.

### 5.3 Ruolo normativo della GCS

In Specific/BVLOS la **GCS è parte del "UAS"** (Reg. 2019/945-947: *UAS* = aeromobile **più** l'equipaggiamento per controllarlo da remoto). Quindi la GCS — hardware, software, antenna, link — è **dentro il perimetro SORA**: affidabilità, HMI, lost-link e prestazione C2 vengono **valutati**, non trattati come accessori. La ridondanza (primario LOS mesh + backup SATCOM) e un **percorso di override manuale** chiaro sono le leve pratiche per il contenimento e per l'OSO#06.

---

## 6. Sintesi e budget cap

| Elemento | Scelta baseline | Stadio | Impatto sul budget |
|---|---|---|---|
| Telemetria | **RFD868x** MAVLink | 1 | CAPEX ~€200–300 |
| C2 primario | MANET mesh **banda UE** (Doodle → Silvus) | 1 → 2 | CAPEX ~€1,5–15k/nodo (×2: bordo + terra) |
| Backup BLOS | **Iridium Certus 100** | 2 | **OPEX ~€60–200/mese** (dominante) |
| Remote ID | **DRI** a bordo (+ NRI se U-space) | 1 | CAPEX basso |
| Sicurezza link | **AES-256 + CRC-32 + OSNMA** | 3 | incluso nell'hardware certificabile |
| GCS software | QGC/Mission Planner → **Veronte Pipe/Auterion** | 1 → 3 | licenza zero (demo) → quote (prodotto) |
| GCS hardware | unità rugged + antenna tracking + RC manuale | 1 | CAPEX medio |

> **Consuntivo cap:** il CAPEX del link è modesto; i veri driver economici sono l'**OPEX SATCOM** (per velivolo, mensile — Stadio 2) e il **CAPEX della migrazione a stack certificabile** (Stadio 3). Entrambi vanno riflessi in `WP-B5`.

---

## 7. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Cifre esatte Silvus/Doodle (da snippet) | Richiedere datasheet e RFQ diretti |
| Confine Stadio 1 → Stadio 2 per il caso specifico | Link budget + verifica con MIMIT delle potenze/bande fuori ISM |
| Scelta banda/potenza per il SORA specifico | Link budget + giustificazione RLP nel ConOps |
| Requisiti Stadio 3 (cifratura, integrità, RLP) | Definire target RLP per il SAIL previsto; verificare prEN 4709-001/ED-325 |
| Evoluzione della 5030–5091 in UE | Monitorare il mandato CEPT **ECC-24-014** (capacità futura) |
| Integrazione DRI/NRI e U-space | Verifica dei volumi U-space applicabili (San Salvo e futuri) |

---

*Analisi first-order, adeguata allo stadio di fattibilità, **in ottica esclusivamente UE/Italia**. Fatti normativi/spettro corroborati; alcune cifre radio da confermare a datasheet. Baseline: **C2 MANET mesh in banda UE + telemetria RFD868x + backup Iridium Certus 100**, **DRI** obbligatorio, GCS **dimostratore→certificabile**, con un **percorso per stadi** (senza autorizzazioni → con autorizzazione → certificabile). Vincolo chiave: la **banda C2 5030–5091 MHz non è un'opzione UE nel 2026**.*

## 8. Fonti principali

- **Spettro/normativa UE:** ECC Report 268 https://www.bakom.admin.ch/dam/bakom/de/dokumente/frequenzen/Drohnen/ecc_report_268.pdf.download.pdf/ECC_Report_268.pdf · mandato CE→CEPT ECC-24-014 https://cept.org/documents/ecc/81470/ecc-24-014_mandate-to-the-cept-on-uas · ERC 70-03 https://docdb.cept.org/download/3700 · Impl. Decision (UE) 2019/1345 https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32019D1345 · ENAC UAS https://www.enac.gov.it/en/safety-security/uas-drones
- **SORA/RLP:** EASA ED Decision 2025/018/R (SORA 2.5) https://www.easa.europa.eu/en/document-library/agency-decisions/ed-decision-2025018r · EASA MOC OSO#6 (SAIL III) https://www.easa.europa.eu/en/downloads/139100/en · JARUS C2 Link RCP/RLP http://jarus-rpas.org/wp-content/uploads/2023/06/jar_02_doc_rpas_c2_link_rcp.pdf
- **Remote ID:** EASA https://www.easa.europa.eu/en/document-library/general-publications/remote-identification-will-become-mandatory-drones-across · ASD-STAN DRI https://cms.stan-shop.org/uploads/2024/01/ASD-STAN_DRI_Introduction_to_the_European_digital_RID_UAS_Standard.pdf
- **Radio (SKU UE):** Silvus SC4200 https://silvustechnologies.com/products/streamcaster-radios/ · Doodle Labs https://doodlelabs.com/products/ · Microhard pMDDL2450 https://www.microhardcorp.com/pMDDL2450.php · RFD900x/868x https://files.rfdesign.com.au/Files/documents/RFD900x%20DataSheet%20V1.2.pdf
- **SATCOM:** Iridium Certus 9770 https://www.iridium.com/products/iridium-certus-9770 · Certus 100 https://www.groundcontrol.com/products/iridium/iridium-certus-100-range/iridium-certus-100-plans/ · Inmarsat SB-UAV https://www.inmarsatgov.com/mission/applications/uas/
- **GCS:** Embention Veronte Control Stations https://www.embention.com/veronte/control-stations/ · Auterion Mission Control https://auterion.com/product/mission-control/ · QGroundControl https://qgroundcontrol.com/
