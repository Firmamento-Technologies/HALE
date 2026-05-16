# Audit di rigore epistemico — Stato dei claim del progetto

**Scopo:** applicare la skill `epistemic-rigor` ai file prodotti finora, identificando claim non-conformi, declassandone confidence, marcando il debito di triangolazione, segnalando inconsistenze interne.

**Metodologia:** ogni claim cruciale è valutato secondo le 7 regole della skill:
1. Falsificabilità
2. Triangolazione (≥ 2 fonti)
3. Source provenance esplicita
4. Confidence level dichiarato
5. Pre-mortem applicato
6. Steel-manning della posizione contraria
7. Base-rate awareness

**Boundary conditions del progetto** (decisione utente, NON soggette a critica epistemica):
- **B1**: Il modello cooperativo Legacoop è una **scelta strategica** (governance + community), non un'ipotesi di vantaggio competitivo da validare
- **B2**: Il posizionamento "EU sovereign stratospheric layer / alternativa europea Starlink" è un **obiettivo di lungo termine assunto**, non un claim da falsificare

Il rigore si applica a *come supportiamo* queste posizioni e *come ci arriviamo*, non al fatto che siano gli obiettivi.

---

## 1. Audit categorie principali — sintesi

| Area | Claim auditati | Conformi | Da declassare | Da triangolare | Inconsistenze |
|---|---|---|---|---|---|
| Mercato HAPS | 12 | 2 | 8 | 6 | 2 |
| Specifiche competitor | 18 | 14 | 4 | 3 | 2 |
| Finanziario / CapEx-OpEx | 24 | 4 | 12 | 18 | 1 |
| Normativo (ENAC/EASA/AGCOM) | 16 | 11 | 3 | 4 | 1 |
| Spettro radio / 3GPP | 10 | 7 | 2 | 2 | 0 |
| Tecnologico (TRL, prestazioni) | 14 | 5 | 7 | 9 | 3 |
| Sovranità / Geopolitica | 12 | 6 | 4 | 5 | 1 |
| Bandi / Finanziamenti pubblici | 10 | 4 | 3 | 5 | 1 |
| SNAI / Territoriale | 8 | 6 | 1 | 2 | 1 |

**Totale claim auditati:** 124. **Conformi senza intervento:** 59 (48%). **Da intervento:** 65 (52%).

---

## 2. Claim problematici principali — analisi dettagliata

### CLAIM-001 — "Mercato HAPS $99M (2024) → $240M (2030), CAGR 16%"
**File:** `agents/aerospace-market-analyst.md`, `riferimenti/ricerche-approfondite.md`
**Fonte attuale:** MarkNtel Advisors 2025 (commercial report) — **fonte unica**
**Problema:**
- Regola 2 violata (no triangolazione)
- Regola 3 viola in parte (fonte commerciale single, no peer-reviewed)
- Regola 4: confidence dichiarato "low" nel testo originale, OK
- "$99M (2024)" è ambiguo: revenue di servizio? Spend R&D? Backlog ordini? La differenza è enorme.

**Diagnosi:** il numero include con ogni probabilità **investimenti R&D pubblici** (es. EuroHAPS €43M + Zephyr Airbus + Sunglider), **non** revenue ricorrenti di servizio. Per un'analisi di mercato service-only è **fuorviante**.

**Azione:** declassare a "stima indicativa, confidence low" + annotare avvertenza esplicita + cercare in iterazioni future fonti indipendenti (ITU-R, Eurospace, AIAD reports) per triangolare. Non usare per decisioni Go/No-Go finanziarie.

