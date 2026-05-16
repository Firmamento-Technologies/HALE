# 🔒 RESERVED — Analisi rischi geopolitici Firmamento HALE

> **CLASSIFICAZIONE: AD ACCESSO RISTRETTO**
>
> Documento confidenziale del progetto Firmamento Technologies. **NON parte dello Studio di Fattibilità pubblico**. Distribuzione limitata a:
> - Founder team Firmamento
> - Consulenti strategici esterni con NDA
> - Stakeholder istituzionali italiani (MIMIT, Dipartimento Coordinamento Politiche Economiche, CIRA) — su richiesta motivata
>
> **NON pubblicare** in bandi, comunicazioni stampa, social media, presentazioni a investitori non sotto NDA.

---

## 1. Quadro di riferimento

Una piattaforma stratosferica persistente sopra il territorio italiano + l'ambizione esplicita di costituire un **layer sovrano europeo HAPS** (vedi `visione-10-anni.md`) configurano Firmamento Technologies come **operatore di infrastruttura potenzialmente strategica**. Questo apre **5 fronti di rischio politico/geopolitico** che il Risk Register operativo non copre adeguatamente.

I rischi qui descritti sono **scenari plausibili**, non previsioni. Confidence dichiarato per ciascuno.

---

## 2. I 5 rischi geopolitici principali

### 🔴 RSK-GEO-001 — Frizione con USA / posizione Starlink

**Descrizione:** Posizionarsi pubblicamente come "alternativa europea a Starlink" è una posizione politicamente carica. L'amministrazione USA (qualunque essa sia) considera Starlink un asset di soft power critico. Un competitor europeo, anche stratosferico e geograficamente limitato, può generare frizione bilaterale.

**Vettori di pressione USA**:
- Restrizioni export per componenti USA critici (chip Honeywell/Collins, celle solari Spectrolab)
- Pressione su Italia/UE attraverso canali NATO (es. condizionalità su accesso a programmi NATO DIANA o Five-Eyes intelligence)
- Lobby USA in EU contro programmi che competono direttamente con asset USA (precedente: pressione su Galileo a inizio anni 2000)
- Restrizioni ITAR/EAR su tecnologie correlate (anche se Firmamento è puramente civile, la dual-use sensitivity esiste)

**Probabilità:** Medio (M) — si attiva solo se Firmamento raggiunge visibilità reale a partire da Fase 3-4 (Y4+)
**Impatto:** Medio-Alto (M-H) — può ritardare/bloccare supply chain US-derived
**Risk score:** ~12-15

**Mitigazione strategica**:
1. **NON utilizzare pubblicamente** il framing "alternativa Starlink". Linguaggio corretto: "complementare a IRIS² su layer stratosferico"
2. **Diversificare supply chain** verso fornitori EU/IT (vedi RSK-GEO-003)
3. **Dialogo Atlantico**: posizionarsi come partner di USA in NATO DIANA / dual-use civile invece di concorrente puro
4. **Avoid US dependency** in componenti core (GNC chip, celle solari, software volo)
5. **Engagement diplomatico**: tramite MIMIT e ambasciata IT a Washington, sondare reazioni preventivamente

**Trigger osservabili**:
- Communiqué USA contro programmi HAPS EU
- Restrizioni export specifiche su componenti HAPS-related
- Pressioni in tavolo NATO

---

### 🔴 RSK-GEO-002 — Golden Power / classificazione strategica IT

**Descrizione:** Il **D.L. 21/2012 (Golden Power)** e successive modifiche (DPCM 2020, 2022, 2024) attribuiscono al Governo italiano poteri speciali su settori strategici inclusi **aerospazio, telecomunicazioni, infrastrutture critiche, dual-use**. Firmamento, raggiungendo visibilità + asset operativi sopra territorio italiano, **rientrerebbe** in più definizioni:
- Aerospazio: chiaro (DPCM 30 dicembre 2020, allegato 1, punto 11)
- Telecomunicazioni / 5G NTN: chiaro (DPR 188/2014; DPCM 2024)
- Infrastrutture critiche: probabile (Direttiva NIS2 + recepimento D.Lgs. 138/2024)
- Tecnologia duale: possibile (Reg.UE 821/2021 dual-use)

