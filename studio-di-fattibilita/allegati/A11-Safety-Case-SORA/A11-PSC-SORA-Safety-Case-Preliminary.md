# Allegato A.11 : PSC Operativo / SORA Safety Case Preliminare

> Volume 2, Allegato A.11
> Piano di Sicurezza e Coordinamento operativo (PSC) + SORA Safety Case preliminare
> Conformità D.Lgs. 36/2023 art. 41 (PSC obbligatorio) + EASA SORA 2.5 (Amendment 3, settembre 2025)

## A.11.0 Premessa metodologica

Il presente allegato consolida due documenti distinti in un'unica istruttoria. Il primo è il **PSC** ex art. 41 D.Lgs. 36/2023, Piano di Sicurezza e Coordinamento operativo per le attività di volo. Il secondo è il **SORA Safety Case** preliminare, redatto secondo **JARUS SORA 2.5 / EASA ED Decision 2025/018/R**.

Lo scope coperto è il Percorso 6A, ovvero il VTOL pilota Pentema BVLOS in Categoria Specific.

Il Safety Case Certified Category della Phase B 6B HALE resta out-of-scope: sarà sviluppato in fase R&D Phase B M+24+.

## A.11.1 Concept of Operations (ConOps) : Sintesi

**Operatore**: Firmamento Technologies S.r.l. (in registrazione presso ENAC come UAS Operator)
**Piattaforma**: VTOL ibrido fixed-wing (JOUAV CW-30E o Tekever AR3, decisione M+6)
**Area operativa primaria**: Pentema (Torriglia, GE) + Valli dell'Antola-Tigullio (SNAI Liguria)
**Profilo missione tipico**: BVLOS, quota 200-500 m AGL, raggio 10-30 km dalla GS

### Use case primari (vedi Cap. 7 §7.2.2)
- UC-001 Monitoraggio frane settimanale (mapping fotogrammetrico)
- UC-002 Antincendio boschivo (IR + alert real-time)
- UC-003 Connettività emergenza (LTE backup on-demand)
- UC-004 Mapping infrastrutture (RGB + LiDAR Y2+)

## A.11.2 SORA 2.5 Analysis Preliminare

### Step 1 : ConOps Description (Concept of Operations)

Si veda §A.11.1 per la sintesi. Il documento ConOps completo è in Cap. 4 §4.4 (ICD) e Cap. 6 §6.1.

### Step 2 : iGRC (intrinsic Ground Risk Class)

**Parametri**:
- Maximum characteristic dimension (UAS): ~2-3 m
- Maximum cruise speed: 100-120 km/h
- Operational scenario: **BVLOS over sparse populated area** (Pentema 14 abitanti + valli sparse)
- Population density: **sparsely populated** (< 25 persone/km²)

**iGRC stimato preliminare**: **4-5** (su tabella SORA 2.5 Annex E per scenari sparse populated + dimensione media UAS)

### Step 3 : Final GRC after mitigations (M1, M2, M3)

| Mitigation | Application | Impact GRC |
|---|---|---|
| **M1 Strategic mitigation**: Geofence aree residenziali + restricted area NOTAM-coordinated | ✓ Application | -1 |
| **M2 Tactical mitigation**: Parachute recovery + auto-return-to-base + ground risk reduction | ✓ Robust application | -1 |
| **M3 ERP**: Emergency Response Plan + crew training + comms with local authorities | ✓ Application | -0.5 |

**Final GRC stimato**: **2-3** (post M1+M2+M3)

### Step 4 : iARC (initial Air Risk Class)

**Air risk parameters**:
- Operating altitude: ≤ 500 m AGL (entirely below FL150)
- Airspace class: **Classe G non-controlled** (Appennino Ligure, fuori CTR aeroporti GE/MI)
- Other traffic: GA occasionale + paracadutisti + parapendio sporadici
- Probability of encountering manned aircraft: **low**

**iARC stimato**: **b** (low traffic VLL non-controlled)

### Step 5 : Final ARC after strategic mitigation

