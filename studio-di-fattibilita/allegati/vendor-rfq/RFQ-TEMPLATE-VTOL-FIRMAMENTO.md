# RFQ, Request for Quotation
## Sistema UAV VTOL per Missioni di Servizi Territoriali, Aree Interne Italia

> **Firmamento Technologies S.r.l.**
> Progetto HALE, Percorso 6A, Pilota Comune di Pentema (Torriglia, GE)
> Bando di riferimento: Cooding Prototypes (Coopfond / Legacoop)
>
> **Documento:** RFQ-FIRMAMENTO-VTOL-001
> **Versione:** 1.0 (template ufficiale M+3)
> **Data emissione:** [DD/MM/YYYY]
> **Riferimento DR:** DR-003 (TRL JOUAV CW-30E EASA-equivalent + quotation vendor + lead time)
> **Allegato a:** Studio di Fattibilità Vol. 1 Cap. 6 §6.3.1 (TS-PLATFORM-6A)
>
> **Bilingua IT/EN:** sezioni 3-6 in inglese per uso vendor internazionali.

---

## NOTA DI USO (NON PARTE DEL DOCUMENTO INVIATO)

Questo è un **template formale** da personalizzare prima dell'invio. Compilare i campi `[BRACKETS]` con i dati specifici della tornata RFQ (vendor target, deadline, contatti). La modalità di invio raccomandata è email PEC più courier tracked (raccomandata A/R), con cover letter (vedi `RFQ-cover-letter-template.md`).

**Lista invio raccomandata (M+3):**
1. JOUAV (CN, Plan A), via reseller EU (es. MARIDS Spagna, SUMEC) o direttamente sales@jouav.com
2. Tekever (PT, Plan B), direttamente info@tekever.com
3. (opzionale) Quantum Systems (DE), Trinity F90+ come fallback ulteriore
4. (opzionale) UAVOS / Skyfront come riserva tecnica

---

## Sezione 1, Soggetto richiedente

### 1.1 Dati anagrafici Firmamento Technologies

| Voce | Dato |
|---|---|
| Ragione sociale | Firmamento Technologies S.r.l. |
| Forma giuridica | Società a Responsabilità Limitata |
| Sede legale | [Indirizzo sede, CAP, Provincia] |
| P.IVA / Codice Fiscale | [P.IVA] |
| REA | [Registro Imprese] |
| PEC | [pec@firmamentotech.legalmail.it] |
| Rappresentante legale | [Nome Cognome] |
| Procurement contact | [Nome Cognome], [email], [+39 …] |
| Technical contact | [Nome Cognome, Systems Engineer], [email] |

### 1.2 Profilo dell'azienda

Firmamento Technologies S.r.l. è una **PMI innovativa italiana** operativa nel settore aerospaziale, con focus sullo sviluppo di una **piattaforma aerea senza pilota** per il **monitoraggio EO** (Earth Observation), **NTN connectivity** (Non-Terrestrial Network 3GPP) e **alert events** (antincendio, frane, alluvioni) destinati alle **Aree Interne italiane** (SNAI, Strategia Nazionale Aree Interne).

**Modello di business: service-only.** Firmamento non è un OEM aeronautico e **non rivende velivoli**. L'acquisizione del sistema UAV oggetto della presente RFQ è finalizzata **all'erogazione di servizi ricorrenti** verso PA (Protezione Civile, Vigili del Fuoco, Comuni, Regioni), cooperative agricole (rete Legacoop) e utility (TLC, energetiche).

**Stakeholder istituzionali del progetto:**
- Regione Liguria
- ENAC (Ente Nazionale Aviazione Civile)
- AGCOM (Autorità per le Garanzie nelle Comunicazioni)
- Protezione Civile (livello nazionale più regionale)
- Cooperative aderenti a Legacoop (10 cooperative, capofila Fabrica)

### 1.3 Bilingua / Bilingual notice

> **EN, About the requester**
> Firmamento Technologies S.r.l. is an Italian innovative SME developing an unmanned aerial platform for Earth Observation, NTN connectivity and alert services for Italy's Inner Areas. Firmamento operates a **service-only business model** and **does NOT resell aircraft**. The UAV system requested in this RFQ will be used internally to deliver recurring services to Italian public administration, cooperatives and utilities.

---

## Sezione 2, Scopo della RFQ

### 2.1 Oggetto

La presente RFQ richiede una **quotation strutturata** per la fornitura di:

- **N. 1 piattaforma UAV VTOL ibrido (fixed-wing transition)** o configurazione equivalente
- **Set di payload modulari** (EO RGB + IR LWIR + opzionale telecom LTE eNodeB)
- **N. 2 Ground Station** (1 fissa + 1 mobile)
- **Pacchetto software** (mission planning, autopilota, downlink, processing)
- **Training piloti più operatori** (5 persone, livelli base più advanced)
- **Supporto tecnico più manutenzione** orizzonte 5 anni (Y1-Y5)
- **Spare parts inventory** 3 anni più emergency restock policy

