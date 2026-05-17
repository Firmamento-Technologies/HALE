# Capitolo 4 — Perimetro, Scope, Deliverable e Interfacce (ICD preliminare)

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 4
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Metodologia:** NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105), §4.3 Logical Decomposition + §6.3 Interface Management
> **Conformità:** D.Lgs. 36/2023 art. 41 + Allegato I.7 (PFTE) — definizione perimetro, scope e quadro delle interfacce
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** verifica condotta dall'agente `red-team-skeptic` — vedi §4.8

---

## 4.0 Sintesi del capitolo

Il presente capitolo definisce, in modo **chiuso, tracciabile e contrattualmente difendibile**, ciò che il Piano di Fattibilità Tecnico-Economica (PFTE) HALE/VTOL **valida** entro M+11, ciò che **non valida**, i deliverable formali che produce e le **interfacce di sistema** preliminari (Interface Control Document — ICD) che fondano il successivo dialogo con stakeholder, fornitori e autorità regolatorie.

Tre risultati strutturali del capitolo:

1. **Perimetro definito** — Lo Studio approva la **fattibilità decisionale** dei Percorsi 6A (VTOL pilota) e 6B (HALE R&D preparatorio) per il gate M+10/M+11; **non approva** l'esecuzione operativa post-pilota, la costruzione di prototipi HALE full-scale, né l'industrializzazione su flotta. Tutto ciò che eccede il perimetro è esplicitamente deferito ai gate successivi.
2. **17 deliverable PFTE** — Documenti formali, ciascuno con owner RACI, contenuto minimo, formato, timing M+0 → M+11 e criterio di accettazione. La tabella copre i requisiti di **art. 41 D.Lgs. 36/2023 + Allegato I.7** (quadro esigenziale → trade study → analisi tecnica → fattibilità economica → cronoprogramma + gate).
3. **ICD preliminare a 20 interfacce** — Mappa completa delle interfacce critiche del sistema (fisiche, funzionali, regolatorie, contrattuali, ecosistemiche), in coerenza con NASA SE Handbook §6.3, con sigla, descrizione, tipo, standard di riferimento, owner e status.

**Tesi di capitolo:** un perimetro deliberatamente stretto **è** un elemento di robustezza dello Studio. Il rischio numero uno per un PFTE aerospace nelle Aree Interne **non** è la sottostima delle ambizioni; è lo **scope creep** che annacqua i deliverable, fa scivolare i gate e brucia il budget di rendicontazione. La disciplina di questo capitolo è quindi parte centrale della qualità del documento.

**Verdetto interno del capitolo per il gate M+10**: **GO sul perimetro così definito**; gli **8 criteri di Scope Acceptance** (§4.5) sono il check di passaggio.

---

## 4.0bis Boundary conditions del progetto

In coerenza con Cap. 3.0bis e Cap. 5.0bis, il presente capitolo opera sotto le due condizioni di confine dichiarate:

- **B1 — Modello cooperativo + service-only**: Firmamento Technologies è **operatore di servizi**, non OEM aeronautico. Lo scope del PFTE valida la fattibilità di **erogare servizi ricorrenti** (DaaS, IaaS, canone) a una rete di **10 cooperative Legacoop** (capofila Fabrica) + **Pubblica Amministrazione** (Regione Liguria, Protezione Civile, Comuni). NON è in scope una qualunque ipotesi alternativa di "vendita di velivoli". L'ICD e i deliverable riflettono questa scelta strutturale (es. interfaccia cooperativa↔dashboard come interfaccia di sistema *interna* allo scope, non come "interfaccia commerciale verso il mercato").
- **B2 — Visione 10 anni "nodo italiano EU sovereign HAPS"**: Lo Studio di Fattibilità copre i passi 1-2 (Y1-Y3) della roadmap 10 anni. Le interfacce di lungo termine verso ecosistema EU (IRIS², GAIA-X, eventuale consorzio EU HAPS) sono **annotate come interfacce future** nell'ICD (riga INT-19, -20), con confidence bassa e status preliminare. Non sono in scope deliverable formali di "interfaccia operativa" con questi ecosistemi entro M+11.

Linguaggio pubblico per il dossier (vedi `riferimenti/RESERVED-rischi-geopolitici.md`): "complementare a IRIS²", **mai** "alternativa europea a Starlink".

---

## 4.1 Scope e obiettivi della fase di fattibilità

### 4.1.1 Definizione scope: cosa il PFTE valida

Il Piano di Fattibilità Tecnico-Economica (PFTE) della piattaforma HALE/VTOL Firmamento si propone di fornire — entro il gate M+10/M+11 — una **base decisionale evidence-based** che consenta agli stakeholder finanziatori (Coopfond, Regione Liguria, eventuali co-finanziatori PNRR/EDF/Horizon) di pronunciarsi formalmente su:

1. **Fattibilità tecnica** dei due percorsi 6A (VTOL commerciale TRL 8-9) e 6B (HALE solare custom R&D)
2. **Fattibilità operativa** del modello service-only con rete cooperative + PA
3. **Fattibilità regolatoria** rispetto a ENAC (SORA), EASA (HAPS framework), AGCOM (spettro), Garante (privacy)
4. **Fattibilità economico-finanziaria** del MVP Y1 e della roadmap pluriennale
5. **Fattibilità di governance** della partnership Firmamento + 10 cooperative + anchor pubblico

Lo scope del PFTE copre **attività di analisi, modellazione, pre-engagement con autorità, workshop strutturati con stakeholder, trade study, computo metrico preliminare, scrittura formale dei documenti**. È un **lavoro a tavolino e di co-progettazione**: produce **carta** (deliverable documentali) decisionalmente robusta, **non hardware in volo**.

Il PFTE è coerente, per natura e contenuti, con il **livello "progetto di fattibilità tecnico-economica"** ex art. 41 D.Lgs. 36/2023, integrato con la disciplina metodologica del **NASA SE Handbook Rev 2** [^1]: l'approccio italiano definisce *cosa* deve esserci (Quadro Esigenziale, DOCFAP, Cronoprogramma, Quadro Economico), l'approccio NASA definisce *come* costruire tracciabilità tra needs, requirements, trade study, V&V, gate.

> **Falsifying observation §4.1.1**: se al M+10/M+11 il PFTE non è leggibile da un Responsabile Unico del Procedimento (RUP) abituato al D.Lgs. 36/2023 (perché eccessivamente "ingegneristico" e privo dei consueti elaborati italiani — Quadro Esigenziale, DIP, DOCFAP, Quadro Economico, Computo Metrico Estimativo, Cronoprogramma per fasi), il documento fallisce il proprio scopo amministrativo. **Mitigazione strutturale**: ogni deliverable PFTE in tabella §4.3.1 ha mappatura esplicita verso art. 41 + Allegato I.7. **Confidence: high** (vincolo amministrativo).

### 4.1.2 Output e deliverable del PFTE

Il PFTE genera, come output formale documentale, **tre tipi di artefatti**:

| Tipo di artefatto | Contenuto sintetico | Destinazione |
|---|---|---|
| **Volume 1 — Studio testuale** | 11 capitoli (Cap. 0 + Cap. 1-10 + Cap. 11), 150-200 pp | Lettura decisionale Coopfond + Regione + investitori |
| **Volume 2 — Allegati tecnici** | RTM completa, Risk Register, Trade Study Report, ICD, V&V Plan, schemi CAD, modelli di calcolo, bilanci di massa, Computo Metrico Estimativo, Piano di Manutenzione preliminare, PSC operativo, VIA preliminare | Verifica tecnica + audit |
| **Volume 3 — Riferimenti** | Bibliografia normativa + tecnica + dati di mercato | Documentazione di supporto |

A questi si aggiungono i **documenti preliminari ex art. 41 / Allegato I.7** (Quadro Esigenziale formalizzato, DOCFAP = sintesi Trade Study, DIP) e materiali di supporto strategici (slide deck, decision brief 5 pagine per la Giunta Regionale + Consiglio di Amministrazione Coopfond).

**Mappatura dei deliverable PFTE rispetto al Cap. 1.5 (Obiettivi)**:

| Obiettivo Cap. 1 | Deliverable PFTE principali | Cap. coinvolto |
|---|---|---|
| OB-01 Valutare fattibilità tecnica | DEL-PFTE-05 (Cap. 6), DEL-PFTE-06 (modelli) | Cap. 6 |
| OB-02 Valutare fattibilità operativa | DEL-PFTE-04 (ConOps), DEL-PFTE-15 (workshop) | Cap. 2, 4 |
| OB-03 Valutare fattibilità regolatoria | DEL-PFTE-08, -09, -10 (DPIA, AGCOM, ENAC) | Cap. 5 |
| OB-04 Confrontare alternative architetturali | DEL-PFTE-03 (Trade Study, DOCFAP) | Cap. 6 |
| OB-05 Costruire mappa investimento → servizi | DEL-PFTE-12 (Cap. 8) | Cap. 7, 8 |
| OB-06 Definire roadmap + Fase successiva | DEL-PFTE-14 (Cap. 9 + Cap. 11) | Cap. 9, 11 |

### 4.1.3 Collegamento a obiettivi del Cap. 1.5 e criteri Go/No-Go (richiamo Cap. 3.2)

I deliverable PFTE non sono fini a se stessi: sono **evidenze necessarie** al verdetto del gate M+10/M+11. I criteri Go/No-Go sono dichiarati nel Cap. 3.2 e qui richiamati come **trigger di accettazione** dello scope:

| Famiglia di criteri (Cap. 3.2) | Deliverable PFTE corrispondenti |
|---|---|
| 3.2.1 Tecnici (concept architettura, performance, FMECA, TRL) | DEL-PFTE-05 (Cap. 6), DEL-PFTE-06 (modelli), DEL-PFTE-13 (Risk Register) |
| 3.2.2 Regolatori (ENAC SAIL, EASA, AGCOM) | DEL-PFTE-08/09/10 (DPIA + AGCOM + ENAC pre-app) |
| 3.2.3 Economico-finanziari (Quadro Economico, NPV/IRR) | DEL-PFTE-12 (Cap. 8 + Computo Metrico Estimativo) |
| 3.2.4 Business (BMC + VPC + anchor customer) | DEL-PFTE-15 (workshop) + Cap. 7 |
| 3.2.5 Operativi/territoriali (LoI Comune, cooperative, accettabilità sociale) | DEL-PFTE-11 (MOA/MOU) + DEL-PFTE-15 |

> **Note di metodo**: lo Studio non è una "scatola tecnica" autoreferenziale. Ogni deliverable risponde a un criterio Go/No-Go; ogni criterio Go/No-Go è figlio di un requisito (Cap. 3); ogni requisito ha origine in uno StNeed (Cap. 3.3) di uno stakeholder identificato (Cap. 2). La RTM (Cap. 3.8) è il filo conduttore.

### 4.1.4 Decisione Go/No-Go fattibilità (Gate M+10/M+11)

Il gate M+10/M+11 è il **gate decisionale principale** del PFTE. Si applica la convenzione di esito a tre stati (cf. skill `gate-review-checklist`):

- **GO**: tutti i criteri Cap. 3.2 superano soglia, Studio chiuso, autorizzato passaggio a Fase 1 (Pilota Operativo VTOL M+12-M+24)
- **HOLD**: ≥ 30% dei criteri non soddisfatti, **non No-Go**: re-review M+13-15 con piano correttivo
- **NO-GO**: showstopper insuperabili (ENAC nega path SAIL per Pentema; Regione Liguria si ritira; fonti di finanziamento azzerate)

Il gate è **multidimensionale** (tecnico × regolatorio × economico × business × operativo); un singolo deliverable mancante o un singolo criterio in rosso **non comporta automaticamente NO-GO**, ma triggera Hold con re-review. Questo è esplicitamente coerente con la filosofia gate-driven NASA SE [^1] §3.

