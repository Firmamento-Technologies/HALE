# Allegato A.10. Piano di Manutenzione Preliminare

> Volume 2, Allegato A.10
> Conformità D.Lgs. 36/2023 art. 41 + Allegato I.7 (elaborato PFTE obbligatorio)
> Riferimento standard: **AS/EN 9110** (Quality Management for Aviation Maintenance Organizations)

## A.10.0 Premessa metodologica

Il Piano di Manutenzione preliminare definisce le procedure di manutenzione programmata e correttiva per il sistema HALE/VTOL Firmamento, in coerenza con:
- **Reg. UE 2019/947** art. 14 (manutenzione SAPR)
- **ENAC Reg. APR Ed. 3** art. 19 (Manutenzione del SAPR)
- **EN 9110:2018** (Maintenance Organizations)
- **AS9100D** (Quality Management Aerospace)

Confidence aggregato: **medium-low** (preliminare; Piano Detailed Maintenance al M+6-12).

## A.10.1 Categorie di manutenzione

| Categoria | Codice | Descrizione | Frequenza tipica |
|---|---|---|---|
| **Pre-flight check** | MNT-PRE | Verifica visiva e funzionale prima di ogni volo | Ogni missione |
| **Post-flight check** | MNT-POST | Ispezione e download log dopo volo | Ogni missione |
| **Daily / Weekly** | MNT-DAILY | Procedure giornaliere e settimanali | Quotidiana operativa |
| **50 hours** | MNT-50H | Major check ogni 50 ore di volo | ~6-12 mesi |
| **200 hours** | MNT-200H | Overhaul intermedio | ~2-4 anni |
| **Annual** | MNT-ANN | Ispezione annuale completa | 12 mesi |
| **Calendar-based** | MNT-CAL | Sostituzione componenti per scadenza | Variabile (es. batterie 24 mesi) |
| **Corrective** | MNT-COR | Riparazione su anomalia | On-condition |

## A.10.2 Piano di Manutenzione Percorso 6A. VTOL

### MNT-PRE (Pre-flight). Ogni missione (~15 min)

- Visual inspection: ala, fusoliera, motori, eliche (no cracks, no dirt, no FOD)
- Connectors check: payload, antenne, batterie
- Battery voltage check (>= 95% nominal)
- GPS lock + IMU calibration
- C2 link test (range + signal strength)
- Payload check (sensori operativi, settings corretti)
- Ground station check (link + computing)
- Weather brief + go/no-go decision
- NOTAM check + airspace clearance
- Pilot crew brief

### MNT-POST (Post-flight). Ogni missione (~20 min)

- Visual inspection post-volo (impatti, danni, contamination)
- Battery temperature check + safe storage
- Log download dal velivolo + GS
- Mission report compilation
- Anomalie incontrate documentate (per follow-up MNT-COR)
- Cleaning superfici critiche (sensori, ottiche)
- Storage in hangar

### MNT-DAILY/WEEKLY (operativa quotidiana)

L'attività ricorrente comprende il battery charging cycle management (LiPo 50-90% optimal storage), il software update FCS e GS su patch release vendor, il cybersecurity patch (Reg. UE 2023/203 Part-IS) e la calibration sensori IR quando utilizzati nella settimana.

### MNT-50H. Major check ogni 50 ore (4-6 settimane in MVP intensivo)

- Smontaggio e ispezione motori VTOL (4 unità + cruise)
- Sostituzione bearings se usurati
- Ispezione e sostituzione eliche se danneggiate
- Ispezione e cleaning sistema raffreddamento motori
- Verifica fissaggi strutturali (torque check)
- Calibrazione IMU + Air Data
- Aggiornamento firmware avionica
- Test funzionale completo end-to-end
- Documentazione manutenzione (logbook)

**Costo stimato MNT-50H**: 4-8 ore tecnico aerospace + €500-1.500 ricambi consumed (ipotesi).

### MNT-200H. Overhaul intermedio (~2-4 anni)

- Smontaggio completo e ispezione strutture primarie (longheroni, ala, fusoliera)
- NDT (Non-Destructive Testing) compositi (ultrasuoni o termografia)
- Sostituzione motori VTOL (lifetime tipico 200-500 h)
- Sostituzione batterie LiPo (lifetime ~300-500 cycle)
- Recalibration completa avionica + sensori
- Test funzionale prolungato (8h continuous)
- Riapprovazione operativa interna

**Costo stimato MNT-200H**: €5.000-15.000 in funzione di parti sostitute.

### MNT-ANN. Ispezione annuale

L'audit annuale copre logbook e storia operativa, compliance check (SORA, dichiarazioni ENAC, assicurazione), re-training piloti UAS (mandatory ENAC + EASA), audit Part-IS Information Security (Reg. UE 2023/203) e renewal certificazioni operatore.

### MNT-CAL. Sostituzione componenti scadenza

| Componente | Scadenza | Costo sostituzione |
|---|---|---|
| Batterie LiPo VTOL | 24-36 mesi o 300-500 cycle | €2.000-4.000 |
| Sensore IMU | 5 anni o 1000 h | €1.500-3.000 |
| Antenna SATCOM (sealing) | 5 anni | €500-1.000 |
| Filtri aria motori | 6 mesi | €100-200 |
| Cavi power MIL-spec | 5-10 anni | €500-1.500 |

## A.10.3 Piano di Manutenzione Percorso 6B. HALE (preliminare Phase B+)