Configurazione operativa target: sito principale Pentema, Comune di Torriglia, Città Metropolitana di Genova (1100-1300 m AMSL). Tipologia missione BVLOS (Beyond Visual Line of Sight) in **Specific Category** EASA Reg. UE 2019/947, **SAIL II-III**. Profili missione: mapping, sorveglianza, antincendio precoce, monitoraggio frane, supporto telecom emergenza. Operatività Y1 circa 150-300 ore-volo, con scale-up Y2-Y3 a **flotta 3-5 piattaforme multi-regione**.

### 2.2 Scope quotation richiesta

| Lotto | Descrizione | Quantità Y1 | Quantità target Y2-Y3 (informativa) |
|---|---|---|---|
| **Lotto 1** | Piattaforma UAV + autopilota integrato | 1 | +2 / +3 |
| **Lotto 2** | Payload EO + IR + (opt.) telecom | 1 set | +1 set |
| **Lotto 3** | Ground Station fissa + mobile | 1+1 | +1 mobile aggiuntiva |
| **Lotto 4** | Training piloti + operatori | 5 pers. | +3 pers. |
| **Lotto 5** | Supporto tecnico + manutenzione 5 anni | – | – |
| **Lotto 6** | Spare parts inventory 3 anni + emergency | – | restock |

La quotation è richiesta come prezzo unitario per ogni lotto (€ EXW Italia più opzione DDP Pentema), bundle price (sconto su acquisto integrato lotti 1-5) e opzione TCO 5 anni (manutenzione più spare più supporto).

### 2.3 Bilingual scope statement

> **EN, Scope of RFQ**
> Firmamento Technologies requests a structured quotation for the supply of: (1) one VTOL hybrid fixed-wing UAV platform, (2) modular payload package (EO RGB + IR LWIR + optional telecom LTE eNodeB), (3) two ground stations (1 fixed + 1 mobile), (4) software package, (5) pilot training (5 persons), (6) 5-year technical support and maintenance, (7) 3-year spare parts inventory.
> The platform shall be operated in Specific Category BVLOS SAIL II-III under EASA Reg. UE 2019/947, in mountainous terrain (1100-1300 m AMSL) in Liguria, Italy.

---

## Sezione 3, Specifiche tecniche richieste / Technical Requirements

> **Nota:** ogni requisito è classificato **MUST** (obbligatorio, non negoziabile), **SHOULD** (preferenziale, deroghe motivate accettate) o **OPTIONAL** (su richiesta).
> Vendor request: please answer with `Comply / Comply with deviation / Non comply` for each requirement, with detailed evidence.

### 3.1 Piattaforma UAV / UAV Platform

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-UAV-001 | MTOW ≤ 40 kg (per consentire Specific Category, no Certified) | MUST | |
| RFQ-UAV-002 | Configurazione VTOL ibrido fixed-wing (transizione automatica) | MUST | |
| RFQ-UAV-003 | Autonomia operativa ≥ 6 h con payload 5-8 kg in condizioni nominali (sea level, vento ≤ 5 m/s, +15°C) | MUST | |
| RFQ-UAV-004 | Autonomia operativa ≥ 4 h in condizioni Pentema (1200 m AMSL, vento 5-10 m/s sustained, -5°C, payload pieno) | MUST | |
| RFQ-UAV-005 | Payload utile massimo ≥ 5 kg (target 8 kg) | MUST | |
| RFQ-UAV-006 | Velocità crociera 80-120 km/h | SHOULD | |
| RFQ-UAV-007 | Quota max operativa ≥ 4000 m AMSL | MUST | |
| RFQ-UAV-008 | Range C2 LOS ≥ 30 km (target 50 km) | MUST | |
| RFQ-UAV-009 | Range C2 BLOS via SATCOM ≥ 100 km | SHOULD | |
| RFQ-UAV-010 | Operating temperature -20°C / +50°C | MUST | |
| RFQ-UAV-011 | Resistenza pioggia ≥ 10 mm/24h, IP rating IP43 o superiore | MUST | |
| RFQ-UAV-012 | Vento sostenuto max ≥ 15 m/s, raffiche ≥ 18 m/s | MUST | |
| RFQ-UAV-013 | Propulsione ibrida (gasoline/heavy oil + battery) o full-electric con autonomia equivalente | SHOULD | |
| RFQ-UAV-014 | Parachute recovery system (FTS) per emergency landing | MUST | |
| RFQ-UAV-015 | Lights ICAO Annex 2 (anti-collision strobe + nav lights) | MUST | |
| RFQ-UAV-016 | ADS-B IN (receiver), preferibile ADS-B OUT (transmitter) per integrazione U-Space | SHOULD | |
| RFQ-UAV-017 | Take-off footprint ≤ 5×5 m (VTOL mode) | MUST | |
| RFQ-UAV-018 | Tempo set-up da casa pre-flight: ≤ 30 min per team 2 piloti | SHOULD | |
| RFQ-UAV-019 | MTBF dichiarata + track record (richiesto report incidenti aperti) | MUST | |