**Conseguenze potenziali Golden Power**:
- **Notifica obbligatoria** di ogni operazione di ingresso/uscita di capitale, partnership strategica, trasferimento tecnologia
- **Prescrizioni** (modifiche obbligatorie al deal o alla governance)
- **Veto** su operazioni con investitori esteri considerati di rischio
- **Imposizione di golden share** sul capitale Firmamento (azione speciale con poteri di veto strutturali)
- **Classificazione di sicurezza** sui dati / progetti
- **Vincoli sul personale** (clearance richiesta per ruoli critici)

**Esempio recente:** Operazione Golden Power su **Avio S.p.A.** (2022) per protezione tecnologia propulsiva strategica.

**Probabilità:** Bassa (L) early stage → Media (M) a partire da Fase 3 (Y4+)
**Impatto:** Alto (H) — se attivato, può bloccare capital raise estero, imporre governance, limitare libertà operativa
**Risk score:** ~10 early → ~16 Fase 3+

**Mitigazione strategica**:
1. **Engagement preventivo con Dipartimento Coordinamento Politiche Economiche** (Presidenza Consiglio) **prima** del primo round con investitori esteri
2. **Ownership italiana stabile**: maggioranza capitale in mani italiane (founder + investitori IT + eventualmente CDP)
3. **Notifica preventiva volontaria** per ogni deal sospetto: meglio chiedere autorizzazione che subire veto
4. **Compliance NIS2** sin dalla Fase 1 — porre Firmamento come "soggetto essenziale" cooperativo, non oggetto di forzatura
5. **Strategic alignment** con Difesa/Intelligence italiani: collaborazione su dual-use civile può **legittimare** la posizione strategica vs **subirla**

**Trigger osservabili**:
- Notifica di avvio procedimento dalla Presidenza Consiglio
- Richiesta di documentazione su capital structure / supplier base
- Audit da DIS / Agenzia per la Cybersicurezza Nazionale

---

### 🔴 RSK-GEO-003 — Dipendenza supply chain non-EU

**Descrizione:** Molti componenti critici della piattaforma HALE hanno **fornitori dominanti non-EU**. In scenario di tensione geopolitica:
- **Celle solari multi-junction GaAs**: Spectrolab (US), Azur Space (DE) ✓, Solar Junction (US) — concentrazione US
- **Celle solari c-Si**: dominanza Cina (LONGi, Jinko, Trina) — Enel 3SUN (IT) e Meyer Burger (CH) sono EU sovereign emergenti ma ancora marginali
- **Batterie Li-S / SS / advanced**: Cina (CATL, BYD) + Corea (LG, Samsung) + emergente EU (Northvolt SE, ACC FR-DE-IT, Italvolt IT) — concentrazione asiatica
- **Chip GNC aerospace-grade**: Honeywell (US), Collins (US), STM (FR-IT) — concentrazione US
- **FPGA radhard / DAL-B**: Microchip (US), Xilinx-AMD (US), STM (EU) — concentrazione US
- **Materiali compositi CFRP**: Toray (JP), Solvay (BE) ✓, HEXCEL (FR-US) — EU presente parzialmente
- **Software volo / autopilot certificati**: Honeywell, Collins (US), Thales, Airbus (EU) — EU OK
- **Connettori e cablaggi MIL-spec**: Amphenol (US), TE Connectivity (CH-US) — concentrazione US

**Scenari di disruzione**:
- **A.** Escalation USA-Cina su Taiwan → blocco chip avanzati (TSMC, semicondotti)
- **B.** Tensioni USA-UE su tecnologia → ITAR/EAR weaponization
- **C.** Conflitto regionale (Medio Oriente, Mar Cinese, Ucraina) → blocco shipping
- **D.** Sanzioni reciproche RU/CN/UE → blocco materiali critici (rare earth, lithium)

**Probabilità:** Media (M) — alcune di queste tensioni sono attive **adesso** (USA-CN tariffe 2025, Ucraina ongoing)
**Impatto:** Alto (H) — può bloccare manufacturing per 12-36 mesi
**Risk score:** ~12-16

**Mitigazione strategica**:
1. **Supply chain mapping rigoroso** Y1: ogni componente, fornitore primario + secondario, paese, sanctions exposure
2. **EU sovereign suppliers roadmap**: identificare per ogni componente critico un **EU sovereign alternative** raggiungibile in 24-36 mesi, anche con costo +20-50%
3. **Inventory strategico**: per Fase 1-2, mantenere 6-12 mesi di buffer su componenti critici single-source
4. **Partnership with Italian/EU OEM**: collaborazione con Leonardo (avionica), STM (chip), Solvay (compositi), 3SUN (solar), ACC (batterie) — vantaggio: forniscono **production capacity** + **policy alignment**
5. **EU Critical Raw Materials Act (2024)**: applicare per "Strategic Project" status, ottenere fast-track regolatorio + financial support

