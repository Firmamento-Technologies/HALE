# Capitolo 3 — Requisiti e Criteri di Successo (baseline)

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 1, Capitolo 3
>
> **Versione:** bozza M+3 (post-Allineamento Strategico Maggio 2026)
> **Metodologia:** NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105), §4.1 Stakeholder Expectations Definition + §4.2 Technical Requirements Definition
> **Conformità:** D.Lgs. 36/2023 art. 41 (Quadro Esigenziale richiamato dal Cap. 1)
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** verifica condotta dall'agente `red-team-skeptic` — vedi §3.11

---

## 3.0 Sintesi del capitolo

Il presente capitolo costituisce la **baseline dei requisiti** dello Studio di Fattibilità, ed è la **colonna portante metodologica** rispetto alla quale tutti i capitoli successivi (Cap. 6 Analisi tecnica, Cap. 7 Mercato, Cap. 8 Finanziario, Cap. 9 Cronoprogramma) devono essere agganciati e tracciati. Senza un set di requisiti solidi, robusti e tracciabili, il documento non supera il rigore di un gate review investment-grade.

La metodologia adottata è il **NASA Systems Engineering Handbook Rev 2** [^1] §4, con le seguenti fasi operative:

1. **Identificazione stakeholder** e raccolta delle aspettative (§4.1.1.2.1-2)
2. **Definizione bisogni, obiettivi, vincoli** (§4.1.1.2.3)
3. **Concept of Operations (ConOps)** preliminare (§4.1.1.2.4)
4. **Trasformazione in System Requirements** misurabili (§4.2)
5. **Costruzione della Requirements Traceability Matrix (RTM)** — `agents/aerospace-systems-engineer.md` + skill `requirements-traceability-matrix`

Output del capitolo:
- **N° 17 Stakeholder Needs (StNeeds)** consolidati, espressi in forma di "vogliamo che..."
- **N° 42 System Requirements (SyR)** misurabili, categorizzati in 7 famiglie, **+ N° 14 Negative Requirements (NegR)** di tipo "shall not" (vincoli di disegno dichiarati come boundary del sistema, cf. §3.5.8)
- **N° ~80 Subsystem Requirements (SsR)** decomposti su 6 sottosistemi (sample rappresentativo nel capitolo, lista completa in Vol. 2 Allegato A.1)
- **RTM v0.5** baseline (cf. §3.8)
- **Criteri Go/No-Go** quantitativi per il gate M+10 (cf. §3.2)
- **34 Assumptions** dichiarate e **18 Open Questions** tracciate per i gate successivi

La presente baseline è **provvisoria al M+3**. Aggiornamenti previsti dopo:
- Pre-application meeting ENAC (M+3-6) per validare SyR di compliance regolatoria
- Workshop cooperative pilota Legacoop (M+3-6) per validare StNeeds di servizio
- Trade study chiave (M+6) per stabilizzare gli SsR architetturali

---

## 3.0bis Boundary conditions del progetto

I requisiti del progetto rispettano le **boundary conditions** dichiarate (vedi Cap. 5.0bis):

- **B1**: Il modello cooperativo Legacoop è scelta strutturale del progetto (no product sale, solo erogazione di servizi a cooperative + PA). I requisiti operativi riflettono questa scelta — non sono validate ipotesi alternative (es. "vendita diretta UAV a clienti privati").
- **B2**: L'obiettivo strategico "EU sovereign stratospheric layer" è posizione di lungo termine. I requisiti del presente Studio coprono i percorsi 6A + 6B preparatori, NON il deployment full-scale che è materia di gate futuri (vedi `riferimenti/visione-10-anni.md`).

---

## 3.1 Razionale e Metodologia

### 3.1.1 Perché un set di requisiti tracciabili

Citando NASA SE Handbook §4.0 [^1]:

> *"Complete and thorough requirements traceability is a critical factor in successful validation of the system. [...] Lack of traceability is a leading cause of cost and schedule overruns in aerospace programs."*

Lo Studio di Fattibilità HALE/VTOL adotta lo standard NASA per i seguenti motivi:

1. **Compliance metodologica** con standard internazionali aerospaziali (NASA SE, INCOSE, ECSS-E-ST-10C)
2. **Audit-readiness** per finanziatori (Coopfond, PNRR, EDF, Horizon Europe richiedono tracciabilità requisiti)
3. **Manageability** del progetto duale (6A + 6B) con interdipendenze complesse
4. **Risk reduction** — ogni requisito tracciato è una via per identificare gap e showstopper prima che diventino crisi

### 3.1.2 Tassonomia dei requisiti

La struttura gerarchica adottata, in linea con NASA SE Handbook §4 [^1] e con la skill `requirements-traceability-matrix`:

```
Stakeholder Needs (StNeed-NNN)
        ↓ derivazione
System Requirements (SyR-NNN)
        ↓ allocazione + decomposizione
Subsystem Requirements (SsR-XXX-NNN)
        ↓ + Interface Requirements (IR-XXX-NNN)
        ↓ verifica
Verification Requirements (VR-NNN)
```

Convenzioni di identificazione:

```
StNeed-NNN           # Stakeholder Need
SyR-NNN              # System Requirement
SsR-XXX-NNN          # Subsystem Requirement (XXX = AERO, PROP, AVI, PAY, GS, COMMS)
IR-XXX-NNN           # Interface Requirement
VR-NNN               # Verification Requirement
```

### 3.1.3 Criteri di buona scrittura (NASA SE Appendix C, regole VAFC)

Ogni requisito del presente Studio è scritto secondo i quattro criteri citati nella skill `requirements-traceability-matrix` (derivati da NASA SE Handbook §4.2 + INCOSE Guide for Writing Requirements):

- **V — Verificabile**: ogni requisito deve dichiarare il metodo di verifica (Inspection, Analysis, Demonstration, Test)
- **A — Atomico**: un requisito = un'affermazione (mai composti con "e/o", "qualora", "in funzione di")
- **F — Feasibile**: dimostrabile entro lo stato dell'arte tecnologico al momento della verifica
- **C — Completo**: privo di ambiguità, autonomo (interpretabile senza altri requisiti)

**Esempio di requisito non conforme:**

> "Il sistema deve essere affidabile e operare in condizioni avverse."

**Esempio di requisito conforme:**

> "Il sistema [Percorso 6A VTOL] deve garantire un MTBF ≥ 200 h di operazione nominale in condizioni ambientali tipiche di area appenninica ligure (T -10°C/+30°C, umidità ≤90%, vento ≤17 m/s, pioggia ≤10 mm/24h), verificato per Analysis e Test in fase di pilota."

### 3.1.4 Disciplina epistemica

In coerenza con la skill `epistemic-rigor`, ogni requisito è annotato con:

- **Source provenance**: stakeholder origine + workshop/meeting + data
- **Confidence level**: high (validato da fonte autoritativa) / medium (in negoziazione) / low (preliminare)
- **Falsifying observation**: cosa renderebbe falso il requisito o ne dimostrerebbe l'infeasibility
- **Verification status**: Open / Planned / In progress / Verified / Failed / Waived
- **Trade Study link**: se il requisito deriva da una scelta di trade study, riferimento al TS-ID
- **Risk link**: se il requisito ha impatto su un rischio, riferimento al RSK-ID

---

## 3.2 Criteri di Successo del Gate M+10 (Go/No-Go Baseline)

Lo Studio di Fattibilità si conclude al gate **M+10/M+11** con verdetto per ciascuno dei due percorsi. I criteri di successo del Gate, formalizzati ai sensi della skill `gate-review-checklist`, sono:

### 3.2.1 Criteri tecnici

| Criterio | Soglia per GO 6A | Soglia per GO 6B condizionato |
|---|---|---|
| Concept architettura definita | ✓ (Cap. 6.1) | ✓ (Cap. 6.1) |
| Performance preliminare verificata | Autonomia ≥ 4h, payload ≥ 4 kg, copertura ≥ 30 km @ Pentema | Energy balance dicembre 21 a 44°N con margine ≥ 30% |
| FMECA + FTA preliminari completi | ✓ Vol. 2 Allegato A.2 | ✓ Vol. 2 Allegato A.2 |
| Risk Register top-10 con mitigation | ✓ nessun rischio rosso senza piano | ✓ showstopper RSK-TEC-001/002 con piano R&D |
| TRL minimo subsistemi | ≥ 8 (commerciali) | ≥ 4 (subsystem critici) |

### 3.2.2 Criteri regolatori (cf. Cap. 5)

| Criterio | Soglia per GO 6A | Soglia per GO 6B condizionato |
|---|---|---|
| Pre-application meeting ENAC | ✓ entro M+9 | ✓ in dialogo informale |
| Stima SAIL preliminare | ≤ III | n/a (Certified path) |
| Engagement EASA su HAPS framework | n/a | ✓ richiesta RMT formalizzata |

### 3.2.3 Criteri economico-finanziari (cf. Cap. 8)

| Criterio | Soglia per GO 6A | Soglia per GO 6B condizionato |
|---|---|---|
| Quadro Economico art. 41 redatto | ✓ | ✓ (preliminare) |
| Piano finanziario NPV/IRR/payback | NPV > 0 con WACC 12%, payback < 6 anni | n/a (R&D phase, no revenue) |
| Funding plan committed | ≥ 60% Y1-Y2 con commitment formali (LoI Regione + Coopfond) | ≥ 40% Phase B con plan multi-source (PNRR + Horizon + EDF + equity) |

### 3.2.4 Criteri business (cf. Cap. 7)

| Criterio | Soglia per GO 6A | Soglia per GO 6B condizionato |
|---|---|---|
| BMC + VPC redatti | ✓ Cap. 7 | ✓ Cap. 7 |
| Anchor customer identificato | Regione Liguria con LoI | n/a |
| MVP definito | ✓ Cap. 7.8 | n/a |
| Pricing model validato | ✓ con almeno 1 cliente | n/a |

### 3.2.5 Criteri operativi/territoriali (cf. Cap. 1-2)

| Criterio | Soglia per GO 6A | Soglia per GO 6B condizionato |
|---|---|---|
| Comune Torriglia disponibilità | ✓ delibera o LoI | n/a |
| Cooperative pilota engagement | ≥ 8 su 10 cooperative aderenti | n/a |
| Comunità Pentema accettabilità sociale | ✓ workshop pubblico + DPIA pubblica | n/a |

> **Falsifying observation Gate M+10**: se al gate M+10/M+11 ≥ 30% dei criteri sopra non è soddisfatto, il verdetto è **HOLD** (non No-Go), con re-review M+13-15. Il No-Go è riservato a showstopper insuperabili (ad es. ENAC esplicitamente nega path SAIL per Pentema, Regione Liguria si tira indietro, fonti di finanziamento completamente azzerate).

---

## 3.3 Stakeholder Map e Stakeholder Needs (StNeeds)

### 3.3.1 Mappa stakeholder consolidata

I principali stakeholder del progetto sono (vedi Cap. 2 per dettaglio governance):