| Mitigation Air | Application | Impact ARC |
|---|---|---|
| TMPR (Tactical Mitigation Performance Requirement): coordinamento ENAV + NOTAM | ✓ | -0 (già b) |
| ATC service NOT applicable (Classe G) | n/a | n/a |

**Final ARC**: **b** confermato

### Step 6 : SAIL Determination

Dalla matrice SORA 2.5: Final GRC 2-3 × Final ARC b conduce a **SAIL II** (preliminary).

Per scenari più aggressivi, ad esempio l'avvicinamento all'abitato di Pentema, la determinazione potrebbe salire a **SAIL III**.

**Stima preliminare**: **SAIL II-III** (vedi DR-004, pre-application meeting ENAC necessario per validation).

### Step 7 : Identify Applicable OSO (Operational Safety Objectives)

Per SAIL II si applicano ~10-12 OSO. Per SAIL III il numero sale a ~16-18 OSO.

Lista OSO chiave (SAIL III):
- **OSO #02**: UAS manufactured by competent and/or proven entity (vendor verification)
- **OSO #03**: UAS maintained by competent and/or proven entity (AS/EN 9110 ref.)
- **OSO #04**: UAS developed to authority recognised design standards (vendor compliance)
- **OSO #05**: UAS is designed considering system safety and reliability (FMECA + FTA Cap. 6.4)
- **OSO #07**: Inspection of the UAS (preflight + post-flight check)
- **OSO #08**: Operational procedures are defined, validated and adhered to (Operations Manual)
- **OSO #09**: Remote crew trained and current and able to control the abnormal situation (training program)
- **OSO #11**: Procedures are in-place to handle the deterioration of external systems supporting UAS operation (lost link, weather)
- **OSO #14**: Operational procedures are defined, validated and adhered to (operations control)
- **OSO #16**: Multi crew coordination (PIC + observer)
- **OSO #18**: Automatic protection of the flight envelope from human errors (autopilot envelope protection)
- **OSO #19**: Safe recovery from human error (auto-return-to-base + parachute)
- **OSO #20**: A safety risk assessment of UAS operation by mass and area population density (this SORA itself)
- **OSO #21**: External services supporting UAS operation are adequate to the operation
- **OSO #23**: Environmental conditions for safe operations defined, measurable and adhered to (weather minima)
- **OSO #24**: UAS designed and qualified for adverse environmental conditions

### Step 8 : Containment Requirements

- **Containment area**: definita pre-volo, raggio 30 km dalla GS, geofenced
- **Termination mechanism**: parachute recovery + auto-land in area designata
- **Loss of containment threshold**: probabilità < 10^-4/h (SAIL III)

### Step 9 : Operations Manual + Maintenance Manual + Procedures

L'Operations Manual è previsto in draft entro M+6 e in versione completa al M+9, per consentire la SORA submission.

## A.11.3 Piano di Sicurezza e Coordinamento (PSC) : Operativo

### A.11.3.1 Sicurezza del personale

Il personale di terra opera con DPI dedicati (elmetto, occhiali, scarpe antinfortunistica). La formazione obbligatoria copre tre figure distinte: il pilota UAS BVLOS, in possesso di attestato ENAC e di abilitazione UAS specific; il ground crew, formato sulla sicurezza generale e sulla gestione ATEX dell'hangar batterie; il mission commander, qualificato in emergency response training. La polizza RC aviation deve garantire copertura BVLOS pari ad almeno €5M.

### A.11.3.2 Sicurezza popolazione e terzi

Le misure operative previste sono le seguenti:
- Geofence aree residenziali Pentema (raggio 200 m da abitazioni)
- NOTAM coordination ENAV ogni missione
- Avviso comunità Pentema (1 settimana prima, via Comune Torriglia)
- Crew brief comunità: workshop pubblico iniziale M+3 (Open Question OQ-009)

### A.11.3.3 Emergency Response Plan (ERP)

| Scenario emergenza | Risposta |
|---|---|
| Lost Link permanente | Auto-return-to-base; se non raggiungibile, auto-land area pre-designata |
| Perdita propulsione | Parachute deployment automatico (< 7 m/s impact velocity) |
| Avaria FCS critica | Fail-safe behaviour + parachute + emergency comms |
| Cyber attack (jamming) | Switch a SATCOM secondary + retreat to base |
| Incidente con conseguenze | Comunicazione immediata: 112 + ENAC ANSV + assicurazione + sindaco Torriglia |
| Evento meteo estremo | Cancellazione missione + secure storage hangar |

