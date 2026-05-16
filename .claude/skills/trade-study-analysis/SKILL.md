---
name: trade-study-analysis
description: Use when the user needs to compare architectural alternatives, technology options, or design choices for the HALE project. Trigger phrases - "trade study", "trade-off", "DOCFAP", "alternative progettuali", "confronto architetture", "decisione tra X e Y", "matrice decisionale", "Pugh matrix", "AHP", "decisione tra VTOL e MALE", "lino vs CFRP", "solare vs ibrido idrogeno". Builds a weighted decision matrix following NASA SE Handbook §6.8 + DOCFAP format (art. 41 D.Lgs. 36/2023) for HALE feasibility study.
---

# Trade Study Analysis — HALE Decision Matrix Builder

Skill per costruire **trade study formali** (= matrici decisionali ponderate) secondo NASA SE Handbook §6.8 e in formato compatibile con il **Documento di Fattibilità delle Alternative Progettuali (DOCFAP)** ex art. 41 D.Lgs. 36/2023.

## Quando usare

- Confronto tra ≥2 alternative architetturali credibili
- Scelta di sottosistema (es. propulsione, payload, materiali)
- Scelta di piattaforma commerciale per Percorso 6A
- Allegato giustificativo a una scelta tecnica nel Cap. 6.3 dello Studio
- DOCFAP per presentazione a Regione / Coopfond / Bando

## Metodi supportati

### 1. Pugh Matrix (concept selection)
Per fase concept (Phase Pre-A / A NASA SE).
- Una baseline + alternative
- Scoring +/0/- (better/same/worse) per criterio
- Output: best concept rispetto al baseline

### 2. Weighted Decision Matrix (multi-criteria)
Per fase di feasibility (Phase A).
- Criteri con peso (% somma = 100)
- Scoring 1-10 (o 1-5) per ogni alternativa
- Score totale ponderato = Σ(peso × score)
- Output: ranking + winner

### 3. Analytic Hierarchy Process (AHP, Saaty)
Per decisioni complesse multi-stakeholder.
- Matrice pairwise comparisons criteri (consistenza CR < 0.1)
- Matrice pairwise alternative su ciascun criterio
- Aggregazione gerarchica
- Output: priorità globale alternative

### 4. Pareto Front Analysis
Per trade-off multi-obiettivo (es. peso vs costo vs prestazione).
- Identificazione di soluzioni Pareto-ottime
- Output: frontiera di trade-off

## Template Trade Study Report

```markdown
# Trade Study: [Titolo decisione]

## TS-ID: TS-XXX-N
## Data: [YYYY-MM-DD]
## Owner: [Nome / agente responsabile]
## Gate associato: [es. M+6 Architettura]

## 1. Statement of the problem
- **Decisione da prendere:** [una frase]
- **Stakeholder primari:** [chi ne beneficia/subisce]
- **Vincoli iniziali:** [must-have / must-not-have]
- **Riferimento RTM:** [Req-IDs collegati]

## 2. Alternative analizzate
| ID | Descrizione | Sintesi |
|---|---|---|
| A1 | [es. VTOL ibrido JOUAV CW-30E] | TRL 8-9, payload 8 kg, 8h autonomia |
| A2 | [es. VTOL Quantum Trinity F90+] | TRL 8-9, payload 1 kg, 90 min |
| A3 | [es. MALE Tekever AR3] | TRL 8, payload 2.5 kg, 16h |
| A0 | [Status quo / no action] | Riferimento "do-nothing" |

## 3. Criteri di valutazione e pesi
| ID | Criterio | Peso (%) | Rationale del peso |
|---|---|---|---|
| C1 | Autonomia missione | 20 | [perché 20%] |
| C2 | Payload compatibility | 15 | |
| C3 | Certificabilità SAIL EASA | 15 | |
| C4 | Lead time | 10 | |
| C5 | TCO 5 anni | 15 | |
| C6 | Supporto tecnico IT/EU | 10 | |
| C7 | Geopolitica/dual-use risk | 10 | |
| C8 | Track record similar missions | 5 | |
| **TOT** | | **100** | |

## 4. Scoring matrix (1-10, 10=ottimo)
| Criterio (peso) | A1 | A2 | A3 |
|---|---|---|---|
| C1 (20%) | 8 | 4 | 9 |
| C2 (15%) | 9 | 4 | 6 |
| C3 (15%) | 7 | 9 | 7 |
| C4 (10%) | 6 | 8 | 6 |
| C5 (15%) | 7 | 8 | 5 |
| C6 (10%) | 7 | 9 | 6 |
| C7 (10%) | 5 | 9 | 8 |
| C8 (5%) | 8 | 5 | 7 |
| **Σ ponderato** | **7.30** | **6.80** | **6.80** |
| **Rank** | **1°** | 2°-3° | 2°-3° |

## 5. Sensitivity analysis
- Variazione peso C1 ±10pp: ranking [stabile / si inverte]
- Variazione score A1 su C7 ±2 punti: ranking [stabile / si inverte]
- → Robustezza decisione: [alta / media / bassa]

## 6. Considerazioni qualitative
- Stoppers eventuali ([es. A3 non disponibile lead time])
- Rischi residui (vedi Risk Register)
- Possibilità di "approccio ibrido" (mix di alternative)

## 7. Raccomandazione
**Raccomandazione: [alternativa scelta]**
- Razionale: [3-5 punti]
- Condizioni necessarie: [validazione richiesta]
- Open Questions: [OQ residue]

## 8. Approvazione
- [ ] Owner tecnico
- [ ] Stakeholder primario
- [ ] Gate review board

## 9. Riferimenti
- NASA SE Handbook §6.8
- D.Lgs. 36/2023 art. 41, Allegato I.7 (DOCFAP)
- ISO/IEC/IEEE 15288:2015 (decision analysis)
```

