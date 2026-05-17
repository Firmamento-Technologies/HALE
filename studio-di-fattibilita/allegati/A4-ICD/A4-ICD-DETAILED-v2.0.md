# Allegato A.4: Interface Control Document (ICD) Detailed v2.0

> **Studio di Fattibilità: Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies, bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 2, Allegato A.4, Supplemento Detailed
>
> **Versione:** v2.0 (Detailed Engineering-Grade, 5 interfacce critiche Percorso 6A)
> **Baseline parent:** A4-ICD-PRELIMINARE-v1.0.md (M+3, Maggio 2026)
> **Data:** 2026-05-17
> **Trigger:** review critica Cap. 4 §4.8 Critica 2: ICD v1.0 "checklist di superficie, non design document"
> **Owner:** Avionics GNC Engineer (Firmamento Technologies)
> **Metodologia:** ARP4754A + DO-178C + DO-326A/ED-202A + NASA SE Handbook §6.3
> **Scope:** INT-03, INT-04, INT-05, INT-13, INT-15. Engineering-grade specification.

---

## Premessa

Questo documento costituisce il **Livello 2 (Detailed ICD)** della roadmap di versioning definita in A4-ICD-PRELIMINARE-v1.0 §A.4.8, prodotto in anticipo rispetto alla milestone nominale M+10/M+12 a seguito del rilievo review critica. Le 5 interfacce trattate sono quelle identificate come **flight-critical o safety-critical** per il Percorso 6A VTOL Pentema BVLOS.

Le rimanenti 15 interfacce (INT-01/02/06-12/14/16-20) restano a livello Preliminary v1.0 fino a M+10/M+12.

**Convenzione difformità rispetto a v1.0:** ogni campo che supera il dettaglio v1.0 è marcato con `[v2.0 NEW]`.

---

## Indice

