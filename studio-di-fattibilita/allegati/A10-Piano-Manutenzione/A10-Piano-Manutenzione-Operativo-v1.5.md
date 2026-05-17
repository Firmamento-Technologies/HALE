# Allegato A.10 — Piano di Manutenzione Operativo v1.5

**Volume 2, Allegato A.10**
**Progetto HALE — Firmamento Technologies**
**Percorso 6A — VTOL Pilota Pentema (Comune di Torriglia, GE)**

> Versione: **v1.5** (aggiornamento da v1.0 preliminary)
> Data emissione: 2026-05-17
> Sostituisce: A10-Piano-Manutenzione-Preliminare.md (v1.0, M+3)
> Prossima revisione: v2.0 target M+10 (gate G3 + SORA application definitiva)
> Confidence aggregato: **MEDIUM** — richiede validazione con manuale tecnico OEM JOUAV CW-30E
> (non disponibile pubblicamente, da acquisire con contratto RFQ M+6) e assunzione maintainer
> certificato (M+6-M+9). I valori economici sono stime di benchmark; i valori di vita
> utile componenti derivano da datasheet vendor non validati da operatori EU indipendenti.

---

## Indice

- [Sezione 1 — Inquadramento normativo e metodologico](#sezione-1)
- [Sezione 2 — Architettura del programma di manutenzione](#sezione-2)
- [Sezione 3 — Maintenance Tasks per sistema](#sezione-3)
- [Sezione 4 — Calendar Maintenance Y1 (80 missioni target)](#sezione-4)
- [Sezione 5 — Maintenance Organization](#sezione-5)
- [Sezione 6 — Spare Parts Strategy](#sezione-6)
- [Sezione 7 — Records, Logbook e Compliance](#sezione-7)
- [Sezione 8 — Costi LCC Y1-Y5](#sezione-8)
- [Sezione 9 — Sicurezza e Ambiente (HSE)](#sezione-9)
- [Sezione 10 — Gap residui pre-operations Y1](#sezione-10)
- [Sezione 11 — Linkage cross-volume](#sezione-11)

---

## Sezione 1 — Inquadramento normativo e metodologico {#sezione-1}

### 1.1 Scopo e campo di applicazione

Il presente Piano di Manutenzione Operativo (PMO) definisce la struttura, le procedure, le responsabilità e i costi del programma di manutenzione per il sistema UAS baseline del Percorso 6A, identificato nella piattaforma JOUAV CW-30E (VTOL ibrido, MTOM 18 kg, endurance dichiarata 6 h, payload 7 kg) operata nel comune di Pentema (Torriglia, GE) nel periodo Y1 (M+0 — M+12, target operazioni: 50-80 missioni).

Il PMO si applica a:
- Velivolo (airframe + propulsione + avionica + payload)
- Ground Control Station fissa (Pentema) e mobile opzionale
- Attrezzature di terra e GSE (Ground Support Equipment)
- Payload integrati: EO Sony Alpha 7R IV, IR Workswell LWIR 640x512, payload comunicazioni

Il PMO supporta: (a) la pre-application ENAC SORA SAIL II-III BVLOS; (b) il calcolo dei costi operativi LCC per Cap. 8 §8.5.1; (c) la conformita EN 9110 per l'organizzazione di manutenzione.

**Piano B (vendor backup)**: se la piattaforma JOUAV CW-30E risultasse non disponibile o bloccata per ragioni di supply chain geopolitica (RSK-GEO-003), il Piano di Manutenzione si applica mutatis mutandis alla piattaforma Tekever AR3 (PT, MTOM 25 kg, endurance 16 h) con intervalli di ispezione da rideterminare secondo manuale OEM Tekever.

### 1.2 Quadro normativo di riferimento

#### 1.2.1 EN 9110:2018 — Maintenance Organisations

La norma EN 9110:2018 (Quality Management Systems — Requirements for Aviation Maintenance Organizations) definisce i requisiti per le organizzazioni che eseguono manutenzione su prodotti aeronautici. Per Firmamento Technologies in fase Y1, l'applicazione avviene in forma di **auto-dichiarazione di conformita interna** (non certificazione accreditata da ente terzo, che e target M+12-18).

Requisiti EN 9110 che il PMO affronta:
- Definizione di ruoli e responsabilita della Maintenance Organization (vedi Sezione 5)
- Procedure documentate per ogni categoria di manutenzione (Sezione 2-3)
- Gestione della configurazione dei componenti (Component Logbook, Sezione 7)
- Controllo dei ricambi e materiali (Sezione 6)
- Competenza e addestramento del personale (Sezione 5)
- Non-conformity management e Corrective Action (Sezione 2.3)
- Audit interni periodici (Sezione 7)

Nota caveat: la certificazione formale EN 9110 da parte di organismo terzo accreditato (es. ACCREDIA) non e requisito ENAC obbligatorio per operatore UAS Specific Category Y1, ma e fortemente raccomandata come evidenza di competenza OSO #03 (SORA 2.5) e come prerequisito di contratti PA.

#### 1.2.2 AS/EN 9100 Rev. D — Quality Management Aerospace

AS/EN 9100D integra ISO 9001:2015 con requisiti aggiuntivi specifici per l'industria aeronautica e spaziale. Per Firmamento in Y1 come operatore di servizi (non OEM), si applicano i requisiti relativi a:
- Gestione del rischio operativo (integrazione con Risk Register A.2)
- Controllo di prodotto e servizi non conformi
- Configuration management (componenti tracciati per s/n e life)
- Supplier control (qualifica vendor JOUAV, Workswell, Sony)
- Operational safety documentation

Target certificazione AS/EN 9100D: M+18-24 (post-scale-up Y2).

#### 1.2.3 ENAC Regolamento APR Edizione 3 — Manutenzione SAPR Specific

Il Regolamento ENAC per i Sistemi Aeromobili a Pilotaggio Remoto (APR), Edizione 3 (riferimento: ENAC, Roma), art. 19 "Manutenzione del SAPR", stabilisce:

- L'operatore Specific Category e responsabile di mantenere il SAPR in condizioni di aeronavigabilita
- Le procedure di manutenzione devono essere documentate e seguite
- Il logbook deve essere tenuto aggiornato e disponibile per ispezione ENAC
- Le sostituzioni di componenti critici (motori, FCS, strutture primarie) devono essere documentate con riferimento al manuale OEM o, in assenza, a una procedura approvata internamente
- Per operazioni BVLOS Specific, ENAC puo richiedere dimostrazione del programma di manutenzione nell'ambito della SORA application

Impatto PMO: il Piano di Manutenzione e un documento obbligatorio da allegare alla dichiarazione ENAC Specific + SORA application. Il presente PMO v1.5 costituisce l'evidenza iniziale; la versione v2.0 (M+10) sara quella allegata alla SORA application definitiva.

#### 1.2.4 Reg. UE 2019/947 + 2019/945 — Conformita operativa e aeronavigabilita

Il Reg. UE 2019/947 (operazioni UAS), artt. 13-16 (Specific Category):
- Art. 14: operatore responsabile della manutenzione del SAPR
- Art. 15: obblighi di notifica incidenti e gravi inconvenienti all'autorita nazionale (ENAC)
- Artt. 16-17: procedure operative documentate (include manutenzione pre-post flight)

Il Reg. UE 2019/945 (requisiti tecnici prodotti UAS) definisce i requisiti di costruzione ma non istituisce un tipo di certificazione obbligatoria per Class III operato in Specific Category. Tuttavia, la Declaration of Conformity del costruttore (JOUAV) e un'evidenza rilevante per OSO #02 e OSO #04.

#### 1.2.5 ISO 14001:2015 — Gestione ambientale

La ISO 14001 si applica alla gestione ambientale delle attivita di manutenzione, in particolare:
- Smaltimento batterie LiPo esaurite (rifiuto speciale RAEE + pile ai sensi D.Lgs. 49/2014)
- Gestione solventi e materiali da pulizia
- Smaltimento componenti compositi (fibra di carbonio/vetro: rifiuto speciale ai sensi D.Lgs. 152/2006)
- Riduzione impatto acustico aree alpine

Target ISO 14001: in scope per certificazione integrata Y2-Y3 (insieme AS/EN 9100D).

#### 1.2.6 D.Lgs. 81/2008 — Sicurezza lavoratori

Titolo XI (ATEX, rischio esplosione) si applica all'area di ricarica/storage batterie LiPo (classificazione zona da determinare con VVF locale, RSK-REG-022). Il Documento di Valutazione dei Rischi (DVR) deve includere le attivita di manutenzione UAS (movimentazione batterie, uso solventi, uso strumenti in quota, rischio ergonomico).

---

## Sezione 2 — Architettura del programma di manutenzione {#sezione-2}

### 2.1 Struttura generale

Il programma di manutenzione del Percorso 6A adotta un approccio **MSG-3 semplificato** (Maintenance Steering Group logic, adattato per UAS commerciale non certificato EASA Type Certificate), integrato con manutenzione **on-condition** per i componenti con deterioramento misurabile (batterie, motori).

Le categorie principali sono:

| Categoria | Codice | Logica | Trigger |
|---|---|---|---|
| Pre-flight Check | MX-PRE | Procedurale obbligatoria | Ogni missione |
| Post-flight Check | MX-POST | Procedurale obbligatoria | Ogni missione |
| Daily Inspection | MX-DAILY | Intervallo calendario | Giorno operativo |
| Weekly Inspection | MX-WEEKLY | Intervallo calendario | Settimana operativa |
| Monthly Inspection | MX-MONTHLY | Intervallo calendario | Ogni 4 settimane operative |
| 25-hour Inspection | MX-25H | Intervallo ore volo | Ogni 25 ore cumulate |
| 100-hour Inspection | MX-100H | Intervallo ore volo | Ogni 100 ore cumulate |
| Annual Inspection | MX-ANN | Intervallo calendario | 12 mesi |
| Manutenzione correttiva | MX-COR | On-condition | Post-anomalia / post-failure |
| Manutenzione straordinaria | MX-EXTR | Evento | Post-incidente / hard landing |
| Overhaul motore/batteria | MX-OVH | Ciclo vita componente | Secondo life limit OEM |

### 2.2 Manutenzione preventiva (PM)

La manutenzione preventiva (Preventive Maintenance, PM) e pianificata secondo intervalli fissi (calendario o ore volo) indipendentemente dallo stato osservato del componente. Per il CW-30E in Y1 (50-80 missioni, missione media 2-3 ore, totale ore stimate 100-240 h/anno):

Intervalli PM principali:
- **MX-PRE/POST**: ogni volo (obbligatorio, non derogabile)
- **MX-DAILY**: ogni giorno operativo (anche se nessun volo effettuato, se velivolo in hangar)
- **MX-WEEKLY**: ogni settimana operativa
- **MX-MONTHLY**: ogni 4 settimane (o mensile solare)
- **MX-25H**: ogni 25 ore di volo cumulate (circa ogni 8-12 missioni da 2-3 h)
- **MX-100H**: ogni 100 ore di volo cumulate (circa M+5 e M+10 in scenario 80 missioni)
- **MX-ANN**: al termine dei 12 mesi operativi

Nota orografia Pentema: le missioni in ambiente alpino con vento canalizzato, turbolenza e temperature sotto zero aumentano il tasso di usura strutturale e dei motori stimato del 15-25% rispetto a condizioni nominal sea-level. Gli intervalli PM vanno pertanto considerati come **massimi**, con possibilita di anticipazione on-condition se health monitoring rileva degradazione.

### 2.3 Manutenzione correttiva (CM)

La manutenzione correttiva (Corrective Maintenance, CM) e attivata da:
1. **Anomalia rilevata in volo** (FCS fault log, sensor dropout, vibrazioni anomale)
2. **Anomalia rilevata a terra** (ispezione visiva, test funzionale)
3. **Failure** che preclude la missione successiva

Processo CM:
1. Apertura Non-Conformity Report (NCR) nel sistema di tracciabilita
2. Root Cause Analysis (RCA) semplificata (per componente critico: FMECA reference Cap. 6 §6.4)
3. Repair o sostituzione componente (secondo manuale OEM o procedura interna approvata)
4. Test funzionale post-repair (ground test + eventuale volo di verifica)
5. Chiusura NCR con firma Maintenance Manager
6. Aggiornamento logbook e component record

### 2.4 Ispezioni post-evento straordinario

Attivate dopo:
- **Hard landing** (impatto fuori envelope normale): ispezione MX-EXTR full (struttura + landing gear + motori + avionica)
- **Bird strike sospetto**: ispezione struttura + eliche + sensori
- **Volo in condizioni meteorologiche severe** (gelo, grandine, vento > limite): ispezione MX-EXTR light (struttura + sensori + connettori)
- **Immersione o contatto con acqua**: ispezione completa + asciugatura 24h prima di riattivazione
- **Incidente formale** (ai sensi Reg. UE 2019/947 art. 15): fermo velivolo fino ad autorizzazione ENAC + apertura dossier ANSV se richiesto

### 2.5 Overhaul programmato

L'overhaul (MX-OVH) e pianificato per i componenti con life limit stabilito da OEM o da analisi on-condition:

| Componente | Life limit stimato | Trigger overhaul |
|---|---|---|
| Motori VTOL (4 unita) | 200-400 h o 2 anni (valore vendor da confermare) | Raggiungimento limite o degradazione misurata |
| Motore cruise (1 unita) | 300-500 h o 2 anni | Come sopra |
| Pack batteria LiPo propulsione | 300-500 cicli o 24-36 mesi | Capacita residua < 80% nominale |
| Pack batteria LiPo payload | 200-400 cicli o 18-24 mesi | Come sopra |
| FCS / computer di volo | 5 anni o 1.000 h (elettronica) | Failure o obsolescenza firmware |
| Struttura composita | Ispezione NDT ogni 200 h o 3 anni | Crack / delamination / impatto |

Nota caveat: i valori di life limit sono tratti da benchmark di mercato UAS commerciale (medium confidence). Il manuale tecnico OEM JOUAV CW-30E (da acquisire al M+6 con RFQ) potrebbe stabilire limiti differenti, che prevalgono sui presenti.

---

## Sezione 3 — Maintenance Tasks per sistema {#sezione-3}

### 3.0 Legenda tabelle

- **Freq**: PRE = pre-flight; POST = post-flight; DAILY = giornaliero; WEEKLY = settimanale; MONTHLY = mensile; 25H = ogni 25 ore volo; 100H = ogni 100 ore volo; ANN = annuale; OVH = overhaul
- **Pers**: PIC = Pilota in Comando; ML1 = Maintainer Livello 1 (qualificato base); ML2 = Maintainer Livello 2 (qualificato avanzato, capace di smontaggio motori e FCS); OEM = tecnico o supervisione JOUAV
- **Durata**: ore stimate per attivita; includono setup strumenti ma non logistica parti
- **Costo mat**: materiali e consumabili stimati; non include manodopera
- **Costo MdO**: manodopera stimata a €40-60/h (ingegnere/maintainer Y1)
- **Rif. OEM**: placeholder — da compilare con sezione manuale JOUAV CW-30E al M+6

---

### 3.1 Sistema 1 — Propulsione ed energia

Comprende: 4 motori brushless VTOL + 1 motore cruise (o configurazione specifici CW-30E), ESC corrispondenti, pack batterie LiPo propulsione, pack batterie payload, sistema BMS (Battery Management System), connettori di potenza.

| ID Task | Descrizione attivita | Freq | Strumenti | Pers | Durata (h) | Costo mat (€) | Costo MdO (€) | Rif. OEM |
|---|---|---|---|---|---|---|---|---|
| MX-PROP-001 | Ispezione visiva eliche (crepe, scheggiature, deformazioni, corrosione hub) | PRE | Torcia ispezione, calibro | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-PROP-002 | Controllo bilanciamento dinamico eliche (vibrazione anormale post-impatto) | On-condition | Bilanciatore propeller portatile | ML1 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-PROP-003 | Sostituzione elica (danno o life limit) | On-condition | Chiave torsiometrica, set esagoni | ML1 | 0.3 | 60-150 per coppia | 15 | JOUAV TBD §X.X |
| MX-PROP-004 | Ispezione visiva motori VTOL (connettori, statore, contaminazione FOD) | PRE | Torcia, specchio ispezione | PIC o ML1 | 0.15 | 0 | 7 | JOUAV TBD §X.X |
| MX-PROP-005 | Test run motori VTOL a terra (spin-up sequenziale, check current draw) | DAILY | GCS + telemetria | PIC o ML1 | 0.2 | 0 | 10 | JOUAV TBD §X.X |
| MX-PROP-006 | Pulizia e ispezione connettori ESC-motore (ossidazione, pin lenti) | WEEKLY | Contact cleaner, torcia, multimetro | ML1 | 0.3 | 5 | 15 | JOUAV TBD §X.X |
| MX-PROP-007 | Ispezione cuscinetti motori VTOL (rumore, gioco assiale) | 25H | Stetoscopio meccanico, comparatore | ML1 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-PROP-008 | Smontaggio + ispezione approfondita motori VTOL (statore, avvolgimenti, cuscinetti) | 100H | Set attrezzi OEM, multimetro, ohmmetro di isolamento | ML2 | 3.0 | 0-50 (consumabili) | 150 | JOUAV TBD §X.X |
| MX-PROP-009 | Sostituzione motore VTOL (raggiungimento life limit o failure) | On-condition / OVH | Set attrezzi OEM, chiave torsiometrica, tester ESC | ML2 + OEM | 2.0 | 400-800 per motore | 100 | JOUAV TBD §X.X |
| MX-PROP-010 | Ispezione batteria LiPo propulsione (housing, terminali, rigonfiamento) | PRE | Calibro, torcia | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-PROP-011 | Misura tensione cella batteria + stato di carica (SoC) | PRE / POST | Multimetro, cell checker LiPo | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-PROP-012 | Ciclo di bilanciamento batteria LiPo (balance charge) | WEEKLY o dopo 5 cicli | Caricabatterie bilanciatrice LiPo (es. Junsi iCharger) | ML1 | 2.0 (non supervisionato) | 0 | 20 | JOUAV TBD §X.X |
| MX-PROP-013 | Storage LiPo a tensione di stoccaggio (3.75-3.85 V/cella) | Ogni stoccaggio > 7gg | Caricabatterie LiPo + storage mode | ML1 | 0.5 | 0 | 10 | JOUAV TBD §X.X |
| MX-PROP-014 | Capacity test batteria LiPo (discharge controllato, misura capacita reale) | MONTHLY | Battery analyzer / discharge tester | ML1 | 1.5 | 0 | 45 | JOUAV TBD §X.X |
| MX-PROP-015 | Sostituzione pack batteria propulsione (degradazione > 20% o fine vita) | On-condition / OVH | Set attrezzi, voltmetro | ML2 | 0.5 | 800-1.500 per pack | 25 | JOUAV TBD §X.X |
| MX-PROP-016 | Ispezione e pulizia sistema BMS (firmware version, alert log) | MONTHLY | Laptop + software BMS JOUAV | ML2 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-PROP-017 | Verifica sistema carica a bordo e connettori DC power | 25H | Multimetro, connettori test | ML1 | 0.3 | 0 | 15 | JOUAV TBD §X.X |
| MX-PROP-018 | Ispezione motore cruise (come MX-PROP-007-008, intervalli da OEM) | 100H | Come MX-PROP-008 | ML2 | 2.0 | 0-30 | 100 | JOUAV TBD §X.X |

**Note operative Sistema 1 — Pentema**:
- Temperature invernali (-10°C): le batterie LiPo perdono il 20-35% di capacita a -10°C rispetto a 25°C. Procedura obbligatoria: preriscaldamento batterie a minimo +10°C prima di qualsiasi carica o utilizzo. Non caricare LiPo a temperature < 5°C.
- Quota (1.100-1.300 m s.l.m.): densita aria ~87% rispetto a sea level — i motori VTOL devono compensare con maggior corrente assorbita (+10-15%); monitorare temperatura motori durante le prime missioni invernali.

---

### 3.2 Sistema 2 — Avionica e GNC (Guidance, Navigation, Control)

Comprende: FCS (Flight Control System, derivato Pixhawk o equivalente JOUAV proprietario), IMU primaria e ridondante, GPS/GNSS-RTK (ricevitore doppia antenna), barometro, magnetometro, computer di missione, datalink C2, software autopilota.

| ID Task | Descrizione attivita | Freq | Strumenti | Pers | Durata (h) | Costo mat (€) | Costo MdO (€) | Rif. OEM |
|---|---|---|---|---|---|---|---|---|
| MX-AVI-001 | Verifica lock GPS + qualita segnale (DOP, num. satelliti >= 8) | PRE | GCS display | PIC | 0.05 | 0 | 3 | JOUAV TBD §X.X |
| MX-AVI-002 | Calibrazione magnetometro (compass) | PRE (se richiesto dal FCS) | Area libera da metalli, GCS | PIC | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-AVI-003 | Verifica parametri FCS (PID, limiti, failsafe RTB) | PRE | GCS + QGC o software JOUAV | PIC o ML2 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-AVI-004 | Download e analisi log FCS post-volo (vibrazione, errori, anomalie) | POST | Laptop + Mission Planner / JOUAV GCS | ML1 o ML2 | 0.3 | 0 | 15 | JOUAV TBD §X.X |
| MX-AVI-005 | Aggiornamento firmware FCS (patch ufficiali OEM) | On-release | Laptop + cavo USB/OTG | ML2 | 1.0 | 0 | 50 | JOUAV TBD §X.X |
| MX-AVI-006 | Aggiornamento patch cybersecurity (Part-IS EASA Reg. UE 2023/203) | Mensile o on-release | Laptop + VPN sicura | ML2 + CISO | 0.5 | 0 | 50 | JOUAV TBD §X.X |
| MX-AVI-007 | Test failsafe (RTB simulato, lost-link test a terra) | WEEKLY | GCS + simulatore | PIC o ML2 | 0.3 | 0 | 15 | JOUAV TBD §X.X |
| MX-AVI-008 | Calibrazione IMU completa (6-point calibration) | MONTHLY o post-intervento strutturale | GCS + JOUAV calibration tool | ML2 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-AVI-009 | Ispezione fisica FCS (connettori, vibrazioni mount, termperatua housing) | 25H | Torcia, multimetro | ML1 | 0.3 | 0 | 15 | JOUAV TBD §X.X |
| MX-AVI-010 | Ispezione ricevitore GPS/RTK (antenna, cavi, connettori) | 25H | Torcia, tester coassiale | ML1 | 0.2 | 0 | 10 | JOUAV TBD §X.X |
| MX-AVI-011 | Verifica accuracy RTK (confronto coordinata nota ground mark) | MONTHLY | Rover RTK + target noto | PIC + ML1 | 0.5 | 0 | 50 | JOUAV TBD §X.X |
| MX-AVI-012 | Health check barometro e sonde aria (ostruzione, contaminazione) | WEEKLY | Torcia, aria compressa | ML1 | 0.2 | 0 | 10 | JOUAV TBD §X.X |
| MX-AVI-013 | Sostituzione modulo IMU o GPS (failure o life limit 1.000 h) | On-condition | Set attrezzi OEM, laptop | ML2 + OEM | 3.0 | 1.500-3.000 | 150 | JOUAV TBD §X.X |
| MX-AVI-014 | Verifica GCS (Ground Control Station) — sw, HW, alimentazione, display | DAILY | Checklist operativa | PIC o ML1 | 0.15 | 0 | 8 | JOUAV TBD §X.X |
| MX-AVI-015 | Backup configurazione FCS + waypoints + parametri missione | WEEKLY | Laptop + storage cifrato | ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-AVI-016 | Revisione completa sistema avionica (ispezione 100H) | 100H | Set attrezzi completo, oscilloscopio, DMM | ML2 + OEM | 4.0 | 50-200 | 200 | JOUAV TBD §X.X |
| MX-AVI-017 | Audit Part-IS: verifica log accessi, aggiornamenti sw, vulnerabilita note | ANN | Checklist CISO + log system | ML2 + CISO | 2.0 | 0 | 200 | JOUAV TBD §X.X |

---

### 3.3 Sistema 3 — Struttura e carrello

Comprende: fusoliera (composito, materiale da confermare OEM), ala fissa (composito), boom + gondole VTOL, sistemi di smontaggio rapido, landing gear (struttura + dampers), meccanismi di lock/unlock VTOL-cruise transition.

| ID Task | Descrizione attivita | Freq | Strumenti | Pers | Durata (h) | Costo mat (€) | Costo MdO (€) | Rif. OEM |
|---|---|---|---|---|---|---|---|---|
| MX-STR-001 | Ispezione visiva fusoliera, ala, boom (crepe, delaminazione, impatti) | PRE | Torcia, lente 10x | PIC o ML1 | 0.2 | 0 | 10 | JOUAV TBD §X.X |
| MX-STR-002 | Verifica integrita giunzioni rapide ala-fusoliera, boom-gondola | PRE | Torcia, mano (gioco residuo) | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-STR-003 | Ispezione landing gear (dampers, struttura, fissaggi) | PRE | Torcia | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-STR-004 | Verifica torque fissaggi critici (viti strutturali secondo tabella torque OEM) | 25H | Chiave torsiometrica calibrata | ML1 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-STR-005 | Ispezione approfondita superfici composte (tap test, lente UV) | 25H | Martello tap test, lente, torcia UV | ML1 | 1.0 | 0 | 50 | JOUAV TBD §X.X |
| MX-STR-006 | NDT compositi (termografia o ultrasuoni su zone critiche) | 100H o post-impatto | Termocamera o ultrasuoni portatile | ML2 o subcontractor NDT | 3.0 | 0 | 150-300 | JOUAV TBD §X.X |
| MX-STR-007 | Verifica meccanismi transizione VTOL-cruise (kinematic, lock, servo) | WEEKLY | Ispezione visiva + funzionale | ML1 | 0.3 | 0 | 15 | JOUAV TBD §X.X |
| MX-STR-008 | Lubrificazione punti articolati (landing gear, flap, servo links) | MONTHLY | Lubrificante appropriato (OEM spec) | ML1 | 0.3 | 5-10 | 15 | JOUAV TBD §X.X |
| MX-STR-009 | Sostituzione dampers landing gear (usura o fine vita) | On-condition | Set attrezzi meccanici | ML1 | 1.0 | 80-200 per coppia | 50 | JOUAV TBD §X.X |
| MX-STR-010 | Riparazione compositi minori (scratches, filling, gelcoat) | On-condition | Kit riparazione epoxy + stucco | ML2 | 2.0-4.0 | 30-80 | 100-200 | JOUAV TBD §X.X |
| MX-STR-011 | Revisione strutturale annuale completa (100H + ANN) | ANN | Tutti gli strumenti + NDT | ML2 + OEM | 8.0 | 200-500 | 400 | JOUAV TBD §X.X |
| MX-STR-012 | Verifica sigillature (impermeabilizzazione zona batterie, payload bay) | MONTHLY | Torcia, ispezione tattile | ML1 | 0.2 | 0-20 (sigillante) | 10 | JOUAV TBD §X.X |
| MX-STR-013 | Protezione anticorrosione (trattamento superfici metalliche, es. landing gear) | 6 mesi | Prodotto anticorrosivo OEM-compatibile | ML1 | 0.5 | 20-40 | 25 | JOUAV TBD §X.X |

**Note operative Sistema 3 — Pentema**:
- L'ambiente alpino con cicli gelo-disgelo frequenti (inverno) accelera la fatica termica dei compositi e dei sigillanti. Aumentare la frequenza MX-STR-005 a ogni 15H durante i mesi novembre-marzo (adattamento locale).
- Dopo ogni atterraggio in terreno non preparato (operativo standard Pentema), eseguire MX-STR-001-003 prima del successivo decollo (non solo pre-volo programmato del giorno successivo).

---

### 3.4 Sistema 4 — Payload EO/IR e gimbal

Comprende: gimbal stabilizzato (3 assi, tipo da confermare OEM), camera EO Sony Alpha 7R IV (61 Mpx), sensore IR Workswell LWIR 640x512, payload comunicazioni, ottica, interfacce elettriche e meccaniche payload-airframe.

| ID Task | Descrizione attivita | Freq | Strumenti | Pers | Durata (h) | Costo mat (€) | Costo MdO (€) | Rif. OEM |
|---|---|---|---|---|---|---|---|---|
| MX-PLD-001 | Ispezione visiva gimbal (housing, assi, connettori, protezione ottica) | PRE | Torcia, ispezione visiva | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-PLD-002 | Verifica lock gimbal (stabilizzazione a terra, risposta comandi) | PRE | GCS payload control | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-PLD-003 | Pulizia elemento ottico Sony 7R IV (soffiatore + pennello + lens cloth) | PRE | Kit pulizia ottica professionale | PIC o ML1 | 0.1 | 0-2 | 5 | Sony manuale |
| MX-PLD-004 | Verifica focale + esposimetria camera EO (target noto a terra) | PRE | Target radiometrico o SIAF panel | PIC o ML1 | 0.1 | 0 | 5 | Sony + JOUAV |
| MX-PLD-005 | Calibrazione sensore IR (NUC — Non-Uniformity Correction, standard body interno) | PRE o ogni 30 min in volo (automatica) | GCS IR software + shutter automatico | ML1 | 0.05 | 0 | 3 | Workswell manual |
| MX-PLD-006 | Pulizia finestra IR (germanio) con tessuto specifico anti-statico | WEEKLY | Panno anti-statico germanio (no solventi convenzionali) | ML1 | 0.1 | 0-5 | 5 | Workswell manual |
| MX-PLD-007 | Download e verifica integrita dati missione (EO + IR, formato + geotag) | POST | Laptop + software Workswell + lightroom/Metashape | ML1 | 0.2 | 0 | 10 | Workswell + JOUAV |
| MX-PLD-008 | Ispezione connettori payload (power + data) + interfaccia meccanica airframe | WEEKLY | Torcia, multimetro | ML1 | 0.2 | 0 | 10 | JOUAV TBD §X.X |
| MX-PLD-009 | Calibrazione radiometrica assoluta sensore IR (target a temperatura nota) | MONTHLY | Blackbody portatile (es. HGH Infrared o equiv.) | ML2 | 1.0 | 0 | 50 | Workswell manual |
| MX-PLD-010 | Calibrazione geometrica gimbal (boresight correction, roll/pitch offset) | 25H o post-intervento meccanico | Target GCP noto + software photogrammetria | ML2 + surveying | 2.0 | 0 | 100 | JOUAV TBD §X.X |
| MX-PLD-011 | Sostituzione filtri ND camera EO (danno o degradazione) | On-condition | Set chiave filtri + filtri ND di ricambio | ML1 | 0.1 | 30-80 per filtro | 5 | Sony manuale |
| MX-PLD-012 | Verifica firmware camera + IR (aggiornamenti vendor) | 25H o on-release | Laptop + software OEM | ML2 | 0.5 | 0 | 25 | Sony + Workswell |
| MX-PLD-013 | Ispezione motori gimbal (gioco, risposta, corrente) | 25H | GCS payload + multimetro | ML1 | 0.3 | 0 | 15 | JOUAV TBD §X.X |
| MX-PLD-014 | Sostituzione gimbal completo (failure motori o damage) | On-condition | Set attrezzi OEM | ML2 + OEM | 2.0 | 2.000-5.000 | 100 | JOUAV TBD §X.X |
| MX-PLD-015 | Pulizia e ispezione payload comunicazioni (antenne, connettori, dissipatori) | MONTHLY | Torcia, contattore | ML1 | 0.3 | 5 | 15 | TBD vendor |
| MX-PLD-016 | Verifica integrita storage interno camera (SD card o SSD) | WEEKLY | Laptop + utility disk | ML1 | 0.1 | 0 | 5 | Sony manuale |

---

### 3.5 Sistema 5 — Sistemi link e RF

Comprende: radio C2 (tipicamente 900 MHz o 2.4/5.8 GHz FHSS, da confermare OEM JOUAV), antenne direzionali GCS, link telemetria velivolo, eventuale SATCOM Iridium per BVLOS long range, ADS-B transponder / receiver (se installato), modulo LTE opzionale backup C2.

| ID Task | Descrizione attivita | Freq | Strumenti | Pers | Durata (h) | Costo mat (€) | Costo MdO (€) | Rif. OEM |
|---|---|---|---|---|---|---|---|---|
| MX-RF-001 | Verifica potenza segnale C2 (RSSI a terra, test link bidirezionale) | PRE | GCS display + RF analyzer opzionale | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-RF-002 | Verifica latenza C2 (round-trip time < limite operativo) | PRE | GCS display | PIC | 0.05 | 0 | 3 | JOUAV TBD §X.X |
| MX-RF-003 | Verifica link telemetria dati missione (throughput, packet loss) | PRE | GCS display | PIC o ML1 | 0.05 | 0 | 3 | JOUAV TBD §X.X |
| MX-RF-004 | Ispezione fisica antenne velivolo (connettori SMA/RP-SMA, housing, orientamento) | PRE | Torcia, chiave antenne | PIC o ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-RF-005 | Ispezione antenne direzionali GCS (supporto, azimut, connettori) | DAILY | Torcia, ispezione visiva | ML1 | 0.1 | 0 | 5 | JOUAV TBD §X.X |
| MX-RF-006 | Misura VSWR (Voltage Standing Wave Ratio) antenne velivolo | MONTHLY | VNA portatile (es. NanoVNA) | ML2 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-RF-007 | Test link SATCOM Iridium (se installato) — connessione + latenza | WEEKLY | Iridium terminal + GCS | ML1 | 0.2 | 0 | 10 | Iridium manual |
| MX-RF-008 | Verifica e aggiornamento configurazione RF (frequenze, potenze, canali) | 25H | Laptop + software RF JOUAV | ML2 | 0.5 | 0 | 25 | JOUAV TBD §X.X |
| MX-RF-009 | Sostituzione antenna velivolo (danno fisico o degradazione VSWR) | On-condition | Chiave antenne, connettori | ML1 | 0.2 | 30-100 per antenna | 10 | JOUAV TBD §X.X |
| MX-RF-010 | Sostituzione modulo radio C2 (failure o fine vita) | On-condition | Set attrezzi OEM + laptop | ML2 + OEM | 2.0 | 500-1.500 | 100 | JOUAV TBD §X.X |
| MX-RF-011 | Verifica conformita spettrale (AGCOM LRA 5.16.13) — test con spectrum analyzer | ANN | Spectrum analyzer portatile o laboratorio | ML2 + RF consultant | 4.0 | 0 | 400 | AGCOM LRA |
| MX-RF-012 | Verifica link ADS-B (se installato) | PRE o WEEKLY | GCS + ADS-B receiver test | PIC o ML1 | 0.05 | 0 | 3 | ENAC APR |
| MX-RF-013 | Test modulo LTE backup C2 (SIM attiva, connessione dati, failover) | WEEKLY | Smartphone o laptop + SIM test | ML1 | 0.15 | 0 | 8 | TBD carrier |

---

## Sezione 4 — Calendar Maintenance Y1 (80 missioni target) {#sezione-4}

### 4.1 Assunzioni operative Y1

- **Periodo operativo**: M+6 — M+18 (primi 12 mesi di operativi, contati da inizio operazioni effettive)
- **Missioni target**: 80 (50 minimo per evidenza SORA)
- **Cadenza**: 1-2 missioni/settimana, concentrata aprile-ottobre; limitata novembre-marzo (meteo)
- **Durata media missione**: 2-3 h di volo (incluse transizioni VTOL-cruise)
- **Ore volo stimate Y1**: 160-240 h (scenario 80 missioni x 2-3 h)
- **Ore volo scenario 50 missioni (minimo)**: 100-150 h

Per semplicita di pianificazione, si assume il **calendario 100-hour inspection a M+5 e M+10** dall'inizio operazioni (corrispondente a ~80 missioni x 2.5 h media = 200 h totali, quindi due 100H inspection durante Y1 nel caso ottimistico).

### 4.2 Pianificazione maintenance per milestone Y1

| Milestone | Mese operativo | Contenuto | Durata prevista | Risorse |
|---|---|---|---|---|
| Go-ahead operativo | M+6 | Accettazione piattaforma + pre-delivery inspection | 2-3 giorni | ML2 + OEM |
| Primo volo locale | M+7 | Pre-flight MX-PRE, post-flight MX-POST + report | 4-6 h totali | PIC + ML1 |
| Ispezione 25H (#1) | M+8 circa | Prima 25H inspection (dopo ~10 missioni 2.5h) | 1 giornata (8 h) | ML2 |
| Ispezione 25H (#2) | M+9 circa | Seconda 25H inspection | 1 giornata | ML2 |
| Ispezione mensile #1-#3 | M+7, M+8, M+9 | Monthly inspection (MX-MONTHLY) | 4-6 h ciascuna | ML1 + ML2 |
| Ispezione 100H (#1) | M+10 circa | Prima 100H inspection completa (scenario 80 missioni) | 2-3 giorni | ML2 + OEM |
| Ispezione 25H (#3 e #4) | M+10-M+11 | Terza e quarta 25H inspection | 1 giornata ciascuna | ML2 |
| Ispezione mensile #4-#6 | M+10, M+11, M+12 | Monthly inspection | 4-6 h ciascuna | ML1 + ML2 |
| Ispezione 100H (#2) | M+12-M+13 circa | Seconda 100H inspection (fine Y1 se 200+ h) | 2-3 giorni | ML2 + OEM |
| Annual inspection (ANN) | M+18 (fine Y1 calendario) | Ispezione annuale completa + audit logbook | 3-5 giorni | ML2 + OEM + Auditor |
| Overhaul componenti | Post-ANN o Y2 | Overhaul motori/batterie secondo life limit | 5-7 giorni | OEM + ML2 |

### 4.3 Carico manutentivo settimanale stimato Y1

| Attivita | Frequenza | Ore/evento | Ore/anno stimate |
|---|---|---|---|
| MX-PRE + MX-POST | Ogni missione (80) | 0.6 h tot | 48 h |
| MX-DAILY | ~100 giorni operativi | 0.3 h | 30 h |
| MX-WEEKLY | ~40 settimane operative | 1.5 h | 60 h |
| MX-MONTHLY | 12 mesi | 5 h | 60 h |
| MX-25H (x4 in 200H) | 4 eventi | 6 h | 24 h |
| MX-100H (x1-2) | 1-2 eventi | 20 h | 20-40 h |
| MX-ANN | 1 evento | 30 h | 30 h |
| MX-COR (stimato 10-15% missioni) | 8-12 eventi | 4 h media | 32-48 h |
| **Totale ore manutenzione Y1** | | | **304-340 h** |

Implicazione personale: con 1 maintainer part-time FTE 0.5 (circa 800-900 h/anno disponibili), il carico di 304-340 h e gestibile con un 40% del tempo del maintainer dedicato alla piattaforma. Il restante 60% copre GCS, payload, formazione e documentazione.

### 4.4 Stagionalita Pentema

| Periodo | Regime operativo | Note manutenzione |
|---|---|---|
| Aprile — Ottobre (estate operativa) | 60-70 missioni/7 mesi | Missioni intensive 1-2/settimana; pre-flight check estesi per polvere/polline |
| Novembre — Marzo (inverno limitato) | 10-20 missioni/5 mesi | Solo meteo favorevole; pre-flight check batterie obbligatorio a T>+5°C; ispezioni strutturali post-gelo |
| Gennaio — Febbraio (fermo operativo consigliato) | 0-3 missioni | Fermo elettivo se T < -10°C persistente; manutenzione programmata (100H, annual) |

---

## Sezione 5 — Maintenance Organization {#sezione-5}

### 5.1 Struttura organizzativa

Per Y1 (startup operations), l'organizzazione di manutenzione e **interna a Firmamento Technologies**, con supporto esterno per attivita specialistiche (NDT, RF, OEM). Non si prevede il conseguimento della certificazione EN 9110 formale in Y1; target M+18-24.

```
Maintenance Manager (0.3 FTE — coinvolto anche come Ingegnere Ops)
    |
    +-- Maintainer Certificato Principale (ML2, 0.5 FTE)
    |       Responsabile: 25H, 100H, ANN, MX-COR complessa
    |
    +-- PIC (Pilota in Comando) — abilitato ML1
    |       Responsabile: MX-PRE, MX-POST, MX-DAILY, osservazione anomalie
    |
    +-- Subcontractor NDT (esterno, on-call)
    |       Attivato per: MX-STR-006 (100H o post-impatto)
    |
    +-- OEM JOUAV Service Contract (remoto + missione annuale)
    |       Attivato per: ispezione accettazione, 100H, ANN, sostituzione motori
    |
    +-- Payload Specialist (esterno, on-call)
            Attivato per: calibrazione radiometrica IR assoluta, boresight correction
```

### 5.2 Requisiti di qualificazione del personale

#### 5.2.1 Maintenance Manager

Requisiti minimi Y1:
- Ingegnere aeronautico o meccanico (laurea triennale o magistrale)
- Esperienza minima 2 anni in manutenzione sistemi UAS o aeromobili
- Conoscenza dei requisiti ENAC Reg. APR Ed. 3 + AS/EN 9110
- Abilitazione interna Firmamento (approvazione Consiglio di Amministrazione)
- Referente ENAC per la Maintenance Organization

Competenze richieste:
- Apertura/chiusura NCR, gestione non-conformita
- Pianificazione del calendario di manutenzione
- Gestione fornitori e contratti SLA
- Reportistica manutenzione per audit ENAC

#### 5.2.2 Maintainer Livello 2 (ML2)

Requisiti minimi Y1:
- Diploma tecnico (aeronautico, elettronico, meccatronico) o esperienza equivalente 3+ anni
- Completamento corso formazione OEM JOUAV (in loco o remoto, target M+6-M+9)
- Conoscenza pratica: FCS, propulsione brushless, LiPo, compositi base
- Abilitazione firmata dal Maintenance Manager

Task autorizzati ML2: tutti i task elencati nelle Sezioni 3.1-3.5, inclusi smontaggio motori, sostituzione FCS, riparazione compositi minori, calibrazioni avioniche.

#### 5.2.3 Maintainer Livello 1 (ML1) — PIC abilitato

Il Pilota in Comando riceve addestramento aggiuntivo per:
- MX-PRE, MX-POST (obbligatorio per licenza PIC)
- MX-DAILY, MX-WEEKLY (attivita di routine non invasive)
- Riconoscimento anomalie e apertura NCR preliminare

Task autorizzati ML1: solo attivita di ispezione visiva e funzionale; nessuno smontaggio/sostituzione componente critico senza supervisione ML2.

#### 5.2.4 Training plan Y1

| Attivita formativa | Target | Timing | Fornitore | Costo stimato |
|---|---|---|---|---|
| Corso OEM JOUAV CW-30E (manutenzione e operazioni) | ML2 + Maintenance Manager | M+6-M+8 | JOUAV (remoto o on-site) | €3.000-8.000 |
| Corso LiPo safety e gestione batterie | ML2 + PIC | M+6 | Interno o provider safety | €500-1.000 |
| Corso compositi base (ispezione e riparazione) | ML2 | M+7-M+8 | Provider esterno (es. AeroConsult) | €1.000-3.000 |
| ENAC UAS Specific recurrency training | PIC | Annuale | Provider ENAC accreditato | €500-1.500/anno |
| Corso Part-IS cybersecurity (Reg. UE 2023/203) | ML2 + CISO | M+6 | Provider CISO | €500-1.000 |

### 5.3 OEM JOUAV — Service Contract

Il contratto di servizio OEM e un elemento critico della strategia di manutenzione Y1. Si raccomanda di negoziare con JOUAV (o distributore EU/IT) al momento della RFQ (M+6) un contratto che includa:

- **On-site training** (1 settimana, presso hangar Pentema o sede JOUAV IT): copertura manuale tecnico completo, procedure di manutenzione, identificazione ricambi
- **Remote support** (email/video call, SLA 48 h risposta): supporto diagnostica anomalie, interpretazione log FCS, aggiornamenti firmware
- **Annual visit** (1 missione/anno tecnico JOUAV in loco): supporto 100H o ANN inspection
- **Spare parts supply agreement**: impegno vendor a garantire disponibilita ricambi critici per 5 anni dal contratto, con lead time massimo concordato (target < 30 giorni per ricambi critici, < 14 giorni per consumabili)

**Caveat supply chain**: come indicato in RSK-GEO-003 (Allegato A.2 Risk Register), la supply chain JOUAV (vendor CN) e soggetta a rischi geopolitici. Il contratto OEM deve prevedere clausola di **stock minimo di emergenza** e identificazione di fornitori alternativi per i componenti non proprietari (es. motori brushless, batterie LiPo, antenne). Vedi Sezione 6 per dettaglio.

### 5.4 Subcontractor specialistici

| Subcontractor | Attivita | Frequenza prevista | Costo stimato/anno |
|---|---|---|---|
| NDT Service (ispezione compositi) | MX-STR-006 (100H + post-impatto) | 1-2 volte/anno | €1.500-3.000 |
| RF/spettrale Laboratory | MX-RF-011 (conformita spettrale AGCOM) | 1 volta/anno | €1.000-2.500 |
| Gimbal/Payload Specialist | MX-PLD-014 (sostituzione gimbal) + calibrazione boresight | On-condition + 2/anno | €1.000-3.000 |
| Battery Service (analisi approfondita cicli) | Analisi stato batterie (oltre capacity test interno) | 1 volta/anno | €500-1.000 |
| Drone Insurance Inspector | Ispezione airworthiness per rinnovo assicurativo | 1 volta/anno | €500-1.500 |

---

## Sezione 6 — Spare Parts Strategy {#sezione-6}

### 6.1 Razionale strategico

La strategia di ricambi risponde direttamente alla Critica 3 del Red Team Cap. 6 (rischio supply chain JOUAV CN) e al RSK-GEO-003 del Risk Register (Allegato A.2). L'obiettivo e garantire la continuita operativa per **12 mesi** anche in caso di blocco temporaneo delle forniture JOUAV (es. restrizioni export, sanzioni, problemi logistici COVID-like).

Lo stock spare target copre:
- **Livello 1 (in stock a Pentema)**: componenti critici ad alta frequenza di sostituzione e lunghi lead time
- **Livello 2 (in stock da fornitore EU/IT con lead time < 5 giorni)**: componenti standard non proprietari
- **Livello 3 (ordine su richiesta a JOUAV, lead time 4-12 settimane)**: componenti OEM proprietari a bassa frequenza di sostituzione

### 6.2 Critical Spare List — Livello 1 (stock a Pentema)

| Componente | Q.ta | Motivo criticita | Costo unit. stimato (€) | Totale (€) | Lead time JOUAV | Fonte prezzo |
|---|---|---|---|---|---|---|
| Motore brushless VTOL completo (set 4) | 4 unita | Alta usura + lead time CN lungo | 300-500 | 1.200-2.000 | 4-8 settimane | Benchmark mercato [vendor] |
| Elica (set 4+4 spare) | 8 set | Usura frequente, sostituzione rapida | 60-120 per set | 480-960 | 2-4 settimane | Benchmark [vendor] |
| Pack batteria LiPo propulsione (1 ricambio) | 1 pack | Failure batteria blocca operationi | 800-1.500 | 800-1.500 | 4-6 settimane | Benchmark [vendor] |
| Pack batteria LiPo payload (1 ricambio) | 1 pack | Come sopra | 400-800 | 400-800 | 4-6 settimane | Benchmark [vendor] |
| Modulo ESC (2 spare) | 2 unita | Failure ESC = fermo piattaforma | 150-300 | 300-600 | 4-8 settimane | Benchmark [vendor] |
| Modulo GPS/RTK (1 spare) | 1 unita | Failure GPS = no-go BVLOS | 400-800 | 400-800 | 6-10 settimane | Benchmark [vendor] |
| Antenna velivolo C2 (2 spare) | 2 unita | Danno fisico frequente | 30-100 | 60-200 | 1-2 settimane | Mercato generico |
| Kit riparazione compositi (epoxy, stucco, fibra) | 1 kit | Riparazioni minori immediate | 80-150 | 80-150 | Immediato (mercato IT) | Mercato IT |
| Connettori XT90 / AS150 (assortimento) | 10 pz | Consumabili elettrici | 5-10 | 50-100 | Immediato (mercato IT) | Mercato IT |
| **Subtotale Livello 1** | | | | **3.770-7.110** | | |

### 6.3 Spare Parts — Livello 2 (stock EU/IT, lead time < 5 giorni)

| Componente | Q.ta | Fornitore possibile EU | Costo unit. (€) | Totale (€) |
|---|---|---|---|---|
| Landing gear dampers | 2 set | Mercato RC/UAS EU (es. Innov8tive, ReadyMadeRC) | 80-200 | 160-400 |
| Modulo LTE (SIM + antenna) | 1 | Mercato IT (es. u-blox reseller) | 80-200 | 80-200 |
| Cavi power silicone (assortimento AWG 8-12) | 1 lot | Mercato elettronico IT | 50-100 | 50-100 |
| Filtri ND per Sony Alpha 7R IV | 3 filtri | Mercato fotografico IT/EU | 30-80 | 90-240 |
| Panno pulizia germanio IR (Workswell) | 5 pz | Workswell direct EU | 20-40 | 100-200 |
| **Subtotale Livello 2** | | | | **480-1.140** |

### 6.4 Ricambi Livello 3 (OEM on-demand) — No stock a Pentema

| Componente | Lead time stimato | Costo stimato (€) | Note |
|---|---|---|---|
| FCS / computer di volo JOUAV | 6-12 settimane | 1.500-3.000 | Proprietario; solo OEM |
| Fusoliera / ala di riserva | 8-16 settimane | 5.000-15.000 | Post-incidente grave |
| Gimbal completo | 8-12 settimane | 2.000-5.000 | Solo OEM o Workswell diretto |
| Modulo SATCOM Iridium (se installato) | 4-6 settimane | 1.000-2.500 | Mercato Iridium EU |
| Motore cruise | 4-8 settimane | 400-900 | OEM o brushless equivalente |

### 6.5 Budget spare parti Y1

| Livello | Stock iniziale (CapEx una tantum) | Consumo medio annuo (OpEx) | Totale Y1 |
|---|---|---|---|
| Livello 1 | €3.770-7.110 | €1.500-3.000 (consumabili ripristino) | €5.270-10.110 |
| Livello 2 | €480-1.140 | €500-1.000 | €980-2.140 |
| Livello 3 | 0 (no stock) | €2.000-5.000 (riparazioni on-condition) | €2.000-5.000 |
| **Totale spare Y1** | **€4.250-8.250** | **€4.000-9.000** | **€8.250-17.250** |

### 6.6 Backup vendor — Piano B Tekever AR3

Se la supply chain JOUAV risultasse bloccata oltre 60 giorni durante Y1, si attiva il Piano B:

1. **Sospensione operazioni** sul CW-30E (non operare con spare insufficienti)
2. **Attivazione RFQ urgente Tekever AR3** (PT, vendor EU, supply chain EU): Tekever Autonomous Systems, Loures (Portogallo); distribuzione EU documentata (utilizzato Maritime Surveillance EMSA)
3. **Adattamento PMO**: intervalli manutenzione Tekever AR3 da acquisire con manuale OEM Tekever (open source parziale per alcuni componenti Tekever)
4. **Stima tempi attivazione Piano B**: 3-6 mesi per acquisizione + training + prime operazioni

Impatto finanziario Piano B: sostituzione piattaforma €150-300k aggiuntivi (CapEx non pianificato). Da coprire con contingency Y1 (15% previsto in Cap. 8 §8.4.1) o rinegoziazione funding Cooding Prototypes.

---

## Sezione 7 — Records, Logbook e Compliance {#sezione-7}

### 7.1 Aircraft Logbook

Ogni velivolo JOUAV CW-30E ha un Aircraft Logbook (cartaceo + digitale) che registra:

**Per ogni volo**:
- Data, ora decollo/atterraggio, durata
- PIC identificato (nome + certificato ENAC)
- Sito operativo (coordinate GPS o nome sito)
- Ore di volo cumulate (aggiornate a ogni voce)
- Peso al decollo (MTOM reale con payload)
- Condizioni meteo (vento, temperatura, visibilita)
- Esito volo (normale / anomalia rilevata / incidente)
- Firma PIC

**Per ogni intervento di manutenzione**:
- Data intervento
- ID Task (es. MX-PROP-008)
- Descrizione attivita eseguita
- Componenti sostituiti (con part number e serial number se applicabile)
- Ora intervento su logbook componente (se life-tracked)
- Firma Maintainer esecutore (ML1 o ML2)
- Firma Maintenance Manager (per attivita 25H+)
- Maintenance Release (CRS — vedi §7.3)

### 7.2 Component Logbook

Per i seguenti componenti critici (life-tracked), viene mantenuto un Component Logbook separato:

| Componente | Info tracciate | Trigger sostituzione |
|---|---|---|
| Motori VTOL (x4, ciascuno) | Ore totali, cicli avviamento, eventuali anomalie | Life limit OEM (da confermare) |
| Motore cruise | Come sopra | Life limit OEM |
| Pack batteria propulsione (x2) | Cicli carica totali, capacity attuale (%) | < 80% capacita nominale |
| Pack batteria payload (x2) | Cicli carica totali, capacity attuale | < 80% capacita nominale |
| FCS / computer di volo | Versione firmware, data installazione, anomalie | 5 anni o 1.000 h o failure |
| Gimbal | Ore operazione, interventi meccanici, boresight error log | Failure motori o danno fisico |
| Modulo GPS/RTK | Versione firmware, ore operazione, accuracy log | Degradazione accuracy o failure |

### 7.3 Maintenance Release Certificate (CRS)

Dopo ogni intervento di manutenzione di livello 25H o superiore, il Maintenance Manager emette un **Certificate of Release to Service (CRS)** interno, equivalente funzionale al modello EASA Form 1 (adattato per UAS non certificato EASA Type Cert).

Il CRS include:
- Identificazione velivolo (numero di serie, marca, modello)
- Descrizione lavori eseguiti
- Riferimento a procedure/standard seguiti
- Dichiarazione di conformita ai requisiti del Piano di Manutenzione
- Firma e data Maintenance Manager
- Validita CRS (data rilascio + prossima scadenza manutenzione programmata)

Il CRS e archiviato nel fascicolo velivolo e disponibile per ispezione ENAC.

### 7.4 Non-Conformity Report (NCR)

Ogni anomalia, malfunzionamento o non-conformita rispetto al Piano di Manutenzione viene documentata in un NCR, che include:
- Descrizione anomalia
- Sistemi/componenti coinvolti
- Impatto sulla sicurezza operativa (safety impact assessment)
- Root Cause Analysis (RCA) semplificata
- Azione correttiva implementata
- Verifica efficacia (follow-up entro 30 giorni)
- Chiusura formale firmata dal Maintenance Manager

Le NCR sono numerate progressivamente (NCR-YYYY-NNN) e archiviate per 5 anni.

### 7.5 Sistema di tracciabilita digitale

**Strumento target Y1**: sistema di manutenzione digitale (possibile utilizzo di piattaforme open-source come **Flightlog.io**, **AirManager** o simile, oppure sistema custom Excel/Sheets con controllo versione) con backup locale cifrato + cloud (AgID PSN o equivalente per dati PA se il sistema e usato come evidenza per contratti PA).

Requisiti minimi sistema digitale:
- Accesso multi-utente con ruoli (PIC = lettura/inserimento volo; ML2 = inserimento manutenzione; Manager = approvazione + report)
- Export in formato standard (CSV, PDF) per audit ENAC
- Backup automatico giornaliero
- Retention dei record: minimo 5 anni dall'ultimo volo o dalla dismissione del velivolo (ENAC Reg. APR Ed. 3)

### 7.6 Audit trail Part-IS (Reg. UE 2023/203)

Come richiesto da Part-IS EASA (RSK-REG-019, Cap. 5 §5.16.4), il sistema di manutenzione deve mantenere:
- Log di accesso al sistema digitale (chi ha inserito/modificato record)
- Log di aggiornamenti firmware FCS (versione, data, autore)
- Log di aggiornamenti cybersecurity patch (vedi MX-AVI-006)
- Audit annuale CISO della sicurezza del sistema di tracciabilita

### 7.7 Notifica incidenti ENAC/ANSV

In caso di incidente o grave inconveniente (ai sensi Reg. UE 2019/947 art. 15 + D.Lgs. 213/2009 per ANSV), la procedura e:
1. **Fermo immediato** velivolo (no operazioni fino a clearance)
2. **Notifica ENAC** entro 72 ore (modulo segnalazione online ENAC)
3. **Notifica ANSV** se incidente grave (art. 5 D.Lgs. 213/2009)
4. **Preservazione evidence** (FCS log, video GCS, fotografie)
5. **Apertura dossier incidente** interno con RCA
6. **Ripristino operazioni** solo dopo autorizzazione Maintenance Manager + eventuale clearance ENAC

---

## Sezione 8 — Costi LCC (Life Cycle Cost) Y1-Y5 {#sezione-8}

### 8.1 Premessa metodologica

I costi LCC sono strutturati in:
- **CapEx manutenzione** (one-time): attrezzature manutenzione (GSE), stock spare iniziale, setup facility, formazione iniziale
- **OpEx manutenzione ricorrente** (annuale): personale manutenzione, consumabili, spare consumati, contratti SLA OEM, subcontractor

I costi sono **stime di benchmark** (confidence: medium), non quotazioni fornitore. Fonte: benchmark operatori UAS commerciali EU, datasheet vendor, costi di mercato IT per manodopera tecnica aerospaziale. I valori definitivi richiederanno conferma al M+6 con RFQ vendor + offerte subcontractor.

**Allineamento Cap. 8 §8.5.1.A**: il baseline Cap. 8 dichiara "Manutenzione piattaforma 5-8% CapEx asset = €30-60k/anno". Il presente PMO fornisce una scomposizione analitica che conferma e raffina tale range.

### 8.2 CapEx manutenzione (investimento una tantum Y1)

| Categoria | Range (€) | Note |
|---|---|---|
| Attrezzature manutenzione (GSE) | 15.000-30.000 | Chiavi torsiometriche, multimetri, oscilloscopio portatile, NanoVNA, cell checker LiPo, laptop dedicated, toolbox, termocamera base |
| Stock spare Livello 1 (§6.2) | 4.250-8.250 | Vedere §6.5 |
| Sistema tracciabilita digitale (setup + licenze Y1) | 1.000-5.000 | Open source + personalizzazione o SaaS |
| Formazione iniziale personale (§5.2.4) | 5.500-13.500 | Corso OEM + LiPo safety + compositi + Part-IS |
| Adeguamento hangar Pentema — area manutenzione | 5.000-20.000 | Illuminazione tecnica, banco lavoro, armadietti sicurezza LiPo (ATEX), scaffalature ricambi |
| **Totale CapEx manutenzione Y1** | **30.750-76.750** | Allineato con Computo Metrico §A9 |

### 8.3 OpEx manutenzione ricorrente Y1 (80 missioni, ~200 h volo)

| Categoria | Range (€/anno) | Note |
|---|---|---|
| Personale manutenzione (0.5 FTE ML2 + 0.3 FTE Manager) | 25.000-45.000 | 0.5 FTE ML2 = €20-30k; 0.3 FTE Manager = €10-15k |
| Contratto OEM JOUAV (remote + annual visit) | 8.000-15.000 | Stima benchmark; da quotare al RFQ M+6 |
| Subcontractor specialistici (NDT + RF + payload) | 3.500-8.500 | Vedere §5.4 |
| Consumabili manutenzione (pulizia, lubrificanti, sigillanti, kit riparazione) | 1.000-3.000 | Annuale |
| Spare consumati Y1 (§6.5 Livello 1-2 consumo annuale) | 4.000-9.000 | Vedere §6.5 |
| Manutenzione correttiva non pianificata (stima 10-15% missioni) | 3.000-8.000 | 8-12 eventi x €300-700 media |
| Assicurazione manutenzione (RC professionale + prodotto) | 2.000-5.000 | Quota manutenzione su polizza operatore |
| Audit compliance + documentazione ENAC | 1.000-3.000 | CRS, NCR, notifiche, aggiornamenti PMO |
| **Totale OpEx manutenzione Y1** | **47.500-96.500** | Centro: ~€72k |

**Raffronto Cap. 8 §8.5.1.A**: il range €47.500-96.500 e compatibile con il benchmark Cap. 8 (€30-60k mantenzione pura + personale aggiuntivo manutenzione non incluso in quel baseline). La differenza e principalmente imputabile alla voce "personale manutenzione" (€25-45k) che in Cap. 8 §8.5.1.A e inclusa parzialmente nella voce "Personnel" aggregata. Non c'e incongruenza; il PMO fornisce una lettura analitica.

### 8.4 Costi LCC Y1-Y5

| Anno | Scenario | CapEx manutenzione | OpEx manutenzione | Totale anno | Note |
|---|---|---|---|---|---|
| **Y1** | Baseline (80 missioni, 1 piattaforma) | €30.750-76.750 | €47.500-96.500 | **€78.250-173.250** | Include investimento iniziale |
| **Y1** | Ottimistico (50 missioni, lean) | €25.000-50.000 | €35.000-65.000 | **€60.000-115.000** | Scenario minimo |
| **Y2** | Scale (2 piattaforme + GS mobile) | €20.000-40.000 | €80.000-150.000 | **€100.000-190.000** | +1 piattaforma, +1 crew |
| **Y3** | Multi-regione (flotta 3-5) | €30.000-60.000 | €150.000-280.000 | **€180.000-340.000** | Flotta 3-5, 2 basi operative |
| **Y4** | Maturita (flotta stabile + HALE prep) | €10.000-20.000 | €200.000-350.000 | **€210.000-370.000** | Overhaul piattaforme Y1 |
| **Y5** | HALE + VTOL (flotta 5+ + subscale HALE) | €15.000-30.000 | €250.000-400.000 | **€265.000-430.000** | Include manutenzione HALE subscale |

**Nota Y2-Y3**: il +30% OpEx/anno per manutenzione (dichiarato in Cap. 8 §8.5.2) e coerente con la crescita di flotta. Il driver principale e il personale (scala quasi linearmente con numero piattaforme) piu che i contratti OEM (economie di scala parziali).

**Nota Y4**: l'overhaul piattaforme Y1 (motori, batterie) genera un CapEx una tantum di €15-40k per piattaforma secondo i life limit (200-400 h per motori, 300-500 cicli per batterie), che cade presumibilmente in Y2-Y3 per i componenti piu sollecitati.

### 8.5 Sensitvita LCC

I tre driver di incertezza principale:

1. **Lead time ricambi JOUAV**: se lead time > 8 settimane (rischio supply chain CN), il costo di scorte Livello 1 aumenta del 50-100% (maggior volume spare richiesto)
2. **MTBF reale motori VTOL**: se MTBF reale < 100 h (vs 200-400 h OEM dichiarato), le sostituzioni motori aumentano OpEx di €8.000-20.000/anno (4 motori x €400-500 x 2-4 sostituzioni/anno)
3. **Retribuzione maintainer IT**: il range ML2 a €40-60/h e congruente con il mercato IT 2025 per tecnici aerospaziali junior (fonte: benchmark Almalaurea 2024 + Metalcontract CCNL aeronautica). Un aumento del 15% impatta OpEx di €3.750-6.750/anno

---

## Sezione 9 — Sicurezza e Ambiente (HSE) {#sezione-9}

### 9.1 Gestione batterie LiPo — Procedure ATEX

In riferimento a RSK-REG-022 (Cap. 5 §5.16.7) e D.Lgs. 81/2008 Titolo XI:

**Classificazione ATEX hangar Pentema**: la zona di ricarica e stoccaggio batterie LiPo deve essere classificata secondo ATEX Direttiva 2014/34/UE. La classificazione (Zona 0/1/2) dipende dalla concentrazione di vapori di solventi organici e gas (H2 in caso di thermal runaway LiPo) e deve essere effettuata da tecnico abilitato (Responsabile del Servizio di Prevenzione e Protezione — RSPP). Target: classificazione Zona 2 con adeguate misure di mitigazione.

**Procedure operative LiPo**:
- Ricarica batterie solo in area designata con ventilazione meccanica attiva (ricambi aria 6x/h minimi) e rilevatore CO/fumo + sistema allarme
- Utilizzo di armadietti ignifughi certificati per stoccaggio LiPo (es. CEMO Lithium Safety Cabinet o equivalente)
- Mai caricare LiPo senza supervisione; mai lasciare LiPo in carica durante chiusura hangar notturna
- In caso di thermal runaway: non avvicinarsi, attivare sistema di soppressione (CO2 o sabbia secca), evacuare area, chiamare VVF
- Batterie LiPo danneggiate (rigonfiamento, perforazione, deformazione): quarantena immediata in contenitore sicurezza metallico + smaltimento entro 5 giorni lavorativi

**Segnaletica obbligatoria**: cartelli "Pericolo batterie LiPo — No fiamme libere — Area ventilata" in italiano + pittogrammi ISO 7010.

### 9.2 Smaltimento materiali — RoHS, REACH, RAEE

In riferimento a RSK-REG-023 (Cap. 5 §5.16.8):

| Materiale | Classificazione rifiuto | Filiera smaltimento | Riferimento normativo |
|---|---|---|---|
| Batterie LiPo esaurite | Rifiuto speciale pericoloso (CER 16 06 05) | Raccolta RAEE + Centro di raccolta pile autorizzato | D.Lgs. 49/2014 |
| Compositi fibra carbonio/vetro | Rifiuto speciale non pericoloso (CER 07 02 13) | Smaltitore autorizzato (non incenerimento standard) | D.Lgs. 152/2006 |
| Schede elettroniche dismesse | Rifiuto RAEE (CER 16 02 14) | Raccolta RAEE autorizzata | D.Lgs. 49/2014 |
| Solventi e pulitori chimici | Rifiuto speciale pericoloso (CER 14 06 03) | Smaltitore autorizzato | D.Lgs. 152/2006 |
| Imballaggi spare parts | Rifiuto urbano assimilato | Raccolta differenziata Comune Torriglia | Regolamento comunale |

**Registro rifiuti**: obbligo di tenuta del Registro di Carico e Scarico rifiuti speciali (D.Lgs. 152/2006 art. 190) per le categorie pericolose. Target: attivazione registro digitale (SISTRI sostituito da RENTRI dal 2023).

**Sostanze REACH**: verifica preliminare dei componenti acquistati per assenza di SVHC (Substances of Very High Concern) nella Candidate List ECHA. Responsabilita: Maintenance Manager verifica le Schede di Dati di Sicurezza (SDS) dei fornitori.

### 9.3 Gestione avifauna — comportamento in area maintenance

Il sito di Pentema e in area appenninica con presenza di rapaci (poiane, falchi, nibbi, possibilmente aquile su crinali vicini). Misure per area manutenzione esterna (parking + prep area):

- **Copertura velivolo** con telone quando in sosta esterna > 30 minuti (prevenzione utilizzo come posatoi da rapaci, potenziale danni a superfici ottiche)
- **Ispezione anti-FOD** prima di ogni decollo (penne, rami, insetti all'interno del velivolo o sulla pista di decollo)
- **Monitoraggio avifauna** pre-volo (scansione visiva 360° per 2 minuti prima di decollo VTOL): se rapace a < 500 m in quota operativa, ritardare decollo
- **Deterrente acustico** (se necessario, solo durante preparazione a terra, non in volo): utilizzare solo sistemi approvati localmente + Ente Parco se area protetta (verificare con Parco Regionale Aveto)
- In caso di bird strike in volo: atterraggio di emergenza immediato + ispezione MX-EXTR completa prima di qualsiasi riutilizzo

### 9.4 Gestione rischi HSE personale

| Rischio | Misura preventiva | DPI richiesto |
|---|---|---|
| Taglio da eliche rotanti | Lock elettrico motori durante manutenzione; protezioni TA (Turn to Arrow) | Guanti anti-taglio |
| Inalazione polveri compositi | Lavoro in area ventilata; uso mascherina FFP2 per tagli/forature compositi | Mascherina FFP2 |
| Esposizione UV (lavoro outdoor estivo) | Limitar ore nelle fasce 11-15; crema solare SPF 50+ | Cappello + crema |
| Caduta in area alpina (operazioni outdoor) | Lavoro in coppia; scarpe antisdrucciolevoli; nessuna manutenzione in solitaria su terreno instabile | Scarpe antinfortunistiche |
| Shock elettrico (batterie alta corrente) | Guanti isolati; disconnessione batteria prima di qualsiasi intervento su elettronica | Guanti isolanti 1000V |
| Rischio incendio LiPo | Procedure §9.1 | Estintore CO2 in area |

---

## Sezione 10 — Gap residui pre-operations Y1 {#sezione-10}

La presente sezione elenca i gap critici da chiudere prima che le operazioni Y1 possano iniziare. Questi gap sono anche condizioni di ingresso (entry criteria) per il gate G2 (M+6) e G3 (M+10).

### 10.1 Gap G1 — Manuale tecnico OEM JOUAV CW-30E

| Attributo | Contenuto |
|---|---|
| **Gap ID** | GAP-MX-001 |
| **Descrizione** | Il manuale tecnico OEM JOUAV CW-30E completo (procedures manutenzione, life limits componenti, torque values, wiring diagrams) non e disponibile pubblicamente. E condizione necessaria per finalizzare il PMO v2.0. |
| **Impatto** | Senza manuale OEM: intervalli di ispezione (25H, 100H) sono stime di benchmark non validate; life limit motori/batterie non certificati; la firma ML2 su CRS non ha fondamento documentale OEM. |
| **Azione richiesta** | Inclusione del manuale tecnico completo come deliverable obbligatorio nel contratto RFQ JOUAV (M+6). Clausola: "Vendor deve fornire documentazione tecnica di manutenzione in lingua italiana o inglese come condizione di accettazione piattaforma." |
| **Owner** | Maintenance Manager + Procurement |
| **Target** | M+6 (RFQ + contratto) → M+8 (ricezione piattaforma + manuale) |
| **Gate** | Condizione entry G2 (M+6): RFQ emessa; condizione exit G2: manuale ricevuto e revisione iniziale completata |

### 10.2 Gap G2 — Assunzione e formazione Maintainer ML2

| Attributo | Contenuto |
|---|---|
| **Gap ID** | GAP-MX-002 |
| **Descrizione** | A M+3 (data presente PMO), non e ancora stata assunta la figura di Maintainer ML2 dedicato. La posizione e critica: senza ML2, le ispezioni 25H e 100H non possono essere condotte internamente. |
| **Impatto** | Senza ML2: attivita manutenzione dipendono interamente da OEM JOUAV (costoso + lento) o subcontractor non qualificato. Rischio: impossibilita di tenere la cadenza di 1-2 missioni/settimana per mancanza di clearance manutenzione. |
| **Azione richiesta** | Avvio recruitment ML2 entro M+4; contratto entro M+6; formazione OEM JOUAV completata entro M+8; prima ispezione 25H in affiancamento OEM entro M+9. |
| **Owner** | Maintenance Manager + HR Firmamento |
| **Target** | M+4: job posting; M+6: contratto; M+9: fully qualified |
| **Gate** | Condizione exit G2 (M+6): contratto ML2 firmato; condizione exit G3 (M+10): ML2 qualificato e autonomo su 25H |

### 10.3 Gap G3 — Contratto SLA OEM e spare parts pipeline

| Attributo | Contenuto |
|---|---|
| **Gap ID** | GAP-MX-003 |
| **Descrizione** | Il contratto SLA con JOUAV (o distributore EU) per supporto tecnico remoto, visite annuali e spare parts supply e da negoziare. Senza questo contratto, il supply chain risk RSK-GEO-003 non e mitigato. |
| **Impatto** | Senza SLA: lead time ricambi non garantito; nessun impegno OEM su disponibilita parti 5 anni; nessuna priorita su supporto tecnico. In caso di failure componente critico (FCS, motore) l'aeromobile puo restare fermo 8-16 settimane. |
| **Azione richiesta** | Negoziazione SLA contestuale alla RFQ piattaforma (M+6). Clausole minime: lead time ricambi < 30 gg (critici) / < 14 gg (consumabili); supporto remoto SLA 48h risposta; impegno disponibilita ricambi 5 anni; 1 visita on-site/anno inclusa. |
| **Owner** | Maintenance Manager + Legal |
| **Target** | M+6: contratto firmato contestualmente alla PO piattaforma |
| **Gate** | Condizione exit G2: SLA firmato o equivalente commitment contrattuale |

### 10.4 Gap G4 — Attrezzature manutenzione e GSE

| Attributo | Contenuto |
|---|---|
| **Gap ID** | GAP-MX-004 |
| **Descrizione** | Il GSE (Ground Support Equipment) per manutenzione non e stato ancora acquisito. Senza gli strumenti adeguati (chiavi torsiometriche calibrate, multimetro precision, NanoVNA, oscilloscopio, battery analyzer, kit riparazione compositi), le ispezioni non possono essere condotte a standard. |
| **Azione richiesta** | Redazione lista GSE definitiva post-ricezione manuale OEM (M+8); acquisizione GSE entro M+9; calibrazione strumenti prima delle prime ispezioni operative. |
| **Owner** | Maintenance Manager |
| **Target** | M+8: lista definitiva; M+9: GSE acquisito e calibrato |
| **Budget**: €15.000-30.000 (incluso in CapEx manutenzione §8.2) |

### 10.5 Gap G5 — Adeguamento facility hangar Pentema

| Attributo | Contenuto |
|---|---|
| **Gap ID** | GAP-MX-005 |
| **Descrizione** | L'hangar Pentema (80-150 m² previsto) deve essere adeguato per le attivita di manutenzione: area separata manutenzione (min 20 m²), illuminazione tecnica, bench work, armadietti ATEX per LiPo, scaffalature ricambi, ventilazione meccanica area ricarica. |
| **Azione richiesta** | Progettazione layout hangar (M+3-M+4, coordinato con A.9 Computo Metrico); lavori adeguamento (M+4-M+8); collaudo area ATEX con RSPP e VVF (M+8-M+9). |
| **Owner** | Ingegnere Ops + RSPP |
| **Target** | M+9: hangar maintenance-ready |
| **Budget**: €5.000-20.000 (incluso in CapEx manutenzione §8.2 e in A.9 Computo Metrico) |
| **Gate**: Condizione exit G2 (M+6): approvazione progetto layout + impegno lavori |

### 10.6 Riepilogo gap e timeline

| Gap ID | Descrizione sintetica | Owner | Target | Gate |
|---|---|---|---|---|
| GAP-MX-001 | Manuale OEM JOUAV CW-30E | Maint. Manager + Procurement | M+8 | G2 entry/exit |
| GAP-MX-002 | Hire + train ML2 Maintainer | HR + Maint. Manager | M+9 | G2 exit / G3 exit |
| GAP-MX-003 | Contratto SLA OEM + spare pipeline | Maint. Manager + Legal | M+6 | G2 exit |
| GAP-MX-004 | GSE acquisition + calibration | Maint. Manager | M+9 | G3 entry |
| GAP-MX-005 | Hangar facility adeguamento | Ingegnere Ops + RSPP | M+9 | G2 exit / G3 entry |

---

## Sezione 11 — Linkage cross-volume {#sezione-11}

### 11.1 Riferimenti interni al Volume 1 (Capitoli Studio)

| Capitolo | Sezione | Contenuto collegato | Tipo relazione |
|---|---|---|---|
| Cap. 5 | §5.16.7 (RSK-REG-022) | ATEX batterie LiPo — classificazione zona hangar | Input normativo → §9.1 PMO |
| Cap. 5 | §5.16.8 (RSK-REG-023) | RoHS componenti — verifica SDS | Input normativo → §9.2 PMO |
| Cap. 5 | §5.16.14 (RSK-REG-029) | Direttiva Macchine — GCS e carrelli UAS come "macchine" | Input normativo → §1.2.6 PMO |
| Cap. 5 | §5.16.4 (RSK-REG-019) | Part-IS EASA — cybersecurity manutenzione | Input normativo → §7.6 PMO |
| Cap. 6 | §6.1 | Architettura tecnica piattaforma JOUAV CW-30E | Input tecnico → Sezioni 3.1-3.5 |
| Cap. 6 | §6.4 | FMECA + FTA — componenti critici per manutenzione | Input prioritizzazione → MX task critici |
| Cap. 8 | §8.4.1 | CapEx piattaforma + ricambi | Input costi → §8.2 PMO |
| Cap. 8 | §8.5.1.A | OpEx manutenzione baseline 5-8% CapEx | Allineamento → §8.3 PMO |
| Cap. 8 | §8.5.2 | Evoluzione OpEx Y3-Y5 (+30%/anno manutenzione) | Coerenza → §8.4 PMO |
| Cap. 9 | §9.x | Cronoprogramma gate G2 (M+6) e G3 (M+10) | Trigger → gap §10 PMO |

### 11.2 Riferimenti interni al Volume 2 (Allegati)

| Allegato | Titolo | Contenuto collegato | Tipo relazione |
|---|---|---|---|
| A.2 | Risk Register | RSK-GEO-003 supply chain JOUAV | Rischio driver → §6.6 backup vendor |
| A.4 | ICD Interfaces | Interfacce meccaniche ed elettriche payload-airframe | Input integration → §3.4 (MX-PLD) |
| A.9 | Computo Metrico Estimativo | Costi facility hangar, GSE | Costi condivisi → §8.2 + §10.5 |
| A.11 | PSC SORA Safety Case | OSO #03 (maintained by competent entity) | Evidence → PMO come prova OSO #03 |
| A.11 | PSC SORA Safety Case | OSO #07 (pre-flight inspection) | Evidence → MX-PRE come prova OSO #07 |
| A.12 | VIA Preliminare | Smaltimento materiali + impatto ambientale | Coerenza → §9.2 PMO |

### 11.3 Dipendenze verso documenti futuri

| Documento futuro | Versione target | Dipendenza da PMO |
|---|---|---|
| PMO v2.0 | M+10 | PMO v1.5 (questo documento) come baseline; aggiornamento post-ricezione manuale OEM e prime operazioni reali |
| Operations Manual (OM) | M+8 | PMO v1.5 alimenta OM cap. 4 (pre-flight) e cap. 5 (anomaly handling) |
| SORA application definitiva | M+10 | PMO v2.0 come allegato obbligatorio (OSO #03 evidence) |
| Dichiarazione ENAC Specific | M+10 | PMO v2.0 come prova di sistema manutenzione documentato |
| Financial Model update | M+6 | §8.3-8.4 PMO affinano OpEx manutenzione per modello LCC |

---

## Appendice A — Lista abbreviazioni

| Abbreviazione | Significato |
|---|---|
| ANN | Annual (ispezione annuale) |
| BMS | Battery Management System |
| CapEx | Capital Expenditure |
| CM | Corrective Maintenance |
| CRS | Certificate of Release to Service |
| DAILY | Daily (ispezione giornaliera) |
| DMM | Digital Multimeter |
| DVR | Documento di Valutazione dei Rischi |
| ESC | Electronic Speed Controller |
| FCS | Flight Control System |
| FOD | Foreign Object Debris/Damage |
| GCS | Ground Control Station |
| GNC | Guidance, Navigation, Control |
| GSE | Ground Support Equipment |
| HSE | Health, Safety, Environment |
| ICD | Interface Control Document |
| LCC | Life Cycle Cost |
| LiPo | Lithium Polymer battery |
| ML1 | Maintainer Level 1 |
| ML2 | Maintainer Level 2 |
| MONTHLY | Monthly (ispezione mensile) |
| MRO | Maintenance, Repair, Overhaul |
| MTOM | Maximum Take-Off Mass |
| MX | Maintenance (prefisso task) |
| NCR | Non-Conformity Report |
| NDT | Non-Destructive Testing |
| NUC | Non-Uniformity Correction (IR camera) |
| OEM | Original Equipment Manufacturer |
| OpEx | Operational Expenditure |
| OSO | Operational Safety Objective (SORA) |
| OVH | Overhaul |
| PIC | Pilota in Comando |
| PM | Preventive Maintenance |
| PMO | Piano di Manutenzione Operativo |
| POST | Post-flight (ispezione post-volo) |
| PRE | Pre-flight (ispezione pre-volo) |
| RCA | Root Cause Analysis |
| RTB | Return to Base |
| RSPP | Responsabile Servizio Prevenzione e Protezione |
| SATCOM | Satellite Communication |
| SDA | Safety Data Sheet |
| SLA | Service Level Agreement |
| SORA | Specific Operations Risk Assessment |
| SVHC | Substances of Very High Concern |
| UAS | Unmanned Aircraft System |
| VNA | Vector Network Analyzer |
| VSWR | Voltage Standing Wave Ratio |
| WEEKLY | Weekly (ispezione settimanale) |
| 25H | 25-hour inspection |
| 100H | 100-hour inspection |

---

## Appendice B — Falsifying observations del PMO

In linea con il principio di rigore epistemico del progetto HALE (CLAUDE.md), si dichiarano le osservazioni falsificanti del presente PMO:

1. **Se MTBF reale motori VTOL < 100 h** (vs 200-400 h vendor dichiarato), il piano PM 25H e insufficiente: attivare ispezione MX-PROP-007-008 ogni 15H e rivedere OpEx al rialzo (+€8-20k/anno per sostituzioni anticipate). Trigger: primo fallimento motore prima delle 100H operative.

2. **Se capacity batterie LiPo scende sotto 80% nominale prima di 200 cicli**, la frequenza MX-PROP-014 (capacity test) va aumentata a ogni 25 cicli; budget sostituzione batterie Y1 aumenta di €1.600-3.000. Trigger: primo capacity test < 80%.

3. **Se VVF Torriglia classifica hangar come ATEX Zona 1** (invece di Zona 2), i costi di adeguamento aumentano di €20-40k (vedi A.9 Computo Metrico). Trigger: classificazione ATEX formale entro M+6.

4. **Se il manuale OEM JOUAV CW-30E stabilisce intervalli diversi** (piu frequenti) rispetto alle stime di benchmark qui utilizzate, il carico manutentivo annuo puo aumentare del 20-50% e il PMO v2.0 deve ricalcolare tutti i costi LCC. Trigger: ricezione manuale al M+8.

5. **Se supply chain JOUAV bloccata per > 60 giorni**, attivare Piano B Tekever AR3 (§6.6) e sospendere operazioni CW-30E. Trigger: ritardo fornitura ricambio critico Livello 1 > 60 giorni.

---

## Appendice C — Versioning e history

| Versione | Data | Autore | Modifiche principali |
|---|---|---|---|
| v1.0 | M+3 | Firmamento Technologies | Piano preliminare (207 righe, categorie base) |
| v1.5 | 2026-05-17 | Firmamento Technologies (vtol-uas-specialist + aerospace-systems-engineer) | Piano operativo completo: 5 sistemi, task table completa, LCC Y1-Y5, spare parts strategy, HSE, gap analysis, cross-volume linkage |
| v2.0 | M+10 (target) | Firmamento Technologies + OEM JOUAV | Aggiornamento post-ricezione manuale OEM + prime operazioni reali + SORA application allegato definitivo |

---

> **Confidence aggregato documento**: **MEDIUM**
> Motivazione: (1) intervalli manutenzione basati su benchmark mercato UAS, non su manuale OEM JOUAV CW-30E (non disponibile pubblicamente); (2) costi LCC basati su stime di benchmark IT 2025, non su quotazioni ferme; (3) vita utile componenti da datasheet vendor non validati da operatori EU; (4) classificazione ATEX hangar non ancora effettuata da tecnico abilitato. Tutti e quattro i gap saranno chiusi tra M+6 e M+9 (vedi Sezione 10). Il PMO v2.0 (M+10) avra confidence HIGH pre-gate G3.
>
> Documento classificazione: **Interno — Volume 2 Allegato A.10**
> Non per distribuzione esterna senza approvazione Firmamento Technologies.
