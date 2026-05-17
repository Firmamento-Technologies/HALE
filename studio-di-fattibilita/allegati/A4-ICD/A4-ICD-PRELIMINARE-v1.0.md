# Allegato A.4: Interface Control Document (ICD) preliminare v1.0

> **Studio di Fattibilità: Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies, bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 2, Allegato A.4
>
> **Versione:** v1.0 (M+3 baseline, post-Allineamento Strategico Maggio 2026)
> **Numero interfacce:** 50+ (questa baseline: **59 interfacce** in 7 categorie)
> **Metodologia:** ARP4754A (Guidelines for Development of Civil Aircraft and Systems) + ISO/IEC/IEEE 24765:2017 (Systems and Software Engineering Vocabulary) + NASA SE Handbook §6.3 (Interface Management)
> **Conformità procedurale IT:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (PFTE, Relazione Tecnica)
> **Disciplina epistemica:** Skill `epistemic-rigor`, confidence levels + falsifying observations su interfacce critiche
> **Boundary conditions:** B1 (service-only cooperative) + B2 (visione 10 anni EU sovereign HAPS) preserve
> **Riferimento padre:** Cap. 4 §4.4 (20 interfacce ICD preliminare); Cap. 6 (architettura sistema)
> **Riferimento agenti:** `avionics-gnc-engineer`, `telecom-ntn-payload-expert`, `aerodynamics-structures-engineer`, `earth-observation-expert`

---

## A.4.0 Premessa metodologica

### A.4.0.1 Scopo dell'Allegato

Il presente Allegato A.4 estende e dettaglia il **Quadro delle Interfacce** introdotto nel Capitolo 4 §4.4 dello Studio di Fattibilità. Il Capitolo 4 identifica **20 interfacce primarie** (INT-01 → INT-20) a livello concept/preliminary; il presente documento le **declina in 59 interfacce dettagliate**, ciascuna corredata di:

- Identificativo univoco strutturato (`INT-XX-YYY-NNN`)
- Caratteristiche tecniche complete (range, banda, voltaggio, protocollo, formato, unità)
- Standard di riferimento (ARP, MIL-STD, IEEE, 3GPP, ITU-R, GDPR, ENAC/EASA)
- Owner agent + test method + status + confidence
- Note operative e, per interfacce critiche, **falsifying observations**

L'ICD v1.0 costituisce il **secondo livello di rigore** previsto dalla disciplina NASA SE Handbook §6.3 [^1]:
- **Livello 0 (Concept ICD)** = Cap. 4 §4.4, 20 interfacce sigla+descrizione
- **Livello 1 (Preliminary ICD v1.0)** = presente documento, 59 interfacce con specifiche preliminary
- **Livello 2 (Detailed ICD v2.0)** = Fase 1 M+12/M+18: byte-level format, latency budget end-to-end, failure mode behavior, contratti vendor sign-off
- **Livello 3 (Frozen ICD v3.0)** = post First Flight 6A: interfacce validate in-flight, baseline contrattuale

### A.4.0.2 Framework normativo applicato

L'ICD v1.0 si conforma a tre famiglie normative complementari.

**Famiglia 1: Aerospace System Development**
- **ARP4754A** (SAE Aerospace Recommended Practice), Guidelines for Development of Civil Aircraft and Systems. Applicato per: allocazione DAL (Development Assurance Level) sulle interfacce, traceability requisiti → interfacce → verifica
- **ARP4761** (Safety Assessment Process). Applicato per FMEA derivata dalle interfacce critiche (vedi §A.4.6 Risk Register)
- **DO-178C** (Software Considerations in Airborne Systems). Applicato per software che attraversa interfacce safety-critical (FCS, GNC)
- **DO-254** (Design Assurance for Airborne Electronic Hardware). Applicato per hardware ridondato (autopilota, IMU)
- **DO-160G** (Environmental Conditions and Test Procedures for Airborne Equipment). Applicato per interfacce fisiche (power, vibration, temperature)
- **DO-326A / ED-202A** (Airworthiness Security Process Specification). Applicato per interfacce cybersecurity (C2 link, telemetry)

**Famiglia 2: Systems Engineering Generale**
- **ISO/IEC/IEEE 24765:2017** (Systems and Software Engineering, Vocabulary). Vocabolario standard per terminologia interfacce
- **ISO/IEC/IEEE 15288:2015** (Systems and Software Engineering, System Life Cycle Processes). Processi gestione interfacce
- **NASA SP-2016-6105 Rev 2** (NASA SE Handbook), §6.3 Interface Management metodologia

**Famiglia 3: Settore-specifica (telecom, RF, U-Space, privacy)**
- **3GPP TS 38.x** series (5G NR + NTN). Applicato per INT-6B-NTN-*
- **ITU-R F.1500/F.1891** (HAPS RF specifications). Applicato per INT-6B-FEEDER-*
- **Reg. UE 2019/947 + AMC SORA 2.5**. Applicato per INT-6A-REG-001 (ENAC)
- **Reg. UE 2021/664** (U-Space framework). Applicato per INT-6A-REG-003 (ENAV/D-Flight)
- **GDPR Reg. UE 2016/679**. Applicato per INT-6A-REG-004 + INT-X-PRIVACY-001
- **D.Lgs. 138/2024** (NIS2 recepimento). Applicato per INT-6A-REG-006 + INT-X-CYBER-001

### A.4.0.3 Convenzioni di nomenclatura

**Convenzione ID interfaccia:**

```
INT - XX - YYY - NNN
 │    │    │     │
 │    │    │     └── Numero progressivo (001, 002, …)
 │    │    └──────── Categoria (PHY, DATA, C2, GS, REG, NTN, FEEDER, OPS)
 │    └───────────── Percorso (6A | 6B | X = trasversale)
 └────────────────── Prefisso interfaccia
```

**Esempi:**
- `INT-6A-PHY-001` = Interfaccia, Percorso 6A, Fisica, numero 1
- `INT-6B-NTN-001` = Interfaccia, Percorso 6B, NTN service link, numero 1
- `INT-X-CLOUD-001` = Interfaccia, trasversale (X), Cloud, numero 1

**Convenzione Status (NASA SE-style):**
| Status | Descrizione |
|---|---|
| **Concept** | Interfaccia identificata; specifica non ancora definita |
| **Preliminary** | Specifica preliminary disponibile (questo documento) |
| **Detailed** | Specifica completa (Fase 1 M+12/M+18) |
| **Tested** | Verificata in test (DDT, Design & Development Test) |
| **Validated** | Validata in operational environment |
| **Frozen** | Baseline contrattuale per vendor |

**Convenzione Confidence:**
| Conf. | Significato | Tipologia evidence |
|---|---|---|
| **high** | Standard COTS consolidato, vendor multipli, validato industria | Standard pubblicato + ≥ 2 vendor case |
| **medium** | Standard noto ma sito-specifico, vendor unico, dipende da test campo | Standard pubblicato, 1 vendor o test pending |
| **low** | R&D in corso, TRL < 6, dipende da partnership/regolatorio | Concept design, no test integrated |
| **speculative** | Frontier R&D, TRL ≤ 3, ipotesi futura | Pre-Phase 0 research |

### A.4.0.4 Boundary conditions B1 + B2 preservate

In coerenza con Cap. 0bis, Cap. 4 §4.0bis e Cap. 6 §6.0bis:

- **B1 (Modello cooperativo + service-only)**: l'ICD include esplicitamente le **interfacce di servizio** (INT-6A-GS-003 Cooperative Dashboard, INT-6A-GS-004 PC Emergency Trigger, INT-X-VENDOR-001 framework vendor SLA) come elementi di sistema **interni allo scope** Firmamento operatore di servizi. NON include "interfaccia di vendita velivolo" perché fuori scope strategico.
- **B2 (Visione 10 anni nodo italiano EU sovereign HAPS)**: l'ICD include la sezione **interfacce trasversali** (INT-X-CLOUD-001 GAIA-X compliance) e le interfacce **HALE Percorso 6B** (INT-6B-*) con confidence prevalentemente low/speculative, in linea con lo status R&D Phase B preparatorio. Linguaggio pubblico: "complementare a IRIS²", NON "alternativa europea a Starlink".

---

## A.4.1 Tassonomia interfacce

### A.4.1.1 Classificazione per tipo

Adotto la tassonomia NASA SE Handbook §6.3 estesa con categorie italiane PFTE:

| Tipo | Descrizione | Esempi nell'ICD v1.0 |
|---|---|---|
| **Fisica meccanica** | Interfacce dimensionali, mount, accoppiamenti meccanici, CG | INT-6A-PHY-001 (Airframe ↔ Payload Bay), INT-6A-PHY-008 (Landing Gear ↔ Helipad) |
| **Fisica elettrica** | Alimentazione, segnali analogici, connettori, distribuzione potenza | INT-6A-PHY-002 (28V power rail), INT-6A-PHY-006 (Battery ↔ PDU), INT-6A-PHY-009 (Mains 230 VAC) |
| **Fisica termica** | Flussi di calore, range operativi temperatura, isolation | INT-6A-PHY-007 (Thermal Payload-Airframe), INT-6B-PHY-003 (HALE Battery Thermal) |
| **Fisica + RF** | Antenne, propagazione, polarizzazione, EIRP | INT-6A-PHY-004 (Ground Antenna), INT-6A-PHY-005 (Whip antenna), INT-6B-PHY-004 (Ka-band aperture) |
| **Funzionale data** | Protocolli digitali, formato dati, throughput, latency | INT-6A-DATA-* (8 interfacce), INT-6A-GS-007 (Anonymization pipeline) |
| **Funzionale control** | Comando, telemetria, autopilot, geofence | INT-6A-C2-* (8 interfacce, link C2 + DAA + lost-link) |
| **Funzionale + RF** | Link radio digitali con specifiche RF | INT-6A-C2-001 (RF 2.4 GHz), INT-6A-C2-003 (SATCOM L-band), INT-6B-NTN-* (5G NR-NTN), INT-6B-FEEDER-* (Ka-band) |
| **Operativa** | Procedure, workflow, escalation, training | INT-6A-GS-004 (PC Emergency Trigger), INT-6A-GS-005 (Flight Authorization Workflow) |
| **Regolatoria** | Autorità competenti, autorizzazioni, compliance | INT-6A-REG-001 (ENAC SORA), INT-6A-REG-002 (AGCOM), INT-6A-REG-004 (Garante DPIA), INT-6A-REG-006 (NIS2) |
| **Contrattuale** | SLA, contratti vendor/cliente, IP, billing | INT-X-VENDOR-001 (Vendor SLA UAS), INT-6A-REG-005 (Assicurazione) |
| **Ecosistemica** | Cloud sovrano, EU compliance, future consortium | INT-X-CLOUD-001 (GAIA-X), proiezione boundary B2 |

### A.4.1.2 Classificazione per criticità di sistema

Il criterio di criticità deriva da **DO-178C/DO-254 DAL allocation** (Development Assurance Level), applicato cross-cutting:

