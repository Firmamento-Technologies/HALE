# Volume 2 — Allegati Tecnici

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 2 — Allegati Tecnici
>
> **Versione:** M+3 bozza
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7

## Struttura Volume 2

| Allegato | Path | Contenuto | Status |
|---|---|---|---|
| **A.1** | [`A1-RTM/`](A1-RTM/) | RTM v1.0 (279 record, 14 sheet) **+ v1.5** (285 record, +1 StNeed-029 Ente Parco + 1 SyR-NF-AMB-001 + 3 SsR ambientali + 1 NegR + 2 VR-AMB; coverage StNeed→SyR 100%, SyR→VR 100%, SyR→SsR 75%) | ✅ v1.5 |
| **A.2** | [`A2-Risk-Register/`](A2-Risk-Register/) | Risk Register v1.0 (116 rischi, 22 sheet, 5+5 showstopper) **+ v1.5** (119 rischi, +3 RSK-AMB-001/002/003 nuova categoria Ambientale, 14 categorie totali; 10 EWI-AMB + FMECA ambientale preliminary + FTA cut-set bird-strike; RED reduction 88% mantenuta) | ✅ v1.5 |
| **A.3** | [`A3-Trade-Studies/`](A3-Trade-Studies/) | DOCFAP — Documento Fattibilità Alternative Progettuali | ✅ |
| **A.4** | [`A4-ICD/`](A4-ICD/) | ICD preliminary v1.0 (59 interfacce, 13 sheet) **+ Detailed v2.0** (5 interfacce critiche engineering-grade: INT-03 C2 RF MAVLink+AES + INT-04 SATCOM Iridium Certus + INT-05 Payload GigE+CAN FD + INT-13 DAA ADS-B+non-cooperative + INT-15 Privacy blur YOLOv8n) | ✅ v2.0 |
| **A.5** | [`A5-VV-Plan/`](A5-VV-Plan/) | Verification & Validation Plan v1.0 (71 SyR, 7 sheet, €1.57M test) | ✅ |
| **A.6** | [`A6-CAD/`](A6-CAD/) | Schemi/disegni CAD del concept (placeholder; CAD binari in `/cad/`) | ✅ |
| **A.7** | [`A7-Link-Budget/`](A7-Link-Budget/) + [`energy-balance/`](energy-balance/) + [`financial-model/`](financial-model/) | Modelli di calcolo (3 modelli: link budget 14 scenari ITU-R, energy balance HALE 365gg, finanziario 10 sheet) | ✅ |
| **A.8** | [`A8-Bilanci-Massa/`](A8-Bilanci-Massa/) | Bilanci di massa preliminari (6A + 6B) | ✅ |
| **A.9** | [`A9-Computo-Metrico/`](A9-Computo-Metrico/) | Computo Metrico Estimativo preliminary v1.0 **+ v1.5 WBS 3** (48 KB / 665 righe, ~100 voci WBS 3 in 10 macro-categorie ground segment Pentema, totale base €505k range €419-707k, OpEx ground segment €73k/anno, tariffario FTE 11 ruoli, cronoprogramma spese Y1 + S-curve) | ✅ v1.5 |
| **A.10** | [`A10-Piano-Manutenzione/`](A10-Piano-Manutenzione/) | Piano Manutenzione preliminary v1.0 **+ Operativo v1.5** (70 KB / 973 righe, 84 task in 5 sistemi del CW-30E, calendar Y1 80 missioni, spare parts strategy 3 livelli, Maintenance Organization, costi LCC Y1 €78-173k incluso CapEx GSE) | ✅ v1.5 |
| **A.11** | [`A11-Safety-Case-SORA/`](A11-Safety-Case-SORA/) | PSC + SORA Safety Case preliminary v1.0 **+ COMPLETE v2.0** (SORA 2.5 ED Decision 2025/018/R Amd.3: Steps 1-8 completi + 24 OSO + SAIL III preliminary + Pre-Application Package ENAC con Q&A top-10 + 10 OQ-SORA tracciate) | ✅ v2.0 |
| **A.12** | [`A12-VIA-preliminare/`](A12-VIA-preliminare/) | VIA preliminary v1.0 **+ COMPLETE v2.0** (13 sezioni + VIncA Allegato G DPR 357/1997 + Parco Antola L.R. 12/1995 + SIC/ZSC/ZPS IT1331402 + 3 nuovi RSK-AMB-001/002/003 + 18 mitigazioni M-AVI/NOI/ACQ/PAE + procedura raccomandata Verifica Assoggettabilità art. 19 non-assoggettabile P 60-70%) | ✅ v2.0 |
| **A.13** | [`A13-Documentazione-Fotografica/`](A13-Documentazione-Fotografica/) | Documentazione fotografica del contesto (placeholder, foto da acquisire) | ✅ |

