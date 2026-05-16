---
name: gate-review-checklist
description: Use when the user needs to prepare, execute, or document a Go/No-Go gate decision for the HALE Feasibility Study. Trigger phrases - "gate review", "Go/No-Go", "M+3", "M+6", "M+10", "M+11", "M+24", "gate decisionale", "verdetto", "criteri di uscita", "entry criteria", "exit criteria", "review checklist", "gate package". Generates entry/exit criteria, deliverable checklists, decision frameworks for the gate-driven NASA SE approach applied to HALE.
---

# Gate Review Checklist — HALE Decision Gates

Skill per gestire i **gate decisionali Go/No-Go** del progetto HALE secondo la metodologia **NASA SE Handbook §3.0 (Project Life Cycle Reviews)** + customizzazione per il caso italiano (Coopfond, Regione Liguria, ENAC).

## Quando usare

- Preparazione di un gate review imminente
- Compilazione del **gate package** (documenti da presentare alla board)
- Definizione **entry criteria** e **exit criteria** di un gate
- Verbalizzazione decisione (Go / Go Condizionato / No-Go / Hold)
- Allegato di compliance per finanziatori (Coopfond, Regione)

## Mappa gate del progetto HALE

| Gate | Milestone | Fase NASA SE | Verdetto target | Deliverable principali |
|---|---|---|---|---|
| **G0** | M+0 | Pre-Phase A | Kick-off (no formal Go/No-Go) | Briefing iniziale, contratto Cooding |
| **G1** | M+3 | Pre-Phase A → A | Concept frozen | Concept document, StNeeds raccolti, Risk Register v0 |
| **G2** | M+6 | Phase A | Architecture baselined | Architettura 6A + 6B baseline, RTM v0.5, ICD prelim, primi Trade Study |
| **G3** | M+10/M+11 | Phase A → B (FEASIBILITY GATE PRIMARIO) | Go / Hold per ciascun percorso | Studio di Fattibilità completo (Vol.1+2+3), tutti trade study chiusi, Risk Register consolidato, Quadro Economico |
| **G4** | M+12 | Fine pilota VTOL (Percorso 6A) | Go espansione SNAI / Hold | Operational results, customer feedback, financial Y1 |
| **G5** | M+24 | Eval HALE R&D (Percorso 6B) | Go Phase B HALE / Defer | EuroHAPS lessons learned, funding readiness EDF/Horizon, regulatory progress HAPS |
| **G6** | M+36+ | HALE Phase B → C | Type Cert path / No-Go | TC Certification Plan, Type Cert Basis, prototype performance |

## Verdetti possibili

| Verdetto | Significato | Conseguenze |
|---|---|---|
| **Go** | Tutte le evidenze a posto | Procedi alla fase successiva con budget completo |
| **Go Condizionato** | Evidenze ok ma con riserve | Procedi con condizioni esplicite + checkpoint anticipato |
| **Hold** | Evidenze mancanti / inconsistenti | Sospendi, recupera evidenze, re-do gate review |
| **No-Go** | Showstopper insuperabile | Stop, valuta pivot, scrivi lessons learned |
| **Defer** | Decisione rinviata | Procedi su parallel paths, decisione a date X |

## Entry criteria — cosa serve PRIMA del gate

Per ogni gate, l'entry criteria definisce i deliverable che devono essere completati per **poter** tenere il review:

### G1 (M+3) — Concept Frozen
- [ ] Briefing iniziale rivisto e approvato
- [ ] Stakeholder identificati e prima mappa engagement
- [ ] StNeeds raccolti (≥ 20 needs documentati con stakeholder)
- [ ] Vincoli e assunzioni iniziali baselined
- [ ] Risk Register v0 (top-10 rischi identificati)
- [ ] Quadro Esigenziale (QE) bozza
- [ ] Identificazione gate successivi e timing

### G2 (M+6) — Architecture Baselined
- [ ] Architettura concettuale 6A + 6B documentata (Cap. 6.1)
- [ ] System Requirements baselined (SyR-XXX completi, ≥ 30 SyR)
- [ ] RTM v0.5 (tracciabilità StNeeds → SyR)
- [ ] ICD preliminare (interfacce principali)
- [ ] Trade Study chiave conclusi (es. TS-PLATFORM-6A, TS-MATERIAL, TS-PROP-6B)
- [ ] Risk Register v1 con scoring P×I
- [ ] DOCFAP draft per le decisioni architetturali principali

### G3 (M+10/M+11) — **FEASIBILITY GATE PRIMARIO** ⭐
- [ ] Studio di Fattibilità Vol.1 + Vol.2 + Vol.3 completo
- [ ] Tutti i trade study chiusi e DOCFAP redatto
- [ ] RTM v1.0 (≥ 80% StNeeds tracciati a SyR; ≥ 80% SyR con V&V method definito)
- [ ] Risk Register v2 (top rischi mitigation actions in progress / planned)
- [ ] Quadro Economico (art. 41) approvato
- [ ] Piano economico-finanziario con sensitivity
- [ ] Strategia finanziamenti consolidata
- [ ] Engagement preliminare ENAC (SORA per 6A, dialogo HAPS per 6B)
- [ ] Engagement Regione Liguria (commitment ufficiale)
- [ ] Privacy/GDPR DPIA preliminare
- [ ] Master schedule M+12 → M+48

