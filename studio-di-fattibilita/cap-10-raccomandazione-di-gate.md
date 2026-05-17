# Capitolo 10 — Raccomandazione di Gate (Verdetto Finale)

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes
> Volume 1, Capitolo 10
>
> **Versione:** bozza M+11 (proiezione del verdetto)
> **Conformità:** NASA SE Handbook §3.0 + skill `gate-review-checklist`
> **Disciplina epistemica:** Regole 1-7 della skill `epistemic-rigor`
> **Red Team review:** combinata — `red-team-skeptic` + `regulatory-adversary` + `competitor-intelligence` — vedi §10.6

---

## 10.0 Premessa

Il presente capitolo formula la **raccomandazione di gate** dello Studio di Fattibilità — il verdetto **Go / Go Condizionato / Hold / No-Go** che il management Firmamento Technologies, in sede di Gate Review M+10/M+11 (G3 — FEASIBILITY GATE), porterà al CdA + sponsor (Coopfond + Regione Liguria) per la decisione formale di proseguire o fermare i due percorsi.

Il capitolo è **sintesi delle evidenze** prodotte nei Cap. 1-9 e 11 dello Studio, valutate contro i **criteri Go/No-Go** definiti nel Cap. 3.2 e Cap. 9.2.4. È deliberato per essere **conclusivo** ma **onesto sui limiti** delle evidenze al M+11.

---

## 10.0bis Revisione Verdetto post-Audit M+3 (CRITICAL — DEFAULT SCENARIO BASE)

> **Inserimento post-audit M+3** (red-team-skeptic + regulatory-adversary + competitor-intelligence): la formulazione originale "Go Condizionato 6A" (vedi §10.1 sotto) **sopravvaluta la probabilità di Go pieno al gate G3**. Calcolo realistico: P(AND 5 hard conditions C1-C5) = **5-15%** scenario realistico (vedi `AUDIT-QUALITY-VOLUME-1.md` §6).
>
> **Scenario base atteso al gate G3 (M+10/M+11) è HOLD CON PIANO REGOLATORIO RAFFORZATO** (probabilità 60-80%), con re-review M+13-16 e attivazione **sliding timeline** del Cap. 9 §9.12. Il verdetto "Go Condizionato" del §10.3 sotto resta valido come **scenario ottimistico** (15-35% probabilità).

### 10.0bis.1 Verdetto consolidato realistico

| Scenario | Probabilità | Verdetto effettivo G3 | Action |
|---|---|---|---|
| **Scenario A — Best case** (5 hard conditions soddisfatte M+10) | **5-15%** | **GO PIENO 6A** | Avvio operations Y1 M+12 come da piano nominale Cap. 9 |
| **Scenario B — Base case** (3-4 hard conditions soddisfatte) | **45-60%** | **HOLD CON PIANO REGOLATORIO RAFFORZATO** | Re-review G3-bis M+13-16; pivot a sliding timeline §9.12 |
| **Scenario C — Worst case operativo** (≤ 2 hard conditions soddisfatte) | **20-30%** | **HOLD ESTESO** | Re-review G3-bis M+16-20; eventuale pivot scope MVP (VLOS-only, area ridotta) |
| **Scenario D — No-Go materiale** (es. ENAC nega esplicitamente SAIL Pentema, Regione si tira indietro definitivamente) | **5-10%** | **PIVOT STRATEGICO** | Riesame business case, possibile pivot regionale (Piemonte/Calabria) o cancellazione 6A |

### 10.0bis.2 Verdetto Percorso 6B in scenario realistico

Il verdetto **HOLD / GO CONDIZIONATO ESTREMO 6B** della §10.4 sotto resta valido. Aggiornamenti post-audit M+3:

- Il 6B non parte mai prima del gate G5 (M+24), e con le sliding timeline §9.12 realisticamente **M+30-48**
- 15 showstopper regolatori aggiuntivi (vedi Cap. 5 §5.16) confermano severità path 6B
- **DR-013 finding (`riferimenti/DR-research-closure-M3.md`)**: base rate consolidato **0% HALE solari commerciali operativi globalmente** in 22 anni di tentativi (12 programmi 2003-2025 analizzati: NASA Helios crashed 2003, Aalto HAWK30 cancellato 2020, Solara 50 dissolto, Sanswire StratXX mai operativo, AALTO Zephyr "commercial entry 2024" è in realtà operations militari, Skydweller solo dual-use Navy AMPA, PHASA-35 operativo 2026 ma dual-use, ecc.) → **HOLD 6B con criteri di uscita estremamente stringenti**
- **DR-014 finding**: capital intensity per HALE solare ad operatività commerciale è $50M-1B → la stima Firmamento €5.5-13.5M Phase B è **R&D Phase 0/A**, NON percorso completo. Rivedere Cap. 8 §8.3.3
- Probabilità operatività perennial Y10 standalone stimata realisticamente **6-15%** (vedi Cap. 11 §11.6bis scenario B2-relaxed)
- **Hold del 6B è il default permanente** fino a evidenza chiara di (a) apertura framework EASA RMT HAPS + (b) partnership prime contractor o consortium EU bid
- **Pivot raccomandato per 6B**: da "HALE proprietario Firmamento" a "Firmamento operatore di servizi su piattaforme prime contractor (Aalto/Sceye/Skydweller/CIRA-EuroHAPS-successor)" come modello primario; standalone HALE Firmamento resta come **fallback R&D only**

### 10.0bis.3 Comunicazione esterna del verdetto

Per evitare l'effetto "CYA decisionale" (Red Team critica §5), il verdetto va comunicato esternamente come segue:

> **Comunicazione raccomandata al CdA + sponsor**:
> "Lo Studio di Fattibilità conferma la solidità tecnica e di mercato del Percorso 6A pilota Pentema. Le evidenze regolatorie e di engagement institutionale al M+11 sono in costruzione: il verdetto è **GO subordinato al completamento del piano regolatorio rafforzato**, con probabilità di Go pieno immediato ~5-15% e probabilità di Hold con re-review ~60-80%. Il Percorso 6B resta in HOLD strutturale subordinato a gate G5 (M+24)."

Questo evita l'overpromise ("Go!") e l'underpromise ("No-Go") che entrambi falsificano la realtà.

### 10.0bis.4 Impatto su Cap. 8 (financial) e Cap. 9 (schedule)

Il scenario base "HOLD con piano regolatorio rafforzato" implica:
- **Cap. 8**: cash burn Y1 più alto (€2-3M cumulato vs €1.2M nominale); bridge financing €500k preallocato
- **Cap. 9**: sliding timeline §9.12 è il **piano operativo di riferimento** per pianificazione finanziaria
- **Cap. 7**: revenue Y1 realistico €100-250k (vs €355-405k baseline); break-even Y5-Y6 vs Y4-Y5
- **Cap. 5 §5.17**: 3 FTE regulatory aggiuntivi (+€450-800k OpEx Y1) sono **fixed cost obbligatorio**

### 10.0bis.5 Action immediato post-Studio M+11

Il CdA + sponsor deve approvare:
- ☐ Budget Y1 **aumentato** a €2.5-3.5M (CapEx + OpEx aggiuntivo regulatory team + bridge financing)
- ☐ **Doppio binario di pianificazione**: piano nominale Cap. 9 + sliding timeline §9.12
- ☐ Re-baseline Gate G3-bis a M+13-16 dichiarata come opzione legittima
- ☐ Hold del 6B come default permanente fino gate G5
- ☐ Strategia comunicazione esterna con linguaggio "GO subordinato" (non "GO pieno")

---

## 10.1 Sintesi del verdetto

### 10.1.1 Verdetto sintetico per ciascun percorso

> **Nota M+3**: la tabella sotto riflette il **verdetto formale al gate G3** se tutte le hard conditions sono soddisfatte (scenario A, P 5-15%). Per scenario base realistico (Hold con piano rafforzato, P 60-80%), vedi §10.0bis.

| Percorso | Verdetto raccomandato | Confidenza | Razionale principale |
|---|---|---|---|
| **6A — VTOL Pilota Pentema** | ✅ **GO CONDIZIONATO** *(scenario A)* / ⚠️ **HOLD CON PIANO RAFFORZATO** *(scenario base B, default)* | medium-high | Fattibilità tecnica, regolatoria, di mercato confermata; rischi gestibili; condizioni: LoI Regione + Coopfond entro M+12, contratti ≥ 3 firmati Y1, SORA approvato |
| **6B — HALE Stratosferico** | ⚠️ **HOLD / GO CONDIZIONATO ESTREMO R&D** | low-medium | Concept fattibile, ma 2 showstopper tecnici aperti + framework regolatorio HAPS EU assente. Phase B autorizzata solo a condizione di funding mix ≥ 50% pubblico al M+24 |

