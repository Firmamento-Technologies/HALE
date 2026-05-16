---
name: link-budget-calculator
description: Use when the user needs to calculate RF link budgets for HALE payload telecommunications (HAPS-to-user service link, HAPS-to-gateway feeder link, C2 link, telemetry). Trigger phrases - "link budget", "calcolo budget radio", "EIRP", "G/T", "C/N0", "fade margin", "path loss", "uplink/downlink", "interferenza", "copertura cella", "rain fade ITU-R P.618". Computes link budgets for HAPS service link, feeder link, and C2 link for the Firmamento Technologies HALE platform.
---

# Link Budget Calculator — HAPS / HALE

Skill per calcolare **link budget RF** per i payload telecom del progetto HALE, secondo:
- **ITU-R P.618** (Propagation data for Earth-space radiocommunications)
- **ITU-R P.676** (Atmospheric attenuation by gases)
- **ITU-R P.840** (Attenuation by clouds and fog)
- **3GPP TR 38.811** (NR-NTN channel models, scenari HAPS)

## Quando usare

- Capitolo 6.2 dello Studio: prestazioni payload telecom
- Allegato A.7: modello di calcolo link budget
- Valutazione copertura cella HAPS Pentema/Liguria
- Compliance allocation spettro AGCOM/ITU
- Trade study payload telecom (es. LTE vs 5G NR-NTN)

## Formula base del link budget

```
C/N0 [dB-Hz] = EIRP_tx - L_path - L_other + G/T_rx - k

dove:
  EIRP_tx [dBW]   = P_tx + G_tx - L_tx        (potenza isotropica irradiata equivalente)
  L_path  [dB]    = 20·log10(4π·d/λ)          (free space path loss)
  L_other [dB]    = L_atm + L_rain + L_cloud + L_pol + L_scint + L_body
  G/T_rx  [dB/K]  = G_rx - 10·log10(T_sys)    (figura di merito ricevitore)
  k       [dBW/K/Hz] = -228.6                  (costante Boltzmann)
```

Per la **disponibilità desiderata** (es. 99.5%, 99.9%):
```
Link margin = C/N0_available - C/N0_required ≥ fade_margin_threshold
```

## Parametri di input tipici

### Geometria

| Parametro | HAPS @20km | LEO @ 500 km | GEO @ 36000 km |
|---|---|---|---|
| Slant range minimo (nadir) | 20 km | 500 km | 36000 km |
| Slant range tipico (10° elev.) | 110 km | 2300 km | 36500 km |
| Free space path loss @ 2 GHz, 20 km | **124.5 dB** | 152 dB | 189.6 dB |
| Free space path loss @ 28 GHz, 20 km | **147.4 dB** | 174.8 dB | 212.4 dB |

### Bande di interesse HAPS (vedi telecom-ntn-payload-expert)

| Banda | Range | Uso tipico | Path loss extra | Rain fade Italia |
|---|---|---|---|---|
| S | 2.0-2.2 GHz | Service link mobile | Basso | ~0-1 dB |
| C HAPS | 6.4-6.7 GHz | Gateway feeder | Basso | ~1-3 dB |
| Ka HAPS gateway | 27.9-28.2 GHz | Feeder | Medio | ~5-15 dB |
| Ka HAPS feeder | 31-31.3 GHz | Feeder | Medio | ~6-18 dB |
| Q/V HAPS | 47.2-48.2 GHz | Future expansion | Alto | ~15-30 dB |
| 5G NR FR1 | 0.45-7.125 GHz | Mobile NTN | Basso-medio | ~0-3 dB |
| 5G NR FR2 | 24.25-52.6 GHz | Mobile NTN mmWave | Alto | ~5-30 dB |

## Template link budget HAPS service link (downlink HAPS → utente)