### 3.2 Payload modulare / Modular Payload

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-PL-001 | Interfaccia payload modulare standardizzata (mechanical + electrical + data) | MUST | |
| RFQ-PL-002 | Tempo swap payload in field ≤ 60 min con team 2 ops trained | MUST | |
| RFQ-PL-003 | Payload **RGB high-res** (target Phase One iXM 100 o equivalente, ≥ 100 MP, GSD ≤ 10 cm @ 500m AGL) | MUST | |
| RFQ-PL-004 | Payload **IR LWIR** (WIRIS Pro, FLIR Vue Pro R o eq., NEdT ≤ 50 mK, GSD termico ≤ 5m @ 500m) | MUST | |
| RFQ-PL-005 | Gimbal stabilizzato 3-assi per RGB+IR, IBIS o EIS | MUST | |
| RFQ-PL-006 | Payload **LiDAR** (YellowScan Voyager o eq., precisione ≤ 5 cm) | OPTIONAL Y2 | |
| RFQ-PL-007 | Payload **multispettrale** (MicaSense Altum-PT o eq., 4 bande VIS-NIR + termico calibrato) | OPTIONAL Y2 | |
| RFQ-PL-008 | Payload **telecom LTE eNodeB tattico** (Athonet, Druid, IP.access o eq.), capability 20+ utenti simultanei, raggio cella circa 3-5 km | OPTIONAL Y1 | |
| RFQ-PL-009 | Onboard storage payload data ≥ 512 GB redondante (RAID-style o dual SSD) | MUST | |
| RFQ-PL-010 | Encryption dati onboard (AES-256 at rest) | MUST | |

### 3.3 Ground Station / GS

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-GS-001 | GS fissa: container 20' o cabina prefabbricata, dotata di mission control + storage primario + link RF | MUST | |
| RFQ-GS-002 | GS mobile: console rugged + antenna torre ripiegabile su veicolo 4x4 | MUST | |
| RFQ-GS-003 | Antenne C2 RF + (opt.) SATCOM L-band Iridium/Inmarsat | MUST | |
| RFQ-GS-004 | UPS minimo 2h backup operativo per GS fissa | MUST | |
| RFQ-GS-005 | Interfaccia HMI multi-operator (pilota + payload op. simultanei) | MUST | |
| RFQ-GS-006 | Logging operazioni black-box compliant SORA OSO #11 (retention ≥ 30 gg) | MUST | |
| RFQ-GS-007 | Integrazione cloud IT/EU (Aruba/OVH) per long-term storage | SHOULD | |
| RFQ-GS-008 | Cyber hardening: penetration test report disponibile + DO-326A awareness | MUST | |

### 3.4 Software autopilota / FCS Software

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-SW-001 | Autopilota proprietario o open-source (es. Pixhawk/ArduPilot custom hardened) | MUST | |
| RFQ-SW-002 | Profilo Lost-Link configurabile (Return-to-Base, Land-at-current-position, Loiter, FTS) | MUST | |
| RFQ-SW-003 | Geofence dinamico (no-fly zones AGCOM/ENAC + privacy zones residenziali) | MUST | |
| RFQ-SW-004 | Mission planning offline + online sync | MUST | |
| RFQ-SW-005 | Telemetry data export in formato standard (MAVLink, JSON, KML, CSV) | MUST | |
| RFQ-SW-006 | API documentate per integrazione third-party (pipeline cloud Firmamento) | SHOULD | |
| RFQ-SW-007 | Update OTA (Over-The-Air) firmware + security patch (cadenza ≥ trimestrale) | MUST | |
| RFQ-SW-008 | Licenza software: perpetual o subscription? Specificare termini | MUST | |
| RFQ-SW-009 | Compatibilità con software italiani GIS open (QGIS) + processing fotogrammetrico (es. Pix4D, Agisoft) | SHOULD | |

### 3.5 Training piloti / Pilot Training

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-TR-001 | Training piloti operator livello base: ≥ 40h teoria + ≥ 20h volo simulator + ≥ 10h volo reale | MUST | |
| RFQ-TR-002 | Training advanced (BVLOS, emergencies, payload ops): ≥ 20h | MUST | |
| RFQ-TR-003 | Training tecnico manutenzione livello 1 (LRU swap, ground checks): ≥ 20h | MUST | |
| RFQ-TR-004 | Certificazione vendor rilasciata (attestato + competence card) | MUST | |
| RFQ-TR-005 | Lingua training: italiano o inglese; eventuale traduzione manualistica IT | SHOULD | |
| RFQ-TR-006 | Sede training: presso vendor (incluso travel/lodging?) o on-site Italia | MUST (specificare) | |
| RFQ-TR-007 | Training capacity totale: 5 persone (2 piloti + 2 op. payload + 1 tech) | MUST | |