### 10.1.2 Riepilogo evidenze chiave

| Dimensione | Cap. | Verdetto | Conferma |
|---|---|---|---|
| **Inquadramento** | 1 | ✓ razionale pubblico confermato | PSNAI 2025 + Briefing + bando Cooding |
| **Stakeholder + SMART** | 2 | ✓ mappa solida + 28 obiettivi SMART | 30 stakeholder mappati |
| **Requisiti + RTM** | 3 | ✓ baseline robusta | 17 StNeeds + 42 SyR + ~80 SsR + RTM v0.5 |
| **Scope + ICD** | 4 | ✓ scope chiaro + 17 deliverable + 20 interfacce | ICD preliminare completo |
| **Quadro Normativo** | 5 | ✓ 6A GO, 6B HOLD (showstopper RSK-REG-001 framework HAPS) | EASA SORA 2.5 settembre 2025 + ENAC Reg. APR Ed.3 |
| **Analisi Tecnica** | 6 | ✓ 6A GO, ⚠️ 6B HOLD (RSK-TEC-001 energy balance inverno + RSK-TEC-002 aeroelasticità) | NASA SE + 3GPP + ITU + Pinato flax |
| **Mercato + Business** | 7 | ✓ 6A GO con caveat su confidence pricing | Template ENAC AAM BP + 4 pilastri vantaggio competitivo |
| **Economico-Finanziario** | 8 | ✓ 6A GO + 6B GO Condizionato | NPV positivo Y4-Y5 scenario base; Phase B subordinato a funding |
| **Cronoprogramma** | 9 | ✓ timeline aggressiva ma fattibile | 11 mesi Studio + 12 mesi pilota 6A realistici |
| **Roadmap post-fattibilità** | 11 | ✓ visione 10 anni coerente con boundary B1+B2 | Fase 1-5 articolate con KPI/Budget/Stakeholder |

### 10.1.3 Verdetto in forma narrativa

> Lo Studio di Fattibilità della piattaforma aerea HALE/VTOL di Firmamento Technologies dimostra che:
>
> 1. Il **Percorso 6A (VTOL pilota Pentema)** è **tecnicamente, operativamente, regolatoriamente e finanziariamente fattibile** entro il time horizon di 12 mesi. La raccomandazione formale è **Go Condizionato** subordinata alla firma di Letter of Intent con Regione Liguria, autorizzazione SORA ENAC, e disponibilità di funding mix ≥ 60% al M+12.
>
> 2. Il **Percorso 6B (HALE stratosferico)** richiede una fase R&D preparatoria (Phase B) di 24 mesi a partire dal M+24, con due showstopper tecnici (energy balance perennial inverno + aeroelasticità) e uno regolatorio (assenza framework HAPS EU). La raccomandazione formale è **Hold / Go Condizionato Estremo**, con commitment a Phase B subordinato a (a) gate G5 (M+24) con criteri tecnici e finanziari quantitativi, (b) progresso del framework regolatorio EASA HAPS, (c) funding mix ≥ 50% pubblico al gate G5.
>
> 3. La **visione strategica 10 anni** (boundary B2: nodo italiano di un futuro consorzio EU sovereign stratosferico, "complementare a IRIS²") è preservata come **vettore strategico**, ma il presente Studio approva esclusivamente i passi 1-2 (Fasi 1+2). Le decisioni per Fasi 3-5 sono subordinate ai gate successivi G5, G6 e oltre.

---

## 10.2 Risk Residuo Aggregato

### 10.2.1 Showstopper formalmente registrati

