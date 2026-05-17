# Studio di Fattibilità HALE/VTOL — INDICE UNICO CROSS-VOLUME

> **Firmamento Technologies** — bando Cooding Prototypes (Coopfond / Legacoop)
> Studio di Fattibilità ex art. 41 D.Lgs. 36/2023 + Allegato I.7
> Bozza M+3 (proiezione M+11 per gate G3 FEASIBILITY)
>
> **Caso pilota**: frazione di Pentema (Comune di Torriglia, GE) — area SNAI Valli Antola-Tigullio
> **Strategia**: Duale — Percorso 6A VTOL pilota (M+0-12) + Percorso 6B HALE R&D Phase B (M+24-48)

---

## Mappa rapida del documento

```
HALE/
├── studio-di-fattibilita/
│   ├── cap-00..11.md (Volume 1)
│   ├── allegati/A1..A13 (Volume 2)
│   └── volume-3-riferimenti/R1..R5 (Volume 3)
├── fonti/ (30 file MD + 26 PDF/DOCX originali — fonti normative + dati)
└── riferimenti/ (audit + visione + ricerche)
```

---

## VOLUME 1 — STUDIO (testuale)

| Cap. | Titolo | File | Pagine A4 stim. | Status |
|---|---|---|---|---|
| **0** | Sintesi Esecutiva | [`cap-00-sintesi-esecutiva.md`](../cap-00-sintesi-esecutiva.md) | 5-7 | ✅ |
| **1** | Inquadramento + Quadro Esigenziale | [`cap-01-inquadramento.md`](../cap-01-inquadramento.md) | 30 | ✅ |
| **2** | Stakeholder + SMART | [`cap-02-stakeholder-e-SMART.md`](../cap-02-stakeholder-e-SMART.md) | 35 | ✅ |
| **3** | Requisiti + RTM | [`cap-03-requisiti-e-RTM.md`](../cap-03-requisiti-e-RTM.md) | 32 | ✅ |
| **4** | Scope + ICD preliminare | [`cap-04-scope-e-ICD.md`](../cap-04-scope-e-ICD.md) | 38 | ✅ |
| **5** | Quadro Normativo + 15 showstopper aggiuntivi | [`cap-05-quadro-normativo.md`](../cap-05-quadro-normativo.md) | 40 | ✅ |
| **6** | Analisi Tecnica + energy balance updated | [`cap-06-analisi-tecnica.md`](../cap-06-analisi-tecnica.md) | 30 | ✅ |
| **7** | Mercato + Business Case + Cluster D | [`cap-07-mercato-e-business-case.md`](../cap-07-mercato-e-business-case.md) | 35 | ✅ |
| **8** | Economico-Finanziario | [`cap-08-economico-finanziario.md`](../cap-08-economico-finanziario.md) | 18 | ✅ |
| **9** | Cronoprogramma + Gate + Sliding Timeline | [`cap-09-cronoprogramma-e-gate.md`](../cap-09-cronoprogramma-e-gate.md) | 25 | ✅ |
| **10** | Raccomandazione di Gate + Hold default | [`cap-10-raccomandazione-di-gate.md`](../cap-10-raccomandazione-di-gate.md) | 18 | ✅ |
| **11** | Roadmap post-fattibilità + B2-relaxed | [`cap-11-roadmap-post-fattibilita.md`](../cap-11-roadmap-post-fattibilita.md) | 30 | ✅ |
| **Tot Vol. 1** | | | **~336 pp** | ✅ |

---

## VOLUME 2 — ALLEGATI TECNICI