| ID | Stakeholder | Categoria | Ruolo |
|---|---|---|---|
| S-01 | Firmamento Technologies | Proponente | Soggetto attuatore, capofila tecnico |
| S-02 | Fabrica (cooperativa capofila Legacoop) | Cliente/Co-progettista | Aggregatore cooperative pilota |
| S-03 | Rete 10 cooperative Legacoop | Cliente/Utente-pilota | Beneficiari servizi DaaS/IaaS |
| S-04 | Regione Liguria | Istituzionale / Anchor customer | Sponsor istituzionale, cliente pilota |
| S-05 | Comune di Torriglia (Pentema) | Istituzionale locale | Sede pilota, autorizzazioni locali |
| S-06 | Protezione Civile Liguria + ARPA Liguria | Istituzionale operativo | Cliente pilota PRIMARIO per missioni di emergenza |
| S-07 | Comunità Pentema | Cittadini | Accettabilità sociale, diritti privacy |
| S-08 | ENAC | Autorità regolatoria nazionale | Autorizzazione operativa SORA, certificazione |
| S-09 | EASA | Autorità regolatoria europea | Framework + Special Condition HAPS |
| S-10 | AGCOM | Autorità regolatoria nazionale | Spettro radio, licensing |
| S-11 | Garante Privacy | Autorità regolatoria nazionale | Tutela dati personali |
| S-12 | ENAV / D-Flight | Operatore traffico aereo | Integrazione U-Space |
| S-13 | MIMIT (Direzione Aerospazio + Comunicazioni) | Istituzionale nazionale | Strategia, PNRF, finanziamenti PNRR |
| S-14 | MIT (Trasporti) | Istituzionale nazionale | Vigilanza ENAC |
| S-15 | ACN — Agenzia Cybersicurezza Nazionale | Istituzionale | NIS2 compliance |
| S-16 | Coopfond + Fondazione PICO ETS | Finanziatore | Bando Cooding Prototypes + Cooding Invest |
| S-17 | Commissione UE (DG CNECT, DEFIS, MOVE) | Istituzionale UE | Programmi EDF, Horizon, IRIS² |
| S-18 | ASI — Agenzia Spaziale Italiana | Istituzionale | Coordinamento spazio + EO |
| S-19 | CIRA — Centro Italiano Ricerche Aerospaziali | Partner R&D potenziale | Phase B HALE consortium |
| S-20 | POLITO — DIMEAS | Partner accademico potenziale | HELIPLAT lineage, R&D HALE |
| S-21 | DTA Puglia + GATB Grottaglie | Partner test bed | BVLOS test bed Percorso 6A |
| S-22 | TIM, Vodafone, Iliad, WindTre, Open Fiber | Potenziali partner/competitor | NTN backhaul futuro |
| S-23 | Leonardo + Telespazio + TAS | Incumbent aerospace IT | Consorzio sovrano EU futuro / acquisition risk |
| S-24 | Vigili del Fuoco, Carabinieri Forestali | Cliente operativo | Antincendio, monitoraggio territoriale |
| S-25 | ASL3 Genovese | Cliente operativo | Telemedicina rurale Aree Interne |
| S-26 | Ente Parco Antola, Ente Parco Aveto | Cliente operativo | Vigilanza ambientale |

### 3.3.2 Stakeholder Needs (StNeeds) consolidati

Di seguito gli **StNeeds principali** raccolti tramite (i) analisi del Briefing e dello Studio di Fattibilità preliminare in `da revisionare/`, (ii) lettura della documentazione SNAI (PSNAI 2025 + dossier Liguria), (iii) workshop preliminare con la rete cooperative (M+0-3, in corso). Sono i requisiti di alto livello degli stakeholder, in forma di "vogliamo che il sistema..."

I 17 StNeeds elencati sotto sono il **set minimo baseline**. La lista completa (estesa post-workshop Cooperative M+3 e post pre-application meeting ENAC M+6) sarà in Vol. 2 Allegato A.1.

#### Categoria A — Servizi a Protezione Civile e PA

> **StNeed-001 — Monitoraggio frane**
> Stakeholder: S-04 (Regione Liguria), S-06 (PC + ARPA Liguria)
> Need: "Vogliamo ricevere mappe ad alta risoluzione (≤0.5 m GSD) dei versanti a rischio nei comuni delle aree SNAI Liguria, con frequenza settimanale durante la stagione piovosa e mensile altrimenti, per supportare la prevenzione del rischio idrogeologico."
> Source: PSNAI 2025 + DGR Regione Liguria. Confidence: **medium** (da formalizzare con LoI Regione Liguria, DR-001 audit-rigore-epistemico.md).

> **StNeed-002 — Antincendio boschivo**
> Stakeholder: S-06 (PC), S-24 (VVF + Carabinieri Forestali), S-26 (Ente Parco)
> Need: "Vogliamo ricevere alert hotspot termico (≥40°C) entro 5 minuti dall'evento durante la stagione antincendio (giugno-settembre), con localizzazione GPS e thumbnail visuale."
> Source: protocollo PC Liguria + Carabinieri Forestali. Confidence: **medium**.

> **StNeed-003 — Connettività di emergenza**
> Stakeholder: S-06 (PC), S-05 (Comune Torriglia), S-07 (Comunità Pentema)
> Need: "Vogliamo ricevere connettività mobile/dati di backup nell'area di Pentema in caso di interruzione delle reti terrestri (alluvioni, neve, blackout), con disponibilità ≥99% durante eventi di crisi."
> Source: workshop PC Liguria. Confidence: **medium**.

> **StNeed-004 — Supporto alla ricerca persone disperse**
> Stakeholder: S-06 (PC), S-24 (CC Forestali)
> Need: "Vogliamo supportare le squadre di ricerca persone disperse in aree montane Liguri con osservazione aerea persistente e payload termico durante operazioni di ricerca."
> Source: protocollo SAR esistente PC/CC. Confidence: medium.

#### Categoria B — Servizi alle Cooperative Legacoop

> **StNeed-005 — Mappatura territoriale per cooperative**
> Stakeholder: S-02 (Fabrica), S-03 (10 cooperative)
> Need: "Vogliamo mappe topografiche aggiornate annualmente del territorio operativo delle cooperative (servizi forestali, agroforestali, manutenzione del verde) con accuratezza posizionale ≤ 2 m."
> Source: workshop cooperative pilota M+0-3 (in corso). Confidence: **low-medium**.

> **StNeed-006 — Monitoraggio agricolo di precisione**
> Stakeholder: cooperative agricole nella rete S-03
> Need: "Vogliamo mappe multispettrali (NDVI, NDRE) dei nostri fondi agricoli con frequenza quindicinale in stagione vegetativa, per supportare la fertirrigazione e il rilevamento di patogeni."
> Source: workshop cooperative agricole. Confidence: **low**.

> **StNeed-007 — Connettività digitale per zone non servite**
> Stakeholder: S-03 (cooperative), S-07 (comunità rurali)
> Need: "Vogliamo accesso a connettività dati > 10 Mbps in aree senza copertura terrestre adeguata, per servizi essenziali (e-banking, telemedicina, formazione online)."
> Source: dossier SNAI Liguria + indagine 2026. Confidence: **medium**.

#### Categoria C — Sostenibilità e accettabilità sociale

> **StNeed-008 — Privacy della comunità**
> Stakeholder: S-07 (comunità Pentema), S-11 (Garante)
> Need: "Vogliamo che le missioni di osservazione aerea non producano sorveglianza personale, non identifichino volti o targhe nelle immagini archiviate, e siano oggetto di comunicazione trasparente alla popolazione."
> Source: principi GDPR + best practice Garante. Confidence: **high** (vincolo regolatorio).

> **StNeed-009 — Minimo impatto ambientale**
> Stakeholder: S-04 (Regione), S-26 (Enti Parco), S-07 (comunità)
> Need: "Vogliamo che il sistema usi propulsione elettrica/solare, materiali a basso impatto ambientale e generi rumore < 65 dB(A) al ground sotto rotta tipica."
> Source: Reg. UE 2019/945 + ISO 14001 + DGR Liguria sostenibilità. Confidence: high.

#### Categoria D — Affidabilità e disponibilità operativa

> **StNeed-010 — Disponibilità operativa**
> Stakeholder: S-01 (Firmamento), S-04 (Regione), S-06 (PC)
> Need: "Vogliamo che il sistema sia disponibile per missioni programmate ≥80% dei giorni dell'anno e per missioni di emergenza con tempo di reazione ≤4h, anno solare."
> Source: SLA tipici PC e servizi essenziali. Confidence: medium.

> **StNeed-011 — Sicurezza operativa BVLOS**
> Stakeholder: S-08 (ENAC), S-12 (ENAV), S-04 (Regione)
> Need: "Vogliamo che il sistema mantenga safe behaviour in caso di lost link, perdita avionica primaria, o degrado payload, senza mai causare incidenti su persone non coinvolte."
> Source: Reg. UE 2019/947 + ENAC Reg. APR Ed.3 + SORA OSO. Confidence: high.

#### Categoria E — Conformità regolatoria

> **StNeed-012 — Conformità EASA UAS Specific**
> Stakeholder: S-08 (ENAC), S-09 (EASA)
> Need: "Vogliamo operare in piena conformità al Reg. UE 2019/947, classe Specific, con SORA application approvata e Operations Manual completo."
> Source: Reg. UE 2019/947 + EASA AMC/GM Amendment 3 (sett 2025). Confidence: high.

> **StNeed-013 — Conformità spettro radio**
> Stakeholder: S-10 (AGCOM), S-13 (MIMIT)
> Need: "Vogliamo che tutti i link radio (C2, payload) operino in bande regolarmente licenziate dall'AGCOM, con coordinamento ITU se rilevante."
> Source: D.Lgs. 259/2003 + Cap. 5.5. Confidence: high.

> **StNeed-014 — Conformità privacy e protezione dati**
> Stakeholder: S-11 (Garante), S-07 (comunità)
> Need: "Vogliamo trattare i dati personali generati dal sistema in piena conformità al GDPR + Codice Privacy, con DPIA documentata per i casi d'uso ad alto rischio."
> Source: Reg. UE 2016/679 + D.Lgs. 196/2003 novellato. Confidence: high.

#### Categoria F — Modello di business e sostenibilità economica

> **StNeed-015 — Modello service-based**
> Stakeholder: S-01 (Firmamento), S-16 (Coopfond)
> Need: "Vogliamo erogare servizi (DaaS, IaaS, canone) anziché vendere asset, in linea con la boundary condition B1 del progetto."
> Source: visione strategica progetto (cf. `riferimenti/visione-10-anni.md`). Confidence: **boundary condition** (non soggetta a falsificazione epistemica).

> **StNeed-016 — Sostenibilità finanziaria del pilota Y1**
> Stakeholder: S-16 (Coopfond), S-04 (Regione)
> Need: "Vogliamo che il Percorso 6A generi revenue ricorrenti ≥ €200k Y1 da contratti PA + cooperative, dimostrando willingness-to-pay e replicabilità."
> Source: requisito Bando Cooding + sostenibilità progetto. Confidence: medium.

#### Categoria G — Visione strategica di lungo termine

> **StNeed-017 — Coerenza con visione 10 anni**
> Stakeholder: S-01 (Firmamento), S-23 (potenziali partner Leonardo/TAS)
> Need: "Vogliamo che le scelte tecnologiche del Percorso 6A producano asset riusabili per il Percorso 6B (ground segment, data governance, brand) e che il Percorso 6B preservi traiettoria verso il consorzio EU stratosferico (boundary condition B2)."
> Source: visione strategica progetto. Confidence: **boundary condition**.