| Criticità | DAL equivalente | Conseguenza failure | Esempi |
|---|---|---|---|
| **Flight-Critical** | DAL-A/B | Loss of aircraft, fatality | INT-6A-C2-001 (C2 link primario), INT-6A-C2-004 (Lost-Link procedure), INT-6A-C2-006 (DAA ADS-B) |
| **Mission-Critical** | DAL-C | Mission abort, hazard reduced | INT-6A-DATA-001 (Payload RGB → MC), INT-6A-DATA-005 (Telemetry), INT-6A-GS-005 (Flight Auth Workflow) |
| **Non-Critical (Op)** | DAL-D/E | Operational impact, no safety | INT-6A-DATA-007 (Photogrammetry pipeline), INT-6A-GS-006 (Maintenance Console) |
| **Compliance-Critical** | N/A (regolatorio) | Authorization rejected, fines | INT-6A-REG-001 (ENAC SORA), INT-6A-REG-004 (Garante DPIA), INT-6A-REG-006 (NIS2) |
| **Business-Critical** | N/A (contrattuale) | Revenue loss, customer churn | INT-X-VENDOR-001 (Vendor SLA), INT-6A-GS-004 (PC Emergency) |

### A.4.1.3 Mappatura su Cap. 4 §4.4 (20 interfacce primarie → 59 dettagliate)

| INT-NN Cap. 4 | Sub-interfacce in A.4 v1.0 | Note |
|---|---|---|
| INT-01 (Airframe ↔ Payload) | INT-6A-PHY-001/002/003/007; INT-6B-PHY-001/002/003 | Mechanical + Power + Data + Thermal + HALE-specific |
| INT-02 (Payload ↔ Autopilot Data) | INT-6A-DATA-001/002 | RGB + IR |
| INT-03 (Air ↔ GS C2 RF Link) | INT-6A-C2-001/002/003/005; INT-6A-DATA-005/006 | Uplink + Downlink + SATCOM + Cyber + Telemetry + Video |
| INT-04 (GS ↔ Aircraft RF Antenna) | INT-6A-PHY-004/005 | Ground + Airborne |
| INT-05 (GS ↔ Backhaul Internet) | INT-6A-PHY-010; INT-6A-DATA-004 | Network + Upload |
| INT-06 (Cloud ↔ Cooperative Dashboard) | INT-6A-GS-003; INT-6A-DATA-007 | Web app + Pipeline |
| INT-07 (Modem ↔ AGCOM Band) | INT-6A-REG-002 | Spettro authorization |
| INT-08 (Power Mgmt ↔ FC Battery SOC) | INT-6A-PHY-006 | Battery integration |
| INT-09 (Autopilot ↔ Sensor Suite) | (interno autopilot JOUAV, no sub-interface) | Vendor-internal |
| INT-10 (Cooperative ↔ GCS ↔ Aircraft) | INT-6A-GS-003 (Dashboard); INT-6A-C2-008 (Geofence); INT-6A-GS-005 (Workflow) | UI + validation + workflow |
| INT-11 (Emergency Escalation PC) | INT-6A-GS-004 | SLA procedure |
| INT-12 (Data Governance ↔ DPO Audit) | INT-6A-DATA-008; INT-6A-GS-007; INT-X-LOGGING-001 | SIEM + Anonymization + Audit |
| INT-13 (Sistema ↔ ENAC SORA) | INT-6A-REG-001 | SORA pathway |
| INT-14 (Sistema ↔ ENAV / D-Flight U-Space) | INT-6A-REG-003; INT-6B-OPS-001/002 | U-Space + ENAV + EUROCONTROL |
| INT-15 (Sistema ↔ Garante Privacy) | INT-6A-REG-004; INT-X-PRIVACY-001 | DPIA + DSAR |
| INT-16 (Firmamento ↔ Vendor UAS) | INT-X-VENDOR-001 | SLA framework |
| INT-17 (Firmamento ↔ Vendor Payload) | INT-X-VENDOR-001 (incluso) | Stesso framework |
| INT-18 (Firmamento ↔ Cooperative) | INT-6A-GS-003 (Dashboard); convenzione operativa | Service framework |
| INT-19 (Firmamento ↔ Anchor PA) | INT-6A-GS-004 (PC); convenzione operativa | LoI/MOA |
| INT-20 (Sistema ↔ Ecosistema EU) | INT-X-CLOUD-001 (GAIA-X) | Boundary B2 long-term |

**Verifica copertura**: tutte le 20 interfacce primarie del Cap. 4 sono **dettagliate o coperte** dall'ICD v1.0. Nessuna interfaccia primaria orphan. **Status M+3: 100% copertura mapping**.

---

## A.4.2 ICD Architettura Percorso 6A (VTOL pilota)

Il Percorso 6A si fonda su una piattaforma VTOL ibrida commerciale TRL 8-9 (baseline JOUAV CW-30E o alternative EU come Tekever AR3/AR5, Quantum Trinity F90+, FlyingBasket FB3). Le interfacce 6A poggiano prevalentemente su **standard COTS aerospace consolidati**, con confidence prevalentemente medium-high.

### A.4.2.1 INT-6A-PHY-*: interfacce fisiche velivolo (10 interfacce)

Le interfacce fisiche del Percorso 6A coprono integrazione meccanica, elettrica e termica payload-airframe, antenne RF, landing gear, alimentazione GS, backhaul internet.

#### Scheda INT-6A-PHY-001: Airframe VTOL ↔ Modular Payload Bay

| Campo | Valore |
|---|---|
| **ID** | INT-6A-PHY-001 |
| **Nome** | Airframe VTOL ↔ Modular Payload Bay |
| **Tipo** | Fisica meccanica |
| **Parte A** | VTOL Airframe (JOUAV CW-30E o eq.) |
| **Parte B** | Payload Module (EO/IR/telecom) |
| **Direzione** | Bidirezionale (statica) |
| **Caratteristiche tecniche** | Bay 250×180×120 mm; massa payload ≤ 3 kg + 0.5 kg buffer; CG shift ≤ 2% MAC; mount quick-release tipo Picatinny-like + vibration isolation MIL-STD-810H Cat 4 (5-2000 Hz, 7.7 grms) |
| **Standard di riferimento** | MIL-STD-810H §514.8 (vibration); ISO 9022-2:2016 (mechanical mounting); vendor-specific dovetail mount |
| **Owner agent** | Avionics Integration Lead (Firmamento) + JOUAV Liaison |
| **Test method** | Inspection + analisi CG calc + shake table test |
| **Status** | Preliminary |
| **Confidence** | medium |
| **Note** | Sub-interface di INT-01 Cap.4. Critica per modularità payload tra missioni diverse (EO inspection / antincendio IR / connettività telecom). |
| **⚠️ Falsifying observation** | Se il vendor JOUAV (o equivalente) **non fornisce CAD interfacce dettagliato** entro M+6 pre-engagement, allora è necessario re-engineering custom mount adapter (+€15-25k + lead time +2-3 mesi), con impatto budget contingency +10-15%. |

#### Schede INT-6A-PHY-002 → INT-6A-PHY-010 (sintesi)

Le rimanenti 9 schede dettagliate sono riportate nel foglio Excel `ICD-v1.0.xlsx → Physical_Interfaces`. Highlights:

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6A-PHY-002 | Payload Power Rail 28 VDC | MIL-STD-704F, DO-160G §16 | high |
| INT-6A-PHY-003 | Payload Data Port Ethernet 1000BASE-T | IEEE 802.3, PoE+ 802.3at | high |
| INT-6A-PHY-004 | Ground Antenna Mount (parabolica 1.2 m) | EIA-222-H | high |
| INT-6A-PHY-005 | Airborne RF Antenna Whip (2.4 GHz) | MIL-STD-348B, MIL-C-39012 | medium |
| INT-6A-PHY-006 | Battery Pack ↔ PDU (LiPo 6S 22.2V) | DO-311A, UN 38.3, IEC 62133 | high |
| INT-6A-PHY-007 | Thermal Payload-Airframe | DO-160G §4, MIL-STD-810H | medium |
| INT-6A-PHY-008 | Landing Gear ↔ Helipad Surface | FAA AC 150/5390-2D | high |
| INT-6A-PHY-009 | GS Power Supply (230 VAC mains) | CEI 64-8, IEC 61000-4 | medium |
| INT-6A-PHY-010 | Backhaul Internet (GS → Cloud) | ITU-T G.983, IEEE 802.3ah | medium |

### A.4.2.2 INT-6A-DATA-*: data link, payload data (8 interfacce)

Le interfacce data del Percorso 6A includono il flusso dati end-to-end (Payload → Mission Computer → Storage → GS → Cloud) e la pipeline elaborazione (photogrammetry, anonymization, audit).

#### Scheda INT-6A-DATA-001: Payload EO RGB → Mission Computer

| Campo | Valore |
|---|---|
| **ID** | INT-6A-DATA-001 |
| **Nome** | Payload EO RGB → Mission Computer |
| **Tipo** | Funzionale data |
| **Parte A** | Camera Phase One iXM 100 (100 MP, 11608×8708 px) |
| **Parte B** | Mission Computer (MC) airborne |
| **Direzione** | Unidirezionale (Camera → MC) |
| **Caratteristiche tecniche** | GigE Vision 2.1 protocol; image RAW IIQ 16-bit ≈ 100 MB/frame; trigger frequency 1-5 fps; geotagging via NTP time sync + GPS PPS pulse 1 PPS ±100 ns |
| **Standard di riferimento** | GigE Vision 2.1 (AIA standard); GenICam 3.x; NTP v4 RFC 5905; PPS NMEA 0183 |
| **Owner agent** | Payload SE + Avionics Lead |
| **Test method** | Image capture test + geotag accuracy verification + throughput test |
| **Status** | Preliminary |
| **Confidence** | high |
| **Note** | Sub-interface di INT-02 Cap.4. GigE Vision costituisce standard consolidato per camera industrial. Phase One iXM 100 lo supporta nativamente. |

#### Sintesi INT-6A-DATA-002 → INT-6A-DATA-008

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6A-DATA-002 | Payload IR LWIR → MC | USB 3.0, FLIR Atlas SDK, ASTM E1862 | high |
| INT-6A-DATA-003 | Mission Data Storage (NVMe SSD) | NVMe 1.4, PCIe Gen3 | high |
| INT-6A-DATA-004 | Mission Data Upload GS → Cloud | AWS S3 API, TLS 1.3, Tus.io | high |
| INT-6A-DATA-005 | Telemetry Real-time Stream | MAVLink v2.0, AES-256-GCM | high |
| INT-6A-DATA-006 | Video Downlink Preview | H.265 HEVC, RTSP/RTP | medium |
| INT-6A-DATA-007 | Photogrammetry Pipeline (Cloud) | OGC GeoTIFF, ASPRS LAS 1.4 | medium |
| INT-6A-DATA-008 | Audit Log → SIEM | RFC 5425 Syslog over TLS, CEF | medium |