| ID | Rischio | Score | Percorso impattato | Mitigation status |
|---|---|---|---|---|
| **RSK-TEC-001** | Energy balance HALE inverno 44°N margin 0-15% | 20 🔴 | 6B | Mitigation: design margin + fallback "seasonal-only marzo-ottobre" |
| **RSK-TEC-002** | Aeroelasticità ala high-AR (flutter, divergenza) | 15 🔴 | 6B | Mitigation: GVT + flight test subscale Phase B |
| **RSK-REG-001** | Mancanza framework HAPS EU (EASA Special Condition non aperto) | 20 🔴 | 6B | Mitigation: engagement EASA Innovation Network + consorzio (CIRA, TAS) |
| **RSK-FIN-001** | Mancanza commitment funding Phase B €5.5-13.5M | 20 🔴 | 6B | Mitigation: mix EDF + Horizon + PNRR + Series B raised |
| **RSK-TEC-003** | Type Certification HALE > 5 anni (no precedente civile EU) | 16 🔴 | 6B | Mitigation: parallel ops 6A + Special Condition negoziata |

### 10.2.2 Rischi alti (giallo) per il Percorso 6A

| ID | Rischio | Score | Mitigation status |
|---|---|---|---|
| RSK-OPS-001 | Operazioni invernali Appennino Liguria | 9 🟡 | Training pilota + finestre operative + de-icing |
| RSK-REG-002 | SORA SAIL Pentema > III | 9 🟡 | Pre-application ENAC + M1/M2 mitigation |
| RSK-SUP-001 | Lead time vendor cinese JOUAV | 9 🟡 | Plan B Tekever + stock 12 mesi spare |
| RSK-MKT-001 | Adozione lenta PA (cicli appalti) | 12 🟡 | Anchor customer Regione + contratti pluriennali |
| RSK-OPS-002 | Incidente UAS BVLOS sul territorio | 10 🟡 | SORA M2 + GRC mitigation + assicurazione |

### 10.2.3 Rischio aggregato per percorso

- **Percorso 6A**: nessun rischio rosso. Top 3 rischi gialli con piano mitigation chiaro. **Profilo rischio: medio-basso**. Compatibile con verdetto Go Condizionato.
- **Percorso 6B**: 5 rischi rossi (showstopper). Mitigation strategy esiste, ma **non garantita**. **Profilo rischio: alto**. Compatibile con verdetto Hold / Go Condizionato Estremo (no Phase B commitment senza milestone gate G5).

---

## 10.3 Verdetto Percorso 6A — Go Condizionato

### 10.3.1 Argomenti a supporto del Go

1. **Tecnicamente fattibile** con piattaforma commerciale TRL 8-9 (JOUAV CW-30E o Tekever)
2. **Regolatoriamente fattibile** in Specific Category SAIL II-III BVLOS — framework EASA SORA 2.5 europea (settembre 2025) disponibile
3. **Mercato target identificato**: Regione Liguria + PC + cooperative pilota = anchor commerciale credibile
4. **Modello di business coerente**: service-only DaaS/canone/ore-volo (boundary B1)
5. **Asset riusabili 6A → 6B**: ~30-40% del CapEx Y1 in valore monetario riutilizzabile in Phase B HALE
6. **Capital intensity gestibile**: €700k-2M Y1 con mix grant 35-55% + equity 25-45%
7. **Tempistiche realistiche**: 12 mesi MVP, gate G4 strutturato

### 10.3.2 Condizioni per il Go (entry criteria gate M+12)

Il verdetto Go Condizionato è **subordinato** al raggiungimento delle seguenti condizioni:

> **⚠️ Caveat probabilistico onesto (post Audit Red Team M+3)**: il verdetto "Go Condizionato" ha probabilità di trasformarsi in **Go pieno** al M+10/M+11 stimata effettivamente ~**15-35%** (non 60-80% come potrebbe suggerire una lettura ottimistica). Le 5 hard conditions sotto sono in AND logico: la P(tutte soddisfatte simultaneamente) è il prodotto delle probabilità marginali. Scenario base atteso: **Hold con piano di mitigazione** in 60-80% dei percorsi, con re-review M+13-14. Lo scenario "Go pieno immediato" richiede esecuzione perfetta multi-stakeholder + nessuno slittamento ENAC. Vedi `AUDIT-QUALITY-VOLUME-1.md` §6 per il calcolo dettagliato.