### 3.6 Supporto tecnico più manutenzione 5 anni

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-MX-001 | Programma manutenzione preventiva schedulato (intervalli + check-list) | MUST | |
| RFQ-MX-002 | Manutenzione correttiva: SLA risposta ≤ 48h business hours, on-site ≤ 7 gg lavorativi | MUST | |
| RFQ-MX-003 | Hotline tecnica H24/7 per emergencies | SHOULD | |
| RFQ-MX-004 | Remote diagnostic capability (telemetria + log analysis) | MUST | |
| RFQ-MX-005 | Spare parts inventory: lista prezziario completa + stock policy | MUST | |
| RFQ-MX-006 | Spare parts critici (struttura, motore, FCS, batterie): stock 3 anni preacquistato | MUST | |
| RFQ-MX-007 | Emergency spare delivery: SLA ≤ 5 gg lavorativi per AOG (Aircraft On Ground) | MUST | |
| RFQ-MX-008 | MRO partner / authorized service center in Italia o EU | SHOULD | |
| RFQ-MX-009 | Warranty piattaforma: minimo 24 mesi o 500 ore-volo, whichever first | MUST | |
| RFQ-MX-010 | Extended warranty Y3-Y5: condizioni e costi | MUST | |

---

## Sezione 4, Compliance regolatoria richiesta / Regulatory Compliance

> **CRITICAL:** la non-compliance regolatoria EASA/ENAC è **show-stopper** per l'aggiudicazione. Il vendor è tenuto a fornire **evidenze documentali** (test reports, dichiarazioni di conformità, technical files).

### 4.1 EASA Reg. UE 2019/947 più 2019/945 (Specific Category)

| Req-ID | Requisito | Classe | Evidenza richiesta |
|---|---|---|---|
| RFQ-REG-001 | Conformità Reg. UE 2019/947, Specific Category SAIL II-III | MUST | Compliance matrix con riferimenti articoli + AMC |
| RFQ-REG-002 | Dichiarazione classe Reg. UE 2019/945 (C0-C6, oppure no-class per Specific) | MUST | Statement vendor + numero notifica |
| RFQ-REG-003 | Conformità AMC2 OSO #1, #2, #3, #4 (technical design + production) | MUST | Technical file UAS + production QC |
| RFQ-REG-004 | Conformità OSO #5, #6 (vendor-controlled procedures, maintenance) | MUST | Maintenance manual + procedure |
| RFQ-REG-005 | Conformità OSO #7, #8 (training) | MUST | Training syllabus + competence assessment |
| RFQ-REG-006 | Conformità OSO #9, #10 (UAS Lost-Link, ground control protection) | MUST | Test reports + design docs FCS Lost-Link |
| RFQ-REG-007 | Conformità OSO #11 (Fly-Away protection, geofencing) | MUST | Geofence implementation + test |
| RFQ-REG-008 | Conformità OSO #12, #13 (UAS Containment) | MUST | Containment design + parachute system spec |
| RFQ-REG-009 | Conformità OSO #14 (UAS Multiple Operations), se applicabile | SHOULD | |
| RFQ-REG-010 | Supporto vendor per SORA application (technical documentation contributo) | MUST | LoI / impegno scritto |

### 4.2 ENAC compliance Italia

| Req-ID | Requisito | Classe | Evidenza richiesta |
|---|---|---|---|
| RFQ-REG-011 | Idoneità per SORA SAIL II BVLOS in spazio aereo non controllato (G) | MUST | Vendor experience + reference |
| RFQ-REG-012 | Idoneità per SORA SAIL III BVLOS (upgrade Y2-Y3) | SHOULD | |
| RFQ-REG-013 | LRA (Light UAS Operator) ENAC pathway compatibility | SHOULD | |
| RFQ-REG-014 | Dichiarazione vendor che la piattaforma è stata operata da operatori autorizzati ENAC | SHOULD | |
| RFQ-REG-015 | Manualistica in italiano disponibile (POH, MM, Flight Manual) | SHOULD | |
| RFQ-REG-016 | Pre-application engagement ENAC / EASA: vendor disponibilità a partecipare a meeting | SHOULD | |

### 4.3 CE Marking più Direttiva Macchine 2006/42/CE

| Req-ID | Requisito | Classe | Evidenza richiesta |
|---|---|---|---|
| RFQ-REG-017 | Marcatura CE conforme Direttiva Macchine 2006/42/CE | MUST | Dichiarazione CE + technical file |
| RFQ-REG-018 | EMC Directive 2014/30/EU compliance | MUST | EMC test report (CISPR 11/22/32) |
| RFQ-REG-019 | RED Directive 2014/53/EU compliance (radio link) | MUST | RED test report (ETSI EN 300/301) |
| RFQ-REG-020 | LVD Directive 2014/35/EU compliance (componenti elettrici) | MUST | LVD declaration |

### 4.4 RoHS più REACH

| Req-ID | Requisito | Classe | Evidenza richiesta |
|---|---|---|---|
| RFQ-REG-021 | RoHS 3 Directive 2011/65/EU compliance (componenti elettronici) | MUST | RoHS declaration |
| RFQ-REG-022 | REACH Regulation 1907/2006 (chemical substances), SVHC list ≤ 0.1% w/w | MUST | REACH declaration |
| RFQ-REG-023 | WEEE Directive 2012/19/EU (end-of-life disposal) | MUST | Take-back commitment |
| RFQ-REG-024 | Battery Regulation 2023/1542 (batterie UAV) | MUST | Battery passport |