### MNT-PRE-HALE (Pre-launch ascesa stratosferica)

- Ispezione struttura completa pre-ascesa (5-7 giorni)
- Test propulsione + storage completo
- Test pannelli solari (cleaning + check connections)
- Test avionica + ridondanza (FCS triplex + IMU triplex)
- Test C2 link (RF + SATCOM)
- Mission planning + sortie envelope + meteo brief 7 giorni
- ENAV coordination + NOTAM
- Crew brief multi-disciplinare

### MNT-POST-HALE (Post-discesa)

- Ispezione struttura post-discesa (gust + ozono damage)
- Cleaning pannelli solari (degrado UV)
- Health check batterie LiS (cycle count + degradazione)
- Log download completo + analisi anomalie
- Sostituzione componenti consumed

### MNT-WEEKLY-HALE (durante operazioni perennial / seasonal)

La gestione settimanale prevede telemetria health monitoring continuativa, anomalie detection con alert automatici e pianificazione di discese opportunistic per maintenance (ciclo indicativo di un mese).

### MNT-CAL-HALE (Stratosphere-specific)

| Componente | Scadenza | Note |
|---|---|---|
| Pannelli solari multi-junction GaAs | 3-5 anni (degradazione 1%/anno) | Sostituzione completa hangar |
| Batterie LiS pack | 200-500 cycle | Sostituzione pack completo |
| Propellers (stratospheric, low-Re) | 500-1000 h | Sostituzione |
| Antenne service link 5G NTN | 5-7 anni | Sostituzione preventiva |

## A.10.4 Organizzazione di Manutenzione (MNT-ORG)

Per il MVP Y1 (Percorso 6A) l'organizzazione resta in-house con 3 FTE (pilota, ingegnere, tecnico), supporto vendor per MNT-200H annuale tramite contratto SLA e certificazione AS/EN 9110 in corso (target M+12-18).

Lo scale-up Y3+ multi-regione richiede MRO facility dedicata (Pentema o sito ottimizzato), 5-8 FTE manutenzione e partnership vendor per overhaul e ricambi.

In Phase B 6B HALE è prevista cooperazione con prime contractor (post DR-014 pivot), MRO facility specializzata stratospheric ops e partnership CIRA/Polito per test e validation.

## A.10.5 Costi annuali di manutenzione (OpEx)

| Categoria | Frequenza | Costo annuo Y1 (€) | Costo Y3 (flotta 3) (€) |
|---|---|---|---|
| MNT-PRE/POST (operativa) | Quotidiana | Incluso in personnel | Incluso |
| MNT-50H spare consumed | ~6-12 mesi | 1.500-4.000 | 5.000-12.000 |
| MNT-200H overhaul | 2-4 anni | 2.500-7.500 (avg/anno) | 8.000-25.000 |
| MNT-CAL batterie + sensori | Variabile | 2.500-6.000 | 7.500-18.000 |
| MNT-CORrective (su anomalia, stima 5-10%) | On-condition | 3.000-8.000 | 9.000-25.000 |
| Vendor SLA + ricambi | Continuo | 5.000-15.000 | 15.000-45.000 |
| **TOTALE MNT OpEx annuale** | | **14.500-40.500** | **44.500-125.000** |

> Allineato con Cap. 8 §8.5.1 OpEx "Manutenzione piattaforma 5-8% CapEx".

## A.10.6 Conformità regolatoria

- **Reg. UE 2019/947** art. 14: Manutenzione SAPR
- **ENAC Reg. APR Ed. 3** art. 19: Procedure manutenzione documentate
- **AS/EN 9110**: Quality Management Maintenance Organization (in corso certificazione M+12-18)
- **Part-IS EASA Reg. UE 2023/203**: Cybersecurity continuing airworthiness
- **D.Lgs. 81/2008**: Safety lavoratori operazioni manutenzione, incluso Titolo XI ATEX per hangar batterie LiPo

## A.10.7 Logbook e tracciabilità

Tutte le operazioni di manutenzione sono registrate in:
- **Aircraft Logbook** per ciascun velivolo, con vita operativa e tutte le manutenzioni
- **Component Logbook** per ciascuna parte critica, con tracciabilità lifetime
- **Maintenance Records** in database digitale, per query, audit e report

Conservazione: almeno 5 anni post-disposal velivolo (requisito ENAC).

## A.10.8 Falsifying observations

Due osservazioni falsificanti pilotano la revisione del piano. Se MTBF reale Y1 risulta inferiore a 100 h (contro target SyR di 200 h al Cap. 3), il Piano di Manutenzione va rivisto al rialzo e lifetime motori/batterie vanno rinegoziati con vendor. Se l'audit Part-IS Reg. UE 2023/203 identifica gap, il CISO attiva remediation entro 30 giorni.

## A.10.9 Versioning

- v1.0 M+3 (presente, preliminare)
- v1.5 M+6: update con piloti reali e vendor manuals
- v2.0 M+10: Maintenance Plan definitivo per gate G3 e SORA application

## A.10.10 Riferimenti

- Cap. 5 §5.8 (Standard tecnici AS/EN 9110)
- Cap. 6 §6.4 (FMECA, input per maintenance priority)
- Cap. 8 §8.5 (OpEx manutenzione)
- Vol. 3 R.1 [N-15] ENAC Reg. APR Ed. 3
- Vol. 3 R.2 [T-33] AS/EN 9100 + [T-34] AS/EN 9110
