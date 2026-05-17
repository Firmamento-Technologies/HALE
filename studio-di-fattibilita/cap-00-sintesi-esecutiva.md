# Capitolo 0 — Sintesi Esecutiva

> **Studio di Fattibilità — Piattaforma Aerea HALE / VTOL per Aree Interne**
> Firmamento Technologies — bando Cooding Prototypes (Coopfond / Legacoop)
> Volume 1, Capitolo 0
>
> **Destinatari:** CdA Firmamento Technologies, Coopfond, Regione Liguria, MIMIT, ENAC, EASA, finanziatori, stakeholder istituzionali
> **Versione:** bozza M+11 (proiezione finale Studio)
> **Lunghezza target:** 5-8 pagine A4

---

## 0.1 Il Progetto

**Firmamento Technologies** propone lo sviluppo e l'attivazione di una **piattaforma aerea unmanned**, operata come **erogatore di servizi** (non come venditore di velivoli), a beneficio delle **Aree Interne italiane** — territori a bassa densità demografica, orografia complessa, carenza di servizi essenziali e divario digitale strutturale.

Il presente Studio di Fattibilità è redatto in conformità all'**art. 41 D.Lgs. 36/2023** + Allegato I.7 (Codice dei Contratti Pubblici), con metodologia derivata dal **NASA Systems Engineering Handbook Rev 2** e dai template italiani autoritativi (**ENAC AAM Business Plan 2021-2030**, **MIMIT prefattibilità aero**, **DTA Puglia Studio Grottaglie**).

