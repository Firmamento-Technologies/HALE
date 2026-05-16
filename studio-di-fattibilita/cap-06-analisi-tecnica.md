# Capitolo 6 — Analisi Tecnica di Fattibilità

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 1, Capitolo 6
>
> **Versione:** bozza M+3
> **Conformità:** D.Lgs. 36/2023 art. 41 (sezione "Analisi tecnica di fattibilità") + NASA SE Handbook Rev 2 §6 (Technical Solution Definition)
> **Disciplina epistemica:** applicate Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** `red-team-skeptic` + `aerospace-systems-engineer` — vedi §6.13

---

## 6.0 Sintesi del capitolo

Il presente capitolo è il **cuore tecnico** dello Studio di Fattibilità, e copre architettura, prestazioni, analisi di rischio ingegneristico e infrastrutture per i due percorsi del progetto. Per ciascuno dei due percorsi, il capitolo:

1. Definisce l'**architettura di sistema** preliminare
2. Calcola le **prestazioni** stimate (autonomia, payload, energia, link budget)
3. Conduce le **trade study** chiave (DOCFAP ex art. 41), con scelte motivate
4. Esegue l'**analisi rischio ingegneristico** (FMECA + FTA preliminare)
5. Dimensiona le **infrastrutture** (ground segment, hangar, base operativa)

### 6.0.1 Verdetto tecnico in sintesi

| Percorso | Verdetto tecnico | Showstopper noti |
|---|---|---|
| **6A VTOL pilota** | ✅ **GO** — tecnicamente fattibile con piattaforma commerciale TRL 8-9 + integrazione payload modulare. Rischi gestibili. | Nessuno bloccante; rischi operativi orografia/inverno → mitigazione operativa |
| **6B HALE stratosferico** | ⚠️ **HOLD / Go Condizionato R&D** — fattibilità tecnica non dimostrata. 2 showstopper critici aperti. | **RSK-TEC-001 (energy balance inverno) + RSK-TEC-002 (aeroelasticità ala high-AR)** |

### 6.0.2 Trade study chiave conclusi al M+3 (preliminari)

| TS-ID | Decisione | Raccomandazione preliminare | Confidence |
|---|---|---|---|
| **TS-PLATFORM-6A** | Scelta piattaforma VTOL | **JOUAV CW-30E** (alternative: Quantum F90+, FlyingBasket FB3) | medium |
| **TS-MATERIAL** | Materiali strutturali HALE | **CFRP primario + lino secondario** (no lino in longherone primario) | high |
| **TS-PROP-6B** | Architettura energetica HALE | **Solare + LiS pack** (target 2028); fallback "seasonal-only" inverno | medium-low |
| **TS-AVI-6A** | Autopilota Percorso 6A | **JOUAV FCS proprietario** (integrato in CW-30E) | high |
| **TS-PAYLOAD-EO** | Payload EO modulare 6A | **RGB + IR LWIR** baseline; LiDAR opzionale; multispettrale Y2 | medium |
| **TS-COMMS** | Link C2 + downlink dati | RF primary (2.4 GHz) + **SATCOM Iridium L-band** secondary per shadow zones Pentema | medium |

I trade study sono **preliminari**, completi in Vol. 2 Allegato A.3. Validazione finale richiesta al gate M+10.

---

## 6.0bis Boundary conditions del progetto

In coerenza con Cap. 5.0bis, Cap. 3.0bis, Cap. 7.0bis:

- **B1**: modello service-only + cooperative Legacoop. Le scelte architetturali devono **supportare l'erogazione di servizi**, non la vendita di asset.
- **B2**: visione strategica "EU sovereign stratospheric layer". Le scelte tecniche del Percorso 6A devono produrre **asset riusabili** per il Percorso 6B (ground segment, data governance, software pipeline).

---

## 6.1 Concept Architetturale dei Due Percorsi

### 6.1.1 Percorso 6A — Architettura VTOL ibrido commerciale

**Architettura selezionata (preliminare, da validare al gate M+6):**

```
┌────────────────────────────────────────────────────────────────┐
│                 PERCORSO 6A — Sistema VTOL pilota              │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────┐    RF 2.4 GHz / SATCOM L-band    ┌─────────┐ │
│  │   VTOL UAV   │ ◄═══════════ C2 + Telemetria ════│ Ground  │ │
│  │              │              dati EO downlink    │ Station │ │
│  │  • JOUAV     │ ◄═══════════════════════════════►│ fissa + │ │
│  │    CW-30E    │                                  │ mobile  │ │
│  │              │                                  │         │ │
│  │  ┌────────┐  │                                  │  ↓      │ │
│  │  │Payload │  │                                  │ Cloud   │ │
│  │  │Module  │  │                                  │ IT/EU   │ │
│  │  │EO+IR+  │  │                                  │ Aruba/  │ │
│  │  │telecom │  │                                  │ OVH     │ │
│  │  └────────┘  │                                  │  ↓      │ │
│  └──────────────┘                                  │ End User│ │
│                                                    │ PA/Coop │ │
│                                                    └─────────┘ │
└────────────────────────────────────────────────────────────────┘
```

**Caratteristiche chiave Percorso 6A:**

| Sottosistema | Soluzione | TRL | Status |
|---|---|---|---|
| **Piattaforma volante** | VTOL ibrido fixed-wing, MTOW ~38 kg, payload max 8 kg, autonomia 6-10h | 8-9 (commerciale) | TS-PLATFORM-6A in corso |
| **Propulsione** | Hybrid gasoline/heavy oil + battery; transizione VTOL→cruise | 9 (commerciale) | OK |
| **Autopilota / FCS** | JOUAV proprietario integrato | 9 | OK |
| **C2 link** | RF 2.4 GHz primario, range 50 km LoS + SATCOM Iridium L-band secondario | 9 | TS-COMMS in corso |
| **Payload EO RGB** | Phase One iXM 100 (100 MP, GSD 8 cm @ 500m AGL) | 9 | OK |
| **Payload IR** | FLIR Vue Pro R o WIRIS Pro (LWIR, NEdT ≤50 mK) | 9 | OK |
| **Payload telecom** | LTE eNodeB tattico (Athonet/Druid/IP.access) | 8 (limited deployment) | TS-PAYLOAD in corso |
| **Ground Station** | 1 GS fissa Pentema (container) + 1 GS mobile (veicolo) | 9 | OK |
| **Cloud / data** | Aruba/OVH IT/EU, GDPR + NIS2 compliant | 9 | OK |