| All. | Titolo | Path | Output | Status |
|---|---|---|---|---|
| **A.1** | Requirements Traceability Matrix v1.0 | [`allegati/A1-RTM/`](../allegati/A1-RTM/) | 4 file (.md + .xlsx 14 sheet + .csv + .py); 279 record | ✅ |
| **A.2** | Risk Register consolidato v1.0 | [`allegati/A2-Risk-Register/`](../allegati/A2-Risk-Register/) | 4 file (.md + .xlsx 22 sheet + .csv + .py); 116 rischi | ✅ |
| **A.3** | DOCFAP — Trade Studies | [`allegati/A3-Trade-Studies/`](../allegati/A3-Trade-Studies/) | 1 .md | ✅ |
| **A.4** | Interface Control Document v1.0 | [`allegati/A4-ICD/`](../allegati/A4-ICD/) | 3 file (.md + .xlsx 13 sheet + .py); 59 interfacce | ✅ |
| **A.5** | Verification & Validation Plan v1.0 | [`allegati/A5-VV-Plan/`](../allegati/A5-VV-Plan/) | 3 file (.md + .xlsx 7 sheet + .py); 71 SyR | ✅ |
| **A.6** | Schemi CAD del concept | [`allegati/A6-CAD/`](../allegati/A6-CAD/) | 1 README (placeholder; CAD binari in `/cad/`) | ✅ |
| **A.7** | Modelli di calcolo (3 modelli) | [`allegati/A7-Link-Budget/`](../allegati/A7-Link-Budget/) + [`energy-balance/`](../allegati/energy-balance/) + [`financial-model/`](../allegati/financial-model/) | (a) Link Budget Python + xlsx 11 sheet + report + 4 PNG; (b) Energy Balance Python + xlsx + CSV 365gg + 4 PNG + report; (c) Financial Model xlsx 10 sheet + Python | ✅ |
| **A.8** | Bilanci di Massa Preliminari | [`allegati/A8-Bilanci-Massa/`](../allegati/A8-Bilanci-Massa/) | 1 .md | ✅ |
| **A.9** | Computo Metrico Estimativo | [`allegati/A9-Computo-Metrico/`](../allegati/A9-Computo-Metrico/) | 1 .md | ✅ |
| **A.10** | Piano di Manutenzione Preliminare | [`allegati/A10-Piano-Manutenzione/`](../allegati/A10-Piano-Manutenzione/) | 1 .md | ✅ |
| **A.11** | PSC + SORA Safety Case Preliminary | [`allegati/A11-Safety-Case-SORA/`](../allegati/A11-Safety-Case-SORA/) | 1 .md | ✅ |
| **A.12** | Relazione VIA Preliminare | [`allegati/A12-VIA-preliminare/`](../allegati/A12-VIA-preliminare/) | 1 .md | ✅ |
| **A.13** | Documentazione Fotografica | [`allegati/A13-Documentazione-Fotografica/`](../allegati/A13-Documentazione-Fotografica/) | 1 .md (indice; foto da acquisire) | ✅ |
| **(extra)** | Vendor RFQ | [`allegati/vendor-rfq/`](../allegati/vendor-rfq/) | 4 file (.md template + cover letter + analysis + CSV) | ✅ |

---

## VOLUME 3 — RIFERIMENTI BIBLIOGRAFICI

| Sez. | Titolo | File | Riferimenti |
|---|---|---|---|
| **R.1** | Bibliografia Normativa | [`R1-bibliografia-normativa.md`](../volume-3-riferimenti/R1-bibliografia-normativa.md) | 72 (N-01..72) |
| **R.2** | Bibliografia Tecnica | [`R2-bibliografia-tecnica.md`](../volume-3-riferimenti/R2-bibliografia-tecnica.md) | 80 (T-01..80) |
| **R.3** | Fonti Mercato + Competitor | [`R3-fonti-mercato-competitor.md`](../volume-3-riferimenti/R3-fonti-mercato-competitor.md) | ~50 (M+C+V+F) |
| **R.4** | Documenti SNAI + Territoriali | [`R4-documenti-SNAI-territoriali.md`](../volume-3-riferimenti/R4-documenti-SNAI-territoriali.md) | 58 (S-01..58) |
| **R.5** | Studi Accademici | [`R5-studi-accademici.md`](../volume-3-riferimenti/R5-studi-accademici.md) | 60 (A-01..60) |
| **Tot Vol. 3** | | | **~320 ref** |

---

## DOCUMENTI DI AUDIT E DEBITO

| Doc | Path | Contenuto |
|---|---|---|
| Audit Red Team Volume 1 | [`AUDIT-REDTEAM-VOLUME-1.md`](../AUDIT-REDTEAM-VOLUME-1.md) | 70+ critiche per capitolo |
| Audit Competitor | [`AUDIT-COMPETITOR-VOLUME-1.md`](../AUDIT-COMPETITOR-VOLUME-1.md) | Wargame scenari + survivability |
| Audit Regulatory | [`AUDIT-REGULATORY-VOLUME-1.md`](../AUDIT-REGULATORY-VOLUME-1.md) | 12 scenari blocco regolatorio |
| Audit Quality consolidato | [`AUDIT-QUALITY-VOLUME-1.md`](../AUDIT-QUALITY-VOLUME-1.md) | Sintesi 3 audit + 10 action items |
| Falsifying Obs addendum | [`FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md`](../FALSIFYING-OBSERVATIONS-M3-ADDENDUM.md) | 10 FO mancanti aggiunte |
| Audit rigore epistemico | [`/riferimenti/audit-rigore-epistemico.md`](../../riferimenti/audit-rigore-epistemico.md) | 124 claim auditati + 15 DR |
| DR research closure M+3 | [`/riferimenti/DR-research-closure-M3.md`](../../riferimenti/DR-research-closure-M3.md) | 9 DR processati |
| Visione strategica 10 anni | [`/riferimenti/visione-10-anni.md`](../../riferimenti/visione-10-anni.md) | 5 fasi + capital intensity scenarios |
| RESERVED rischi geopolitici | [`/riferimenti/RESERVED-rischi-geopolitici.md`](../../riferimenti/RESERVED-rischi-geopolitici.md) | 🔒 Accesso ristretto |

---

## FRAMEWORK OPERATIVO (`.claude/`)

| Componente | Path | Contenuto |
|---|---|---|
| Agenti esperti | `.claude/agents/` | 17 esperti di dominio (aerospace, regolatorio, finanziario, etc.) |
| Skill operative | `.claude/skills/` | 7 skill (feasibility framework, RTM, risk, trade study, link budget, gate review, epistemic rigor) |
| README | `.claude/README.md` | Catalogo agenti + skill + workflow patterns |

