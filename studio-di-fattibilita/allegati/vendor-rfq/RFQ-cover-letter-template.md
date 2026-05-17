# Cover Letter — RFQ-FIRMAMENTO-VTOL-001

> **Template formale di accompagnamento alla RFQ** (`RFQ-TEMPLATE-VTOL-FIRMAMENTO.md`)
> Da inviare insieme al template RFQ via email PEC + (opzionale) raccomandata A/R
> **Bilingua IT/EN** per uso vendor internazionali
>
> **Versione:** 1.0
> **Data emissione:** [DD/MM/YYYY]

---

## NOTA DI USO (NON PARTE DELLA LETTERA INVIATA)

Personalizzare i campi `[BRACKETS]` con:
- Dati Firmamento (sede, P.IVA, contatti)
- Dati vendor (denominazione, sede, contatto referente)
- Date specifiche di scadenza
- Firma del Procurement Manager + Amministratore Delegato

**Suggerimento:** mantenere la versione IT come primaria; la versione EN viene dopo come "courtesy translation" per facilitare la comprensione vendor internazionali.

---

## VERSIONE ITALIANA

**Firmamento Technologies S.r.l.**
[Indirizzo completo sede legale]
[CAP] [Città] ([Provincia])
P.IVA / C.F.: [P.IVA]
PEC: [pec@firmamentotech.legalmail.it]
Tel: [+39 ___ ___ ____]

---

**Spett.le**
[Denominazione Vendor]
[Indirizzo sede legale Vendor]
[CAP] [Città] [Paese]
c.a. [Nome Cognome Referente Vendor]
[email referente]

**Oggetto:** Richiesta di Quotazione (RFQ) — Sistema UAV VTOL per missioni di servizi territoriali Aree Interne italiane — Progetto HALE — Riferimento `RFQ-FIRMAMENTO-VTOL-001`

[Città], [DD/MM/YYYY]

---

Gentile [Nome Referente Vendor],

con la presente Firmamento Technologies S.r.l. **richiede formalmente una quotazione tecnico-economica** per la fornitura di un sistema UAV VTOL completo, secondo le specifiche dettagliate nel documento allegato `RFQ-TEMPLATE-VTOL-FIRMAMENTO.md` (riferimento interno `RFQ-FIRMAMENTO-VTOL-001`).

### Inquadramento del progetto

Firmamento Technologies è una **PMI innovativa italiana** che sta sviluppando una piattaforma di servizi territoriali per le **Aree Interne italiane** — focus pilota sul **Comune di Pentema (Torriglia, Genova)** — con applicazioni di:

- Earth Observation (mapping, antincendio precoce, monitoraggio frane)
- Connettività NTN-grade (in scenari emergency)
- Supporto Protezione Civile e Vigili del Fuoco
- Servizi a cooperative agricole (rete Legacoop, capofila Fabrica)

Il progetto si inserisce nel bando **Cooding Prototypes (Coopfond / Legacoop)** ed è inquadrato nello **Studio di Fattibilità** redatto secondo metodologia ibrida **NASA SE Handbook + art. 41 D.Lgs. 36/2023** (Codice dei Contratti Pubblici italiano).

### Modello di business: service-only

Si precisa che Firmamento Technologies opera con un **modello di business service-only**: la piattaforma UAV oggetto della presente RFQ sarà utilizzata **internamente** per l'erogazione di **servizi ricorrenti** verso PA italiana (Protezione Civile, Vigili del Fuoco, Comuni, Regioni) e cooperative. **Firmamento NON è un rivenditore** di velivoli e NON acquisisce la piattaforma per scopi di rivendita commerciale.

### Sintesi dello scope quotation

Si richiede quotation per:
1. **N. 1 piattaforma UAV VTOL ibrido fixed-wing** (MTOW ≤ 40 kg, payload ≥ 5-8 kg, autonomia ≥ 6h)
2. **Set di payload modulari** (EO RGB + IR LWIR + opzionale telecom LTE)
3. **N. 2 Ground Station** (1 fissa Pentema + 1 mobile)
4. **Pacchetto software** (autopilota + mission planning + downlink)
5. **Training** per 5 persone (piloti, operatori payload, tecnico manutenzione)
6. **Supporto tecnico + manutenzione 5 anni**
7. **Spare parts inventory 3 anni** + emergency restock policy