### 4.5 Cybersecurity (NIS2 più DO-326A)

| Req-ID | Requisito | Classe | Evidenza richiesta |
|---|---|---|---|
| RFQ-REG-025 | NIS2 Directive 2022/2555, vendor assessment cybersecurity | MUST | NIS2 self-assessment |
| RFQ-REG-026 | DO-326A / ED-202A airworthiness security awareness | SHOULD | DO-326A statement |
| RFQ-REG-027 | Penetration test report (PT esterno indipendente, ≤ 12 mesi) | MUST | Test report (executive summary OK, dettaglio sotto NDA) |
| RFQ-REG-028 | Encryption C2 link (AES-256 minimo, autenticazione mutua) | MUST | Crypto design statement |
| RFQ-REG-029 | Vulnerability disclosure policy + SBOM (Software Bill of Materials) | MUST | SBOM CycloneDX/SPDX format |
| RFQ-REG-030 | Update di sicurezza: cadenza + commitment temporale (≥ 5 anni) | MUST | Service Level Commitment |

### 4.6 AGCOM (uso frequenze)

| Req-ID | Requisito | Classe | Evidenza richiesta |
|---|---|---|---|
| RFQ-REG-031 | Frequenze C2 conformi PNRF italiano (banda ISM 2.4 GHz, 5.8 GHz, o altre licenziate AGCOM) | MUST | Frequency plan + power spectral density |
| RFQ-REG-032 | Compatibilità AGCOM Delibera 666/19/CONS (uso UAS) | MUST | Declaration |
| RFQ-REG-033 | SATCOM L-band o Ka-band: tipo terminale + provider compatibile (Iridium, Inmarsat, …) | MUST | Spec link + roaming agreement |

---

## Sezione 5, Termini commerciali / Commercial Terms

### 5.1 Prezzo unitario per piattaforma più opzioni

Il vendor fornisce **breakdown dettagliato** per:

| Lotto | Voce | Quantità | Prezzo unitario (€) | Sconto bundle | Totale (€) |
|---|---|---|---|---|---|
| **Lotto 1, Piattaforma** | UAV VTOL configurazione base | 1 | | | |
| | UAV VTOL options (es. heavy oil engine, payload bay extension, etc.) | – | | | |
| **Lotto 2, Payload** | Gimbal RGB high-res (es. iXM 100 eq.) | 1 | | | |
| | Sensore IR LWIR (WIRIS Pro eq.) | 1 | | | |
| | Telecom LTE eNodeB (opzionale Y1) | 1 | | | |
| | LiDAR (opzionale Y2) | 1 | | | |
| **Lotto 3, Ground Segment** | GS fissa container + antenna + console | 1 | | | |
| | GS mobile veicolo + console | 1 | | | |
| **Lotto 4, Training** | Pacchetto training 5 persone | – | | | |
| **Lotto 5, Supporto + manutenzione 5 anni** | Pacchetto annuo Y1-Y5 | 5 anni | | | |
| **Lotto 6, Spare parts** | Inventory 3 anni preacquistato + emergency restock policy | – | | | |
| | **TOTALE EXW Vendor** | | | | **€ ________** |
| | **TOTALE DDP Pentema (IT)** | | | | **€ ________** |

**Currency:** quotation in **EUR**. Se la base prezzo è altra valuta (USD, GBP, CNY), indicare cambio applicato e validità.

**Incoterms 2020:** EXW (vendor) e DDP (Pentema, IT) entrambe richieste. Indicare costi shipping più customs più insurance per opzione DDP.

### 5.2 Spare parts inventory (3 anni più emergency)

Il vendor fornisce la lista completa spare parts (LRU più consumable più structural critical) con part number e prezzo unitario, il recommended stock level per 3 anni operativi (assunzione 200-400 ore-volo/anno), l'SLA di emergency restock per AOG (Aircraft On Ground) e la pricing escalation clause sui prezzi spare nei 3 anni (es. CPI-indexed).

### 5.3 Lead time consegna

| Item | Lead time vendor → consegna (DDP Pentema) | Note |
|---|---|---|
| Piattaforma UAV completa | __ settimane / mesi | |
| Payload package | __ settimane / mesi | |
| Ground Station fissa | __ settimane / mesi | |
| Ground Station mobile | __ settimane / mesi | |
| Spare parts inventory iniziale | __ settimane / mesi | |
| Training (sede e calendario) | __ settimane / mesi | |
| **Full system operational** (post commissioning + training) | __ mesi totali | |

**Vincoli logistici:** il vendor dichiara la customs clearance pre-tested (esperienza export in Italia), gli eventuali permessi export richiesti (es. licenze dual-use) e i tempi tipici dogana Italia (settimane).

### 5.4 Warranty (anni più condizioni)