---

## 3.4 Concept of Operations (ConOps) — Preliminare

In coerenza con NASA SE Handbook §4.1.1.2.4 [^1], il **ConOps** descrive *come* il sistema verrà operato per soddisfare gli StNeeds. Riportato qui in forma sintetica (versione completa: Cap. 4 Perimetro e Vol. 2 Allegato A.4 ICD).

### 3.4.1 ConOps Percorso 6A — Pilota Pentema Y1

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Use case primari Percorso 6A:                                            │
│  • UC-001 Monitoraggio frane (BVLOS, settimanale stagione piovosa)       │
│  • UC-002 Antincendio boschivo (BVLOS, on-demand stagione estiva)        │
│  • UC-003 Connettività emergenza (LTE tattico, on-demand)               │
│  • UC-004 Mappatura cooperative (VLOS/EVLOS, trimestrale)                │
└─────────────────────────────────────────────────────────────────────────┘

Piattaforma: VTOL ibrido commerciale TRL 8-9 (JOUAV CW-30E baseline)
Base operativa: Pentema (Torriglia, GE), 1100-1300 m s.l.m.
Pilot remoto: 1 PIC (Pilot in Command) + 1 observer (training in corso)
Ground Station: 1 fissa Pentema + 1 mobile (veicolo cooperativa)
Payload: EO RGB + IR termico (mappa termica antincendio) + telecom backup

Profilo missione tipico (monitoraggio frane):
  T+0   Briefing meteo + ConOps + NOTAM
  T+15  Decollo VTOL
  T+18  Climb a 500 m AGL, transizione a cruise
  T+25  Inizio sorvolo aree target a 200-500 m AGL
  T+1h  Trasmissione real-time imagery a GS
  T+5h  Return-to-base e atterraggio VTOL
  T+5.5h Download dati + processamento + delivery PA <24h
```

### 3.4.2 ConOps Percorso 6B — HALE R&D Phase B Y3-Y5

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Use case primari Percorso 6B (post-pilota subscale):                     │
│  • UC-005 EO persistente su area Liguria (>72h continuativi)             │
│  • UC-006 NTN gNB regenerative HAPS (banda S o 700 MHz, ≥10 km cella)    │
│  • UC-007 Dual-use civile-difesa (ISR, NATO DIANA, conditional)          │
└─────────────────────────────────────────────────────────────────────────┘

Piattaforma: HALE solare custom Firmamento, b ≈ 25-30 m, MTOW ≈ 80-150 kg
Base operativa: TBD (GATB Grottaglie test bed + base operativa Liguria)
Quota operativa: 18-21 km (FL590-690)
Endurance target: > 30 giorni perennial in stagione estiva (Y3); 12 mesi target Y5
Payload: EO multispettrale + IR + NTN gNodeB Rel-17/18

Profilo missione tipico (persistent EO Liguria):
  D-7   Mission planning + meteo + NOTAM + Airspace Coordination ENAV
  D-1   Sortie da GATB con ascesa nominale 3-6h
  D+0   Stabilizzazione FL650 + handover to mission control Liguria
  D+0   to D+30  Persistent observation con tasking dinamico da GS
  D+30  Discesa programmata o emergency return-to-base
```

---

## 3.5 System Requirements (SyR)

I System Requirements traducono gli StNeeds in specifiche **misurabili, verificabili, allocabili** a sottosistemi. Sono il livello dove avvengono le scelte di trade study (Cap. 6.3) e dove emergono i vincoli del progetto.

I 42 SyR baseline sono categorizzati in **7 famiglie**. Riportiamo nel capitolo i SyR principali; la lista completa è in Vol. 2 Allegato A.1.

### 3.5.1 Famiglia F — Functional Requirements

> **SyR-F-001** — Il sistema [Percorso 6A] deve eseguire missioni di osservazione aerea con payload EO + termico in area appenninica ligure entro un raggio di 30 km dalla GS, con GSD ≤ 0.5 m a 500 m AGL.
> **Parent:** StNeed-001, StNeed-002 | **Allocation:** PAY (Payload), AVI (Avionics), GS (Ground Station)
> **Verification:** A (Analysis) + T (Test in volo) | **Confidence: high** | **Status: Open**

> **SyR-F-002** — Il sistema [Percorso 6A] deve eseguire missioni BVLOS con autorizzazione SORA SAIL ≤ III secondo Reg. UE 2019/947 art. 11 + AMC/GM Amendment 3.
> **Parent:** StNeed-011, StNeed-012 | **Allocation:** sistema completo | **Verification:** I (compliance documentale ENAC) | **Confidence: medium** | **Status: Open** | **Risk:** RSK-REG-002 | **Falsifying observation:** ENAC pre-application nega SAIL II-III → re-design ConOps

> **SyR-F-003** — Il sistema [Percorso 6A] deve rilevare hotspot termici ≥ 40°C in area boschiva e inviare alert + thumbnail a Ground Station entro 5 minuti dall'evento.
> **Parent:** StNeed-002 | **Allocation:** PAY (IR), AVI (on-board processing), COMMS (downlink) | **Verification:** D (Demonstration in test scenario) + T | **Confidence: medium** | **Status: Open**

> **SyR-F-004** — Il sistema [Percorso 6A] deve fornire connettività LTE locale (banda non commerciale o licenziata temporaneamente) in raggio ≥ 5 km dal velivolo durante operazioni di emergenza.
> **Parent:** StNeed-003 | **Allocation:** PAY (LTE eNodeB) | **Verification:** T | **Confidence: low** | **Status: Open** | **Risk:** RSK-REG-005 (AGCOM licensing)

> **SyR-F-005** — Il sistema [Percorso 6B] deve eseguire missioni HAPS persistenti con quota nominale 18-21 km e endurance ≥ 30 giorni continuativi in stagione estiva (Y3 target).
> **Parent:** StNeed-017, visione strategica | **Allocation:** PROP (Propulsion), AERO (Aerodynamics), AVI | **Verification:** A + T (subscale) | **Confidence: low** | **Status: Open** | **Risk:** RSK-TEC-001 (energy balance inverno)

### 3.5.2 Famiglia P — Performance Requirements

> **SyR-P-001** — [Percorso 6A] Autonomia operativa: il sistema deve fornire ≥ 4h di volo operativo in condizioni nominali (T -5°C/+25°C, vento ≤10 m/s) con payload pieno.
> **Parent:** StNeed-001, StNeed-002, StNeed-010 | **Verification:** T | **Confidence: medium** | **Status: Open**

> **SyR-P-002** — [Percorso 6A] Velocità di crociera: ≥ 100 km/h ground speed in still air.
> **Parent:** ConOps efficienza operativa | **Verification:** T | **Confidence: medium**

> **SyR-P-003** — [Percorso 6A] Payload max: ≥ 4 kg utili (esclusi batterie/struttura aggiuntiva).
> **Parent:** StNeed-001, -002, -003 (multi-sensor mission) | **Verification:** I + T | **Confidence: high**

> **SyR-P-004** — [Percorso 6B] L/D crociera @ 20 km: ≥ 25.
> **Parent:** SyR-F-005 (energy balance) | **Verification:** A (XFLR5 + CFD) + T (wind tunnel) | **Confidence: medium**

> **SyR-P-005** — [Percorso 6B] Energy balance perennial estate (giugno-agosto, 44°N): margine ≥ 50%.
> **Parent:** SyR-F-005 | **Verification:** A | **Confidence: medium-low** | **Risk:** RSK-TEC-001

> **SyR-P-006** — [Percorso 6B] Energy balance perennial worst-case (solstizio inverno 21/12, 44°N): margine ≥ 30%, o seasonal-only operation marzo-ottobre.
> **Parent:** SyR-F-005 | **Verification:** A | **Confidence: low** | **Risk:** RSK-TEC-001 🔴 (showstopper) | **Falsifying observation:** energy balance simulation con tech 2026 mostra margine < 0% al 21/12 → seasonal fallback obbligatorio

### 3.5.3 Famiglia O — Operational Requirements

> **SyR-O-001** — Disponibilità operativa: il sistema [Percorso 6A] deve essere disponibile ≥ 80% dei giorni dell'anno per missioni programmate, ≥ 99% per missioni di emergenza chiamate con preavviso ≥ 4h.
> **Parent:** StNeed-010 | **Verification:** D (uptime monitoring) | **Confidence: medium**

> **SyR-O-002** — [Percorso 6A] Tempo di reazione emergenza: il sistema deve essere pronto al decollo in ≤ 60 minuti dalla chiamata di emergenza.
> **Parent:** StNeed-002, -003, -004 | **Verification:** D | **Confidence: medium**

> **SyR-O-003** — Il sistema deve operare nelle condizioni ambientali tipiche di Pentema: T -10°C/+30°C, umidità 40-90%, vento ≤17 m/s sostenuto, pioggia ≤10 mm/24h.
> **Parent:** StNeed-010 + caratteristiche territoriali | **Verification:** I (compliance datasheet) + T (operations log) | **Confidence: high**

### 3.5.4 Famiglia S — Safety Requirements

> **SyR-S-001** — Lost-Link behaviour: in caso di perdita totale del C2 link per > 60 s, il sistema deve eseguire un Return-to-Base autonomo verso la GS principale o, se non raggiungibile, un atterraggio sicuro in area pre-designata.
> **Parent:** StNeed-011 + Reg. UE 2019/947 OSO #9 | **Verification:** D + T | **Confidence: high**

> **SyR-S-002** — Il sistema deve includere parachute recovery o equivalente per impact velocity ≤ 7 m/s in caso di perdita di propulsione.
> **Parent:** StNeed-011 + SORA M2 mitigation | **Verification:** T | **Confidence: high**

> **SyR-S-003** — Il sistema deve avere ridondanza N+1 sui sensori IMU primari e GNSS.
> **Parent:** SyR-F-002 (SAIL III) + Reg. ENAC Art. 26 BVLOS | **Verification:** I | **Confidence: high**

> **SyR-S-004** — [Percorso 6B HALE] Il sistema deve avere Detect-And-Avoid (DAA) cooperativo (ADS-B IN) durante climb/descent attraverso spazio aereo controllato.
> **Parent:** SyR-F-005 + ENAV coordination | **Verification:** I + D | **Confidence: medium**

### 3.5.5 Famiglia E — Environmental & Sustainability

> **SyR-E-001** — Propulsione del sistema: 100% elettrica per il Percorso 6A; 100% solare/batterie per il Percorso 6B.
> **Parent:** StNeed-009 | **Verification:** I | **Confidence: high**

> **SyR-E-002** — Rumore al ground sotto rotta tipica (200 m AGL, cruise): ≤ 65 dB(A) misurato a 100 m laterali.
> **Parent:** StNeed-009 + Reg. UE 2019/945 acoustic + ISO 3744 | **Verification:** T | **Confidence: medium**

> **SyR-E-003** — Materiali strutturali: ≥ 20% in massa con materiali a basso impatto ambientale (compositi a fibre naturali, riciclati), in coerenza con narrativa ESG progetto.
> **Parent:** StNeed-009 | **Verification:** I (BoM analysis) | **Confidence: medium** | **Trade Study link:** TS-MATERIAL (Cap. 6.3.3)