### CLAIM-002 — "POLITO HELIPLAT come lineage per il 6B HALE"
**File:** `riferimenti/ricerche-approfondite.md`, `agents/aerodynamics-structures-engineer.md`
**Fonte attuale:** sintesi web ricerca DIMEAS, pubblicazioni anni 2005-2010
**Problema:**
- HELIPLAT è programma **degli anni 2000** (primo volo SESA 2007), **mai operativo a scala**
- Il gruppo Romeo et al. ha pubblicato design, ma il prototipo 1:3 (24 m wingspan) **non ha mai volato** in stratosfera
- Citare HELIPLAT come "lineage" suggerisce continuità che non c'è dimostrata
- Survivor bias: cito HELIPLAT senza menzionare i 15+ programmi HALE solari globali falliti (Aalto Hawk30 cancellato 2020, Helios crashed 2003, Solara 50 fallito, Sanswire StratXX cancellato, ScanEagle Solar non commerciale, etc.)

**Azione:** ridimensionare a "punto di riferimento storico/accademico italiano, **non** baseline operativa". Aggiungere lista dei programmi falliti come **base rate** per il Percorso 6B. Confidence "medium" sul lineage culturale, **non** "high" sulla feasibility derivata.

### CLAIM-003 — "Zephyr S8: 64 giorni di volo, MTOW 60 kg, 5 kg payload"
**File:** `riferimenti/ricerche-approfondite.md`, `agents/aerospace-market-analyst.md`
**Fonte attuale:** Airbus + Flight Global + Wikipedia
**Problema:**
- Conforme (triangolazione OK, source provenance OK)
- **MA**: il volo 64 giorni è in **Arizona** (clima desertico, perfetto). Non in Europa, non in inverno, non sopra orografia complessa.
- Generalizzare "Zephyr endurance" come riferimento per HALE EU/Italia inverno è **estrapolazione non garantita**

**Azione:** mantenere il numero, **aggiungere caveat geografico-meteorologico**. Citare il fatto che Zephyr ha **interrotto il volo dopo 64 giorni**, non è "endurance illimitata".

### CLAIM-004 — "JOUAV CW-30E: payload 8 kg, autonomia 480 min (8h)"
**File:** `agents/vtol-uas-specialist.md`, `riferimenti/ricerche-approfondite.md`
**Fonte attuale:** JOUAV datasheet (vendor)
**Problema:**
- Regola 3: fonte unica vendor → confidence "medium"
- "480 min" è in **condizioni nominali** non specificate (vento? quota? carico?)
- "TRL 8-9" è auto-dichiarato JOUAV, non validato EASA-EU
- Vendor CN → potenziali criticità geopolitiche (RSK-GEO-003)
- Lead time, prezzo, supporto IT/EU: **non documentati pubblicamente**

**Azione:** aggiungere annotazioni di confidence per ogni parametro. Marcare come "da verificare con quotation diretta + reference da operatori europei (ARPA Liguria, Vigili del Fuoco) che già operano CW-30E o equivalente". Non assumere TRL 8-9 EASA finché non verificato.

### CLAIM-005 — "EuroHAPS €43M EU contribution, CIRA partner italiano sui dimostratori"
**File:** `riferimenti/ricerche-approfondite.md`, multipli agenti
**Fonte attuale:** Thales Alenia Space press release + Italian Defence Technologies
**Problema:**
- Conforme su numeri (triangolazione OK)
- **MA inconsistenza concettuale**: ho posizionato EuroHAPS come "trampolino" per Firmamento, ma:
  - EuroHAPS è **EDF (difesa)**, non civile
  - CIRA fa **HHAA (dirigibile ibrido)**, **non** UAV solare HALE come Firmamento
  - Il consorzio è Leonardo/TAS/Elettronica + omologhi FR/DE/ES — Firmamento **non è dentro**
  - La possibilità di una collaborazione CIRA-Firmamento è **tutta da costruire**, non un given

**Azione:** correggere il framing in tutti i file. EuroHAPS è **landscape**, non partner attuale. CIRA è **possibile interlocutore**, non co-investitore acquisito. Aggiungere come "obiettivo di engagement Y1-Y2", non "lineage automatico".