**Hard conditions** (vincolanti, no-Go se mancanti):
- ☐ **C1**: LoI o accordo formale Regione Liguria firmato entro M+9
- ☐ **C2**: Autorizzazione SORA ENAC operativa entro M+9
- ☐ **C3**: Mix funding ≥ 60% committed (Coopfond + Regione + equity + R&D credit) entro M+10
- ☐ **C4**: ≥ 8 cooperative pilota su 10 confermano partecipazione formale entro M+6
- ☐ **C5**: Pre-application meeting ENAC con feedback documentato entro M+3-6

**Soft conditions** (raccomandate, no blocking ma trigger review):
- ☐ S1: DPIA pubblica preliminare entro M+6
- ☐ S2: Vendor quotation confermato (JOUAV + Plan B Tekever) entro M+3
- ☐ S3: Workshop comunità Pentema con feedback positivo entro M+6
- ☐ S4: Partnership intent letter CIRA (per Phase B 6B) entro M+9
- ☐ S5: Almeno 1 LoI per espansione 2nda regione SNAI entro M+12

### 10.3.3 Scenari alternativi se condizioni non soddisfatte

Se al M+10/M+11:
- **C1-C2-C3 tutte soddisfatte** → **GO pieno** verso operatività Y1 M+12
- **C4-C5 mancanti, ma C1-C3 OK** → **GO Condizionato** con re-check M+13
- **C1 (LoI Regione) mancante** → **HOLD** automatico con re-review M+14 per cercare anchor alternative (es. Regione Piemonte, Calabria)
- **C2 (SORA) mancante** → **HOLD** con re-application + scope adjustment (VLOS solo Y1)
- **C3 (funding) < 40%** → **HOLD** con bridge financing strategy
- **C4 (cooperative) < 6 su 10** → **HOLD + workshop urgenza** per re-confirm impegni

---

## 10.4 Verdetto Percorso 6B — Hold / Go Condizionato Estremo

### 10.4.1 Argomenti a supporto del Hold (non No-Go)

1. **Concept tecnicamente plausibile**: HALE solare 80-150 kg MTOW con energy balance estate OK
2. **Lineage tecnologico italiano disponibile**: POLITO DIMEAS (HELIPLAT history) + CIRA EuroHAPS-adjacent
3. **Riferimenti internazionali esistenti**: Zephyr AALTO, Skydweller, PHASA-35 dimostrano fattibilità in scala simile
4. **Boundary B2 (visione EU sovereign) richiede** un Percorso 6B preparatorio per non perdere il vettore strategico
5. **Funding sovrano EU disponibile** in trajectory (EDF + Horizon + PNRR + potenzialmente futuro programma sovrano stratosferico)

### 10.4.2 Argomenti a supporto del No-Go (rigettati)

Argomenti che potrebbero portare a un No-Go diretto, e nostra risposta:

| Argomento No-Go | Risposta |
|---|---|
| "Energy balance inverno < 15% margin → progetto perennial impossibile" | Vero per perennial. **Fallback seasonal-only** (operatività marzo-ottobre) resta robusto e commercialmente valido. No-Go non giustificato. |
| "Framework HAPS EU non esiste, perdiamo 5+ anni per certificazione" | Vero. Mitigation: parallel ops 6A genera revenue + esperienza + engagement EASA in parallelo. No-Go non giustificato; **Defer 6B 1-2 anni** se necessario. |
| "Capital intensity €10-30B per scala EU sovereign è oltre nostre possibilità" | Vero. Boundary B2 mantiene visione, ma **lo Studio non approva Fase 5 oggi**. Solo Fase 3 R&D è in scope. No-Go non giustificato. |
| "Competitor Tier 1 (AALTO/Skydweller) sono troppo avanti" | Vero in capacità assoluta. Differenziazione Firmamento è geografica + cooperativa + sovranità italiana, non scale assoluta. No-Go non giustificato. |

### 10.4.3 Condizioni per Go Phase B (gate G5 — M+24)

Il commitment Phase B 6B è subordinato al raggiungimento, al gate G5 (M+24), delle seguenti condizioni:

