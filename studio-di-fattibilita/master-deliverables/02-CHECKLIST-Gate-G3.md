# Master Checklist, Gate G3 FEASIBILITY (M+10/M+11)

> Studio di Fattibilità HALE/VTOL Firmamento Technologies
> Master Deliverable, checklist completa per Gate Review G3

## Premessa

Il **Gate G3 FEASIBILITY** è il gate decisionale primario dello Studio (M+10/M+11). Il verdetto target si declina su quattro esiti possibili: Go, Go Condizionato, Hold, No-Go, applicati separatamente a ciascuno dei due percorsi. Questa checklist è lo strumento operativo del Board per verificare la prontezza al gate.

Il verdetto base atteso alla milestone M+3 (vedi Cap. 10 §10.0bis) prevede HOLD CON PIANO REGOLATORIO RAFFORZATO per il Percorso 6A (P 45-60%), con re-review M+13-16, e HOLD CON CRITERI DI USCITA STRINGENTI per il Percorso 6B, accompagnato da un pivot strutturale verso il modello prime contractor.

---

## A. Entry criteria documentali (PFTE conforme art. 41 + Allegato I.7)

### Volume 1, Studio

- [x] Cap. 0 Sintesi Esecutiva
- [x] Cap. 1 Inquadramento + Quadro Esigenziale
- [x] Cap. 2 Stakeholder + SMART
- [x] Cap. 3 Requisiti + RTM (v0.5 → v1.0 in Vol. 2)
- [x] Cap. 4 Scope + ICD preliminare
- [x] Cap. 5 Quadro Normativo + 15 showstopper aggiuntivi
- [x] Cap. 6 Analisi Tecnica + energy balance updated
- [x] Cap. 7 Mercato + Business Case + Cluster D
- [x] Cap. 8 Economico-Finanziario
- [x] Cap. 9 Cronoprogramma + Gate + Sliding Timeline
- [x] Cap. 10 Raccomandazione di Gate + Hold default
- [x] Cap. 11 Roadmap post-fattibilità + B2-relaxed

### Volume 2, Allegati Tecnici (13)

- [x] A.1 RTM v1.0 (279 record)
- [x] A.2 Risk Register v1.0 (116 rischi)
- [x] A.3 DOCFAP Trade Studies
- [x] A.4 ICD v1.0 (59 interfacce)
- [x] A.5 V&V Plan v1.0
- [x] A.6 CAD placeholder (file binari in `/cad/`)
- [x] A.7 Modelli di calcolo (energy balance + link budget + financial)
- [x] A.8 Bilanci di Massa Preliminari
- [x] A.9 Computo Metrico Estimativo
- [x] A.10 Piano di Manutenzione Preliminare
- [x] A.11 PSC + SORA Safety Case Preliminary
- [x] A.12 VIA Preliminare
- [x] A.13 Documentazione Fotografica (indice; foto da acquisire)

### Volume 3, Riferimenti (5)

- [x] R.1 Bibliografia Normativa (72 ref)
- [x] R.2 Bibliografia Tecnica (80 ref)
- [x] R.3 Fonti Mercato + Competitor (~50 ref)
- [x] R.4 Documenti SNAI Territoriali (58 ref)
- [x] R.5 Studi Accademici (60 ref)

---

## B. Criteri tecnici (Cap. 3 §3.2)

| Criterio | Soglia GO 6A | Soglia GO 6B condizionato | Status M+3 |
|---|---|---|---|
| Concept architettura definita | OK Cap. 6.1 | OK Cap. 6.1 | OK |
| Performance preliminare verificata | Autonomia ≥ 4h, payload ≥ 4 kg, copertura ≥ 30 km | Energy balance dicembre 21 a 44°N margine ≥ 30% | OK 6A; NO 6B (margine -50.1%, fallback E5 mandatory) |
| FMECA + FTA preliminari | OK Vol. 2 A.2 | OK Vol. 2 A.2 | OK |
| Risk Register top-10 con mitigation | Nessun rischio rosso senza piano | RSK-TEC-001/002 con piano R&D | OK (vedi mitigation A.2) |
| TRL minimo subsistemi | ≥ 8 (commerciali) | ≥ 4 (subsystem critici) | OK 6A (TRL 8-9 JOUAV); warning 6B (TRL 3-4) |

---

## C. Criteri regolatori (Cap. 3 §3.2.2 + Cap. 5)

| Criterio | Soglia GO 6A | Soglia GO 6B | Status M+3 | DR-XXX |
|---|---|---|---|---|
| Pre-application meeting ENAC | OK entro M+9 | OK in dialogo informale | pending DR-004 aperto | DR-004 |
| Stima SAIL preliminare | ≤ III | n/a | OK SAIL II-III preliminare (Cap. 5.1.5) | |
| Engagement EASA HAPS framework | n/a | OK richiesta RMT formalizzata | pending Y1+ | DR-008 |
| Conformità Reg. UE 2019/947 + 945 | OK dichiarata | OK dichiarata | OK | |
| Privacy DPIA preliminare pubblica | OK M+6 | OK M+6 | pending DR-006 parziale | DR-006 |
| AGCOM licensing spettro | OK M+9 | n/a Y1 | pending DR-005 | DR-005 |