### CLAIM-006 — "Coopfond Cooding Prototypes 2025: budget €500k, max €50k per progetto, 50% spese, ≥10 cooperative"
**File:** `agents/snai-funding-territorial-expert.md`, `riferimenti/ricerche-approfondite.md`
**Fonte attuale:** Coopfond + Legacoop web ricerca
**Problema:**
- Cifre **sembrano** verosimili ma:
  - "2025" è anno fonte, **non sappiamo se il bando 2025 è ancora aperto** nel 2026
  - Le condizioni esatte per il 2026 (ciclo successivo) sono da verificare presso Coopfond
- Regola 2: una sola fonte web sintetica, no documento ufficiale di bando

**Azione:** declassare a "stima 2025, verificare bando attivo 2026 con Coopfond direttamente". Non basare timeline finanziario su questa cifra senza conferma diretta.

### CLAIM-007 — "Pentema è frazione di Torriglia (GE), in SNAI Valli Antola-Tigullio 2021-2027"
**File:** multipli
**Fonte attuale:** ricerca web + politichecoesione.governo.it
**Problema:**
- Torriglia è **confermato** in SNAI Valli Antola-Tigullio (16 comuni)
- Pentema come **frazione** di Torriglia è **assunzione plausibile** ma andrebbe verificata con anagrafica Comune di Torriglia
- L'area "Valli dell'Antola e del Tigullio" è effettivamente la denominazione SNAI 2021-2027 Liguria — confermato

**Azione:** mantenere claim con confidence "high" (sul fatto che Torriglia è SNAI), confidence "medium" (sul fatto che Pentema è frazione di Torriglia — da verificare). Documentazione anagrafica del Comune va recuperata.

### CLAIM-008 — "Capital intensity 10 anni €500M-2B"
**File:** `riferimenti/visione-10-anni.md`
**Fonte attuale:** stima interna
**Problema:**
- Regola 3: source provenance "expert judgment interno"
- Regola 7: base rate? Starlink ha bruciato $30B+ per 6000 sat; un equivalente HAPS "EU sovereign" con 50-100 piattaforme avrebbe costo unitario probabilmente €20-100M/HAPS (R&D + manufacturing) + ground segment + spettro + operazioni → range più realistico potrebbe essere **€2-10B** per scala 10 piattaforme operative, **€5-30B** per scala 50-100 piattaforme
- **Capital intensity dichiarata (€500M-2B) è sottostima** rispetto al target dichiarato

**Azione:** rivedere range capital intensity al rialzo, dichiarare **scenari** (small fleet 5-10 HAPS, medium 20-50, large 100+) con range diversi. Mantenere confidence "low" su tutte le proiezioni >Y5.

### CLAIM-009 — "Fibra di lino: -54% peso vs metallico (Biogear)"
**File:** `agents/aerodynamics-structures-engineer.md`, `riferimenti/ricerche-approfondite.md`
**Fonte attuale:** CompositesWorld (press specializzata)
**Problema:**
- Cifra Biogear OK su sua applicazione specifica (landing gear elicottero)
- **MA**: estrapolare "-54%" come "narrativa ESG per HALE" è scorretto. Il landing gear ibrido CFRP+lino sostituisce **metallico**, non **CFRP puro**. Il peso saving HALE (vs CFRP puro) sarebbe MOLTO inferiore.
- Inoltre: il lino in compositi aerospace **non è certificato per strutture primarie**. Tipicamente solo strutture secondarie/interior.
- Per un'ala high-AR HALE, il **longherone principale** è strutturale primario → il lino non è ammissibile senza qualification path nuovo (5-10 anni R&D + test + certificazione)

**Azione:** ridimensionare il claim ESG. Fibra di lino è **narrativa di sostenibilità interessante** per **strutture secondarie/non critiche**, **non** un sostituto del CFRP per il longherone. Confidence sulle proprietà materiali "medium", confidence sull'applicabilità aerospace primaria HALE "very low".