---

## FONTI ESTERNE SCARICATE

Path: `/fonti/` (root del repo)

- 26 documenti normativi/tecnici originali (PDF + DOCX)
- 30 file .md convertiti (~80 MB indicizzabile)
- Coverage: D.Lgs.36/2023, Reg.UE UAS, EASA SORA, ENAC, 3GPP NTN, ITU P.618, NASA SE Handbook, ENAC AAM BP, PSNAI, etc.

---

## STATISTICHE AGGREGATE

| Dimensione | Valore |
|---|---|
| **Capitoli Vol. 1** | 11/11 (100%) |
| **Allegati Vol. 2** | 13/13 (100%) + extra |
| **Sezioni Vol. 3** | 5/5 (100%) |
| **Audit avversariali** | 4 (RedTeam + Competitor + Regulatory + Quality) |
| **DR chiusi** | 9/15 (4 ✓ + 4 parz + 1 aperto + 6 esterni) |
| **Falsifying observations** | ~50+ totali distribuite |
| **Citazioni autoritative** | ~270 totali (Vol. 3) |
| **Mercati di mercato/competitor profiled** | 27 (Tier 1+EU+sub+Cluster D+Vendor) |
| **System Requirements** | 65 (Cap. 3 + A.1) |
| **Risk identified** | 116 (A.2) |
| **Interface Requirements** | 59 (A.4) |
| **NegR (Negative Requirements)** | 14 (Cap. 3 + A.1) |
| **Showstopper formali** | 5 (RSK-TEC-001/002/003 + RSK-REG-001 + RSK-FIN-001) |
| **Critical aggiuntivi** | 5-6 RSK-REG (post Cap.5 §5.16) |
| **Dimensione totale ripo** | ~3 GB (incluso file binari fonti + CAD) |
| **Dimensione documenti Studio** | ~3 MB Markdown indicizzabile |
| **Equivalente pagine A4** | ~400-500 pp Volume 1+2+3 |

---

## VERDETTO CONSOLIDATO M+3

> **Lo Studio di Fattibilità HALE/VTOL è formalmente completo (Vol. 1+2+3) per gate G3 FEASIBILITY** (M+10/M+11 proiezione).
>
> **Verdetto operativo**:
> - **Percorso 6A (VTOL pilota Pentema)**: HOLD CON PIANO REGOLATORIO RAFFORZATO (scenario base P 45-60%) → re-review M+13-16; GO pieno P 5-15%
> - **Percorso 6B (HALE R&D Phase B)**: HOLD CON CRITERI DI USCITA ESTREMAMENTE STRINGENTI; base rate 0% HALE solari commerciali in 22 anni; pivot strutturale verso "operatore servizi su prime contractor"
>
> **Confidence aggregato**: MEDIUM-LOW (richiede engagement esterno per chiusura DR-002, 003, 004, 005, 010 + LoI Regione + workshop cooperative).

---

## VERSIONING

- **v1.0 M+3** (presente) — Sprint completo (Vol. 1+2+3 + audit + modelli + RFQ)
- **v1.5 M+6** — Update post pre-application ENAC + workshop cooperative + vendor quotation
- **v2.0 M+10** — Definitivo per gate G3 FEASIBILITY
- **v2.5 M+12** — Update post gate G3 + Y1 MVP launch
- **v3.0 M+24** — Update per gate G5 Phase B 6B

---

## CONTACTS + LICENSE

**Soggetto proponente**: Firmamento Technologies S.r.l.
**Documento**: Studio di Fattibilità HALE/VTOL per Aree Interne
**Bando**: Cooding Prototypes (Coopfond / Legacoop)
**Versione**: M+3 bozza
**Data**: 17 maggio 2026
**Confidentiality**: Documento di lavoro — distribuzione interna + stakeholder formali. Sezioni RESERVED ad accesso ristretto.

---

## QUICK START NAVIGATION

**Per uno stakeholder esterno che apre il documento per la prima volta**:

1. Leggere [`cap-00-sintesi-esecutiva.md`](../cap-00-sintesi-esecutiva.md) (5 min)
2. Leggere [`cap-10-raccomandazione-di-gate.md`](../cap-10-raccomandazione-di-gate.md) §10.0bis (verdetto realistico)
3. Riferimento `master-deliverables/CdA-1pager.md` per board summary
4. Approfondire capitoli su interesse specifico

**Per un finanziatore** (Coopfond, FESR, PNRR):
1. Cap. 0 + Cap. 7 (mercato) + Cap. 8 (finanziario) + Cap. 10 (verdetto)
2. Vol. 2 A.7 financial-model (Excel)
3. Vol. 2 A.9 Computo Metrico

**Per un regolatore** (ENAC, EASA, AGCOM, Garante):
1. Cap. 5 + Vol. 2 A.11 SORA + A.12 VIA
2. Vol. 3 R.1 (bibliografia normativa)

**Per un partner tecnico** (CIRA, Polito, TAS):
1. Cap. 6 + Vol. 2 A.1 RTM + A.4 ICD + A.7 modelli
2. Vol. 3 R.2 (bibliografia tecnica) + R.5 (accademica)