**Caso pilota**: frazione di **Pentema (Comune di Torriglia, Genova)**, area SNAI riconosciuta nel ciclo 2021-2027 (Valli dell'Antola e del Tigullio), in Regione Liguria — laboratorio italiano per le politiche pubbliche delle Aree Interne.

**Rete di utenti-pilota**: **10 cooperative** aderenti a Legacoop, con **Fabrica** come capofila. Le cooperative sono utenti + co-progettiste + custodi di fabbisogni operativi reali.

---

## 0.2 Strategia Duale (Percorso 6A + 6B)

Il progetto adotta una **strategia duale a riduzione del rischio**:

### 🚁 Percorso 6A — VTOL Pilota Pentema (operativo, 0-12 mesi)

**Tecnologia**: piattaforma commerciale Vertical Take-Off and Landing **TRL 8-9** (baseline JOUAV CW-30E con Plan B Tekever AR3 ITAR-free EU), payload modulare EO + IR + telecom backup.

**Casi d'uso target**:
1. Monitoraggio rischio idrogeologico (frane, dissesto) — Regione Liguria + Protezione Civile
2. Antincendio boschivo (early detection ≤ 5 min) — VVF + Carabinieri Forestali
3. Connettività di emergenza — PC + Comune Torriglia
4. Mapping infrastrutture rurali — Comuni SNAI
5. Servizi alle cooperative (agricolo, forestale) — rete Legacoop

**Budget**: CapEx Y1 **€700k – €2M** (incluse IVA + contingency 15%). **OpEx run-rate Y2 RECONCILED post Cap. 5 §5.17**: **€1.18M/anno centrale (range €1.05-1.30M)** — include €260-480k baseline tecnico + €400-590k regulatory team mandatory (CISO + DPO + Head Regulatory) + €115-230k overhead amministrativo. Il legacy €260-480k/anno è solo OpEx tecnico, NON sufficiente operativamente post Cap. 5 §5.17 (5+1 critical regolatori: Part-IS, AgID/PSN, NIS2, art. 50, ENAV, EUROCONTROL).

**Revenue Y1 baseline RECALIBRATED post-Cluster D audit (M+3)**: **€260k centrale (range €220-300k)** da 5 contratti pluriennali, min SyR-Cost-003 €200k. **Soglia minima**: €200k (SyR-Cost-003 hard floor). **Pricing PA**: €60-90k/anno base + €30-60k/anno premium persistence/sovranità (post-falsificazione baseline originale €150k/anno → €355-405k da Cluster D benchmark Planetek/e-GEOS/NHazca: €30-80k/anno). Dettaglio Cap. 7 §7.4.4-5 + §7.8.2.

### 🛰 Percorso 6B — HALE Stratosferico (R&D, 24-48+ mesi)

**Tecnologia**: piattaforma **High Altitude Long Endurance** solare, apertura 25-30 m, MTOW 80-150 kg, quota operativa 18-21 km (FL590-690), endurance target ≥ 30 giorni perennial estate (Y3) / 12 mesi target (Y5).

**Casi d'uso target post-pilota**:
- Osservazione persistente persistente del territorio (EO multispettrale)
- Connettività NTN 5G NR (3GPP Rel-17/18 regenerative gNB)
- Servizi dual-use civile-difesa (potenziale, condizionato)

**Budget Phase B R&D**: **€5.5-13.5M** (M+24 → M+48), con mix 50-75% grant pubblico (EDF + Horizon + PNRR + ASI).

---

## 0.3 Verdetto dello Studio

### ⚠️ Percorso 6A — **HOLD CON PIANO REGOLATORIO RAFFORZATO** (scenario base default, P 45-60%) / **GO CONDIZIONATO** (scenario ottimistico, P 5-15%)

> **Caveat probabilistico onesto** (post audit M+3): le 5 hard conditions sotto sono in AND logico. P(AND tutte) realistica al gate G3 = **5-15%** (Go pieno) vs **45-60%** (Hold con piano + re-review M+13-16). Scenario base atteso = HOLD CON PIANO RAFFORZATO. Per dettaglio vedi Cap. 10 §10.0bis.

**Tecnicamente, regolatoriamente, di mercato e finanziariamente fattibile** entro l'orizzonte di 12 mesi. Il verdetto è subordinato alle seguenti **condizioni vincolanti** (gate M+10-12):
- LoI/accordo formale Regione Liguria firmato entro M+9
- Autorizzazione SORA ENAC SAIL II-III BVLOS operativa entro M+9
- Mix funding ≥ 60% committed entro M+10
- ≥ 8 cooperative pilota su 10 confermano partecipazione formale entro M+6
- Pre-application meeting ENAC con feedback documentato entro M+3-6

### ⚠️ Percorso 6B — **HOLD CON CRITERI DI USCITA ESTREMAMENTE STRINGENTI** + Pivot Strutturale

**Pivot strategico post audit M+3** (DR-013 + DR-014):
- Base rate 0% HALE solari commerciali operativi in 22 anni (12 programmi falliti analizzati)
- Capital intensity benchmark internazionale $50M-1B per programma → Firmamento €5.5-13.5M = **R&D Phase 0/A only**, NON percorso completo a operatività
- **Pivot raccomandato**: da "HALE proprietario Firmamento" a **"Firmamento operatore di servizi su piattaforme prime contractor"** (Aalto/Sceye/Skydweller/CIRA-EuroHAPS-successor)

Fattibilità tecnologica plausibile ma con **5 showstopper aperti**:
- **RSK-TEC-001**: energy balance HALE inverno 44°N **margine reale -50.1% DEFICIT** (simulazione completa allegato A.7 supera la stima hand-calc "0-15% critico"); **E5 Seasonal-only (marzo-ottobre) mandatory plan A**; perennial 44°N NON fattibile con tech baseline 2026-2028 — score RSK aggiornato a 25
- **RSK-TEC-002**: aeroelasticità ala high-AR
- **RSK-REG-001**: assenza framework regolatorio HAPS EU (EASA Special Condition non ancora aperto)
- **RSK-FIN-001**: funding Phase B €5.5-13.5M non commitato al M+11
- **RSK-TEC-003**: tempi Type Certification HALE > 5 anni

Phase B R&D autorizzata **subordinatamente** al raggiungimento delle conditions al gate G5 (M+24), inclusi funding mix ≥ 50% pubblico e engagement EASA aperto.

---

## 0.4 Visione 10 Anni

Posizionamento strategico target: **nodo italiano fondatore di una futura infrastruttura sovrana europea HAPS**, complementare a **IRIS²** (LEO sovereign EU) e a Galileo/Copernicus.

**Linguaggio pubblico**: "complementare a IRIS²", **mai** "alternativa europea a Starlink" (per ragioni geopolitiche dichiarate in documento riservato).

**5 fasi della visione**:
1. **Y1**: Pilota Pentema VTOL — pilot validato + revenue €200-400k
2. **Y2-Y3**: Scale-up SNAI Italia (3-4 regioni, flotta 3-8 VTOL/MALE) + R&D HALE subscale
3. **Y3-Y6**: Primo HALE prototipo operativo italiano + servizio commerciale HAPS pilota
4. **Y6-Y8**: Costellazione italiana 3-10 HAPS + servizi NTN + EO persistente
5. **Y8-Y10**: Consorzio EU stratospheric layer (Italia + FR/DE/ES) + posizionamento ufficiale "EU sovereign stratospheric layer" complementare IRIS²

**Capital intensity 10 anni dichiarata onestamente**: **€500M – €2B** scenario "small fleet" (5-10 HAPS) / **€10-30B** scenario "EU sovereign full scale" (100+ HAPS, richiede programma EU equivalente IRIS² come precondizione esterna).

Lo Studio approva **solo Y1-Y3** (Fasi 1+2). Le fasi 3-5 sono **vettore strategico mantenuto**, decisione formale ai gate G5 (M+24), G6 (M+36), e oltre.

---

## 0.5 Modello di Business

Boundary condition strutturale: **service-only, no product sale**.

- Linee di servizio: monitoraggio EO + connettività emergenza + analytics — erogate come **canone fisso**, **ore-volo + analytics**, **outcome-based**, **DaaS** (Data-as-a-Service).
- Canali distributivi prevalenti: **B2G regionale** (anchor Regione Liguria), **B2G locale** (PC, ARPA, Enti Parco), **B2B cooperative** (rete Legacoop scaled).
- 4 pilastri vantaggio competitivo: (i) specializzazione geografica Aree Interne, (ii) modello cooperativo, (iii) sostenibilità + narrativa ESG (propulsione 100% solare/elettrica + fibra di lino in strutture secondarie), (iv) approccio incrementale VTOL → MALE → HALE che produce **asset riusabili 30-40%** del CapEx Y1.

---

## 0.6 Quadro Normativo

Lo Studio è conforme a:
- **D.Lgs. 36/2023 art. 41 + Allegato I.7** (Codice Contratti Pubblici)
- **Reg. (UE) 2019/947 + 2019/945** (UAS Operations + Design)
- **EASA AMC/GM Issue 1 Amendment 3** (settembre 2025) — versione europea **SORA 2.5**
- **ENAC Regolamento Mezzi Aerei a Pilotaggio Remoto Ed. 3 + Emend. 1**
- **Reg. (UE) 2021/664** + **ENAC LG-2023/006** (U-Space)
- **GDPR + D.Lgs. 196/2003 novellato** (privacy)
- **NIS2 + D.Lgs. 138/2024** (cybersecurity)
- **AS/EN 9100 + ISO 9001** (sistemi di gestione qualità aerospace)

Strategia regolatoria 6A: **Specific Category** SAIL II-III BVLOS, SORA application + Operations Manual + Operator Declaration ENAC. Strategia 6B: **Certified Category** via Special Condition HAPS negoziata con EASA (5-8 anni timeline tipica).

---

## 0.7 Stakeholder Critici

| # | Stakeholder | Ruolo | Commitment richiesto |
|---|---|---|---|
| 1 | **Regione Liguria** | Anchor customer + sponsor istituzionale | LoI/DGR formale entro M+9 |
| 2 | **Coopfond + Legacoop** | Finanziatore primary + governance cooperative | Contratto Cooding + Cooding-Invest |
| 3 | **Rete 10 cooperative (Fabrica capofila)** | Utenti-pilota + co-progettisti | ≥ 8 su 10 confermano partecipazione M+6 |
| 4 | **Comune Torriglia + Comunità Pentema** | Sede pilota + accettabilità sociale | Delibera comunale + workshop comunità |
| 5 | **Protezione Civile Liguria + ARPA Liguria** | Cliente operativo primario | Convenzione operativa + protocollo |
| 6 | **ENAC** | Regolatore aviazione civile | Autorizzazione SORA SAIL II-III BVLOS |
| 7 | **EASA** | Regolatore europeo | Engagement Innovation Network HAPS framework |
| 8 | **AGCOM** | Regolatore spettro radio | Licensing temporaneo bande ISM o commerciali |
| 9 | **Garante Privacy** | Regolatore protezione dati | DPIA pubblica preliminare M+6 |
| 10 | **CIRA** | Partner R&D potenziale Phase B 6B | Letter of intent M+9-12 |

---

## 0.8 Risk Aggregato

**Percorso 6A**: nessun rischio rosso (showstopper). 5 rischi gialli con mitigation plan chiaro. Profilo rischio: medio-basso. Compatibile con Go Condizionato.

**Percorso 6B**: **5 showstopper rossi** (energy balance inverno, aeroelasticità, framework HAPS, funding Phase B, Type Certification timeline). Mitigation strategy esiste ma non garantita. Profilo rischio: alto. Compatibile con Hold / Go Condizionato Estremo.

---

## 0.9 Finanziamento

### Mix raccomandato Y1 Percorso 6A (€0.75-1.75M target)
- **Coopfond Cooding Prototypes 2026**: €50k (max), 5% mix
- **Coopfond Cooding-Invest**: €150-300k, 15-20%
- **Regione Liguria FESR 2021-2027**: €300-500k, 25-40%
- **PNRR Aerospazio / IS4Aerospace**: €0-300k, 0-20%
- **Equity privato (founder + seed)**: €200-500k, 25-35%
- **R&D tax credit (L. 160/2019)**: €50-150k, 5-15%

### Mix Phase B 6B (€5.5-15.5M target, M+24-48)
- **EDF** call HAPS post-EuroHAPS: €2-5M, 30-40%
- **Horizon Europe Cluster 4/5**: €1-3M, 15-25%
- **PNRR Aerospazio / ASI / MIMIT**: €1-2.5M, 15-20%
- **Equity privato Series A/B**: €1-2.5M, 10-25%
- **R&D tax credit + Patent Box**: €0.5-1.5M, 5-10%

---

## 0.10 Cronoprogramma e Gate

```
M+0   M+3   M+6   M+10/11   M+12         M+24            M+36            M+48
│     │     │     │         │            │               │               │
│ G0  │ G1  │ G2  │ G3       │ G4         │ G5            │ G6            │ Phase B end
│     │     │     │ ★ FEAS   │            │               │               │
│           │     │ VERDICT  │            │               │               │
│  STUDIO DI FATTIBILITÀ    │  PILOTA 6A VTOL OP         │   R&D 6B HALE PHASE B           │
```

**Gate principali**:
- **G3 (M+10-11)** ⭐ — **FEASIBILITY GATE PRIMARIO** — verdetto Go / Hold / No-Go per ciascun percorso (oggetto del presente Studio)
- **G4 (M+12)** — fine pilota VTOL 6A, decisione scale-up SNAI
- **G5 (M+24)** — decisione Phase B 6B Go / Defer
- **G6 (M+36)** — Phase B HALE midterm review

---

## 0.11 Numeri Chiave

| Metric | Valore |
|---|---|
| Durata Studio di Fattibilità | 11 mesi (M+0 → M+11) |
| Durata pilota 6A | 12 mesi (M+0 → M+12), operativo da M+9 |
| Durata Phase B 6B R&D | 24 mesi (M+24 → M+48) |
| CapEx 6A Y1 | €700k – €2M |
| OpEx 6A Y2 run-rate (RECONCILED post Cap. 5 §5.17) | €1.18M/anno centrale (range €1.05-1.30M); legacy "tecnico-only" €260-480k/anno NON sufficiente operativamente |
| Revenue 6A Y1 baseline (RECALIBRATED) | €260k centrale, range €220-300k (min €200k SyR-Cost-003) — post-Cluster D audit |
| ARR Y3 target | €1.5-3.5M (scale-up Liguria + 1 regione) |
| ARR Y5 target | €3-8M (multi-regione + HAPS subscale) |
| Break-even cumulato | Y4-Y5 (scenario base) |
| NPV 10y scenario base | +€3-8M |
| IRR 10y scenario base | 18-25% |
| Payback semplice | 4-6 anni |
| Capital intensity Y10 small fleet | €500M – €2B |
| Capital intensity Y10 EU sovereign | €10-30B (precondizione esterna) |
| 10 cooperative pilota | Fabrica capofila + 9 aderenti |
| Stakeholder mappati | 30 |
| StNeeds baseline | 17 |
| System Requirements | 42 |
| Subsystem Requirements | ~80 (sample, ~200 in v1.0) |
| Showstopper formali | 5 (tutti su 6B) |
| Falsifying observations dichiarate | ~40 (totale Volume 1) |
| Citazioni autoritative | ~200 (totale Volume 1) |

---

## 0.12 Decisione Richiesta

Ai destinatari del documento (CdA + Coopfond + Regione Liguria + altri sponsor) è richiesto:

1. ☐ **Approvazione formale dello Studio di Fattibilità** Volume 1+2+3
2. ☐ **Approvazione GO CONDIZIONATO Percorso 6A** con piano di attivazione M+12
3. ☐ **Approvazione HOLD / GO CONDIZIONATO ESTREMO Percorso 6B** con commitment a gate G5 (M+24)
4. ☐ **Approvazione budget Y1 6A** (CapEx + OpEx + mix funding)
5. ☐ **Approvazione engagement plan istituzionale** Cap. 5.11.3
6. ☐ **Approvazione master schedule** M+12 → M+48

---

## 0.13 Riferimenti

Per il dettaglio di ciascun argomento, vedere i Cap. 1-11 del presente Volume 1, gli Allegati Tecnici del Volume 2, e i Riferimenti bibliografici del Volume 3.

Documenti di contesto:
- `riferimenti/visione-10-anni.md` — vettore strategico 10 anni
- `riferimenti/analisi-fac-simili-IT.md` — mappatura art. 41 + NASA SE
- `riferimenti/ricerche-approfondite.md` — dataset di ricerca
- `riferimenti/audit-rigore-epistemico.md` — audit confidence levels + debito di rigore

Documento riservato (accesso ristretto, non parte dello Studio pubblico):
- `riferimenti/RESERVED-rischi-geopolitici.md` — 5 rischi geopolitici e mitigation strategie

---

## 0.14 Verdetto in Una Riga

> **Lo Studio di Fattibilità raccomanda**: scenario base **HOLD CON PIANO REGOLATORIO RAFFORZATO** Percorso 6A (P 45-60%, re-review M+13-16; eventuale GO pieno P 5-15% solo se 5 hard conditions soddisfatte simultaneamente M+10-11) + **HOLD CON CRITERI USCITA STRINGENTI** Percorso 6B con **pivot strutturale** verso "operatore di servizi su piattaforme prime contractor" (R&D Phase 0/A M+24-48 subordinato a gate G5, NON path autonomo a operatività). Posizionamento strategico 10 anni: "complementare a IRIS²", scenario realistico B2-relaxed "Standalone IT Operator Small Fleet €30-80M ARR Y10" (P 30-50%) vs B2 full "EU sovereign stratospheric layer 100+ HAPS" (P 6-15%).

---

*Firmamento Technologies — Studio di Fattibilità HALE/VTOL — Volume 1 Capitolo 0 — Bozza M+11 — Maggio 2026*