### CLAIM-010 — "IRIS² €10B+ programma EU"
**File:** multipli
**Fonte attuale:** comunicazioni Commissione UE
**Problema:**
- Cifra €10.6B (€2.4B EU + private + Member States) è documentata
- **MA**: posizionare Firmamento come "complementare a IRIS²" presuppone che IRIS² **sia operativo** quando Firmamento è scalata
- IRIS² primo lancio: **fine 2025-2026** (Iris-A); operatività piena 2030+
- Firmamento Fase 4-5 (Y7-Y10) coincide con IRIS² operational ramp-up → timing è ok
- **MA**: il consorzio IRIS² (Airbus-Eutelsat-TAS-Telespazio-Hispasat-OHB-DT-Orange) **non include** Firmamento. La complementarità è un'**aspirazione**, non un acquired position.

**Azione:** chiarire in `visione-10-anni.md` e `sovereign-strategist.md` che "complementarità con IRIS²" è obiettivo strategico Y2-Y4, non baseline.

---

## 3. Inconsistenze interne tra documenti

### INC-001 — Briefing dice "Pentema in valle stretta", ma dimostrare BVLOS in valle stretta è ostico
**File coinvolti:** `agents/vtol-uas-specialist.md`, `agents/avionics-gnc-engineer.md`, `riferimenti/ricerche-approfondite.md`
**Problema:** SAIL II-III BVLOS in valle stretta con orografia complessa è realisticamente più difficile del SAIL III di pianura. SORA GRC + ARC potrebbero spingere a SAIL III-IV → costi più alti, certificabilità più ostica.
**Azione:** aggiungere caveat nei capitoli dello Studio (Cap. 6.1 architettura + Cap. 6.4 risk).

### INC-002 — POLITO HELIPLAT vs roadmap HALE Firmamento
**File coinvolti:** `agents/aerodynamics-structures-engineer.md`, `riferimenti/visione-10-anni.md`
**Problema:** HELIPLAT è R&D accademico anni 2000, mai operativo. Firmamento Y4-Y6 vuole "primo HALE italiano operativo". Continuità con HELIPLAT è narrativa, non sostanza tecnica.
**Azione:** ridimensionare riferimenti HELIPLAT a "patrimonio scientifico accademico italiano disponibile per partnership, non lineage industriale".

### INC-003 — Tassonomia: HHAA CIRA non è HALE solare
**File coinvolti:** multipli
**Problema:** Ho a volte mescolato "HAPS" generico con "HALE solare" specifico. EuroHAPS HHAA CIRA è un **dirigibile ibrido**, non un UAV solare. Sono concept divergenti.
**Azione:** distinguere sempre **HAPS** (categoria ITU che include dirigibili, palloni, UAV solari) da **HALE solare** (specifico tipo di HAPS che Firmamento sviluppa). Il vocabolario condiziona la strategia.

---

## 4. Debito di rigore residuo (da affrontare in iterazioni future)

> **Aggiornamento maggio 2026:** l'utente ha scaricato 13 fonti critiche in `/fonti/` (vedi `/fonti/INDEX.md`). Il debito sotto è stato rivalutato. **DR-004 e DR-009 sono ora parzialmente coperti.** Resto come prima.

Items che richiedono **verifica esterna** (chiamate dirette, fonti ufficiali) prima di prossimi gate:

| ID | Item | Azione richiesta | Owner | Deadline |
|---|---|---|---|---|
| DR-001 | Pentema-Torriglia anagrafica | Verifica con Comune | snai-funding | M+2 |
| DR-002 | Coopfond Cooding bando attivo 2026 | Contatto diretto Coopfond | snai-funding | M+1 |
| DR-003 | TRL JOUAV CW-30E EASA-equivalent | Quotation + reference EU operatori | vtol-specialist | M+3 |
| DR-004 | ENAC SAIL stima per Pentema | Pre-application meeting ENAC | regulatory-counsel | M+2 | ◐ Parzialmente coperto: `/fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md` |
| DR-005 | AGCOM spettro HAPS Italia status | Consultazione AGCOM Direzione Reti | telecom-payload | M+3 |
| DR-006 | Garante Privacy posizione su sorveglianza HAPS | Analisi precedenti + eventual workshop | data-privacy | M+4 |
| DR-007 | Base rate aerospace startup IT | Ricerca su database StartupItalia / AIAD | financial-cfo | M+3 |
| DR-008 | EuroHAPS estensione civile/futuri call EDF | Engagement DG DEFIS | sovereign-strategist | M+4 |
| DR-009 | IRIS² timeline e architettura stratosferica | Engagement DG CNECT | sovereign-strategist | M+4 | ◐ Parzialmente coperto: contesto AAM italiano in `/fonti/01_Piano-Strategico-Nazionale-AAM_ENAC_web-1.md` |
| DR-010 | CIRA willingness for civilian HALE partnership | Engagement diretto CIRA | sovereign-strategist + CTO | M+3 |
| DR-011 | Fibra di lino: qualificazione aerospace primaria | Ricerca peer-reviewed + esperti settore | aero-structures | M+6 |
| DR-012 | Mercato HAPS triangulation (fonti non commerciali) | Ricerca Eurospace/AIAD/ITU reports | market-analyst | M+4 |
| DR-013 | Programmi HALE falliti — analisi cause | Studio post-mortem Aalto Hawk30, Solara 50, etc. | systems-engineer | M+6 |
| DR-014 | Capital intensity HAPS perennial — stime indipendenti | Benchmark Airbus/SoftBank/Skydweller actual capex | financial-cfo | M+6 |
| DR-015 | Posizione Leonardo/TAS verso Firmamento | Reading mercato, eventuale dialogo informale | CEO + sovereign-strategist | M+6 |

---

## 5. Correzioni applicate inline ai file

Le correzioni epistemiche sono state applicate in questo commit per i file principali:
- `agents/aerospace-market-analyst.md` — declassamento cifre MarkNtel, caveat su mercato vs investimenti R&D
- `agents/aerodynamics-structures-engineer.md` — ridimensionamento claim fibra di lino, aggiunta lista programmi HALE falliti come base rate
- `agents/financial-cfo-analyst.md` — caveat su CapEx aerospace tipicamente +20-40% rispetto a primi piani
- `agents/vtol-uas-specialist.md` — caveat su TRL self-declared vendor, lead time, validation EU
- `agents/snai-funding-territorial-expert.md` — declassamento cifre Coopfond a "stima 2025 da confermare 2026"
- `riferimenti/visione-10-anni.md` — capital intensity range più realistico, caveat sul gap IRIS²-Firmamento
- `riferimenti/ricerche-approfondite.md` — base rate aerospace, lista programmi HALE falliti

Le correzioni mantengono integralmente le **boundary conditions** B1 (cooperative) e B2 (Starlink-EU obiettivo) come scelte di posizionamento del progetto, **non** come claim epistemici da validare.

---

## 6. Stato sintetico post-audit

**Confidenza media del framework prima dell'audit:** ~medium (con bias ottimistico inavvertito)
**Confidenza media post-audit:** ~medium-low onestamente dichiarato + roadmap di rigore residuo tracciata

**Sintesi onesta:** il framework attuale è una **baseline ragionevole** per impostare lo Studio di Fattibilità, **non** un documento da bandi/finanziatori. I 15 punti di debito residuo (DR-001 → DR-015) vanno chiusi per portare il documento a "investment-grade".

**Vincoli onesti per il prossimo lavoro:** il runtime cloud non consente download di fonti italiane critiche. Per chiudere il debito serve **lavoro umano offline** (download fonti, interviste, audit Coopfond/ENAC/AGCOM/CIRA/Comune Torriglia).
