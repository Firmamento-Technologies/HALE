# Studio di Fattibilità HALE/VTOL, Indice Unico Cross-Volume

> **Firmamento Technologies**, bando Cooding Prototypes (Coopfond / Legacoop)
> Studio di Fattibilità ex art. 41 D.Lgs. 36/2023 + Allegato I.7
> Bozza M+3 (proiezione M+11 per gate G3 FEASIBILITY)
>
> **Caso pilota**: frazione di Pentema (Comune di Torriglia, GE), area SNAI Valli Antola-Tigullio
> **Strategia**: duale, Percorso 6A VTOL pilota (M+0-12) e Percorso 6B HALE R&D Phase B (M+24-48)

---

## Mappa rapida del documento

```
HALE/
├── studio-di-fattibilita/
│ ├── cap-00..11.md (Volume 1)
│ ├── allegati/A1..A13 (Volume 2)
│ └── volume-3-riferimenti/R1..R5 (Volume 3)
├── fonti/ (30 file MD + 26 PDF/DOCX originali, fonti normative e dati)
└── riferimenti/ (audit, visione, ricerche)
```

---

## VOLUME 1, STUDIO (testuale)

Il primo volume raccoglie gli undici capitoli che costituiscono il corpo testuale dello Studio, dalla Sintesi Esecutiva alla Roadmap post-fattibilità. La tabella seguente indica titolo, file e pagine A4 stimate per ciascun capitolo.

| Cap. | Titolo | File | Pagine A4 stim. | Status |
|---|---|---|---|---|
| **0** | Sintesi Esecutiva | [`cap-00-sintesi-esecutiva.md`](../cap-00-sintesi-esecutiva.md) | 5-7 | OK |
| **1** | Inquadramento + Quadro Esigenziale | [`cap-01-inquadramento.md`](../cap-01-inquadramento.md) | 30 | OK |
| **2** | Stakeholder + SMART | [`cap-02-stakeholder-e-SMART.md`](../cap-02-stakeholder-e-SMART.md) | 35 | OK |
| **3** | Requisiti + RTM | [`cap-03-requisiti-e-RTM.md`](../cap-03-requisiti-e-RTM.md) | 32 | OK |
| **4** | Scope + ICD preliminare | [`cap-04-scope-e-ICD.md`](../cap-04-scope-e-ICD.md) | 38 | OK |
| **5** | Quadro Normativo + 15 showstopper aggiuntivi | [`cap-05-quadro-normativo.md`](../cap-05-quadro-normativo.md) | 40 | OK |
| **6** | Analisi Tecnica + energy balance updated | [`cap-06-analisi-tecnica.md`](../cap-06-analisi-tecnica.md) | 30 | OK |
| **7** | Mercato + Business Case + Cluster D | [`cap-07-mercato-e-business-case.md`](../cap-07-mercato-e-business-case.md) | 35 | OK |
| **8** | Economico-Finanziario | [`cap-08-economico-finanziario.md`](../cap-08-economico-finanziario.md) | 18 | OK |
| **9** | Cronoprogramma + Gate + Sliding Timeline | [`cap-09-cronoprogramma-e-gate.md`](../cap-09-cronoprogramma-e-gate.md) | 25 | OK |
| **10** | Raccomandazione di Gate + Hold default | [`cap-10-raccomandazione-di-gate.md`](../cap-10-raccomandazione-di-gate.md) | 18 | OK |
| **11** | Roadmap post-fattibilità + B2-relaxed | [`cap-11-roadmap-post-fattibilita.md`](../cap-11-roadmap-post-fattibilita.md) | 30 | OK |
| **Tot Vol. 1** | | | **~336 pp** | OK |

---

## VOLUME 2, ALLEGATI TECNICI

Tredici allegati tecnici accompagnano il Volume 1 con i dati operativi: RTM, Risk Register, ICD, V&V Plan, schemi CAD, modelli di calcolo, bilanci di massa, Computo Metrico Estimativo, Piano di Manutenzione, Safety Case SORA, VIA preliminare e documentazione fotografica.