### A.11.3.4 Coordinamento con autorità locali

Il coordinamento istituzionale prevede comunicazione preventiva e accordi operativi con il Comune di Torriglia, l'attivazione di un canale dedicato con i Carabinieri Forestali per le attività SAR e antincendio, un protocollo emergenza con i Vigili del Fuoco Liguria, una collaborazione con ARPA Liguria sul monitoraggio ambientale e una convenzione operativa con la Protezione Civile Liguria per il servizio backup.

### A.11.3.5 Documentazione operativa obbligatoria

- Operations Manual (entro M+9)
- Maintenance Manual (entro M+9)
- Pilot License + Currency Records (continuativo)
- Aircraft Logbook (continuativo)
- Insurance Certificate (annuale)
- ENAC Authorization (rinnovo annuale)
- SORA documentation (sempre disponibile per audit)
- ERP documentation (annuale review + drill)

## A.11.4 Risk Acceptance Matrix

| Risk level | Action |
|---|---|
| **Catastrophic** (Fatal accident) | NOT ACCEPTABLE: operazione vietata |
| **Hazardous** (Serious injury or major damage) | Mitigation obbligatoria + insurance coverage |
| **Major** (Operational disruption) | Mitigation raccomandata + procedure |
| **Minor** (Minor inconvenience) | Procedures + monitoring |
| **Negligible** | Logged for trend analysis |

## A.11.5 Engagement plan ENAC

| Fase | Action | Deadline |
|---|---|---|
| **Pre-application meeting** | Presentazione preliminare ConOps + SORA approach | M+3-6 (DR-004) |
| **SORA application submission** | Documenti SORA completi + Operations Manual + Maintenance Manual | M+9-12 |
| **Risposte integrazioni** | Risposta a richieste ENAC (tipicamente 2-3 round) | M+10-18 |
| **Authorization issuance** | Autorizzazione operativa ENAC | M+12-24 (sliding timeline Cap. 9 §9.12) |
| **Operations + reporting** | Reportistica eventi + annual review | Continuativo |

## A.11.6 Sliding timeline rischio regolatorio

In linea con Cap. 9 §9.12 sliding timeline e con l'audit `regulatory-adversary`, si distinguono due scenari di percorrenza. Lo scenario nominale prevede pre-app M+3, SORA M+9, Authorization M+9 e Operations M+10. Lo scenario sliding realistico, viceversa, sposta pre-app a M+6-9, SORA a M+10-12, Authorization a M+15-24 e Operations a M+16-26.

**Falsifying observation**: se al M+12 ENAC pre-application restituisce GRC > 5 (SAIL ≥ IV), il modello operativo va rivisto a VLOS-only Y1 con re-design ConOps per Y2.

## A.11.7 Status M+3 + roadmap

- ✅ ConOps preliminare definito (Cap. 4 §4.4 + Cap. 6 §6.1)
- ✅ SORA Step 1-6 preliminare (questo allegato)
- ⏳ Step 7-9 detailed (M+6-9)
- ⏳ Operations Manual + Maintenance Manual (M+6-9)
- ⏳ SORA application submission ENAC (M+9-12)
- ⏳ ERP testing + drill (M+6+)

## A.11.8 Riferimenti

- Cap. 5 §5.1.5 (Metodologia SORA 2.5) + §5.4.1 (Strategia 6A Specific Category)
- Cap. 6 §6.4 (FMECA + FTA, input safety case)
- Vol. 3 R.1 [N-05] Reg. UE 2019/947 + [N-07] EASA ED Decision 2025/018/R
- Vol. 3 R.1 [N-15] ENAC Reg. APR Ed. 3 art. 11 + 26
- Vol. 3 R.2 [T-31] JARUS SORA 2.5
- DR-004 (audit-rigore-epistemico.md), pre-application ENAC ancora aperto
