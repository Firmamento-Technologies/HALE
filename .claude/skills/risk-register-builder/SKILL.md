---
name: risk-register-builder
description: Use when the user needs to identify, score, mitigate, or track project risks for the HALE Feasibility Study. Trigger phrases - "risk register", "registro rischi", "FMECA", "FTA", "showstopper", "Hold/Go", "rischio tecnico", "rischio regolatorio", "rischio finanziario", "P×I matrix", "rischio residuo", "owner del rischio". Builds and maintains the Risk Register following NASA NPR 8000.4 (Continuous Risk Management) + FMECA + ARP4761 framework.
---

# Risk Register Builder — HALE

Skill per costruire e mantenere il **Risk Register** del progetto HALE secondo:
- **NASA NPR 8000.4** (Continuous Risk Management)
- **FMECA** (Failure Mode Effects and Criticality Analysis) — MIL-STD-1629A / IEC 60812
- **ARP4761** (Safety Assessment Process for Civil Airborne Systems)
- **ISO 31000** (Risk Management — Principles and Guidelines)

## Quando usare

- Stesura iniziale del Risk Register (Cap. 6.4 + Allegato A.2)
- Aggiornamento dopo ogni trade study, gate review, evento esterno
- Identificazione **showstopper** per gate decisionali
- Allegato a presentazione bandi (Coopfond, FESR, EDF)
- Safety Case per autorizzazioni ENAC

## Tassonomia rischi del progetto HALE

| Categoria | Codice | Esempi |
|---|---|---|
| **Tecnico** | RSK-TEC-XXX | Energy balance inverno HALE, flutter ala high-AR, integrazione payload |
| **Regolatorio** | RSK-REG-XXX | Framework HAPS mancante, SORA SAIL, U-Space transizione, spettro AGCOM |
| **Finanziario** | RSK-FIN-XXX | Mancato grant Coopfond, sovracosti CapEx, ritardo finanziamenti |
| **Mercato** | RSK-MKT-XXX | Pricing pressure, competizione Sentinel/satellite, slow PA adoption |
| **Operativo** | RSK-OPS-XXX | Maltempo, indisponibilità piattaforma, sicurezza UAS |
| **Privacy/Legale** | RSK-PRV-XXX | DPIA fail, contenzioso privacy, GDPR breach |
| **Supply chain** | RSK-SUP-XXX | Lead time piattaforma, embargo CN, ritardo componenti |
| **Risorse umane** | RSK-HR-XXX | Mancanza piloti UAS, turnover, formazione |
| **Reputational** | RSK-REP-XXX | Incidente UAS, contestazioni comunità Pentema, controversie cooperative |
| **Cybersecurity** | RSK-SEC-XXX | Hijacking C2 link, data breach, ransomware ground segment |

## P×I Matrix (Probability × Impact)

### Scala Probabilità (P)
| Livello | Descrizione | Probabilità qualitativa | Range quantitativo |
|---|---|---|---|
| 1 | Very Low | Improbabile | < 5% |
| 2 | Low | Possibile ma raro | 5-20% |
| 3 | Medium | Possibile | 20-50% |
| 4 | High | Probabile | 50-80% |
| 5 | Very High | Quasi certo | > 80% |

### Scala Impatto (I) — multidimensionale
| Livello | Tecnico | Schedule | Costo | Safety | Reputational |
|---|---|---|---|---|---|
| 1 — Negligible | Aggiornamento minimo doc | < 1 settimana | < €5k | Nessun rischio safety | Nessuno |
| 2 — Minor | Modifica subsystem | 1-4 settimane | €5-50k | Incidente minore, no ferite | Locale |
| 3 — Moderate | Re-design subsystem | 1-3 mesi | €50-200k | Incidente, ferite leggere | Regionale |
| 4 — Major | Re-design system | 3-12 mesi | €200k-1M | Ferite gravi | Nazionale |
| 5 — Severe | Showstopper o catastrofe | > 12 mesi | > €1M | Decesso, danni gravi a terzi | Internazionale |

### Risk Score = P × I
- **Verde (1-6)**: rischio accettabile, monitor
- **Giallo (8-12)**: mitigation richiesta
- **Rosso (15-25)**: **showstopper**, richiede risposta immediata (Hold gate)

## Schema Risk Register

| ID | Categoria | Descrizione | Trigger | P | I | Score | Status | Owner | Risposta | Mitigation actions | Residual P | Residual I | Residual Score | Status update | Last review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Risposte al rischio (NASA + ISO 31000)

| Risposta | Quando usarla | Esempio |
|---|---|---|
| **Avoid** | Eliminare la causa | Cambiare architettura per rimuovere singolo punto di guasto |
| **Mitigate** | Ridurre P e/o I | Migliorare design, ridondanza, test aggiuntivi |
| **Transfer** | Spostare il rischio | Assicurazione, contratto vendor, partnership |
| **Accept** | Tollerare con monitoring | Rischio basso, costo mitigation > exposure |

## Showstopper del progetto HALE (dal Briefing — da approfondire e formalizzare)

### Percorso 6B — HALE stratosferico