---

## D. Criteri economico-finanziari (Cap. 3 §3.2.3 + Cap. 8)

| Criterio | Soglia GO 6A | Soglia GO 6B | Status M+3 |
|---|---|---|---|
| Quadro Economico art. 41 redatto | OK | OK (preliminare) | OK Vol. 2 A.9 + A.7 financial |
| Piano finanziario NPV/IRR/payback | NPV > 0 WACC 12%, payback < 6 anni | n/a (R&D phase) | OK NPV +€3.5M base, IRR 18-22%, payback 5y |
| Funding plan committed | ≥ 60% Y1-Y2 LoI Regione + Coopfond | ≥ 40% Phase B mix EDF + Horizon + PNRR + equity | pending DR-002 + LoI Regione |
| Modello finanziario Excel | OK con sensitivity | n/a | OK Vol. 2 A.7 financial-model |

---

## E. Criteri business (Cap. 3 §3.2.4 + Cap. 7)

| Criterio | Soglia GO 6A | Soglia GO 6B | Status M+3 |
|---|---|---|---|
| BMC + VPC redatti | OK Cap. 7 | OK Cap. 7 | OK |
| Anchor customer identificato | Regione Liguria con LoI | n/a | pending LoI |
| MVP definito | OK Cap. 7.9 | n/a | OK |
| Pricing model validato | OK con almeno 1 cliente | n/a | warning RECALIBRATED post Cluster D, validation richiesta |
| Cluster D analysis | OK riconosciuto vero competitor Y1 | n/a | OK Cap. 7 §7.4.4 |

---

## F. Criteri operativi/territoriali (Cap. 3 §3.2.5 + Cap. 1-2)

| Criterio | Soglia GO 6A | Status M+3 |
|---|---|---|
| Comune Torriglia disponibilità | OK delibera o LoI | pending engagement attivo |
| Cooperative pilota engagement | ≥ 8 su 10 cooperative aderenti | pending workshop M+3-6 |
| Comunità Pentema (14 abitanti) accettabilità sociale | OK workshop pubblico + DPIA pubblica | pending workshop M+3-6 |
| Pentema population verificato | 14 ISTAT confermato | OK DR-001 chiuso |

---

## G. Hard Conditions per Go pieno 6A (Cap. 10 §10.3.2)

P(AND tutte) realistico **5-15%** scenario ottimistico, da cui lo scenario base coincide con HOLD CON PIANO RAFFORZATO.

- [ ] **C1**: LoI o accordo formale Regione Liguria firmato entro M+9 pending
- [ ] **C2**: Autorizzazione SORA ENAC operativa entro M+9 pending
- [ ] **C3**: Mix funding ≥ 60% committed entro M+10 pending
- [ ] **C4**: ≥ 8 cooperative pilota su 10 confermano partecipazione formale entro M+6 pending
- [ ] **C5**: Pre-application meeting ENAC con feedback documentato entro M+3-6 pending

## H. Soft Conditions Go 6A (non-blocking)

- [ ] **S1**: DPIA pubblica preliminare entro M+6 pending
- [ ] **S2**: Vendor quotation confermato (JOUAV + Plan B Tekever) entro M+3 pending
- [ ] **S3**: Workshop comunità Pentema con feedback positivo entro M+6 pending
- [ ] **S4**: Partnership intent letter CIRA entro M+9 pending
- [ ] **S5**: Almeno 1 LoI per espansione 2nda regione SNAI entro M+12 pending

## I. Hard Conditions Go Phase B 6B (Gate G5 M+24)

- [ ] **C-6B-1**: Pilota 6A KPI gate G4 ≥ 3 contratti + €200k revenue + 0 FATAL pending (Y1)
- [ ] **C-6B-2**: Funding mix Phase B ≥ 50% committed entro M+24 pending
- [ ] **C-6B-3**: Engagement EASA RMT HAPS aperto / Special Condition in dialogo pending (M+12+)
- [ ] **C-6B-4**: Energy balance simulazione completa con scenari decisi (E5 Seasonal vs perennial) pending
- [ ] **C-6B-5**: Partnership formalizzata con almeno 1 prime contractor o partner R&D italiano pending (DR-010)

---

## J. Decisione Formale CdA + Sponsor (Cap. 10 §10.8.1)

La decisione formale richiede l'approvazione del CdA, di Coopfond e della Regione Liguria su otto deliberazioni puntuali.