**Trigger osservabili**:
- Restrizioni export USA su componenti aerospace
- Sanzioni UE su forniture cinesi
- Lead time fornitori >18 mesi su componenti critici

---

### 🔴 RSK-GEO-004 — Misalignment con IRIS² (EU sovereign satcom)

**Descrizione:** La UE sta costruendo **IRIS²** (Infrastructure for Resilience, Interconnectivity and Security by Satellite) come asset sovrano: €10.6B budget, 170-300 sat multi-orbit, operatori principali: consorzio Airbus-Eutelsat-Thales-Telespazio-Hispasat-OHB-DT-Orange. Operativa 2027-2030+.

Firmamento, ambendo a un layer stratosferico sovrano EU, **deve definire la propria relazione con IRIS²**:
- **Scenario A**: complementare (HAPS = low-latency stratospheric layer of IRIS² architecture) → opportunità
- **Scenario B**: concorrente (HAPS = alternative to IRIS² for some use cases) → rischio assorbimento o esclusione
- **Scenario C**: ignorata (HAPS = irrelevant for EU sovereign architecture) → rischio marginalizzazione

**Rischio dominante**: Scenario B o C senza azione esplicita.

**Conseguenze Scenario B**:
- DG CNECT non finanzia programmi HAPS che concorrono con IRIS²
- Pressione consorzio IRIS² per "annetterci": acquisizione/joint venture forzata
- Esclusione da bandi EU per "duplicazione di programmi sovrani"

**Conseguenze Scenario C**:
- Firmamento opera in vacuum strategico EU
- Finanziamenti limitati a IT nazionale + bandi tematici Horizon
- No scaling EU possibile

**Probabilità:** Media (M)
**Impatto:** Alto (H) — determina la scalabilità Fase 4-5
**Risk score:** ~12-15

**Mitigazione strategica**:
1. **Position paper esplicito** "Stratospheric Complementarity to IRIS²" — pubblicato Y1-Y2
2. **Engagement DG CNECT** (Networks Directorate) e **DG DEFIS** (Defence) preventivo
3. **Joint workshop** Firmamento + (TAS / Telespazio / Leonardo) su layer stratosferico in EU architecture
4. **Allineamento timing**: posizionare HAPS Fase 3-4 in coincidenza con IRIS² operational ramp-up (2027-2030) come "Phase 2" dell'architettura
5. **Avoid linguaggio competitivo**: mai posizionare Firmamento "vs" Eutelsat/IRIS²
6. **Cooperazione con consorzio IRIS²**: offrire a TAS/Telespazio role of strategic partner stratosferico

**Trigger osservabili**:
- IRIS² roadmap include o esclude HAPS layer
- Bandi EU DG CNECT specifici per HAPS aperti o chiusi
- Dichiarazioni pubbliche consorzio IRIS² su HAPS

---

### 🔴 RSK-GEO-005 — Acquisizione difensiva da incumbent IT

**Descrizione:** Il panorama aerospace italiano è dominato da **Leonardo (statale)** e **Thales Alenia Space / Telespazio (JV Thales-Leonardo)**. Questi player possono percepire Firmamento, raggiungendo certa visibilità, come:
- **Asset interessante** da acquisire per controllare la narrativa "HAPS italiana"
- **Concorrente irritante** in bandi UE/IT da neutralizzare

L'acquisizione **difensiva** avviene tipicamente al passaggio Fase 2 → Fase 3 (Y3-Y4), quando Firmamento è abbastanza dimostrabile da valere come asset ma non abbastanza grande da essere indipendente.

**Conseguenze acquisizione**:
- Founder exit con multipli "fair value" (5-15x revenue, NON 50-100x come scaleup tech success)
- Tecnologia HALE integrata in portfolio Leonardo/TAS
- Vision "EU sovereign stratosphere" diluita o ridiretta
- Talenti dispersi in BU di grandi gruppi

**Probabilità:** Media (M) a partire da Fase 2-3
**Impatto:** Alto (H) — termina la traiettoria indipendente (= la visione 10 anni)
**Risk score:** ~12-15