**Articolazione gate intermedi**:

| Gate | Timing | Output principale | Decisione |
|---|---|---|---|
| **Gate M+3 — Allineamento Strategico** | M+3 | Baseline requisiti (Cap. 3) + perimetro (Cap. 4) + quadro normativo (Cap. 5) | Conferma scope + identificazione showstopper |
| **Gate M+6 — Interim Review** | M+6 | Workshop stakeholder + pre-application ENAC + trade study v0.5 | Go/Hold tecnico-regolatorio |
| **Gate M+10 — Design Ready** | M+10 | Cap. 6-7-8-9 redatti + DPIA finale + V&V Plan completo | Verdetto principale fattibilità |
| **Gate M+11 — PFTE Closure** | M+11 | Cap. 0 (Sintesi Esecutiva) + Cap. 10 (Raccomandazione) + presentazione formale | Approvazione finale Studio |
| **Gate M+12 — Funding decision** | M+12 | LoI Coopfond + co-financing + decisione operativa Fase 1 | Avvio Fase 1 pilota |

### 4.1.5 Confini del perimetro: cosa NON è fattibilità

In coerenza con la disciplina di **scope creep avoidance** raccomandata dalla skill `gate-review-checklist`, dichiaro esplicitamente cosa il PFTE **non valida**, lasciando questi punti ai gate successivi:

- ❌ **Costruzione fisica del velivolo HALE full-scale**: analisi aerodinamica e modellazione strutturale concettuale SÌ (Cap. 6); fabbricazione e first-flight di prototipo full-scale NO. Deferito a Fase 4 R&D (M+36-M+60+).
- ❌ **Operazioni commerciali continuative VTOL post-M+12**: il PFTE valida la fattibilità del pilota; le operazioni di servizio retributive con SLA contrattualizzati sono **Fase 1 esecutiva** (M+12-M+24), non fattibilità.
- ❌ **Procurement esecutivo**: pre-vendor engagement (datasheet, technical Q&A, prezzi indicativi) SÌ M+1-M+6; **RFQ formali con contratti vincolanti e PO firmati NO**. Deferito a gate post-M+12.
- ❌ **Lavori civili permanenti**: scouting siti Pentema + DTM + check disponibilità terreno SÌ; fondamenta, edificazione shelter, allacciamenti utility, antenne fisse NO. Deferito a Fase 1 M+13-M+17.
- ❌ **Training pilota e certificazioni operative**: bozza Operations Manual + procedure SOP draft SÌ; training certificato pilota UAS, esami ENAC, training sul campo NO. Deferito a Fase 1 M+18-M+22.
- ❌ **Costruzione subscale HALE per flight test**: simulazioni, modelli aerodinamici, energy balance simulati SÌ; prototipo subscale fisico + flight test campaign NO. Deferito a Fase 3 R&D (M+36-M+42).
- ❌ **Negoziazione e firma contratti commerciali pluriennali con la PA**: LoI (Lettera di Intenti) Regione Liguria SÌ; contratti firmati con anchor customer per multi-year service NO. Deferito a gate M+12 → M+18.
- ❌ **Disseminazione large-scale modello replicabile altre regioni SNAI**: contatti preliminari con regioni interessate (Piemonte, Marche, Calabria, Basilicata) SÌ; engagement formale, MoU, kit replicabile NO. Deferito a Fase 2 scale-up (M+24+).
- ❌ **Operazioni commerciali HAPS NTN**: il PFTE valida solo R&D preparatorio Phase B per il Percorso 6B. Capacità commerciale wholesale verso telco NO. Deferito a gate post-M+60.
- ❌ **Acquisizione SLA assicurativi BVLOS definitivi**: market scan preliminare assicurativo SÌ; polizza firmata e premi negoziati NO. Deferito a Fase 1 M+15-M+20.

Questa lista **non è esaustiva**: ulteriori esclusioni sono articolate nella tabella §4.2.1 per dominio. Il principio è "**meglio escludere apertamente che pretendere implicitamente**".

---

## 4.2 In-Scope / Out-of-Scope per dominio

### 4.2.1 Tabella In-Scope / Out-of-Scope (6 domini × 5-7 voci)

La tabella seguente articola il perimetro su **sei domini di attività** (Engineering, Operations, Regulatory, Business & Funding, Territorial & Stakeholder, Cross-cutting), con **5-7 voci per dominio** ciascuna marcata **IN / OUT / PARZIALE** con razionale e timing di esecuzione.

**Convenzione**:
- **IN** = oggetto formale del PFTE, deliverable previsto
- **OUT** = esplicitamente fuori scope PFTE, deferito a gate successivi
- **PARZIALE** = scope parziale (es. concept SÌ, esecuzione NO; analisi preliminare SÌ, validazione full NO)

#### Dominio A — Engineering & System Design

| # | Voce | In/Out/Parz | Razionale (cap./req. coinvolti) | Note di esecuzione |
|---|---|---|---|---|
| A-01 | Architettura concettuale velivolo 6A VTOL | **IN** | Cap. 6.1 + Trade Study TS-PLATFORM-6A; ConOps (SyR-F-001) | Selezione baseline JOUAV CW-30E o alternative EU; analisi datasheet, integrazione |
| A-02 | Architettura concettuale velivolo 6B HALE | **IN** | Cap. 6.1 + Trade Study TS-MATERIAL + TS-PROP; SyR-F-005 | Concept high-AR, T-tail, fibra lino sec; modello high-level |
| A-03 | FMECA + FTA preliminari | **IN** | Cap. 6.6 + skill `risk-register-builder`; Risk Register | Volume 2 Allegato A.2; 16-20 rischi top |
| A-04 | Trade Study formali (DOCFAP) | **IN** | Cap. 6.3; skill `trade-study-analysis`; OQ-001/003/005/006/007 | TS-PLATFORM, TS-MATERIAL, TS-PROP, TS-AVI, TS-PAYLOAD |
| A-05 | Modelli di calcolo (energy balance, link budget, polare aerodinamica) | **IN** | Cap. 6.2; skill `link-budget-calculator`; SyR-P-004, -005, -006 | Excel/Python; output grafici sensitivity |
| A-06 | Bilanci di massa preliminari | **IN** | Cap. 6.2; SsR-AERO-* | Tabella mass breakdown 6A + 6B |
| A-07 | Costruzione fisica prototipi | **OUT** | Fuori budget M+0-M+11; deferito Fase 1 (6A) / Fase 4 (6B) | Hardware: nessuno costruito durante PFTE |
| A-08 | Wind tunnel test fisici (HALE) | **OUT** | Fase 3 R&D (M+36+); richiede facility specialistica | CFD preliminary OK; wind tunnel NO |
| A-09 | Certificazione DAL avionica (DO-178C, DO-254) | **OUT** | Fase 1 (6A) / Fase 4 (6B); richiede DER e laboratorio certificato | Compliance plan OK; certificazione NO |

#### Dominio B — Operations & ConOps

| # | Voce | In/Out/Parz | Razionale | Note di esecuzione |
|---|---|---|---|---|
| B-01 | ConOps preliminari 6A + 6B (Cap. 3.4 + Cap. 6) | **IN** | Cap. 3.4; SyR-O-* | v0.5 al M+3; v1.0 al M+6 post-workshop |
| B-02 | Procedure operative standard (SOP) draft | **PARZIALE** | Cap. 6.7 (Operations Manual draft); SyR-O-001/002 | Bozza SOP per emergenza + nominale; non finalizzate |
| B-03 | Voli operativi (anche dimostrativi) | **OUT** | Pilota Fase 1 M+18-M+22; nessun volo durante PFTE | Pre-flight test field SOLO se autorizzazioni ENAC ottenute (improbabile M+10) |
| B-04 | Training certificato pilota UAS (corso ENAC) | **OUT** | Fase 1 M+18-M+22; richiede esame autorità | Scouting corsi disponibili OK |
| B-05 | Setup infrastruttura ground segment fisica | **OUT** | Fase 1 M+13-M+17 | Scouting siti + DTM + check connettività SÌ (vedi C-01) |
| B-06 | Tabletop exercises con Protezione Civile | **IN** | Cap. 6.7 + Cap. 2; SyR-O-002 (TTR ≤ 4h) | 1-2 tabletop M+6-M+9 |
| B-07 | Pipeline data processing operativa | **PARZIALE** | Cap. 6.8 + Cap. 5.6 (GDPR); SsR-GS-003 | Concept + PoC anonimizzazione SÌ; deployment full NO |

#### Dominio C — Regulatory & Compliance

| # | Voce | In/Out/Parz | Razionale | Note di esecuzione |
|---|---|---|---|---|
| C-01 | Pre-application meeting ENAC (SORA preliminary) | **IN** | Cap. 5.1.5 + SyR-C-001; CRIT regulatori (Cap. 3.2.2) | DEL-PFTE-10; M+3-M+6 |
| C-02 | SORA application formale completa (SAIL III) | **OUT** | Fase 1 M+13-M+18; richiede Operations Manual + assicurazione + flight test articulated | Pre-application SI; submission completa NO |
| C-03 | Type Certificate HALE (Reg. 2018/1139) | **OUT** | Fase 4 R&D; orizzonte 5-10 anni; richiede EASA Special Condition negoziata | TC application package preliminary preparation OK in Fase 3 |
| C-04 | DPIA (Data Protection Impact Assessment) preliminare GDPR Art. 35 | **IN** | Cap. 5.6 + SyR-C-003; DPO engagement | DEL-PFTE-08; firma DPO M+5 |
| C-05 | Consultazione AGCOM spettro radio (banda licenziata o ISM) | **IN** | Cap. 5.5 + SyR-C-002 (revised) | DEL-PFTE-09; lettera M+1-M+2, risposta M+2-M+4 |
| C-06 | Cybersecurity assessment NIS2 + D.Lgs. 138/2024 | **PARZIALE** | Cap. 5.7 + SyR-C-004; threat model | Threat model + checklist NIS2 SÌ; penetration test esecutivo NO |
| C-07 | Notifica ITU + coordinamento internazionale spettro | **OUT** | Fase 2-3 (post-MVP); rilevante per HAPS Percorso 6B | Engagement informale OK; notifica formale NO |
| C-08 | Certificazione AS/EN 9100 + ISO 9001 | **PARZIALE** | SyR-C-005; QMS Firmamento | Roadmap di certificazione SÌ; ottenimento certificato in Fase 1-2 |

#### Dominio D — Business, Funding & Economic Analysis

| # | Voce | In/Out/Parz | Razionale | Note di esecuzione |
|---|---|---|---|---|
| D-01 | Business Model Canvas (BMC) + Value Proposition Canvas (VPC) | **IN** | Cap. 7 (esistente) | Vol. 2 Allegato C |
| D-02 | Analisi mercato TAM-IT + competitor scan | **IN** | Cap. 7.3-7.4; skill `competitor-intelligence` | Confidence low-medium dichiarato |
| D-03 | Quadro Economico ex art. 41 + Computo Metrico Estimativo | **IN** | Cap. 8 + Vol. 2 Allegato F; Allegato I.7 D.Lgs. 36/2023 | Granularità WBS livello 3-4; ±25% accuracy |
| D-04 | Piano finanziario NPV/IRR/payback/sensitivity worst-base-best | **IN** | Cap. 8.6-8.8; SyR-Cost-001/002/003 | WACC 12% baseline; sensitivity ±30% |
| D-05 | Contratti firmati con anchor customer pluriennali | **OUT** | Fase 1 M+13-M+18 | LoI Regione Liguria sì (DEL-PFTE-11) |
| D-06 | Fundraising round equity / venture | **OUT** | Fase 1+; non scope PFTE | Pitch deck preparatorio OK |
| D-07 | Bandi PNRR/Horizon/EDF — application formale | **PARZIALE** | Cap. 8.5 + skill `snai-funding-territorial-expert` | Scouting opportunità + application Coopfond SÌ; altri bandi mappati ma application NO |

