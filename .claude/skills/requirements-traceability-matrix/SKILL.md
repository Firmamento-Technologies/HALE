---
name: requirements-traceability-matrix
description: Use when the user needs to write, update or verify the Requirements Traceability Matrix (RTM) of the HALE Feasibility Study. Trigger phrases - "RTM", "matrice tracciabilità", "requisiti", "stakeholder needs", "system requirements", "tracciamento requisito", "verifica copertura requisito", "scrivi requisito", "Req-ID", "needs to requirements". Builds and maintains NASA SE compliant requirements traceability from Stakeholder Needs → System Requirements → Subsystem Requirements → Verification.
---

# Requirements Traceability Matrix (RTM) — HALE

Skill per costruire/aggiornare la **RTM** dello Studio di Fattibilità HALE, secondo **NASA SE Handbook §4** (Requirements Definition) e **INCOSE SE Handbook 5th ed.**.

## Quando usare

- Stesura iniziale del Cap. 3 dello Studio
- Aggiornamento dopo decisione di trade study che modifica i requisiti
- Verifica della **completezza** della tracciabilità (ogni decisione → requisito → need)
- Verifica della **copertura** di V&V (ogni requisito → metodo verifica)
- Allegato A.1 del Volume 2

## Tassonomia dei requisiti (NASA SE)

| Livello | Esempio | Owner |
|---|---|---|
| **Stakeholder Needs (StNeeds)** | "I cooperative agricoli vogliono mappe NDVI mensili in stagione" | Stakeholder primario |
| **System Requirements (SyR)** | "Il sistema deve produrre ortomosaici multispettrali con GSD ≤ 0.5 m su aree ≥ 100 ha" | System Engineer |
| **Subsystem Requirements (SsR)** | "Il payload EO deve includere sensore multispettrale ≥ 4 bande con risoluzione ≥ 8 cm @ 1500 m AGL" | Subsystem Engineer |
| **Interface Requirements (IR)** | "L'interfaccia payload-bus deve supportare ≥ 1 Gbps Ethernet + 28 VDC ≤ 80 W" | Integration Engineer |
| **Verification Requirements (VR)** | "SyR-001 verificato per Test in volo su Pentema + Analysis simulazione" | V&V Engineer |

## Schema RTM (Excel/Markdown table)

| Req-ID | Description | Rationale | Source | Type | Parent | Owner | Priority | Verification Method | V&V Status | Phase | Trade Studies | Risks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| StNeed-001 | I cooperative vogliono mappe NDVI mensili | Supporto fertirrigazione | Workshop coop 2026-03-12 | StNeed | - | snai-funding-expert | M | - | - | Pre-A | - | RSK-MKT-003 |
| SyR-001 | Sistema produce ortomosaico multispettrale GSD ≤0.5m | Soddisfare StNeed-001 + risoluzione cartografica | StNeed-001 | SyR | StNeed-001 | aerospace-SE | H | A+T | Open | A | TS-PAYLOAD-EO | RSK-TEC-012 |
| SsR-PAY-001 | Payload EO include sensore 4-band 8cm@1.5km AGL | Compliance SyR-001 | SyR-001 | SsR | SyR-001 | EO expert | H | A+I+T | Open | A | TS-PAYLOAD-EO | RSK-TEC-012 |
| IR-PAY-001 | Payload-bus iface 1Gbps Eth + 28 VDC ≤80W | Compatibilità payload modulare | SsR-PAY-001, ICD prelim | IR | SsR-PAY-001 | integration | H | I+T | Open | A | TS-AVI | RSK-INT-005 |

## Convenzioni Req-ID

```
StNeed-NNN          # Stakeholder Need
SyR-NNN             # System Requirement
SsR-XXX-NNN         # Subsystem (XXX = AERO, PROP, AVI, PAY, GS, COMMS, etc.)
IR-XXX-NNN          # Interface
VR-NNN              # Verification

Esempi:
- StNeed-012        # 12° need raccolto da stakeholder
- SyR-007           # 7° system requirement
- SsR-PROP-003      # 3° requisito del sottosistema propulsione
- IR-PAY-005        # 5° requisito interfaccia payload
```

## Categorie tipiche dei requisiti