### 3.5.6 Famiglia C — Compliance & Regulatory

> **SyR-C-001** — Conformità Reg. UE 2019/947 + 2019/945 + ENAC Reg. APR Ed.3 + Emend. 1.
> **Parent:** StNeed-012 + Cap. 5 | **Verification:** I (compliance audit) | **Confidence: high**

> **SyR-C-002** — Conformità EASA AMC/GM Issue 1 Amendment 3 (SORA 2.5 europea, settembre 2025).
> **Parent:** StNeed-012 + Cap. 5.1.4 | **Verification:** I | **Confidence: high**

> **SyR-C-003** — Conformità GDPR + D.Lgs. 196/2003 novellato per i dati personali eventualmente trattati.
> **Parent:** StNeed-014 + Cap. 5.6 | **Verification:** I (DPIA documentata) | **Confidence: high**

> **SyR-C-004** — Conformità NIS2 + D.Lgs. 138/2024 per gli aspetti di cybersecurity.
> **Parent:** StNeed-014 (estesa) + Cap. 5.7 | **Verification:** I + A | **Confidence: high**

> **SyR-C-005** — Conformità AS/EN 9100 per i processi di progettazione e produzione aerospaziale + ISO 9001 per la gestione qualità.
> **Parent:** dichiarazioni di conformità per bandi pubblici | **Verification:** I (certificazione) | **Confidence: medium** | **Status:** in corso (Y1-Y2)

> **SyR-C-006** — Conformità D.Lgs. 36/2023 art. 41 + Allegato I.7 per la documentazione PFTE.
> **Parent:** requisito Bando Cooding | **Verification:** I | **Confidence: high**

### 3.5.7 Famiglia Cost — Cost & Business Model

> **SyR-Cost-001** — CapEx Percorso 6A Y1 ≤ €1.2M (con riserva contingency 30%), in linea con range Briefing €600-900k baseline + buffer realistico aerospace.
> **Parent:** StNeed-015, -016 + Cap. 8 | **Verification:** A (Quadro Economico) | **Confidence: medium**

> **SyR-Cost-002** — OpEx run-rate Y2 (post-MVP) ≤ €450k/anno per le operazioni 6A.
> **Parent:** sostenibilità modello service-only | **Verification:** A | **Confidence: medium**

> **SyR-Cost-003** — Revenue 6A Y1 ≥ €200k da contratti pluriennali PA + cooperative.
> **Parent:** StNeed-016 + Cap. 7 | **Verification:** D (contratti firmati) | **Confidence: medium** | **Falsifying observation:** revenue Y1 < €100k → revisione drastica MVP scope

> **SyR-Cost-004** — Modello di servizio: il sistema deve essere erogato come servizio ricorrente (DaaS, IaaS, canone), no vendita asset agli utenti pilota.
> **Parent:** StNeed-015 + boundary condition B1 | **Verification:** I (contratti) | **Confidence: boundary**

---

### 3.5.8 Negative Requirements (NegR) — vincoli di disegno "shall not"

#### Introduzione

I **Negative Requirements** (NegR) sono requisiti espressi in forma negativa — "il sistema **NON** deve fare X" — e dichiarano vincoli di disegno che restringono lo spazio delle soluzioni ammissibili. Sono **complementari** ai SyR positivi delle famiglie F/P/O/S/E/C/Cost (§3.5.1-3.5.7), che invece descrivono **cosa il sistema deve fare**. La letteratura sistemistica (NASA SE Handbook §4.2.2 + INCOSE GtWR Rule R47 "Avoid Negative Requirements") raccomanda di limitare il numero dei NegR e di esplicitarne la verifica, perché un requisito formulato in negativo è intrinsecamente più difficile da testare di un requisito positivo: si verifica per **assenza** del comportamento proibito, tipicamente tramite **Inspection** (process audit, contract review, BoM check) anziché Test.

L'introduzione di una sezione NegR nel PFTE risponde alla critica del Red Team (vedi §3.11, Critica 5: "i 17 StNeeds non includono need negativi") e ha tre funzioni nello Studio di Fattibilità HALE/VTOL: (i) rendere **espliciti** vincoli che altrimenti rimarrebbero impliciti nelle boundary conditions (B1 service-only + B2 EU sovereign stratospheric layer), creando agganci tracciabili nella RTM; (ii) ridurre il **rischio reputazionale e regolatorio** dichiarando *a priori* ciò che il sistema **non** farà (es. niente dual-use offensivo, niente cloud US default, niente linguaggio "alternativa Starlink"); (iii) fornire **falsifying observations** chiare — un NegR è violato se si osserva il comportamento proibito, e tale osservazione costituisce evento di re-baseline. Lo status di ciascun NegR nella RTM è uno dei tre seguenti: **Active** (vincolo vivo e monitorato), **Waived** (vincolo sospeso con razionale documentato e approvazione gate), **Reviewed** (vincolo confermato all'ultimo audit semestrale).

#### Tassonomia in 5 famiglie

I 14 NegR baseline sono organizzati in 5 famiglie, ciascuna con prefisso identificativo univoco:

- **NegR-B** — Business / Modello (vincoli derivanti da boundary B1 service-only + cooperative Legacoop)
- **NegR-Geo** — Sovranità / Geopolitica (vincoli derivanti da `RESERVED-rischi-geopolitici.md` e da boundary B2)
- **NegR-Reg** — Compliance regolatoria (vincoli derivanti da GDPR, NIS2, AI Act, ENAC/EASA, ITU/AGCOM)
- **NegR-Tech** — Architettura tecnica (vincoli su componentistica, fornitori, supply chain)
- **NegR-Mkt** — Comunicazione / Posizionamento pubblico (vincoli su messaging, claim pubblici)

#### Lista completa dei 14 Negative Requirements

##### Famiglia NegR-B — Business / Modello

> **NegR-B-001** — Il sistema **NON** deve essere venduto come prodotto/asset agli utenti pilota o a terzi: la piattaforma HALE/VTOL è erogata esclusivamente come **servizio ricorrente** (DaaS, IaaS, canone, capacity wholesale).
> **Rationale:** boundary condition B1 (service-only + cooperative Legacoop). La vendita di velivoli trasformerebbe Firmamento in OEM aeronautico, richiedendo Type Certificate proprio (EASA Part 21J/G), capitale OEM-grade (>€50M), e snaturando il modello equivalente Starlink/operatore.
> **Parent:** Boundary B1 (CLAUDE.md) + StNeed-015 + SyR-Cost-004 | **Verification:** Contract clause review (audit semestrale dei contratti con cooperative + PA) | **Status:** Active | **Confidence:** boundary | **Falsifying observation:** firma di un contratto di vendita asset (anche prototipale, anche a 1 cliente) → re-baseline immediato del business model + revisione boundary conditions in Cap. 1.

> **NegR-B-002** — Il sistema **NON** deve essere offerto come servizio retail B2C (vendita diretta a consumatori finali individuali, abbonamenti residenziali, app store).
> **Rationale:** boundary B1 + scelta strategica di servizio wholesale (B2B/B2G) verso cooperative aggregatrici + PA. Modello retail richiederebbe customer care 24/7, billing residenziale, marketing mass-market, fuori scope e fuori capability di Firmamento.
> **Parent:** Boundary B1 + visione 10 anni (`riferimenti/visione-10-anni.md`) | **Verification:** Inspection del listino + audit dei canali commerciali | **Status:** Active | **Confidence:** high | **Falsifying observation:** apertura di un canale e-commerce o app store con abbonamenti individuali → violazione modello.

> **NegR-B-003** — Il sistema **NON** deve concorrere direttamente in scala assoluta con i Tier 1 HAPS internazionali (Airbus Zephyr, AALTO HAPS Sunglider, Aerovironment Sceye) nel medesimo segmento e mercato.
> **Rationale:** asimmetria di capitale e maturità tecnologica. La strategia è di **occupare nicchie regolatorie italiane** (cooperative Legacoop, SNAI, anchor PA Liguria) e contribuire come **nodo italiano** a un futuro consorzio EU, non confrontarsi head-to-head su scala globale.
> **Parent:** Cap. 7 §7.4 (competitor analysis) + Boundary B2 | **Verification:** Process audit annuale del positioning competitivo | **Status:** Active | **Confidence:** high | **Falsifying observation:** lancio di bid su tender internazionale in head-to-head con Zephyr/Sunglider (es. NATO ISR contract) senza partner Tier 1 di copertura.

##### Famiglia NegR-Geo — Sovranità / Geopolitica

> **NegR-Geo-001** — Il sistema **NON** deve utilizzare cloud statunitense (AWS, Azure, GCP, Oracle US regions) come **default** per lo stoccaggio e processamento di imagery EO, dati C2, telemetria operativa, dati personali UE.
> **Rationale:** sovranità dati UE (GDPR Art. 44-50 trasferimenti extra-UE + Schrems II + Data Act 2024). Cloud hosting di default deve essere Italia/EU sovrano (Aruba, OVH, IONOS, GAIA-X compliant). Eccezione ammessa solo con: (i) accordo specifico documentato, (ii) DPIA approvata, (iii) DR esplicito nel risk register.
> **Parent:** StNeed-014 + SyR-C-003 + SsR-GS-002 + `RESERVED-rischi-geopolitici.md` | **Verification:** Inspection del provider cloud (contratti SaaS/IaaS + datasheet datacenter location) — audit semestrale | **Status:** Active | **Confidence:** high | **Falsifying observation:** imagery EO o dati personali UE stoccati in datacenter US senza accordo specifico documentato e DPIA approvata → violazione GDPR + NIS2 + boundary sovranità.

> **NegR-Geo-002** — Il sistema **NON** deve sviluppare *capability dual-use militare offensiva* (armamento, weapon-mount integration, payload kinetic, mission planning per targeting militare letale).
> **Rationale:** scope dichiarato in Cap. 5 §5.7.2 (operatore civile di servizi essenziali, ISR difensivo è ammesso solo per dual-use *difensivo*, NATO DIANA conditional). Capability offensive richiederebbero classification militare, autorizzazione MAECI export-control, governance non compatibile con modello cooperativo Legacoop + bando civile Coopfond.
> **Parent:** Boundary B1 (cooperative civile) + Cap. 5.7.2 §10.7 + `RESERVED-rischi-geopolitici.md` | **Verification:** Process audit del payload roadmap + contratti commerciali (clausola "no offensive capability") + Cap. 4 Scope review | **Status:** Active | **Confidence:** high | **Falsifying observation:** firma di un contratto/PoC per integrazione di payload kinetic/armamento/targeting militare letale → re-baseline immediato governance + scope + revisione boundary B1.

> **NegR-Geo-003** — Il sistema **NON** deve operare in **difesa pura** (clienti unici Difesa nazionale o NATO con scope ISR/strike) senza una **separazione strutturale** (società dedicata, governance separata, accounting distinto, contratto framework EDF/EDA).
> **Rationale:** la commistione operatore civile + difesa pura comprometterebbe la natura cooperativa Legacoop e l'eligibilità a bandi civili (Coopfond, FESR, PNRR civile). Dual-use *difensivo* è ammesso (es. ISR per Protezione Civile + supporto NATO DIANA in regime di sperimentazione) ma con governance trasparente.
> **Parent:** Boundary B1 + Cap. 5.7.2 + Cap. 7.3 (segmentazione mercato) | **Verification:** Inspection della struttura societaria + bilancio di esercizio (segregazione revenue stream) | **Status:** Active | **Confidence:** high | **Falsifying observation:** > 30% del fatturato annuo da clienti Difesa nazionali senza una società/divisione separata e governance dedicata.