### A.4.2.3 INT-6A-C2-*: C2 link RF + SATCOM (8 interfacce)

Le interfacce C2 sono le **più critiche per safety** del Percorso 6A. Coprono il link RF primario, SATCOM fallback, lost-link procedure, DAA cooperativo e non-cooperativo, cybersecurity link, geofence.

#### Scheda INT-6A-C2-001: C2 Uplink Primary (RF 2.4 GHz ISM)

| Campo | Valore |
|---|---|
| **ID** | INT-6A-C2-001 |
| **Nome** | C2 Uplink Primary (RF 2.4 GHz ISM) |
| **Tipo** | Funzionale control |
| **Parte A** | GS RF Transceiver (Microhard pMDDL2450 o equivalente) |
| **Parte B** | UAV RF Transceiver (FCS-side) |
| **Direzione** | Unidirezionale (GS → UAV) per comandi |
| **Caratteristiche tecniche** | Frequenza 2400-2483.5 MHz ISM; modulazione OFDM adaptive; bitrate 0.5-9 Mbps; EIRP ≤ 100 mW (20 dBm) per AGCOM ISM o ≤ 1 W con licenza individuale; latency one-way ≤ 100 ms; fade margin ≥ 12 dB |
| **Standard di riferimento** | EN 300 328 (ISM 2.4 GHz harmonized EU); RED 2014/53/EU; AGCOM PNRF |
| **Owner agent** | RF Systems Engineer + AGCOM Liaison |
| **Test method** | Range test campo aperto + fade margin verification + spectrum analyzer |
| **Status** | Preliminary |
| **Confidence** | medium |
| **Note** | Sub-interface di INT-03 Cap.4 (uplink). |
| **⚠️ Falsifying observation** | Nelle **valle Pentema shadow zones** orograficamente probabili (Val Trebbia, Val Pentemina) il range effettivo 50 km LOS si riduce a 20-30 km con NLOS. Mitigazione: **switch automatico a SATCOM L-band (INT-6A-C2-003) entro 5 s** di lost-link. Test campo M+11 (in autorizzazione condizionata) per misura effettiva orografia. |

#### Scheda INT-6A-C2-004: Lost-Link Procedure (Autonomous RTH)

| Campo | Valore |
|---|---|
| **ID** | INT-6A-C2-004 |
| **Nome** | C2 Lost-Link Procedure (Autonomous RTH) |
| **Tipo** | Funzionale control + safety |
| **Parte A** | FCS Flight Computer |
| **Parte B** | Autopilot State Machine |
| **Direzione** | Internal logic |
| **Caratteristiche tecniche** | Trigger lost-link > 5 s consecutivi senza heartbeat MAVLink; primary action: RTH (Return-To-Home) verso ultimo home point GPS; secondary action se RTH fail: loiter + emergency land alla quota minima sicura; alert SMS PC + pilot |
| **Standard di riferimento** | RTCA DO-377 (C2 link); JARUS SORA 2.5 Annex F (lost-link procedure); EUROCAE ED-269 |
| **Owner agent** | Avionics Lead + Safety Engineer |
| **Test method** | Simulation HIL + flight test (in autorizzazione condizionata) |
| **Status** | Concept |
| **Confidence** | medium |
| **Note** | Critico per SORA SAIL III BVLOS authorization. Compliance OSO #2 (C2 link integrity). |
| **⚠️ Falsifying observation** | Se l'RTH path attraversa **shadow zone GPS** (canyon profondo Pentema) o ostacolo orografico non mappato, l'emergency land può atterrare in **area non sicura** (centro abitato, strada). **Mitigazione obbligatoria**: 3 RTH waypoint intermedi pre-pianificati con altitude buffer ≥ 100 m AGL; emergency land zones identificate via DTM 10m Liguria (Vol. 2 Allegato A.16); flight envelope no-fly zone su centri abitati (geofence INT-6A-C2-008). |

#### Sintesi INT-6A-C2-002, 003, 005-008

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6A-C2-002 | C2 Downlink Telemetry RF | MAVLink v2.0, AES-256-GCM | high |
| INT-6A-C2-003 | C2 Secondary SATCOM Iridium L-band | ITU-R RR Art.22, Iridium Certus, DO-262C | medium |
| INT-6A-C2-005 | Cybersecurity C2 (Mutual TLS + JWT) | TLS 1.3, X.509, JWT, DO-326A | medium |
| INT-6A-C2-006 | ADS-B IN Receiver (Cooperative DAA) | RTCA DO-260C, ICAO Annex 10 Vol IV | high |
| INT-6A-C2-007 | Non-Cooperative DAA (EO/Acoustic) | RTCA DO-365B, ASTM F3442 | low |
| INT-6A-C2-008 | Geofence Boundary | OGC GeoJSON RFC 7946 | high |

#### Scheda INT-6A-C2-007: Non-Cooperative DAA (Visual EO or Acoustic), CRITICA

| Campo | Valore |
|---|---|
| **Confidence** | **low** |
| **⚠️ Falsifying observation** | Se ENAC valuta Pentema BVLOS come SAIL IV e **richiede DAA non-cooperativo certificato** (oltre cooperative ADS-B IN), e la tecnologia COTS EO-based detection range ≥ 1 NM con false alarm rate ≤ 0.01/h **non è disponibile** entro M+18 (Fase 1 SORA submission), allora va in **Hold SORA submission** con impatto: ritardo first flight di 6-12 mesi + costi R&D EO DAA +€100-200k. **Mitigazione**: avviare R&D DAA EO in parallelo Fase 1 (non attendere SORA feedback); engagement con vendor specializzati (Daedalean, Iris Automation, Casia). |

### A.4.2.4 INT-6A-GS-*: Velivolo-GS, GS-Cloud, GS-EndUser (8 interfacce)

Le interfacce Ground Segment coprono HMI workstation, GS mobile (Protezione Civile), dashboard cooperativa, emergency trigger, workflow autorizzazione volo, console manutenzione, anonymization pipeline, backup & DR.

#### Scheda INT-6A-GS-004: Protezione Civile Emergency Trigger

| Campo | Valore |
|---|---|
| **ID** | INT-6A-GS-004 |
| **Nome** | Protezione Civile Emergency Trigger |
| **Tipo** | Operativa + contrattuale |
| **Parte A** | Sala Operativa PC Regione Liguria (operatore) |
| **Parte B** | Firmamento GCS On-Call Pilot |
| **Direzione** | Bidirezionale (PC → Firmamento richiesta; Firmamento → PC stato) |
| **Caratteristiche tecniche** | Trigger via (1) SMS gateway dedicato +39 numero unico, (2) email PEC priority, (3) webform dashboard. Acknowledge entro 5 min; launch decision entro 15 min TTR; ortofoto live entro 30 min (target nominale) |
| **Standard di riferimento** | SOP standard tabletop tested M+6/M+7; D.Lgs. 1/2018 Codice Protezione Civile; convenzione operativa ex art. 15 L. 241/90 |
| **Owner agent** | Operations Lead + PC Liaison Officer (Regione) |
| **Test method** | Tabletop exercise + scenario simulation + response time measurement |
| **Status** | Concept |
| **Confidence** | medium |
| **Note** | Sub-interface di INT-11 Cap.4. SLA TTR ≤ 4h nominale; emergency ≤ 30 min target. |
| **⚠️ Falsifying observation** | In caso di **meteo avverso** (vento sostenuto > 17 m/s, raffiche > 22 m/s, pioggia > 10 mm/h) la **launch può non essere possibile** per safety. SLA **degraded a 'best effort'** dichiarato esplicitamente in convenzione operativa Regione. Workshop M+6/M+9 con PC deve allineare aspettative su SLA "weather-conditional". |

#### Sintesi INT-6A-GS-001, 002, 003, 005-008

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6A-GS-001 | GS Control Room HMI | ISO 9241, MIL-STD-1472H, EUROCAE ED-269 | medium |
| INT-6A-GS-002 | GS Mobile Vehicle Integration | ISO 16750, IEC 60529 IP54 | medium |
| INT-6A-GS-003 | Cooperative Dashboard (Web App) | SAML 2.0 SPID, OAuth 2.0, WAI-ARIA WCAG 2.1 AA | medium |
| INT-6A-GS-005 | Flight Authorization Workflow | EUROCAE ED-269, JARUS SORA 2.5 OSO #19 | medium |
| INT-6A-GS-006 | GS Maintenance Console (Health Mon) | ARINC 624, MIL-HDBK-2155 | medium |
| INT-6A-GS-007 | Data Anonymization Pipeline (GDPR) | GDPR Art. 17+25, ISO/IEC 27701 | medium |
| INT-6A-GS-008 | Backup & Disaster Recovery | ISO/IEC 27031, NIST SP 800-34 | medium |

### A.4.2.5 INT-6A-REG-*: interfacce regolatorie (6 interfacce)

Le interfacce regolatorie vengono **gestite tramite formalismi documentali** (lettere PEC, application formali, DPIA, polizze assicurative). Sono **compliance-critical**: il loro failure compromette l'autorizzazione operativa.

#### Scheda INT-6A-REG-001: ENAC SORA Authorization (SAIL III BVLOS)