### StNeeds (Stakeholder Needs)
- Cooperative pilota (10) — fabbisogni operativi
- Regione Liguria — obiettivi di programma
- Protezione Civile — esigenze di emergenza
- ENAC — vincoli regolatori
- AGCOM — vincoli spettro
- Comunità Pentema — accettabilità sociale

### SyR (System Requirements)
- **Funzionali**: cosa deve fare il sistema (missioni, output)
- **Performance**: GSD, autonomia, copertura, latenza, throughput
- **Operativi**: condizioni ambientali, profili di missione
- **Affidabilità/Disponibilità**: MTBF, MTTR, availability%
- **Sicurezza**: failure rate, SAIL EASA, OSO compliance
- **Sostenibilità**: emissioni, riciclo, riparabilità
- **Costo**: target unit cost, TCO

### SsR (Subsystem Requirements)
- Aerodinamica & strutture
- Propulsione & energia
- Avionica & GNC
- Payload (EO, telecom, custom)
- Ground segment
- Sistemi di comunicazione (link C2, link dati)

### Verification methods (NASA SE §6.5)
| Codice | Metodo | Quando usarlo |
|---|---|---|
| **I** | Inspection | Verifica visiva o documentale (specs, etichette) |
| **A** | Analysis | Calcoli, simulazioni, modeling |
| **D** | Demonstration | Esercizio operativo del sistema |
| **T** | Test | Misure quantitative su prototype/articolo di volo |

## Workflow tipico

1. **Raccolta StNeeds** (workshop, interviste, analisi documentale)
   - Output: lista StNeed-NNN
2. **Derivazione SyR** dai StNeeds (NASA SE §4.2.2)
   - Output: lista SyR-NNN, con `Parent = StNeed-NNN`
3. **Decomposizione SsR** dai SyR (allocazione)
   - Output: lista SsR-XXX-NNN, con `Parent = SyR-NNN`
4. **Definizione IR** alle interfacce
   - Output: lista IR-XXX-NNN
5. **Pianificazione V&V** per ogni requisito
   - Output: VR-NNN con metodo (I/A/D/T) e Phase target
6. **Verifica di copertura**:
   - Ogni StNeed ha ≥1 SyR figlio? (no orphan needs)
   - Ogni SyR ha ≥1 SsR figlio? (no unallocated SyR)
   - Ogni SyR ha ≥1 metodo V&V? (no untestable)
7. **Aggancio a Risk Register**: ogni requisito a rischio referenzia un RSK-ID
8. **Aggancio a Trade Studies**: ogni requisito derivato da decisione referenzia TS-ID

## Esempio: stack RTM per il caso d'uso "antincendio boschivo Pentema"

```
StNeed-008  La Protezione Civile Liguria deve ricevere alert hotspot termico in <5 min
   ↓
SyR-014    Il sistema deve fornire alert hotspot ≥40°C con FAR<5% e latency <5 min
   ↓
SsR-PAY-007 Payload IR LWIR risoluzione ≥5m GSD, sensibilità NEdT <50mK
SsR-COMM-003 Downlink min 50 kbps per alert + thumbnail in <30s
SsR-GS-002  Ground segment ricezione alert + push a interfaccia PC in <60s
   ↓
VR-014.1   SyR-014 verificato per Demonstration su scenario emergenza in Pentema
VR-014.2   SyR-014 verificato per Analysis su tasso FAR < 5%
```

## Stati del requisito (V&V status)

- **Open** — non ancora verificato
- **Planned** — pianificato (data, metodo)
- **In progress** — verifica in corso
- **Verified** — verificato con successo
- **Failed** — verifica fallita (richiede iterazione/waiver)
- **Waived** — non applicabile, motivato

## Aggiornamento RTM

La RTM è un **documento vivente**:
- Aggiornata dopo ogni trade study che cambia decisioni
- Aggiornata dopo ogni risk re-assessment
- Aggiornata dopo ogni gate review
- Versionata (es. RTM v0.5 → v0.6 → v1.0 al Feasibility Gate M+10)

## Output

- RTM Excel completa (per Allegato A.1 dello Studio)
- RTM markdown table (per Cap. 3.5)
- Coverage report (% StNeeds con SyR figlio, % SyR con V&V planned, etc.)
- Gap list (orphan needs, unallocated, untestable)