**Hard conditions Phase B**:
- ☐ **C-6B-1**: Pilota 6A ha raggiunto KPI gate G4 (≥ 3 contratti + ≥ €200k revenue + 0 FATAL)
- ☐ **C-6B-2**: Funding mix Phase B ≥ 50% committed (EDF + Horizon + PNRR / equity Series B) al M+24
- ☐ **C-6B-3**: Engagement EASA aperto: o (a) RMT HAPS aperto, o (b) Special Condition path in dialogo
- ☐ **C-6B-4**: Energy balance simulazione completa con scenari decisi (perennial vs seasonal) entro M+10
- ☐ **C-6B-5**: Partnership formalizzata con almeno un partner R&D italiano (CIRA preferito; POLITO DIMEAS secondario)

**Soft conditions Phase B**:
- ☐ S-6B-1: Posizionamento Firmamento in ASD-Eurospace HAPS working group
- ☐ S-6B-2: Position paper "Italian Stratospheric Sovereignty" pubblicato
- ☐ S-6B-3: Engagement DG CNECT + DG DEFIS per allineamento IRIS² complementarity

### 10.4.4 Scenari alternativi Phase B

Se al gate G5 (M+24):
- **Tutte C-6B soddisfatte** → **GO Phase B** pieno (€5.5-13.5M, M+24-48)
- **3 su 5 soddisfatte** → **GO Phase B ridotto** (focus subscale + simulazione, no full prototype)
- **Funding < 30%** → **DEFER 6B** a M+36 con re-review
- **EASA framework chiuso o RMT non aperto entro 2028** → **Hold permanente** 6B fino a 2030+, focus esclusivo su 6A scale-up
- **Pilota 6A failed (<€100k revenue Y1)** → **No-Go 6B** (incompatibile con strategia ladder)

---

## 10.5 Verdetto Aggregato per la Visione 10 Anni

Lo Studio approva:
- ✅ **Fase 1 — VTOL Pilota Pentema** (Y1 = M+12)
- ✅ **Fase 2 — Scale-up Liguria + 1 regione SNAI** (Y2-Y3 = M+12-36) **condizionato a gate G4 (M+12) successo**
- ⚠️ **Fase 3 — HALE Prototipo R&D Phase B** (Y3-Y5 = M+24-60) **condizionato a gate G5 (M+24) successo**

Lo Studio **NON approva, ma preserva come vettore strategico**:
- 🎯 **Fase 4 — Costellazione italiana iniziale** (Y6-Y8) — decisione a gate G6 (M+36) e oltre
- 🎯 **Fase 5 — Consorzio EU stratospheric layer** (Y8-Y10) — decisione a gate futuri post-G6

I gate G4, G5 e oltre sono i punti di verifica formali per il proseguimento.

---

## 10.6 Red Team — Critica Combinata al Verdetto

Critica aggregata da `red-team-skeptic` + `regulatory-adversary` + `competitor-intelligence` + `business-model-strategist` + `financial-cfo-analyst`.

### Critica 1 — "Go Condizionato 6A è troppo morbido: hard conditions C1-C5 sono ambizione, non realismo"
**Razionale**: 5 hard conditions tutte da soddisfare al M+9-10 = AND di probabilità ~70%-90% ognuno → P(tutte) ~25-60%. Significa che ~40% scenario è Hold, non Go.
**Risposta**: confermato. La raccomandazione "Go Condizionato" significa esattamente questo: "Go subordinato a conditions, altrimenti Hold". Il punto del gate è **garantire che decisione Go pieno avvenga solo con condizioni**. Confidence verdetto: medium-high *condizionato* alle conditions.

### Critica 2 — "Hold 6B preserva la visione ma non risolve i 5 showstopper"
**Razionale**: ammettere 5 rischi rossi e proseguire (anche solo R&D) è capital-intensive in modo speculativo. Forse meglio Defer 6B 2-3 anni e investire solo in 6A scale-up.
**Risposta**: parzialmente corretto. La Phase B 6B è R&D, **non manufacturing né operazioni commerciali**. È esattamente la fase dove si dovrebbero risolvere i showstopper. Defer 6B 2-3 anni significa **perdere il vettore B2** (EU sovereign window of opportunity 2028-2032). Il Hold con condizioni stringenti al gate G5 (no Phase B se conditions non soddisfatte) è il bilanciamento corretto tra "preservare il vettore" e "non spendere male".