Dettaglio completo dei requisiti tecnici, regolatori e commerciali è contenuto nel template RFQ allegato (sezioni 3-6).

### Vincoli regolatori essenziali

La piattaforma deve essere idonea per operazioni **BVLOS in Specific Category SAIL II-III** secondo Reg. UE 2019/947, con compliance:
- **EASA Reg. UE 2019/947 + 2019/945**
- **ENAC** (Italia)
- **CE Marking** + Direttiva Macchine + EMC + RED + LVD
- **RoHS + REACH + WEEE + Battery Regulation 2023/1542**
- **Cybersecurity** (NIS2 Directive 2022/2555 + DO-326A awareness)
- **AGCOM** (uso frequenze in Italia)

### Vincoli geopolitici e sovranità dati

In ragione degli stakeholder istituzionali coinvolti (Regione Liguria, ENAC, Protezione Civile), Firmamento richiede al vendor:
- Dichiarazione **ITAR-free** + classificazione EAR (Export Administration Regulations US) per componenti US-origin
- Conformità Reg. UE 2021/821 (dual-use)
- **Sovranità dati operativi su cloud IT/EU** (dati telemetria + payload NON memorizzati su server extra-EU senza autorizzazione esplicita)
- Disponibilità a fornire documentazione per istruttoria **Golden Power** (D.L. 21/2012) se richiesta dalla Presidenza del Consiglio dei Ministri italiana

### Timing del processo

| Fase | Data prevista |
|---|---|
| Emissione RFQ | [DD/MM/YYYY] |
| **Deadline domande di chiarimento vendor** | [DD/MM/YYYY] (15 gg solari) |
| Risposta Firmamento a domande | [DD/MM/YYYY] |
| **Deadline submission quotation completa** | [DD/MM/YYYY] (45 gg solari da emissione) |
| Notifica esito valutazione | [DD/MM/YYYY] (~90 gg da emissione) |
| Negoziazione contratto (con finalist) | [DD/MM/YYYY] |
| Decisione finale | [DD/MM/YYYY] |

### Modalità di submission

La risposta del vendor deve essere inviata:
- Via **PEC** all'indirizzo: [pec@firmamentotech.legalmail.it]
- Con copia conoscenza a: [procurement@firmamentotech.it]
- Subject: `RFQ-FIRMAMENTO-VTOL-001 — Quotation [VENDOR NAME]`

**Lingua accettata:** italiano o inglese.

**Formato:** PDF firmato + Excel/CSV per breakdown prezzi (sez. 5.1 RFQ).

### NDA bidirezionale

L'invio della presente RFQ è subordinato alla firma di un **NDA bidirezionale**. Il template Firmamento è allegato (`NDA-FIRMAMENTO-VENDOR-template.pdf` — separate file). Il vendor può proporre modifiche al template o utilizzare proprio template equivalente, da concordare entro 5 giorni dalla ricezione.

### Confidentiality

Si ricorda che tutte le informazioni scambiate sono sottoposte a confidentiality. Il vendor è tenuto a:
- Non divulgare l'esistenza della RFQ a competitori Firmamento
- Limitare accesso documenti RFQ a personale strettamente necessario
- Distruggere/restituire documenti a conclusione del processo

### Contatti per chiarimenti

**Procurement Manager:**
- [Nome Cognome]
- email: [procurement@firmamentotech.it]
- tel.: [+39 ___ ___ ____]

**Lead Systems Engineer** (per chiarimenti tecnici):
- [Nome Cognome]
- email: [systems@firmamentotech.it]

### Conclusione

Firmamento Technologies considera [Denominazione Vendor] un **potenziale partner strategico** per il Percorso 6A del progetto HALE, in ragione delle capabilities tecniche e del track record consolidato. La presente RFQ rappresenta l'avvio formale del processo di selezione vendor.

Restiamo a disposizione per qualsiasi chiarimento e auspichiamo di ricevere una quotation completa entro la deadline indicata.