### 6.1.2 Percorso 6B — Architettura HALE solare stratosferico

**Architettura selezionata (preliminare, R&D Phase B, gate M+10-24):**

```
┌────────────────────────────────────────────────────────────────┐
│            PERCORSO 6B — Sistema HALE stratosferico            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│                  ┌──────────────┐                              │
│                  │  HALE solare │  Quota: 18-21 km (FL590-690) │
│                  │  alta high-AR│                              │
│                  │              │                              │
│                  │  • Wing 25-30m│                              │
│                  │  • MTOW 80-150kg                            │
│                  │  • Solar cells multi-junction               │
│                  │  • Batterie LiS pack 350 Wh/kg              │
│                  │  • Payload 5-10 kg                          │
│                  │  • Endurance 30+ giorni (estate)            │
│                  │                                             │
│                  │  ┌───────────┐                              │
│                  │  │ Payload   │                              │
│                  │  │ EO/NTN/IR │                              │
│                  │  └───────────┘                              │
│                  └──────┬───────┘                              │
│                         │                                      │
│             Feeder link Ka 31 GHz                              │
│                         │                                      │
│                         ▼                                      │
│                  ┌──────────────┐                              │
│                  │ HAPS Gateway │                              │
│                  │  ground      │                              │
│                  └──────┬───────┘                              │
│                         │                                      │
│                         ▼                                      │
│            Service link S-band 2.0-2.2 GHz (NTN 3GPP Rel-17/18)│
│                         │                                      │
│                         ▼                                      │
│                  End User 5G NTN-capable                       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Caratteristiche chiave Percorso 6B:**

| Sottosistema | Soluzione preliminare | TRL attuale (2026) | TRL target Phase B (Y4) |
|---|---|---|---|
| **Velivolo HALE** | Ala high-AR (AR≥25), MTOW 80-150 kg, b 25-30 m | 3-4 (concept) | 5-6 (subscale flight test) |
| **Propulsione** | Elettrica solare + LiS / SS Li pack 350 Wh/kg | 4 (subsystem); 3 (integrato) | 5 (subscale demo) |
| **Energia diurna** | Pannelli solari multi-junction GaAs (Spectrolab/Azur Space), η ≥ 30% | 6 (cell-level); 4 (integrato HALE) | 5-6 |
| **Energia notturna** | Batterie LiS (target 350 Wh/kg pack), TBD | 4 (LiS cell), 3 (HALE integration) | 5 |
| **Autopilota / FCS** | Custom DAL-C, ridondante 2oo3 | 4 (proprietario) | 6 |
| **Avionica** | Triplex IMU + dual-frequency GNSS + ADS-B IN | 6 (component); 4 (integrato HALE) | 6 |
| **C2 link** | SATCOM Inmarsat/Iridium per BLOS + RF backup | 8 (component); 4 (integrato) | 6 |
| **Payload EO** | RGB high-res + IR LWIR + (opt.) multispettrale | 8 (component); 4 (integrato) | 7 |
| **Payload NTN** | gNodeB 5G NR-NTN Rel-17/18 regenerative | 4-5 (gNB component); 3 (integrato HALE) | 5 |
| **Ground segment HAPS** | Gateway 31 GHz Ka-band feeder + mission control | 6 (Ka comp); 3 (gateway dedicato) | 5-6 |

> **Falsifying observation §6.1.2**: se al gate M+24 il TRL integrato 6B subsystem critici non raggiunge 5, la Phase C-D è non finanziabile e il Percorso 6B va sospeso o ridimensionato a "seasonal-only" / "regional-only".
> **Probabilità: M-H, impatto: H**. È il showstopper #1 trasversale.

### 6.1.3 Coerenza architetturale 6A → 6B (boundary B2)

In linea con boundary B2 (asset riusabili dal Percorso 6A al 6B), le scelte architetturali 6A privilegiano elementi che restano usabili in fase 6B:

| Asset 6A | Riuso 6B | Note |
|---|---|---|
| Ground segment (GS fissa + mobile, software pipeline) | ✅ Riuso ~80% (espansione con gateway Ka HAPS) | Investimento difensibile |
| Cloud IT/EU GDPR + NIS2 | ✅ Riuso 100% | |
| Data governance + privacy by design | ✅ Riuso 100% | |
| Autorizzazioni regolatorie SORA + experience ENAC engagement | ✅ Riuso 70% (path Specific → Certified richiede riavvio TC) | |
| Brand + reputation + cooperative network | ✅ Riuso 100% | |
| Payload EO RGB+IR | ⚠️ Adattabile (alleggerito per HALE) | Re-engineering richiesto |
| Avionica VTOL JOUAV proprietaria | ❌ Non riusabile (HALE custom DAL-C) | |
| Piattaforma volante | ❌ Non riusabile (concept diverso) | |

**Riuso medio asset 6A → 6B**:
- **~60% in conteggio di categorie di asset riusabili** (ground segment + cloud + data governance + autorizzazioni + brand + payload adattabile vs piattaforma volante + avionica + propulsione 6A specifici)
- **~30-40% in valore monetario riusato** (€250-550k di asset Y1 riusabili su CapEx 6A €700k-€2M — vedi Cap. 10 §10.3.1)

Le due metriche misurano cose diverse e sono entrambe corrette. Confidence: medium (qualitativo); quantificazione monetaria precisa in Vol. 2 Allegato A.7.

---

## 6.2 Analisi delle Prestazioni Preliminari

### 6.2.1 Prestazioni Percorso 6A (VTOL pilota Pentema)

**Riferimento metodologico**: NASA SE Handbook §6.1 (Performance Analysis) + dati vendor JOUAV CW-30E [^1].

| Parametro | Valore baseline | Sorgente | Confidence | Falsifying observation |
|---|---|---|---|---|
| Autonomia operativa | 6-10h | Vendor datasheet `[JOUAV CW-30E datasheet \| 2024 \| vendor \| medium]` | medium | -30/40% in condizioni Pentema (vento + freddo + payload pieno) → soglia 4h |
| Velocità crociera | 100-120 km/h | Vendor | medium | Vento canalizzato Pentema riduce ground speed netta |
| MTOW | 38 kg | Vendor | high | – |
| Payload utile max | 8 kg | Vendor | high | – |
| Quota max operativa | 4500 m AMSL | Vendor | medium | Pentema 1100-1300 m → margine OK |
| Range C2 (LOS) | 50 km | Vendor | medium | Shadow zones valle riducono effettivo a ~20-30 km LOS, mitigate con SATCOM |
| Operating temp | -20°C / +55°C | Vendor | high (self-heating systems) | Inverno Pentema -10°C → OK con caveat su batterie |
| Vento sostenuto max | 13.9-17.1 m/s | Vendor | medium | Pentema raffiche locali possibili > soglia → giorni operativi limitati |
| Pioggia max | ≤10 mm/24h | Vendor | medium | Eventi estremi alluvionali Liguria > soglia → operatività interrotta |

> **Calcolo realistico autonomia Pentema** (vedi `agents/aerodynamics-structures-engineer.md` + `agents/propulsion-energy-engineer.md`):
> - Quota terreno 1200 m AMSL: motore -10% prestazione vs sea level
> - Vento canalizzato 5-10 m/s sustained: +15% consumo
> - Temperatura inverno -5°C: -10% capacità batterie LiPo
> - Payload pieno (~6-7 kg): consumo nominale
> - **Autonomia realistica Pentema inverno: 4-6h** (vs 6-10h nominale)

Conforme al SyR-P-001 (autonomia ≥ 4h in condizioni nominali) con margine.

### 6.2.2 Prestazioni Percorso 6B (HALE stratosferico)

**Riferimento metodologico**: aerodinamica low-Re + energy balance stratosferico (vedi `agents/aerodynamics-structures-engineer.md` + `agents/propulsion-energy-engineer.md`).

#### 6.2.2.1 Aerodinamica HALE preliminare

| Parametro | Valore target | Note |
|---|---|---|
| Aspect Ratio (AR) | ≥ 25 | Standard HALE solare per minimizzare drag indotto |
| Apertura (b) | 25-30 m | Bilanciamento tra L/D e massa strutturale |
| Superficie alare (S) | ~25-35 m² | Da AR + b |
| MTOW | 80-150 kg | Range a confidence low (dipende da massa batterie + payload) |
| Wing loading (W/S) | 30-50 N/m² | Tipico HALE solar (vs ~500 N/m² aviazione commerciale) |
| L/D max | ≥ 25 (target 30+) | Per energy balance perennial |
| Re crociera a 20 km | O(10⁵-10⁶) | Profili low-Re dedicati (SD8000, E387, HALE-specific) |
| Velocità crociera (TAS) | 30-50 km/h | Bassa, per minimizzare drag |
| CL crociera | 0.7-1.2 | Lift coefficient |

**Profili low-Re raccomandati** (riferimento accademico [^2]): SD7037, SD8000, E387, oppure profili custom HALE-specific (alcune tesi POLITO DIMEAS [^3]).

#### 6.2.2.2 Energy balance preliminare HALE 44°N

Riferimento metodologico: `agents/propulsion-energy-engineer.md` + ricerca POLITO DIMEAS HELIPLAT [^3].

**Condizioni operative**:
- Latitudine: 44°N (Liguria nord)
- Quota: 20 km (sopra strato Ozono, ~1366 W/m² irradianza extraterrestre)
- Efficienza pannelli GaAs multi-junction: 30-32% (Spectrolab XTJ Prime ≈ 30%)
- Efficienza ciclo carica-scarica: 90-93%
- Margine richiesto: ≥30% sul caso peggiore (solstizio inverno)

**Caso estate (solstizio 21 giugno, 44°N)**:
- Elevazione solare max: 69.5°
- Fotoperiodo: ~15.5h
- Energia solare giornaliera disponibile (sea level equivalent): ~12-14 kWh/m² × area pannelli
- Energia notturna richiesta: ~8.5h × P_cruise

**Calcolo preliminare estate (area pannelli stimata 25 m²)**:
- E_solar_day ≈ 25 m² × 12 kWh/m² × 0.30 = **90 kWh/giorno**
- E_consumption_24h ≈ P_cruise × 24h (P_cruise stimato 0.5-1.0 kW)
  - Se P_cruise = 800 W → E_24h = 19.2 kWh
- **Margine estate: ~370%** ✅ ottimo, surplus utilizzabile per ricarica batteria + payload aggressivo

**Caso inverno (solstizio 21 dicembre, 44°N)**:
- Elevazione solare max: 22.5° (basso)
- Fotoperiodo: ~8.5h
- Energia solare giornaliera (clear sky equivalente): ~3-4 kWh/m² × area
- Energia notturna richiesta: ~15.5h × P_cruise

**Calcolo preliminare inverno**:
- E_solar_day ≈ 25 m² × 3.5 kWh/m² × 0.30 = **26 kWh/giorno**
- E_consumption_24h = 800 W × 24h = 19.2 kWh
- E_storage_night = 800 W × 15.5h = 12.4 kWh
- Energia per ricarica batteria = E_solar_day - E_consumption_day = 26 - (800W × 8.5h) = 26 - 6.8 = **19.2 kWh** ← appena sufficiente per la notte
- **Margine inverno: ~0-15%** ❌ critico, **showstopper RSK-TEC-001**

> **Falsifying observation §6.2.2.2** (RSK-TEC-001 — formalizzato Risk Register):
> - Margine inverno < 30% al gate M+10 con design baseline (MTOW 100 kg, pannelli 25 m², LiS 350 Wh/kg) → **scenario "seasonal-only fallback"** (operatività marzo-ottobre)
> - Margine inverno < 10% → **abbandono Percorso 6B perennial**, ridimensionamento a seasonal commercial service
> - Margine inverno > 30% con design avanzato (LiS 400+ Wh/kg, pannelli 30+ m², HALE alleggerito) → **GO Phase B con riserva**

**Sensitivity analysis chiave** (vedi `agents/propulsion-energy-engineer.md`):
- Massa batterie + densità energetica → driver primario
- Area pannelli → driver secondario (limite strutturale apertura ≤30 m)
- L/D crociera → driver terziario (riduce P_cruise)

### 6.2.3 Bilancio di Massa Preliminare HALE

Stima preliminare massa (vedi Vol. 2 Allegato A.8 per il bilancio dettagliato):

| Voce | Massa stimata (kg) | % MTOW | Note |
|---|---|---|---|
| Struttura primaria (ala + fusoliera + coda) | 35-50 | 35-40% | CFRP + fibra di lino secondaria |
| Pannelli solari + film | 8-15 | 8-12% | 25 m² × ~0.5 kg/m² |
| Batterie | 20-35 | 20-25% | LiS pack, target 350 Wh/kg |
| Propulsione (motori + eliche + governo) | 5-10 | 5-8% | Elettrica, ridondante |
| Avionica + GNC | 5-10 | 5-8% | Triplex IMU + GNSS + FCS |
| Sistema C2 (antenne + transceiver) | 2-5 | 2-4% | SATCOM L-band + RF backup |
| Payload | 5-10 | 5-10% | EO + IR + (eventuale) gNB |
| Sistema termico | 3-7 | 3-6% | Riscaldamento batterie + raffreddamento |
| Cablaggi + connettori | 2-4 | 2-3% | |
| **MTOW totale** | **85-146 kg** | 100% | |

**Range MTOW**: 85-150 kg → coerente con specifica 80-150 kg.

---

## 6.3 Trade Studies (DOCFAP — Documento di Fattibilità delle Alternative Progettuali ex art. 41)

Per ciascuna decisione architetturale chiave, conduciamo trade study formali secondo skill `trade-study-analysis`. Riportiamo qui i **sei trade study principali**, con dettaglio in Vol. 2 Allegato A.3.

### 6.3.1 TS-PLATFORM-6A — Selezione Piattaforma VTOL

**Decisione**: scelta della piattaforma commerciale baseline per il Percorso 6A pilota Pentema.

**Alternative valutate**:
- A1: JOUAV CW-30E (CN, ibrido VTOL+fixed-wing, 8 kg payload)
- A2: Quantum Trinity F90+ (DE, VTOL puro, 1 kg payload)
- A3: FlyingBasket FB3 (IT, multirotore heavy, 100 kg payload)
- A4: Tekever AR3 (PT, fixed-wing catapulta + atterraggio reti, 2.5 kg payload)
- A0: Status quo (no acquisizione, sub-contract a operatori esistenti)

**Criteri pesati** (skill `trade-study-analysis`):

| Criterio | Peso | A1 JOUAV | A2 Quantum | A3 FB3 | A4 Tekever |
|---|---|---|---|---|---|
| Autonomia missione | 20% | 8 | 4 | 5 | 9 |
| Payload compatibility | 15% | 9 | 4 | 8 | 6 |
| Certificabilità SAIL | 15% | 7 | 9 | 7 | 7 |
| Lead time | 10% | 6 | 8 | 6 | 6 |
| TCO 5 anni | 15% | 7 | 8 | 5 | 6 |
| Supporto tecnico IT/EU | 10% | 7 | 9 | 9 | 8 |
| Geopolitica/dual-use risk | 10% | 5 | 9 | 9 | 8 |
| Track record similar missions | 5% | 8 | 5 | 5 | 7 |
| **Σ ponderato** | 100% | **7.30** | **6.80** | **6.80** | **7.30** |

**Raccomandazione preliminare**: **A1 JOUAV CW-30E** o **A4 Tekever AR3** (parità).

**Considerazioni qualitative**:
- A1 JOUAV: massimo payload (8 kg), autonomia ottima (8h), ma **vendor cinese** (RSK-GEO-003 supply chain)
- A4 Tekever (Portogallo): EU sovereign supply ✓, autonomia ottima (16h), ma payload limitato (2.5 kg) + catapulta richiede infrastruttura

**Mitigazioni RSK-GEO-003 per A1**: stock spare parts 12 mesi, contratto vendor con clausole continuità, valutazione path migrazione futura verso Tekever/Quantum.

**Decisione provvisoria**: **A1 JOUAV CW-30E** come baseline, con **A4 Tekever come Plan B** se vincoli geopolitici impongono ripiego entro M+9.

**Falsifying observation**: se sanzioni o restrizioni export US-CN bloccano JOUAV entro M+6, attivazione automatica path A4 Tekever, con CapEx 6A +€100-200k.

### 6.3.2 TS-MATERIAL — Materiali strutturali HALE

**Decisione**: composizione materiali per la struttura HALE (longherone primario, ricoprimento, fusoliera).

**Alternative valutate**:
- M1: CFRP puro standard (carbon fiber reinforced polymer)
- M2: Ibrido CFRP + fibra di lino (skin lino, longherone CFRP)
- M3: Full bio-composite (lino + matrice bio-resin)

**Caratteristiche meccaniche** (vedi `fonti/2023_05_Pinato_Tesi_01.md` Polimi 2023 [^4]):

| Proprietà | CFRP standard | Lino UD | Ibrido lino/CFRP |
|---|---|---|---|
| Modulo E (GPa) | 135 | 35-50 | 80-100 |
| Densità ρ (g/cm³) | 1.55 | 1.4 | 1.45-1.5 |
| Resistenza specifica | alta | media | media-alta |
| Smorzamento naturale | basso | **5-10× CFRP** | medio |
| Sostenibilità | media | **alta** | medio-alta |
| Costo (€/kg) | 80-200 | 20-50 | 50-100 |
| Vulnerabilità umidità | bassa | **alta** | media |
| Maturità aerospace certificata | strutture primarie ✓ | strutture secondarie (Biogear ItalDesign) | strutture secondarie sperimentali |

**Criteri pesati**:

| Criterio | Peso | M1 CFRP | M2 Ibrido | M3 Full Bio |
|---|---|---|---|---|
| Rigidezza specifica | 20% | 10 | 7 | 4 |
| Smorzamento (anti-flutter) | 15% | 4 | 8 | 9 |
| Massa totale struttura | 20% | 9 | 7 | 4 |
| Costo materiali + manufacturing | 10% | 5 | 7 | 6 |
| Sostenibilità ESG | 15% | 5 | 9 | 10 |
| Certificabilità aerospace | 15% | 10 | 6 | 3 |
| Durabilità ambientale | 5% | 9 | 6 | 4 |
| **Σ ponderato** | 100% | **7.65** | **7.20** | **5.50** |

**Raccomandazione**: **M2 Ibrido CFRP + lino per strutture secondarie**, con longherone primario in CFRP.

**Razionale**:
- Longherone alare primario certificabile → CFRP standard (M1)
- Skin ala + componenti secondari (fairings, accessi, etc.) → fibra di lino (narrativa ESG)
- Saving peso vs full CFRP: 5-10% sulla massa skin (non longherone)
- Saving peso vs metallico: irrilevante (HALE non ha metallico)

> **⚠️ Caveat epistemico §6.3.2** (Regola 1): la fibra di lino in **struttura primaria certificata aerospace** richiede **5-10 anni di qualification path** (test panel + structural test + qualification authority). **Fuori scope dello Studio attuale**. Confidence: high su lino in secondarie (vedi Biogear Fuko+Turtle [^5]); **very low** su lino in primarie.

### 6.3.3 TS-PROP-6B — Architettura energetica HALE

**Decisione**: combinazione propulsione + storage per il Percorso 6B HALE.

**Alternative valutate**:
- E1: Solare + Li-ion (stato dell'arte 250-300 Wh/kg pack)
- E2: Solare + LiS (target 350-450 Wh/kg pack, TRL 4-5 nel 2026, 5-6 atteso 2028)
- E3: Solare + Solid-State Li (target 380 Wh/kg pack, TRL 3-4 oggi)
- E4: Solare + PEM Fuel Cell + LH2 (alta densità energetica, ma complessità criogenica)
- E5: Seasonal solar-only (no batteria notturna, operatività solo marzo-ottobre)

**Trade-off** (vedi `agents/propulsion-energy-engineer.md` per dettaglio):

| Architettura | Margine inverno | Maturità tech 2028 | Massa relativa | Complessità integrazione | Verdetto |
|---|---|---|---|---|---|
| **E1 Solar+Li-ion** | < 0% (impossibile perennial inverno) | ✅ | + 50% vs LiS | bassa | ❌ no perennial |
| **E2 Solar+LiS** | 0-30% (critico) | TRL 5 atteso 2028 | baseline | medio-bassa | ⚠️ marginale |
| **E3 Solar+SS Li** | 10-25% | TRL 5 atteso 2029-2030 | -10% vs LiS | media | ⚠️ marginale |
| **E4 Solar+PEM+LH2** | 50%+ teorico | TRL 3-4 (criogenia HALE) | + 30% baseline | **alta** (LH2 safety) | possibile Y6+ |
| **E5 Seasonal-only** | n/a (no inverno) | ✅ tech disponibile | + 0% (no batteria estesa) | bassa | ✅ fallback robusto |

**Raccomandazione baseline Y3-Y5**: **E2 Solar+LiS** con fallback **E5 Seasonal-only** se margine inverno < 10% al gate M+24.

**Raccomandazione Y6+ (post-Phase B)**: valutare migrazione a E3 SS Li (per safety + ciclo vita) o E4 PEM+LH2 (per perennial guaranteed).

**Falsifying observation §6.3.3**: se al gate M+24 TRL pack LiS < 5 (target 2028), il Percorso 6B perennial è bloccato; attivazione automatica E5 Seasonal-only.

### 6.3.4 TS-AVI-6A — Autopilota Percorso 6A

**Decisione**: software/hardware FCS per il Percorso 6A.

**Alternative**:
- AV1: JOUAV FCS proprietario (integrato in CW-30E)
- AV2: Pixhawk Cube modificato + ArduPilot custom
- AV3: MicroPilot MP21283X (DAL-C certificabile)
- AV4: UAVOS Aerospace AP-1

**Trade study** (sintetico):

| Criterio | Peso | AV1 JOUAV | AV2 Pixhawk | AV3 MicroPilot | AV4 UAVOS |
|---|---|---|---|---|---|
| Integrazione con piattaforma | 25% | 10 | 6 | 5 | 5 |
| Costo aggiuntivo | 15% | 10 | 8 | 4 | 5 |
| Certificabilità SORA SAIL III | 15% | 7 | 5 | 9 | 8 |
| Maturità + track record | 15% | 9 | 8 | 8 | 7 |
| Customizability future 6B | 10% | 3 | 9 | 8 | 8 |
| Supporto vendor EU | 10% | 5 | 7 | 8 | 9 |
| **Σ ponderato** | 100% | **8.05** | **6.85** | **6.40** | **6.20** |

**Raccomandazione**: **AV1 JOUAV FCS** per il Percorso 6A (integrazione naturale).

### 6.3.5 TS-PAYLOAD-EO — Payload EO modulare 6A

Riferimento: `agents/earth-observation-expert.md`.

**Configurazione baseline raccomandata Percorso 6A**:

- **Sensore RGB high-res**: Phase One iXM 100 (100 MP, 4.6 μm pixel) + lente 50-200 mm → GSD 8 cm @ 500 m AGL
- **Sensore IR LWIR**: WIRIS Pro (NEdT < 30 mK, GSD termico 5 m @ 500 m)
- **Configurazione opzionale Y2**: aggiunta multispettrale MicaSense Altum-PT (4 bande VIS-NIR + termico calibrato) per uso agricolo cooperative
- **Configurazione opzionale Y3+**: LiDAR (YellowScan Voyager) per mapping infrastrutture lineari ad alta precisione

**Modularità garantita** da interfaccia payload standard (cf. ICD Cap. 4.4): swap < 30 min in ground operations.

### 6.3.6 TS-COMMS — Architettura C2 + downlink dati

Riferimento: `agents/avionics-gnc-engineer.md` + `agents/telecom-ntn-payload-expert.md`.

**Percorso 6A — C2 link**:
- **Primary**: RF 2.4 GHz (banda ISM, no AGCOM licensing necessario), LOS range 30-50 km, fade margin 12 dB
- **Secondary**: SATCOM Iridium Certus L-band per shadow zones Pentema (geopoliticamente accettabile, Iridium è US-EU joint)
- **Tertiary fallback**: cellulare 4G se disponibile (per operazioni di emergenza in area coperta da TIM/Vod)

**Percorso 6B — Service link + Feeder link** (vedi `agents/telecom-ntn-payload-expert.md`):
- **Service link**: S-band 2.0-2.2 GHz (NTN 3GPP Rel-17 n255/n256) oppure 700 MHz (5G NR rural)
- **Feeder link**: Ka-band 31-31.3 GHz (banda HAPS dedicata ITU)
- **C2 + telemetria**: SATCOM L-band Inmarsat o Iridium

**Link budget preliminare downlink HAPS service link** (skill `link-budget-calculator` applicata):

```
Configurazione: HAPS @ 20 km, banda 2.6 GHz (n7 LTE), BW 20 MHz, 16QAM 5/6
Slant range typical 25 km nadir + 10° offset