> **NegR-Geo-004** — Il sistema **NON** deve dipendere, per i sottosistemi critici di Phase B (Percorso 6B HALE), da componenti **ITAR-classified** statunitensi senza un piano documentato di EU-sourcing alternative.
> **Rationale:** sovranità tech + ITAR restrictions limitano l'export control e l'autonomia operativa europea (rif. Reg. UE 2021/821 dual-use export). I sottosistemi critici (FCS DAL-C, GNSS anti-spoofing, propulsion solare, batterie LiS/SS) devono essere EU-sourced o avere fonte EU alternative qualificata entro M+24 per Phase B.
> **Parent:** Boundary B2 + `RESERVED-rischi-geopolitici.md` + SyR-F-005 + RSK-GEO-001 | **Verification:** Inspection della BoM (Bill of Materials) per ITAR flag + audit supply chain annuale | **Status:** Active | **Confidence:** medium | **Falsifying observation:** > 20% del valore BoM Phase B in componenti ITAR-classified US senza piano EU-sourcing alternative entro M+24.

##### Famiglia NegR-Reg — Compliance regolatoria

> **NegR-Reg-001** — Il sistema **NON** deve trattare dati personali (immagini riconoscibili di persone, targhe veicoli, dati biometrici, dati di localizzazione individuale) senza una **DPIA documentata e approvata** dal DPO e, ove richiesto dal Garante (rif. GDPR Art. 35-36).
> **Rationale:** GDPR Art. 35 (DPIA obbligatoria per trattamenti ad alto rischio, incluse sorveglianza sistematica e dati biometrici) + posizione Garante 2025 su droni urbani. Trattare dati personali senza DPIA è violazione amministrativa con sanzioni fino al 4% fatturato globale.
> **Parent:** StNeed-008 + StNeed-014 + SyR-C-003 + SsR-GS-003 | **Verification:** Inspection del registro trattamenti + DPIA per ogni caso d'uso che processa imagery riconoscibile | **Status:** Active | **Confidence:** high | **Falsifying observation:** missione operativa che acquisisce imagery riconoscibile di persone senza DPIA depositata e validata dal DPO.

> **NegR-Reg-002** — Il sistema **NON** deve eseguire **onboard processing di dati biometrici** (riconoscimento facciale, identificazione individuale tramite AI inferenza in-flight) né classificare individui in categorie sensibili (etnia, religione, orientamento politico).
> **Rationale:** AI Act (Reg. UE 2024/1689) Art. 5 (pratiche proibite) + Art. 6 Annex III (high-risk systems incluso identificazione biometrica remota). Le pipeline ML on-board del payload EO devono essere progettate per **anonimizzazione automatica edge-level** (blur volti/targhe — già coperto da SsR-GS-003), non per identificazione individuale.
> **Parent:** SyR-C-003 + SsR-GS-003 + AI Act + Garante | **Verification:** Inspection del codice ML on-board (algorithmic audit) + design review del payload AI pipeline | **Status:** Active | **Confidence:** high | **Falsifying observation:** documentazione di una pipeline ML on-board che esegue identificazione biometrica individuale (>1:N matching) senza anonimizzazione preventiva.

> **NegR-Reg-003** — Il sistema **NON** deve operare in **spazio aereo controllato** (CTR, TMA, AWY, classi A-D ICAO) senza coordinamento formale ENAV / D-Flight e clearance ATC esplicita.
> **Rationale:** Reg. UE 2019/947 + ENAC Reg. APR Ed.3 + ENAV procedures U-Space. Operazioni HALE Phase B richiedono climb/descent attraverso CTR Genova, Milano, Roma — il coordinamento ENAV è precondizione non negoziabile. Per Percorso 6A VTOL Pentema, lo spazio aereo è non-controllato (G class) sotto 500 ft AGL ma climb >500 ft AGL deve essere coordinato.
> **Parent:** StNeed-011 + SyR-F-002 + SyR-S-004 | **Verification:** Inspection del Letter of Agreement (LoA) ENAV + Operations Manual procedures ATC | **Status:** Active | **Confidence:** high | **Falsifying observation:** volo BVLOS in CTR senza LoA ENAV e clearance ATC documentata → enforcement ENAC + sospensione operativa.

##### Famiglia NegR-Tech — Architettura tecnica

> **NegR-Tech-001** — Il sistema **NON** deve sviluppare un **Type Certificate** proprio EASA Part 21J (Design Organisation Approval + TC) **in autonomia** per il velivolo HALE Phase B: il TC richiede consorzio EU strutturato (lead OEM Tier 1 + Firmamento come technology partner / service operator).
> **Rationale:** capex TC EASA full-cycle: €50-200M, durata 5-8 anni, manpower 50-150 FTE engineering qualified (vedi Pinato 2023 + AAM business cases). Fuori scope Firmamento standalone. Strategia: certificazione *via* consorzio EU (lead potenziale Leonardo / Airbus DS / partner industriale identificato post-M+24).
> **Parent:** Boundary B2 + Cap. 5.1 + Cap. 6.2 + RSK-FIN-001 | **Verification:** Inspection del piano di certificazione (Cap. 9 + Vol. 2 Allegato A.3) + roadmap consorzio | **Status:** Active | **Confidence:** high | **Falsifying observation:** attivazione di un programma TC standalone Firmamento per HALE Phase B con budget > €5M e timeline > 24 mesi senza partner lead OEM identificato.

> **NegR-Tech-002** — Il sistema **NON** deve utilizzare componenti **DJI** (o altri vendor cinesi soggetti a ban/restrizioni in EU/USA) come componenti critici per il C2 link, autopilota primario, gimbal payload o GS, per applicazioni in regime di sicurezza nazionale o PA italiana.
> **Rationale:** Trump-era + Biden-era + Trump-2 export ban DJI in USA (NDAA 2024); posizione MIT/MEF e ACN su componentistica cinese in PA italiana (rif. NIS2 + Golden Power D.L. 21/2012). Rischio compliance + reputazionale + escalation regolatoria EU.
> **Parent:** SyR-C-004 (NIS2) + AS-008 (vendor JOUAV CN accessibility) + `RESERVED-rischi-geopolitici.md` | **Verification:** Inspection della BoM + audit fornitori (no-DJI clause nei contratti) | **Status:** Active | **Confidence:** medium | **Falsifying observation:** vendor JOUAV (CN) bannato in EU entro M+12 senza piano sostituzione EU vendor (Quantum, FlyingBasket) documentato. NOTA: AS-008 attualmente assume JOUAV accessibile; se invalidata, vendor switch EU obbligatorio con CapEx +30%.

> **NegR-Tech-003** — Il sistema **NON** deve trasferire ground segment, mission control, data hosting o dati operativi a infrastrutture extra-UE come **default operativo**, anche se più economiche.
> **Rationale:** sovranità tech + GDPR + NIS2 + accordi quadro PA italiana che richiedono cloud certificato AgID/ACN (rif. Strategia Cloud Italia + Polo Strategico Nazionale).
> **Parent:** SyR-C-004 + SsR-GS-002 + NegR-Geo-001 | **Verification:** Inspection del physical location dei datacenter + certificazioni AgID/ACN/GAIA-X | **Status:** Active | **Confidence:** high | **Falsifying observation:** spostamento di ground segment o data hosting in datacenter extra-UE per ragioni di costo, senza accordo specifico documentato e DPIA approvata.

##### Famiglia NegR-Mkt — Comunicazione / Posizionamento

> **NegR-Mkt-001** — Il sistema **NON** deve essere comunicato pubblicamente come "**alternativa europea a Starlink**" o "**Starlink europeo**" in materiali ufficiali (pitch deck pubblici, comunicati stampa, sito web, social media, slide investitori non-NDA).
> **Rationale:** boundary condition B2 (linguaggio pubblico: "**complementare a IRIS²**", **non** "alternativa a Starlink"). Ragioni geopolitiche dettagliate in `riferimenti/RESERVED-rischi-geopolitici.md`: evitare confronto diretto con asset US strategico (rischio retaliation tariffaria + diplomatica), preservare opzionalità consorzio EU dove Starlink non è target ma complemento (HAPS layer vs LEO layer).
> **Parent:** Boundary B2 (CLAUDE.md) + `RESERVED-rischi-geopolitici.md` | **Verification:** Process audit dei materiali pubblici (sito, slide, press release) — review pre-publication per ogni materiale > 500 visualizzazioni stimate | **Status:** Active | **Confidence:** boundary | **Falsifying observation:** linguaggio "alternativa Starlink" / "Starlink europeo" appare in materiali pubblici ufficiali → re-baseline messaging + addestramento team comms + revisione governance comunicazione.

> **NegR-Mkt-002** — Il sistema **NON** deve essere comunicato come "**capability militare offensiva**" o "**arma**" o "**UCAV**" (Unmanned Combat Aerial Vehicle) in materiali ufficiali, anche per scopi di marketing in conferenze difesa.
> **Rationale:** coerenza con NegR-Geo-002 (no capability offensive) + NegR-Geo-003 (no difesa pura senza separazione strutturale). Posizionamento pubblico = "servizi ISR civili + dual-use difensivo NATO DIANA conditional", non "armamento aereo".
> **Parent:** Boundary B1 + Cap. 5.7.2 + NegR-Geo-002 | **Verification:** Process audit pre-publication + monitoring stampa e social | **Status:** Active | **Confidence:** high | **Falsifying observation:** materiale pubblico ufficiale Firmamento usa terminologia "UCAV", "armamento", "strike capability" → violazione e revisione immediata.

#### Tabella riepilogativa dei 14 NegR — Priority Matrix

| NegR-ID | Statement breve | Famiglia | Priority | Impact-if-violated | Status | Conf. |
|---|---|---|---|---|---|---|
| **NegR-B-001** | NON vendere velivoli (service-only) | B | **Critical** | Re-baseline business model + perdita boundary B1 + perdita eligibility bando Coopfond | Active | boundary |
| NegR-B-002 | NON offrire retail B2C | B | Medium | Re-scope canali commerciali (limitato impatto se contenuto) | Active | high |
| NegR-B-003 | NON concorrere head-to-head Tier 1 HAPS | B | High | Esaurimento capitale + perdita differenziazione competitive | Active | high |
| **NegR-Geo-001** | NON usare cloud US default | Geo | **Critical** | Violazione GDPR + NIS2 + Schrems II → sanzioni + perdita PA contracts | Active | high |
| **NegR-Geo-002** | NON sviluppare capability dual-use offensiva | Geo | **Critical** | Perdita boundary B1 + perdita bandi civili + escalation diplomatica | Active | high |
| NegR-Geo-003 | NON operare difesa pura senza separazione | Geo | High | Compromissione natura cooperativa + perdita eligibility bandi civili | Active | high |
| NegR-Geo-004 | NON dipendere ITAR US Phase B critici | Geo | High | Perdita sovranità tech + export control restrictions EU | Active | medium |
| **NegR-Reg-001** | NON trattare dati personali senza DPIA | Reg | **Critical** | Sanzioni GDPR fino 4% fatturato + sospensione operativa Garante | Active | high |
| NegR-Reg-002 | NON onboard biometric processing | Reg | High | Violazione AI Act high-risk + sanzioni + reputational damage | Active | high |
| NegR-Reg-003 | NON operare CTR senza ENAV LoA | Reg | High | Enforcement ENAC + sospensione operativa + incidente safety | Active | high |
| NegR-Tech-001 | NON sviluppare TC EASA in autonomia | Tech | High | Esaurimento capitale (€50-200M) + delay 5-8 anni | Active | high |
| NegR-Tech-002 | NON usare componenti DJI/CN bannati PA | Tech | Medium | Compliance NIS2/Golden Power + perdita contratti PA | Active | medium |
| NegR-Tech-003 | NON ospitare ground segment extra-UE | Tech | High | Violazione sovranità + perdita certificazione AgID/PSN | Active | high |
| **NegR-Mkt-001** | NON usare "alternativa Starlink" pubblico | Mkt | **Critical** | Violazione boundary B2 + escalation US + perdita opzionalità EU consortium | Active | boundary |
| NegR-Mkt-002 | NON comunicare come UCAV/arma | Mkt | High | Perdita boundary B1 + escalation politica + perdita bandi civili | Active | high |