**Disclaimer:** la presente RFQ **non costituisce impegno contrattuale** da parte di Firmamento Technologies S.r.l. La quotation richiesta è esclusivamente valutativa. Firmamento si riserva ogni diritto di non procedere, richiedere chiarimenti, modificare scope, aggiudicare a vendor diverso dal miglior prezzo sulla base della valutazione complessiva, o aggiudicare per lotti separati.

Cordiali saluti,

___________________________
**[Nome Cognome]**
Procurement Manager
Firmamento Technologies S.r.l.

___________________________
**[Nome Cognome]**
Amministratore Delegato
Firmamento Technologies S.r.l.

**Allegati:**
- `RFQ-TEMPLATE-VTOL-FIRMAMENTO.md` (RFQ tecnico-commerciale completa)
- `NDA-FIRMAMENTO-VENDOR-template.pdf` (template NDA bidirezionale)
- Profilo aziendale Firmamento Technologies (brochure PDF — opzionale)

---

---

## ENGLISH VERSION (Courtesy Translation)

**Firmamento Technologies S.r.l.**
[Full legal address]
[ZIP] [City] ([Province]), Italy
VAT / Tax ID: [VAT number]
Certified email: [pec@firmamentotech.legalmail.it]
Phone: [+39 ___ ___ ____]

---

**To:**
[Vendor Name]
[Vendor legal address]
[ZIP] [City] [Country]
Attn: [Vendor Reference Contact Name]
[contact email]

**Subject:** Request for Quotation (RFQ) — VTOL UAV System for Italian Inner Areas territorial services — HALE Project — Reference `RFQ-FIRMAMENTO-VTOL-001`

[City], [DD/MM/YYYY]

---

Dear [Vendor Reference Name],

Firmamento Technologies S.r.l. hereby **formally requests a technical and commercial quotation** for the supply of a complete VTOL UAV system, as detailed in the attached document `RFQ-TEMPLATE-VTOL-FIRMAMENTO.md` (internal reference `RFQ-FIRMAMENTO-VTOL-001`).

### Project framework

Firmamento Technologies is an **Italian innovative SME** developing a territorial services platform for **Italian Inner Areas** — pilot focus on the **Municipality of Pentema (Torriglia, Genoa)** — with applications in:

- Earth Observation (mapping, early wildfire detection, landslide monitoring)
- NTN-grade connectivity (emergency scenarios)
- Civil Protection and Fire Department support
- Services for agricultural cooperatives (Legacoop network, lead cooperative Fabrica)

The project is part of the **Cooding Prototypes call (Coopfond / Legacoop)** and is framed in a Feasibility Study drafted under the hybrid methodology **NASA SE Handbook + art. 41 of Italian Legislative Decree 36/2023** (Italian Public Contracts Code).

### Business model: service-only

It is hereby clarified that Firmamento Technologies operates with a **service-only business model**: the UAV platform subject to this RFQ will be used **internally** to deliver **recurring services** to Italian public administration (Civil Protection, Fire Department, Municipalities, Regions) and cooperatives. **Firmamento is NOT a reseller** of aircraft and does NOT acquire the platform for commercial resale purposes.

### Quotation scope summary

Quotation is requested for:
1. **One (1) VTOL hybrid fixed-wing UAV platform** (MTOW ≤ 40 kg, payload ≥ 5-8 kg, endurance ≥ 6h)
2. **Modular payload package** (EO RGB + IR LWIR + optional LTE telecom)
3. **Two (2) Ground Stations** (1 fixed at Pentema + 1 mobile)
4. **Software package** (autopilot + mission planning + downlink)
5. **Training** for 5 persons (pilots, payload operators, maintenance technician)
6. **Technical support and maintenance, 5-year horizon**
7. **3-year spare parts inventory** + emergency restock policy

Full detail of technical, regulatory and commercial requirements is contained in the attached RFQ template (sections 3-6).

### Essential regulatory constraints