| Campo | Valore |
|---|---|
| **ID** | INT-6A-REG-001 |
| **Nome** | ENAC SORA Authorization (SAIL III BVLOS) |
| **Tipo** | Regolatoria |
| **Parte A** | Firmamento Technologies (operatore UAS) |
| **Parte B** | ENAC Ufficio RPAS |
| **Direzione** | Bidirezionale (application + authorization) |
| **Caratteristiche tecniche** | Application: Operations Manual + SORA worksheet + Operator Declaration + insurance certificate + DAA mitigation evidence; iter: pre-application meeting M+3/M+6, application formal M+15/M+18 (Fase 1), authorization expected M+18/M+22; categoria Specific SAIL III stimato per BVLOS Pentema |
| **Standard di riferimento** | Reg. UE 2019/947 art. 12 + AMC/GM Amendment 3 (Sett 2025) SORA 2.5 EU; ENAC Reg. APR Ed. 3 |
| **Owner agent** | Aviation Regulatory Counsel + ENAC Liaison |
| **Test method** | Documentation review + pre-application feedback |
| **Status** | Concept |
| **Confidence** | medium |
| **Note** | Sub-interface di INT-13 Cap.4. |
| **⚠️ Falsifying observation** | Se ENAC valuta Pentema come **'area sensibile'** (zona ad alta protezione naturale es. parte del Parco dell'Aveto o vicinanza Riserva, vincolo paesaggistico), il SAIL IV viene richiesto, con impatto: **costi +€200-400k** (test addizionali, evidence richiesta più stringente, eventuale Type Certification preliminary) + **tempo +6 mesi** + **possibile rifiuto** se DAA non-cooperativo non maturo. **Mitigazione**: pre-application meeting **early M+3**; alternative site analysis (es. fascia pre-appenninica meno sensibile) ready as Plan B; coordination con Comune + Regione + ENAC ufficio territoriale. |

#### Scheda INT-6A-REG-002: AGCOM Spectrum Authorization

| Campo | Valore |
|---|---|
| **Confidence** | **medium** |
| **⚠️ Falsifying observation** | Se AGCOM **rifiuta licenza individuale 2.4 GHz EIRP > 100 mW** (ISM unlicensed limita a 100 mW, range max ~10-20 km LOS), il **range C2 risulta limitato**. **Mitigazione**: Fallback ISM 100 mW + SATCOM Iridium L-band primario (INT-6A-C2-003), costo operativo +€800-1200/mese. **Confidence: medium-low** che AGCOM rifiuti (precedenti positivi per altri operatori UAS commerciali); engagement M+1/M+2. |

#### Sintesi INT-6A-REG-003 → INT-6A-REG-006

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6A-REG-003 | ENAV/D-Flight U-Space Coordination | Reg. UE 2021/664, ENAC LG-2023/006 | medium |
| INT-6A-REG-004 | Garante Privacy DPIA + DSAR | GDPR Art. 35, EDPB Guidelines 01/2022 | medium |
| INT-6A-REG-005 | Assicurazione Aviation Third-Party | Reg. UE 785/2004, ENAC LRA 25/2023 | medium |
| INT-6A-REG-006 | NIS2 Cybersecurity Notification | D.Lgs. 138/2024 (Dir. UE 2022/2555) | medium |

---

## A.4.3 ICD Architettura Percorso 6B (HALE)

Il Percorso 6B (HALE solare stratosferico) si trova in stato **R&D Phase B preparatorio**. Le interfacce 6B presentano confidence prevalentemente **low/speculative** e sono dichiarate **Concept**: il dettaglio Detailed ICD viene deferito a Phase C-D (M+48/M+60+).

### A.4.3.1 INT-6B-PHY-*: interfacce fisiche HALE (4 interfacce)

#### Scheda INT-6B-PHY-001: HALE Airframe ↔ Solar Panel Array

| Campo | Valore |
|---|---|
| **ID** | INT-6B-PHY-001 |
| **Nome** | HALE Airframe ↔ Solar Panel Array |
| **Tipo** | Fisica meccanica + termica |
| **Parte A** | HALE Wing structure (CFRP primario + lino secondario) |
| **Parte B** | Solar Panel Array (GaAs multi-junction Spectrolab XTJ Prime o eq.) |
| **Direzione** | Statica (bonded) |
| **Caratteristiche tecniche** | Area pannelli ≥ 25 m² (worst-case calc inverno 44°N); panel mass density 0.5-0.8 kg/m² (~0.6 kg/m² target); encapsulation Honeywell Aclar (UV resistant); bonding film 3M VHB structural; thermal CTE matching CFRP critical |
| **Standard di riferimento** | ECSS-Q-ST-70-71 (Materials and Processes for spacecraft); ASTM E1980 (solar reflectance) |
| **Owner agent** | Aerodynamics-Structures Engineer + Solar Cell Specialist |
| **Test method** | Bonding strength test (lap shear) + thermal cycling -65/+40°C + UV exposure 1000h |
| **Status** | Concept |
| **Confidence** | low |
| **Note** | Sub-interface di INT-01 Cap.4 per 6B. R&D dedicato. |
| **⚠️ Falsifying observation** | RSK-TEC-001 cross-reference: se il peso pannelli effettivo risulta **> 0.8 kg/m²** (vs target 0.6), il MTOW cresce +12-15 kg e **l'energy balance inverno deficit viene aggravato** del 20-30%. Se l'efficienza effettiva è **< 28%** (vs target 30%), E_solar_day cala del 10% e il deficit margine inverno peggiora. Verifica supplier specs early M+12/M+18 (Fase 1+). |

#### Schede INT-6B-PHY-002, 003, 004 (sintesi)

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6B-PHY-002 | HALE Wing Spar ↔ Fuselage Joint | ECSS-E-ST-32-08, MIL-HDBK-17, ASTM D5868 | low |
| INT-6B-PHY-003 | HALE Battery Pack Thermal Mgmt | DO-311A, UN 38.3, ECSS-E-ST-31C | low |
| INT-6B-PHY-004 | HALE Antenna Aperture Ka-band | ITU-R F.1500, RTCA DO-262C | low |

#### Scheda INT-6B-PHY-003: HALE Battery Pack Thermal Management, CRITICA

| Campo | Valore |
|---|---|
| **Confidence** | **low** |
| **⚠️ Falsifying observation** | RSK-TEC-001 cross-reference (energy balance inverno deficit -50.1% post-simulazione M+3): se il thermal management **heater richiede > 80 W continuous** (vs baseline 50 W) per mantenere batterie LiS in range +5/+45°C @ ambient -65°C, l'**energy balance notturno peggiora ulteriormente**, lo showstopper RSK-TEC-001 viene confermato e si arriva all'**abbandono perennial flight 44°N** con fallback "E5 Seasonal-only" (marzo-ottobre) e revisione business case Percorso 6B (riduzione revenue persistente, focus su seasonal services). Test bench inverno simulato Fase 3 M+38. |

### A.4.3.2 INT-6B-NTN-*: Service link 5G NR-NTN (4 interfacce)

Le interfacce service link NTN costituiscono **frontier R&D**: 3GPP Rel-17/18 NTN solutions risultano pubblicate, ma il deployment commerciale HAPS è in fase pre-operativa globalmente (2026).

#### Scheda INT-6B-NTN-001: 5G NR-NTN Service Link Downlink (HAPS → UE)

| Campo | Valore |
|---|---|
| **ID** | INT-6B-NTN-001 |
| **Nome** | 5G NR-NTN Service Link Downlink (HAPS → UE) |
| **Tipo** | Funzionale + RF |
| **Parte A** | HAPS gNodeB regenerative payload |
| **Parte B** | User Equipment 5G NTN-capable (smartphone, IoT, vehicular) |
| **Direzione** | Unidirezionale (DL) |
| **Caratteristiche tecniche** | Frequency S-band 2010-2025 MHz (3GPP banda n255) o 1980-2010 MHz (n256); bandwidth 5-20 MHz per beam; modulation up to 256-QAM; coverage cell 30-50 km diameter @ 20 km altitude; capacity per beam 50-200 Mbps; 16-32 beam aggregato 1-3 Gbps per HAPS |
| **Standard di riferimento** | 3GPP TS 38.211/.212/.213/.214 (NR L1); TS 38.811 (NTN study report); TS 38.821 (NTN solutions); ITU-R M.2150 |
| **Owner agent** | Telecom-NTN Payload Expert |
| **Test method** | Link budget simulation + over-the-air test (vs UE simulator) + capacity test field |
| **Status** | Concept |
| **Confidence** | low |
| **Note** | Per 6B HALE service link. S-band ideale per copertura aree interne 5G NTN. |
| **⚠️ Falsifying observation** | Lo spettro S-band n255 risulta **contestato con MNO terrestri** (TIM, Vodafone) che dispongono di licenze IMT regionali. Senza **accordi spectrum sharing** o **spectrum trading**, Firmamento non può operare commercialmente in S-band. **Mitigazione**: (1) engagement TIM/Vodafone per partnership wholesale (Firmamento fornisce capacity, MNO eroga al cliente finale); (2) alternative banda HAPS dedicata C-band 6.4-6.7 GHz (post-WRC-19), meno congestionata, ma con UE penetration più limitata. Roadmap regolatoria spettro: vedi Cap. 5 §5.5. |

#### Sintesi INT-6B-NTN-002, 003, 004

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6B-NTN-002 | 5G NR-NTN Service Link Uplink | 3GPP TS 38.101-5, ITU-R M.2150 | low |
| INT-6B-NTN-003 | NTN Doppler Compensation | 3GPP TS 38.811 §6.4, TS 38.821 §6.4.2 | medium |
| INT-6B-NTN-004 | Inter-Beam Handover (intra-HAPS) | 3GPP TS 38.331, TS 38.300 | medium |

### A.4.3.3 INT-6B-FEEDER-*: Gateway 31 GHz (3 interfacce)

Il feeder link Ka-band 27.9-31.3 GHz risulta **HAPS-dedicated post-WRC-19**: lo spettro è disponibile globalmente per HAPS, ma la coexistence con Fixed Satellite Service (FSS) GEO richiede coordinamento ITU.

#### Sintesi INT-6B-FEEDER-001, 002, 003

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6B-FEEDER-001 | Ka-band Feeder Link DL (HAPS → Gateway) | ITU-R F.1500/F.1891, ETSI EN 302 307-2 DVB-S2X, ITU-R P.618-14 | low |
| INT-6B-FEEDER-002 | Ka-band Feeder Link UL (Gateway → HAPS) | ITU-R F.1500, ITU RR Appendix 30B | low |
| INT-6B-FEEDER-003 | Gateway HAPS ↔ Core Network 5G | 3GPP TS 23.501 (5G architecture), TS 29.281 (GTP-U) | low |

#### Scheda INT-6B-FEEDER-001: Ka-band Feeder Link Downlink, CRITICA

| Campo | Valore |
|---|---|
| **Confidence** | **low** |
| **⚠️ Falsifying observation** | Il **rain fade Genova Zona K (ITU-R P.618-14)** può raggiungere **25 dB @ 99.9% availability** in stagione invernale-primaverile, imponendo un margine link significativo. Se l'EIRP HAPS non riesce a eguagliare o superare questo margine, combinato con uplink interference da operatori vicini, l'**outage diventa non accettabile per servizio commerciale wholesale** (SLA tipico telco ≥ 99.5%). **Mitigazione**: Adaptive Coding & Modulation (ACM) DVB-S2X mandatory; site diversity (2+ gateway separati > 30 km, es. Genova + La Spezia, statisticamente decorrelati); strategia operatività graceful degradation in eventi estremi. |

### A.4.3.4 INT-6B-OPS-*: ENAV, EUROCONTROL, U-Space (3 interfacce)

Le interfacce operative HALE sono **prevalentemente long-term**: HAPS commerciale operativo richiede coordinamento con ATM nazionale (ENAV) e europeo (EUROCONTROL) per cleared corridor permanenti.

#### Sintesi INT-6B-OPS-001, 002, 003

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-6B-OPS-001 | HALE Air Traffic Coordination (ENAV) | ICAO Annex 11, ICAO Doc 4444, Reg. UE 923/2012 SERA | low |
| INT-6B-OPS-002 | EUROCONTROL Cross-Border Coordination | EUROCONTROL FPL format, ICAO Doc 7030 | low |
| INT-6B-OPS-003 | HALE Launch & Recovery Site | FAA AC 91-79, EASA AMC1 SPA.SPO | low |

#### Scheda INT-6B-OPS-003: HALE Launch & Recovery Site, CRITICA

| Campo | Valore |
|---|---|
| **Confidence** | **low** |
| **⚠️ Falsifying observation** | **Pentema NON è adatta come launch site HALE** (terreno montano, runway grass impossibile, accesso aerotraino impossibile). Site candidato realistico: **ex aeroporto Sarzana-Luni o aeroporto Albenga** (entrambi Liguria, ma con vincoli operativi propri). **Lead time site permitting ≥ 12 mesi** dopo Phase C-D Go decision. **Weather window stringente** (wind ≤ 5 m/s @ ground, no rain, clear sky per visibility), operabilità launch/recovery ≤ 60-80 giorni/anno realisticamente in Liguria. Necessaria flotta multi-HALE per garantire copertura continua wholesale. |

---

## A.4.4 ICD Trasversali (Cloud + Privacy + Cybersecurity)

Le interfacce trasversali sono **comuni ai Percorsi 6A + 6B** e coprono cloud sovrano (GAIA-X compliance), privacy operativa (DSAR), cybersecurity continua, logging centralizzato, vendor SLA framework.

### A.4.4.1 INT-X-CLOUD-001: Cloud Hosting GAIA-X Compliant

| Campo | Valore |
|---|---|
| **ID** | INT-X-CLOUD-001 |
| **Nome** | Cloud Hosting GAIA-X Compliant |
| **Tipo** | Funzionale + regolatoria + contrattuale |
| **Parte A** | Firmamento Cloud Workload (data + apps + ML pipeline) |
| **Parte B** | Cloud Provider GAIA-X compliant (Aruba IT / OVHcloud Italia / IONOS Italia) |
| **Direzione** | Contrattuale |
| **Caratteristiche tecniche** | Provider GAIA-X Label Level 2+ (data sovereignty); region IT or EU; SLA uptime ≥ 99.9% (Tier 3 datacenter); RPO ≤ 4h; data residency garantita IT/EU; subprocessor list GDPR Art. 28; backup geo-redundant EU |
| **Standard di riferimento** | GAIA-X Compliance Framework v22.10 (e successive); ISO/IEC 27001; SOC 2 Type II; CSA STAR Level 2 |
| **Owner agent** | Cloud Architect + Procurement + DPO |
| **Test method** | Provider audit + GAIA-X attestation review + data residency test + DR drill |
| **Status** | Concept |
| **Confidence** | high |
| **Note** | Sub-interface di INT-20 Cap.4. Aruba dispone di **label GAIA-X confermato 2025**. OVH Italia e IONOS Italia pari opportunità. Hyperscaler USA (AWS/Azure/GCP) **NON GAIA-X compliant** per default, da escludere strategicamente per boundary B2 (sovereign infrastructure). |

### A.4.4.2 Sintesi altre interfacce trasversali

| ID | Nome | Standard chiave | Conf. |
|---|---|---|---|
| INT-X-PRIVACY-001 | DSAR Workflow | GDPR Art. 12-22, EDPB Guidelines 01/2022 | high |
| INT-X-CYBER-001 | Penetration Testing + Vuln Mgmt | OWASP Testing Guide v4.2, PTES, ISO/IEC 27001 A.12.6 | high |
| INT-X-LOGGING-001 | Centralized Logging + Audit Trail | RFC 5424 Syslog, CEF, NIST SP 800-92, GDPR Art. 32 | high |
| INT-X-VENDOR-001 | Vendor SLA Framework (UAS Manufacturer) | AS/EN 9100D, ICAO Annex 19 | medium |

#### Scheda INT-X-VENDOR-001: Vendor SLA Framework, CRITICA

| Campo | Valore |
|---|---|
| **Confidence** | **medium** |
| **⚠️ Falsifying observation** | Il vendor baseline **JOUAV (CN, Cina)** potrebbe risultare soggetto a **export control issues** post-evoluzione geopolitica (tensioni EU-CN su dual-use, evolution Wassenaar Arrangement, eventuali sanzioni settoriali), con impossibilità di importare CW-30E o di ricevere spare parts/support. **Mitigazione obbligatoria**: identificare **vendor alternativi EU pre-RFQ M+6**: (1) **Tekever AR3/AR5** (Portogallo, EU AIRBUS partnership), (2) **Quantum Systems Trinity F90+** (Germania, dual-use cleared), (3) **FlyingBasket FB3** (Italia, supply chain europea). Decisione vendor finale con criterio supply chain risk + geopolitical resilience ponderato in DOCFAP M+8. Vedi `riferimenti/RESERVED-rischi-geopolitici.md` per analisi geopolitica completa. |

---

## A.4.5 Matrice compatibility interfacce

La **Matrice di Compatibilità** valuta interfacce-interfacce potenziali conflitti (mass+power+thermal+EMC) o sinergie. Costituisce uno strumento di **integration engineering**: identifica accoppiamenti dove un parametro di un'interfaccia (es. potenza payload) impatta un'altra (es. battery sizing).

### A.4.5.1 Matrice condensata (10×10 critical 6A)

Per leggibilità riporto qui solo la matrice condensata su 10 interfacce 6A critiche. La matrice completa (50×50) si trova nel foglio Excel `ICD-v1.0.xlsx → Compatibility_Matrix`.

| | PHY-001 | PHY-002 | PHY-004 | PHY-005 | PHY-006 | PHY-007 | PHY-009 | PHY-010 | C2-001 | C2-003 |
|---|---|---|---|---|---|---|---|---|---|---|
| **PHY-001** Payload Bay | n/a | OK | OK | OK | OK | Check (mass+thermal) | OK | OK | OK | OK |
| **PHY-002** 28V Power | OK | n/a | OK | OK | OK (BMS) | OK | OK | OK | OK | OK |
| **PHY-004** Ground Ant | OK | OK | n/a | OK (RF coupling) | OK | OK | OK | OK | OK (RF feeder) | OK |
| **PHY-005** Whip Ant | OK | OK | OK (RF coupling) | n/a | OK | OK | OK | OK | OK | OK |
| **PHY-006** Battery | OK | OK (BMS) | OK | OK | n/a | Check (thermal) | OK | OK | OK | OK |
| **PHY-007** Thermal | Check (mass+thermal) | OK | OK | OK | Check (thermal) | n/a | OK | OK | OK | OK |
| **PHY-009** GS Power | OK | OK | OK | OK | OK | OK | n/a | OK | OK | OK |
| **PHY-010** Backhaul | OK | OK | OK | OK | OK | OK | OK | n/a | OK | OK |
| **C2-001** RF Uplink | OK | OK | OK (RF feeder) | OK | OK | OK | OK | OK | n/a | OK (fallback) |
| **C2-003** SATCOM | OK | OK | OK | OK | OK | OK | OK | OK | OK (fallback) | n/a |

**Legenda:**
- **OK** = Compatibile (nessun conflitto rilevato)
- **Check** = Richiede verifica multi-dominio (es. mass+thermal+EMC)
- **Conflict** = Conflitto identificato, mitigation richiesta
- **n/a** = Self (diagonal)

### A.4.5.2 Punti di attenzione identificati

1. **(PHY-001, PHY-007) Mass + Thermal**: il payload bay deve sostenere mass budget + thermal dissipation. Se il payload genera oltre 80 W heat e l'operating range è stringente, il design termico (heat path + NACA cooling) va validato congiuntamente al design meccanico.
2. **(PHY-004, PHY-005) RF Coupling Antenna**: ground antenna e airborne antenna devono operare nello stesso link RF. Pattern, polarizzazione, EIRP e sensitivity vanno co-progettati.
3. **(PHY-006, PHY-007) Battery Thermal**: la batteria genera heat in discharge e assorbe heat in charge. Il thermal management influisce sul SOC sensing accuracy e sulla safety (thermal runaway prevention).
4. **(C2-001, C2-003) Primary + Secondary Link Switch**: la logica di switch automatico tra RF 2.4 GHz e SATCOM L-band deve gestire seamlessly la transizione (no perdita comando). Test critico in field test.

---

## A.4.6 Risk register interfacce critiche

12 rischi interfaccia ad alta criticità (P×I score ≥ 9) sono tracciati nel Risk Register dell'Allegato. Sintesi top 5:

| RISK-ID | Interfaccia | Descrizione | P | I | P×I | Mitigazione |
|---|---|---|---|---|---|---|
| **RSK-INT-005** | INT-6B-PHY-003 | Battery thermal mgmt heater > 80W, energy balance deficit inverno | 4 | 5 | **20** | Cross-ref RSK-TEC-001; design alternativi (E5 Seasonal-only); R&D thermal Phase 3 |
| **RSK-INT-001** | INT-6A-C2-001 | Shadow zones C2 RF 2.4 GHz Pentema, loss link | 4 | 4 | **16** | Doppio link RF + SATCOM Iridium; RTH automatico < 5 s |
| **RSK-INT-006** | INT-6B-NTN-001 | Spettro S-band n255 contestato MNO, no spectrum sharing | 4 | 4 | **16** | Engagement TIM/Vodafone partnership; alternative banda HAPS C-band 6.4 GHz |
| **RSK-INT-002** | INT-6A-REG-001 | ENAC valuta Pentema 'area sensibile', SAIL IV richiesto | 3 | 5 | **15** | Pre-application early M+3; alternative site analysis; coord Comune+Regione+ENAC |
| **RSK-INT-004** | INT-6B-PHY-001 | Solar array bonding fail thermal cycling, delamination | 3 | 5 | **15** | R&D dedicato Fase 3; test panel qualification ECSS |

(Lista completa 12 rischi nel foglio Excel `ICD-v1.0.xlsx → Risk_Register_Interfacce`.)

### A.4.6.1 Risk trend analysis

| Categoria | # rischi P×I ≥ 15 (red) | # rischi P×I 9-14 (yellow) | # rischi P×I < 9 (green) |
|---|---|---|---|
| Interfacce 6A | 1 (RSK-INT-001) | 5 (RSK-INT-002,003,007,008,010,011,012) | 0 |
| Interfacce 6B | 4 (RSK-INT-004,005,006 + altro showstopper) | 0 | 0 |
| Trasversali | 0 | 1 (RSK-INT-007 vendor) | 0 |

**Osservazione**: il **profilo di rischio interfacce 6B risulta strutturalmente più alto** del 6A, coerentemente con stato R&D Phase B preparatorio e confidence prevalentemente low. Il Risk Register è dinamico: aggiornamento M+6 + M+9 + M+11 con trend P×I (target downward).

---

## A.4.7 Test plan integrazione interfacce

Il Test Plan v1.0 identifica **20 test campaign** correlate alle interfacce dell'ICD, articolate in 4 fasi:

| Fase Test | Periodo | # test | Tipologia |
|---|---|---|---|
| **DDT (Design & Development Test)** | M+10/M+12 (PFTE) | 4 | Lab bench, simulazione, vendor facility test |
| **Integration Test** | Fase 1 M+13/M+18 | 6 | Integration UAV + GS + Cloud + SATCOM |
| **Field Test / Verification** | Fase 1 M+18/M+22 | 6 | Field test in autorizzazione condizionata + first flight |
| **Validation** | Fase 1 M+20/M+24 (+ ongoing) | 4 | Operational scenario validation con stakeholder (PC, cooperative) |

### A.4.7.1 Test Plan summary (sintesi)

| ID Interfaccia | Test Method | Test Phase | Owner | Timing (M+) |
|---|---|---|---|---|
| INT-6A-PHY-001 | Inspection + CG analysis + shake table | DDT | Avionics Integration Lead | M+10/M+12 |
| INT-6A-PHY-002 | Lab bench + transient injection + load step | DDT | Power Mgmt SE | M+10 |
| INT-6A-DATA-001 | Image capture + geotag + throughput | DDT | Payload SE | M+11 |
| INT-6A-C2-001 | Range test + fade margin + spectrum analyzer | DDT + Field Test | RF Systems Engineer | M+11 (limited) + Fase 1 |
| INT-6A-C2-003 | Link test + handover + latency | Integration Test | Avionics Lead | Fase 1 M+13/M+15 |
| INT-6A-C2-004 | HIL simulation + flight test | Verification | Avionics Lead + Safety | Fase 1 M+16/M+18 |
| INT-6A-GS-004 | Tabletop exercise + scenario sim | Validation | Operations Lead + PC | M+6/M+9 + Fase 1 |
| INT-6A-REG-001 | Documentation review + ENAC feedback | Regulatory Compliance | Aviation Reg Counsel | M+3/M+6 (pre-app) + Fase 1 |
| INT-6A-REG-002 | Doc review + AGCOM response | Regulatory Compliance | Aviation Reg + RF SE | M+1/M+4 |
| INT-6A-REG-004 | DPIA review + DSAR drill | Regulatory Compliance | Data Privacy Counsel + DPO | M+4/M+5 + ongoing |
| INT-6A-GS-003 | Functional + RBAC + accessibility | Validation | Cloud Architect + DPO | Fase 1 M+14/M+16 |
| INT-6A-GS-007 | AI inference quality test | Validation | DPO + AI/ML Engineer | Fase 1 M+15/M+17 |
| INT-6B-PHY-001 | Lap shear + thermal cycling + UV | Subscale Test | Aero-Struct Engineer | Fase 3 M+36/M+42 |
| INT-6B-PHY-002 | FEA + GVT + structural test | Subscale + Component Test | Aero-Struct Engineer | Fase 3 M+36/M+44 |
| INT-6B-NTN-001 | Link budget sim + OTA test | Lab Test | Telecom-NTN Expert | Fase 3 M+40/M+46 |
| INT-6B-FEEDER-001 | Link budget + rain fade sim | Lab + Simulation | Ka-band RF Engineer | Fase 3 M+40/M+45 |
| INT-X-CLOUD-001 | Provider audit + attestation review | Procurement Validation | Cloud Architect + Procurement | M+5/M+9 |
| INT-X-PRIVACY-001 | DSAR drill + audit | Validation | DPO + Customer Support | Fase 1 M+15/M+17 |
| INT-X-CYBER-001 | External pentest annuale | Verification | Cybersecurity Engineer | Fase 1 M+16/M+18 + annuale |
| INT-X-VENDOR-001 | Vendor audit + SLA monitoring | Procurement Validation | Procurement Lead + QM | M+1/M+6 (pre-eng) + Fase 1 |

(Pass/Fail criteria + Test Environment dettagliati nel foglio Excel `ICD-v1.0.xlsx → Test_Plan`.)

---

## A.4.8 Versioning roadmap (v1.0 → v1.5 → v2.0)

L'ICD v1.0 costituisce la **baseline preliminary**. Le versioni successive aggiungeranno detail e validazione progressiva:

| Versione | Milestone | Data target | Scope |
|---|---|---|---|
| **v0.5** | Cap. 4 §4.4 baseline | M+3 (Mag 2026) | 20 interfacce primarie identificate nel Capitolo 4 ICD preliminare |
| **v1.0** | Vol. 2 Allegato A.4 baseline | M+3/M+6 (Mag-Ago 2026) | **PRESENTE DOCUMENTO**: 50+ interfacce dettagliate, 7 categorie, risk register, test plan |
| **v1.5** | Post pre-engagement vendor + ENAC/AGCOM feedback | M+6/M+8 (Ago-Ott 2026) | Specifications updated post-vendor RFQ responses; INT-6A-REG-001/002 refined post-feedback; potenziali nuove interfacce identificate in workshop |
| **v2.0** | Detailed ICD pre-Phase 1 execution | M+10/M+12 (Dic 2026-Feb 2027) | Byte-level format, latency end-to-end budget, failure mode behaviors, ICD frozen per vendor contracts. Tutte interfacce 6A: Detailed; 6B: Concept |
| **v2.5** | Post-First Flight 6A | M+20/M+24 (Ago-Dic 2027) | Interfacce validate in-flight; lessons learned incorporated; SLA backhaul/cloud measured baseline; 6A: Validated; 6B: Preliminary |
| **v3.0** | HALE 6B Phase B closure | M+48/M+60 (Y4-Y5) | ICD 6B Detailed completo post-subscale flight test; preparazione Phase C-D. 6A: Operational baseline; 6B: Detailed Preliminary |

### A.4.8.1 Triggers di re-baselining

L'ICD viene re-baselined al verificarsi di uno dei seguenti **trigger eventi**:

1. **Change Control Board (CCB) decision** su modifica architettura (es. cambio vendor UAS post-Trade Study)
2. **Falsifying observation confermata** (es. ENAC richiede SAIL IV, INT-6A-REG-001 cambia scope)
3. **Nuovo standard normativo** (es. AGCOM aggiorna PNRF allocando nuova banda HAPS)
4. **Major audit finding** (red team / regulatory adversary / RINA-DNV) che identifica gap critico
5. **First Flight lessons learned** (Fase 1 M+22/M+24)

---

## A.4.9 Riferimenti

[^1]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2), §6.3 Interface Management. Confidence: high (norma metodologica internazionale).