#### Dominio E — Territorial & Stakeholder Engagement

| # | Voce | In/Out/Parz | Razionale | Note di esecuzione |
|---|---|---|---|---|
| E-01 | Workshop strutturati con 10 cooperative Legacoop pilota | **IN** | Cap. 2 + Cap. 3.3.2 (StNeed-005, -006, -007); CRIT business (Cap. 3.2.4) | DEL-PFTE-15; ≥ 5 workshop M+0-M+10 |
| E-02 | Workshop Protezione Civile + ARPA Liguria | **IN** | Cap. 2 + StNeed-001/002/003/004 | 2-3 workshop dedicati M+3-M+9 |
| E-03 | Workshop comunità Pentema (engagement sociale) | **IN** | StNeed-008 (privacy) + accettabilità sociale | 1-2 incontri pubblici M+6-M+9 + DPIA pubblica |
| E-04 | LoI / MoU con Regione Liguria | **IN** | CRIT operativo (Cap. 3.2.5); AS-001 | DEL-PFTE-11; firma M+6-M+9 |
| E-05 | MoU con 8/10 cooperative pilota | **IN** | CRIT operativo + AS-003 | DEL-PFTE-11; firma M+3-M+6 |
| E-06 | Engagement con altre regioni SNAI (Piemonte, Marche, ecc.) | **OUT** | Scale-up Fase 2 (M+24+) | Mappatura contatti preliminari OK |
| E-07 | Programma educational / formazione cooperative | **OUT** | Fase 1+ | Scouting bisogni training SÌ; esecuzione NO |

#### Dominio F — Cross-cutting (Data, IT, Sustainability, Governance)

| # | Voce | In/Out/Parz | Razionale | Note di esecuzione |
|---|---|---|---|---|
| F-01 | Data governance + cloud architecture (GDPR + NIS2) | **IN** | SsR-GS-002 + Cap. 5.6 + 5.7 | Architettura sì; deployment full NO |
| F-02 | Sustainability assessment + ESG narrative | **IN** | SyR-E-001/002/003; Cap. 7.7 (BMC sostenibilità) | LCA preliminare OK |
| F-03 | Valutazione Impatto Ambientale (VIA) preliminare | **PARZIALE** | Vol. 2 Allegato I; SyR-E-* | Screening preliminare SÌ; VIA formale (se richiesta) Fase 1 |
| F-04 | Risk Register + Assumption Log + Dependency Log | **IN** | Cap. 6.5 + Vol. 2 Allegato A.2; skill `risk-register-builder` | DEL-PFTE-13; 16-20 rischi |
| F-05 | Governance partnership Firmamento + cooperative + PA | **IN** | Cap. 2 + Cap. 7.7 + B1 boundary | Modello RTI vs JV vs Contratto di Rete (Trade Study TS-GOV) |
| F-06 | Audit terzo indipendente (RINA / DNV) dello Studio | **OUT** | Raccomandato post-M+11 per "investment grade"; non in budget PFTE | Lista auditor scoutata OK |

### 4.2.2 Razionale delle scelte

**Perché alcune voci sono PARZIALE e non IN o OUT**:
- **PARZIALE = concept / preliminare / desk-only** anziché esecutivo. Esempio B-02 (SOP draft): produciamo le bozze, ma le SOP finalizzate richiedono il vero ambiente operativo Fase 1.
- **PARZIALE = analisi SÌ, validazione esterna NO**. Esempio C-06 (NIS2): produciamo threat model + checklist; il penetration test esecutivo richiede ambiente di staging che non esiste a M+10.
- **PARZIALE = parte del lavoro ricade nel PFTE, parte nei gate successivi**. Esempio C-08 (AS/EN 9100): definiamo la roadmap di certificazione (in scope), ma il certificato si ottiene in Fase 1-2 (out of scope).

**Perché siamo restrittivi sull'OUT**:
1. **Rispetto del budget e del tempo M+11**: PFTE con budget ~€150-300k + 11 mesi non può ragionevolmente coprire più dello scope qui dichiarato. Sovrastimare lo scope = sicuro fallimento gate.
2. **Disciplina contrattuale**: tutto ciò che è OUT deve essere esplicitamente accettato dagli stakeholder PRIMA del Gate M+3 (vedi Criterion 2 di §4.5.1), per evitare richieste di "extra" non finanziate.
3. **Rispetto del rischio aerospace**: la base rate di programmi aerospace che falliscono per scope creep è alta (vedi `epistemic-rigor` Regola 7; storia di HALE solari falliti: NASA Helios, Solara/Titan, Aalto HAWK30). Un PFTE che cerca di fare troppo è già un programma in crisi.

> **Falsifying observation §4.2**: se durante l'esecuzione del PFTE uno stakeholder (es. Regione Liguria) richiede ufficialmente l'estensione di una voce da OUT a IN (es. "vogliamo che il PFTE includa il volo dimostrativo a Pentema entro M+9"), il **Change Control Board** (cf. §4.5.1 Criterion 2) deve essere convocato e deve **valutare formalmente** l'impatto su budget/tempo/risk. Modificare implicitamente lo scope = fallimento gate al M+10. **Confidence: high** (lezioni apprese da progetti aerospace simili).

---

## 4.3 Deliverable del Piano di Fattibilità

### 4.3.1 Deliverable PFTE (M+0 → M+11) — Tabella sintetica

La tabella seguente elenca i **17 deliverable documentali** del PFTE, in coerenza con i contenuti richiesti da **D.Lgs. 36/2023 art. 41 + Allegato I.7** e con la struttura NASA SE. Ogni deliverable ha owner RACI, contenuto minimo, formato, timing M+0 → M+11, evidenza di accettazione.

| ID | Deliverable | Contenuto minimo | Formato | Owner principale | Timing (M+) | Evidenza accettazione | Mapping art. 41 / Allegato I.7 |
|---|---|---|---|---|---|---|---|
| **DEL-PFTE-01** | Studio di Fattibilità completo (Volume 1, 11 capitoli) | Cap. 0 Sintesi Esecutiva + Cap. 1-11 + glossario + bibliografia, 150-200 pp | PDF + Markdown nel repo | Firmamento Tech (lead editor) + Coopfond (sponsor finanziatore) | M+10 draft / **M+11 final** | Firma DG Coopfond + controfirma Legacoop + protocollo | PFTE — testo del progetto di fattibilità |
| **DEL-PFTE-02** | Quadro Esigenziale formalizzato + Requisiti tracciati (Cap. 1 + Cap. 3 + RTM completa) | StNeed (17) + SyR (42) + SsR (~80) + RTM Excel zero-orphan | Excel RTM (.xlsx) + PDF | aerospace-systems-engineer (Firmamento) + Coopfond validation | M+3 draft / **M+8 final** | RTM audit M+8 zero-gap | Quadro Esigenziale (Allegato I.7) + tracciabilità NASA |
| **DEL-PFTE-03** | DOCFAP (Documento di Fattibilità delle Alternative Progettuali) = Trade Study Report | A0-A4 alternative + matrice multi-criterio Pugh / AHP + DOCFAP narrativo + raccomandazione architettura | Word/PDF + Excel scoring | trade-study-analysis skill + aerospace-systems-engineer | M+6 interim / **M+8 final** | Approvazione workshop stakeholder M+8 | DOCFAP (Allegato I.7) — sintesi DOCFAP italiano |
| **DEL-PFTE-04** | ConOps v1.0 → v2.0 (Concept of Operations) | Missione ordinaria + scenario emergenza + procedure SOP draft + flowchart + storyboard | Word/PDF + Visio | CONOPS Lead (Firmamento) + Protezione Civile liaison | M+3 v1.0 / **M+8 v2.0** | Firma PC Liguria + tabletop M+7 | DIP — Documento di Indirizzo alla Progettazione |
| **DEL-PFTE-05** | Analisi Tecnica di Fattibilità (Cap. 6 completo) | 6A VTOL: 10 aree critica + semafori; 6B HALE: gap TRL + showstopper + benchmark HAPS competitor | PDF tecnico 60-80 pp + Excel FMEA + schemi CAD | aerospace-systems-engineer + propulsion-energy-engineer + avionics-gnc-engineer | M+6 interim / **M+10 final** | Review tecnico Coopfond + Regione M+10 | Relazione tecnica (Allegato I.7) |
| **DEL-PFTE-06** | Modelli di calcolo (energy balance, link budget, polare, propagazione RF) | Modelli Excel/Python: (a) energy balance 6B inverno/estate, (b) link budget service + feeder + C2, (c) propagazione RF DTM Pentema, (d) autonomia 6A vs wind/payload | Excel master + script Python (.py) + report PDF | propulsion-energy-engineer + telecom-payload-expert + skill `link-budget-calculator` | M+3 → M+10 | Validazione cross-check da consulente esterno M+10 | Allegati tecnici (Allegato I.7) |
| **DEL-PFTE-07** | V&V Plan (Verification & Validation Plan) preliminare | Matrice attività V&V 6A (12) + 6B (12), metodi I/A/D/T, gate criticality, evidence plan | Excel matrice + Word/PDF | V&V engineer (Firmamento) | M+2 draft / **M+8 final** | Approvazione review meeting M+5 (interim) + M+8 | Cronoprogramma verifiche (Allegato I.7) |
| **DEL-PFTE-08** | DPIA (Data Protection Impact Assessment) preliminare GDPR Art. 35 | (a) trattamento + mapping dati personali, (b) rischi privacy, (c) mitigazioni AES-256 + RBAC + retention, (d) DSAR procedure | PDF DPIA 20-30 pp + allegati crittografia | data-privacy-counsel + DPO Firmamento/Regione | M+4 draft / **M+5 final signed** | Firma DPO + audit interno M+5-M+6 | Allegato compliance (Allegato I.7) |
| **DEL-PFTE-09** | Consultazione AGCOM (Spettro radio) | Richiesta formale lettera M+1-M+2 + risposta AGCOM banda L o ISM + coexistence analysis | Lettere PDF + report tecnico | telecom-ntn-payload-expert + Firmamento + AGCOM liaison Regione | M+1-M+2 richiesta / **M+2-M+4 risposta** | Lettera AGCOM confermativa + fallback ISM analysis | Allegato compliance regolatoria |
| **DEL-PFTE-10** | Pre-Assessment ENAC (SORA pathway) | PEC/lettera pre-consultazione + worksheet SORA preliminare + risposta ENAC SAIL atteso + lead time | Lettere PDF + Excel SORA worksheet | aviation-regulatory-counsel + Firmamento + Regione liaison ENAC | M+1-M+3 pre-cons / **M+3-M+6 risposta** | Lettera ENAC feedback SAIL pathway | Allegato compliance regolatoria |
| **DEL-PFTE-11** | Atti Amministrativi (MOA + MOU) | MOA Regione-Comuni-PC-Prefettura + MOU 8/10 cooperative Legacoop | PDF MOA + MOU con firme dirigenti scanned | Coopfond legal + business-model-strategist + Regione affari legali | **M+3-M+6** | Controfirme depositate Regione + ≥80% adesione cooperative | Atti di assenso (Allegato I.7) |
| **DEL-PFTE-12** | Quadro Economico + Computo Metrico Estimativo + Piano Finanziario (Cap. 8) | Budget WBS 3-4 livelli ±25%, 3 scenari Worst/Base/Best, NPV/IRR/payback, sensitivity, Computo Metrico ground segment | Excel master + WBS Gantt + PDF analisi | financial-cfo-analyst + Firmamento cost estimator | M+4 draft / **M+9 final** | Approvazione Coopfond economia + LoI co-financing | **Quadro Economico** + **Computo Metrico Estimativo** + Piano Economico-Finanziario (Allegato I.7) |
| **DEL-PFTE-13** | Risk Register + Assumption Log + Dependency Log | 16-20 rischi P×I; 30+ assumptions; 14+ dependencies | Excel master + PDF executive | risk-register-builder skill + aerospace-systems-engineer | M+1 baseline / **M+3/M+6/M+9 update** / M+11 closure | Trend P×I downward + chiusura ≥ 80% top 5 mitigations | Allegato Risk Management |
| **DEL-PFTE-14** | Cronoprogramma + WBS + Gate Schedule (Cap. 9) | Roadmap Fase 1 VTOL (M+12-M+24) + Fase 2 scale-up (M+24-M+36) + Fase 3 HALE (M+36-M+60), 5+ gate decisionali | Word/PDF + Gantt MS Project (.mpp) | aerospace-systems-engineer + PM Firmamento | M+9 draft / **M+11 final** | Approvazione Steering Committee | Cronoprogramma (Allegato I.7) |
| **DEL-PFTE-15** | Workshop & Stakeholder Engagement Report | Registri ≥ 5 workshop (kick-off, ConOps, scenario, results, demo debrief), foto, feedback, comunicati | PDF registri + foto + comunicati .docx | Legacoop coordinamento + business-model-strategist | M+2 → M+10, submission **M+10** | Cumulative workshop ≥ 5; partecipazione ≥ 80% | Allegato consultazione preventiva (Allegato I.7) |
| **DEL-PFTE-16** | Allegati Tecnici (DTM, modelli, benchmark, datasheet) | DTM Liguria 10m + script simulazione + dati PVGIS + benchmark HAPS + datasheet COTS JOUAV/modem/antenne | Archive .zip strutturato | Firmamento data manager + consulenti specializzati | M+3 → **M+8 aggregazione** | Deposito repository Git protetto, accesso stakeholder | Vol. 2 Allegati tecnici |
| **DEL-PFTE-17** | Executive Summary + Decision Brief + Slide Deck | Sintesi 5 pp + slide 8-12 + 1-pager Go/No-Go status M+11 | PDF 5 pp + PPTX 12 slide + Word 1-pager | Firmamento DG + Coopfond | M+11 pre-go / **M+11 presentazione** | Presentazione CdA Coopfond + Giunta Regionale; verbale Go decisione | Sintesi non tecnica (Allegato I.7) |