**Mitigazione strategica**:
1. **Capital structure resistente**: founder mantiene controllo (≥51%) o golden share fino almeno Fase 3
2. **Strategic anchor investors**: CDP (Italian state) + EIB + EIC — investitori "non ostili", senza obiettivi di assorbimento
3. **Partnership controllate**: collaborare con Leonardo/TAS su progetti specifici **senza** rendersi acquisibili (no equity stakes da loro)
4. **Speed**: la velocità è difesa. Maggiore è il valore di Firmamento al raggiungimento Fase 3, più costosa la acquisizione difensiva
5. **Pluralismo cooperative**: la struttura cooperativa pilota (10 coop) crea uno **stakeholder pool** che rende governance più resistente a take-over
6. **Public mission narrative**: posizionarsi come "ente strategico nazionale aperto", legittima difesa da takeover privato

**Trigger osservabili**:
- Approccio informale di Leonardo/TAS per "JV" o "investment"
- Tentativi di acquisire personale chiave Firmamento
- Mosse di lobbing in bandi MIMIT per favorire concorrenti

---

## 3. Risk register geopolitico — riassunto

| ID | Rischio | P | I | Score | Fase critica | Owner |
|---|---|---|---|---|---|---|
| RSK-GEO-001 | Frizione USA / Starlink narrative | M | M-H | 12-15 | Y4+ | sovereign-strategist + CEO |
| RSK-GEO-002 | Golden Power / classificazione IT | L→M | H | 10→16 | Y3+ | sovereign-strategist + legal |
| RSK-GEO-003 | Supply chain non-EU disruption | M | H | 12-16 | Y1+ | sovereign-strategist + supply chain |
| RSK-GEO-004 | Misalignment con IRIS² | M | H | 12-15 | Y2-Y4 | sovereign-strategist + CEO |
| RSK-GEO-005 | Acquisizione difensiva da incumbent IT | M | H | 12-15 | Y3-Y4 | CEO + Board |

## 4. Indicatori di allerta precoce (Early Warning Indicators — EWI)

Da monitorare **trimestralmente** dal team strategico:

- **EWI-1**: Dichiarazioni pubbliche US su programmi HAPS EU → RSK-GEO-001
- **EWI-2**: Audit da Presidenza Consiglio o DIS → RSK-GEO-002
- **EWI-3**: Lead time fornitori > 12 mesi → RSK-GEO-003
- **EWI-4**: Roadmap IRIS² pubblicata senza menzione layer stratosferico → RSK-GEO-004
- **EWI-5**: Approcci informali Leonardo/TAS per investment → RSK-GEO-005

## 5. Engagement plan strategico

### Tavoli istituzionali da presidiare

| Istituzione | Tavolo | Owner | Cadenza target |
|---|---|---|---|
| MIMIT Direzione Aerospazio | Strategia nazionale aerospazio | CEO | Q |
| Dipartimento Politiche Economiche (PdC) | Golden Power preview | Legal | Annuale |
| Cybersicurezza Nazionale (ACN) | NIS2 compliance | CTO | Q |
| MIT / ENAC | AAM / HAPS framework | Regulatory counsel | Q |
| ESA / DG CNECT (Bruxelles) | IRIS² coordination | Sovereign strategist | Q |
| DG DEFIS (Bruxelles) | EDF HAPS programmes | Sovereign strategist | Semestrale |
| NATO DIANA | Dual-use civil tech | CEO | Annuale |
| ASD-Eurospace HAPS WG | Industry alignment | CTO | Bimensile |
| ASI / CIRA | R&D consortium | CTO | Bimensile |

### Documenti strategici a tenuta

1. **Position paper "Italian Stratospheric Sovereignty"** — Y1, pubblicato
2. **MOU CIRA-Firmamento** — Y1, riservato
3. **MoU TAS-Leonardo "Stratospheric Complementarity"** — Y2, riservato
4. **Italy HAPS White Paper** (MIMIT-led, Firmamento principal author) — Y2-Y3
5. **EU Position Paper "HAPS as the third layer of EU sovereign infrastructure"** — Y3, pubblicato

## 6. Note finali

Questo documento è **strategicamente sensibile**. Le decisioni e mosse qui descritte hanno effetti di lungo termine sulla traiettoria di Firmamento. Errori in questo dominio sono **molto costosi e raramente reversibili** (es. una golden power impostata male può vincolare la società per decenni).

**Aggiornamento atteso**: trimestrale. Owner: CEO + sovereign-infrastructure-strategist.

**Review esterna**: annuale, da parte di un consulente strategico senior con NDA (preferibilmente ex-MAE/MIMIT, ex-Leonardo, o senior partner di studio legale specializzato in M&A regolato).