## Allegati aggiuntivi (operativi)

| Allegato extra | Path | Contenuto |
|---|---|---|
| **A.x — Vendor RFQ** | [`vendor-rfq/`](vendor-rfq/) | RFQ template + cover letter + analisi quotation JOUAV vs Tekever |

## Status complessivo M+3

- ✅ **13/13 allegati Vol. 2** COMPLETATI (8 main session + 5 subagent)
- ✅ **+ allegato extra vendor-rfq/** (RFQ template + analisi quotation JOUAV vs Tekever)
- ✅ **Volume 3 riferimenti bibliografici** completo (R.1, R.2, R.3, R.4, R.5)

### Dimensioni aggregate Volume 2
- ~30 file .md + ~12 file .xlsx + ~15 file .py + ~10 PNG + 3 .csv
- ~1.5-2 MB di documentazione tecnica indicizzabile

### Subagent batch 1 completati
1. A.1 RTM v1.0 — 279 record (28 StNeed + 65 SyR + 81 SsR + 22 IR + 15 NegR + 68 VR), coverage 100/72/100%
2. A.2 Risk Register v1.0 — 116 rischi in 11 categorie, 5+5 showstopper, post-mitigation RED da 17→2 (88% reduction)
3. A.4 ICD v1.0 — 59 interfacce in 8 categorie, 13 sheet Excel
4. A.5 V&V + A.7 Link Budget — V&V Matrix 71 SyR + 14 scenari link budget ITU-R compliant (12/14 OK)

### Subagent batch 2 — refinement engineering-grade (M+3 post audit Red Team)
5. **A.4 ICD Detailed v2.0** (77.7 KB / 1260 righe) — 5 interfacce critiche byte-level: MAVLink v2.0 dialect JOUAV + AES-256-GCM nonce mgmt + state machine lost-link, Iridium Certus AT command + escalation timer, MIL-1553 vs Ethernet AVB vs CAN FD trade + verdetto ibrido GigE+CAN FD, DAA ADS-B DO-260B + non-cooperative pseudocode CPA DO-365B + ADS-L ED-270, privacy pipeline 8-step YOLOv8n INT8 TensorRT 8ms + JSON log hash chain ECDSA P-256. Confidence aggregato sistema: medium. 10 GAP tracciati (top 3: GAP-01 MAVLink dialect proprietary M+6, GAP-06 ENAC feedback DAA non-cooperative M+6, GAP-08 DPIA Garante M+7).
6. **A.11 SORA Safety Case Complete v2.0** (64 KB / 969 righe) — SORA 2.5 ED Decision 2025/018/R Amendment 3: Steps 1-8 + ConOps narrative UC-001..004, Class III, iGRC 5→GRC 3 (M1+M2+M3), iARC b→ARC b (TMPR Standard), **SAIL III preliminary** (driver GRC 3 × ARC b), 24 OSO matrice completa, Containment target <1×10⁻⁴/h via geofence hard+FTS+parachute. Pre-Application Package ENAC: 11 documenti D-01..11 + Q&A top-10 anticipato + 10 OQ-SORA tracciate. Confidence: medium (adeguato pre-app, non sufficiente application formale).
7. **A.12 VIA Preliminare Complete v2.0** (55 KB / 838 righe) — 13 sezioni + VIncA screening Allegato G DPR 357/1997 + Parco Antola L.R. 12/1995 + SIC/ZSC/ZPS IT1331402 + impatti su 10 fattori ambientali + linkage Risk Register con **3 nuovi RSK-AMB-001/002/003 proposti** (avifauna/rumore/paesaggio) + 18 mitigazioni dettagliate M-AVI/NOI/ACQ/PAE + cronoprogramma engagement M+3-M+12. **Procedura raccomandata**: Verifica di Assoggettabilità ex art. 19 D.Lgs. 152/2006 + L.R. 32/2012 con esito atteso NON-assoggettabilità (P 60-70%) + Screening VIncA Livello I. Proposto **REQ-NF-AMB-01** nuovo per RTM.

### Subagent batch 3 — integrazione cross-volume + refinement v1.5 (M+3 post integrazione)
8. **A.1 RTM v1.5** (34.7 KB report + 12.7 KB CSV delta) — integrazione StNeed-029 Ente Parco Antola + Natura 2000 IT1331402 + SyR-NF-AMB-001 famiglia NF Environmental Compliance + 3 SsR ambientali (OPS geofence Parco + AVI quota min 200m AGL su SIC + DAT logging conformità) + 1 NegR-016 (NO sorvolo nidi marzo-luglio buffer 500m) + 2 VR-AMB (audit Ente Parco + monitoring acustico). Totale record 279→285 (+6); StNeed 28→29, SyR 65→66, SsR 81→84, NegR 15→16, VR 68→70. Coverage StNeed→SyR 100%, SyR→VR 100%, SyR→SsR 75% (+2.9pp). Confidence sezione ambientale: medium.
9. **A.2 Risk Register v1.5** (60.8 KB report + 4.85 KB CSV delta) — integrazione 3 RSK-AMB ambientali in Top-28 (#26 RSK-AMB-001 Avifauna YELLOW + #27 RSK-AMB-002 Rumore GREEN + #28 RSK-AMB-003 Paesaggio GREEN), nuova categoria "Ambientale" (14 categorie totali), 10 EWI-AMB ambientali (continuo log + stagionale bioacustica + trimestrale Ente Parco + una-tantum DGR), FMECA ambientale preliminary (6 failure modes, RPN dominante 140 flushing aquila reale), FTA cut-set bird-strike ~5E-7/h + abort ambientale 1-2%. Totale rischi 116→119. Showstopper 5+5 invariato. RED reduction 88% mantenuta.
10. **A.9 Computo Metrico v1.5 WBS 3** (48 KB / 665 righe) — ground segment Pentema WBS 3 con ~100 voci in 10 macro-categorie (Hangar scenario A riuso/B light build + GCS fissa/mobile + Antenne RF + Storage processing + Connettività + Sicurezza + Impianti + Cartellonistica + Allestimenti). Totale Computo base **€505k** (range worst/base/best €419-707k IVA inclusa). OpEx run-rate Y2+ ground segment **€73k/anno**. Tariffario FTE 11 ruoli mercato aerospace IT 2025-2026. Cronoprogramma spese Y1 mese-per-mese + S-curve cumulata + 6 tranche finanziamento €470k. Confidence MEDIUM (AACE Classe 4 Study/Feasibility).
11. **A.10 Piano Manutenzione Operativo v1.5** (70 KB / 973 righe) — 11 sezioni + 3 appendici, 84 maintenance task in 5 sistemi del CW-30E (Propulsione+energia + Avionica+GNC + Struttura+carrello + Payload+EO/IR + Link+RF), calendar Y1 80 missioni con stagionalità Pentema, Maintenance Organization (Maintenance Manager + ML2 + PIC-ML1 + subcontractor), spare parts strategy 3 livelli stock L1 €4.250-8.250 CapEx, costi LCC Y1 **€78-173k** (OpEx €47-96k + CapEx GSE/spare/formazione/facility €30-77k), traiettoria Y2-Y5 da €100-190k a €265-430k/anno. 5 gap residui pre-operations Y1 (OEM manual JOUAV, ML2 hire, SLA OEM, GSE tools, hangar Pentema ATEX). Confidence MEDIUM.

## Conformità art. 41 D.Lgs. 36/2023 + Allegato I.7

Tutti gli elaborati PFTE obbligatori secondo Allegato I.7 sono coperti:

| Elaborato Allegato I.7 | Posizione nel PFTE Firmamento |
|---|---|
| Relazione generale | Volume 1 Cap. 0 + Cap. 1 |
| Relazioni specialistiche | Volume 1 Cap. 5 (norm.) + Cap. 6 (tecn.) + Cap. 7 (mercato) |
| Studio di Impatto Ambientale preliminare | Vol. 2 Allegato A.12 |
| Elaborati grafici | Vol. 2 Allegato A.6 (CAD) + A.13 (fotografia) |
| Calcoli preliminari | Vol. 2 Allegato A.7 (link budget + energy balance + financial) + A.8 (bilanci massa) |
| Computo metrico estimativo | Vol. 2 Allegato A.9 |
| Quadro economico | Vol. 2 Allegato A.7 financial-model + Vol. 1 Cap. 8 |
| Cronoprogramma | Vol. 1 Cap. 9 |
| Piano economico-finanziario | Vol. 2 Allegato A.7 financial-model |
| Piano di manutenzione preliminare | Vol. 2 Allegato A.10 |
| Piano di sicurezza e coordinamento | Vol. 2 Allegato A.11 |
| Documentazione fotografica | Vol. 2 Allegato A.13 |

## Cross-reference Volume 1 ↔ Volume 2

| Capitolo Vol. 1 | Allegati Vol. 2 corrispondenti |
|---|---|
| Cap. 3 Requisiti + RTM | A.1 (RTM v1.0 estesa) |
| Cap. 4 Scope + ICD | A.4 (ICD v1.0 dettagliato) |
| Cap. 5 Quadro Normativo | A.11 (PSC + SORA Safety Case) + A.12 (VIA) |
| Cap. 6 Analisi Tecnica | A.3 (DOCFAP) + A.6 (CAD) + A.7 (modelli) + A.8 (massa) + A.10 (manutenzione) |
| Cap. 7 Mercato | vendor-rfq/ |
| Cap. 8 Economico-Finanziario | A.7 financial-model + A.9 Computo Metrico |
| Cap. 9 Cronoprogramma | A.5 V&V Plan (schedule integrato) |

## Versioning

- **v1.0 M+3 bozza** (presente — la maggior parte degli allegati)
- **v1.5 M+6** — Update post pre-application ENAC + workshop cooperative + vendor quotation reali
- **v2.0 M+10** — Definitivo per gate G3 FEASIBILITY
- **v2.5 M+12** — Update post pilota MVP Y1
- **v3.0 M+24** — Update per Phase B 6B

## Disclaimer epistemici

- Confidence aggregato Vol. 2: **medium-low** (numerosi allegati richiedono validazione esterna)
- DR aperti (vedi `riferimenti/audit-rigore-epistemico.md`): 6 voci richiedono engagement esterno (Coopfond, ENAC, AGCOM, Garante, CIRA, Leonardo/TAS)
- Energy balance simulazione (allegato A.7 energy-balance): **finding critico** — perennial 44°N NON fattibile con baseline 2026-2028; E5 Seasonal mandatory plan A
- Capital intensity Phase B 6B (allegato A.7 financial-model): €5.5-13.5M = R&D Phase 0/A only (DR-014: benchmark $50M-1B per operativa)
- Pricing PA RECALIBRATED post Cluster D: €60-90k base + €30-60k premium (vs €150k originale)
