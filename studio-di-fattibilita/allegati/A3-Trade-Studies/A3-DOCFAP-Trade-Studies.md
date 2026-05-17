# Allegato A.3 ‑ DOCFAP, Documento di Fattibilità delle Alternative Progettuali

> Volume 2, Allegato A.3
> Equivalente DOCFAP ex art. 41 D.Lgs. 36/2023 (Documento di Fattibilità delle Alternative Progettuali)
> Sintesi consolidata dei trade study chiave dello Studio di Fattibilità HALE/VTOL Firmamento Technologies
> **Metodologia:** metodologia di trade study (NASA SE Handbook §6.8 + INCOSE)

## A.3.0 Premessa metodologica

Il presente allegato sintetizza i **trade study formali** condotti per le decisioni architetturali chiave del progetto, in formato compatibile con il **DOCFAP** (Documento di Fattibilità delle Alternative Progettuali) ex art. 41 D.Lgs. 36/2023 + Allegato I.7.

Ogni trade study segue lo schema:
1. Problema decisionale
2. Alternative valutate (incluso "do nothing" / status quo)
3. Criteri di valutazione con pesi
4. Scoring matrix (1-10 per criterio per alternativa)
5. Sensitivity analysis (variazione pesi)
6. Considerazioni qualitative
7. Raccomandazione + condizioni
8. Falsifying observation

## A.3.1 Indice trade study

| TS-ID | Decisione | Capitolo riferimento | Status M+3 |
|---|---|---|---|
| **TS-PLATFORM-6A** | Selezione piattaforma VTOL pilota | Cap. 6.3.1 + allegato vendor RFQ | Update post audit: Tekever 7.05 vs JOUAV 6.25 |
| **TS-MATERIAL** | Composizione materiali strutturali HALE | Cap. 6.3.2 | Confermato: M2 Ibrido CFRP+lino (lino solo secondarie) |
| **TS-PROP-6B** | Architettura energetica HALE | Cap. 6.3.3 | Update post energy balance: E5 Seasonal mandatory plan A |
| **TS-AVI-6A** | Autopilota Percorso 6A | Cap. 6.3.4 | Confermato: AV1 JOUAV FCS proprietario integrato |
| **TS-PAYLOAD-EO** | Payload EO modulare Percorso 6A | Cap. 6.3.5 | Confermato: RGB + IR LWIR baseline |
| **TS-COMMS** | Architettura C2 + downlink dati | Cap. 6.3.6 | Confermato: RF primary + SATCOM Iridium secondary |

## A.3.2 TS-PLATFORM-6A, update M+3 (post analisi vendor RFQ)

**Decisione**: scelta della piattaforma VTOL commerciale baseline per il Percorso 6A.

**Alternative finali**:
- A1: JOUAV CW-30E (CN), payload 8 kg, autonomia 8h, vendor cinese
- A2: Tekever AR3 (PT), payload 2.5 kg, autonomia 16h, EU sovereign
- A3: Quantum Trinity F90+ (DE), payload 1 kg, autonomia 90 min
- A4: FlyingBasket FB3 (IT), payload 100 kg, autonomia 1h, made in IT

**Scoring rivisto post-audit vendor RFQ**:

| Criterio | Peso | A1 JOUAV | A2 Tekever | A3 Quantum | A4 FB3 |
|---|---|---|---|---|---|
| Autonomia missione | 20% | 8 | 9 | 4 | 2 |
| Payload compatibility | 15% | 9 | 6 | 4 | 10 |
| Certificabilità SAIL EASA | 15% | 5 ↓ | 9 ↑ | 9 | 7 |
| Lead time | 10% | 7 | 6 | 8 | 7 |
| TCO 5 anni | 15% | 8 | 6 | 8 | 5 |
| Supporto tecnico IT/EU | 10% | 5 | 9 | 9 | 10 |
| Geopolitica/dual-use risk | 10% | 3 ↓ | 9 ↑ | 9 | 9 |
| Reference customers EU | 5% | 3 | 8 | 7 | 6 |
| **Σ ponderato** | 100% | **6.25** | **7.05** | **6.85** | **6.50** |

**Shift vs Cap. 6.3.1 originale**: la parità A1/A2 (7.30/7.05) lascia ora spazio a un vantaggio chiaro per A2 Tekever.

**Raccomandazione aggiornata M+3**: avviare una **doppia RFQ formale parallela JOUAV + Tekever**, con decisione a M+6 sulle quotation reali. Tekever è il current preferred baseline.

**Falsifying observation**: se la quotation reale JOUAV restituisce CapEx 50% sotto stima e 6 reference EU verificati, il riequilibrio resta possibile.

## A.3.3 TS-MATERIAL, materiali strutturali HALE (confermato)

**Decisione**: composizione dei materiali per la struttura HALE.

**Verdetto M+3**: si sceglie **M2 Ibrido CFRP + lino per strutture secondarie**, con longherone primario in CFRP.

**Razionale**:
- Lino in **secondary structures** (skin, fairings), narrativa ESG e saving del 5-10% di peso rispetto a CFRP puro.
- CFRP standard per il **longherone primario** (certificabile).
- Saving vs full CFRP marginale ma con narrativa unica.
- Saving vs metallico non applicabile (HALE non metallico).