### Critica 3 — "Boundary B2 (EU sovereign) è preservata ma capital intensity €10-30B fa diventare lo Studio una fantasia"
**Razionale**: includere capital intensity scenarios fino a €30B in uno Studio di una PMI italiana è surreale. Riduce la credibilità del documento.
**Risposta**: il numero €10-30B è dichiarato **per scenario "EU sovereign full scale 100+ HAPS"** e dichiarato **precondizione esterna** (programma analog IRIS²). Lo Studio non chiede questi soldi. Lo Studio richiede €0.7-2M Y1 + €5.5-13.5M Phase B. Il number grande serve a **dichiarare onestamente** dove porta la visione 10 anni, non a chiedere finanziamento. Boundary B2 mantenuta come vettore, non come operativa.

### Critica 4 — "Survivor bias: citate Zephyr/Skydweller/PHASA-35 senza menzionare i programmi falliti"
**Razionale**: NASA Helios, Aalto HAWK30, Solara 50, Sanswire — tutti falliti. Base rate HALE solari ~30% successo. Lo Studio non incorpora questa base rate nelle confidence.
**Risposta**: il survivor bias è dichiarato in Cap. 7 §7.1.2 + Cap. 6 §6.0 (lista programmi falliti). Confidence baseline 6B = low-medium proprio per riflettere la base rate. La raccomandazione Hold riflette questa cautela.

### Critica 5 — "Verdetto Go Condizionato è 'CYA decisionale': non commetterà mai un errore perché ha hedge ovunque"
**Razionale**: vagheggiare un verdetto che dice "Go se tutto va bene, altrimenti Hold" non è una decisione, è una postura.
**Risposta**: corretto in parte. La differenza tra Go Condizionato e Hold:
- **Go Condizionato** = "procediamo nell'implementazione, raggiungiamo le conditions, se al M+12 raggiunte → operations Y1"
- **Hold** = "non procediamo, attendiamo evidenze, re-review tra 30-60 giorni"

Go Condizionato è una **decisione attiva di procedere con piano di mitigation specificato**. Hold è una **decisione passiva di attendere**. Il verdetto Go Condizionato è la scelta corretta perché lo Studio dimostra che le condizioni sono raggiungibili con effort ragionevole entro M+9-10.

### Critica 6 — "Manca una sezione 'cosa scartiamo'"
**Razionale**: lo Studio non esplicita scelte che NON facciamo (es. "non sviluppiamo dirigibili", "non concorriamo con AALTO scale", "non vendiamo a Difesa pura").
**Risposta**: corretto. Implicito in boundary B1+B2 ma da esplicitare in §10.7 (aggiunto).

---

## 10.7 Cosa Esplicitamente NON Facciamo (per chiarezza)

In coerenza con boundary B1+B2 e con il verdetto, lo Studio dichiara esplicitamente che Firmamento Technologies **non**:

- **Non vende velivoli** né asset hardware (boundary B1). Tutto è erogazione di servizi.
- **Non concorre con Tier 1 globale HAPS** (AALTO/Skydweller/PHASA-35) in scala assoluta. Si differenzia per geografia + cooperative + sovranità.
- **Non costruisce dirigibili** (HHAA CIRA EuroHAPS è un'altra strada). Focus su HALE solare ala fissa.
- **Non opera in difesa pura** (può fare dual-use civile, ma non target Difesa primario nel piano M+0-48).
- **Non promette "alternativa Starlink europea"** nel linguaggio pubblico (boundary B2 RSK-GEO-001).
- **Non sviluppa Type Certificate proprio** in autonomia (richiede consorzio + EASA + 5-8 anni).
- **Non opera retail B2C** (target B2G + B2B).
- **Non sostituisce satelliti EO** (modello complementare a Sentinel/Copernicus, non sostitutivo).
- **Non promette ROI immediato** (R&D phase Y3-Y5 senza revenue commerciale 6B).

---

## 10.8 Decisione Formale e Action Items Immediati

### 10.8.1 Decisione formale richiesta al CdA + sponsor

| Decisione | Status |
|---|---|
| Approva Studio di Fattibilità M+11 | ☐ |
| Approva GO CONDIZIONATO Percorso 6A | ☐ |
| Approva HOLD Percorso 6B con commitment Phase B subordinato a G5 | ☐ |
| Approva budget Y1 6A (CapEx €0.7-2M, mix funding raccomandato) | ☐ |
| Approva engagement plan istituzionale Cap. 5.11.3 | ☐ |
| Approva versionamento progressive RTM v0.5 → v1.0 | ☐ |
| Approva master schedule M+12 → M+48 | ☐ |

### 10.8.2 Action items immediati post-Gate G3 (M+11 → M+12)

**Per il management Firmamento**:
1. ☐ Firma contratto Coopfond per Y1 entro M+11
2. ☐ Chiusura LoI Regione Liguria (DGR formale) entro M+12
3. ☐ Acquisto piattaforma VTOL (Plan A JOUAV o Plan B Tekever) entro M+12
4. ☐ Submission SORA application ENAC se non già fatta entro M+11
5. ☐ Workshop pubblico comunità Pentema (governance condivisa) entro M+12
6. ☐ Formalizzazione governance Firmamento + 10 cooperative (contratto di rete vs RTI)

**Per il team operativo**:
7. ☐ Set-up GS Pentema entro M+12
8. ☐ Training pilota UAS BVLOS entro M+12
9. ☐ DPIA pubblica preliminare submitted entro M+11

**Per la fase Phase B 6B (preparatoria, no commitment manufacturing)**:
10. ☐ Engagement letter CIRA entro M+12
11. ☐ Engagement letter POLITO DIMEAS entro M+12
12. ☐ Position paper "Italian Stratospheric Sovereignty" pubblicato entro M+12
13. ☐ Engagement EASA Innovation Network entro M+9-12

---

## 10.9 Considerazioni di Chiusura

Il presente Studio di Fattibilità è il **primo passo formale** del progetto Firmamento Technologies. Il verdetto Go Condizionato 6A + Hold 6B è **deliberatamente prudente**: non si tratta di una corsa né a costruire UAV né a inseguire Starlink, ma di **costruire una infrastruttura di servizi italiana per le Aree Interne** con un vettore strategico chiaro verso un futuro consorzio EU.

Il successo del progetto si misurerà a tre livelli:

1. **Livello micro (M+12)**: il pilota Pentema deve generare ≥ €200k di revenue ricorrente e dimostrare la validità del modello service-only.
2. **Livello meso (M+36)**: la scala multi-regione SNAI deve raggiungere ARR € 1.5-3.5M e attivare la Phase B HALE.
3. **Livello macro (M+120 e oltre)**: il posizionamento Firmamento come "principal Italian node" di un futuro consorzio EU sovereign stratosferico, complementare a IRIS², con capability dimostrata.

Per ognuno di questi livelli il presente Studio fornisce evidenze, requisiti, e gate decisionali. Le decisioni finali al CdA + sponsor sono ora le seguenti:

> **Verdetto finale Studio di Fattibilità M+11**:
>
> ✅ **Percorso 6A — GO CONDIZIONATO**
> ⚠️ **Percorso 6B — HOLD / GO CONDIZIONATO ESTREMO R&D**
>
> **Action richiesta**: approvazione formale CdA + sponsor + avvio immediato fase operativa M+12.

---

## 10.10 Riferimenti

[^1]: NASA SE Handbook Rev 2 — §3.0 Project Life Cycle Reviews. Source: `fonti/NASA04. SysEng Handbook (NASA_SP-2016-6105 Rev 2).md`.

[^2]: D.Lgs. 36/2023 art. 41 — gate review framework PFTE. Source: `fonti/2023_0036.md`.

[^3]: Skill `gate-review-checklist` + `epistemic-rigor` + `red-team-skeptic`.

[^4]: Tutti i Cap. 1-9 e 11 dello Studio di Fattibilità sono fonti per le evidenze citate nel presente capitolo.

[^5]: Risk Register completo (Vol. 2 Allegato A.2) per dettaglio showstopper.

---

## 10.11 Note di chiusura del capitolo

Il Cap. 10 è la **sintesi conclusiva** dello Studio di Fattibilità. È redatto per essere portato al gate review M+11 e alle decisioni formali del CdA + sponsor (Coopfond + Regione Liguria).

Il verdetto è coerente con boundary B1+B2 e con la disciplina epistemica del progetto. Le condizioni del Go Condizionato sono dichiarate ed verificabili. I showstopper sono formalmente registrati e mappati al gate review.

Il capitolo è **chiuso al M+11** (proiezione) con il verdetto finale dello Studio di Fattibilità.