EIRP HAPS (P_tx 25W + G_antenna 24 dBi - L_tx 1 dB)        37.0 dBW
- Free space path loss @ 2.6 GHz, 25 km                    -128.7 dB
- Atmospheric + cloud + rain (ITU-R P.618-14 zona K Italia)  -2.0 dB
- Polarization + scintillation + body loss                   -3.8 dB
+ G/T receiver UE                                           -25.6 dB/K
+ k correction Boltzmann                                   +228.6 dB
= C/N0                                                     106.0 dB-Hz

- 10·log10(BW = 20 MHz = 73 dB-Hz)                          -73.0 dB
= SNR                                                       33.0 dB

SNR required (16QAM 5/6)                                    11 dB
LINK MARGIN                                                 22 dB ✓
```

**Verdetto link budget**: ampio margine, design del payload telecom HAPS è **tecnicamente fattibile**. Capacità cella stimabile ~88 Mbps per cella sotto FRC NR-NTN.

---

## 6.4 Analisi di Rischio Ingegneristico (FMECA + FTA preliminare)

In coerenza con D.Lgs. 36/2023 art. 41 ("analisi di rischio ingegneristico") + skill `risk-register-builder` + ARP4761.

### 6.4.1 Top-10 rischi tecnici (estratto Risk Register, dettaglio Vol. 2 Allegato A.2)

| ID | Rischio | P | I | Score | Tipo | Owner | Mitigation principale |
|---|---|---|---|---|---|---|---|
| **RSK-TEC-001** 🔴 | Energy balance HALE inverno 44°N | 4 | 5 | **20** | Tech | propulsion-energy-engineer | Design margin + fallback seasonal-only |
| **RSK-TEC-002** 🔴 | Aeroelasticità ala high-AR (flutter, divergenza) | 3 | 5 | **15** | Tech | aero-structures-engineer | Aeroelastic analysis nonlineare + GVT + flight test subscale |
| **RSK-TEC-003** 🔴 | Type Certification timeline HALE > 5 anni | 4 | 4 | 16 | Reg | aviation-regulatory | Parallel approach + Special Condition pathway |
| RSK-TEC-004 🟡 | Integrazione payload modulare 6A (compatibilità elettrica/SW) | 3 | 3 | 9 | Tech | systems-engineer | Test bed pre-deploy + ICD rigoroso |
| RSK-OPS-001 🟡 | Operazioni invernali Appennino (neve, ghiaccio, basse temp) | 3 | 3 | 9 | Ops | vtol-uas-specialist | Training pilota + finestre operative + de-icing |
| RSK-REG-002 🟡 | SORA SAIL Pentema BVLOS > III (richiede percorso Certified) | 3 | 3 | 9 | Reg | aviation-regulatory | Pre-application ENAC + M1/M2 mitigation |
| RSK-SUP-001 🟡 | Lead time JOUAV / sanzioni USA-CN | 3 | 3 | 9 | Supply | vtol-uas-specialist | Plan B Tekever + stock 12 mesi |
| RSK-TEC-005 🟡 | Cybersecurity link C2 (jamming, spoofing) | 2 | 4 | 8 | Tech | avionics-gnc-engineer | Frequency hopping + crypto authentication |
| RSK-TEC-006 🟡 | Privacy by design fail (DPIA bocciata Garante) | 2 | 4 | 8 | Reg/Tech | data-privacy-counsel | Edge anonymization + geofence aree residenziali |
| RSK-TEC-007 🟡 | Lost-Link behaviour mismatch SORA OSO #9 | 2 | 4 | 8 | Tech/Reg | avionics-gnc-engineer | Lost-Link Profile + Return-to-Base testato |

### 6.4.2 FMECA preliminare — Sottosistema Payload EO

Riferimento: skill `risk-register-builder` §FMECA.

| Item | Failure Mode | Cause | Local Effect | System Effect | S | F | D | RPN | Mitigation |
|---|---|---|---|---|---|---|---|---|---|
| Camera RGB | No image | Sensor failure | Loss EO mission | Mission abort | 3 | 2 | 2 | 12 | Ridondanza dual sensor, healthcheck onboard |
| Camera RGB | Blur image | Vibrazioni gimbal | Quality degradata | Re-fly necessario | 2 | 3 | 3 | 18 | Gimbal damping + IBIS |
| Gimbal | Stuck | Motor failure | Off-target | Reduced area coverage | 3 | 3 | 2 | 18 | Service interval + ridondanza motor |
| IR sensor | Calibrazione persa | Termica + tempo | False alarms / missed hotspot | False positive antincendio | 4 | 3 | 4 | 48 | NUC frequente + crosscheck con RGB |
| Storage on-board | Corruzione data | Bit flip / temperatura | Loss data missione | Re-fly necessario | 3 | 2 | 3 | 18 | RAID-style ridondanza + on-line backup |
| Downlink data | Interruzione bandwidth | RF interference | Delay delivery | Latency degradata | 2 | 3 | 4 | 24 | Buffer + retry + alt downlink |

**RPN limite di intervento**: ≥ 40 (mitigation obbligatoria). Top item: IR sensor calibrazione (RPN 48) → procedure NUC + crosscheck applicate.

### 6.4.3 FTA preliminare — Top event "Loss of Vehicle in BVLOS"

Per il Percorso 6A, costruzione albero AND/OR del top event "Loss of Vehicle":

```
Loss of Vehicle in BVLOS [TOP]
├─ OR ─ Lost Link permanente E Return-to-Base fail
│   ├─ Lost Link (P ~ 10⁻⁴/h, RF + SATCOM entrambi)
│   └─ Return-to-Base procedure fail (P ~ 10⁻³ given Lost Link)
├─ OR ─ Avaria FCS critica
│   ├─ Failure autopilota DAL-C primario
│   ├─ AND ─ IMU 1 + IMU 2 fail simultaneo
│   └─ GNSS spoofing / jamming sostenuto
├─ OR ─ Avaria propulsione + atterraggio fail
│   ├─ Engine failure
│   ├─ Battery thermal runaway
│   └─ Parachute deployment fail
└─ OR ─ Cyber attack hijacking
    ├─ Crypto key compromise
    └─ Authentication bypass