| Componente | Warranty base | Extended warranty (opz) | Coverage |
|---|---|---|---|
| Piattaforma UAV airframe | __ mesi / __ ore-volo | __ anni @ €__ | parts + labor / parts only |
| Engine / Propulsione | __ mesi | __ anni @ €__ | |
| Avionica / FCS | __ mesi | __ anni @ €__ | |
| Payload (RGB, IR, gimbal) | __ mesi | __ anni @ €__ | |
| Ground Station hardware | __ mesi | __ anni @ €__ | |
| Software (bug fix + security) | __ mesi (gratuito) | __ anni @ €__ | |

**Esclusioni:** specificare condizioni che invalidano la warranty (crash, abuso, alterazioni, ambient out-of-spec, ecc.).

**Procedura claim:** descrivere il process di warranty claim (notifica, RMA, turn-around time).

### 5.5 Termini di pagamento (milestones)

**Pagamento richiesto da Firmamento:**

| Milestone | % pagamento | Note |
|---|---|---|
| M1, Firma contratto | 20-30% | Anticipo |
| M2, Inizio produzione / FAT (Factory Acceptance Test) | 30-40% | Su verifica produzione |
| M3, Consegna DDP Pentema + SAT (Site Acceptance Test) | 20-30% | Su accettazione sito |
| M4, Training completato + commissioning | 10-15% | Su validazione operatività |
| M5, Hold-back warranty (12 mesi post-consegna) | 5-10% | A liberazione warranty period |
| **Totale** | **100%** | |

Il vendor può proporre milestones alternative motivate. Eventuali deroghe sui termini saranno oggetto di negoziazione.

**Strumenti di pagamento ammessi:** bonifico SEPA (preferito) o SWIFT internazionale.

### 5.6 Penalty per ritardo o non-conformità

Penalty consegna ritardata: 0.5% del valore contratto per settimana di ritardo (max 10% valore contratto). Un ritardo superiore a 6 mesi rispetto alla data contrattuale dà a Firmamento diritto di recesso unilaterale più restituzione anticipi versati.

Penalty non-conformità tecnica: la mancata compliance MUST requirements comporta rifiuto consegna più restituzione anticipi; la mancata compliance SHOULD requirements comporta riduzione prezzo da negoziare (5-15% del valore lotto interessato); il mancato superamento SAT (Site Acceptance Test) per due o più volte comporta penalty 5% valore contratto più rework a carico vendor.

Penalty SLA manutenzione: il mancato rispetto SLA manutenzione correttiva on-site (≥ 7 gg lavorativi) comporta penale €500/giorno; il mancato rispetto AOG spare delivery (≥ 5 gg lavorativi) comporta penale €1.000/giorno.

**Force majeure:** eccezioni standard (guerra, pandemia, sanzioni internazionali) per cause non imputabili al vendor.

---

## Sezione 6, Vincoli geopolitici e legali / Geopolitical and Legal Constraints

> **CRITICAL:** Firmamento Technologies opera in **ambito sovrano italiano/UE** con stakeholder istituzionali (ENAC, Regione Liguria, Protezione Civile). Il vendor deve garantire **continuità di fornitura** anche in scenari di tensione geopolitica internazionale.
> **CRITICAL EN:** Firmamento operates in sovereign IT/EU context with institutional stakeholders. Vendor must guarantee supply continuity also in international geopolitical tension scenarios.

### 6.1 Export licensing (ITAR, EAR, dual-use Reg. UE 2021/821)

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-GEO-001 | Dichiarazione **ITAR-free** (no US Munitions List items) | MUST | |
| RFQ-GEO-002 | Dichiarazione status EAR (Export Administration Regulations US): ECCN classification per ogni componente US-origin | MUST | |
| RFQ-GEO-003 | Conformità Reg. UE 2021/821 (dual-use): classification + license disponibile | MUST | |
| RFQ-GEO-004 | Componenti US ≥ 25% valore (de minimis rule): dichiarare | MUST | |
| RFQ-GEO-005 | Licenze export richieste paese di origine vendor → Italia: lista + timeline | MUST | |
| RFQ-GEO-006 | Impegno vendor a fornire **technical assistance** in caso di indagine export control italiana o EU | SHOULD | |

### 6.2 Sanzioni internazionali compliance

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-GEO-007 | Vendor + supply chain non in sanctions list OFAC, UE, UN (anti-money laundering check) | MUST | Self-declaration |
| RFQ-GEO-008 | Vendor non collegato (proprietà, controllo, contratti) a entità sanzionate RU, IR, KP, SY | MUST | |
| RFQ-GEO-009 | Tracciabilità supply chain componenti critici (cell origine, FPGA, sensori) | SHOULD | |
| RFQ-GEO-010 | Compliance commitment vs nuove sanzioni durante esecuzione contratto | MUST | |