[^2]: ARP4754A, Guidelines for Development of Civil Aircraft and Systems (SAE International). Applicato per DAL allocation + traceability requisiti-interfacce-verifica. Confidence: high.

[^3]: ISO/IEC/IEEE 24765:2017, Systems and Software Engineering Vocabulary. Confidence: high.

[^4]: ISO/IEC/IEEE 15288:2015, Systems and Software Engineering Life Cycle Processes. Confidence: high.

[^5]: DO-178C, Software Considerations in Airborne Systems and Equipment Certification (RTCA). Applicato per software safety-critical. Confidence: high.

[^6]: DO-254, Design Assurance Guidance for Airborne Electronic Hardware (RTCA). Applicato per hardware ridondato. Confidence: high.

[^7]: DO-160G, Environmental Conditions and Test Procedures for Airborne Equipment (RTCA). Applicato per environmental qualification interfacce fisiche. Confidence: high.

[^8]: DO-326A / ED-202A, Airworthiness Security Process Specification (RTCA/EUROCAE). Applicato per cybersecurity interfacce. Confidence: high.

[^9]: 3GPP TS 38.811 (NR NTN Study Report) + TS 38.821 (NTN Solutions). Applicato per INT-6B-NTN-*. Confidence: high (standard pubblicato).

[^10]: ITU-R F.1500 / F.1891, HAPS technical and operational characteristics. Applicato per INT-6B-FEEDER-*. Confidence: high.