## Esempi di trade study tipici per il progetto HALE

| Trade study | Alternative | Criteri principali | Agente da consultare |
|---|---|---|---|
| TS-PLATFORM-6A | JOUAV CW-30E vs Quantum Trinity vs FlyingBasket FB3 vs custom | Autonomia, payload, lead time, TCO, IT/EU | vtol-uas-specialist |
| TS-AIRFOIL | Wing high-AR std vs box-wing vs three lifting-surface | L/D, peso, stabilità, manufacturability | aerodynamics-structures-engineer |
| TS-MATERIAL | CFRP puro vs lino-CFRP ibrido vs full bio-composite | Massa, costo, sostenibilità, durabilità | aerodynamics-structures-engineer |
| TS-PROP | Solar+LiS vs Solar+SS Li vs Solar+SOFC+LH2 vs Seasonal solar | Energy balance, TRL, costo, massa | propulsion-energy-engineer |
| TS-AVI | Pixhawk modified vs MicroPilot vs custom DAL-B | Affidabilità, costo, certificabilità | avionics-gnc-engineer |
| TS-PAYLOAD-EO | RGB+IR vs RGB+LiDAR vs full multispectral | GSD, massa, costo, use cases | earth-observation-expert |
| TS-PAYLOAD-NTN | LTE eNodeB tactical vs 5G NR-NTN regenerative | Throughput, peso, spettro | telecom-ntn-payload-expert |
| TS-SAIL | SAIL II vs III vs IV | Operations limit, regulatory cost, complexity | aviation-regulatory-counsel |
| TS-FINANCE | Mix grant 60% + equity 40% vs grant 40% + debt 30% + equity 30% | Cost of capital, dilution, risk | financial-cfo-analyst |
| TS-BIZMODEL | DaaS pure vs canone + DaaS vs outcome-based | ARPU, predictability, CAC | business-model-strategist |

## Workflow uso skill

1. Definire il **problema** (statement of the problem)
2. Identificare **alternative credibili** (almeno 3, incluso A0 status quo se rilevante)
3. Definire **criteri** con stakeholder (workshop o asincrono)
4. Assegnare **pesi** (Σ = 100%) con razionale
5. **Scoring**: ogni alternativa su ogni criterio (1-10), con assunzioni dichiarate
6. Calcolare **score ponderato totale** e **ranking**
7. **Sensitivity analysis**: variazione pesi e score per testare robustezza
8. **Considerazioni qualitative**: stopper, rischi, approccio ibrido
9. **Raccomandazione formale** con condizioni
10. **Pubblicare TS-ID** nel registro centralizzato

## Output

- Trade Study Report (markdown o docx)
- Tabella decisionale Excel (con sensitivity)
- Riferimento da inserire in Cap. 6.3 dello Studio
- Allegato DOCFAP-ready
