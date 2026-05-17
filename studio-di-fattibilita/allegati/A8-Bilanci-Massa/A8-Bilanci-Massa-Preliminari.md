# Allegato A.8 — Bilanci di Massa Preliminari

> Volume 2, Allegato A.8
> Mass budgets preliminari Percorso 6A (VTOL) + Percorso 6B (HALE)

## A.8.0 Premessa metodologica

I bilanci di massa sono stimati secondo metodologia **NASA SE Handbook §6.4** + **AIAA aerospace mass properties standard**. Per ogni voce:
- **Dry mass** (massa a vuoto)
- **Margin** (% riserva per design evolution Phase A → C)
- **Confidence** (high/medium/low)

## A.8.1 Mass Budget Percorso 6A — JOUAV CW-30E (vendor baseline)

### Riferimento vendor: JOUAV datasheet CW-30E (Confidence: medium)

| Subsistema | Massa baseline (kg) | Margin Phase A | Total con margin (kg) | Confidence |
|---|---|---|---|---|
| Struttura fusoliera + ala fissa | 12.0 | 10% | 13.2 | M |
| Sistema VTOL (4 motori + eliche) | 5.5 | 15% | 6.3 | M |
| Sistema cruise (motore traente + elica) | 2.5 | 10% | 2.8 | M |
| Avionica (FCS + GNC + ridondanza) | 1.5 | 20% | 1.8 | M |
| Batterie LiPo VTOL | 4.5 | 10% | 5.0 | M |
| Carburante (benzina/heavy oil) + tank | 4.0 | 10% | 4.4 | H |
| Sistema comunicazione (RF + SATCOM) | 0.8 | 25% | 1.0 | M |
| **TOTALE EMPTY** | **30.8** | | **34.5** | M |
| Payload max | 8.0 | 0% | 8.0 | H |
| **MTOW** | **38.8** | | **42.5** | M |

> **Vendor MTOW dichiarato**: 38 kg. Con margin Phase A standard aerospace 10-25%, MTOW effettivo Y1 può raggiungere 42 kg. Verificare con quotation reale (DR-003).

### Payload breakdown (8 kg disponibili)

| Configurazione | Componenti | Massa stimata (kg) |
|---|---|---|
| **Baseline EO** | Phase One iXM 100 + gimbal + storage | 4-5 |
| **Antincendio** | WIRIS Pro IR LWIR + lens + storage | 3-4 |
| **Configurazione combinata baseline + antincendio** | EO + IR + gimbal multi | 6-7 |
| **Configurazione + telecom backup** | + LTE eNodeB tattico (~50W RF) | 7-8 (limite) |
| **Configurazione + LiDAR** | LiDAR YellowScan Voyager | 6-8 (sostitutivo) |

> Trade-off: telecom backup eslcude LiDAR contemporaneo. Mission planning dedicato per configurazione swap (60-90 min ground).

## A.8.2 Mass Budget Percorso 6A — Tekever AR3 (vendor benchmark Plan B)

### Riferimento vendor: Tekever AR3 datasheet (Confidence: medium-high)

| Subsistema | Massa baseline (kg) | Margin | Total (kg) |
|---|---|---|---|
| Struttura fixed-wing (ala + fusoliera + coda) | 10.0 | 10% | 11.0 |
| Sistema propulsione elettrica | 2.0 | 15% | 2.3 |
| Sistema decollo (catapulta-launched, no VTOL) | 1.5 | 10% | 1.7 |
| Batterie Li-ion | 4.5 | 10% | 5.0 |
| Avionica (FCS + GNC) | 1.0 | 20% | 1.2 |
| Sistema comunicazione | 0.5 | 25% | 0.6 |
| **TOTALE EMPTY** | **19.5** | | **21.8** |
| Payload max | 2.5 | 0% | 2.5 |
| **MTOW** | **22.0** | | **24.3** |

> Tekever AR3 ha MTOW dichiarato 25 kg. Margin più stretto di JOUAV (più piccolo). Payload 2.5 kg = limita configurazioni (RGB + IR baseline OK; aggiunte limitate).

## A.8.3 Mass Budget Percorso 6B — HALE solare (stima preliminare)

### Riferimento: concept Polito HELIPLAT + Zephyr 8/S benchmark (Confidence: low-medium)