```

**Probabilità top event preliminare**: ~10⁻⁵ - 10⁻⁶/h (ordine di grandezza). Target per SAIL III: 10⁻⁵/h (conforme).

> **Falsifying observation §6.4.3**: se FTA dettagliato post-DOA (Detailed Operational Analysis) mostra single point of failure non mitigato con probabilità > 10⁻⁴/h, design FCS è da rivedere prima del SAIL III approval.

---

## 6.5 Infrastrutture e Ground Segment

### 6.5.1 Ground Segment Percorso 6A

**Architettura distribuita Pentema-centric**:

| Elemento | Posizione | Funzione | Dimensione |
|---|---|---|---|
| **GS fissa Pentema** | Pentema (Torriglia, GE), 1100-1300m | Mission control + storage primario + link RF primario | Container 20' o cabin 30 m² |
| **GS mobile** | Veicolo cooperativa (mobile) | Operazioni in campo + link RF secondario + supporto piloti remoto | Veicolo 4x4 con torre antenna |
| **Hangar protetto** | Pentema | Storage UAV + manutenzione + ricarica batterie | 50-100 m² coperto |
| **Server cloud IT/EU** | Aruba o OVH IT | Storage long-term + processing + delivery PA | Hosted (no infrastructure on-site) |

**Costo infrastrutturale stimato**: €70-200k (vedi Cap. 8 dettaglio).

### 6.5.2 Ground Segment Percorso 6B (preliminare Y3-Y5)

| Elemento | Posizione | Funzione |
|---|---|---|
| **Mission Control HAPS** | Base operativa principale (Liguria o GATB Grottaglie) | Controllo missioni perennial + payload management |
| **Gateway Ka-band 31 GHz** | Site dedicato (vicino MC) | Feeder link HAPS↔terra a 31 GHz |
| **Hangar tecnologico** | Site dedicato | Storage HAPS subscale + maintenance + ascent prep |
| **Test site (per Phase B)** | Sardegna (EuroHAPS analog) o test bed estero | Flight test stratosferico subscale |

**Costo infrastrutturale stimato Phase B**: €500k-2M (incluso nel R&D €5.5-13.5M).

---

## 6.6 Verification & Validation Tecnica (Riferimento Cap. 3.7)

V&V plan dettagliato in Vol. 2 Allegato A.5. Sintesi per il Cap. 6:

| Sottosistema | Metodi V&V preliminari (Phase A) | V&V Phase B | V&V Phase C-D |
|---|---|---|---|
| Aerodinamica | XFLR5 / AVL low-fidelity | CFD RANS + wind tunnel subscale | Flight test full-scale |
| Strutture | Calcoli analitici + FEA preliminare | Test panel + structural test subscale | GVT + flight test load envelope |
| Propulsione energia | Modello energy balance + sensitivity | Test cell pannelli + batterie ground | Test integrato subscale + perennial flight |
| Avionica/FCS | Simulazione HIL (Hardware In the Loop) | Test bed integrato | Flight test BVLOS |
| Payload | Test bench bench-level | Test integrato + fly-and-measure | Operations validation |
| Comms | Link budget + simulazione | Test link bench + range test ground | Test link in volo |
| Ground segment | Walkthrough + simulazione operativa | Test bed integrato | Operations validation |

---

## 6.7 Open Questions Tecniche (Riepilogo, dettaglio Cap. 3.10)

Le 18 Open Questions del Cap. 3.10 si applicano direttamente al Cap. 6. Le più critiche tecnicamente:

- **OQ-001** Quale piattaforma VTOL baseline definitiva? → TS-PLATFORM-6A da chiudere M+6
- **OQ-003** Quale layup composito longherone HALE? → TS-MATERIAL da affinare M+12
- **OQ-004** Energy balance HALE inverno: perennial o seasonal? → simulazione completa M+10
- **OQ-005** Quale architettura propulsione 6B definitiva? → TS-PROP-6B da chiudere M+12
- **OQ-006** Quale autopilota 6A? → TS-AVI-6A in chiusura
- **OQ-007** Quale payload modulare baseline? → TS-PAYLOAD-EO da affinare M+6
- **OQ-013** Quale test bed BVLOS (Pentema vs GATB Grottaglie)? → decisione M+6

---

## 6.8 Red Team Check — Adversarial Technical Review

Critica condotta da `red-team-skeptic` + `aerospace-systems-engineer`.

### Critica 1 — "Energy balance inverno è dichiarato marginale (margine 0-15%): è gente che si racconta che il progetto funziona quando i numeri dicono il contrario"
**Razionale**: il calcolo §6.2.2.2 mostra margine inverno ~0-15% con baseline (MTOW 100 kg, pannelli 25 m², LiS 350 Wh/kg). Significa che operazione perennial a 44°N è **marginale al limite del fattibile**. Non è "Go", è "Pray".
**Risposta**: confermato. Per questo il fallback **seasonal-only** è esplicitamente nel design come Plan B, e RSK-TEC-001 è formalmente score 20 🔴. La narrativa onesta è: **estate perennial OK, inverno marginale → seasonal o margin tech innovation richiesta**.
**Action item**: simulazione energy balance ad alta fedeltà (clear sky variability + monthly profile) entro M+10 per decisione gate.

### Critica 2 — "La fibra di lino come 'asset ESG' è marketing, non ingegneria"
**Razionale**: §6.3.2 ammette che lino è ammissibile solo per strutture secondarie. Il saving massa è marginale (~5-10% sulle skin, non strutture primarie). La narrativa "HALE in fibra di lino italiano sostenibile" è esagerata.
**Risposta**: confermato. Il claim "ESG-friendly HALE" è ridimensionato a "uso di compositi naturali in strutture secondarie + propulsione 100% solare = miglior carbon footprint vs alternative satellite + diesel". È **veritiero ma misurato**, non hype.
**Action item**: quantificare carbon footprint comparativo (LCA — Life Cycle Assessment) entro M+12 per supportare narrativa con dati.

### Critica 3 — "TS-PLATFORM-6A: la scelta JOUAV CW-30E è dominata da rischi geopolitici"
**Razionale**: scegliere vendor cinese in 2026, con escalation tariffaria USA-CN possibile, è **fragile**. La scelta razionale per stabilità sarebbe Tekever (PT) o Quantum (DE), anche con prestazioni inferiori.
**Risposta**: corretto. La raccomandazione preliminare resta **A1 JOUAV con Plan B A4 Tekever pronto**. Verifica continua del quadro geopolitico (DR-008 chiusura via engagement DG DEFIS).
**Action item**: contratto JOUAV con clausole continuità + stock spare 12 mesi + valutazione Tekever quotation parallelo entro M+6.

### Critica 4 — "L'integrazione payload modulare in 30 min in ground è ottimistica"
**Razionale**: lo swap di payload UAV (EO ↔ IR ↔ telecom) tipicamente richiede 1-2h con calibrazione + test. Pretendere 30 min è "vendor marketing".
**Risposta**: vero, 30 min è **target stretch**. Realisticamente 60-90 min con team trained, 2-4h primo swap. Aggiorno OQ-007 per validare in test bed reale.

### Critica 5 — "Link budget HAPS @20 km mostra 22 dB margin: solo per scenario nominale. Ma in rain fade reale?"
**Razionale**: il calcolo usa ITU-R P.618-14 zona K che è già ragionevole, ma scenari di temporali estremi possono spingere rain fade > 5 dB anche in S-band. Il margin 22 dB tiene ma è meno comodo.
**Risposta**: confermato. Aggiornare link budget con scenarios "stormy day worst-case 1% time" per validare margine in scenari estremi. Probabilmente margine cade a 12-15 dB worst case, ancora **sufficiente**.

### Critica 6 — "Il riuso 60% asset 6A → 6B è dichiarato ma non quantificato"
**Razionale**: la tabella §6.1.3 elenca asset riusabili, ma non quantifica il valore economico riusato. Affermazione "riuso 60%" è qualitativa.
**Risposta**: corretto. Aggiungere Cap. 8 (Economico-finanziario) con quantificazione: ground segment ~€80-150k riusati, software pipeline ~€50-100k, brand+rete ~€100-300k stimati (intangible). Riuso quantitativo ~€250-550k su CapEx 6A €700-1200k → ~30-40% in valore monetario.

---

## 6.9 Riferimenti

[^1]: JOUAV CW-30E Hybrid VTOL UAV — Datasheet vendor 2024. Source: `fonti/...` (datasheet vendor, da quotation diretta). **Confidence: medium** (vendor self-declared).

[^2]: Profili low-Re per HALE — Selig SD8000 / Eppler E387 / NACA 64-series HALE-specific. Pubblicazioni accademiche AIAA + Polito DIMEAS.

[^3]: POLITO DIMEAS — Romeo et al., "Design of solar high altitude long endurance aircraft for multi payload & operations" — Heliplat programme 2005-2010. Source: ResearchGate + ScienceDirect (citato in `riferimenti/ricerche-approfondite.md` §9).

[^4]: Pinato Elia, "Material characterization of a flax fiber reinforced composite for crashworthiness applications", Polimi 2023. Source: `fonti/2023_05_Pinato_Tesi_01.md`. **Confidence: high** (peer-reviewed academic).

[^5]: Biogear (Fuko Roma + Turtle Srl Bologna) — landing gear elicottero CFRP+lino, -54% peso vs metallico. Source: CompositesWorld 2024 + `riferimenti/ricerche-approfondite.md` §10.

[^6]: NASA SE Handbook Rev 2 — Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`. **Confidence: high**.