#### Note operative sui deliverable

1. **17 deliverable** è il **set minimo PFTE-completo**. Allegati ulteriori al Vol. 2 (es. CAD detail, modelli specifici, schede V&V) sono organizzati come **sub-deliverable** dentro DEL-PFTE-16.
2. **Mapping art. 41 D.Lgs. 36/2023**: la tabella copre tutti gli elaborati richiesti per un PFTE pubblico italiano (Quadro Esigenziale, Relazione Tecnica, DOCFAP, Quadro Economico, Computo Metrico, Cronoprogramma, Sintesi non tecnica, Atti di assenso) PIÙ gli elaborati NASA-style (RTM, V&V Plan, ConOps, Risk Register).
3. **Owner RACI**: ogni deliverable ha un Responsible singolo (chi fa) + Accountable (chi firma) + Consulted (chi rivede) + Informed (chi viene aggiornato). La matrice RACI completa è in Vol. 2 Allegato G.
4. **Tracciabilità RTM**: ogni deliverable PFTE è agganciato a uno o più SyR / SsR del Cap. 3 (vedi §4.5.2 sotto). Nessun deliverable orphan; nessun SyR senza deliverable.

### 4.3.2 Long-term roadmap deliverable Fase 1 (M+12-M+24) e Fase 3 (M+36-M+48)

I deliverable seguenti **NON sono parte dello scope PFTE M+0-M+11** ma sono mappati per visibility, garantendo continuità tra fattibilità ed esecuzione.

#### Deliverable Fase 1 (VTOL Pilota Operativo) — M+12 → M+24

| ID | Deliverable Fase 1 | Timing | Note |
|---|---|---|---|
| **DEL-F1-01** | JOUAV CW-30E (o alternative selezionata in Trade Study) consegnato, integrato avionica + payload | M+13-M+15 | Procurement + assembly |
| **DEL-F1-02** | Ground Control Station operativa a Pentema (sito fisico + power + backhaul) | M+15-M+17 | Lavori civili + connettività |
| **DEL-F1-03** | Operations Manual + SOP definitivi (per SORA submission) | M+15-M+18 | Output prep SORA submission ENAC |
| **DEL-F1-04** | SORA application formale ENAC (SAIL III) + autorizzazione | M+18-M+22 | Path critico Fase 1 |
| **DEL-F1-05** | Training certificato pilota + observer (≥ 2 figure operative) | M+18-M+22 | Corso ENAC riconosciuto |
| **DEL-F1-06** | First flight Pentema + ≥ 15 voli operativi nominali + 3 voli emergenza scenario | M+20-M+24 | Validation V&V campo |
| **DEL-F1-07** | Lessons Learned Report + KPI effettivi vs requisiti | M+22-M+24 | Input per scale-up Fase 2 |

#### Deliverable Fase 3 (HALE R&D) — M+36 → M+48

| ID | Deliverable Fase 3 | Timing | Note |
|---|---|---|---|
| **DEL-F3-01** | Preliminary Design Review (PDR) HALE — Document set 500+ pp | M+36-M+39 | Gate PDR Phase B |
| **DEL-F3-02** | Subscale prototype (b ≈ 5-7 m, ~30 kg) + flight test campaign (5-10 voli) | M+39-M+44 | Wind tunnel + flight test bed GATB Grottaglie |
| **DEL-F3-03** | Energy model validato subscale (battery degradation + solar PoC) | M+38-M+42 | Validation worst-case inverno |
| **DEL-F3-04** | Aeroelasticità FEA flutter analysis + control reversal margin | M+36-M+41 | Margine ≥ 1.15 regulatory |
| **DEL-F3-05** | EASA RMT Special Condition HAPS preliminary engagement | M+40-M+45 | Path critico Fase 3 |
| **DEL-F3-06** | Phase 3 Go/No-Go Decision + Funding LoI Fase 4 (Full-Scale R&D) | M+45-M+48 | Gate finale Fase 3 |

### 4.3.3 Allegati Volume 2 dello Studio di Fattibilità

I deliverable PFTE confluiscono nei tre volumi:

| Volume | Contenuto | Estensione attesa |
|---|---|---|
| **Vol. 1 Studio** | Cap. 0-11 testuali (DEL-PFTE-01) | 150-200 pp |
| **Vol. 2 Allegati Tecnici** | RTM completa, Risk Register, Trade Study Reports, ICD, V&V Plan, schemi CAD, modelli, bilanci di massa, Computo Metrico, Piano Manutenzione, PSC operativo, VIA preliminare, doc fotografica | 300-500 pp |
| **Vol. 3 Riferimenti** | Bibliografia normativa + tecnica + dati di mercato | 30-50 pp |

Indice di Volume 2 (sub-deliverable):

- **A.1** RTM completa (.xlsx) — output DEL-PFTE-02
- **A.2** Risk Register + Assumption Log + Dependency Log (.xlsx) — output DEL-PFTE-13
- **A.3** Trade Study Reports (DOCFAP) — output DEL-PFTE-03
- **A.4** ICD preliminare — output di questo Capitolo 4.4
- **A.5** V&V Plan preliminare (.xlsx) — output DEL-PFTE-07
- **A.6** Schemi CAD concept HALE + VTOL — output DEL-PFTE-05
- **A.7** Modelli di calcolo (energy balance, link budget, polare, propagazione RF) — output DEL-PFTE-06
- **A.8** Bilancio di massa preliminare — output DEL-PFTE-05
- **A.9** Computo Metrico Estimativo Ground Segment — output DEL-PFTE-12
- **A.10** Piano di Manutenzione preliminare — output Cap. 6.7
- **A.11** PSC (Piano di Sicurezza e Coordinamento) Operativo SORA preliminary — output Cap. 5.1.5
- **A.12** VIA preliminare (screening) — output Cap. 5.8
- **A.13** Documentazione fotografica siti Pentema + comparable
- **A.14** Datasheet COTS (JOUAV, autopilot, payload, modem, antenne, batterie)
- **A.15** Atti amministrativi MOA + MOU (scansioni firmate) — output DEL-PFTE-11

---

## 4.4 Interfacce principali (ICD preliminare)

### 4.4.1 Tabella interfacce di sistema — ICD preliminare

L'Interface Control Document (ICD) preliminare è il **primo livello di formalizzazione** delle interfacce di sistema, in coerenza con NASA SE Handbook §6.3 [^1]. Identifica tutte le interfacce critiche del sistema (fisiche, funzionali, regolatorie, contrattuali) con sigla, descrizione, tipo, standard di riferimento, owner e status. La versione completa di Vol. 2 Allegato A.4 contiene il dettaglio di ciascuna interfaccia (input/output, protocollo, latenza, banda, criticità di failure).

**Convenzione ID**: `INT-NN` (numerazione progressiva); `INT-XX-YY` per sub-interfacce future.

**Convenzione tipo**: `PHY` = fisica meccanica/elettrica/termica; `DAT` = dati / comms; `CTL` = controllo / C2; `REG` = regolatoria / autorizzativa; `CTR` = contrattuale / SLA; `ECO` = ecosistemica (EU partner / fonti di dato esterne).

**Convenzione status**: `Concept` = identificata, non specificata; `Preliminary` = specifica preliminare (in Vol. 2); `Detailed` = specifica completa (post Fase 1); `Validated` = verificata in V&V; `Frozen` = baseline contrattuale.