```markdown
# Link Budget — HAPS Downlink Service Link

## Configurazione
- Scenario: HAPS @20 km a nadir, utente fisso a terra
- Banda: 2.6 GHz (downlink LTE/NR n7)
- Modulazione: 16QAM, 5/6 coding rate (effective spectral efficiency 4.4 bps/Hz)
- Banda di canale: 20 MHz
- Disponibilità target: 99.5% (rain fade modello ITU-R P.618 zona Liguria)

## Transmitter (HAPS)
| Parametro | Valore | Unità |
|---|---|---|
| Potenza trasmessa | 25 | W |
| Potenza trasmessa | 14.0 | dBW |
| Antenna gain | 24 | dBi (beamforming) |
| Antenna loss | 1 | dB |
| **EIRP** | **37.0** | **dBW** |

## Propagation losses
| Parametro | Valore | Note |
|---|---|---|
| Distance (slant range) | 25 | km (nadir + ~10° offset) |
| Free space path loss @ 2.6 GHz, 25 km | 128.7 | dB |
| Atmospheric loss (ITU-R P.676) | 0.1 | dB |
| Cloud loss (ITU-R P.840) | 0.3 | dB |
| Rain fade 99.5% Italia (ITU-R P.618) | 1.2 | dB |
| Polarization loss | 0.5 | dB |
| Scintillation | 0.3 | dB |
| Body loss (UE on body) | 3.0 | dB |
| **Total L_other** | **5.4** | **dB** |
| **Total path loss** | **134.1** | **dB** |

## Receiver (UE)
| Parametro | Valore |
|---|---|
| Antenna gain | 0 dBi (omni small UE) |
| Antenna loss | 1 dB |
| LNA NF | 7 dB |
| System temperature | 290 K → 24.6 dB-K |
| **G/T** | **-25.6** dB/K |

## C/N0 budget
| Riga | Valore |
|---|---|
| EIRP | 37.0 dBW |
| - Total path loss | -134.1 dB |
| + G/T | -25.6 dB/K |
| + k correction | +228.6 dB |
| **C/N0** | **106.0 dB-Hz** |

## Conversione SNR e capacità
| Parametro | Valore |
|---|---|
| Banda | 20 MHz → 73.0 dB-Hz |
| **SNR = C/N0 - 10·log10(BW)** | **33.0 dB** |
| Spectral efficiency (Shannon) | 10.9 bps/Hz |
| Spectral efficiency (16QAM 5/6) | 4.4 bps/Hz |
| **Throughput pratico** | **88 Mbps** |

## Margin
| Parametro | Valore |
|---|---|
| SNR required (16QAM 5/6) | 11 dB |
| SNR available | 33 dB |
| **Link margin** | **22 dB** |

✓ Link feasible con largo margine. Possibile ulteriore modulation upgrade (256QAM) per maggior throughput.
```

## Template link budget HAPS feeder link (uplink utente → HAPS — più critico)

Per service link uplink (UE → HAPS), il bottleneck è tipicamente la **potenza UE**:

```
UE potenza tx: 23 dBm (200 mW, max 5G NR)
UE antenna gain: 0 dBi
EIRP_UE: 22 dBW
Path loss: 134.1 dB
HAPS G/T: alto (antenna grande + LNA buono)
HAPS BW: 5-10 MHz allocato per UE
SNR risultante: critico, da modellare con accuratezza
```

## ITU-R P.618 — Rain fade Italia

Per la **Liguria**, zona rain climate "K" (ITU-R P.837):
- Rain rate 0.01% (R_0.01): ~28-32 mm/h
- A 2.6 GHz, 25 km slant: rain fade 0.01% ≈ 0.5 dB → negligibile
- A 28 GHz, 25 km slant: rain fade 0.01% ≈ 25 dB → significativo
- A 47 GHz, 25 km slant: rain fade 0.01% ≈ 40 dB → dominant

**Conclusione:** per service link Italia preferire bande sub-6 GHz; bande mm-wave solo per feeder link con site diversity.

## Trade-off chiave

### Antenna gain HAPS vs copertura cella
- Antenna larga (≥ 3 m) → gain alto (≥ 28 dBi) → cella stretta (≤ 5 km diametro)
- Antenna stretta (≤ 0.5 m) → gain basso (≤ 12 dBi) → cella larga (≥ 30 km)
- **Soluzione moderna**: AESA digitale → multi-beam, ogni beam settabile

### Numero di beam
| Beam | Antenna size | Copertura totale | Capacità per beam |
|---|---|---|---|
| 1 (single) | 0.3 m | ~50 km diametro | Bassa |
| 4-8 | 0.5-1 m | ~50 km, 4-8 celle | Media (5-20 Mbps/cella) |
| 16-32 (AESA) | 1-2 m | ~50 km, 16-32 celle | Alta (50-200 Mbps/cella) |
| 64-128 (AESA digitale) | 2-3 m | ~50 km, dense | Molto alta |

## C2 link (Command & Control)

Per la C2 dal pilota UAS al velivolo:
- Banda: tipicamente 2.4 GHz o 5.8 GHz (UAS) o SATCOM (Iridium Certus, L-band)
- BW richiesta: 1-100 kbps (telemetria + comandi)
- Latency budget: ≤ 250 ms one-way (EASA SC-Light-UAS)
- Disponibilità target: 99.9% (continuity of control)
- Fade margin: ≥ 12 dB (per ostacoli orografici)

Per **Pentema** (valle stretta): probabile **necessità SATCOM** come secondary link per shadow zones RF terrestre.

## Output che produce questa skill

- Excel link budget (uplink + downlink + feeder + C2)
- Margin charts (margin vs distance, vs frequency, vs elevation)
- Coverage maps (analitiche, anche solo a tavolino)
- Capacità aggregata cella (Mbps × n. beam)
- Rain fade analysis ITU-R P.618 per zona target
- Compliance check con allocation AGCOM/PNRF
