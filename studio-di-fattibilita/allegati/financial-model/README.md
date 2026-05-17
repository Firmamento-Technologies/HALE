# Modello Finanziario HALE/VTOL Firmamento Technologies

**Versione:** M+3 bozza (post Audit + DR research closure)
**Data:** 17 maggio 2026
**Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (PFTE: Piano Economico-Finanziario)

## File

- `HALE-Financial-Model-M3.xlsx` (22.7 KB, 10 sheet): modello finanziario completo
- `build_financial_model.py` (42 KB): script Python riproducibile (openpyxl)

## Sheet del workbook

| # | Sheet | Contenuto |
|---|---|---|
| 0 | Cover | Disclaimer epistemici + struttura |
| 1 | CapEx_Y1 | Quadro Economico Y1 (A + B + IVA), formato art. 41 |
| 2 | OpEx_Y2+ | OpEx run-rate Y2-Y5 con evoluzione scale-up |
| 3 | Revenue | Revenue Y1-Y5 RECALIBRATED post Cluster D |
| 4 | Cash_Flow | Cash flow Y1-Y5 + cumulato (conditional formatting) |
| 5 | NPV_IRR | NPV / IRR / Payback / ROI 10y |
| 6 | Sensitivity | Sensitivity su 7 driver primari |
| 7 | Scenarios | Worst / Base / Best con probabilità |
| 8 | Funding_Mix | Mix finanziamenti Y1 + Phase B 6B |
| 9 | Quadro_Economico_art41 | QE formato Codice Contratti compatto |

## KPI principali (scenario base)

- **CapEx Y1 baseline**: €1.4M (range €0.97M-€1.96M)
- **OpEx Y2 run-rate**: €1.18M (incl. +3 FTE regulatory post Cap.5 §5.17)
- **Revenue Y1 RECALIBRATED**: €260k (vs €355-405k originale; falsificato da Cluster D)
- **Break-even cumulato**: Y4-Y5 (scenario base) / Y6-Y7 (sliding timeline)
- **NPV 10y (WACC 12%)**: +€3.5M scenario base
- **IRR 10y**: 18-22% scenario base
- **Payback**: 5 anni scenario base

## Disclaimer epistemici critici

1. **Confidence aggregato medio**: MEDIUM-LOW (numerose stime non triangolate)
2. **Pricing PA recalibrato**: €75k/anno (vs €150k Cap.7 originale, falsificato da Cluster D)
3. **CapEx Y1 reale atteso sliding timeline**: €2.5-3.5M (vs €0.7-2M nominale)
4. **Phase B 6B €5.5-13.5M = R&D Phase 0/A only** (DR-014: benchmark $50M-1B operativa commerciale)
5. **Y6-Y10 sono extrapolazioni** (confidence LOW)
6. **Investment-grade richiede**: chiusura DR (Coopfond, ENAC, AGCOM, vendor quotation, CIRA) + LoI firmate + modello Monte Carlo

## Riproducibilità

Per rigenerare il workbook:

```bash
cd /home/user/HALE/studio-di-fattibilita/allegati/financial-model
pip install openpyxl
python3 build_financial_model.py
```

Output: `HALE-Financial-Model-M3.xlsx`

## Workflow di utilizzo

1. **Aprire il file** in Excel / LibreOffice / Google Sheets (formule supportate)
2. **Modificare gli input baseline** nello script Python (sezione `ASSUMPTIONS`) per re-run scenari
3. **Validare con benchmark esterni** (RFQ vendor quotation, LoI Regione, contratti reali) nella sezione confidence
4. **Update post-validation**: re-genera workbook con nuovi numeri reali

## Cross-reference

- Vedi `studio-di-fattibilita/cap-08-economico-finanziario.md` per il testo dello Studio
- Vedi `studio-di-fattibilita/cap-07-mercato-e-business-case.md` §7.4.4-5 per pricing Cluster D
- Vedi `riferimenti/DR-research-closure-M3.md` per i benchmark capital intensity DR-014
- Vedi `studio-di-fattibilita/cap-09-cronoprogramma-e-gate.md` §9.12 per sliding timeline
- Vedi `studio-di-fattibilita/cap-10-raccomandazione-di-gate.md` §10.0bis per verdetto realistico

## Note legali

Il presente modello è una **bozza M+3** per uso interno e per gate review G3 (M+10/M+11). **NON costituisce business plan investment-grade** né documento contrattuale. Per uso esterno con finanziatori istituzionali richiede:
- Validazione esterna (RINA, DNV, ente terzo)
- Modello Monte Carlo + scenario analysis estesi
- LoI/contratti firmati per validare revenue
- Quotation vendor reali per validare CapEx
- Audit revisore contabile per conformità IFRS/OIC