**Legenda priority:**
- **Critical** (5 NegR): violazione = re-baseline immediato del progetto / showstopper boundary
- **High** (7 NegR): violazione = revisione formale + remediation plan + gate review
- **Medium** (2 NegR): violazione = correzione operativa entro 30 giorni + log audit

#### Integrazione con la RTM

I 14 NegR sono tracciati nella **RTM v0.5 estesa** (Vol. 2 Allegato A.1) come righe dedicate con `Type = NegR` (oltre ai tipi StNeed / SyR / SsR / IR / VR esistenti). I campi specifici dei NegR sono:

| Campo RTM | Contenuto per NegR |
|---|---|
| Req-ID | NegR-X-NNN (X ∈ {B, Geo, Reg, Tech, Mkt}) |
| Description | Statement in forma "NON deve..." |
| Source | Boundary B1/B2 + parent SyR + RSK-XXX correlato |
| Type | NegR |
| Parent | Boundary condition (CLAUDE.md) o SyR positivo correlato o RSK del Risk Register |
| Priority | Critical / High / Medium / Low |
| V&V Method | Inspection (process audit, contract review, BoM check) — raramente Test |
| V&V Status | Active / Waived (con razionale) / Reviewed |
| Confidence | high / medium / low / boundary |
| Falsifying observation | Evento osservabile che indica violazione |

**Audit semestrale dei NegR**: a ogni gate review (M+6, M+10, M+13, M+24...) il systems engineer + il governance lead conducono uno **status check** dei 14 NegR. Per ciascuno: (i) confermare status Active (default), (ii) richiedere Waiver formale con razionale documentato e approvazione board (downgrade a Waived), (iii) marcare come Reviewed se l'audit non rileva violazioni nel periodo. Il **Waiver** richiede approvazione esplicita di Firmamento board + risk owner + (per NegR Critical) Coopfond / Coopfond stakeholder advisory.

**Trigger di review immediata** (fuori cadenza semestrale): qualunque **falsifying observation** dichiarata triggera review entro 30 giorni con coinvolgimento del red-team-skeptic agent + risk-register-builder skill per re-valutazione boundary conditions.

#### Falsifying observations critiche dettagliate

Per i 3 NegR più critici, riportiamo la falsifying observation in forma estesa con trigger osservabile, fonte di evidenza, azione di remediation:

**FO-NegR-B-001 (NON vendere velivoli)**
- **Trigger osservabile**: firma di un contratto/MoU/LoI di **vendita asset velivolo** (qualunque importo, qualunque cliente) — anche prototype, anche cooperative pilota, anche "vendita simbolica".
- **Fonte di evidenza**: contract registry Firmamento + cap. dichiarazioni fiscali (DR-2025 / DR-2026 dichiarazione redditi) + scrittura privata + pubblicità presso CCIAA.
- **Remediation**: re-baseline immediato del business model in Cap. 1 + revisione boundary B1 in CLAUDE.md (con board approval) + comunicazione formale a Coopfond + revisione narrativa "service-only" in tutti i materiali pubblici.

**FO-NegR-Geo-001 (NON cloud US default per imagery EO)**
- **Trigger osservabile**: imagery EO o dati C2 o dati personali UE stoccati in **datacenter US** (AWS, Azure, GCP region us-east-1, us-west-2, ecc.) **senza**: (i) accordo specifico documentato (es. EU-US Data Privacy Framework adequacy decision per quel trattamento), (ii) DPIA approvata dal DPO, (iii) DR esplicito tracciato in Risk Register.
- **Fonte di evidenza**: cloud audit log (provider) + DNS resolution endpoint + audit trail data residency + ispezione contratto SaaS/IaaS.
- **Remediation**: migrazione obbligatoria entro 30 giorni a cloud EU sovrano (Aruba, OVH, IONOS, PSN) + notifica Garante (Art. 33 GDPR breach assessment) + log incident in Risk Register come RSK-REG-NEW + addestramento team DevOps.

**FO-NegR-Mkt-001 (NON usare "alternativa Starlink" pubblico)**
- **Trigger osservabile**: linguaggio "**alternativa Starlink**", "**Starlink europeo**", "**competitor di Starlink**" appare in: (i) sito web pubblico Firmamento, (ii) comunicato stampa ufficiale, (iii) pitch deck per investitori non-NDA o per finanziatori istituzionali, (iv) post social media account ufficiale, (v) intervista pubblica esponente Firmamento (CEO, CTO, comms lead).
- **Fonte di evidenza**: monitoring stampa (Google Alerts + Mention + Brand24) + web archive snapshot + screenshot social + transcript intervista.
- **Remediation**: rimozione/correzione del materiale entro 7 giorni + statement correttivo pubblico + retraining team comms + governance review della catena di approvazione materiali pubblici + log violazione in Risk Register come RSK-GEO-NEW.

#### Caveat — NegR vs Risk Register

I Negative Requirements **non sostituiscono** il Risk Register (Vol. 2 Allegato A.2). I due strumenti sono **complementari** e operano su orizzonti diversi:

| Aspetto | Risk Register (RSK-XXX) | Negative Requirements (NegR-X-NNN) |
|---|---|---|
| Natura | Evento incerto futuro con P×I | Vincolo di disegno dichiarato come boundary del sistema |
| Quando si applica | Solo se si manifesta (probabilità < 1) | Sempre, durante tutto il lifecycle del progetto |
| Modalità di trattamento | Mitigation plan + owner + KRI monitoring | Compliance + inspection + audit + waiver process |
| Esempio | RSK-REG-001: "ENAC ritarda SAIL approval" | NegR-Reg-003: "Sistema NON deve operare CTR senza ENAV LoA" |
| Trigger di azione | KRI threshold breach (es. probability ≥ 50%) | Falsifying observation (violazione osservata o imminente) |
| Output | Risk Register table + heatmap P×I | RTM rows + audit semestrale + waiver log |

In sintesi: un **RSK** è qualcosa che **potrebbe accadere e va mitigato**; un **NegR** è qualcosa che **non deve accadere per design**. La violazione di un NegR Critical equivale al manifestarsi di un risk di livello rosso ad alto impatto — ma a differenza del risk, il NegR non ha probabilità < 1 di occorrere: la probabilità è governata dalla disciplina operativa interna, non da eventi esterni.

I NegR sono inoltre coordinati con le 3 skill di project governance:
- **`requirements-traceability-matrix`** — i NegR estendono la tassonomia RTM e sono tracciati con la stessa rigorosità dei SyR positivi
- **`risk-register-builder`** — ogni falsifying observation di un NegR diventa un evento di re-baseline che innesca aggiornamento del Risk Register
- **`epistemic-rigor`** — i NegR sono dichiarati con confidence level + falsifying observation, in piena coerenza con la disciplina epistemica del progetto

---

## 3.6 Subsystem Requirements (SsR) — Campione rappresentativo

I System Requirements sono **decomposti** in Subsystem Requirements, allocati ai 6 sottosistemi principali del sistema. Riportiamo qui un **campione rappresentativo** per ciascun sottosistema; la lista completa (~80 SsR) è in Vol. 2 Allegato A.1.

### 3.6.1 Sottosistema AERO — Aerodinamica e Strutture

> **SsR-AERO-001** — [Percorso 6B] Wing aspect ratio (AR) ≥ 25 per minimizzare resistenza indotta.
> **Parent:** SyR-P-004 (L/D ≥ 25) | **Verification:** A | **Confidence: high**

> **SsR-AERO-002** — [Percorso 6B] Layup composito longherone alare: CFRP standard con cap moduli alti (HM); fibra di lino solo strutture secondarie (vedi Cap. 5.8 + Pinato 2023). **Falsifying observation:** uso lino in longherone primario richiederebbe qualification path aerospace 5-10 anni, fuori scope progetto.
> **Parent:** SyR-E-003 | **Confidence: high** | **Trade Study:** TS-MATERIAL

### 3.6.2 Sottosistema PROP — Propulsione ed Energia

> **SsR-PROP-001** — [Percorso 6A] Powertrain ibrido VTOL+cruise commerciale TRL ≥ 8.
> **Parent:** SyR-F-001 + scelta JOUAV/equivalente | **Verification:** I (datasheet vendor) | **Confidence: medium**

> **SsR-PROP-002** — [Percorso 6B] Pannelli solari multi-junction GaAs efficienza η ≥ 30% (worst case after 1y degradation in stratosphere).
> **Parent:** SyR-P-005, -006 (energy balance) | **Verification:** A + T panel-level | **Confidence: medium**

> **SsR-PROP-003** — [Percorso 6B] Batterie Li-S o SS Li, densità energetica pack ≥ 350 Wh/kg (TRL ≥ 5 nel 2027-2028 target).
> **Parent:** SyR-P-006 (energy balance worst case) | **Verification:** I + T cell-level | **Confidence: low** | **Risk:** RSK-TEC-001

### 3.6.3 Sottosistema AVI — Avionica, GNC, FCS

> **SsR-AVI-001** — [Percorso 6A] Autopilota: TRL ≥ 8 con DAL-C minimo per FCS (es. MicroPilot, UAVOS, Pixhawk Cube modificato).
> **Parent:** SyR-F-002 (SAIL III) + Reg. ENAC Art. 26 | **Verification:** I | **Confidence: medium**

> **SsR-AVI-002** — [Percorso 6A] C2 link primary + secondary: combinazione RF terrestre (2.4 GHz o 5.8 GHz) + SATCOM L-band (Iridium Certus) per shadow zones Pentema.
> **Parent:** SyR-S-001 (Lost-Link) | **Verification:** T (range test) | **Confidence: medium**

> **SsR-AVI-003** — [Percorso 6A] GNSS dual-frequency multi-constellation (GPS L1/L5 + Galileo E1/E5a + GLONASS) con anti-spoofing.
> **Parent:** SyR-S-003 (sensor redundancy) | **Confidence: high**

### 3.6.4 Sottosistema PAY — Payload (EO + Telecom)