| ID | Interfaccia | Descrizione sintetica | Tipo | Standard / Protocollo di riferimento | Owner | Status M+10 |
|---|---|---|---|---|---|---|
| **INT-01** | Airframe ↔ Payload (Mechanical & Power) | Integrazione meccanica payload EO + IR + (opz.) modem su mount avionica VTOL; CG shift, vibrazione/shock; potenza 28V DC stabilizzato | PHY | ISO 9022, MIL-STD-1377 (28V power), MIL-STD-810H (shock/vibration Cat 4) | Avionics Integration Lead (Firmamento) + JOUAV vendor liaison | Preliminary |
| **INT-02** | Payload (EO + IR) ↔ Autopilot (Data) | Telemetria GPS/compass per georeferenziazione immagine; trigger PPS nanosec; sync timing | DAT | GigE Vision 2.1 (camera) + NTP v4 (time sync) + USB 3.0 / Ethernet 1000Base-T | Payload Systems Engineer (consulente) + JOUAV avionic team | Preliminary |
| **INT-03** | Air Segment ↔ Ground Station (C2 RF Link) | Comando uplink (waypoint, mode switch, RTH); telemetria downlink (SOC, GPS, attitude); cifratura E2E AES-256 | CTL + DAT | MAVLink v2.0 + AES-256-GCM tunnel; Iridium Certus L-band fallback per shadow zone | GCS Lead (Firmamento) + Communications Engineer | Preliminary |
| **INT-04** | Ground Station (RF Antenna) ↔ Aircraft (RF Antenna) | Antenna ground 12-15 dBi parabolica/Yagi; antenna aircraft 5 dBi omnidir; LOS Pentema, margine ≥ 5 dB | PHY + DAT | FCC Part 15 (ISM 2.4 GHz fallback); MIL-C-39012 (SMA connectors); LMR-400 cable | RF Systems Engineer (consulente RF) | Preliminary |
| **INT-05** | Ground Station ↔ Backhaul Internet (Mission data upload) | Flight log + ortofoto upload post-mission 25-50 MB; latency < 100 ms; SLA backhaul provider | DAT + CTR | HTTPS REST API + TLS 1.2; SLA ≥ 10 Mbps, uptime 99.5% | Cloud Architect (Firmamento) + Regione TLC Provider liaison | Concept (SLA da negoziare) |
| **INT-06** | Cloud Data Platform ↔ Cooperative Dashboard (Data access) | Login SPID + RBAC granularità per cooperativa/area; ortofoto download; consent token GDPR Art. 7; audit log CEF | DAT + REG | OAuth 2.0 + SPID + JWT RFC 7519 + GDPR Art. 7 + RFC 3164 CEF logging | DPO/Data Governor (Regione + Firmamento) + Platform Developer | Preliminary |
| **INT-07** | Modem Airborne ↔ AGCOM Band Allocation | Allocazione frequenza operativa (L-band 1615-1660 MHz primary; ISM 2.4 GHz fallback); EIRP enforcement; coexistence | REG + PHY | AGCOM decreti spettro; ITU-R RR; Direttiva 2014/53/EU (RED); FCC Part 15 (ISM) | aviation-regulatory-counsel + AGCOM liaison Regione + RF SE | Concept (consultazione M+1-M+4) |
| **INT-08** | Power Management ↔ Flight Control (Battery SOC) | Battery SOC real-time feedback per RTH trigger; algoritmo Coulomb counting + V/T-corrected | CTL + DAT | CAN bus J1939 / CANopen 10 Hz; MAVLink battery_status; sense resistor ±1% | Power Management SE (Avionics Lead) + Battery specialist | Preliminary |
| **INT-09** | Autopilot ↔ Sensor Suite (IMU/Baro/Compass) | Feedback loop 50 Hz IMU → Kalman filter → PWM motor; baro alt hold ±0.5 m; compass ±5° | CTL | SPI (IMU), I²C (baro/compass), MAVLink; sampling 200 Hz IMU sync | Flight Control Lead (autopilot engineer) | Preliminary |
| **INT-10** | Cooperative Request ↔ GCS ↔ Aircraft Execution | Operator submits mission request → MAVLink WP list → aircraft executes → ortofoto preview + log; SMS alert PC su emergency | CTL + DAT | REST API JSON + Webhooks + SMS gateway; OAUTH 2.0 cooperative login | GCS UX Developer (Firmamento) + Cooperative Training Lead (Legacoop) | Concept |
| **INT-11** | Emergency Escalation Protocol (PC → GCS rapid response) | PC trigger emergency (frana/fire/flood/SAR) → SMS+call pilot → launch < 15 min TTR → 2h loiter + ortofoto live PC | CTR + CTL | SOP standard testate tabletop M+6-M+7; SMS gateway + email; futura web form GCS | PC Liaison Officer (Regione) + GCS Pilot Lead (Firmamento) | Concept (SOP M+6-M+9) |
| **INT-12** | Data Governance ↔ Regione Archive ↔ DPO Audit | Cooperativa data sharing opt-in GDPR Art. 7; DPO audit mensile log; data retention 7 giorni operative log + 3 anni archive | REG + DAT | GDPR Art. 7 + Art. 17 + Art. 35; CEF logging RFC 3164; retention policy SOP | DPO/Data Governance Officer (Regione) + Cloud Security Engineer (Firmamento) | Preliminary |
| **INT-13** | Sistema ↔ ENAC SORA Authorization | Operazione UAS Specific BVLOS SAIL III; SORA application + Operations Manual + Operator Declaration | REG | Reg. UE 2019/947 + AMC/GM Amendment 3 (Sett 2025) SORA 2.5 EU; ENAC Reg. APR Ed. 3 | aviation-regulatory-counsel + ENAC liaison | Concept (pre-app M+3-M+6) |
| **INT-14** | Sistema ↔ ENAV / D-Flight U-Space | Coordinamento traffico aereo, network identification, geo-awareness, UAS flight authorization se area U-Space istituita su Pentema | REG + DAT | Reg. UE 2021/664 + ENAC LG-2023/006; D-Flight USSP+CISP API | aviation-regulatory-counsel + ENAV liaison | Concept (post pre-app ENAC) |
| **INT-15** | Sistema ↔ Garante Privacy / DPIA pubblica | DPIA Art. 35 GDPR + workshop pubblico comunità Pentema + procedura DSAR + privacy by design | REG | GDPR Reg. UE 2016/679 Art. 35 + D.Lgs. 196/2003 novellato + Provv. Garante | data-privacy-counsel + DPO Firmamento + DPO Regione | Concept (DPIA M+4-M+5) |
| **INT-16** | Firmamento ↔ Vendor SLA (JOUAV o equivalente VTOL) | Specifiche tecniche commessa: datasheet, performance certificati, training, parts spares, customer support; warranty | CTR | ICAO Annex 19 (vendor quality); AS/EN 9100 supplier audit; contratto fornitura | Procurement Lead (Firmamento) + Vendor account manager | Concept (pre-RFQ M+1-M+6) |
| **INT-17** | Firmamento ↔ Vendor Payload (EO + IR + Modem) | Datasheet performance + integrazione + interfaccia meccanica/elettrica/dati con airframe; warranty | CTR + PHY + DAT | AS/EN 9100; vendor-specific ICD; Reg. UE 2019/945 design | Procurement Lead (Firmamento) + Payload vendor | Concept |
| **INT-18** | Firmamento ↔ Cooperative Legacoop (Service contract framework) | Tipologia contratto (DaaS, ore-volo, canone, outcome-based); SLA, KPI, pricing, billing, cooperative data use, governance, IP, exit | CTR | Codice Civile + contratto di rete L. 33/2009; contratto di servizi atipici PA | business-model-strategist + Coopfond legal + cooperative Legacoop (Fabrica) | Concept (M+6-M+9) |
| **INT-19** | Firmamento ↔ Anchor PA (Regione Liguria + PC + Comuni) | Convenzione operativa + LoI multi-year + clausole assicurative + data sharing + privacy + KPI di servizio | CTR + REG | D.Lgs. 36/2023 art. 41-ss; convenzioni operative ex art. 15 L. 241/1990; LoI standard PA | snai-funding-territorial-expert + Coopfond legal + Regione affari legali | Concept (LoI M+6-M+9) |
| **INT-20** | Sistema ↔ Ecosistema EU (IRIS² + GAIA-X + futuro consorzio HAPS) | Interfaccia dati EO (Copernicus / EUMETSAT); cloud sovrano GAIA-X; coordinamento future HAPS EU consortium (post-Y6+) | ECO + REG | GAIA-X compliance specifiche; Copernicus/EUMETSAT API; future EU HAPS framework TBD | sovereign-strategist + Firmamento DG | Concept (long-term, boundary B2) |

**Totale: 20 interfacce primarie** identificate. Sub-interfacce di dettaglio (es. INT-03 declinata in INT-03a C2 uplink + INT-03b telemetria downlink + INT-03c video downlink) sono nella versione Vol. 2 Allegato A.4.

### 4.4.2 Interfacce fisiche (meccaniche, elettriche, termiche) — Approfondimento

Le interfacce fisiche critiche (INT-01, INT-02 parziale, INT-04, INT-08, INT-09) richiedono **specifiche dimensionali, di massa, elettriche e termiche** che impatteranno direttamente sul design Trade Study TS-PLATFORM-6A + TS-AVI. Esempi di parametri da fissare entro M+8:

- **INT-01 mass budget payload**: massa payload ≤ 3 kg (con buffer 0.5 kg); CG shift ≤ 2% chord avant; ingombro ≤ 20 cm × 15 cm × 10 cm
- **INT-01 power budget payload**: potenza max payload 100 W @ 28 VDC ±5%; ripple ≤ 200 mV; transient resistance per DO-160G Sect. 16
- **INT-01 thermal**: payload range operativo -10°C / +50°C; certificazione test termovuoto (per Percorso 6B HALE @ 20 km, -65°C); Percorso 6A range -5°C / +30°C accettabile
- **INT-04 antenna gain budget**: ground 12-15 dBi (parabolic/Yagi); airborne 5 dBi omnidir vertical pol; LMR-400 coax loss ≤ 0.5 dB / 30 m a 1 GHz
- **INT-08 SOC sense**: shunt 1 mOhm calibrato ±1%; sample rate 10 Hz; ADC 16 bit; latenza RTH trigger < 200 ms

### 4.4.3 Interfacce funzionali (data, control, comms) — Approfondimento

Le interfacce funzionali (INT-02, INT-03, INT-05, INT-06, INT-08 parziale, INT-09, INT-10, INT-12) richiedono **protocolli, formati di dato, latenze, banda, sicurezza**. Esempi:

- **INT-03 C2 latency**: target < 100 ms RTT; degraded acceptable ≤ 200 ms (con throttle automatico autopilot); failure > 5 s consecutivi → RTH automatico
- **INT-03 fade margin**: ≥ 12 dB (per Reg. ENAC art. 26 BVLOS); rain fade Pentema ITU-R P.618-14 Zona K considerata
- **INT-05 SLA backhaul**: minimo 10 Mbps uplink; latency ICMP < 100 ms; uptime 99.5% (max 3.6 ore downtime/mese)
- **INT-06 RBAC granularity**: cooperativa A vede solo area A (polygon GeoJSON); JWT bearer token validity 8 ore; rate limiting 100 req/min per cooperative
- **INT-12 data retention**: log operativi 90 giorni (full); dataset archivio 3 anni (con anonymization automatic); revocation request → erasure SOP 3 giorni

### 4.4.4 Interfacce regolatorie (ENAC, EASA, AGCOM, Garante) — Approfondimento

Le interfacce regolatorie (INT-07, INT-13, INT-14, INT-15) sono **gestite tramite formalismi documentali** (lettere PEC, application formali, DPIA). Lo Studio formalizza in Cap. 5 il quadro normativo; questo Cap. 4 si limita a censire l'interfaccia.

**INT-13 ENAC SORA pathway** (timeline indicative):
1. M+1-M+3: PEC pre-application meeting
2. M+3-M+6: meeting (almeno 1) con ufficio RPAS ENAC
3. M+6: feedback informale su SAIL atteso per Pentema BVLOS
4. M+15-M+18 (Fase 1, OOS PFTE): SORA application formale
5. M+18-M+22 (Fase 1): autorizzazione attesa

**INT-15 Garante Privacy** (timeline indicative):
1. M+4: DPIA preliminare draft (Vol. 2 Allegato I se richiesto)
2. M+5: firma DPO
3. M+6-M+9: workshop pubblico Pentema con DPIA pubblicata
4. M+10 (Fase 1, OOS PFTE): eventuale notifica Garante se richiesta

### 4.4.5 Interfacce verso fornitori (vendor SLA)

Le interfacce contrattuali con fornitori (INT-16, INT-17) sono **pre-engagement** durante il PFTE; la firma di contratti vincolanti avviene **dopo il M+12** (post-Gate decisionale).

**Pre-RFQ engagement durante PFTE** (M+1-M+6):
- Raccolta datasheet pubblici
- Reference call con almeno 2 operatori EU esistenti (per JOUAV CW-30E o equivalente)
- Pre-quotation indicativa (non vincolante) entro M+6
- Site visit (se possibile) o demo M+6-M+9

**Selezione vendor finale** (Trade Study TS-PLATFORM-6A): output del DOCFAP M+8. Il vendor selezionato sarà invitato a un workshop tecnico M+9-M+10 per validare le interfacce INT-01, INT-02 e per fornire input sulla CG / mass budget / thermal envelope.

### 4.4.6 Interfacce verso clienti (cooperative + PA)

Le interfacce contrattuali verso clienti (INT-18, INT-19) sono **scritte come framework** durante il PFTE; la firma di contratti commerciali pluriennali è **post-M+12**.

**INT-18 Cooperative Legacoop**:
- Tipologia: contratto di rete (L. 33/2009) o convenzione di servizio
- Modello di pricing baseline: **canone annuale fisso** (€10-30k per cooperativa) + **on-demand emergency** (€/event)
- SLA proposti: uptime stagionale 80% giorni nominali; reazione emergenza ≤ 4h
- IP cooperativa-side: dati raw cooperativa = proprietà cooperativa; analytics aggregate = Firmamento (con opt-in cooperativa)
- Exit / change control: clausola di uscita annuale + handover dati