| All. | Titolo | Path | Output | Status |
|---|---|---|---|---|
| **A.1** | Requirements Traceability Matrix v1.0 | [`allegati/A1-RTM/`](../allegati/A1-RTM/) | 4 file (.md +.xlsx 14 sheet +.csv +.py); 279 record | OK |
| **A.2** | Risk Register consolidato v1.0 | [`allegati/A2-Risk-Register/`](../allegati/A2-Risk-Register/) | 4 file (.md +.xlsx 22 sheet +.csv +.py); 116 rischi | OK |
| **A.3** | DOCFAP, Trade Studies | [`allegati/A3-Trade-Studies/`](../allegati/A3-Trade-Studies/) | 1.md | OK |
| **A.4** | Interface Control Document v1.0 | [`allegati/A4-ICD/`](../allegati/A4-ICD/) | 3 file (.md +.xlsx 13 sheet +.py); 59 interfacce | OK |
| **A.5** | Verification & Validation Plan v1.0 | [`allegati/A5-VV-Plan/`](../allegati/A5-VV-Plan/) | 3 file (.md +.xlsx 7 sheet +.py); 71 SyR | OK |
| **A.6** | Schemi CAD del concept | [`allegati/A6-CAD/`](../allegati/A6-CAD/) | 1 README (placeholder; CAD binari in `/cad/`) | OK |
| **A.7** | Modelli di calcolo (3 modelli) | [`allegati/A7-Link-Budget/`](../allegati/A7-Link-Budget/) + [`energy-balance/`](../allegati/energy-balance/) + [`financial-model/`](../allegati/financial-model/) | (a) Link Budget Python + xlsx 11 sheet + report + 4 PNG; (b) Energy Balance Python + xlsx + CSV 365gg + 4 PNG + report; (c) Financial Model xlsx 10 sheet + Python | OK |
| **A.8** | Bilanci di Massa Preliminari | [`allegati/A8-Bilanci-Massa/`](../allegati/A8-Bilanci-Massa/) | 1.md | OK |
| **A.9** | Computo Metrico Estimativo | [`allegati/A9-Computo-Metrico/`](../allegati/A9-Computo-Metrico/) | 1.md | OK |
| **A.10** | Piano di Manutenzione Preliminare | [`allegati/A10-Piano-Manutenzione/`](../allegati/A10-Piano-Manutenzione/) | 1.md | OK |
| **A.11** | PSC + SORA Safety Case Preliminary | [`allegati/A11-Safety-Case-SORA/`](../allegati/A11-Safety-Case-SORA/) | 1.md | OK |
| **A.12** | Relazione VIA Preliminare | [`allegati/A12-VIA-preliminare/`](../allegati/A12-VIA-preliminare/) | 1.md | OK |
| **A.13** | Documentazione Fotografica | [`allegati/A13-Documentazione-Fotografica/`](../allegati/A13-Documentazione-Fotografica/) | 1.md (indice; foto da acquisire) | OK |
| **(extra)** | Vendor RFQ | [`allegati/vendor-rfq/`](../allegati/vendor-rfq/) | 4 file (.md template + cover letter + analysis + CSV) | OK |

---

## VOLUME 3, RIFERIMENTI BIBLIOGRAFICI

Il terzo volume documenta le fonti su cinque assi: normativo, tecnico, mercato-competitor, territoriale SNAI e accademico, per un totale di circa 320 riferimenti.

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

A corredo del corpo principale, lo Studio ospita gli atti dei quattro cicli di review critica indipendente, un addendum di Falsifying Observations, l'audit di rigore epistemico con i Debiti di Rigore, la visione decennale e il dossier riservato sui rischi geopolitici.

