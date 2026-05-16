# `.claude/` — Esperti e Skill per il Progetto HALE

Questa cartella contiene **agenti esperti** (subagents) e **skill** (procedure operative) specifici per lo Studio di Fattibilità della piattaforma aerea HALE/VTOL di Firmamento Technologies.

## Come è organizzato

```
.claude/
├── README.md                  ← Questo file
├── agents/                    ← Esperti di dominio (invocabili via Task tool)
└── skills/                    ← Procedure/workflow (invocabili via Skill tool)
```

## Agenti esperti (`agents/`)

Subagent specializzati. Da invocare con il Task tool quando serve un parere/output di dominio.

### Ingegneria aerospaziale & aeronautica

| Agente | Quando invocarlo |
|---|---|
| `aerospace-systems-engineer` | Architettura di sistema, RTM, V-model, trade study, gate review, NASA SE compliance |
| `aerodynamics-structures-engineer` | Aerodinamica (alto allungamento, polare, polare invernale), aeroelasticità, strutture composite + fibre naturali (lino) |
| `propulsion-energy-engineer` | Bilancio energetico solare/batterie, propulsione elettrica, caso critico inverno stratosferico |
| `avionics-gnc-engineer` | Autopilota, GNC, sense-and-avoid, BVLOS/BLOS, integrità link C2 |
| `vtol-uas-specialist` | Piattaforme commerciali VTOL/MALE TRL 8-9 (JOUAV CW-30E, Quantum Trinity, etc.) per il Percorso 6A |

### Payload & comunicazione

| Agente | Quando invocarlo |
|---|---|
| `telecom-ntn-payload-expert` | NTN 4G/5G da HAPS, link budget, allocazione spettro AGCOM, copertura cella |
| `earth-observation-expert` | Payload EO/SAR/multispettrale/termico, GSD, casi d'uso PA/Protezione Civile |

### Regolatorio & legale

| Agente | Quando invocarlo |
|---|---|
| `aviation-regulatory-counsel` | EASA UAS (Open/Specific/Certified), ENAC, U-Space, framework HAPS, SORA, BVLOS |
| `data-privacy-counsel` | GDPR per sorveglianza aerea, dati territoriali, condivisione con PA |

### Business, mercato, finanza

| Agente | Quando invocarlo |
|---|---|
| `aerospace-market-analyst` | TAM/SAM/SOM HAPS/UAV, competitor (Zephyr, Aalto, Aurora, Skydweller), pricing benchmark |
| `business-model-strategist` | BMC, value proposition, modello servizio DaaS/IaaS per cooperative e PA |
| `financial-cfo-analyst` | CapEx/OpEx per fase, NPV/IRR, sensitivity, break-even, struttura finanziamenti |

### Territorio, governance, funding

| Agente | Quando invocarlo |
|---|---|
| `snai-funding-territorial-expert` | SNAI/PSNAI, aree interne Liguria, Pentema, bandi Cooding/PNRR/Horizon Europe/EDF, governance Legacoop |

## Skill (`skills/`)

Procedure ripetibili invocabili via Skill tool. Tutte calibrate sul progetto HALE.

| Skill | Cosa fa |
|---|---|
| `feasibility-study-framework` | Genera scheletro di un capitolo dello studio secondo il framework NASA SE (Stakeholder → Requisiti → Architettura → Trade → Verifica → Gate) |
| `trade-study-analysis` | Costruisce una matrice decisionale ponderata per confrontare alternative architetturali (es. VTOL ibrido vs. multirotore vs. MALE) |
| `requirements-traceability-matrix` | Costruisce/aggiorna la RTM: Need → StRq → SyRq → Verifica → Status |
| `risk-register-builder` | Compila risk register con FMEA, P×I matrix, owner, trigger, mitigazione, residuo |
| `link-budget-calculator` | Calcola link budget per payload telecom HAPS (uplink/downlink, fade margin, EIRP, G/T) |
| `gate-review-checklist` | Checklist Go/No-Go per i gate decisionali (Gate M+3, M+6, M+10, ecc.) |

## Skill ufficiali Anthropic (installazione separata)

Le skill ufficiali per generare i deliverable finali (Word, PowerPoint, Excel, PDF) non sono incluse qui per ragioni di licenza. Installa il marketplace Anthropic:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropics
```

Skill incluse nel pacchetto `document-skills`:
- `docx` — generazione documento finale dello Studio di Fattibilità
- `pdf` — estrazione contenuto dai PDF SNAI e generazione PDF di output
- `pptx` — generazione slide deck di presentazione
- `xlsx` — costruzione modello finanziario, RTM, risk register in Excel

## Pattern d'uso tipici

**Generare il capitolo 5 — Analisi di Mercato:**
1. Invoca `aerospace-market-analyst` per analisi competitor HAPS
2. Invoca `snai-funding-territorial-expert` per stima domanda territoriale
3. Invoca skill `feasibility-study-framework` per impaginare il capitolo
4. Genera l'output finale `.docx` con la skill `docx`

**Decidere l'architettura del Percorso 6A:**
1. Invoca skill `trade-study-analysis` per impostare la matrice
2. Invoca `vtol-uas-specialist` per dati su JOUAV, Quantum, ecc.
3. Invoca `aerospace-systems-engineer` per validare i criteri NASA SE
4. Invoca `aviation-regulatory-counsel` per il vincolo regolatorio
5. Pubblica la decisione nel risk register e nella RTM

**Sessione di Gate Review M+10:**
1. Invoca skill `gate-review-checklist` per la checklist
2. Aggiorna risk register (`risk-register-builder`) e RTM (`requirements-traceability-matrix`)
3. Convoca i pareri di `aerospace-systems-engineer`, `financial-cfo-analyst`, `aviation-regulatory-counsel` per il verdetto Go/No-Go