> **SsR-PAY-001** — [Percorso 6A] Sensore RGB high-res Phase One iXM 100 o equivalente, GSD ≤ 8 cm @ 500 m AGL.
> **Parent:** SyR-F-001 | **Verification:** I (datasheet) + T (fly-and-measure) | **Confidence: medium**

> **SsR-PAY-002** — [Percorso 6A] Sensore IR LWIR (8-14 µm) NEdT ≤ 50 mK, GSD termico ≤ 5 m @ 500 m AGL.
> **Parent:** SyR-F-003 (antincendio) | **Verification:** I + T | **Confidence: medium**

> **SsR-PAY-003** — [Percorso 6A] LTE eNodeB tattico (es. Athonet, Druid), potenza ≤ 50 W RF, banda licenziata o ISM in mode di emergenza.
> **Parent:** SyR-F-004 | **Verification:** T | **Confidence: low** | **Risk:** RSK-REG-005 (AGCOM)

> **SsR-PAY-004** — [Percorso 6B] gNodeB 5G NR-NTN Rel-17/18 con beamforming digitale, 8-32 beams, banda S-band o 700 MHz.
> **Parent:** SyR-F-005 + Cap. 5.5.3 | **Verification:** A (link budget) + T | **Confidence: low**

### 3.6.5 Sottosistema COMMS — Comunicazioni e Link

> **SsR-COMMS-001** — Link budget service link 2.6 GHz @ 25 km slant range: SNR ≥ 11 dB con disponibilità 99.5% (rain fade ITU-R P.618-14 zona K).
> **Parent:** SyR-F-001 + skill `link-budget-calculator` | **Verification:** A | **Confidence: high** | **Source:** ITU-R P.618-14 + 3GPP TR 38.821 v16.2.0

### 3.6.6 Sottosistema GS — Ground Segment

> **SsR-GS-001** — Ground Station fissa Pentema: copertura visiva del sito di operatione + connettività backup (4G/SATCOM); supporto pilota remoto + operatore payload.
> **Parent:** SyR-O-001, -002 | **Verification:** I + D | **Confidence: high**

> **SsR-GS-002** — Cloud / data hosting Italia/EU (Aruba, OVH, GAIA-X compliant), GDPR + NIS2 compliant, no cloud US/CN per default.
> **Parent:** SyR-C-003, -004 | **Verification:** I | **Confidence: high**

> **SsR-GS-003** — Pipeline processing imagery: anonimizzazione (blur volti/targhe) automatica edge-level, GIS-ready output entro 24h da acquisizione (non-emergenza) o entro 30 min (emergenza).
> **Parent:** SyR-C-003 (GDPR) + StNeed-008 | **Verification:** D | **Confidence: medium**

---

## 3.7 Verification & Validation Plan — Preliminare

In coerenza con NASA SE Handbook §5.3 (Verification) e §5.4 (Validation) [^1], il **V&V Plan preliminare** definisce per ogni requisito il **metodo di verifica** e la **fase di V&V** target.

I 4 metodi standard (cf. skill `requirements-traceability-matrix`):

| Codice | Metodo | Tipico per |
|---|---|---|
| **I** | Inspection | Verifica documentale / visiva (datasheet, etichette, processo) |
| **A** | Analysis | Calcoli, simulazioni, modeling (es. link budget, energy balance) |
| **D** | Demonstration | Esercizio operativo del sistema |
| **T** | Test | Misure quantitative su prototype / articolo di volo |

**Distribuzione metodi V&V per i 42 SyR baseline:**

| Famiglia | I | A | D | T | Totale |
|---|---|---|---|---|---|
| F — Functional | 1 | 2 | 1 | 1 | 5 |
| P — Performance | 0 | 3 | 0 | 3 | 6 |
| O — Operational | 1 | 0 | 2 | 0 | 3 |
| S — Safety | 1 | 0 | 2 | 1 | 4 |
| E — Environmental | 2 | 0 | 0 | 1 | 3 |
| C — Compliance | 6 | 0 | 0 | 0 | 6 |
| Cost — Cost & Business | 3 | 1 | 0 | 0 | 4 |
| **Totale** | **14** | **6** | **5** | **6** | **31** |

(Restanti 11 SyR: SsR/IR/VR allocati a livelli inferiori, non riportati in tabella.)

**Distribuzione per fase NASA SE V-model:**

| Fase | SyR target |
|---|---|
| Pre-Phase A (M+0-3) | Inspection compliance (SyR-C-001-006) |
| Phase A (M+3-12) | Analysis (link budget, energy balance, FMECA) |
| Phase B (M+12-24) | Demonstration in test bed + Test subscale |
| Phase C-D (M+24-48) | Test full-scale (per Percorso 6B) |

---

## 3.8 Requirements Traceability Matrix (RTM v0.5)

La RTM completa è in Vol. 2 Allegato A.1. Riportiamo qui un **estratto rappresentativo** per dimostrare la struttura.

### 3.8.1 Estratto RTM — Caso d'uso "Antincendio boschivo Pentema"

| Req-ID | Description | Rationale | Source | Type | Parent | Owner agent | Priority | V&V Method | V&V Status | Phase | Trade Study | Risks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| StNeed-002 | PC Liguria + CC Forestali vogliono alert hotspot termico ≤ 5 min | Tempestività intervento antincendio | Protocollo PC Liguria | StNeed | – | snai-funding-expert | High | – | – | Pre-A | – | RSK-OPS-002 |
| SyR-F-003 | Sistema rileva hotspot ≥ 40°C, alert + thumbnail in ≤ 5 min | Soddisfare StNeed-002 con margine di confidenza | StNeed-002 | SyR | StNeed-002 | aerospace-SE | High | D + T | Open | Phase A | – | RSK-OPS-002 |
| SsR-PAY-002 | IR LWIR sensor, NEdT ≤ 50 mK, GSD ≤ 5 m @ 500 m AGL | Compliance SyR-F-003 + risoluzione termica utile | SyR-F-003 | SsR | SyR-F-003 | EO-expert | High | I + T | Open | Phase A | TS-PAYLOAD-EO | RSK-OPS-002 |
| SsR-COMMS-001 | C2 + dati downlink ≥ 50 kbps + thumbnail in ≤ 30 s | Compliance SyR-F-003 con margine | SyR-F-003 | SsR | SyR-F-003 | telecom-payload | Medium | A + T | Open | Phase A | – | – |
| SsR-GS-001 | GS riceve alert + push a interfaccia PC in ≤ 60 s | Catena end-to-end SyR-F-003 | SyR-F-003 | SsR | SyR-F-003 | aerospace-SE | High | D | Open | Phase A | – | – |
| VR-F-003.1 | Verify SyR-F-003 by Demonstration in scenario fuoco-pilota | – | SyR-F-003 | VR | SyR-F-003 | V&V engineer | High | D | Planned | Phase A | – | – |
| VR-F-003.2 | Verify SyR-F-003 by Analysis of FAR (False Alarm Rate) target ≤ 5% | – | SyR-F-003 | VR | SyR-F-003 | V&V engineer | High | A | Planned | Phase A | – | – |

### 3.8.2 Tasso di copertura RTM v0.5

| Metrica | Valore baseline | Soglia per gate M+6 | Soglia per gate M+10 |
|---|---|---|---|
| StNeeds con SyR figlio | 17/17 (100%) | 100% | 100% |
| SyR con SsR figlio (decomposti) | 31/42 (74%) | 80% | 95% |
| SyR con metodo V&V definito | 31/42 (74%) | 80% | 100% |
| SsR con allocazione subsystem | 80/80 (100%) | 100% | 100% |
| Orphan SyR (senza parent StNeed) | 0 | 0 | 0 |
| Untestable SyR | 3 (Cost SyR senza verifica D/T) | 2 | 0 |
| **NegR con status Active / monitored** | **14/14 (100%)** (5 Critical + 7 High + 2 Medium) — audit semestrale | 14/14 Active + 0 violazioni rilevate | 14/14 Active + 0 violazioni rilevate + waiver log up-to-date |

---

## 3.9 Assumptions e Limiti (baseline)

Le **assunzioni** sotto sono dichiarate esplicitamente. La loro **invalidazione** richiede revisione dei requisiti dipendenti.

### 3.9.1 Assumptions baseline

| ID | Assunzione | Conf. | Impatto se invalidata |
|---|---|---|---|
| AS-001 | Regione Liguria mantiene impegno per pilota Pentema almeno fino M+24 | medium | re-design anchor customer, ricerca alternative regioni SNAI |
| AS-002 | Coopfond rinnova bando Cooding nel 2026 con condizioni analoghe a 2025 | medium | re-design funding plan, ricerca alternative |
| AS-003 | Almeno 8 cooperative su 10 mantengono adesione al gruppo pilota | medium | re-design partnership Legacoop |
| AS-004 | ENAC riconosce Pentema come SAIL II-III BVLOS feasible | medium | re-design ConOps (VLOS-only, areas more isolate) |
| AS-005 | EASA pubblica framework HAPS RMT entro M+36 | low | Percorso 6B Phase B rinviato/cancellato |
| AS-006 | AGCOM apre licensing dedicato HAPS entro WRC-27 | low | Percorso 6B payload commerciale telecom rinviato |
| AS-007 | Tech batterie LiS / SS raggiunge 350 Wh/kg pack-level entro 2028 | low | Percorso 6B energy balance fail, seasonal-only fallback |
| AS-008 | Vendor JOUAV (o equivalente CN) accessibile commercialmente in EU | medium | re-source vendor EU (Quantum, FlyingBasket), CapEx +30% |
| AS-009 | Comunità Pentema accetta sperimentazione con DPIA pubblica | medium | re-design caso d'uso + relocate pilota |
| AS-010 | Risorse umane (piloti UAS, ingegneri) reperibili in IT/EU | medium | turnover risk, formazione in-house richiesta |

(Altre 24 assumptions di dettaglio: Vol. 2 Allegato A.1)

### 3.9.2 Limiti dichiarati dello Studio

1. **Scope temporale**: lo Studio approva solo i passi 1-2 della visione (M+0 → M+48), non l'intera roadmap 10 anni.
2. **Confidence aggregata**: come dichiarato in `audit-rigore-epistemico.md`, la confidence media del documento è **medium-low**, con 15 voci di debito di rigore (DR-001 → DR-015) ancora aperte.
3. **Validazione esterna**: lo Studio non è stato validato da ente terzo (RINA, DNV); validazione è raccomandata per uso "investment-grade".
4. **Numerosità requisiti**: 42 SyR + 80 SsR sono **baseline minima**. La RTM completa richiede tipicamente 200-500 requisiti per un programma aerospace di questa scala.

---

## 3.10 Open Questions (OQ)

Le **Open Questions** sono i quesiti irrisolti che devono essere chiusi per i gate successivi. Ne riportiamo 18 prioritarie; la lista completa è in Vol. 2 Allegato A.1.