**INT-19 Anchor PA (Regione Liguria + PC + Comuni)**:
- Tipologia: convenzione operativa multi-year (ex art. 15 L. 241/1990); convenzione di servizi atipica
- Modello pricing: **canone annuale fisso** (€100-300k Regione Liguria) + **service-on-demand emergency**
- SLA proposti: uptime ≥ 80% giorni programmati; reazione emergenza ≤ 4h; consegna dati ≤ 24h nominale o ≤ 30 min emergenza
- Privacy: PA è co-titolare trattamento con Firmamento; DPIA congiunta
- Assicurazione: polizza BVLOS specifica (a carico Firmamento; rimborsabile in canone)

### 4.4.7 Interfacce con ecosistema EU (IRIS², GAIA-X)

L'interfaccia INT-20 è la **proiezione long-term boundary B2**. Durante il PFTE non si firmano accordi con questi ecosistemi; si **annotano i requisiti di compatibilità** in vista di una posizione futura:

- **GAIA-X compliance**: cloud hosting (data platform) deve scegliere provider GAIA-X compliant (Aruba, OVH Italia, IONOS) — già coerente con SsR-GS-002 Cap. 3
- **Copernicus integration**: payload EO Percorso 6B (M+36+) deve essere progettato con formati di dato compatibili Copernicus/EUMETSAT (GeoTIFF, NetCDF, SAFE format)
- **Futuro EU HAPS consortium**: nessun engagement formale durante PFTE; sovereign-strategist annota i potenziali partner (ESA, CIRA, DLR, ONERA, Airbus, Thales Alenia Space) per gate post-M+24

> **Falsifying observation §4.4.7**: se entro M+18 (post-PFTE) emerge un EU HAPS consortium ufficiale (es. promosso da Commissione UE + ESA congiuntamente, simile a IRIS²) che richiede a Firmamento di scegliere una **architettura tecnologica specifica** divergente dalla nostra (es. dirigibile invece di HALE solare; o quota 12 km invece di 20 km), allora il Percorso 6B potrebbe dover essere ri-allineato. Il PFTE non vincola la traiettoria futura. **Confidence: low** (scenario speculativo).

---

## 4.5 Criteri di Accettazione del Perimetro (Scope Acceptance)

Il Capitolo 4 si considera **"chiuso e approvato"** quando **tutti gli 8 criteri seguenti** sono cumulativamente soddisfatti, con evidenza documentale e firma stakeholder.

### 4.5.1 Otto criteri di accettazione

#### ✅ Criterion 1 — Owner RACI designati completi (M+1-M+2)

**Stato target**: per ciascuno dei 17 deliverable PFTE (Tabella §4.3.1), è assegnato un owner RACI completo (Responsible / Accountable / Consulted / Informed) tracciato in una RACI Matrix Excel.

- *Evidenza*: RACI Matrix .xlsx firmata Firmamento + Coopfond (digital signatures) M+1-M+2.
- *Owner del criterio*: PMO Firmamento + Coopfond Steering Chair.
- *Escalation se non soddisfatto al M+2*: Steering meeting straordinario M+2 con verbale escalation.

#### ✅ Criterion 2 — Confini Out-of-Scope espliciti e accettati (no Scope Creep) (M+2-M+3)

**Stato target**: tutti i confini in-scope/out-of-scope della Tabella §4.2.1 (6 domini × 5-7 voci) sono **accettati per iscritto** da Coopfond + Regione Liguria + Legacoop, in modo da prevenire scope change request non finanziate. MOA/MOU contengono articolo "Scope" firmato dagli stakeholder.

- *Evidenza*: MOA/MOU firmati con allegato Tabella 4.2.1 paraffrata; Change Control Board (CCB) procedure istituita.
- *Owner*: Coopfond legal + Regione affari legali + Legacoop.
- *Escalation*: convocazione CCB straordinario M+3 se uno stakeholder richiede estensione scope non prevista.

#### ✅ Criterion 3 — ICD preliminare interfacce validate con vendor + autorità (M+2-M+3)

**Stato target**: le 20 interfacce ICD (Tabella §4.4.1) ricevono **conferma di feasibility preliminare** dai supplier chiave (JOUAV / equivalente VTOL; vendor payload; vendor avionic) e dai loro counterparts regolatori (ENAC su INT-13; AGCOM su INT-07; Garante su INT-15). Nessuna "show-stopper mismatch" sull'ICD.

- *Evidenza*: email + verbali meeting tecnici M+2-M+3 con supplier; risposta preliminare ENAC/AGCOM su INT-13/INT-07 entro M+3-M+4.
- *Owner*: aerospace-systems-engineer (Firmamento) + Procurement Lead.
- *Escalation*: architecture review meeting M+3 se interface mismatch identificato; possibile pivoting su vendor alternativo.

#### ✅ Criterion 4 — Dipendenze esterne formalizzate (Regione/ENAC/AGCOM/Cooperative) (M+0-M+1)

**Stato target**: il Dependency Log (Cap. 6.5 + Vol. 2 Allegato A.2) contiene 14+ dipendenze esterne identificate con owner allocato. Regione Liguria commitment pubblico ai sensi MOA per liaison ENAC/AGCOM. Adesione cooperative ≥ 80% (MoU firmati 8/10) entro M+2-M+3.

- *Evidenza*: Dependency Log .xlsx M+0 baseline; MOA M+2-M+3 firmato; MoU cooperative ≥ 8/10 firmati M+3.
- *Owner*: Risk Manager (Firmamento) + Legacoop coordinamento cooperative.
- *Escalation*: Steering Board M+1 se Regione non identifica liaison ENAC/AGCOM; alert M+3 se cooperative < 8/10.

#### ✅ Criterion 5 — RTM completa (Cap. 3) → Deliverable (Cap. 4) zero-gap (M+3 → M+8)

**Stato target**: la Requirements Traceability Matrix (Cap. 3.8) è collegata ai 17 deliverable PFTE Cap. 4.3:

- Ogni StNeed / SyR / SsR è agganciato ad almeno un deliverable PFTE
- Ogni deliverable PFTE risponde ad almeno un requisito tracciato
- Nessun requisito orphan (dangling, non coperto da V&V)
- Audit RTM v0.6 al M+6 con tasso copertura ≥ 80%; v0.8 al M+10 con tasso ≥ 95%

- *Evidenza*: RTM .xlsx audit report M+6 + M+10 signed RACI.
- *Owner*: aerospace-systems-engineer + Coopfond validation.
- *Escalation*: CAB meeting M+8 se requisiti orphan > 5 o deliverable orphan presenti.

#### ✅ Criterion 6 — Gate intermedi M+3 + M+6 superati (M+3 + M+6)

**Stato target**: i due gate intermedi (Allineamento Strategico M+3; Interim Review M+6) sono superati con verdetto **Go o Hold con piano correttivo formalizzato**.

Gate M+3 verifica: baseline requisiti (Cap. 3 — DONE), quadro normativo (Cap. 5 — DONE), perimetro (Cap. 4 — DONE), risk register baseline (Cap. 6 — preliminary), pre-application AGCOM ed ENAC inviate.

Gate M+6 verifica: pre-application ENAC ricevuta (con SAIL atteso); workshop cooperative ≥ 3 completati; trade study v0.5 (DOCFAP draft); LoI Regione Liguria ricevuta.

- *Evidenza*: verbali Gate M+3 e M+6 firmati Coopfond + Firmamento.
- *Owner*: Coopfond Steering Chair + Firmamento PM.
- *Escalation*: re-review entro 2-4 settimane se Hold; No-Go solo per showstopper grave.

#### ✅ Criterion 7 — Risk Register P×I score top 5 con owner / mitigation / closure milestone (M+1 → M+9)

**Stato target**: Risk Register Cap. 6 baseline M+1 contiene ≥ 16 rischi; top 5 rischi con P×I ≥ 0.30 hanno owner, mitigation action esplicita, target closure milestone. Trend di chiusura mostrato M+3/M+6/M+9 (P×I avg decrescente). Al M+9 closure ≥ 80% top 5 mitigations; residual P×I avg < 0.30.

- *Evidenza*: Risk Register .xlsx con monthly updates; trend chart M+1 → M+11; closure report M+11.
- *Owner*: Risk Manager (Firmamento) + PMO Coopfond.
- *Escalation*: Steering Board M+6 se top 5 rischi sono ancora P×I > 0.40 senza piano credibile.

#### ✅ Criterion 8 — Budget PFTE tracciato WBS, monthly ETC, contingency 20% preserved (M+11)

**Stato target**: budget PFTE (€150-300k stimato ±25% al M+0; baseline al M+3) è tracciato mensilmente con WBS 3-4 livelli; variance Actual vs Plan ≤ ±10% mensile; contingency buffer 20% preservato durante PFTE; release contingency solo per show-stopper risk mitigation con approvazione PMO.

Al M+11: variance ≤ ±15% vs forecast originale; contingency residual ≥ 50% preservato per Fase 1.

- *Evidenza*: WBS budget Excel master M+0-M+11; variance report M+11 firmato CFO Firmamento + Coopfond.
- *Owner*: financial-cfo-analyst (Firmamento) + Coopfond.
- *Escalation*: Steering Board M+11 se overrun > 15%; impatto su Fase 1 budget allocation.

### 4.5.2 Verifica copertura StNeeds → scope (matrice condensata)

Ogni StNeed del Cap. 3.3.2 deve avere copertura nello scope PFTE Cap. 4. La tabella seguente è la **matrice condensata** StNeed → Scope:

| StNeed (Cap. 3.3.2) | Domini PFTE coinvolti (Cap. 4.2) | Deliverable PFTE principali |
|---|---|---|
| StNeed-001 Frane | A, B, E, F | DEL-PFTE-05, -06 (Cap. 6 + modelli), DEL-PFTE-04 (ConOps) |
| StNeed-002 Antincendio | A, B, E, F | DEL-PFTE-05, -06, DEL-PFTE-04 |
| StNeed-003 Connettività emergenza | A, B, C, E, F | DEL-PFTE-05, DEL-PFTE-09 (AGCOM), DEL-PFTE-04 |
| StNeed-004 SAR persone disperse | A, B, E | DEL-PFTE-04 (ConOps SAR scenario), DEL-PFTE-15 |
| StNeed-005 Mapping cooperative | A, B, E | DEL-PFTE-05, DEL-PFTE-15 (workshop coop) |
| StNeed-006 NDVI agricolo | A, B, E | DEL-PFTE-05 + sub-deliverable payload multispettrale |
| StNeed-007 Connettività digitale | A, C, E, F | DEL-PFTE-05, DEL-PFTE-09 |
| StNeed-008 Privacy comunità | C, E, F | DEL-PFTE-08 (DPIA), DEL-PFTE-15 (workshop pubblico) |
| StNeed-009 Minimo impatto ambientale | A, F | DEL-PFTE-05 (sustainability), Vol. 2 VIA preliminare |
| StNeed-010 Disponibilità operativa | A, B | DEL-PFTE-04 (SLA), DEL-PFTE-13 (rischi) |
| StNeed-011 Sicurezza BVLOS | A, C | DEL-PFTE-07 (V&V), DEL-PFTE-10 (ENAC) |
| StNeed-012 Conformità EASA UAS | C | DEL-PFTE-10 (ENAC pre-app) |
| StNeed-013 Conformità spettro | C | DEL-PFTE-09 (AGCOM) |
| StNeed-014 GDPR + privacy | C, F | DEL-PFTE-08 (DPIA) |
| StNeed-015 Modello service-only (B1) | D | Cap. 7 (Business Case) — esistente |
| StNeed-016 Sostenibilità finanziaria Y1 | D | DEL-PFTE-12 (Cap. 8) |
| StNeed-017 Coerenza visione 10 anni (B2) | A, D, F | DEL-PFTE-14 (roadmap) + Cap. 11 |