[^11]: Reg. UE 2019/947 (UAS Operations) + AMC/GM Amendment 3 (Sett 2025) SORA 2.5 EU. Applicato per INT-6A-REG-001. Confidence: high.

[^12]: Reg. UE 2021/664 (U-Space regulatory framework). Applicato per INT-6A-REG-003. Confidence: high.

[^13]: GDPR Reg. UE 2016/679. Applicato per INT-6A-REG-004 + INT-X-PRIVACY-001. Confidence: high.

[^14]: D.Lgs. 138/2024 (recepimento Direttiva UE 2022/2555 NIS2). Applicato per INT-6A-REG-006 + INT-X-CYBER-001. Confidence: high.

[^15]: GAIA-X Compliance Framework v22.10 (e successive). Applicato per INT-X-CLOUD-001. Confidence: high.

[^16]: Cap. 4 §4.4 dello Studio (`studio-di-fattibilita/cap-04-scope-e-ICD.md`), ICD preliminare a 20 interfacce. Riferimento padre del presente Allegato. Confidence: high.

[^17]: Cap. 6 dello Studio (`studio-di-fattibilita/cap-06-analisi-tecnica.md`), Architettura 6A + 6B + verdetto tecnico. Riferimento architetturale. Confidence: high.

[^18]: Agenti `.claude/agents/avionics-gnc-engineer.md`, `telecom-ntn-payload-expert.md`, `aerodynamics-structures-engineer.md`, `earth-observation-expert.md`. Riferimenti specialistici. Confidence: high (interni progetto).

[^19]: Skill `epistemic-rigor`, disciplina falsifiability + triangulation + confidence levels applicata in tutto il documento. Confidence: high.

---

## A.4.10 Diagrammi di sistema

### A.4.10.1 Architettura sistema completo 6A (block diagram)