| OQ-ID | Domanda | Trigger per chiusura | Owner agent | Deadline |
|---|---|---|---|---|
| OQ-001 | Quale piattaforma VTOL baseline (JOUAV CW-30E vs Quantum vs FlyingBasket)? | Trade Study TS-PLATFORM-6A | vtol-uas-specialist | M+6 |
| OQ-002 | Quale SAIL finale ENAC per Pentema BVLOS? | Pre-application meeting | aviation-regulatory-counsel | M+6 |
| OQ-003 | Quale layup composito longherone HALE? | Trade Study TS-MATERIAL | aero-structures-engineer | M+12 |
| OQ-004 | Energy balance HALE inverno 44°N feasible o seasonal fallback? | Simulazione completa | propulsion-energy-engineer | M+10 |
| OQ-005 | Quale architettura propulsione 6B (solar+LiS vs solar+SS vs solar+H2)? | Trade Study TS-PROP | propulsion-energy-engineer | M+12 |
| OQ-006 | Quale autopilota 6A (commerciale vs custom DAL-C)? | Trade Study TS-AVI | avionics-gnc-engineer | M+6 |
| OQ-007 | Quale payload modulare baseline 6A (EO+IR vs EO+IR+LiDAR vs EO+IR+telecom)? | Trade Study TS-PAYLOAD | earth-observation-expert | M+6 |
| OQ-008 | Banda radio operativa per payload telecom 6A: ISM vs banda commerciale licenziata? | Engagement AGCOM | telecom-ntn-payload-expert | M+9 |
| OQ-009 | Quale ground segment scope (fissa+mobile vs solo mobile)? | Decisione operativa post-ConOps | aerospace-SE | M+6 |
| OQ-010 | Quale anchor customer Regione Liguria (DGR + LoI)? | Engagement Regione | snai-funding-territorial-expert | M+6 |
| OQ-011 | Quale ruolo cooperative (utenti vs co-investitori)? | Workshop cooperative | business-model-strategist | M+6 |
| OQ-012 | Quale partnership CIRA per Percorso 6B? | Engagement CIRA | sovereign-strategist | M+9 |
| OQ-013 | Quale test bed per Percorso 6A BVLOS (Pentema vs GATB Grottaglie vs altri)? | Verifica disponibilità + costi | vtol-uas-specialist | M+6 |
| OQ-014 | Quale modello pricing servizi PA (canone vs ore-volo vs outcome-based)? | Negoziazione Regione | business-model-strategist | M+9 |
| OQ-015 | Quale mix finanziamenti Y1 (Coopfond + FESR + equity + R&D credit)? | Mappatura bandi disponibili | financial-cfo-analyst | M+6 |
| OQ-016 | Quale governance Firmamento + cooperative (RTI vs JV vs contratto rete)? | Decisione strategica + legale | business-model-strategist | M+9 |
| OQ-017 | DPIA preliminare: quale risposta Garante? | Workshop privacy + DPIA pubblica | data-privacy-counsel | M+6 |
| OQ-018 | Quale calendario gate decisionali (M+3, M+6, M+10, M+12)? | Master schedule | aerospace-SE | M+3 |

---

## 3.11 Red Team Check — Critical Review

L'agente `red-team-skeptic` ha condotto attacco strutturato al presente capitolo. Sintesi delle critiche e risposte:

### Critica 1 — "I 17 StNeeds sono raccolti senza workshop strutturati con TUTTI gli stakeholder"
**Razionale critica**: il documento parla di "raccolta tramite Briefing + analisi documentale + workshop in corso". Workshop "in corso" non è "fatto". Confidence dichiarata medium-low per StNeeds principali.
**Risposta**: corretto. Il capitolo lo dichiara esplicitamente in §3.3.2 (Confidence: low-medium per StNeeds principali). Workshop strutturati pianificati M+3-6 con cooperative + Regione + PC. Il set baseline è **provvisorio**, da validare.
**Action item**: workshop strutturati con stakeholder primari (S-02, S-03, S-04, S-06) entro M+6. Update RTM v0.6.

### Critica 2 — "I 42 SyR sono basati su numeri spesso non triangolati"
**Razionale critica**: SyR-P-001 (autonomia ≥ 4h Pentema) e SyR-P-002 (velocità ≥ 100 km/h) sono numeri vendor-driven (JOUAV CW-30E datasheet). Non validati da operatori EU.
**Risposta**: confermato. È debito di rigore DR-003 (vedi `audit-rigore-epistemico.md`). I numeri sono dichiarati confidence medium, e sono **input di progetto**, non claim di marketing. La validazione richiede quotation + reference da operatori EU.
**Action item**: contatto distributore JOUAV EU + reference call con almeno 2 operatori EU che già operano CW-30E o equivalente, entro M+3.

### Critica 3 — "L'energy balance HALE inverno (SyR-P-006) è il vero showstopper non risolto"
**Razionale critica**: il SyR dichiara "margine ≥ 30% O seasonal-only fallback". È una **clausola di sopravvivenza**, non un requisito. Operativamente significa "ammettiamo di non riuscire a fare HALE perennial in inverno a 44°N".
**Risposta**: confermato. Il **fallback seasonal-only** (operazione marzo-ottobre) è esplicitamente la mitigazione del rischio RSK-TEC-001. È una scelta strategica accettata: Y3 perennial estivo, Y6+ perennial annuale solo se tech batterie raggiunge target.
**Action item**: simulazione energy balance completa worst-case M+6-10 con propulsion-energy-engineer per decisione formale (Y3 estivo vs Y5+ annuale).

### Critica 4 — "Le boundary conditions B1 e B2 sono dichiarate fuori critica, ma i SyR cost (-001, -002, -003) sono assumption-driven non validati"
**Razionale critica**: SyR-Cost-001 (CapEx ≤ €1.2M) e SyR-Cost-003 (Revenue Y1 ≥ €200k) sono soglie di progetto, non requisiti validati da mercato.
**Risposta**: confermato. Sono SyR di tipo "stakeholder expectation" (Firmamento + Coopfond) con confidence medium. Falsifying observation per SyR-Cost-003 è già dichiarata (revenue Y1 < €100k → revisione drastica MVP scope).
**Action item**: Cap. 8 (Economico-finanziario) deve produrre scenari worst/base/best con sensitivity sul revenue Y1, NON solo lo scenario base.

### Critica 5 — "I 17 StNeeds non includono need negativi (cosa NON dobbiamo fare)"
**Razionale critica**: i requisiti "anti-pattern" (es. "il sistema non deve usare cloud US per stoccaggio imagery EO") sono assenti.
**Risposta**: **RISOLTO nella revisione M+3 estesa**. Aggiunta sezione **§3.5.8 Negative Requirements (NegR)** con **14 requisiti negativi** organizzati in 5 famiglie (NegR-B Business, NegR-Geo Sovranità, NegR-Reg Regolatoria, NegR-Tech Tecnica, NegR-Mkt Comunicazione), di cui 5 Critical (NegR-B-001 no vendita velivoli, NegR-Geo-001 no cloud US default, NegR-Geo-002 no capability dual-use offensiva, NegR-Reg-001 no trattamento dati personali senza DPIA, NegR-Mkt-001 no linguaggio "alternativa Starlink") + 7 High + 2 Medium. Ciascun NegR tracciato in RTM v0.5 estesa con falsifying observation, verification method (Inspection / process audit / contract review), confidence level e status (Active / Waived / Reviewed). Audit semestrale dei NegR a ogni gate review. Coordinamento con Risk Register (RSK-GEO / RSK-REG) chiarito: NegR sono vincoli di disegno, RSK sono eventi incerti — strumenti complementari, non sostitutivi.
**Action item**: ✓ **chiuso M+3**. Prossimo step: estensione fine-grained nella RTM v0.6 (M+6) con eventuali NegR addizionali emersi dai workshop stakeholder + pre-application meeting ENAC.

### Critica 6 — "Tasso di copertura RTM 74% al M+3 è basso per un gate M+6"
**Razionale critica**: target 80% al gate M+6 (cf. §3.8.2). 74% al M+3 lascia 6 SyR senza decomposizione e 11 senza V&V plan completo.
**Risposta**: confermato. Lavoro residuo per portare la RTM a 80% al M+6: ~15-25 ore di analyst engineering work, fattibile.
**Action item**: aerospace-SE lavora sulla decomposizione SsR mancanti e V&V Plan completo per i 6 SyR aperti entro M+5.

---

## 3.12 Riferimenti

[^1]: NASA Systems Engineering Handbook Rev 2 (NASA/SP-2016-6105 Rev 2). Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. Specifico: §4.0 System Design Processes, §4.1 Stakeholder Expectations Definition, §4.2 Technical Requirements Definition, §5.3-5.4 V&V Processes. Confidence: high (norma metodologica internazionale).

[^2]: INCOSE Systems Engineering Handbook, 5th Edition (2023). Riferimento esterno (non incluso in `fonti/`); citato per coerenza metodologica VAFC.

[^3]: ISO/IEC/IEEE 15288:2015 "Systems and software engineering — System life cycle processes". Standard di riferimento internazionale per il systems engineering.

[^4]: Reg. UE 2019/947 (Operations UAS). Source: `fonti/CELEX_32019R0947_IT_TXT.md`. Confidence: high. Vedi Cap. 5 di questo Studio per analisi dettagliata.

[^5]: ENAC Regolamento "Mezzi Aerei a Pilotaggio Remoto" Ed. 3 + Emendamento 1. Source: `fonti/Regolamento_APR_Ed_3_Emend_1.md`. Confidence: high.

[^6]: Skill `requirements-traceability-matrix` (`/.claude/skills/requirements-traceability-matrix/SKILL.md`) — workflow di costruzione RTM applicato in questo capitolo.

[^7]: Skill `epistemic-rigor` (`/.claude/skills/epistemic-rigor/SKILL.md`) — disciplina di falsifiability + triangulation + source provenance applicata in questo capitolo.

---

## 3.13 Note di chiusura del capitolo

La baseline dei requisiti M+3 è stata redatta usando il NASA SE Handbook come riferimento metodologico autoritativo e citando direttamente dal documento ufficiale NASA. Il set baseline (17 StNeeds + 42 SyR + ~80 SsR) è sufficiente come **punto di partenza** per i Cap. 6-7-8.

**Prossimi step richiesti** (in ordine di criticità per i gate M+6 e M+10):

1. **Workshop strutturati con stakeholder primari** (M+3-6) per validare i 17 StNeeds
2. **Pre-application meeting ENAC** (M+3-6) per validare SyR-F-002 (SAIL) e SyR-C-002 (SORA application)
3. **Trade Studies chiave** (M+6 → M+12) per chiudere OQ-001 (platform), OQ-003 (material), OQ-005 (propulsion), OQ-006 (autopilot), OQ-007 (payload)
4. **RTM expansion** verso copertura 80% al M+6 e 95% al M+10
5. ~~Negative Requirements addition~~ ✓ **CHIUSO M+3** — §3.5.8 con 14 NegR in 5 famiglie. Estensione fine-grained M+6 con NegR emersi dai workshop stakeholder.
6. **Audit semestrale NegR** (M+6, M+10, M+13...): status check Active/Waived/Reviewed dei 14 NegR + verifica assenza falsifying observations

**Versionamento RTM**:
- v0.5 (M+3, presente capitolo): 17 StNeed + 42 SyR + 80 SsR (campione)
- v0.6 (M+6): post-workshop stakeholder + 30% expansion
- v0.8 (M+10): post trade study + V&V plan completo
- v1.0 (M+12, baseline finale per Phase B): set congelato per Operations Manual e SORA application

Il capitolo è **chiuso al M+3** con verdetto Red Team **OK con action items**.
