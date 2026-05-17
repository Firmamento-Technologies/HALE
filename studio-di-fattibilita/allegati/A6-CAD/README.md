# Allegato A.6 — Schemi/Disegni CAD del Concept

> Volume 2, Allegato A.6
> Documentazione CAD del concept HALE/VTOL

## Stato corrente M+3

I file CAD originali del concept HALE sono presenti nella cartella `cad/` alla root del repository (file binari proprietari Solidworks/CAT/STEP/IGES).

```
cad/
├── (file CAD binari del concept HALE high-AR T-tail)
└── (eventuali file aggiuntivi)
```

## Mappatura logica al Concept

Il concept tecnico HALE descritto in:
- `Progetto concettuale struttura HALE.md` (root del repository)
- Cap. 6 §6.1 (Concept Architettura)
- Cap. 6 §6.2 (Prestazioni)

prevede le seguenti unità geometriche modellate:

### Modelli CAD essenziali

| ID modello | Descrizione | Status M+3 |
|---|---|---|
| CAD-AERO-001 | Ala high-AR (≥ 25) con diedro positivo esterno | ✓ concept |
| CAD-AERO-002 | T-tail empennage | ✓ concept |
| CAD-FUSE-001 | Fusoliera low-drag pod | ✓ concept |
| CAD-FUSE-002 | Tail boom | ✓ concept |
| CAD-PROP-001 | Configurazione propulsiva traente | ✓ concept |
| CAD-ALT-001 | Three Lifting Surface alternative (canard + main + T-tail) | ✓ studio |
| CAD-STRUCT-001 | Layup composito longherone CFRP | ⏳ Phase A M+6+ |
| CAD-STRUCT-002 | Layup composito skin ibrido CFRP+lino | ⏳ Phase A M+6+ |
| CAD-PROP-002 | Subscale 1:3 prototype (24 m wingspan) per Phase B test | ⏳ Phase B M+24+ |
| CAD-GS-001 | Ground Station fissa Pentema (container + antenne) | ⏳ Y1 design |
| CAD-GS-002 | Ground Station mobile (veicolo + console) | ⏳ Y1 design |
| CAD-HANGAR-001 | Hangar protetto Pentema | ⏳ Y1 design |

## Roadmap CAD development

### Phase Pre-A (M+0-3) — completato
- Concept CAD high-level
- Three Lifting Surface alternative XFLR5 analysis

### Phase A (M+3-12)
- Detailed CAD ala + fusoliera (aerodynamic optimization)
- Layup composito iterativo (CFRP + lino)
- Mass distribution + CG analysis
- Wind tunnel scale model design (1:10 o 1:5)

### Phase B (M+12-48)
- CAD subscale prototype 1:3 (24 m wingspan, replica Polito HELIPLAT)
- Detailed structural CAD per analisi FEM (Nastran/Patran)
- Tooling CAD per manifattura compositi
- Ground equipment CAD detailed

### Phase C+ (out-of-scope Studio)
- Full-scale CAD finale
- Type Certification CAD package (TC Data Package)
- Manufacturing CAD detailed

## Standard di riferimento

I file CAD seguiranno gli standard:
- **ISO 10303 (STEP)** per interscambio neutrale CAD
- **ASME Y14.5:2018** per dimensioning + tolerancing (GD&T)
- **AS9100** per controllo qualità progettuale aerospace
- **ECSS-E-ST-32C** per structural design space-related

## Software CAD candidati

| Software | Pros | Cons | Uso target |
|---|---|---|---|
| **Solidworks** | Standard industriale, ben supportato | Costo licenze | Concept + detail design |
| **CATIA V5/V6** | Riferimento aerospace primary | Costo licenze alto | Detail design Phase B+ |
| **NX Siemens** | Buon supporto FEM integrato | Costo medio-alto | Detail design + tooling |
| **FreeCAD** | Open source | Limitazioni in composite | R&D + early concept |
| **OpenSCAD** | Programmatico, open | Limitato | Solo geometrie semplici |

**Raccomandazione M+3**: utilizzare **Solidworks** per Phase A; valutare **CATIA** per Phase B+ se entrato in partnership prime contractor.

## Analisi FEM + CFD planificate

| Software | Uso | Phase |
|---|---|---|
| ANSYS Fluent / CFX | CFD aerodinamica low-Re | A-B |
| OpenFOAM | CFD open-source alternativo | A |
| MSC Nastran / Patran | FEM strutturale + aeroelasticità | A-B |
| ANSYS Mechanical | FEM strutturale alternativo | A-B |
| XFLR5 / AVL | Low-fidelity preliminary | Pre-A-A |
| MASTAN | Educational structural | Pre-A |

## File deliverables per Vol. 2

Status M+3: il presente file è **placeholder**. I CAD effettivi sono nella cartella `cad/` alla root del repo (file binari non convertibili in markdown).

**Roadmap completamento Allegato A.6**:
- v1.5 M+6 — esportazione PNG/PDF di viste 2D dei modelli CAD principali
- v2.0 M+10 — CAD package completo per gate G3 (concept + Phase A iniziale)
- v3.0 M+24 — subscale CAD per Phase B 6B

## Falsifying observation

Se al gate G2 (M+6) non esistono CAD detailed degli elementi critici (longherone, ala completa, propulsione), il concept non è sufficientemente maturo per supportare la decisione architetturale del gate G3.

## Riferimenti

- `Progetto concettuale struttura HALE.md` (root)
- Cap. 6 §6.1 + §6.2
- Skill `trade-study-analysis` per TS-MATERIAL + TS-AERO
- Vol. 3 R.2 [T-65] CMH-17 + standard CAD aerospace