| Subsistema | Massa baseline (kg) | Margin Phase A | Total con margin (kg) | Note |
|---|---|---|---|---|
| **Struttura primaria** (ala + fusoliera + coda) | 35-50 | 25% | 44-63 | CFRP + lino skin secondaria |
| Pannelli solari multi-junction GaAs + film | 8-15 | 15% | 9-17 | 25 m² × ~0.5 kg/m² |
| Batterie LiS (target 2028) | 20-35 | 20% | 24-42 | Range dipende da architettura E2 vs E5 |
| Propulsione elettrica (motori + eliche) | 5-10 | 15% | 6-12 | Ridondante |
| Avionica + GNC + FCS DAL-C | 5-10 | 25% | 6-13 | Triplex IMU + GNSS |
| Sistema C2 (antenne + transceiver) | 2-5 | 25% | 3-6 | SATCOM + RF backup |
| Payload (EO + IR + opt. NTN gNB) | 5-10 | 0% (allocato) | 5-10 | Configurabile |
| Sistema termico (heat/cool) | 3-7 | 30% | 4-9 | Riscaldamento batterie + cooling payload |
| Cablaggi + connettori MIL-spec | 2-4 | 25% | 3-5 | |
| Sistema struttura secondaria (fairings, etc.) | 3-6 | 20% | 4-7 | Possibile lino |
| **TOTALE MTOW** | **88-152** | | **108-184** | Range con margin |

> **Range MTOW** baseline: 85-150 kg (target Y3-Y5). Con margin Phase A 20-25%: **108-184 kg effettivi**. Vincolo strutturale apertura b ≤ 30 m + AR ≥ 25 → wing area ≤ 36 m².

### Centro di gravità (CG)

Bilanciamento longitudinale richiede:
- CG entro 25-30% MAC (Mean Aerodynamic Chord)
- Batterie posizionate strategicamente per CG control (tipicamente 40-60% MTOW = 35-90 kg)
- Payload bay vicino al CG ideale

### Wing loading (W/S)

- MTOW baseline 100 kg, S = 25 m² → W/S = (100 × 9.81) / 25 = **39.2 N/m²**
- Target HALE: 30-50 N/m² (tipico — vs aviazione manned 500+ N/m²)
- Conferma profilo low-Re + bassa velocità (TAS 30-50 km/h)

## A.8.4 Mass evolution Phase A → Phase B (HALE 6B)

| Fase | MTOW target (kg) | Margin remaining | Confidence |
|---|---|---|---|
| Pre-Phase A (concept) | 80-150 | 30% | Low |
| Phase A (PFTE M+0-12) | 100 ± 25 | 25% | Low-Medium |
| Phase B subscale 1:3 (M+24-48) | 30-50 (scale 1:3 di 80-150 kg) | 20% | Medium |
| Phase C/D full-scale | 100-150 | 10-15% | Medium-High (post test) |
| Production | 90-140 (mass optimization) | 5-10% | High |

## A.8.5 Sensitivity di MTOW su energy balance

Mass overrun ha impatto significativo su energy balance perennial (cfr Cap. 6 §6.2.2 + allegato A.7 energy-balance):

| ΔMTOW vs baseline 100 kg | P_cruise (W) | Margine inverno (%) | Verdetto |
|---|---|---|---|
| -20 kg (80 kg) | -25% ≈ 600 W | +12% (best case) | Marginale OK |
| Baseline 100 kg | 800 W | -50.1% (simulazione) | DEFICIT |
| +20 kg (120 kg) | +25% ≈ 1000 W | -68% | DEFICIT severe |
| +50 kg (150 kg) | +60% ≈ 1280 W | -85% | NON FATTIBILE |

> **Implicazione**: ogni kg risparmiato in mass budget = ~0.5% margine inverno (vedi sensitivity allegato A.7). Aggressive mass optimization è critica per Phase B 6B.

## A.8.6 Bilancio strutturale (preliminare, Confidence: low)

### V-n diagram preliminare (HALE 6B)

- Velocità manovra Va: ~50 km/h TAS
- Velocità crociera Vc: 30-40 km/h TAS
- Velocità dive Vd: ~70 km/h TAS
- Limit load factor n+: +3.0 / n-: -1.5
- Ultimate load factor: limit × 1.5

### Gust envelope

- Cruise gust 5 m/s (FAR 23 / CS-23 reference)
- Margin di sicurezza struttura: ≥ 50% sopra ultimate

## A.8.7 Status M+3 + roadmap

| Item | Status | Deadline |
|---|---|---|
| Mass budget concept | ✓ | M+3 |
| Detail Phase A mass breakdown | ⏳ | M+6 |
| Wind tunnel scale model mass | ⏳ | M+12 |
| Subscale 1:3 mass budget detailed | ⏳ | M+24 |
| Mass property testing | ⏳ | M+24-30 |

## A.8.8 Falsifying observations

- Se Phase B subscale 1:3 weight effettivo > 50 kg, scale-up full size MTOW > 180 kg → energy balance inverno definitivamente non fattibile anche seasonal
- Se Phase A detailed CAD restituisce struttura primaria > 60 kg, intera architettura va rivista (riduzione dimensione o materiali più aggressivi)

## A.8.9 Riferimenti

- Cap. 6 §6.1, §6.2
- Allegato A.7 (energy balance)
- Allegato A.3 (TS-MATERIAL)
- Vol. 3 R.2 [T-60] Megson Aircraft Structures
- Vol. 3 R.5 [A-01..A-06] Polito HELIPLAT papers