- [INT-03: C2 RF Link (UAV ↔ GCS)](#int-03)
- [INT-04: C2 SATCOM Backup](#int-04)
- [INT-05: Payload-to-Avionics Interface](#int-05)
- [INT-13: DAA Detect-And-Avoid](#int-13)
- [INT-15: Privacy by Design (Blur On-Board)](#int-15)
- [Matrice di confronto v1.0 → v2.0](#confronto)
- [Gap residui per Fase 1 Engineering](#gap)
- [Riferimenti](#riferimenti)

---

<a name="int-03"></a>
## INT-03: C2 RF Link (UAV ↔ GCS)

### Scheda di identità

| Campo | Valore |
|---|---|
| **ID v2.0** | INT-6A-C2-001/002 (unificati in INT-03 per v2.0 spec) |
| **Nome** | C2 RF Link bidirezionale UAV ↔ GCS |
| **Tipo** | Funzionale control + safety (Flight-Critical) |
| **DAL equivalente** | DAL-B (DO-178C / ARP4754A); failure conduce a categoria Hazardous |
| **Endpoint A** | GS RF Transceiver: Microhard pMDDL2450 o Silvus StreamCaster SC-4200 |
| **Endpoint B** | UAV RF Transceiver: modulo integrato FCS JOUAV CW-30E (proprietario) |
| **Direzione** | Full-duplex TDD (Time Division Duplex) |
| **Status** | **Detailed** |
| **Confidence** | **medium**; specifiche MAVLink consolidate, comportamento FCS JOUAV proprietario non ancora documentato dal vendor |
| **Cross-ref RTM** | SyRq-C2-001, SyRq-C2-002, SyRq-C2-005 |
| **Cross-ref Risk** | RSK-INT-001, RSK-TEC-003 |

### Protocol Stack OSI L1-L7

```
┌─────────────────────────────────────────────────────────────────┐
│ L7 Application │ MAVLink v2.0 dialect (Common + JOUAV ext.) │
│ L6 Presentation │ AES-256-GCM (payload encryption) │
│ L5 Session │ MAVLink session (SYSTEM_ID / COMP_ID) │
│ L4 Transport │ UDP/IP (primario) o raw serial (fallback) │
│ L3 Network │ IP punto-punto (subnet /30) o no-IP serial │
│ L2 Data Link │ CSMA/TDD frame; CRC-X25 per MAVLink packet │
│ L1 Physical │ OFDM 2400-2483.5 MHz; BPSK/QPSK/16QAM/ │
│ │ 64QAM adattivo; DSSS fallback (link budget) │
└─────────────────────────────────────────────────────────────────┘
```

**Note L1:** Frequenza nominale 2.4 GHz ISM (EN 300 328 v2.2.1, RED 2014/53/EU). Potenza EIRP ≤ 20 dBm (100 mW) senza licenza individuale AGCOM, ≤ 30 dBm (1 W) con licenza individuale (iter AGCOM stimato 60-90 gg da domanda). Antenna ground: yagi direzionale 15 dBi + tracking. Antenna UAV: dipolo omnidirezionale 2 dBi.

**Note L2:** Frame TDD con ciclo 10 ms: 7 ms downlink (telemetry + video), 3 ms uplink (comandi). Il CRC-X25 (CRC-16/MCRF4XX, polinomio 0x1021, init 0xFFFF) viene calcolato sull'intero MAVLink v2.0 packet (header + payload), come definito in MAVLink Common Message Set §2.4 [^MAVLink].

### MAVLink v2.0: messaggi tipici JOUAV CW-30E

**Formato header MAVLink v2.0 (10 byte fissi):**

```
Byte 0: Magic (0xFD)
Byte 1: Payload length (0-253)
Byte 2: Incompat flags
Byte 3: Compat flags
Byte 4: Packet sequence (0-255 wrap)
Byte 5: System ID (UAV=1, GCS=255)
Byte 6: Component ID (autopilot=1, payload=100, GCS=0)
Byte 7-9: Message ID (24-bit little-endian)
Byte 10-N: Payload (variable)
Byte N+1-N+2: CRC-X25 (2 byte, little-endian)
[Byte N+3-N+25: Signature (25 byte, se MAVLINK_IFLAG_SIGNED)]
```

**Messaggi operativi primari, rate e payload:**

| MSG ID | Nome | Rate Hz | Payload byte | Direzione | Note |
|---|---|---|---|---|---|
| 0 | HEARTBEAT | 1 | 9 | bidirezionale | autopilot_type=MAV_TYPE_VTOL_TAILSITTER (20); base_mode bit flags |
| 1 | SYS_STATUS | 1 | 31 | UAV→GCS | battery voltage mV, current cA, % remaining; errors_count sensor failure bitmap |
| 30 | ATTITUDE | 10 | 28 | UAV→GCS | roll/pitch/yaw rad; rollspeed/pitchspeed/yawspeed rad/s (float32 × 6) |
| 32 | LOCAL_POSITION_NED | 5 | 28 | UAV→GCS | x/y/z m; vx/vy/vz m/s (float32 × 6, frame LOCAL_NED) |
| 33 | GLOBAL_POSITION_INT | 5 | 28 | UAV→GCS | lat/lon 1e7 deg (int32); alt/relative_alt mm (int32); vx/vy/vz cm/s (int16) |
| 65 | RC_CHANNELS | 2 | 42 | UAV→GCS | 18 canali uint16 (1000-2000 µs PWM) + RSSI 0-254 |
| 74 | VFR_HUD | 2 | 20 | UAV→GCS | airspeed/groundspeed m/s; heading deg; throttle %; alt/climb m/m/s |
| 76 | COMMAND_LONG | on-demand | 33 | GCS→UAV | target_system, target_component, command MAV_CMD, confirmation, param1-7 |
| 77 | COMMAND_ACK | on-demand | 10 | UAV→GCS | command echo, result MAV_RESULT (0=ACCEPTED…4=FAILED), progress, result_param2 |
| 83 | ATTITUDE_TARGET | 5 | 37 | GCS→UAV | type_mask byte; q[4] float; body_roll/pitch/yaw_rate; thrust float |
| 85 | POSITION_TARGET_GLOBAL_INT | 2 | 51 | GCS→UAV | type_mask; lat/lon int32; alt/vel/acc/yaw targets |
| 105 | HIGHRES_IMU | 10 | 62 | UAV→GCS | acc/gyro/mag 3-axis float; abs_pressure; diff_pressure; temperature |
| 147 | BATTERY_STATUS | 1 | 41 | UAV→GCS | voltages[10] mV; current cA; battery_remaining %; time_remaining s |
| 253 | STATUSTEXT | on-demand | 54 | bidirezionale | severity MAV_SEVERITY (0-7); text[50] ASCII; id uint16 |

**Comandi MAV_CMD critici (COMMAND_LONG param1-7):**

| MAV_CMD | Codice | Azione | Trigger condizione |
|---|---|---|---|
| MAV_CMD_NAV_RETURN_TO_LAUNCH | 20 | RTL immediato | Lost-link > 5 s (automatico FCS) |
| MAV_CMD_NAV_LOITER_UNLIMITED | 17 | Loiter in posizione corrente | Lost-link 3-5 s (pre-RTL warning) |
| MAV_CMD_DO_SET_MODE | 176 | Cambio flight mode | GCS operator command |
| MAV_CMD_COMPONENT_ARM_DISARM | 400 | Arm/Disarm motori | Pre-flight / emergency |
| MAV_CMD_NAV_LAND | 21 | Atterraggio autonomo | Emergency land procedure |
| MAV_CMD_DO_CHANGE_SPEED | 178 | Cambio velocità | Mission replanning |
| MAV_CMD_NAV_WAYPOINT | 16 | Waypoint navigation | Missione autonoma |

**Throughput aggregato nominale:**

```
Uplink (GCS→UAV): COMMAND_LONG on-demand ~5 pkt/s × 33+10 B = ~215 B/s
Downlink (UAV→GCS): telemetry aggregata ≈ 10 Hz × 200 B/pkt = ~2000 B/s
 + video preview H.265 (INT-6A-DATA-006) = 0.5-2 Mbps separato
Bitrate C2 netto richiesto: ~50-100 kbps (solo MAVLink, senza video)
```

### [v2.0 NEW] AES-256-GCM: Nonce Management

La cifratura del payload MAVLink v2.0 utilizza **AES-256-GCM** (AEAD, Authenticated Encryption with Associated Data) come definito in NIST SP 800-38D e richiesto da DO-326A §6.3.2 per link C2 airworthiness security.

**Struttura frame cifrato:**

```
┌──────────────────────────────────────────────────────────────┐
│ MAVLink v2.0 header (10 byte in chiaro, ASSOCIATED DATA) │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ AES-256-GCM Ciphertext (payload cifrato) │ │
│ │ + GCM Tag (16 byte, autenticazione) │ │
│ └────────────────────────────────────────────────────────┘ │
│ MAVLink signature field (25 byte): │
│ link_id (1B) | timestamp_48 (6B) | signature (13B→GCM Tag)│
└──────────────────────────────────────────────────────────────┘
```

**Nonce construction (96-bit / 12 byte):**

```
Nonce = LINK_ID (8 bit) || SYSTEM_ID (8 bit) || COMP_ID (8 bit)
 || SEQUENCE_48 (48 bit) || DIRECTION_BIT (1 bit) || RESERVED (7 bit)

dove SEQUENCE_48 = MAVLink timestamp_48 (µs epoch, resolution 10 µs)
 DIRECTION_BIT = 0 (GCS→UAV uplink), 1 (UAV→GCS downlink)
```

**Requisiti nonce:**
- Nonce mai riutilizzato con la stessa chiave (AES-256-GCM nonce-reuse vulnerability)
- SEQUENCE_48 incrementato monotonicamente; il wrap-around reset forza re-keying
- Re-keying obbligatorio ogni **2^32 frame** (circa 4 miliardi di pacchetti, circa 50 giorni a 1 kHz) o ogni **24 ore operative** (whichever first)
- Key derivation: ECDH P-256 a pre-flight (a terra, non in volo); chiavi distribuite via QR code cifrato o NFC su hardware security token (vedi INT-6A-C2-005 cybersecurity)

**GCM Tag verification:** il ricevitore verifica il tag a 128 bit prima di processare il comando. I pacchetti con tag non valido vengono scartati silenziosamente, con incremento del contatore CRYPTO_FAILURE_COUNT. Se CRYPTO_FAILURE_COUNT supera 10 in 1 s, il sistema genera un log STATUSTEXT severity=ERROR e un alert GCS.

### [v2.0 NEW] CRC-X25: dettaglio

Il CRC-X25 MAVLink v2.0 usa CRC-CCITT (0x1021) con:
- Init value: 0xFFFF
- Poly: 0x1021 (CCITT)
- Input: tutti i byte del header + payload (da byte 1 a N, escludendo magic 0xFD)
- **CRC_EXTRA byte**: ogni message ID ha un byte extra (derivato dalla definizione XML del messaggio) concatenato prima del calcolo CRC per prevenire incompatibilità di versione dialect
- Output: 2 byte little-endian

**Esempio HEARTBEAT (MSG_ID=0, CRC_EXTRA=50=0x32):**
```
CRC calcolato su: [len=9][incompat][compat][seq][sysid][compid][0x00][0x00][0x00] + payload[9] + [0x32]
```

### [v2.0 NEW] Retry Logic e Link Drop Fallback

**Definizione "link drop":** assenza di HEARTBEAT valido ricevuto dall'UAV per un intervallo di tempo determinato. HEARTBEAT atteso a 1 Hz (periodo 1 s).

**Stato macchina lost-link (FCS state machine):**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ LINK MONITORING STATE MACHINE │
│ │
│ LINK_OK ──────── last_heartbeat_age > 2s ──────► LINK_DEGRADED │
│ ▲ │ │
│ │ heartbeat received │ age > 3s │
│ │ ▼ │
│ └────────────────────────────── LINK_WARNING ◄──────┘ │
│ │ │
│ │ age > 5s (consecutive) │
│ ▼ │
│ LINK_LOST ───► TRIGGER RTL │
│ │ │
│ │ age > 30s (RTL unreachable) │
│ ▼ │
│ EMERGENCY_LAND ───► descend + land │
└─────────────────────────────────────────────────────────────────────────┘
```

**Timer e azioni per ogni stato:**

| Stato | Condizione ingresso | Durata max | Azione FCS | Alert GCS |
|---|---|---|---|---|
| LINK_OK | heartbeat age ≤ 2 s | n/a | Normale | n/a |
| LINK_DEGRADED | heartbeat age 2-3 s | 1 s | Throttle back 10%, prepara RTH waypoint | WARNING amber |
| LINK_WARNING | heartbeat age 3-5 s | 2 s | Switch tentativo SATCOM (INT-04) | WARNING red + audio |
| LINK_LOST | heartbeat age > 5 s consecutivi | n/a | **RTL automatico** (MAV_CMD_NAV_RETURN_TO_LAUNCH) | CRITICAL + SMS PC |
| EMERGENCY_LAND | RTL fail o fuel/battery critical | n/a | **Land in situ** (MAV_CMD_NAV_LAND) su pre-computed safe zone | CRITICAL + 406 MHz ELT |

**COMMAND_LONG retry per uplink (GCS→UAV):**

```
Protocollo retry:
1. GCS invia COMMAND_LONG (confirmation=0)
2. Attende COMMAND_ACK entro T_ack = 500 ms
3. Se no ACK: retransmit con confirmation++ (max 3 tentativi)
4. Se no ACK dopo 3 tentativi: log + escalate a pilot alert
5. Per comandi safety-critical (RTL, LAND): confirmation ignorata dopo LINK_LOST
 (FCS esegue autonomamente senza attendere ACK uplink)

T_ack = 500 ms (≤ latency budget 250 ms × 2 = margine 500 ms round-trip)
Max retry = 3
Total timeout per comando = 500 ms × 3 = 1.5 s
```

**Sequenza timing link drop → RTL:**

```
t=0: ultimo HEARTBEAT valido ricevuto
t=2s: LINK_DEGRADED, prepara RTH waypoint, throttle -10%
t=3s: LINK_WARNING, tentativi switch SATCOM (vedi INT-04)
t=5s: LINK_LOST, esegue RTL autonomo (no uplink richiesto)
t=5s+Δ: UAV vira verso home waypoint pre-caricato a pre-flight
t=5s+60s-120s: stimata rientro (dipende da distanza, circa 5-10 km/min)
t=RTL+30s: GCS tenta riconnessione ogni 5 s durante RTL
```

**[v2.0 NEW] Comportamento con link parzialmente degradato (NLOS orografia Pentema):**

Nelle shadow zone orografiche previste in Val Trebbia e Val Pentemina, il link può presentare:
- RSSI < -85 dBm, PER (Packet Error Rate) > 20%, heartbeat intermittenti
- Scenario: 3 heartbeat consecutivi mancati su 5 (entro finestra 5 s), trigger LINK_LOST

Per evitare false LINK_LOST in condizioni di link degradato, il FCS adotta il criterio:
- **LINK_LOST** = 5 heartbeat consecutivi mancati (non window-based)
- In accordo con RTCA DO-377A §3.4.2 [^DO377]: "consecutive loss" più robusto di "window loss" per link RF a riflessioni

### Latency Budget

| Segmento | Latenza one-way | Note |
|---|---|---|
| Applicazione GCS (generazione comando) | 5 ms | Software GCS processing |
| Encoding MAVLink + AES-GCM | 2 ms | Microhard hardware AES accelerator |
| Codifica RF + modulazione | 1 ms | OFDM framing |
| Propagazione RF (LOS, 50 km) | 0.17 ms | c = 3×10⁸ m/s |
| Demodulazione UAV | 1 ms | n/a |
| Decifrazione AES-GCM + CRC verify | 2 ms | n/a |
| FCS processing (autopilot loop) | 5 ms | JOUAV FCS tipicamente 10 Hz loop = 100 ms loop time |
| **Totale one-way (GCS→UAV comandi)** | **≈ 16 ms** | **Margine rispetto a 250 ms: +234 ms** |
| RTT comandi + ACK | ≈ 32 ms | Entro limite DO-377A pilot-in-the-loop |

**[v2.0 NEW] Latency budget con NLOS (shadow zone Pentema):**
- In NLOS, il multipath introduce delay spread fino a 5 µs (trascurabile a L7)
- OFDM cyclic prefix 800 ns di copertura: sufficiente per delay spread < 800 ns
- Se NLOS severo: il link margin scende sotto 6 dB, BER > 10^-3, ARQ L2, latency +10-50 ms
- Budget worst-case NLOS: circa 80 ms one-way, ancora entro 250 ms

### Error Detection

| Strato | Meccanismo | Copertura |
|---|---|---|
| L1 | FEC convolutivo rate 1/2, K=7 (Viterbi) | BER < 10^-6 a SNR ≥ 10 dB |
| L2 | CRC-X25 (16 bit) sul packet MAVLink | HD=4 per burst error ≤ 4 bit |
| L6 | AES-256-GCM Tag (128 bit) | Autenticazione + integrità payload |
| L7 | MAVLink sequence number | Rilevazione packet loss + out-of-order |

### Standard di riferimento

Il link C2 RF si conforma a: MAVLink Common Message Set v2.0 dialect [^MAVLink]; RTCA DO-377A "Minimum Operational Performance Standards for C2 Link Systems" [^DO377]; DO-326A / ED-202A "Airworthiness Security Process Specification" [^DO326A]; EN 300 328 v2.2.1 "WLAN/ISM 2.4 GHz harmonized standard EU"; NIST SP 800-38D "Recommendation for GCM (AES-GCM)" [^NIST38D]; JARUS SORA 2.5 Annex F §4.2 sui requisiti lost-link procedure.

### Failure Mode Behavior

| Failure Mode | Effetto | Categoria (ARP4761) | Mitigation |
|---|---|---|---|
| RF link drop > 5 s | LINK_LOST → RTL auto | Hazardous (DAL-B) | Doppio link + RTL logic FCS |
| Crypto failure (GCM tag invalid) | Packet scartato | Major (DAL-C) | Counter + alert; non esegue comando non autenticato |
| CRC failure | Packet scartato | Minor (DAL-D) | Sequence counter gap alert |
| Nonce wrap-around | Re-keying obbligatorio | Major (DAL-C) | Timer pre-flight check; auto re-key a terra |
| FCS loop crash | No command processing | Catastrophic (DAL-A) | FCS watchdog + redundant CPU (vendor JOUAV) |
| GCS software crash | No uplink | Hazardous (DAL-B) | LINK_LOST timer in FCS indipendente |

### Test Plan

| ID Test | Descrizione | Fase | Metodo | Pass Criteria |
|---|---|---|---|---|
| T-INT03-01 | MAVLink message decode fidelity | DDT (M+10) | Bench test: replay pcap MAVLink vs reference decoder | 0 decoding errors su 10.000 frame |
| T-INT03-02 | AES-256-GCM encrypt/decrypt latency | DDT (M+10) | Oscilloscopio su HW accelerator; 10.000 frame | Latency ≤ 3 ms @ 99th percentile |
| T-INT03-03 | CRC-X25 bit error injection | DDT (M+10) | Fault injector: flip 1-4 bit in payload | 100% detection su 1000 corrupted frames |
| T-INT03-04 | Link drop → RTL timing | HIL (M+14) | Hardware-in-the-loop: disconnetti RF transceiver | RTL trigger in 5.0 ± 0.5 s |
| T-INT03-05 | Link drop in shadow zone | Field test (M+18) | Valle Pentema: drone a distanza variabile | Riconnessione SATCOM entro 3 s; RTL se no SATCOM |
| T-INT03-06 | Nonce uniqueness stress test | DDT (M+11) | 10^8 frame su banco; verifica no nonce reuse | 0 nonce collisions |
| T-INT03-07 | GCS crash → RTL autonomo | HIL (M+15) | Kill GCS process; monitor FCS behavior | RTL in ≤ 5 s dal LINK_LOST |

---

<a name="int-04"></a>
## INT-04: C2 SATCOM Backup Link

### Scheda di identità

| Campo | Valore |
|---|---|
| **ID v2.0** | INT-6A-C2-003 (aggiornato a INT-04 per v2.0) |
| **Nome** | C2 Secondary SATCOM Link (backup RF primario) |
| **Tipo** | Funzionale control + safety (Flight-Critical) |
| **DAL equivalente** | DAL-B (backup safety-critical per BVLOS Pentema) |
| **Endpoint A** | GCS SATCOM modem (a terra) |
| **Endpoint B** | UAV SATCOM modem airborne |
| **Direzione** | Full-duplex (asimmetrico) |
| **Status** | **Detailed** |
| **Confidence** | **medium**; specifiche Iridium/Inmarsat/Starlink consolidate, latency end-to-end Pentema non ancora misurata |
| **Cross-ref RTM** | SyRq-C2-003, SyRq-C2-006 |
| **Cross-ref Risk** | RSK-INT-001, RSK-REG-002 |

### Architettura a tre livelli (link hierarchy)

```
┌──────────────────────────────────────────────────────────────────────┐
│ C2 LINK HIERARCHY: PERCORSO 6A │
│ │
│ LIVELLO 1 (PRIMARY): RF 2.4 GHz ISM / Licensed │
│ LIVELLO 2 (SECONDARY): SATCOM (selezione per scenario, vedi sotto)│
│ LIVELLO 3 (FALLBACK): Loiter → RTL → Emergency Land │
│ │
│ Escalation logic: │
│ t=0-3s link degraded → SATCOM switch attempt │
│ t=3-5s no RF + no SATCOM → LINK_LOST → RTL (Livello 3) │
└──────────────────────────────────────────────────────────────────────┘
```

### Comparazione tecnologie SATCOM (trade specifico INT-04)

| Parametro | Iridium Certus 100 | Inmarsat BGAN / IsatPhone | Starlink Aviation Mini |
|---|---|---|---|
| Costellazione | LEO 66 sat, 780 km | GEO (Inmarsat I-4/I-5/I-6) | LEO ~5500 sat, 550 km |
| Bitrate uplink | 22 kbps | 432 kbps (BGAN) | 20-40 Mbps |
| Bitrate downlink | 352 kbps | 432 kbps | 50-200 Mbps |
| Latency one-way | ~800 ms - 1.5 s | ~240-280 ms (GEO) | ~25-50 ms |
| Latency RTT | ~1.5-3 s | ~480-560 ms | ~50-100 ms |
| Coverage Italia | Globale (polar) | Globale incl. Liguria (el. ≥ 5°) | Globale (con Starlink coverage map verificata) |
| Elevazione minima | 8° (Iridium LEO coverage) | 20° (GEO I-4F2 @19.2°E) | 25° (consigliato per Starlink) |
| Peso modem UAV | Iridium 9770: 45 g + antenna | Inmarsat SAILOR 250: 320 g | Starlink Mini: 1.1 kg (ECCESSIVE per CW-30E) |
| Costo mensile | €150-300/mese (IPTRS) | €200-500/mese | €250/mese (Starlink Roam) |
| Protocollo dati | IP/PPP over serial | IP/PPP | TCP/IP Ethernet |
| Autorizzazione AGCOM | Licenza individuale (L-band 1616-1626.5 MHz) | Licenza individuale (L-band 1525-1559 MHz) | Licenza Ka-band (AGCOM) |
| Conformità BVLOS | Idoneo (C2 latency ≤ 1.5 s accettabile per RTL) | Idoneo (GEO latency 280 ms borderline per pilot-in-loop) | Idoneo (latency eccellente) ma peso UAV modem critico |
| **Verdetto per CW-30E** | **SELEZIONATO PRIMARY SATCOM** | Backup secondario | **NON idoneo** per peso (1.1 kg eccede budget massa) |

**Giustificazione selezione Iridium Certus 100:**
1. Peso modem UAV 45 g compatibile con budget massa CW-30E payload ≤ 500 g per SATCOM
2. Copertura polare garantita, nessuna shadow zone satellitare (solo orografica)
3. Bitrate 352 kbps downlink sufficiente per MAVLink telemetry (< 100 kbps necessari)
4. Latency 1.5 s accettabile: non per pilot-in-the-loop manovre tattiche, ma per RTL command e telemetry monitoring durante BVLOS
5. L-band (1616-1626.5 MHz) presenta attenuazione rain fade < 1 dB @ Liguria (ITU-R P.618-14), affidabilità > 99.9%

**Limitazione nota:** la latency Iridium 1.5 s supera il limite DO-377A §3.4.1 di 250 ms per pilot-in-the-loop. SATCOM non viene usato per manovre in tempo reale, ma esclusivamente per:
- Heartbeat monitoring (conferma UAV alive durante RF gap)
- RTL command invio (non time-critical una volta deciso)
- Telemetria di sicurezza a bassa frequenza (1 Hz)
- Ricezione acknowledgment comandi safety

### Protocol Stack OSI: Iridium Certus 100

```
┌─────────────────────────────────────────────────────────────────┐
│ L7 Application │ MAVLink v2.0 (subset ridotto, vedi sotto) │
│ L6 Presentation │ AES-256-GCM (stesso schema INT-03) │
│ L5 Session │ TCP keepalive (60 s interval) │
│ L4 Transport │ TCP/IP (affidabilità vs UDP per link lento) │
│ L3 Network │ IP (Iridium PPP address assignment) │
│ L2 Data Link │ PPP (RFC 1661) over Iridium IRDSS bearer │
│ L1 Physical │ L-band 1616-1626.5 MHz, TDMA/FDMA IRIDIUM │
└─────────────────────────────────────────────────────────────────┘
```

**Nota TCP vs UDP:** a differenza del link RF primario (UDP, latency-optimized), il link SATCOM adotta TCP per garantire delivery affidabile dei comandi safety-critical (RTL) in presenza di burst error L-band.

### [v2.0 NEW] MAVLink subset ridotto per SATCOM

Il bitrate Iridium 22 kbps uplink impone un subset di messaggi MAVLink.

**Downlink UAV→GCS via SATCOM (22 kbps uplink Iridium = circa 2750 B/s; NOTA: uplink Iridium = UAV trasmette a satellite):**

| MSG | Rate Hz | B/pkt | kbps | Priorità |
|---|---|---|---|---|
| HEARTBEAT | 0.2 (ogni 5 s) | 9+10 = 19 | 0.03 | CRITICA |
| GLOBAL_POSITION_INT | 0.5 | 28+10 = 38 | 0.15 | ALTA |
| SYS_STATUS | 0.2 | 31+10 = 41 | 0.07 | ALTA |
| BATTERY_STATUS | 0.1 | 41+10 = 51 | 0.04 | ALTA |
| STATUSTEXT (allarmi) | on-demand | 54+10 = 64 | variabile | CRITICA |
| **Totale downlink SATCOM** | | | **< 1 kbps** | n/a |

**Uplink GCS→UAV via SATCOM (352 kbps downlink Iridium):**

| MSG | Rate | B/pkt | Note |
|---|---|---|---|
| HEARTBEAT GCS | 0.2 Hz | 19 | Keepalive |
| COMMAND_LONG (RTL/LAND) | on-demand | 43 | Solo comandi safety |
| COMMAND_ACK response | on-demand | 20 | Conferma ricezione |

**Messaggi esclusi da SATCOM** (bandwidth insufficiente o latency non adatta): ATTITUDE (10 Hz, troppo frequente), HIGHRES_IMU (10 Hz), RC_CHANNELS, video preview di qualsiasi formato.

### [v2.0 NEW] Fallback Escalation Timer

```
┌─────────────────────────────────────────────────────────────────────────┐
│ LINK ESCALATION SEQUENCE: TEMPORIZZAZIONE │
│ │
│ t=0: Ultimo HEARTBEAT RF valido │
│ t=2s: RF DEGRADED, inizia switch SATCOM (modem power-on se dormante) │
│ AT+SBDIX tentativo connessione Iridium │
│ t=3s: SATCOM connessione stabilita (se disponibile) │
│ MAVLink rerouting: UDP socket → TCP socket SATCOM │
│ GCS alert: "C2 via SATCOM, latency elevated 1.5s" │
│ t=3s+: Operazioni con latency SATCOM; no pilot-in-loop manovre │
│ Missione autonoma waypoint prosegue; operator monitora solo │
│ │
│ IF SATCOM NOT available at t=3s: │
│ t=5s: LINK_LOST definitivo → RTL autonomo (FCS indipendente) │
│ t=5s: GCS alert CRITICAL + SMS Protezione Civile via gateway │
│ │
│ During RTL (RF still absent, SATCOM present): │
│ t=5s-RTL: SATCOM heartbeat monitoring; FCS stato via SATCOM │
│ IF RF restored: seamless switch back RF primary │
│ │
│ IF SATCOM lost DURING RTL: │
│ t+60s: Loiter 2 min @ RTL altitude (wait RF restoration) │
│ t+120s: Emergency land pre-computed safe zone (DTM Liguria) │
└─────────────────────────────────────────────────────────────────────────┘
```

### [v2.0 NEW] AT Command Set: Iridium 9770 Modem Switch

Il modem Iridium 9770 (o compatibile Iridium Certus 100) viene controllato via **UART 115200 baud 8N1** dal Mission Computer. La sequenza di attivazione link SATCOM è:

```
# 1. Verifica stato modem
AT → OK
AT+SBDMTA=1 → OK (abilita ricezione MT SBD, mobile-terminated)

# 2. Tentativo connessione e invio primo heartbeat
AT+SBDWB=19 → READY (write binary 19 byte, HEARTBEAT MAVLink)
[invia 19 byte MAVLink HEARTBEAT + 2 byte checksum]
 → 0 (OK)
AT+SBDIX → +SBDIX: <MO_status>,<MOMSN>,<MT_status>,<MTMSN>,<MT_len>,<MT_queued>
# MO_status=0 → successo invio; MO_status=1 → nessun response; >2 → errore

# 3. Lettura risposta MT (se MT_status=1 → dato in coda)
AT+SBDRB → [binary data MT, MAVLink da GCS]

# 4. Loop telemetria SATCOM (ogni 5 s)
AT+SBDWB=<len> → READY
[dati] → 0
AT+SBDIX → +SBDIX: 0,... (success)

# 5. Switch back a RF primario (se heartbeat RF restored)
# Nessun comando AT necessario, il routing layer software gestisce
# SATCOM rimane in standby (warm) per riattivazione rapida < 2 s
```

**Tempo di setup link da cold start modem:** circa 30 s (acquisizione satellite Iridium, registration network).
**Tempo di setup da warm standby (modem acceso, non in sessione):** circa 2-3 s.
**Raccomandazione operativa:** modem SATCOM sempre in warm standby durante volo BVLOS, switch in < 3 s garantito.

### Latency Budget SATCOM

| Segmento | Latenza one-way | Note |
|---|---|---|
| Mission Computer → modem UART | 5 ms | Serializzazione 115200 baud |
| SBD framing + burst transmission | 150 ms | Iridium TDMA burst 90 ms + processing |
| Propagazione LEO (780 km × 2 hop) | 5.2 ms | 780000/3×10^8 × 2 |
| ISU processing Iridium gateway | 200 ms | Iridium ground station processing |
| Internet routing gateway→GCS | 20 ms | TCP/IP Italia |
| GCS processing | 5 ms | n/a |
| **Totale one-way (UAV→GCS telemetry)** | **≈ 385 ms** | n/a |
| **RTT comandi (GCS→UAV→ACK)** | **≈ 1.5-2.0 s** | Iridium spec ±500 ms jitter |

### Failure Mode Behavior

| Failure Mode | Effetto | Mitigation |
|---|---|---|
| SATCOM non disponibile (no satellite in view) | Dipende da RF status | RTL se RF anche assente |
| Latency SATCOM > 3 s (congestione rete Iridium) | Comandi safety in ritardo | TCP retry 3× + RTL timeout FCS indipendente |
| Modem power failure in volo | Perdita backup | Watchdog MCU; modem su bus power separato da payload |
| L-band jamming (raro) | No SATCOM | RTL se RF assente; log evento per DO-326A security |

### Test Plan

| ID Test | Descrizione | Fase | Pass Criteria |
|---|---|---|---|
| T-INT04-01 | Switch RF→SATCOM timing | Integration test (M+13) | Switch completato in ≤ 3 s da LINK_DEGRADED |
| T-INT04-02 | MAVLink over Iridium integrità | Bench (M+12) | 0 message loss su 1000 cicli SBD |
| T-INT04-03 | RTL command via SATCOM | HIL (M+15) | RTL command ricevuto e eseguito in ≤ 5 s end-to-end |
| T-INT04-04 | Switch back SATCOM→RF | Field test (M+18) | Seamless switch; no command gap > 2 s |
| T-INT04-05 | Coverage test Pentema | Field test (M+19) | SATCOM disponibile ≥ 99% tempo in Val Trebbia (satellite elevation > 8°) |

---

<a name="int-05"></a>
## INT-05: Payload-to-Avionics Interface

### Scheda di identità

| Campo | Valore |
|---|---|
| **ID v2.0** | INT-6A-DATA-001/002/003 (unificati in INT-05 per v2.0) |
| **Nome** | Payload EO/IR ↔ Mission Computer. Interfaccia dati + controllo |
| **Tipo** | Funzionale data + control (Mission-Critical) |
| **DAL equivalente** | DAL-C (DO-178C); failure produce mission abort senza safety hazard diretto |
| **Endpoint A** | Payload Module: Sony Alpha 7R IV (RGB) + Workswell WIRIS Security (LWIR) + gimbal |
| **Endpoint B** | Mission Computer (MC) airborne (es. NVIDIA Jetson Orin NX 16 GB o equivalente) |
| **Direzione** | Bidirezionale: dati payload → MC; comandi gimbal/payload MC → payload |
| **Status** | **Detailed** |
| **Confidence** | **medium**; Sony GigE Vision consolidato, Workswell USB SDK well-documented. La bus architecture finale dipende dalla selezione hardware MC. |
| **Cross-ref RTM** | SyRq-PAY-001, SyRq-PAY-002, SyRq-PAY-003 |
| **Cross-ref Risk** | RSK-TEC-005 |

### Architettura bus: trade interno MIL-STD-1553 vs Ethernet AVB vs CAN

| Parametro | MIL-STD-1553B | Ethernet AVB (IEEE 802.1Qav) | CAN FD (ISO 11898-2) |
|---|---|---|---|
| Bitrate | 1 Mbps | 100 Mbps / 1 Gbps | 1-8 Mbps |
| Latenza deterministica | ≤ 1 ms | ≤ 2 ms (con credito) | ≤ 1 ms (CANopen) |
| Certificabilità | DAL-A consolidato (avionica militare) | DO-178C DAL-C possibile | DO-178C DAL-C possibile |
| Peso/ingombro | Bus coupler 50 g; cavo shielded | Cavo CAT6 lightweight | Cavo twisted pair 2 fili |
| Complessità | Alta (BC/RT/BM) | Media (switch AVB dedicato) | Bassa |
| Adeguatezza per dati RAW immagini | NO (1 Mbps insufficiente) | SI (Gbps Ethernet) | NO (8 Mbps insufficiente) |
| Adeguatezza per comandi gimbal | SI (1 Mbps più che sufficiente) | SI (overhead eccessivo) | SI (standard gimbal CAN) |
| **Verdetto** | **NO per dati** (banda) | **SI per dati RGB/IR** | **SI per comandi gimbal** |

**Architettura selezionata (ibrida):**

```
┌────────────────────────────────────────────────────────────────────┐
│ PAYLOAD-TO-AVIONICS BUS ARCHITECTURE │
│ │
│ Sony α7R IV ─── GigE Vision 1000BASE-T ──┐ │
│ (100 MP RAW 16-bit, trigger 1-5 fps) │ │
│ ├──► Mission Computer │
│ Workswell WIRIS ─ USB 3.1 Gen1 ──────────┤ (Jetson Orin NX) │
│ (LWIR 640×512, 60 fps, 16-bit thermal) │ │
│ │ │
│ Gimbal PWM/CAN ─ CAN FD (500 kbps) ─────┘ │
│ (pan/tilt/roll control; FOV commands) │
│ │
│ GNSS PPS ──────────────────────────────────► MC timestamp engine │
│ (1 PPS ±50 ns GPS disciplined, NMEA 0183) (geotagging sync) │
└────────────────────────────────────────────────────────────────────┘
```

### [v2.0 NEW] Payload Data Rates: calcolo dettagliato

**Sony Alpha 7R IV (RGB):**

```
Sensore: 61.0 MP (9504 × 6336 px)
RAW 14-bit: 9504 × 6336 × 14 bit = 843.5 Mbit = 105.4 MB/frame
RAW 16-bit (processato): 9504 × 6336 × 16 bit = 964.0 Mbit = 120.5 MB/frame
Compresso JPEG lossless (ratio 2:1): ~60 MB/frame
Compresso HEIF 10-bit (ratio 4:1): ~30 MB/frame

Rate operativo:
 - Fotogrammetria ispezione: 1 fps → 60-120 MB/s (bus GigE 125 MB/s → OK margine)
 - Ispezione continua HD: 3 fps → 180-360 MB/s (ECCEDE GigE 1G, richiede compressione in-camera o riduzione risoluzione)
 
Soluzione: Sony α7R IV in modalità APS-C crop (26 MP) a 3 fps = 26×10^6 × 16 bit / 8 = 52 MB/frame × 3 = 156 MB/s < 125 MB/s GigE
→ OPPURE: full frame 1 fps + burst 3 fps in memoria buffer camera (buffer interno 828 MB per circa 7 frame burst)

GigE Vision configurazione: binning 2×2 → 4752×3168 = 15 MP × 16 bit = 30 MB/frame × 5 fps = 150 MB/s
→ Effettivo con GigE overhead: throughput utile ~950 Mbps → 118 MB/s → OK a 3 fps 15 MP
```

**Workswell WIRIS Security (LWIR):**

```
Sensore: FLIR Lepton 3.5 o Lynred Pico640, 640×512 px, 16-bit thermal
Frame rate: 25 fps (EXPORT CONTROLLED) o 9 fps (non-export-restricted)
Bitrate RAW: 640 × 512 × 16 bit × 25 fps = 131.1 Mbps
 640 × 512 × 16 bit × 9 fps = 47.2 Mbps

USB 3.1 Gen1 bandwidth: 5 Gbps → ampiamente sufficiente
Formato output: TIFF 16-bit radiometrico o JPG 8-bit display
SDK: Workswell CorePlayer SDK + FLIR Atlas SDK

NOTE EXPORT CONTROL: LWIR 640×512 > 9 Hz → dual-use (EAR/ITAR/Reg. UE 2021/821)
→ Workswell WIRIS Security è prodotto EU (Czech Republic) con compliance CE + export license EU
→ Verificare EAR license se UAV opera in zone non-EU
```

**Gimbal (CAN FD):**

```
Gimbal: DJI Zenmuse X7-equivalent o gimbal custom 3-axis
Bus: CAN FD (ISO 11898-2) @ 500 kbps nominal, 2 Mbps data phase
Protocollo: MAVLink GIMBAL_DEVICE_SET_ATTITUDE (MSG ID 284) over CAN-MAVLink bridge
 o DroneCAN (ex UAVCAN v1.0) per gimbal di nuova generazione

Messaggi gimbal (frequenza 10 Hz per controllo smooth):
 - GIMBAL_DEVICE_SET_ATTITUDE: q[4] float, angular_velocity[3] float, flags
 - GIMBAL_DEVICE_ATTITUDE_STATUS: attitude corrente, failure flags
 Bitrate: 10 Hz × (50 byte CAN frame × 8) = 4 kbps → < 500 kbps OK ampiamente

FOV control protocol:
 MAV_CMD_SET_CAMERA_ZOOM (MSG ID 531): zoom_type, zoom_value
 MAV_CMD_DO_MOUNT_CONTROL (MSG ID 205): pitch/roll/yaw target
 MAV_CMD_IMAGE_START_CAPTURE (MSG ID 2000): interval, total_images, sequence
```

### [v2.0 NEW] GNSS PPS Timing Sync: sub-microsecond Geotagging

La sincronizzazione temporale per geotagging sub-microsecondo è critica per fotogrammetria e correlazione dati EO/IR.

```
┌──────────────────────────────────────────────────────────────────────┐
│ GNSS PPS TIMING ARCHITECTURE │
│ │
│ GNSS Receiver (u-blox F9P o equivalente) ──PPS signal──► MC GPIO │
│ (1 PPS rising edge, accuracy ±50 ns RMS, NMEA $GPRMC time ref) │
│ │
│ MC Timestamp Engine: │
│ - PPS interrupt handler latency < 10 µs (kernel PREEMPT_RT) │
│ - Hardware timer latch at PPS rising edge: absolute time = TAI │
│ - Software interpolation between PPS pulses: 100 kHz counter │
│ - Timestamp resolution: 10 µs (counter period) │
│ - Timestamp accuracy: ±50 ns PPS + ±10 µs interpolation ≈ ±10 µs│
│ │
│ Geotagging injection: │
│ - Camera trigger signal: MC GPIO → camera external trigger │
│ - Trigger latency measured: camera shutter lag (α7R IV ≈ 30 ms) │
│ - Correction applied: timestamp = T_PPS_latch + shutter_lag_cal │
│ - Shutter lag calibration: factory test M+10 (measured per unit) │
│ │
│ EXIF/XMP embedding: │
│ - Lat/Lon/Alt: GLOBAL_POSITION_INT MAVLink interpolated @ T_shutter│
│ - Timestamp: UTC ISO 8601 µs precision │
│ - IMU attitude: ATTITUDE MAVLink @ T_shutter (roll/pitch/yaw) │
└──────────────────────────────────────────────────────────────────────┘
```

### Data Rate Summary

| Flusso | Interfaccia | Rate min | Rate tipico | Rate max | Bus |
|---|---|---|---|---|---|
| RGB RAW 15 MP | GigE Vision 1000BASE-T | 0 (idle) | 30 MB/s (1 fps) | 90 MB/s (3 fps) | Ethernet |
| LWIR 640×512 | USB 3.1 Gen1 | 0 | 6 MB/s (9 fps) | 16 MB/s (25 fps) | USB |
| Gimbal control | CAN FD | 0 | 4 kbps | 20 kbps | CAN |
| PPS timing | GPIO | n/a | 1 pulse/s | 1 pulse/s | GPIO |
| MC → Storage NVMe | PCIe Gen3 x4 | 0 | 200 MB/s | 2 GB/s | PCIe |

### Failure Mode Behavior

| Failure Mode | Effetto | Categoria | Mitigation |
|---|---|---|---|
| GigE link drop | Nessun dato RGB | Major (Mission abort) | USB 3.0 fallback stream JPEG; log event |
| USB 3.1 drop LWIR | Nessun dato IR | Major (Mission abort) | Reconnect automatico SDK; log event |
| PPS signal loss | Geotagging inaccurato | Minor (data quality) | NTP fallback ±1 ms; flag in EXIF |
| Gimbal CAN failure | Camera puntata fissa | Minor (operational) | Manual pointing workaround; log |
| MC overtemperature | Throttling CPU | Major (processing gap) | Thermal design 45°C operativo; OTA cooling NACA vent |
| Storage full | Nessuna registrazione | Major (mission abort) | Pre-flight check storage ≥ 80 GB free |

### Test Plan

| ID Test | Descrizione | Fase | Pass Criteria |
|---|---|---|---|
| T-INT05-01 | GigE Vision throughput bench | DDT (M+10) | ≥ 90 MB/s sustained; 0 frame drop a 3 fps 15 MP |
| T-INT05-02 | LWIR USB latency | DDT (M+10) | Frame latency < 50 ms @ 25 fps |
| T-INT05-03 | PPS geotagging accuracy | DDT (M+11) | ΔXY geotag vs ground truth ≤ 5 cm @ 100 m AGL |
| T-INT05-04 | Gimbal CAN control | DDT (M+10) | Pointing error ≤ 0.1° steady-state; response < 200 ms |
| T-INT05-05 | Full pipeline integration | Integration test (M+14) | RGB+IR+gimbal simultanei; no buffer overflow |
| T-INT05-06 | Thermal stress MC | HIL (M+13) | MC operativo a 55°C ambiente (simula copertura estate) |

---

<a name="int-13"></a>
## INT-13: DAA Detect-And-Avoid

### Scheda di identità

| Campo | Valore |
|---|---|
| **ID v2.0** | INT-6A-C2-006/007 (unificati in INT-13 per v2.0) |
| **Nome** | DAA: Detect-And-Avoid cooperativo + non-cooperativo |
| **Tipo** | Safety (Flight-Critical + Compliance-Critical) |
| **DAL equivalente** | DAL-B (cooperativo ADS-B); DAL-C (non-cooperativo EO/acoustic per SAIL III) |
| **Endpoint A** | Sensori DAA a bordo (ADS-B IN receiver + eventuale radar/EO) |
| **Endpoint B** | FCS DAA logic + GCS alerting |
| **Status** | **Detailed** (cooperativo); **Preliminary** (non-cooperativo) |
| **Confidence** | **high** (ADS-B cooperativo DO-260B consolidato); **low** (non-cooperativo, TRL 5-6 per SAIL III Pentema) |
| **Cross-ref RTM** | SyRq-DAA-001, SyRq-DAA-002, SyRq-DAA-003 |
| **Cross-ref Risk** | RSK-INT-003, RSK-TEC-004, RSK-REG-001 |

### Architettura DAA: livelli

```
┌──────────────────────────────────────────────────────────────────────┐
│ DAA ARCHITECTURE: PERCORSO 6A │
│ │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ SENSORI │ │
│ │ ADS-B IN Receiver (uAvionix ping2020i o equiv) │ │
│ │ - 1090ES (DF17/18/19): traffico GA cooperativo │ │
│ │ - ADS-L (868 MHz): UAV cooperativi registrati U-Space │ │
│ │ - FLARM (868 MHz OGN): alianti, ULM, parapendio │ │
│ │ │ │
│ │ [SAIL III OPZIONALE] Radar non-cooperativo │ │
│ │ o EO visual detection (se ENAC richiede) │ │
│ └─────────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ DAA PROCESSING (Mission Computer / FCS) │ │
│ │ - Track fusion: ADS-B + ADS-L + FLARM │ │
│ │ - Threat assessment: CPA (Closest Point of Approach) │ │
│ │ - DMOD/ZTHR thresholds (DO-365B §2.2.3) │ │
│ │ - Alert levels: TA (Traffic Advisory) + RA (Resolution)│ │
│ └─────────────────────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ RESPONSE │ │
│ │ - TA: GCS alert + pilot decision (pilot-in-loop) │ │
│ │ - RA: Auto maneuver suggerita (SAIL III: auto-execute │ │
│ │ se pilot no-response in 5 s) │ │
│ └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

### [v2.0 NEW] ADS-B 1090ES: formato messaggi (DO-260B / MOPS)

**ADS-B 1090ES message types per ricezione (DAA):**

| Downlink Format | Nome | Dati chiave | Rilevanza DAA |
|---|---|---|---|
| DF17 | ADS-B Squitter (ICAO 24-bit address) | Posizione, velocità, identificativo | PRIMARIA |
| DF18 | TIS-B / ADS-R (non-ICAO) | Posizione, velocità | ALTA (traffico GA senza transponder ICAO) |
| DF19 | Military ADS-B Extended Squitter | n/a | Trascurabile (escluso zona) |
| DF20/21 | Mode S ATCRBS reply | Altitude, identity (squawk) | SUPPLEMENTARE |

**DF17 payload structure (56-bit data block = 7 byte, ME field):**

```
ME Type Code (5 bit) → determina tipo messaggio:
 TC 1-4: Aircraft Identification (callsign 8 char)
 TC 5-8: Surface Position (lat/lon, ground speed)
 TC 9-18: Airborne Position (lat/lon, altitude, CPR)
 TC 19: Airborne Velocity (speed, heading, vertical rate)
 TC 20-22: Airborne Position (Gillham altitude)
 TC 28: Aircraft Status (emergency/priority)
 TC 29: Target State and Status (FMS targets)
 TC 31: Aircraft Operational Status (ADS-B version, capability)

Per DAA, messaggi prioritari:
 TC 9-18: Posizione (lat/lon CPR encoded, altitude Gillham/Gray)
 - CPR (Compact Position Reporting): 17 bit lat + 17 bit lon
 - Risoluzione dopo decode: ~5.1 m @ equatore
 - Update rate: 0.5-2 Hz (regime crociera) o fino a 5 Hz (superficie)
 TC 19: Velocità
 - Subsonic: East-West velocity (11 bit) + North-South velocity (11 bit)
 - Vertical rate (9 bit, 64 fpm resolution)
```

**MOPS DO-260B §2.2.1: Range di ricezione DAA:**

| Parametro | Valore MOPS | Note per Percorso 6A |
|---|---|---|
| Minimum range reception | 80 NM (148 km) @ FL180 | In area Pentema (bassa quota), gli ostacoli orografici riducono il range effettivo |
| Altitude accuracy | ±25 ft (7.6 m) | Sufficiente per separazione verticale |
| Position accuracy NACp ≥ 9 | < 30 m (95%) | Richiesto per DAA credibile |
| Update rate | ≥ 0.5 Hz | Per tracciamento CPA |
| Latency position → alert | ≤ 1 s | MOPS requirement |

**Receiver selezionato:** uAvionix ping2020i (RTCA DO-260B + DO-282B compliant, SWaP: 28 g, 25×25×5 mm, 5 VDC). Dual-frequency 1090 MHz (DF17/18) + 978 MHz UAT (per traffico USA, opzionale in Italia). Interfaccia: UART/USB JSON output oppure GDL 90 protocol.

### [v2.0 NEW] ADS-L 868 MHz: UAV cooperativi U-Space

**ADS-L (Automatic Dependent Surveillance-Light):** standard EUROCAE ED-270 [^ED270] per UAV in U-Space. Frequenza 868 MHz (LoRa o FSK), portata tipica 5-10 km in LOS.

```
ADS-L message format (EUROCAE ED-270 Annex A):
 Header: 3 byte (version, message type, source ID)
 Position: lat/lon 4 byte each (WGS-84, 10e-7 deg resolution)
 Altitude: 3 byte (cm above WGS-84, range 0-16777 m)
 Velocity: 2 byte N/S + 2 byte E/W (cm/s, range ±327 m/s)
 Heading: 2 byte (0.01 deg resolution)
 Timestamp: 4 byte (Unix epoch seconds)
 CRC: 2 byte CRC-16/CCITT
 Total: ≈ 26 byte per frame
 Rate: 1 Hz obbligatorio (ogni 1 s ±200 ms jitter)
```

**Integrazione con U-Space via D-Flight:** il FCS del CW-30E trasmette ADS-L (o FLARM + traduzione ADS-L via bridge) verso D-Flight USSP (U-Space Service Provider) per tracciamento cooperativo. Il receiver ADS-L a bordo riceve gli altri UAV registrati nel volume operativo.

### [v2.0 NEW] Threat Assessment: algoritmo CPA

**Closest Point of Approach (CPA):** calcolo del punto di minima separazione tra UAV ownship e intruder.

```
Input per ogni intruder tracciato:
 p_own = [lat, lon, alt, Vn, Ve, Vd] (ownship da GNSS + IMU)
 p_int = [lat, lon, alt, Vn, Ve, Vd] (intruder da ADS-B/ADS-L)

Calcolo:
 Δp = p_int - p_own (relativa posizione, frame NED)
 Δv = v_int - v_own (relativa velocità)
 
 t_CPA = -dot(Δp, Δv) / dot(Δv, Δv) (tempo a CPA)
 CPA_range = |Δp + Δv × t_CPA| (distanza al CPA)
 CPA_alt = Δalt + ΔVd × t_CPA (separazione verticale)

Alert thresholds (derivati DO-365B §2.2.3 [^DO365B]):
 DMOD (Distance Modification Threshold): 0.66 NM (1.22 km) per Specific Category
 ZTHR (Z Threshold vertical): 450 ft (137 m) per Specific Category
 TMOD (Time to CPA): ≤ 35 s → Traffic Advisory (TA)
 ≤ 20 s → Resolution Advisory (RA)

Alert latency from track update to alert: ≤ 5 s (target < 2 s per TA)
Safe separation maneuver: climb/descend 500 fpm + turn ≤ 25° bank
```

### [v2.0 NEW] Non-Cooperative DAA (SAIL III, condizionale)

**Contesto:** ENAC SORA 2.5 per SAIL III Pentema potrebbe richiedere DAA non-cooperativo per protezione da alianti, ULM, parapendio senza transponder (comuni in Val Trebbia), e da elicotteri di soccorso in emergenza (Soccorso Alpino, 118).

**Tecnologie disponibili (TRL 5-6, 2026):**

| Tecnologia | Vendor / Prodotto | Detection Range | False Alarm Rate | SWaP | TRL | Note |
|---|---|---|---|---|---|---|
| Radar FMCW millimetrico | Echodyne EchoDrive Sense | 1 km × piccolo UAS; 5 km × aereo | < 0.01/h (spec) | 450 g, 20 W | 6 | Non ancora DO-365B certificato |
| EO Visual Detection | Iris Automation Casia G | 0.5-1 NM vs GA | < 0.1/h (spec) | 350 g, 5 W | 6 | Certificazione in corso FAA |
| EO + Acustico fusion | Daedalean ADL-1 | 1 NM vs GA | < 0.05/h (spec) | 600 g, 8 W | 5-6 | Integration effort alto |
| **Verdetto per Fase 1** | **Non selezionato** | n/a | n/a | n/a | n/a | **Confidence low; defer a ENAC feedback** |

**Strategia per Percorso 6A Fase 1:**
1. Avviare operazioni con solo DAA cooperativo (ADS-B IN + ADS-L + FLARM)
2. In SORA application, dichiarare mitigazione OSO #3 tramite (a) coordination con autorità locali (FIVL alianti, ANA parapendio) per awareness mutua, (b) NOTAM volume operativo Pentema, (c) orari operativi selettivi (evitare peak traffic GA)
3. Se ENAC richiede DAA non-cooperativo per SAIL III: engagement vendor Echodyne/Iris Automation per integration study (M+6/M+9)

**Falsifying observation:** se ENAC valuta che SAIL III Pentema richiede DAA non-cooperativo certificato DO-365B Annex C prima del first flight, allora le operazioni BVLOS vanno in hold; costo addizionale €150-300k + 6-12 mesi lead time. Cross-ref: RSK-INT-003 (P=3, I=5, P×I=15 RED).

### [v2.0 NEW] Latency Response DAA

```
┌─────────────────────────────────────────────────────────────────────────┐
│ DAA LATENCY CHAIN: END-TO-END │
│ │
│ ADS-B message received (1090 MHz) → ADS-B receiver decode │
│ Latency: 50 ms (receiver processing + UART output) │
│ │ │
│ ▼ │
│ GDL90 / JSON → Mission Computer track fusion │
│ Latency: 100 ms (track association, CPA calculation) │
│ │ │
│ ▼ │
│ Alert generated → MAVLink STATUSTEXT + TRAFFIC_REPORT (MSG 246) │
│ Latency: 10 ms (MAVLink encoding + transmission RF/SATCOM) │
│ │ │
│ ▼ │
│ GCS alert display + audio │
│ Latency: 50 ms (network + display rendering) │
│ │ │
│ ▼ │
│ Pilot assessment + decision │
│ Latency: 2-5 s (human factor, DO-365B §3.2 pilot reaction time) │
│ │ │
│ TOTAL TA latency (ADS-B rx → pilot aware): ≈ 2.5-5.5 s │
│ TOTAL RA latency (to auto-maneuver initiation): ≤ 5 s (threshold) │
│ │
│ DO-365B §2.2.3 requirement: alert ≤ 35 s before CPA per TA │
│ → Budget residuo: 35 s - 5.5 s = 29.5 s sufficiente ✓ │
└─────────────────────────────────────────────────────────────────────────┘
```

**MAVLink TRAFFIC_REPORT (MSG ID 246):**
```
icao_address: uint32 (24-bit ICAO + parity bits)
lat: int32 (1e7 deg)
lon: int32 (1e7 deg)
altitude_type: uint8 (0=ADSB_ALTITUDE_TYPE_PRESSURE, 1=GNSS)
altitude: float (m, MSL o GNSS)
heading: uint16 (cdeg, 0-35999)
hor_velocity: uint16 (cm/s)
ver_velocity: int16 (cm/s, + up)
callsign: char[9] (ICAO callsign)
emitter_type: uint8 (ADSB_EMITTER_TYPE enum)
tslc: uint8 (Time Since Last Communication, s)
flags: uint16 (ADSB_FLAGS bitmap: VALID_COORDS, VALID_ALTITUDE, etc.)
squawk: uint16 (Mode C squawk)
```

### Failure Mode Behavior

| Failure Mode | Effetto | Categoria | Mitigation |
|---|---|---|---|
| ADS-B receiver power failure | Nessun track cooperativo | Hazardous (DAL-B) | Dual ADS-B receiver (primary + hot spare); watchdog |
| ADS-B antenna failure | Range ridotto; no track lontani | Major (DAL-C) | Ridondanza antenna (2 antenne diversified) |
| CPA algorithm software crash | Nessun alert | Hazardous (DAL-B) | Watchdog MCU + fallback "loiter + alert pilot" |
| False RA (intruder fantasma) | Manovra non necessaria | Minor | False alarm filter (track persistence ≥ 3 frame) |
| Intruder no ADS-B (non-cooperativo) | Blind spot | Hazardous (condizionale) | NOTAM + orari + (Fase 2) radar EO |

### Test Plan

| ID Test | Descrizione | Fase | Pass Criteria |
|---|---|---|---|
| T-INT13-01 | ADS-B DF17 decode accuracy | DDT (M+10) | 100% decode su 10.000 frame test ADSB-Exchange replay |
| T-INT13-02 | CPA algorithm validation | DDT (M+11) | CPA error < 10 m vs reference; TA alert in ≤ 2 s |
| T-INT13-03 | Range test ADS-B IN | Field test (M+18) | Track acquisition ≥ 50 NM in LOS (aeroporto vicino) |
| T-INT13-04 | Alert latency end-to-end | HIL (M+14) | Alert GCS in ≤ 5 s da ADS-B rx |
| T-INT13-05 | False alarm rate | DDT (M+12) | FAR ≤ 0.01/h su 100 h replay scenario Pentema |
| T-INT13-06 | Auto-maneuver RA (se SAIL III) | HIL (M+15) | Avoidance maneuver inizia ≤ 5 s da RA trigger |

---

<a name="int-15"></a>
## INT-15: Privacy by Design (Blur On-Board)

### Scheda di identità

| Campo | Valore |
|---|---|
| **ID v2.0** | INT-6A-GS-007 / INT-X-PRIVACY-001 (unificati in INT-15 per v2.0) |
| **Nome** | Pipeline Privacy by Design: anonymization EO on-board |
| **Tipo** | Funzionale data + compliance (GDPR-Critical + DAL-D per software non-safety) |
| **DAL equivalente** | DAL-D (DO-178C); failure produce compliance violation senza safety hazard diretto |
| **Endpoint A** | Mission Computer (MC), pipeline di elaborazione immagini |
| **Endpoint B** | Cloud storage + DPO audit trail |
| **Direzione** | Unidirezionale (RAW → processed → cloud) |
| **Status** | **Detailed** |
| **Confidence** | **medium**; algoritmi YOLOv8n/OpenCV consolidati, pipeline completa non ancora integrata e testata su MC Jetson |
| **Cross-ref RTM** | SyRq-PRIV-001, SyRq-PRIV-002, SyRq-PRIV-003 |
| **Cross-ref Risk** | RSK-REG-003, RSK-REG-004 |

### [v2.0 NEW] Pipeline completa: schema OSI equivalente

```
┌──────────────────────────────────────────────────────────────────────┐
│ PRIVACY PIPELINE: FLOW DETTAGLIATO │
│ │
│ INPUT: EO RAW frame (15 MP GigE Vision, 1-3 fps) │
│ │
│ STEP 1: Resize per inference │
│ RAW 15 MP → resize bicubic → 640×640 px (YOLO input size) │
│ Latency: 5 ms (GPU CUDA resize, Jetson Orin) │
│ │
│ STEP 2: Face detection (YOLOv8n) │
│ Model: YOLOv8n (nano) quantized INT8 (TensorRT engine) │
│ Input: 640×640×3 uint8 │
│ Output: bounding boxes [x,y,w,h,confidence,class] │
│ Threshold: confidence ≥ 0.5, NMS IoU 0.45 │
│ Latency: 8-12 ms (Jetson Orin GPU, batch=1) │
│ Classes: face (class 0), person (class 1) │
│ │
│ STEP 3: Plate detection (ANPR, Automatic Number Plate Rec.) │
│ Model: custom YOLO fine-tuned su targhe EU (IT, FR, DE, EU std) │
│ Input: 640×640×3 uint8 (stessa inference pass di Step 2) │
│ Output: bounding boxes targa │
│ Latency: incluso in Step 2 (multi-class detection) │
│ │
│ STEP 4: Backproject ROI → coordinate originale 15 MP │
│ Scale factor: 15 MP / 640px → scale_x = 9504/640 = 14.85 │
│ scale_y = 6336/640 = 9.9 │
│ Expand ROI: +10% padding per coprire occhiali/capello │
│ Min size check: ROI < 5×5 px @ scala originale → skip (già blur) │
│ │
│ STEP 5: Blur applicazione │
│ Algoritmo: Gaussian blur kernel 51×51 σ=15 (face) │
│ Pixelation 8×8 block average (plate, più leggibile) │
│ OpenCV: cv2.GaussianBlur(roi, (51,51), 15) su ROI estratto │
│ Iniettato back nel frame originale a coordinata backprojected │
│ Latency: 2-5 ms (CPU, per ROI; GPU possibile se > 10 ROI/frame) │
│ │
│ STEP 6: Encoding H.265 │
│ Standard: HEVC (ITU-T H.265 / ISO/IEC 23008-2) │
│ Profile: Main 10 (10-bit per qualità fotogrammetrica) │
│ Encoder: hardware NVENC Jetson Orin (non degradare processing GPU)│
│ CRF equivalent: 23 (visually lossless per fotogrammetria) │
│ Container: MP4 (ISO Base Media File Format) │
│ Latency: 10-20 ms (hardware encoder, latency mode = low) │
│ │
│ STEP 7: DPIA Evidence Chain │
│ Hash frame processed: SHA-256(frame_H265_encoded) → 32 byte │
│ Hash frame RAW: SHA-256(frame_RAW_original) → 32 byte │
│ Timestamp: TAI µs precision (PPS-disciplined, vedi INT-05) │
│ Log entry: JSON record → append-only log (immutable) │
│ Latency: 1 ms (SHA-256 hardware accelerator Jetson) │
│ │
│ STEP 8: Cloud Upload │
│ API: AWS S3 compatible (Aruba Object Storage GAIA-X) │
│ Protocol: HTTPS (TLS 1.3) + pre-signed URL │
│ Chunk: multipart upload 10 MB per chunk │
│ Latency upload: dipende da backhaul (INT-6A-PHY-010) │
│ │
│ TOTAL PIPELINE LATENCY: 5+12+5+20+1 = 43 ms (nominal 1 fps) │
│ TARGET: < 500 ms ✓ (ampio margine) │
└──────────────────────────────────────────────────────────────────────┘
```

### [v2.0 NEW] Specifica algoritmi di rilevamento

**YOLOv8n (Face detection):**

```
Framework: Ultralytics YOLOv8n (open-source, AGPL-3.0 o commercial)
Versione: YOLOv8n v8.x (weights pubblici pre-trained COCO + fine-tuning WiderFace)
Model size: 6.3 MB (FP32) → 1.6 MB (INT8 quantized TensorRT)
Input: 640×640×3 RGB
Output: [N_detections × 6] → [x_center, y_center, width, height, confidence, class_id]
Performance (Jetson Orin NX 16 GB):
 - FP32: ~50 fps
 - INT8 TensorRT: ~120 fps
 - Batch=1 latency: ≈ 8 ms (INT8)
Accuracy (WiderFace val hard): mAP ≈ 0.72 (distanza > 5 m, face > 5×5 px @ 640px)
 NOTA: a bassa quota UAV (≤ 100 m AGL) i volti sono tipicamente > 20×20 px → detection rate > 95%
 A quota ≥ 150 m AGL: volti < 5 px → detection impossibile → non è tecnicamente necessario blur
 Soglia operativa raccomandata: altitudine ≤ 120 m AGL per privacy-sensitive operations
False positive rate: ≈ 2-5% (pose non-frontale, oggetti simili a volti) → blurring conservativo OK per GDPR

Requirement GDPR Art. 25 (privacy by design):
 Qualsiasi bounding box con confidence ≥ 0.5 → BLURRED (approccio conservative)
 Non si richiede certezza di identificazione; sufficiente probabilità di essere un volto
```

**ANPR (Plate detection):**

```
Approccio: fine-tuning YOLOv8n su dataset targhe EU
Training data: OpenALPR + EU plates dataset (pubblico) + augmentation
Classi: [plate_IT, plate_EU, plate_motorcycle]
Accuracy: mAP ≈ 0.80 per targe EU leggibili (angolo ≤ 30°, distanza ≤ 30 m)
Nota operativa: a quota ≥ 60 m AGL, targhe auto generalmente illeggibili (< 10 px)
 → ANPR detection significativa solo a quota < 60 m (poco frequente in missioni BVLOS standard)
 → Inserire comunque nel pipeline per coprire fasi take-off/landing

Alternativa COTS: OpenALPR (Apache License 2.0), già addestrato su targhe EU
 Performance: ≈ 95% detection rate su immagini ad alta risoluzione
 Integrazione: Python API o C++ library su Jetson
```

### [v2.0 NEW] DPIA Evidence Chain: specifiche immutabilità

**Requisito GDPR:** il trattamento dati con riprese aeree costituisce trattamento a rischio elevato (EDPB Guidelines 01/2022 §3.2 [^EDPB]) e richiede DPIA obbligatoria + audit trail verificabile.

**Log record JSON (per ogni frame processato):**

```json
{
 "frame_id": "6A-20260901-143022-000142",
 "timestamp_tai_us": 1756741822123456,
 "timestamp_utc_iso": "2026-09-01T12:30:22.123456Z",
 "gnss_lat_1e7": 446123456,
 "gnss_lon_1e7": 91234567,
 "gnss_alt_mm": 850000,
 "platform_id": "VTOL-6A-001",
 "operator_id": "FIRMAMENTO-IT-001",
 "mission_id": "PENTEMA-MISSION-042",
 "privacy_processing": {
 "faces_detected": 2,
 "faces_blurred": 2,
 "plates_detected": 0,
 "plates_blurred": 0,
 "model_version": "yolov8n-face-v1.3",
 "confidence_threshold": 0.5,
 "processing_latency_ms": 43
 },
 "hashes": {
 "frame_raw_sha256": "a3f2b1c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2",
 "frame_processed_sha256": "b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3"
 },
 "raw_retained": false,
 "raw_retention_reason": null,
 "log_version": "1.0"
}
```

**Catena di custodia dell'evidenza (DO-326A §5.3 + GDPR Art. 32):**

```
1. Frame RAW non salvato su storage persistente (memoria volatile MC solo)
 ECCEZIONE: se operatore dichiara legittimo interesse + consenso esplicito
 (es. incidente aereo in corso → evidence preservation)
 → log entry: raw_retained=true, raw_retention_reason="INCIDENTE-202609-001"

2. Log record → append-only file (ext4 append-only flag: chattr +a log.jsonl)
 → Integrazione SIEM via RFC 5425 TLS Syslog (vedi INT-X-LOGGING-001)

3. Hash chain: H(frame_n) incluso in log_entry(frame_n+1)
 → Blockchain-light: ogni record firma il precedente (Merkle-like senza distributed ledger)

4. Firma digitale log batch (ogni 100 frame o 60 s):
 → Batch hash = SHA-256(concatenazione di tutti H(frame_i) nel batch)
 → Firma: ECDSA P-256 con chiave privata HSM airborne (Hardware Security Module)
 → Firma inviata a cloud ogni ciclo → immutabilità garantita post-landing

5. DPO access: dashboard cloud con ricerca per mission_id, data, area geografica
 → DSAR response entro 30 giorni (GDPR Art. 12)
 → Evidenza: esporta log JSON per periodo richiesto + hash verification
```

### Processing Latency: analisi

| Step | Latency nominale | Latency worst-case | HW |
|---|---|---|---|
| Resize 15 MP → 640px | 5 ms | 10 ms | GPU CUDA |
| YOLOv8n inference (INT8) | 8 ms | 15 ms | GPU TensorRT |
| Backproject + blur (5 ROI) | 5 ms | 15 ms (20 ROI) | CPU OpenCV |
| H.265 encode (1 frame) | 15 ms | 25 ms | NVENC HW |
| SHA-256 hash (2 frame) | 1 ms | 2 ms | HW accelerator |
| Log write + SIEM | 2 ms | 5 ms | NVMe SSD |
| **Totale pipeline** | **36 ms** | **72 ms** | n/a |
| **Target < 500 ms** | ✓ | ✓ | Margine 6-14× |

### Failure Mode Behavior

| Failure Mode | Effetto | Categoria | Mitigation |
|---|---|---|---|
| YOLOv8n crash | Frame non blurred → GDPR violation | Compliance-Critical | Watchdog: se model fail, applica FULL FRAME BLUR (tutta immagine oscurata) + alert + abort mission |
| GPU overtemperature | Inference throttle → latency > 500 ms | Major (data quality) | Thermal design Jetson; watchdog temperatura; full-blur fallback |
| Log storage full | Nessun audit trail | Compliance-Critical | Pre-flight check; alert ≥ 20% free; ring buffer con alert |
| Hash mismatch | Integrità catena compromessa | Major (audit) | Alert DPO; segmento log invalidato + annotazione |
| Cloud upload failure | Dati solo on-board | Minor (backup) | On-board retention 7 gg; retry automatico; no GDPR violation immediata |
| False negative detection (volto non rilevato) | Dato personale non anonimizzato | Compliance-Critical | (1) Altitude constraint ≤ 120 m AGL per operazioni privacy-sensitive; (2) missioni residenziali: revisione DPO campione 5% frame post-missione; (3) DPIA dichiara residual risk accettabile + misure compensative |

### Standard di riferimento

La pipeline si conforma a: GDPR Reg. UE 2016/679 Art. 25 (Privacy by Design), Art. 32 (sicurezza), Art. 35 (DPIA); EDPB Guidelines 01/2022 on data subject rights (update 2023) [^EDPB]; EDPB Guidelines 10/2020 on restrictions under Art. 23 GDPR; D.Lgs. 196/2003 (Codice Privacy IT) come modificato da D.Lgs. 101/2018; OpenCV 4.x (Apache License 2.0) per cv2.GaussianBlur e cv2.rectangle; Ultralytics YOLOv8 (AGPL-3.0 / commercial license) come detection framework; NIST SP 800-57 Part 1 Rev. 5 per Key Management (ECDSA P-256 signing); RFC 5425 "Transport Layer Security (TLS) Transport Mapping for Syslog".

### Test Plan

| ID Test | Descrizione | Fase | Pass Criteria |
|---|---|---|---|
| T-INT15-01 | Face detection accuracy | DDT (M+11) | Detection rate ≥ 95% su dataset test 1000 immagini UAV (h ≤ 100 m AGL) |
| T-INT15-02 | ANPR detection accuracy | DDT (M+11) | Detection ≥ 80% targhe EU leggibili (h ≤ 60 m AGL) |
| T-INT15-03 | Pipeline latency end-to-end | DDT (M+10) | P99 latency ≤ 200 ms (Jetson Orin NX, 3 fps) |
| T-INT15-04 | Full-blur fallback | DDT (M+12) | Se YOLOv8n crash, 100% frame oscurati; alert entro 1 s |
| T-INT15-05 | Hash chain integrity | DDT (M+11) | Nessuna collision; hash chain verificabile end-to-end |
| T-INT15-06 | DSAR drill (simulato) | Validation (M+16) | DPO recupera tutti frame per missione in ≤ 10 min; hash verificato |
| T-INT15-07 | DPIA review DPO | Regulatory (M+7/M+9) | DPIA approvata da Garante (o no-reaction entro 8 settimane) |
| T-INT15-08 | Pentest pipeline | Verification (M+17) | Nessuna injection SQL/RCE sul log API; TLS 1.3 verified |

---

<a name="confronto"></a>
## Matrice di confronto v1.0 → v2.0

| Interfaccia | v1.0 Preliminary | v2.0 Detailed: cosa è stato aggiunto |
|---|---|---|
| **INT-03 C2 RF** | MAVLink v2.0 + AES-256-GCM dichiarati; no byte-level spec | Byte-level MAVLink v2.0 header + payload per 14 messaggi; AES-256-GCM nonce construction 96-bit; CRC-X25 polinomio + CRC_EXTRA; state machine 5 stati lost-link; retry logic 3× 500 ms; timing diagram ASCII completo |
| **INT-04 SATCOM** | Iridium Certus menzionato; no trade, no AT commands, no latency budget | Trade table 3 tecnologie (Iridium/Inmarsat/Starlink) + giustificazione selezione; escalation timer diagram ASCII; AT command set Iridium 9770 completo; MAVLink subset SATCOM; latency budget segmentato |
| **INT-05 Payload** | GigE Vision + USB 3.0 + rate dichiarati; no trade bus, no timing sync | Trade MIL-1553/Ethernet AVB/CAN FD; data rate calcolo dettagliato Sony 15 MP + LWIR; CAN FD gimbal protocol (MAVLink 284); GNSS PPS timing architecture ±10 µs geotagging; bus architecture diagram ASCII |
| **INT-13 DAA** | ADS-B IN dichiarato; no message format, no algoritmo, no threshold | DF17/18/19 payload structure; CPR decode; MOPS DO-260B table; CPA algorithm pseudocode; DO-365B DMOD/ZTHR thresholds; ADS-L ED-270 format; TRAFFIC_REPORT MSG 246 spec; latency chain diagram; trade non-coop tecnologie |
| **INT-15 Privacy** | Anonymization pipeline dichiarata; no algoritmo, no latency, no evidence chain | Pipeline 8-step con latency per step; YOLOv8n spec INT8 TensorRT; ANPR fine-tuning approach; JSON log record completo; hash chain immutabile con ECDSA firma batch; failure mode full-blur fallback; test plan 8 test |

**Riduzione gap review critica §4.8 Critica 2:**

| Critica originale | Status in v2.0 |
|---|---|
| INT-03: "MAVLink v2.0 + AES-256-GCM senza formato payload byte-level" | CHIUSO: 14 messaggi specificati byte per byte |
| INT-03: "No codice di rilevazione errore" | CHIUSO: CRC-X25 con polinomio, init, CRC_EXTRA specificati |
| INT-03: "No retry logic" | CHIUSO: 3× retry 500 ms + state machine 5 stati |
| INT-03: "No behavior link drop > 5s" | CHIUSO: timing diagram con azioni per ogni stato |
| INT-04: SATCOM non specificato | CHIUSO: trade + AT commands + latency budget |
| INT-05: Bus non scelto | CHIUSO: trade + architettura ibrida selezionata |
| INT-13: DAA senza algoritmo | CHIUSO (cooperativo); PRELIMINARY (non-cooperativo, vincolato a TRL) |
| INT-15: Pipeline senza step | CHIUSO: pipeline 8-step con latency misurabili |

---

<a name="gap"></a>
## Gap residui per Fase 1 Engineering (M+10/M+18)

I seguenti gap rimangono aperti e devono essere risolti in Fase 1:

| Gap ID | Interfaccia | Descrizione | Owner | Deadline | Rischio se non risolto |
|---|---|---|---|---|---|
| GAP-01 | INT-03 | Specifiche interne FCS JOUAV CW-30E non ancora documentate dal vendor (MAVLink dialect extension proprietaria) | Avionics Lead + JOUAV Liaison | M+6 (vendor RFQ) | Incompatibilità GCS↔FCS, rework integration +€15-30k |
| GAP-02 | INT-04 | Coverage test SATCOM Iridium in Valle Pentema (shadow zone orografiche) non ancora eseguito | RF Systems Engineer | M+11 (field test) | SATCOM non disponibile in shadow zone, RTL prematuro |
| GAP-03 | INT-04 | Latency Iridium end-to-end misurata in ambiente reale (vs spec 1.5 s tipica) | RF Systems Engineer | M+13 (integration test) | RTL command delay > 3 s, safety concern SORA |
| GAP-04 | INT-05 | MC hardware finale non selezionato (Jetson Orin NX o alternativa), trade study richiesto | Avionics Lead | M+7 | Bus architecture può cambiare parzialmente |
| GAP-05 | INT-05 | Shutter lag calibrazione Sony α7R IV (geotagging accuracy) | Payload SE | M+10 (DDT) | Geotagging error > 5 cm, fotogrammetria degradata |
| GAP-06 | INT-13 | ENAC feedback su necessità DAA non-cooperativo per SAIL III Pentema | Aviation Regulatory Counsel | M+6 (pre-application) | Se richiesto: +€150-300k + 6-12 mesi ritardo |
| GAP-07 | INT-13 | Test DO-365B MOPS compliance per ADS-B IN receiver selezionato | Avionics Lead | M+10 (DDT) | Non-conformità MOPS, SORA rejection |
| GAP-08 | INT-15 | DPIA formale redatta e inviata al Garante | Data Privacy Counsel + DPO | M+7 (DPIA submission) | Operazioni bloccate senza DPIA approvata |
| GAP-09 | INT-15 | YOLOv8n performance su dataset immagini UAV italiane (non COCO) | AI/ML Engineer | M+11 (DDT) | False negative rate > 5%, GDPR risk residuo |
| GAP-10 | INT-03/04 | Dual-link switch seamless test (no command gap durante transizione RF→SATCOM) | Avionics Lead | M+13 (integration) | Gap > 2 s durante switch, LINK_LOST prematuro |

---

<a name="riferimenti"></a>
## Riferimenti

[^MAVLink]: MAVLink Common Message Set v2.0, Dialect specification. https://mavlink.io/en/messages/common.html (online, aggiornamento continuo; versione di riferimento MAVLink Wire Protocol §2.4 per CRC-X25). Confidence: high.

[^DO377]: RTCA DO-377A, Minimum Operational Performance Standards for C2 Link Systems Supporting Operations of Unmanned Aircraft Systems in U.S. Airspace (2020). Confidence: high (standard RTCA pubblicato, in uso per certificazione FAA/EASA C2 link).

[^DO326A]: RTCA DO-326A / EUROCAE ED-202A, Airworthiness Security Process Specification (2014). Confidence: high.

[^NIST38D]: NIST SP 800-38D, Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC (2007). Confidence: high (norma crittografica NIST definitiva).

[^DO260B]: RTCA DO-260B, Minimum Operational Performance Standards for 1090 MHz Extended Squitter ADS-B and TIS-B (2009, Change 2 2012). MOPS per ADS-B IN/OUT. Confidence: high.

[^DO365B]: RTCA DO-365B, Minimum Operational Performance Standards for Detect and Avoid (DAA) Systems (2020). Confidence: high (standard primario RTCA per DAA UAS). Nota: versione B aggiornata da DO-365A con ampliamento scenari BVLOS.

[^ED270]: EUROCAE ED-270, Minimum Operational Performance Standards for UAS Geo-Awareness and ADS-L (2022). Confidence: high (standard EUROCAE U-Space).

[^EDPB]: EDPB Guidelines 01/2022 on data subject rights, right of access (Version 2.0, adopted 28 March 2023). Confidence: high.

[^ARP4754A]: SAE ARP4754A, Guidelines for Development of Civil Aircraft and Systems (2010). Applicato per DAL allocation interfacce. Confidence: high.

[^DO178C]: RTCA DO-178C, Software Considerations in Airborne Systems and Equipment Certification (2011). Applicato per DAL software. Confidence: high.

[^SORA25]: JARUS SORA 2.5 (Joint Authorities for Rulemaking on Unmanned Systems), Specific Operations Risk Assessment, versione 2.5 (2022). Applicato per lost-link procedure e DAA thresholds. Confidence: high.

[^ITU618]: ITU-R P.618-14, Propagation data and prediction methods required for the design of Earth-space telecommunication systems (2019). Applicato per rain fade SATCOM L-band Liguria. Confidence: high.

---

*Fine documento A4-ICD-DETAILED-v2.0.md*

*Versione: 2.0 | Data: 2026-05-17 | Owner: Avionics GNC Engineer, Firmamento Technologies*
*Baseline parent: A4-ICD-PRELIMINARE-v1.0.md (M+3)*
*Trigger: audit review critica Cap. 4 §4.8 Critica 2*
