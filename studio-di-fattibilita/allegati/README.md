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
| **A.1** | [`A1-RTM/`](A1-RTM/) | Requirements Traceability Matrix v1.0 completa | ⏳ subagent |
| **A.2** | [`A2-Risk-Register/`](A2-Risk-Register/) | Risk Register consolidato v1.0 | ⏳ subagent |
| **A.3** | [`A3-Trade-Studies/`](A3-Trade-Studies/) | DOCFAP — Documento Fattibilità Alternative Progettuali | ✅ |
| **A.4** | [`A4-ICD/`](A4-ICD/) | Interface Control Document preliminare v1.0 | ✅ |
| **A.5** | [`A5-VV-Plan/`](A5-VV-Plan/) | Verification & Validation Plan v1.0 | ⏳ subagent |
| **A.6** | [`A6-CAD/`](A6-CAD/) | Schemi/disegni CAD del concept (placeholder; CAD binari in `/cad/`) | ✅ |
| **A.7** | [`A7-Link-Budget/`](A7-Link-Budget/) + [`energy-balance/`](energy-balance/) + [`financial-model/`](financial-model/) | Modelli di calcolo (link budget telecom, energy balance HALE, modello finanziario Excel) | ✅ (energy + financial); ⏳ link budget subagent |
| **A.8** | [`A8-Bilanci-Massa/`](A8-Bilanci-Massa/) | Bilanci di massa preliminari (6A + 6B) | ✅ |
| **A.9** | [`A9-Computo-Metrico/`](A9-Computo-Metrico/) | Computo Metrico Estimativo ground segment | ✅ |
| **A.10** | [`A10-Piano-Manutenzione/`](A10-Piano-Manutenzione/) | Piano di Manutenzione preliminare | ✅ |
| **A.11** | [`A11-Safety-Case-SORA/`](A11-Safety-Case-SORA/) | PSC operativo + SORA Safety Case preliminare | ✅ |
| **A.12** | [`A12-VIA-preliminare/`](A12-VIA-preliminare/) | Relazione VIA preliminare | ✅ |
| **A.13** | [`A13-Documentazione-Fotografica/`](A13-Documentazione-Fotografica/) | Documentazione fotografica del contesto (placeholder, foto da acquisire) | ✅ |

## Allegati aggiuntivi (operativi)

| Allegato extra | Path | Contenuto |
|---|---|---|
| **A.x — Vendor RFQ** | [`vendor-rfq/`](vendor-rfq/) | RFQ template + cover letter + analisi quotation JOUAV vs Tekever |

## Status complessivo M+3

- ✅ **10/13 allegati Vol. 2** completati dalla main session
- ⏳ **3 allegati** in lavoro via subagent (A.1 RTM, A.2 Risk Register, A.5 V&V + A.7 Link Budget)

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