```
+-----------------------------------------------------------------------------------+
|                       PERCORSO 6A: SISTEMA COMPLETO VTOL                          |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|   +-------------------+                                                           |
|   |  AIR SEGMENT      |                                                           |
|   |  (VTOL JOUAV)     |                                                           |
|   |                   |     INT-6A-C2-001 (Uplink RF 2.4 GHz, OFDM)              |
|   |   +-----------+   |     INT-6A-C2-002 (Downlink Telemetry MAVLink)           |
|   |   | FCS +     |   | <=========================================>+             |
|   |   | Autopilot |   |     INT-6A-DATA-005 (Telemetry 10 Hz)      |             |
|   |   +-----------+   |     INT-6A-DATA-006 (Video Preview H.265)  |             |
|   |        ^          |                                            |             |
|   |        | INT-09   |     INT-6A-C2-003 (SATCOM L-band fallback) |             |
|   |        v          | <-------> Iridium NEXT LEO -----+          |             |
|   |   +-----------+   |                                 |          |             |
|   |   | Sensors:  |   |     INT-6A-C2-006 (ADS-B IN)    |          |             |
|   |   | IMU 3x    |   | <----- Air Traffic ADS-B        |          |             |
|   |   | GNSS 2-band   |     INT-6A-C2-008 (Geofence)    |          v             |
|   |   | Baro/Compass  |                                  |   +-------------+      |
|   |   +-----------+   |                                  +-->|  GROUND     |      |
|   |        ^          |                                      |  SEGMENT    |      |
|   |   +-----------+   |                                      |             |      |
|   |   | Modular   |   |                                      | +---------+ |      |
|   |   | Payload   |   |     INT-6A-DATA-001 (RGB GigE)      | | GS Fixed| |      |
|   |   | Bay       |   | <-- INT-6A-DATA-002 (IR USB 3.0)    | | Pentema | |      |
|   |   | EO/IR/    |   |     INT-6A-DATA-003 (NVMe storage)  | | (cont.) | |      |
|   |   | telecom   |   |                                      | +---------+ |      |
|   |   +-----------+   |     INT-6A-PHY-001 (Mech mount)     | +---------+ |      |
|   |        ^          |     INT-6A-PHY-002 (28V power)      | | GS      | |      |
|   |        | INT-6A-PHY-003 |                               | | Mobile  | |      |
|   |        | (Ethernet GigE)|                               | | (vehicle)| |     |
|   |        v          |                                      | +---------+ |      |
|   |   +-----------+   |                                      |             |      |
|   |   | Battery   |   |     INT-6A-PHY-006 (BMS, CAN)       | INT-6A-GS-001 HMI |
|   |   | LiPo 6S   |   |                                      | INT-6A-GS-002 Mobile|
|   |   | 22.2V     |   |                                      | INT-6A-GS-006 HMS |
|   |   +-----------+   |                                      +-------------+      |
|   +-------------------+                                            |              |
|                                                                    | INT-6A-PHY-010 (Backhaul)
|                                                                    | INT-6A-DATA-004 (S3 upload)
|                                                                    v              |
|                                                              +-------------+      |
|                                                              |  CLOUD IT/EU|      |
|                                                              | (Aruba/OVH) |      |
|                                                              | GAIA-X      |      |
|                                                              |             |      |
|                                                              | INT-6A-DATA-007 (Pipeline)
|                                                              | INT-6A-GS-007 (Anonymization)
|                                                              | INT-6A-GS-008 (Backup DR)
|                                                              | INT-X-LOGGING-001 (SIEM)
|                                                              +-------------+      |
|                                                                    |              |
|                                                                    | INT-6A-GS-003 (HTTPS)
|                                                                    v              |
|                                +-------------------+        +-------------+       |
|                                |  END USER:        |        | Cooperative |       |
|                                |  Cooperative      |<======>| Dashboard   |       |
|                                |  (Legacoop)       |  SPID  | (Web App)   |       |
|                                +-------------------+  SAML  +-------------+       |
|                                                                                   |
|                                +-------------------+                              |
|                                |  END USER:        |   INT-6A-GS-004              |
|                                |  Protezione Civile|<=====================+       |
|                                |  Sala Operativa   |   (SMS/PEC/Webform)         |
|                                +-------------------+                              |
|                                                                                   |
|   REGULATORY INTERFACES (compliance overlay):                                     |
|   - INT-6A-REG-001 (ENAC SORA SAIL III)    [Operatore <-> ENAC]                  |
|   - INT-6A-REG-002 (AGCOM Spectrum 2.4+L)  [Operatore <-> AGCOM]                  |
|   - INT-6A-REG-003 (ENAV / D-Flight U-Space)[GCS <-> USSP]                       |
|   - INT-6A-REG-004 (Garante DPIA)          [Operatore <-> Garante]               |
|   - INT-6A-REG-005 (Insurance EU 785/2004) [Operatore <-> Broker]                |
|   - INT-6A-REG-006 (NIS2 ACN)              [Operatore <-> ACN]                   |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### A.4.10.2 Architettura sistema completo 6B (block diagram)

```
+-----------------------------------------------------------------------------------+
|                  PERCORSO 6B: SISTEMA COMPLETO HALE STRATOSFERICO                 |
|                            (Quota 18-21 km, FL590-690)                            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                                                                                   |
|             +--------------------------------------------+                        |
|             |  HALE SOLARE                               |                        |
|             |  Wing 25-30 m, MTOW 80-150 kg              |                        |
|             |                                            |                        |
|             |  +------------+      INT-6B-PHY-001        |                        |
|             |  | Solar Array|<===== (Mech+Thermal Bond)  |                        |
|             |  | GaAs 25+ m2|                            |                        |
|             |  +------------+                            |                        |
|             |        v                                   |                        |
|             |  +------------+      INT-6B-PHY-003        |                        |
|             |  | LiS Battery|<===== (Thermal Mgmt)       |                        |
|             |  | 100+ kWh   |       Heater 50W cont      |                        |
|             |  +------------+                            |                        |
|             |        v                                   |                        |
|             |  +------------+      INT-6B-PHY-002        |                        |
|             |  | Airframe   |<===== (Spar-Fuselage Joint)|                        |
|             |  | CFRP/lino  |       Flutter margin >=20% |                        |
|             |  | hi-AR >25  |                            |                        |
|             |  +------------+                            |                        |
|             |        v                                   |                        |
|             |  +------------+      INT-6B-PHY-004        |                        |
|             |  | AESA       |<===== (Ka-band aperture)   |                        |
|             |  | Phased Arr |       256-element, 30x30cm |                        |
|             |  | 31 GHz     |                            |                        |
|             |  +------------+                            |                        |
|             |        ^                                   |                        |
|             |        | INT-6B-FEEDER-001 (DL 31-31.3 GHz)|                        |
|             |        | INT-6B-FEEDER-002 (UL 27.9-28.2 GHz)                      |
|             |        v                                   |                        |
|             +--------------------------------------------+                        |
|                            ^               ^                                      |
|                            |               |                                      |
|             +--------------|---------------|----------------------------+         |
|             |              |               |                            |         |
|             v              v               v                            v         |
|         +-------+    +-----------+    +-------+              +------------------+ |
|         | UE 1  |    | UE 2 IoT  |    | UE 3  |              | GATEWAY HAPS     | |
|         | 5G    |    | NTN       |    | Vehic |              | Ground Station   | |
|         | smart |    |           |    | 5G    |              | (Genova / La Spez)| |
|         | phone |    |           |    |       |              |                  | |
|         +-------+    +-----------+    +-------+              | Parabola 3-5 m   | |
|             ^              ^               ^                  | RX Ka-band       | |
|             |              |               |                  +------------------+ |
|             +--------------+---------------+                          |            |
|                            |                                          v            |
|                  INT-6B-NTN-001 (DL S-band 2.0-2.025 GHz)    INT-6B-FEEDER-003   |
|                  INT-6B-NTN-002 (UL S-band)                  (5G Core SBA, MPLS)  |
|                  INT-6B-NTN-003 (Doppler ±50 Hz)                      |            |
|                  INT-6B-NTN-004 (Inter-Beam HO)                       v            |
|                                                              +------------------+ |
|                                                              | 5G CORE NETWORK  | |
|                                                              | (TIM / Vodafone) | |
|                                                              | (or wholesale    | |
|                                                              |  via Open Fiber) | |
|                                                              +------------------+ |
|                                                                                   |
|   OPERATIONAL INTERFACES (HALE-specific):                                         |
|   - INT-6B-OPS-001 (HALE ATC ENAV)         [Ops Center <-> ACC Milano]           |
|   - INT-6B-OPS-002 (EUROCONTROL Cross-Border)[Ops Center <-> NM Brussels]        |
|   - INT-6B-OPS-003 (Launch/Recovery Site)  [HALE <-> Sarzana-Luni or Albenga]    |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### A.4.10.3 Data flow 6A (UAV → GS → Cloud → User)

```
+---------+      +---------+      +---------+      +---------+      +---------+
| Sensor  |      | Mission |      | Ground  |      | Cloud   |      | End User|
| (RGB/IR)|----->| Computer|----->| Station |----->| (Aruba) |----->| (Coop/PA)|
+---------+      +---------+      +---------+      +---------+      +---------+
   |                  |                |                |                |
   | INT-6A-DATA-001  |                |                |                |
   | (GigE Vision)    |                |                |                |
   | RGB 100MB/frame  |                |                |                |
   |----------------> |                |                |                |
   |                  |                |                |                |
   | INT-6A-DATA-002  |                |                |                |
   | (USB 3.0)        |                |                |                |
   | IR 9 Hz LWIR     |                |                |                |
   |----------------> |                |                |                |
   |                  |                |                |                |
   |       INT-6A-DATA-003             |                |                |
   |       (NVMe SSD R/W 1.5 GB/s)     |                |                |
   |       store onboard               |                |                |
   |                  | ============>  |                |                |
   |                  |                |                |                |
   |                  |   INT-6A-DATA-005 (MAVLink 10 Hz)               |
   |                  |   Telemetry real-time GS                         |
   |                  |--------------> |                |                |
   |                  |                |                |                |
   |                  |   INT-6A-DATA-006 (RTSP H.265)                  |
   |                  |   Video preview low-bitrate                      |
   |                  |--------------> |                |                |
   |                  |                |                                  |
   |                  |    POST-MISSION INGEST (NVMe rimovibile o WiFi 6) |
   |                  |                |                                  |
   |                  |                | INT-6A-PHY-010 + INT-6A-DATA-004 |
   |                  |                | (Fibra/FWA/Starlink + S3 API)    |
   |                  |                |--------------->|                 |
   |                  |                | 25-50 GB upload                  |
   |                  |                |                |                 |
   |                  |                |  INT-6A-DATA-007 (Pipeline)     |
   |                  |                |  Photogrammetry SfM             |
   |                  |                |  Pix4D/Agisoft                  |
   |                  |                |  30-120 min processing          |
   |                  |                |                | ============>  |
   |                  |                |                |                |
   |                  |                |  INT-6A-GS-007 (Anonymization) |
   |                  |                |  Face/plate blur AI inference  |
   |                  |                |  ≤ 5 min/ortofoto              |
   |                  |                |                | ============>  |
   |                  |                |                |                |
   |                  |                |  INT-6A-GS-003 (Dashboard)     |
   |                  |                |  HTTPS + SPID + RBAC polygon   |
   |                  |                |                |--------------->|
   |                  |                |                | GeoTIFF + PDF  |
   |                  |                |                |                |
   +------------------+----------------+----------------+----------------+
                           AUDIT TRAIL & LOGGING
                       INT-6A-DATA-008 + INT-X-LOGGING-001
                          (Syslog over TLS, CEF, SIEM)
```

### A.4.10.4 C2 link architecture (primary + secondary)