### G4 (M+12) — Fine Pilota VTOL
- [ ] Operations Y1 completate
- [ ] ≥ 50 missioni eseguite
- [ ] Customer feedback Regione + PC + cooperative documentato
- [ ] Financial Y1 (utilization, revenue, OpEx)
- [ ] Lessons learned report
- [ ] Plan espansione SNAI multi-area redatto

### G5 (M+24) — Evaluation HALE R&D
- [ ] Risultati EuroHAPS / CIRA collaboration valutati
- [ ] Funding readiness (commitment finanziatori per Phase B €5.5M+)
- [ ] Regulatory progress (EASA Special Condition HAPS in costruzione)
- [ ] Technology maturity 6B subsystems re-assessed (TRL targets)

## Exit criteria — cosa serve PER passare al gate

L'exit criteria del gate corrente = entry criteria del prossimo (in genere).

Inoltre per ogni gate:
- [ ] Decisione formalmente verbalizzata
- [ ] Action items registrati con owner e deadline
- [ ] Risk Register aggiornato post-gate
- [ ] Comunicazione decisione agli stakeholder

## Composizione board del gate review

### Board standard (interno)
- Project Manager (chair)
- Aerospace Systems Engineer (technical lead)
- Financial CFO Analyst
- Aviation Regulatory Counsel
- Business Model Strategist

### Board allargato (per gate G3 — Feasibility primario)
- Tutti i sopra +
- Rappresentante Regione Liguria
- Rappresentante Coopfond
- Rappresentante cooperative (Fabrica capofila)
- Independent reviewer (es. consultant aerospace senior, eventuale RINA)
- Osservatore ENAC (informale, ove possibile)

## Gate Package — template

```markdown
# Gate Review Package — Gate G-X (M+N)

## 0. Executive Summary (1 pagina)
- Periodo coperto
- Risultati principali
- Verdetto proposto: [Go / Go Condizionato / Hold / No-Go]
- Condizioni / azioni richieste

## 1. Entry Criteria Status
[Checklist completata]

## 2. Deliverable status
- [ ] Vol. 1 — Studio (capitoli rilevanti)
- [ ] Vol. 2 — Allegati tecnici
- [ ] Vol. 3 — Riferimenti

## 3. Achievements
- Tecnici
- Regolatori
- Finanziari
- Mercato/Business
- Operativi

## 4. Open issues / blockers
- Issue tecnici aperti
- Issue regolatori aperti
- Issue finanziari aperti

## 5. Risk update
- Top-10 rischi attivi
- Showstopper status
- Mitigation actions

## 6. Recommendation
- Verdetto proposto
- Razionale (3-5 punti)
- Condizioni (se Go Condizionato)
- Alternative scenarios

## 7. Action items post-gate
- Owner, deadline, ID

## 8. Verbale di decisione
- Verdetto finale (firmato)
- Data
- Membri board presenti
```

## Decision framework per il verdetto

### Go (tutte le condizioni vere):
1. ≥ 90% entry criteria soddisfatti
2. Nessun rischio rosso (score ≥ 15) senza mitigation chiara
3. Budget OK per fase successiva
4. Stakeholder primari (Regione, Coopfond) allineati

### Go Condizionato:
- 80-90% entry criteria + condizioni esplicite scritte
- Checkpoint anticipato (es. M+13 invece di aspettare G4 a M+12)

### Hold:
- < 80% entry criteria
- Issue critico aperto senza piano
- Re-review entro 60-90 giorni

### No-Go:
- Showstopper insuperabile in tempi/risorse
- Funding non disponibile
- Mercato/normativa cambiate radicalmente

### Defer (specifico Percorso 6B):
- Phase B HALE rimandata in attesa di:
  - Maturazione framework HAPS EASA
  - Risultati EuroHAPS/CIRA
  - Disponibilità call EDF/Horizon target

## Riferimenti specifici progetto HALE

Dal **Briefing**:
- Verdetto attuale Percorso 6A: **Go Condizionato** (raccomandazione esistente)
- Verdetto attuale Percorso 6B: **Hold / Go Condizionato Estremo** (showstopper noti)

Questi verdetti sono **provvisori** e vanno **formalizzati al Gate G3 (M+10/11)** con il framework di questa skill.

## Output che produce questa skill

- Gate package completo (markdown o docx)
- Entry/Exit criteria checklist per gate target
- Decision framework score
- Verbale di gate review (template)
- Action items list post-gate
- Communication plan post-decisione