The platform must be suitable for **BVLOS operations in Specific Category SAIL II-III** under Reg. EU 2019/947, with compliance to:
- **EASA Reg. EU 2019/947 + 2019/945**
- **ENAC** (Italian National Aviation Authority)
- **CE Marking** + Machinery Directive + EMC + RED + LVD
- **RoHS + REACH + WEEE + Battery Regulation 2023/1542**
- **Cybersecurity** (NIS2 Directive 2022/2555 + DO-326A awareness)
- **AGCOM** (Italian Communications Authority — frequency use)

### Geopolitical constraints and data sovereignty

Due to the institutional stakeholders involved (Liguria Region, ENAC, Italian Civil Protection), Firmamento requires the vendor to provide:
- **ITAR-free declaration** + EAR classification (US Export Administration Regulations) for US-origin components
- Compliance with EU Reg. 2021/821 (dual-use)
- **Operational data sovereignty on IT/EU cloud only** (telemetry and payload data NOT stored on extra-EU servers without explicit Firmamento authorization)
- Availability to provide documentation for **Golden Power investigation** (Italian Decree-Law 21/2012) if required by the Italian Presidency of the Council of Ministers

### Process timing

| Phase | Expected date |
|---|---|
| RFQ issuance | [DD/MM/YYYY] |
| **Deadline for vendor clarification questions** | [DD/MM/YYYY] (15 calendar days) |
| Firmamento response to questions | [DD/MM/YYYY] |
| **Deadline for complete quotation submission** | [DD/MM/YYYY] (45 calendar days from issuance) |
| Evaluation outcome notification | [DD/MM/YYYY] (~90 days from issuance) |
| Contract negotiation (with finalists) | [DD/MM/YYYY] |
| Final decision | [DD/MM/YYYY] |

### Submission modalities

Vendor response shall be submitted:
- Via **certified email (PEC)** to: [pec@firmamentotech.legalmail.it]
- Cc to: [procurement@firmamentotech.it]
- Subject: `RFQ-FIRMAMENTO-VTOL-001 — Quotation [VENDOR NAME]`

**Accepted language:** Italian or English.

**Format:** Signed PDF + Excel/CSV for price breakdown (sect. 5.1 RFQ).

### Bilateral NDA

The issuance of this RFQ is subject to signing of a **bilateral NDA**. The Firmamento template is attached (`NDA-FIRMAMENTO-VENDOR-template.pdf` — separate file). The vendor may propose template modifications or use its own equivalent template, to be agreed upon within 5 days of receipt.

### Confidentiality

It is recalled that all information exchanged is subject to confidentiality. The vendor is required to:
- Not disclose the existence of this RFQ to Firmamento competitors
- Limit access to RFQ documents to strictly necessary personnel
- Destroy/return documents upon process completion

### Contacts for clarifications

**Procurement Manager:**
- [Name Surname]
- email: [procurement@firmamentotech.it]
- phone: [+39 ___ ___ ____]

**Lead Systems Engineer** (technical clarifications):
- [Name Surname]
- email: [systems@firmamentotech.it]

### Conclusion

Firmamento Technologies considers [Vendor Name] a **potential strategic partner** for HALE Project Path 6A, given its technical capabilities and consolidated track record. This RFQ represents the formal start of the vendor selection process.

We remain available for any clarification and look forward to receiving a complete quotation by the indicated deadline.

**Disclaimer:** This RFQ does **NOT constitute a contractual commitment** by Firmamento Technologies S.r.l. The requested quotation is purely evaluative. Firmamento reserves all rights to not proceed, request clarifications, modify scope, award to a vendor other than the lowest-price bidder based on overall evaluation, or award separate lots.

Best regards,

___________________________
**[Name Surname]**
Procurement Manager
Firmamento Technologies S.r.l.

___________________________
**[Name Surname]**
Chief Executive Officer
Firmamento Technologies S.r.l.

**Attachments:**
- `RFQ-TEMPLATE-VTOL-FIRMAMENTO.md` (complete technical-commercial RFQ)
- `NDA-FIRMAMENTO-VENDOR-template.pdf` (bilateral NDA template)
- Firmamento Technologies corporate profile (brochure PDF — optional)

---

**END OF COVER LETTER**

Bilingual document IT/EN. Version 1.0.