**Caveat DR-011 (chiuso)**: l'impiego di fibra di lino in strutture primarie certificate aerospace richiede un **qualification path di 7-11 anni** e €30-80M (vedi Springer 2024 [A-12]). Fuori scope dello Studio attuale. Confidence high sulle secondarie, **very low** sulle primarie.

## A.3.4 TS-PROP-6B, architettura energetica HALE (post simulazione energy balance)

**Decisione**: combinazione propulsione + storage per il Percorso 6B HALE.

**Alternative**:
- E1: Solare + Li-ion (250-300 Wh/kg pack)
- E2: Solare + LiS (350-450 Wh/kg target 2028)
- E3: Solare + Solid-State Li (380-450 Wh/kg target 2029-2030)
- E4: Solare + PEM Fuel Cell + LH2
- E5: Seasonal solar-only (no batteria perennial, marzo-ottobre)

**Risultati simulazione completa (allegato A.7 energy-balance)**:

| Architettura | Margine inverno 21/12 | Verdetto |
|---|---|---|
| E1 Solar+Li-ion | -75% (impossibile) | no perennial |
| E2 Solar+LiS | **-50.1%** (deficit) | no perennial (vs hand-calc "0-15%") |
| E3 Solar+SS Li | -42% (deficit) | no perennial |
| E4 Solar+PEM+LH2 | -35% (peggio del previsto) | no perennial loop (round-trip 0.50) |
| **E5 Seasonal-only (marzo-ottobre)** | **+31.4% equinozio marzo** | **ONLY VIABLE PLAN A** |

**Raccomandazione aggiornata M+3**: **E5 Seasonal-only** è **mandatory plan A** per la Phase B 6B. La perennial a 44°N non è fattibile con la tecnologia baseline 2026-2028.

**Plan B Y6+**: ri-valutazione con SS Li 450+ Wh/kg, profili ultra-low-Re e alleggerimento drastico.

**Falsifying observation**: confermata in Cap. 6 §6.2.2.3 e §6.3.3.

## A.3.5 TS-AVI-6A, autopilota Percorso 6A (confermato)

**Raccomandazione**: **AV1 JOUAV FCS proprietario** (integrato in CW-30E), score 8.05/10.

**Plan B se shift a Tekever**: Tekever FCS proprietario (score stimato ~7.5/10).

## A.3.6 TS-PAYLOAD-EO, payload EO modulare (confermato)

**Baseline**:
- RGB high-res: Phase One iXM 100 (100 MP, GSD 8 cm @ 500 m AGL)
- IR LWIR: WIRIS Pro (NEdT < 30 mK, GSD termico 5 m @ 500 m)
- **Y2+**: + multispettrale MicaSense Altum-PT (cooperative agricole)
- **Y3+**: + LiDAR YellowScan Voyager (infrastrutture lineari)

**Modularità**: swap in meno di 60 min (rivisto rispetto ai 30 min ottimistici iniziali) con team trained.

## A.3.7 TS-COMMS, architettura C2 + downlink (confermato)

**Percorso 6A**:
- **Primary**: RF 2.4 GHz ISM
- **Secondary**: SATCOM Iridium Certus L-band (per shadow zones Pentema)
- **Tertiary**: cellulare 4G fallback (dove disponibile)

**Percorso 6B**:
- **Service link**: S-band 2.0-2.2 GHz (3GPP Rel-17 n255/n256) o 700 MHz
- **Feeder link**: Ka 31-31.3 GHz (HAPS dedicata ITU)
- **C2 + telemetria**: SATCOM L-band Inmarsat/Iridium

## A.3.8 Trade study aggiuntivi futuri (M+6+)

- **TS-GOVERNANCE**: RTI vs JV vs contratto rete per Firmamento + 10 cooperative
- **TS-GROUND-CLOUD**: cloud IT/EU multi-provider vs single-provider per data hosting
- **TS-INSURANCE**: assicurazione BVLOS broker selection
- **TS-PARTNER-PHASE-B**: Aalto vs Sceye vs Skydweller vs CIRA vs TAS come prime contractor 6B (post DR-014)

## A.3.9 Conformità DOCFAP art. 41 D.Lgs. 36/2023

Il presente allegato soddisfa i requisiti del **DOCFAP** ex art. 41 + Allegato I.7:
- Identificazione delle alternative
- Criteri di valutazione comparativa
- Confronto strutturato
- Motivazione delle scelte
- Verifica di fattibilità tecnica + economica
- Considerazione vincoli regolatori + ambientali

## A.3.10 Versioning

- v1.0 M+3 (presente)
- v1.5 M+6, update post vendor quotation + workshop cooperative
- v2.0 M+10, definitivo per gate G3

## A.3.11 Riferimenti

- Cap. 6 (Analisi Tecnica)
- Metodologia trade study interna
- Vol. 3 R.2 (NASA SE + INCOSE)
- Vendor RFQ analysis (allegati/vendor-rfq/)
- Energy balance simulation (allegati/energy-balance/)