- [ ] **D1**: Approvazione formale Studio di Fattibilità M+11
- [ ] **D2**: Approvazione **GO CONDIZIONATO** Percorso 6A (con 5 hard conditions C1-C5)
- [ ] **D3**: Approvazione **HOLD / GO CONDIZIONATO ESTREMO** Percorso 6B (subordinato G5)
- [ ] **D4**: Approvazione budget Y1 6A €2.5-3.5M (vs €0.7-2M nominale; include +3 FTE regulatory)
- [ ] **D5**: Approvazione engagement plan istituzionale Cap. 5.11.3
- [ ] **D6**: Approvazione versionamento RTM v1.0 → v3.5
- [ ] **D7**: Approvazione master schedule M+12 → M+48 (con sliding timeline §9.12)
- [ ] **D8**: Approvazione assunzione 3 FTE regulatory (CISO + DPO + Head Regulatory)

---

## K. Action Items Immediati Post-G3 (Cap. 10 §10.8.2)

### Per management Firmamento

1. [ ] Firma contratto Coopfond per Y1 entro M+11
2. [ ] Chiusura LoI Regione Liguria (DGR formale) entro M+12
3. [ ] Acquisto piattaforma VTOL (Plan A JOUAV o Plan B Tekever) entro M+12
4. [ ] Submission SORA application ENAC entro M+11
5. [ ] Workshop pubblico comunità Pentema (governance condivisa) entro M+12
6. [ ] Formalizzazione governance Firmamento + 10 cooperative (RTI vs JV vs contratto rete)

### Per team operativo

7. [ ] Set-up GS Pentema entro M+12
8. [ ] Training pilota UAS BVLOS entro M+12
9. [ ] DPIA pubblica preliminare submitted entro M+11

### Per Phase B 6B (preparatoria, no commitment manufacturing)

10. [ ] Engagement letter CIRA entro M+12
11. [ ] Engagement letter POLITO DIMEAS entro M+12
12. [ ] Position paper "Italian Stratospheric Sovereignty" pubblicato entro M+12
13. [ ] Engagement EASA Innovation Network entro M+9-12

---

## L. Composizione Board Gate G3 (Cap. 9 §9.7.2)

Il **Board allargato per G3 (FEASIBILITY GATE)** comprende la componente interna e quella esterna.

Internal:
- [ ] Project Manager (chair)
- [ ] Aerospace Systems Engineer (technical lead)
- [ ] Financial CFO Analyst
- [ ] Aviation Regulatory Counsel
- [ ] Business Model Strategist

External:
- [ ] Rappresentante Regione Liguria
- [ ] Rappresentante Coopfond
- [ ] Rappresentante cooperative (Fabrica capofila)
- [ ] **Independent reviewer** (consultant aerospace senior o ente terzo, es. RINA, per validation indipendente)
- [ ] Osservatore ENAC (su invito informale)

---

## M. Documentazione Output Post-G3

Output formali da produrre al gate review:

- [ ] Gate Review Package (template Cap. 9 §9.7.5)
- [ ] Verbale Decisione Formale
- [ ] Action Items List
- [ ] Risk Register Update v1.1 (post G3)
- [ ] RTM v1.1 (post G3 review)
- [ ] Master Schedule Update (nominal + sliding)
- [ ] Communication Plan Post-G3 (stakeholder + community)
- [ ] Press release (se applicabile, con scope ridotto = solo GO 6A)

---

## N. Falsifying Observations al Gate

Trigger di scenari alternativi al verdetto formale:

| Trigger | Scenario attivato |
|---|---|
| < 80% entry criteria soddisfatti | **HOLD** con re-review entro 30-60 giorni |
| C1 (LoI Regione) mancante | **HOLD automatico** con re-review M+14; cercare anchor alternative |
| C2 (SORA) mancante | **HOLD** + re-application + scope adjustment (VLOS-only Y1) |
| C3 (funding) < 40% | **HOLD** + bridge financing strategy |
| C4 (cooperative) < 6 su 10 | **HOLD + workshop urgenza** per re-confirm |
| ENAC esplicitamente nega path SAIL Pentema | **PIVOT** scope o **No-Go** Y1 |
| Regione Liguria si tira indietro definitivamente | **PIVOT** anchor regione (Piemonte/Calabria) |
| Funding zero al M+10 | **No-Go** o ricerca emergency bridge |

---

## O. Versioning Checklist

La checklist segue un versionamento allineato ai gate. La v1.0 M+3, presente, copre lo sprint M+3. La v1.5 M+6 incorporerà gli esiti del pre-application ENAC e del workshop cooperative, mentre la v2.0 M+10 sarà la versione definitiva per il gate G3 (target).

---

## P. Riferimenti

- Cap. 3 §3.2 (Criteri Go/No-Go)
- Cap. 9 §9.2.4 (G3 Entry/Exit criteria)
- Cap. 10 §10.0bis + §10.3.2 (Hard conditions + scenari)
- Cap. 10 §10.8 (Decisione formale CdA)
- Vol. 2 A.5 V&V Plan (gate review process)
- Metodologia interna di checklist gate review.