### 6.3 Golden Power notifica (D.L. 21/2012, modif. D.L. 23/2020 più D.L. 50/2022)

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-GEO-011 | Acquisizione di asset aerospace da vendor extra-UE può triggera **Golden Power notifica** alla Presidenza Consiglio Ministri italiana | INFORMATIVA | Vendor acknowledge |
| RFQ-GEO-012 | Vendor disponibilità a fornire documentazione tecnica + corporate structure per istruttoria Golden Power se richiesto | MUST | Engagement statement |
| RFQ-GEO-013 | Vendor disponibilità ad accettare clausole contrattuali con escape clause in caso di esito Golden Power negativo | MUST | |

### 6.4 Sovranità dati operativi (cloud IT/EU mandatory)

| Req-ID | Requisito | Classe | Risposta vendor |
|---|---|---|---|
| RFQ-GEO-014 | Tutti i **dati operativi** (telemetria, payload data, logs) devono essere memorizzati e processati **solo su cloud IT o EU** (es. Aruba, OVH, Outscale, ecc.) | MUST | |
| RFQ-GEO-015 | Telemetria UAV NON deve essere trasmessa a server vendor extra-EU (es. server cinesi, server US privati vendor) senza autorizzazione esplicita Firmamento | MUST | |
| RFQ-GEO-016 | Componenti software vendor (mission planning, telemetry, ecc.) deployable **on-premise** senza chiamate esterne obbligatorie | MUST | Architecture diagram + network flows |
| RFQ-GEO-017 | Vendor accetta clausola contrattuale **data sovereignty IT/EU** + audit Firmamento dei flussi dati | MUST | |
| RFQ-GEO-018 | Conformità GDPR Reg. UE 2016/679 + Codice Privacy italiano (D.Lgs. 196/2003) per eventuali dati personali captati | MUST | DPIA support documentation |
| RFQ-GEO-019 | NIS2 Directive 2022/2555 compliance (vendor come fornitore essenziale digitale ICT) | MUST | NIS2 self-assessment |

---

## Sezione 7, Criteri di valutazione vendor / Vendor Evaluation Criteria

Le offerte sono valutate secondo i seguenti criteri pesati (metodologia di trade study Firmamento):

| Criterio | Peso | Sotto-criteri / Metriche |
|---|---|---|
| **Conformità tecnica** | 25% | % MUST compliant + % SHOULD compliant + qualità evidenze |
| **Compliance regolatoria** | 20% | EASA + ENAC + CE + cybersecurity (vedi §4) |
| **Costo iniziale (CapEx)** | 15% | Prezzo totale DDP Pentema (vedi §5.1) |
| **TCO 5 anni (CapEx + OpEx)** | 15% | Manutenzione + spare + supporto |
| **Risk geopolitico / supply chain** | 10% | Origine vendor + supply chain + export risk (vedi §6) |
| **Reference customers EU** | 5% | N. operatori EU + similarità use case |
| **Lead time** | 5% | Tempo consegna full system (vedi §5.3) |
| **Supporto IT/EU** | 5% | Presenza service center + lingua + canali |

**Soglia di esclusione automatica:** compliance MUST inferiore al 95%, mancanza di dichiarazione ITAR-free o EAR classification, vendor in sanctions list.

**Processo decisionale:** screening compliance (MUST requirements) a M+0; valutazione tecnica vs criteri pesati a M+1 (clarification round se necessario); negoziazione commerciale finalisti a M+2; Decision Review Board Firmamento a M+3; notifica vendor più contract drafting a M+3-4.

---

## Sezione 8, Timing e modalità di risposta

### 8.1 Calendario RFQ

| Fase | Data |
|---|---|
| Emissione RFQ | [DD/MM/YYYY] |
| **Deadline domande di chiarimento** | [DD/MM/YYYY] (15 gg da emissione) |
| Risposta Firmamento a chiarimenti | [DD/MM/YYYY] (5 gg da deadline domande) |
| **Deadline submission quotation** | [DD/MM/YYYY] (45 gg da emissione) |
| Round chiarimenti tecnici (eventuale) | [DD/MM/YYYY+15] |
| Notifica esito | [DD/MM/YYYY+90] |
| Negoziazione contratto (con finalist) | [DD/MM/YYYY+90 → +120] |
| **Decisione finale** | [DD/MM/YYYY+150] |

### 8.2 Modalità di submission

Submission richiesta in formato documento PDF firmato (signed) più Excel/CSV per breakdown prezzi (sez. 5.1). Lingua: italiano o inglese (entrambe accettate). Encryption: PDF protected with password (separate channel) per documenti sensibili.

**Canale di submission:**
- Email PEC: [pec@firmamentotech.legalmail.it] più email tecnica [procurement@firmamentotech.it]
- Subject: `RFQ-FIRMAMENTO-VTOL-001, Quotation Vendor [VENDOR NAME]`
- Allegati: massimo 50 MB per email; per file più grandi usare WeTransfer o SFTP separato

**Contatti per chiarimenti:**
- Procurement Manager: [Nome], [email], [telefono]
- Lead Systems Engineer (technical clarifications): [Nome], [email]

---

## Sezione 9, NDA più confidentiality / Non-Disclosure Agreement

### 9.1 NDA bidirezionale