```
                         GROUND STATION (Pentema)
                                  |
                                  v
                    +---------------------------+
                    | RF Transceiver Microhard  |
                    | pMDDL2450 (2.4-2.485 GHz) |
                    +---------------------------+
                              ^      v
                              |      | INT-6A-C2-001 (Uplink RF OFDM)
                              |      | EIRP <= 100 mW or 1 W lic
                              |      | latency <= 100 ms one-way
                              |      | fade margin >= 12 dB
                              |      |
                INT-6A-C2-002 |      |
                  (Downlink   |      |
                Telemetry)    |      |
                MAVLink v2.0  |      |
                AES-256-GCM   |      v
                              |      \
                              |       \  RF LOS
                              |        \   ~50 km nominale
                              |         \    (Pentema effetto: ~20-30 km)
                              |          \
                              |           v
                            +---------------------------+
                            |  AIRBORNE                 |
                            |  RF Transceiver           |
                            |  Whip Antenna 5 dBi omni  |
                            +---------------------------+
                                  ^         ^
                                  |         |
                                  |         | INT-6A-C2-005
                                  |         | (Mutual TLS + JWT)
                                  |         |
                                  v         v
                            +---------------------------+
                            |  FCS (Flight Computer)    |
                            |                           |
                            |  +---------------------+  |
                            |  | INT-6A-C2-004       |  |
                            |  | Lost-Link Procedure |  |
                            |  | Trigger > 5s lost   |  |
                            |  | RTH automatic       |  |
                            |  +---------------------+  |
                            |                           |
                            |  +---------------------+  |
                            |  | INT-6A-C2-006       |  |
                            |  | ADS-B IN (DAA coop) |  |
                            |  +---------------------+  |
                            |                           |
                            |  +---------------------+  |
                            |  | INT-6A-C2-008       |  |
                            |  | Geofence enforcer   |  |
                            |  +---------------------+  |
                            +---------------------------+
                                       ^
                                       |
                                       | If RF link lost > 5s OR
                                       | shadow zone detected
                                       v
                            +---------------------------+
                            |  FALLBACK: Iridium Certus |
                            |  L-band 1616-1626.5 MHz   |
                            |  Patch antenna 70x70 mm   |
                            |  conformal                |
                            +---------------------------+
                                       ^
                                       | INT-6A-C2-003 (SATCOM)
                                       | Throughput 22-700 kbps
                                       | Latency one-way 200-400 ms
                                       | Coverage globale (66 sat LEO)
                                       v
                              +---------------------+
                              | Iridium NEXT LEO    |
                              | Constellation       |
                              +---------------------+
                                       |
                                       v
                              +---------------------+
                              | Iridium Gateway     |
                              | (terrestrial hub)   |
                              +---------------------+
                                       |
                                       v
                              +---------------------+
                              | GS Pentema          |
                              | (via IP backhaul)   |
                              +---------------------+
```

### A.4.10.5 HAPS service link + feeder link (6B)

```
                                            +-----------------+
                                            |  HALE @ 20 km   |
                                            |  station-keep   |
                                            |  ±5 km nominal  |
                                            +--+-----------+--+
                                               |           |
                                               |           |
                                               |           |
                       INT-6B-FEEDER-002       |           |    INT-6B-FEEDER-001
                       Ka UL 27.9-28.2 GHz     |           |    Ka DL 31-31.3 GHz
                       Gateway TX EIRP 70 dBW  |           |    HAPS TX EIRP 60 dBW
                       UL capacity 100M-1Gbps  |           |    DL capacity 1-10 Gbps
                       <-----------------------+           +----------------------->
                                               |           |
                                               |           |
                       INT-6B-NTN-001          |           |    INT-6B-NTN-002
                       DL S-band 2.0-2.025 GHz|           |    UL S-band paired
                       Cell 30-50 km diam      |           |    UE EIRP max 23 dBm
                       Per-beam 50-200 Mbps    |           |    UL bottleneck
                       <-----------------------+           +----------------------->
                                               |           |
                                               |           |
                                               v           v
       +----------------+          +----------+ +----------+          +----------------+
       | UE Smartphone  |          | UE IoT-NTN|| UE Vehicle           | Gateway HAPS   |
       | 5G NTN capable |          | sensor   | | 5G       |          | Genova or      |
       | 23 dBm EIRP    |          | low pwr  | | mobile   |          | La Spezia      |
       +----------------+          +----------+ +----------+          | Parabola 3-5m  |
                                                                       | Site diversity |
                                                                       +----------------+
                                                                              |
                                                                              | INT-6B-FEEDER-003
                                                                              | (5G Core SBA)
                                                                              | N2/N3 over MPLS
                                                                              v
                                                                       +----------------+
                                                                       | 5G CORE (TIM   |
                                                                       | / Vodafone)    |
                                                                       | AMF/SMF/UPF    |
                                                                       +----------------+
                                                                              |
                                                                              v
                                                                       +----------------+
                                                                       | Internet PA    |
                                                                       | Cooperative    |
                                                                       | Wholesale      |
                                                                       +----------------+
```

### A.4.10.6 Regulatory interfaces overlay

```
+-------------------------------------------------------------------+
|              FIRMAMENTO TECHNOLOGIES (Operatore)                   |
+-------------------------------------------------------------------+
       |                |                |                |
       v                v                v                v
+--------------+ +-------------+ +-------------+ +---------------+
|  ENAC        | |  AGCOM      | |  Garante    | |  ACN          |
|  Ufficio     | |  PNRF +     | |  Privacy    | |  (NIS2)       |
|  RPAS        | |  Codice CCE | |             | |               |
|              | |             | |             | |               |
| INT-6A-REG-001| INT-6A-REG-002| INT-6A-REG-004| INT-6A-REG-006 |
| SORA SAIL III| | Spectrum    | | DPIA + DSAR | | Incident      |
| BVLOS auth   | | 2.4 GHz +   | | Workshop    | | notification  |
| Pre-app M+3-6| | L-band      | | pubblico    | | 24h initial    |
| Final Fase 1 | | M+1-M+4     | | M+4-M+5     | | 72h detailed   |
+--------------+ +-------------+ +-------------+ +---------------+

+--------------+ +---------------+ +---------------+
|  ENAV /      | |  Insurance    | |  EUROCONTROL  |
|  D-Flight    | |  Broker       | |  (HALE 6B)    |
|  USSP        | |  (Lloyd/AON)  | |               |
|              | |               | |               |
| INT-6A-REG-003| INT-6A-REG-005 | | INT-6B-OPS-002|
| U-Space      | | Reg.UE 785/04 | | IFPS flight   |
| network ID + | | Massimale     | | plan          |
| flight auth  | | 750k DSP min  | | Cross-border  |
| Reg.UE 21/664| | (€870k)       | | coord         |
+--------------+ +---------------+ +---------------+

+--------------+ +---------------+
|  GAIA-X      | |  ITU-R        |
|  Compliance  | |  (long-term   |
|  (Cloud)     | |   HAPS coord  |
|              | |   6B)         |
| INT-X-CLOUD-001| INT-6B-FEEDER-* |
| Provider     | | Coordination  |
| Aruba/OVH    | | FSS Coexist   |
| Label Lvl 2+ | | post-WRC-23   |
+--------------+ +---------------+
```

---

## A.4.11 Note di chiusura

L'**ICD preliminare v1.0** rappresenta il **secondo livello di rigore** sulle interfacce di sistema HALE/VTOL Firmamento, dopo il livello concept del Cap. 4 §4.4. Con **59 interfacce dettagliate** organizzate in 7 categorie, l'ICD copre l'intero spettro di accoppiamenti del sistema:

- **40 interfacce 6A** (VTOL pilota TRL 8-9): prevalentemente Preliminary status con confidence medium-high, base solida per Detailed ICD v2.0 in Fase 1
- **14 interfacce 6B** (HALE stratosferico): prevalentemente Concept status con confidence low, in linea con stato R&D Phase B preparatorio
- **5 interfacce trasversali** (Cloud + Privacy + Cybersecurity + Vendor SLA): comuni 6A+6B, confidence prevalentemente high

### A.4.11.1 Falsifying observations critiche identificate (≥ 5)

L'ICD v1.0 identifica **8 falsifying observations critiche** (riferimento skill `epistemic-rigor` Regola 1):

1. **INT-6A-PHY-001**: se il vendor JOUAV (o eq.) non fornisce CAD interfacce, scatta re-engineering custom +€15-25k
2. **INT-6A-C2-001**: shadow zones C2 Pentema, switch automatico SATCOM entro 5s richiesto
3. **INT-6A-C2-004**: lost-link RTH path attraverso shadow zone GPS, mitigazione 3 waypoint intermedi
4. **INT-6A-C2-007**: se ENAC richiede DAA non-cooperativo certificato SAIL IV, Hold SORA submission
5. **INT-6A-REG-001**: se ENAC valuta Pentema 'area sensibile' (parco Aveto), SAIL IV +€200-400k + 6 mesi
6. **INT-6A-REG-002**: se AGCOM rifiuta licenza individuale 2.4 GHz > 100 mW, fallback ISM + SATCOM
7. **INT-6B-PHY-003**: se il thermal management heater supera 80W, l'energy balance inverno peggiora fino allo showstopper
8. **INT-6B-NTN-001**: spettro S-band n255 contestato MNO, no spectrum sharing, alternative C-band

### A.4.11.2 Action items prioritari per ICD v1.5 (M+6/M+8)

1. **Pre-engagement vendor** (M+1/M+6): validazione interfacce INT-6A-PHY-001, 002, 003 con JOUAV/Tekever/Quantum
2. **Pre-application ENAC/AGCOM** (M+1/M+4): feedback su INT-6A-REG-001/002
3. **DPIA finalization** (M+4/M+5): signature DPO su INT-6A-REG-004
4. **Workshop PC tabletop** (M+6/M+9): test scenario INT-6A-GS-004
5. **DTM Liguria + site analysis Pentema** (M+3/M+6): validazione INT-6A-PHY-008 + INT-6A-C2-001 shadow zones
6. **GAIA-X provider selection** (M+5/M+9): RFQ Aruba/OVH/IONOS per INT-X-CLOUD-001

### A.4.11.3 Punti di attenzione cross-document

L'ICD si accoppia strettamente con:

- **Cap. 4 §4.4**: riferimento padre (20 interfacce primarie)
- **Cap. 5** (Quadro Normativo): autorità coinvolte in REG interfaces
- **Cap. 6** (Analisi Tecnica): architettura sistema 6A + 6B con showstopper RSK-TEC-001/002
- **Allegato A.1 RTM**: tracciabilità requisiti → interfacce
- **Allegato A.2 Risk Register**: cross-reference con RSK-INT-* (12 rischi interfaccia)
- **Allegato A.5 V&V Plan**: pianificazione test methods per ciascuna interfaccia
- **Allegato A.10 Piano Manutenzione**: RCM derivata da INT-6A-GS-006 health monitoring

### A.4.11.4 Status finale documento

| Attributo | Valore |
|---|---|
| Versione | v1.0 (M+3 baseline) |
| Numero interfacce | 59 (40 6A + 14 6B + 5 X) |
| Status distribuzione | Concept: 31; Preliminary: 28; Detailed: 0 (deferito v2.0) |
| Confidence distribuzione | high: 16; medium: 28; low: 15; speculative: 0 |
| Falsifying observations | 8 critiche identificate |
| Risk Register interface | 12 rischi (5 P×I ≥ 15 red; 7 P×I 9-14 yellow) |
| Test Plan entries | 20 test campaign in 4 fasi |
| Versioning roadmap | 6 versioni v0.5 → v3.0 (Y0 → Y5) |
| Approval target | Senior SE + Integration Engineer Lead M+3 |

---

*Fine Allegato A.4: Interface Control Document (ICD) preliminare v1.0*

*Documento di lavoro generato in coerenza con ARP4754A + ISO/IEC/IEEE 24765 + NASA SE Handbook §6.3*
*Boundary conditions B1 + B2 preserve. Disciplina epistemica `epistemic-rigor` applicata.*