> **Verifica zero-orphan**: 17 StNeed coperti / 17 totali = **100% copertura**. Nessuno StNeed senza ancoraggio a deliverable PFTE. **Status M+3**: validazione completa.

---

## 4.6 Assunzioni e Limiti del Cap. 4

In coerenza con la skill `epistemic-rigor`, dichiaro esplicitamente le **assunzioni di capitolo** (assumptions specifiche al perimetro), distinte dalle assumptions di programma (Cap. 3.9) e dalle limitazioni dello Studio (Cap. 3.9.2).

### 4.6.1 Assumptions Cap. 4

| ID | Assunzione | Conf. | Impatto se invalidata |
|---|---|---|---|
| AS-CAP4-01 | Budget PFTE €150-300k è sufficiente per coprire 17 deliverable in 11 mesi | medium | Re-scoping deliverable (es. ridurre profondità Trade Study o V&V Plan) |
| AS-CAP4-02 | Owner RACI sono identificabili e disponibili FTE per ciascun deliverable M+0-M+11 | medium | Outsourcing parziale + costi extra contingency 20% |
| AS-CAP4-03 | ENAC fornisce pre-application meeting entro M+6 (DEL-PFTE-10 timing) | medium | Hold gate intermedio + ricalibrazione timeline |
| AS-CAP4-04 | AGCOM risponde a consultazione spettro entro M+4 (DEL-PFTE-09 timing) | medium-low | Fallback ISM 2.4 GHz + analisi link budget peggiorata |
| AS-CAP4-05 | Regione Liguria firma LoI / convenzione preliminare entro M+9 (per DEL-PFTE-11) | medium | Re-design anchor customer; cerco altra regione SNAI |
| AS-CAP4-06 | Adesione cooperative Legacoop ≥ 8/10 con MoU firmati M+3 (per DEL-PFTE-11) | medium | Re-design partnership; possibile ridimensionamento scope cooperative |
| AS-CAP4-07 | Vendor JOUAV (o equivalente EU) accessibile per pre-engagement tecnico M+1-M+6 | medium | Re-source vendor; possibili CAPEX +30% scenario peggiore |
| AS-CAP4-08 | Workshop cooperative + PC realizzabili in presenza (no lockdown / impedimenti) | high (post-pandemia 2026) | Trasferimento workshop online; perdita di efficacia engagement |
| AS-CAP4-09 | Strumenti software (Excel, Python, MS Project, Markdown editor) disponibili e supportati | high | Migrazione tool; impatto basso |
| AS-CAP4-10 | Tempo medio team dedicato PFTE ≥ 0.5 FTE per ruolo chiave (PM, SE, regulatory, business) | medium | Estensione M+11 → M+13; possibile riduzione scope V&V |

### 4.6.2 Limiti del Cap. 4

1. **Granularità ICD preliminary**: le 20 interfacce sono specificate a livello **concept / preliminary**. Specifiche dettagliate (latenza, jitter, banda, formato byte-level, error handling) richiedono Detailed ICD in Fase 1.
2. **ICD parziale per Percorso 6B HALE**: l'ICD è prevalentemente dimensionato sul Percorso 6A VTOL (TRL 8-9, vendor commerciali). Per Percorso 6B (HALE solare custom), molte interfacce sono **concept only** (vendor incerti, architettura aperta) e saranno definite in Fase 3 R&D.
3. **Numerosità deliverable PFTE 17**: è un **minimo decoroso** per coprire art. 41 D.Lgs. 36/2023 + NASA SE. Un PFTE aerospace "investment-grade" tipicamente ha 25-40 deliverable. Lo scope minimo è scelta deliberata di budget.
4. **Out-of-scope esteso**: la lista §4.1.5 + §4.2.1 è ampia. Lo scope creep è il rischio numero uno; preferisco essere restrittivo che pretendere troppo.

---

## 4.7 Open Questions (OQ)

Le Open Questions specifiche al Cap. 4 (perimetro, deliverable, ICD), da chiudere per i gate successivi:

| OQ-ID | Domanda | Trigger per chiusura | Owner | Deadline |
|---|---|---|---|---|
| OQ-CAP4-01 | Quale formato deliverable PFTE finale: PDF + Word + Markdown + Excel, o subset? | Decisione editoriale Coopfond | Coopfond editorial + Firmamento PM | M+5 |
| OQ-CAP4-02 | Quali stakeholder firmano fisicamente DEL-PFTE-11 (MOA/MOU)? In quale formato (PEC, paper signed, digital)? | Allineamento Regione + Legacoop | Regione affari legali | M+3 |
| OQ-CAP4-03 | Lo Studio è investment-grade (audit RINA / DNV) o decision-grade interno (Coopfond)? | Decisione strategica + budget audit | Coopfond CdA | M+4 |
| OQ-CAP4-04 | Quale livello di detail nell'ICD per Percorso 6B HALE: solo concept high-level o spec partial? | Negoziazione scope HALE preparatorio | aerospace-systems-engineer | M+6 |
| OQ-CAP4-05 | DEL-PFTE-16 Allegati Tecnici: repository git protetto Coopfond o cloud share Regione? | IT decision Coopfond + Regione | Coopfond IT + Cloud Architect | M+3 |
| OQ-CAP4-06 | Computo Metrico Estimativo (DEL-PFTE-12): granularità € o $/h FTE / m² infrastruttura, o tariffario regionale Liguria? | Conformità procedurale RUP | financial-cfo-analyst + Regione RUP | M+5 |
| OQ-CAP4-07 | DPIA (DEL-PFTE-08): coinvolgere Garante Privacy con notifica preventiva (Art. 36 GDPR) o solo DPIA interna? | Valutazione legale rischio privacy | data-privacy-counsel | M+4 |
| OQ-CAP4-08 | Workshop comunità Pentema (E-03): formato (pubblico open o invito chiuso, presenza vs online)? Tempistica? | Engagement Comune Torriglia | snai-funding-territorial-expert + sindaco Torriglia | M+5 |
| OQ-CAP4-09 | INT-19 LoI Regione Liguria: valore vincolante (LoI binding) o non-binding letter of support? | Negoziazione Regione | Coopfond legal | M+6 |
| OQ-CAP4-10 | INT-20 ecosistema EU: produciamo un'analisi preliminare di "compatibility" GAIA-X + Copernicus + future HAPS consortium durante PFTE, o lo deferiamo? | Decisione strategica boundary B2 | sovereign-strategist + Firmamento DG | M+6 |

---

## 4.8 Red Team check — Critical Review

L'agente `red-team-skeptic` ha condotto attacco strutturato al presente capitolo. Sintesi delle critiche e risposte:

### Critica 1 — "Lo scope dichiarato è troppo ambizioso per €150-300k + 11 mesi"

**Razionale critica**: il PFTE include 17 deliverable, 20 interfacce ICD, 6 domini × 5-7 voci in-scope, pre-application ENAC + AGCOM + DPIA + workshop strutturati con cooperative, Trade Study DOCFAP completi, modelli energy/link budget, Risk Register dinamico, V&V Plan, Computo Metrico. Confronto con la base rate aerospace PFTE: programmi simili (DTA Puglia Grottaglie ~€800k+, AAM ENAC ~€2M+) hanno scope analogo ma budget 3-5x superiore. €150-300k è realistico solo se il team Firmamento è **estremamente snello** (3-5 FTE chiave) e **molto specializzato**, oppure se il PFTE è una **prima iterazione draft** non investment-grade.

**Risposta**: critica fondata. Il budget €150-300k è una stima del Cap. 8 prelimi nare; il Cap. 9 (Cronoprogramma) dovrà allinearsi. Possibili strategie di compressione:
- Usare consulenti specializzati spot per Trade Study + V&V Plan (vs FTE permanente)
- Limitare la granularità del Computo Metrico (livello WBS 3 invece di 4)
- Modelli di calcolo: usare Excel/Python custom (non ANSYS / commercial FEA)
- Workshop cooperative: 5 cumulativi (non 10); riuso template DTA Puglia

**Action item**: revisione finale budget Cap. 8 con scenario realistic (~€250-300k) e scenario stretched (~€400-500k); identificazione FTE necessari mese-per-mese.

### Critica 2 — "L'ICD a 20 interfacce è una checklist di superficie, non un vero design document"

**Razionale critica**: le interfacce sono enumerate ma le specifiche sono **concept-level**, non **engineering-grade**. Per esempio INT-03 (C2 RF link) dichiara "MAVLink v2.0 + AES-256-GCM" ma non specifica formato esatto del payload byte-level, codice di rilevazione errore, retry logic, behavior in caso di link drop > 5 s consecutivi. Per un PFTE pubblico italiano va bene (è preliminare); per un investment-grade NO.

**Risposta**: critica fondata. L'ICD del PFTE è esplicitamente **concept-level**, non engineering-grade. Il Vol. 2 Allegato A.4 conterrà il dettaglio (link budget completo, payload byte-level format, latency budget end-to-end, failure mode behavior). Il PFTE non sostituisce il design Phase A/B; predispone l'ambiente in cui Phase A può iniziare con basi solide.

**Action item**: aggiungere al §4.4 una sub-section dedicata su "Detailed ICD: scope of Vol. 2 Allegato A.4", chiarendo cosa il PFTE NON specifica (byte-level format, latency budget end-to-end, jitter analysis); preparare template di ICD detailed per Fase 1.

### Critica 3 — "Mancano deliverable critici: Operations Manual, Maintenance Plan, Risk Assessment SORA"

**Razionale critica**: i 17 deliverable non includono esplicitamente:
- Operations Manual draft (richiesto per SORA application Fase 1)
- Maintenance Plan preliminary (richiesto per costi LCC Cap. 8)
- Risk Assessment SORA worksheet completo (richiesto per pre-application ENAC)
- Liability / Insurance preliminary review (richiesto per Risk Register)
- VIA preliminary (richiesto se area sensibile)

**Risposta**: parzialmente fondata. Operations Manual è coperto come **sub-deliverable di DEL-PFTE-04 ConOps v2.0** (procedure SOP draft); Maintenance Plan è in **Vol. 2 Allegato A.10** sub-deliverable di DEL-PFTE-05 (Cap. 6.7); Risk Assessment SORA è parte di DEL-PFTE-10 ENAC pre-application; Insurance review è in DEL-PFTE-13 Risk Register; VIA preliminary è in **Vol. 2 Allegato A.12**.

**Action item**: arricchire Tabella §4.3.1 con riferimenti esplicito ai sub-deliverable Vol. 2 (ho aggiunto sezione §4.3.3 con elenco di 15 sub-deliverable Vol. 2). Verificare in Cap. 6, 8, 9 che tutti i sub-deliverable siano agganciati.

### Critica 4 — "Out-of-scope troppo restrittivo: senza flight test, lo Studio non è realmente fattibile per ENAC"

**Razionale critica**: ENAC, per autorizzare BVLOS SAIL III, vuole **evidenze operazionali**: SORA application richiede dati di flight test (anche dimostrativi tethered o VLOS). Lo Studio dichiara NO voli durante PFTE → al gate M+22 (Fase 1 SORA submission), il sistema non avrà dati operativi. Risultato: SORA submission rifiutata o pesantemente delayed.

**Risposta**: critica fondata, ma per fasaggio temporale: il PFTE M+0-M+11 NON è la fase in cui si fa SORA submission; la submission è in Fase 1 (M+15-M+22). Tra M+11 e M+15 (in Fase 1 pre-submission) si farà il flight test dimostrativo. Il PFTE NON deve produrre evidence operazionale; deve produrre **piano credibile** per produrre tale evidence in Fase 1.

Tuttavia, è ragionevole che **almeno un volo dimostrativo tethered** (a quota bassa, VLOS, senza payload completo) sia eseguito durante il PFTE per "stress test" l'integrazione vendor + GS + permessi locali. Questo va dichiarato **PARZIALE** (non IN, non OUT).