[^7]: 3GPP TR 38.811 V15.4.0 — NTN channel models. Source: `fonti/38811.md`. **Confidence: high**.

[^8]: 3GPP TR 38.821 V16.2.0 — NR-NTN solutions Release 16. Source: `fonti/3GPP_TR_38821_v16-2-0_NR-NTN-solutions.md`. **Confidence: high**.

[^9]: ITU-R P.618-14 — Propagation data for Earth-space radiocommunications, Aug 2023. Source: `fonti/R-REC-P.618-14-202308-I.md`. **Confidence: high**.

[^10]: Skill `aerodynamics-structures-engineer`, `propulsion-energy-engineer`, `avionics-gnc-engineer`, `telecom-ntn-payload-expert`, `earth-observation-expert`, `vtol-uas-specialist` (vari in `.claude/agents/`).

[^11]: Skill `trade-study-analysis`, `risk-register-builder`, `link-budget-calculator`, `epistemic-rigor` (in `.claude/skills/`).

---

## 6.10 Note di chiusura del capitolo

Il Cap. 6 è bozza M+3 con **rigore tecnico medio-alto** dove le fonti consentono triangulation (NASA SE, 3GPP, ITU, Pinato) e **medium-low** dove le scelte richiedono ancora trade study completi (TS-PLATFORM, TS-MATERIAL, TS-PROP-6B).

**Verdetto tecnico riepilogato**:
- **Percorso 6A: GO** tecnicamente fattibile, rischi gestibili
- **Percorso 6B: HOLD / Go Condizionato R&D** con 2 showstopper aperti (RSK-TEC-001 energy balance inverno + RSK-TEC-002 aeroelasticità)

**Action items chiave entro M+10**:
- Simulazione completa energy balance inverno HALE
- Chiusura TS-PLATFORM-6A con quotation vendor + reference EU operatori
- Test integrato payload + GS + cloud pipeline
- Pre-application ENAC SORA (cf. Cap. 5)
- Aeroelastic analysis preliminare ala high-AR

Il capitolo è chiuso al M+3 con verdetto Red Team **OK con 6 action items**.