L'invio della presente RFQ è subordinato alla firma di **NDA bidirezionale** tra Firmamento Technologies S.r.l. e il vendor.

Il template NDA di Firmamento è allegato (vedi Allegato A `NDA-FIRMAMENTO-VENDOR-template.pdf`). Il vendor può proporre modifiche o usare proprio template equivalente.

**Coverage NDA:** specifiche tecniche e operative scambiate; prezzi, termini commerciali, struttura business model Firmamento; identità degli stakeholder istituzionali e cooperative coinvolte; roadmap strategica Firmamento (10 anni vision); Risk Register tecnico-regolatorio.

**Durata NDA:** 5 anni dalla data di firma, salvo proroga per asset strategici.

**Eccezioni standard:** informazioni di dominio pubblico, indipendentemente sviluppate dal vendor, ottenute legittimamente da terzi.

### 9.2 Confidentiality vendor obligations

Il vendor si impegna a non divulgare l'esistenza della presente RFQ a competitori Firmamento (es. altri operatori di servizi VTOL Italia), a non utilizzare informazioni Firmamento per offrire servizi competitivi a terzi senza consenso scritto, a limitare l'accesso ai documenti RFQ al personale strettamente necessario (need-to-know basis) e a distruggere o restituire i documenti RFQ a conclusione del processo (entro 90 gg da notifica esito).

---

## Sezione 10, Allegati richiesti dal vendor / Vendor Submission Annexes

Insieme alla quotation, il vendor deve fornire i seguenti allegati obbligatori:

| Allegato | Descrizione | Formato | Lingua |
|---|---|---|---|
| **A.1** | Datasheet completo piattaforma + tutti i payload offerti | PDF | IT o EN |
| **A.2** | Compliance matrix EASA Reg. UE 2019/947 + 2019/945 + ENAC (vs requisiti §3-4) | Excel + PDF | IT o EN |
| **A.3** | Reference customers EU operativi (≥ 5 references, contact info verificabili) | PDF | IT o EN |
| **A.4** | Cybersecurity attestation: penetration test executive summary + SBOM | PDF (SBOM in CycloneDX/SPDX) | IT o EN |
| **A.5** | Insurance liability statement (vendor + manufacturer liability coverage) | PDF | IT o EN |
| **A.6** | Sample contract template (vendor standard contract) | PDF Word | IT o EN |
| **A.7** | Corporate structure + beneficial owners disclosure (per Golden Power / NIS2) | PDF | IT o EN |
| **A.8** | Quality management certification (es. ISO 9001, AS/EN 9100) | PDF | IT o EN |
| **A.9** | Manualistica POH (Pilot Operating Handbook) + MM (Maintenance Manual), campione | PDF | IT preferibile, EN accettato |
| **A.10** | Lista spare parts completa con part number + prezzi + lead time | Excel | IT o EN |
| **A.11** | NDA firmato (template Firmamento o equivalente) | PDF firmato | IT (italiano) o EN bilingual |
| **A.12** | Training syllabus dettagliato (modules + ore + valutazione) | PDF | IT preferibile |

**Allegati opzionali (premiati in valutazione):** flight test reports certificati (es. EASA SC-Light UAS, ENAC, FAA Part 107 / Part 137); LCA / Carbon footprint statement (per supporto narrativa ESG); reference papers e publications tecniche; award e certificazioni industria (Aerospace Excellence, NATO eligible vendor list).

---

## Disclaimer Firmamento

> La presente RFQ **non costituisce impegno contrattuale** da parte di Firmamento Technologies S.r.l. La quotation richiesta è valutativa.
> Firmamento si riserva il diritto di: non procedere all'aggiudicazione in qualsiasi fase del processo senza alcun onere; richiedere chiarimenti integrativi al vendor; modificare lo scope della fornitura sulla base delle risposte ricevute; aggiudicare a vendor che non ha la quotation di costo più bassa qualora la valutazione complessiva (vedi §7) sia superiore; aggiudicare per lotti separati a vendor diversi; estendere o ridurre il timing del processo.
>
> **EN, Disclaimer:** This RFQ does not constitute a contractual commitment from Firmamento Technologies S.r.l. Firmamento reserves the right to not proceed, request clarifications, modify scope, award to non-lowest bidder based on weighted evaluation, award separate lots, or extend timing.

---

## Approvazione interna Firmamento (NON inviare al vendor)

| Ruolo | Nome | Firma | Data |
|---|---|---|---|
| Procurement Manager | | | |
| Lead Systems Engineer | | | |
| CFO | | | |
| Legal Counsel | | | |
| Amministratore Delegato | | | |

---

**FINE DOCUMENTO RFQ-FIRMAMENTO-VTOL-001**

Documento bilingua IT/EN. Versione 1.0. Confidence: high (template strutturato, validato vs requirements Cap. 6 §6.3.1 e Cap. 8 §8.4.1 dello Studio di Fattibilità Firmamento).

Per chiarimenti sul template vedi `RFQ-cover-letter-template.md` (cover letter di accompagnamento).