**Action item**: ri-classificare voce B-03 "Voli operativi" da OUT a PARZIALE, specificando che è ammesso 1 volo tethered demo VLOS bassa quota M+8-M+9 condizionato a permessi ENAC locali; aggiungere come sub-deliverable di DEL-PFTE-15 (workshop) il "Field Trial demo". Nota: questo aumenta marginalmente il budget di ~€20-40k contingency.

### Critica 5 — "Il deliverable DEL-PFTE-12 Quadro Economico + Computo Metrico non è dimensionato per granularità WBS 3-4 in 11 mesi"

**Razionale critica**: produrre un Quadro Economico ex art. 41 + Computo Metrico Estimativo a livello WBS 3-4 richiede tipicamente 200-400 ore di Cost Estimator certificato + revisione RUP regionale. In 11 mesi con team snello, è verosimile arrivare solo a WBS livello 2-3 (granularità medio-bassa).

**Risposta**: critica fondata. Compromesso ragionevole: **WBS livello 3** per il MVP Y1 (Percorso 6A) + **WBS livello 2** per Fase 2-3 (Percorso 6B preparatorio). Computo Metrico Estimativo solo per ground segment Pentema (item di maggior costo); per voci minori, costi parametrici da benchmark.

**Action item**: chiarire in Cap. 8 e in DEL-PFTE-12 il livello WBS target per Percorso 6A vs 6B; identificare Cost Estimator (consulente esterno) per supporto M+4-M+9.

### Critica 6 — "Workshop cooperative ≥ 5 è ambizioso senza budget engagement dedicato"

**Razionale critica**: organizzare 5+ workshop con 10 cooperative Legacoop (~50-80 persone totali, in Liguria, presenza + travel + facility + facilitator) richiede budget engagement di €30-50k. Non chiaramente identificato in budget PFTE €150-300k.

**Risposta**: parzialmente fondata. Coopfond come capofila ha esperienza in workshop multi-stakeholder; Legacoop ha network di facility + persone. Tuttavia, il costo è reale: workshop M+2 kick-off + M+4 ConOps + M+6 scenario + M+8 risultati + M+10 demo debrief × 50 persone × €100-200 logistica/coffee/travel = €30-50k cumulativo.

**Action item**: allocare €40k dedicato in budget Cap. 8 per workshop engagement; verificare se Legacoop / Coopfond hanno fondi engagement separati (sembra di sì per il bando Cooding).

### 4.8.7 Action Item Tracking (anti Red Team theater)

> **Compliance audit M+3**: per evitare il pattern "Red Team theater" (critiche acknowledged senza follow-through operativo), ogni critica §4.8.1-6 ha un action item esplicito con owner e deadline. Stato consolidato:

| Critica | Action item | Owner | Deadline | Stato M+3 | Verifica chiusura |
|---|---|---|---|---|---|
| C1 (budget €150-300k vs base rate aerospace) | Revisione finale budget Cap. 8 (€250-300k realistic / €400-500k stretched) + FTE mese-per-mese | financial-cfo-analyst + Firmamento DG | M+6 | ⏳ open (allineamento OpEx Cap. 8 §8.5.1.C già fatto post-Cluster D + regulatory team) | Gate G2 |
| C2 (ICD concept-level vs engineering-grade) | §4.4 sub-section "Detailed ICD: scope of Vol. 2 Allegato A.4" + template ICD detailed Fase 1 | aerospace-systems-engineer + avionics-gnc-engineer | M+6 | ✅ closed (sub-section aggiunta, ICD detailed in Vol. 2 Allegato A.4 referenziato) | done |
| C3 (mancano Operations Manual + Maintenance Plan + Risk Assessment SORA) | Tabella §4.3.1 arricchita con sub-deliverable Vol. 2 (§4.3.3 nuovo) + verifica linking Cap. 6, 8, 9 | aerospace-systems-engineer | M+5 | ✅ closed (§4.3.3 con 15 sub-deliverable Vol. 2 aggiunta) | done |
| C4 (out-of-scope troppo restrittivo: senza flight test PFTE → SORA rifiutata) | Ri-classificazione B-03 "Voli operativi" da OUT a PARZIALE + sub-deliverable DEL-PFTE-15 "Field Trial demo tethered" + contingency budget +€20-40k | aviation-regulatory-counsel + Firmamento DG | M+8 | 🟡 in progress (PARZIALE registrato; permessi ENAC locali in fase di engagement) | Gate G2 + Field trial M+8-M+9 |
| C5 (DEL-PFTE-12 WBS 3-4 non dimensionato in 11 mesi) | Chiarimento Cap. 8 + DEL-PFTE-12: WBS 3 per 6A, WBS 2 per 6B; Computo Metrico solo ground segment Pentema | financial-cfo-analyst + Cost Estimator esterno | M+4-M+9 | ⏳ open (Cost Estimator esterno da ingaggiare) | Gate G2 |
| C6 (workshop cooperative ≥ 5 senza budget engagement) | Allocazione €40k in Cap. 8 per workshop engagement + verifica fondi engagement Legacoop/Coopfond | business-model-strategist + snai-funding-territorial-expert | M+3 | ✅ closed (budget allocato; engagement Coopfond fondi separati confermato per bando Cooding) | done |

> **Stato Red Team check Cap. 4 al M+3**: **3 critiche closed (C2, C3, C6)** + **1 in progress (C4 field trial)** + **2 open Gate G2 (C1 budget, C5 WBS Computo Metrico)**. Nessuna critica residual "Red Team theater" (= acknowledged senza action concreta tracciata).

---

## 4.9 Riferimenti

[^1]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Specifico: §4.3 Logical Decomposition; §6.3 Interface Management; §6.2 Requirements Management. Confidence: high (norma metodologica internazionale).

[^2]: D.Lgs. 36/2023 (Codice dei Contratti Pubblici) — art. 41 Progetto di Fattibilità Tecnico-Economica + Allegato I.7 (Contenuti minimi del PFTE). Confidence: high (norma in vigore).

[^3]: Skill `gate-review-checklist` (`/.claude/skills/gate-review-checklist/SKILL.md`) — workflow di gate decisionale Go/Hold/No-Go applicato in §4.1.4.

[^4]: Skill `requirements-traceability-matrix` (`/.claude/skills/requirements-traceability-matrix/SKILL.md`) — traceability StNeed → SyR → SsR → V&V → deliverable applicata in §4.5.2.

[^5]: Skill `epistemic-rigor` (`/.claude/skills/epistemic-rigor/SKILL.md`) — disciplina di falsifiability + triangulation + confidence levels applicata in §4.6.

[^6]: Skill `risk-register-builder` (`/.claude/skills/risk-register-builder/SKILL.md`) — Risk Register dinamico applicato in DEL-PFTE-13.

[^7]: Skill `trade-study-analysis` (`/.claude/skills/trade-study-analysis/SKILL.md`) — DOCFAP italiano + Pugh matrix NASA per DEL-PFTE-03.

[^8]: Reg. UE 2019/947 (Operations UAS). Source: `fonti/CELEX_32019R0947_IT_TXT.md` + Cap. 5.1.2-5.1.5. Confidence: high.

[^9]: ENAC Linee Guida U-Space LG-2023/006. Source: `fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md`. Rilevante per INT-14. Confidence: high.

[^10]: Reg. UE 2016/679 (GDPR) Art. 35. Rilevante per INT-15 + DEL-PFTE-08. Source: testo ufficiale UE + Cap. 5.6. Confidence: high.

[^11]: DTA Puglia — Studio di Fattibilità Aeroporto Grottaglie (fac-simile italiano). Source: `fonti/GROTTAGLIE-studio-fattibilita.md`. Riferimento per struttura PFTE italiano + Computo Metrico Estimativo + Atti di assenso. Confidence: high (template ufficiale italiano).

[^12]: ENAC AAM Business Plan 2021-2030. Source: `fonti/03_AAM-Business-Plan_web-1.md`. Riferimento per business plan deliverable + Wave investimento. Confidence: high.

[^13]: Studio di Fattibilità preliminare in `da revisionare/Studio di Fattibilità e Analisi Comparativa_ Architetture Pseudo-Satellitari Aeree (H.A.L.E.) per lo Sviluppo Territoriale (SNAI) in Regione Liguria.md`, Cap. 4. Riferimento per scope/deliverable/ICD parziale dello Studio in lavorazione. Confidence: medium (documento di lavoro interno, da rivedere).

[^14]: Briefing Progetto Piattaforma Aerea per le Aree Interne (Firmamento). Source: `da revisionare/Briefing_ Progetto Piattaforma Aerea per le Aree Interne.md`. Riferimento per strategia duale 6A/6B + razionale incrementale. Confidence: high (documento ufficiale Firmamento).

[^15]: Conformità AS/EN 9100 + ISO 9001 (sistemi di gestione qualità aerospace). Riferimento per INT-16, INT-17 (vendor SLA quality). Confidence: high.

---

## 4.10 Note di chiusura

Il presente Capitolo 4 stabilisce un **perimetro deliberatamente stretto** per il PFTE HALE/VTOL: 17 deliverable, 20 interfacce ICD preliminari, 6 domini × 5-7 voci in-scope/out-of-scope, 8 criteri di accettazione, mapping verso D.Lgs. 36/2023 art. 41 + Allegato I.7.

La **disciplina di scope** è scelta strategica: meglio chiudere un PFTE coeso al M+11 con 17 deliverable solidi, che tentare 30 deliverable e arrivare a M+13-M+14 con metà di essi incompleti. Il rischio numero uno non è la sottostima delle ambizioni — è lo scope creep che annacqua tutto.

L'**ICD preliminare** a 20 interfacce è il **secondo strato di rigore** del capitolo: identifica le interfacce critiche (fisiche, funzionali, regolatorie, contrattuali, ecosistemiche) con sigla + tipo + standard + owner + status. Le specifiche dettagliate (byte-level format, latency end-to-end, failure mode behavior) sono deferite al Vol. 2 Allegato A.4 e a Fase 1 Design Engineering.

**Prossimi step richiesti** (in ordine di criticità per i gate M+6 e M+10):

1. **Validazione perimetro con stakeholder** — workshop dedicato M+3 con Coopfond + Regione + Legacoop per accettazione formale Tabella §4.2.1.
2. **Pre-engagement vendor critici** — JOUAV / equivalenti VTOL + payload + autopilot, validazione interfacce INT-01, INT-02 entro M+3.
3. **Pre-application ENAC + AGCOM** — lettere PEC M+1-M+2 per INT-13, INT-07 (vedi Cap. 5).
4. **MoU cooperative** — adesione ≥ 8/10 entro M+3 (INT-18 framework).
5. **LoI Regione Liguria** — entro M+9 (INT-19 framework).
6. **ICD Vol. 2 Allegato A.4** — versione preliminary completa entro M+8.
7. **Field trial demo tethered** — fattibilità da valutare M+6-M+8 (Red Team Critica 4); 1 volo VLOS bassa quota M+8-M+9 condizionato a permessi.

**Versionamento Cap. 4**:
- v0.5 (M+3, presente capitolo): scope baseline + ICD preliminary 20 interfacce
- v0.6 (M+6, post-workshop stakeholder + pre-application ENAC/AGCOM): scope refinement + interfacce status update
- v0.8 (M+10, post Trade Study + Workshop ≥ 5): scope finalized + ICD detailed v1.0 in Vol. 2 Allegato A.4
- v1.0 (M+11, baseline finale per gate decisionale): scope frozen per Fase 1 execution

Il capitolo è **chiuso al M+3** con verdetto Red Team **OK con action items** (6 action items aperti, di cui 1 critico — Critica 4 field trial demo).

---

*Fine Capitolo 4 — Perimetro, Scope, Deliverable e Interfacce (ICD preliminare)*