| Doc | Path | Contenuto |
|---|---|---|
| review critica Volume 1 | [la review critica interna](../review critica interna) | 70+ critiche per capitolo |
| Audit Competitor | [l'analisi competitor interna](../analisi competitor interna) | Wargame scenari + survivability |
| Audit Regulatory | [la review regolatoria interna](../review regolatoria interna) | 12 scenari blocco regolatorio |
| Audit Quality consolidato | [l'audit qualita interno](../audit qualita interno) | Sintesi 3 audit + 10 action items |
| Falsifying Obs addendum | [addendum falsifying observations](../addendum falsifying observations) | 10 FO mancanti aggiunte |
| Audit rigore epistemico | [`/riferimenti/audit-rigore-epistemico.md`](../../riferimenti/audit-rigore-epistemico.md) | 124 claim auditati + 15 DR |
| DR research closure M+3 | [`/riferimenti/DR-research-closure-M3.md`](../../riferimenti/DR-research-closure-M3.md) | 9 DR processati |
| Visione strategica 10 anni | [`/riferimenti/visione-10-anni.md`](../../riferimenti/visione-10-anni.md) | 5 fasi + capital intensity scenarios |
| RESERVED rischi geopolitici | [`/riferimenti/RESERVED-rischi-geopolitici.md`](../../riferimenti/RESERVED-rischi-geopolitici.md) | Accesso ristretto |

---

## METODOLOGIE INTERNE DI LAVORO

Lo Studio è stato sviluppato applicando un framework metodologico interno che integra consulenze specialistiche per dominio (aerospaziale, regolatorio, finanziario, di mercato, ambientale) e metodologie operative consolidate (feasibility framework PFTE, RTM, risk register, trade study DOCFAP, link budget, gate review checklist, rigore epistemico). Le metodologie sono coerenti con NASA SE Handbook Rev 2 e con la prassi italiana di art. 41 D.Lgs. 36/2023.


## FONTI ESTERNE SCARICATE

Le fonti esterne risiedono in `/fonti/` (root del repo): 26 documenti originali (PDF + DOCX), 30 file `.md` convertiti per circa 80 MB indicizzabile. La copertura tematica comprende D.Lgs.36/2023, Reg.UE UAS, EASA SORA, ENAC, 3GPP NTN, ITU P.618, NASA SE Handbook, ENAC AAM BP e PSNAI.

---

## STATISTICHE AGGREGATE

| Dimensione | Valore |
|---|---|
| **Capitoli Vol. 1** | 11/11 (100%) |
| **Allegati Vol. 2** | 13/13 (100%) + extra |
| **Sezioni Vol. 3** | 5/5 (100%) |
| **Review critiche indipendenti** | 4 |
| **DR chiusi** | 9/15 (4 OK + 4 parz + 1 aperto + 6 esterni) |
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

Lo Studio di Fattibilità HALE/VTOL risulta formalmente completo (Vol. 1+2+3) per il gate G3 FEASIBILITY, in proiezione M+10/M+11. Sul piano operativo, il verdetto si articola in due binari distinti.

Per il Percorso 6A (VTOL pilota Pentema) lo scenario base è HOLD CON PIANO REGOLATORIO RAFFORZATO (P 45-60%), con re-review prevista in finestra M+13-16; un GO pieno resta possibile con probabilità 5-15%.

Per il Percorso 6B (HALE R&D Phase B) prevale HOLD CON CRITERI DI USCITA ESTREMAMENTE STRINGENTI: il base rate degli HALE solari commerciali è pari a 0% negli ultimi 22 anni e impone un pivot strutturale verso il modello "operatore di servizi su prime contractor".

Il confidence aggregato è MEDIUM-LOW: la chiusura richiede engagement esterno su DR-002, 003, 004, 005, 010 oltre alla LoI Regione e al workshop cooperative.

---

## VERSIONING

La traiettoria di versionamento prevede cinque tappe successive. La v1.0 M+3, attualmente in vigore, raccoglie lo sprint completo (Volume 1, 2 e 3, audit, modelli e RFQ). La v1.5 M+6 introdurrà gli aggiornamenti post pre-application ENAC, workshop cooperative e vendor quotation. La v2.0 M+10 sarà la versione definitiva per il gate G3 FEASIBILITY, seguita dalla v2.5 M+12 post gate G3 e Y1 MVP launch, e infine dalla v3.0 M+24 in vista del gate G5 Phase B 6B.

---

## CONTATTI E LICENZA

**Soggetto proponente**: Firmamento Technologies S.r.l.
**Documento**: Studio di Fattibilità HALE/VTOL per Aree Interne
**Bando**: Cooding Prototypes (Coopfond / Legacoop)
**Versione**: M+3 bozza
**Data**: 17 maggio 2026
**Confidenzialità**: Documento di lavoro, distribuzione interna e stakeholder formali. Sezioni RESERVED ad accesso ristretto.

---

## QUICK START NAVIGATION

Per uno stakeholder esterno che apre il documento per la prima volta, il percorso suggerito parte dalla Sintesi Esecutiva ([`cap-00-sintesi-esecutiva.md`](../cap-00-sintesi-esecutiva.md), circa 5 minuti di lettura), prosegue con la Raccomandazione di Gate ([`cap-10-raccomandazione-di-gate.md`](../cap-10-raccomandazione-di-gate.md) §10.0bis, verdetto realistico) e si chiude con il board summary in `master-deliverables/CdA-1pager.md`. Da qui, l'approfondimento sui capitoli di interesse specifico è demandato al lettore.

Per un finanziatore (Coopfond, FESR, PNRR) la sequenza prioritaria comprende Cap. 0, Cap. 7 (mercato), Cap. 8 (finanziario) e Cap. 10 (verdetto), affiancati da Vol. 2 A.7 financial-model (Excel) e Vol. 2 A.9 Computo Metrico.

Per un regolatore (ENAC, EASA, AGCOM, Garante) la lettura mirata è Cap. 5 con Vol. 2 A.11 SORA e A.12 VIA, integrata da Vol. 3 R.1 (bibliografia normativa).

Per un partner tecnico (CIRA, Polito, TAS) il riferimento è Cap. 6 con Vol. 2 A.1 RTM, A.4 ICD e A.7 modelli, supportati da Vol. 3 R.2 (bibliografia tecnica) e R.5 (accademica).