| RSK-ID | Showstopper | P | I | Score | Owner | Risposta |
|---|---|---|---|---|---|---|
| RSK-TEC-001 | Energy balance invernale 20 km lat. 44°N (solstizio dic.) | 4 | 5 | **20** 🔴 | propulsion-energy-engineer | Mitigate: design margin, fallback seasonal |
| RSK-TEC-002 | Stabilità aeroelastica ala high-AR | 3 | 5 | 15 🔴 | aero-structures-engineer | Mitigate: aeroelastic analysis, GVT, flight test subscale |
| RSK-REG-001 | Mancanza framework HAPS EASA/ENAC | 5 | 4 | **20** 🔴 | aviation-regulatory | Mitigate: engagement EASA/ENAC, Special Condition path |
| RSK-FIN-001 | Mancanza finanziamento R&D €5.5-11M | 4 | 5 | **20** 🔴 | financial-cfo | Mitigate: mix EDF+Horizon+equity, fasi graduali |
| RSK-TEC-003 | Type Certification timeline >5 anni | 4 | 4 | 16 🔴 | aviation-regulatory | Accept + Mitigate: parallelizzare con operazioni 6A |

### Percorso 6A — VTOL pilota Pentema

| RSK-ID | Rischio | P | I | Score | Owner | Risposta |
|---|---|---|---|---|---|---|
| RSK-OPS-001 | Operazioni invernali Appennino Ligure (neve, ghiaccio) | 3 | 3 | 9 🟡 | vtol-uas-specialist | Mitigate: training, periodi operativi, anti-icing |
| RSK-REG-002 | Autorizzazione SORA BVLOS in valle stretta | 3 | 3 | 9 🟡 | aviation-regulatory | Mitigate: SORA early dialogue, M1/M2 mitigation |
| RSK-SUP-001 | Lead time JOUAV (vendor CN) + tensioni geopolitiche | 3 | 3 | 9 🟡 | vtol-uas-specialist | Mitigate: alternative EU (Quantum, Wingtra), Plan B |
| RSK-MKT-001 | Adozione lenta PA (cicli appalti pubblici) | 4 | 3 | 12 🟡 | snai-funding | Mitigate: anchor customer Regione Liguria, contratti pluriennali |
| RSK-PRV-001 | DPIA blocca casi d'uso sorveglianza | 2 | 3 | 6 🟢 | data-privacy | Monitor + Mitigate: privacy by design, edge anonymization |
| RSK-FIN-002 | Mancato grant Coopfond Cooding (€50k) | 2 | 2 | 4 🟢 | financial-cfo + snai-funding | Accept + alternative funding |
| RSK-HR-001 | Difficoltà reclutamento pilota UAS specialist BVLOS | 3 | 3 | 9 🟡 | business-model | Mitigate: training in-house, partnership con scuole UAS |
| RSK-OPS-002 | Incidente UAS BVLOS sul territorio | 2 | 5 | 10 🟡 | aviation-regulatory + ops | Mitigate: SORA M2, GRC mitigation, assicurazione |
| RSK-SEC-001 | Cyber attack ground segment (data breach Pentema) | 2 | 4 | 8 🟡 | cybersec (futuro) | Mitigate: zero-trust, segregation, NIS2 readiness |

## FMECA — Analisi di guasto per sottosistema

Per ogni sottosistema critico:

```markdown
### Sottosistema: [es. Payload EO]

| Item | Failure Mode | Cause | Local Effect | System Effect | Severity (1-5) | Frequency (1-5) | Detection (1-5) | RPN = S×F×D | Mitigation |
|---|---|---|---|---|---|---|---|---|---|
| Camera RGB | No image | Sensor failure | Loss of mission EO | Loss of EO product | 3 | 2 | 2 | 12 | Ridondanza 2 camere, healthcheck onboard |
| Gimbal | Stuck | Motor failure | Image off-target | Reduced area cov. | 3 | 3 | 2 | 18 | Service interval, redundant motor |
```

## FTA — Fault Tree Analysis

Per eventi top-level critici (es. "Loss of vehicle in BVLOS"):
- Costruzione albero AND/OR
- Identificazione cut sets minimi
- Calcolo probabilità top event
- Identificazione single point of failure (SPOF)

## Workflow tipico

1. **Risk identification workshop** con multidisciplinary team
2. **Categorizzazione** secondo tassonomia
3. **Scoring** P e I per ogni rischio
4. **Selezione risposta** (avoid/mitigate/transfer/accept)
5. **Definizione mitigation actions** con owner e deadline
6. **Calcolo residual risk** (post-mitigation)
7. **Gate review** dei rischi rossi (showstopper) per decisione Go/No-Go
8. **Continuous monitoring** + re-assessment trimestrale

## Trigger di re-assessment

- Cambio di scope o requisiti
- Nuovo trade study completato
- Gate review imminente
- Evento esterno (cambio regolatorio, market shock)
- Incidente o near-miss

## Output

- Risk Register Excel/Markdown (Allegato A.2)
- Sintesi rischi top-10 (Cap. 6.4)
- Showstopper Register dedicato (per gate review)
- FMECA per sottosistema critico
- FTA per top events (incl. Safety Case input)
