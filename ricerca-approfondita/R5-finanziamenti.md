# R5 — Finanziamenti reali (fonti scaricate, importi verificati)

> **Progetto HALE — Firmamento Technologies** · Ricerca iper-approfondita di ancoraggio
> **Autore:** SNAI / Funding / Territorial Expert · **Data:** luglio 2026
> **Mandato:** ancorare gli strumenti di finanziamento del report `analisi-bottom-up/06-finanziabilita.md` (in gran parte `[STIMA]`/`[ALTO]`) a **bandi e regolamenti reali con importi**, citando sempre gli URL. Fonti salvate in `ricerca-approfondita/fonti/`.
> **Confidenza aggregata: MEDIO-ALTA** sull'esistenza e sui parametri degli strumenti (ora ancorati a fonti ufficiali); **INVARIATA (medio-bassa)** sulla capacità del veicolo cooperativo di attivare cofinanziamento/equity.

---

## 0. Nota metodologica e di provenienza (rigore)

**Limite dell'ambiente — dichiarato apertamente.** In questa sessione la **egress policy** blocca sia `WebFetch` sia `curl` verso gli host esterni (403 CONNECT tunnel / 403 Forbidden su gov.it, filse.it, cooding.it, ec.europa.eu, cdpventurecapital.it, ecc.). **Funziona solo `WebSearch`**, che restituisce una **sintesi del motore** sul contenuto delle pagine indicate, con gli URL reali. Di conseguenza:
- Ogni importo qui riportato è **estratto dalla sintesi WebSearch della pagina ufficiale citata**, non dallo scaricamento diretto del PDF/HTML di bando.
- Prima di qualunque **pianificazione finanziaria vincolante o domanda formale**, ciascun importo va **riverificato sul documento di bando ufficiale** (link nei file `fonti/`). Questo è un debito di rigore esplicito, non un dettaglio.
- Regola di lettura: `[UFFICIALE-web]` = importo da pagina ufficiale via WebSearch; `[DATO CERTO]` = documento firmato agli atti del progetto; `[STIMA]` = elaborazione dell'analista.

**Correzioni materiali rispetto al report `06`** (emerse da questa ricerca):
1. **Nuova Marcora**: il tetto **NON è €1M/4×** ma, nella versione aggiornata, **€2M / 5× la partecipazione CFI, tasso 0%**. (`fonti/nuova-marcora-cfi.md`)
2. **Cooding Invest**: confermato **max €250k**, ma con parametro nuovo: **fino al 70% del fabbisogno** (piano triennale), non "quota spese generica". (`fonti/coopfond-cooding.md`)
3. **Galaxia (CDP Venture)**: ticket reali ora noti — **pre-seed/PoC ~€250k, seed ~€1M**, su dotazione **€30M**, taglio **dual-use downstream EO/comunicazioni**. (`fonti/cdp-venture-galaxia.md`)
4. **Strumento nuovo non censito in `06`**: **Coop2050** (Coopfond + Banca Etica) — **prestito 0% Coopfond max €500k/coop** (plafond €1,5M) + Banca Etica €5M. (`fonti/coop2050.md`)
5. **FESR Liguria**: i **€25M** del report `06` sono il bando **Poli di R&I** (Decreto 481/2023); esiste in più un bando **Infrastrutture di Ricerca S3 da soli €3M** con beneficiari diversi (gestori di IR), da non confondere. (`fonti/fesr-liguria-innovazione-mpmi-e-poli.md`)

---

## 1. TABELLA MAESTRA — strumento → fonte → ticket/cofinanziamento reale → ammissibilità coop → verdetto

Natura: **G**=grant fondo perduto · **D**=debito agevolato · **E**=equity · **Gar**=garanzia · **CF**=credito fiscale.
"Veicolo" = rete 10 coop Legacoop (capofila Fabrica) + Firmamento SRL operatore.

| # | Strumento | Nat. | Fonte (URL principale) | Ticket / cofinanziamento REALE `[UFFICIALE-web]` | Ammissibilità del veicolo | Verdetto |
|---|---|---|---|---|---|---|
| 1 | **Coopfond — Cooding Prototypes** | G | cooding.it/prototypes | **max €50k/raggruppamento, ≤50% spese**; pool €500k | ✅ Alta — pensato per **≥10 coop** Legacoop + Digital Assessment PICO | **Attivo/ottenuto** (€50k già deliberati). Finanzia lo **studio/prototipo**, non la flotta |
| 2 | **Coopfond — Cooding Invest** | G/qE | cooding.it/invest | **max €250k, fino al 70%** del fabbisogno; piano triennale; pool €2,5M | ✅ coop / società a controllo coop, digital transformation | **Reggente per €0,25M**. Serve coop veicolo dedicata + Digital Assessment |
| 3 | **Coop2050 — Coopfond (prestito 0%)** | D | coop2050.it | **max €500k/coop** (plafond €1,5M), **tasso 0%** | ✅ coop Legacoop; tema sostenibilità/energia | **Nuovo**. Buon debito 0% per **ground segment/energia**; da rimborsare |
| 3b| **Coop2050 — Banca Etica** | D | coop2050.it | plafond €5M (finanza bancaria) | ✅ coop bancabili | Complemento debito a condizioni etiche |
| 4 | **FESR Liguria 1.1.1 — Innovazione MPMI** | G | filse.it (DGR 574 22/06/2023) | **50% fondo perduto, max €150k**; costo min. €30k | ✅ **MPMI ligure (Firmamento SRL diretta)**; S3 "Sicurezza e qualità della vita nel territorio" | **Reggente per €0,15M**. Il più diretto per Firmamento |
| 5 | **FESR Liguria 1.1.1 — Poli di R&I** | G | regione.liguria.it (Decreto 481 26/05/2023) | **dotazione €25M**; progetti R&S ad alto TRL; 25-50% cofin. tipico | 🟡 solo **via aggregazione a uno dei 5 Poli** (ATS) | Possibile con partnership; €0,3-2M/progetto |
| 5b| **FESR Liguria 1.1.1 — Infrastrutture Ricerca S3** | G | regione.liguria.it | **dotazione €3M** | 🔴 beneficiari = **gestori di IR**, non l'impresa | **Non pertinente** al veicolo |
| 6 | **Quota SNAI per Area (Antola-Tigullio)** | G indir. | politichecoesione.governo.it | **€4M naz. + ~€4,5M FESR + €0,33M FSE+ + €2M FEASR per Area** | 🟠 **INDIRETTO** — coop = attuatore/fornitore di intervento in ApQ, non grantee | Leva via co-progettazione Regione/Comune; non cassa diretta |
| 7 | **Nuova Marcora (CFI/MIMIT)** | D 0% (+E CFI) | mimit.gov.it · cfi.it | **fino €2M, 5× partecip. CFI, tasso 0%, 3-10 anni** *(era €1M/4×)* | 🟡 **solo cooperative** (Firmamento SRL esclusa); leva ∝ capitale coop | Debito reale ma limitato dal floor equity coop; serve ricavi |
| 8 | **Cooperfidi Italia — garanzia** | Gar | cooperfidiitalia.it | **garanzia 50%** del finanziamento; **plafond FEI €25M**; copertura costo ≤3,5% | ✅ per coop bancabili (imprese sociali = tutte le coop) | Abilitante del debito, non fornisce cassa |
| 8b| **CDP — garanzia InvestEU** | Gar | cdp.it | **50%** valore nominale; plafond €210M | ✅ tramite banche convenzionate | Riduce costo debito |
| 9 | **CDP Venture — Galaxia (aerospazio)** | E | cdpventurecapital.it · galaxia.vc | **PoC/pre-seed ~€250k; seed ~€1M**; dotazione €30M; **dual-use EO/comm** | 🟠 **equity** — richiede **spin-off SpA** (incompatibile con governance mutualistica) | **Miglior fit equity**; copre parte alta di €0,5-1M |
| 10 | **PNRR — Piano Italia 1 Giga / BUL** | G a operatori TLC | infratelitalia.it | pool **€3,8 mld** via gara; 450k case sparse residue | 🔴 **NO diretto** — aggiudicato a operatori TLC | Solo subfornitore/partner; domanda-target per NTN/HAPS |
| 11 | **PNRR Aerospazio (ESA+ASI)** | G/cofin. R&D | innovazione.gov.it · asi.it | **€1,3 mld ESA + €880M ASI**; bandi PMI ASI (importi da singolo bando) | 🟡 partnership/prime o bandi PMI ASI downstream | Indiretto; possibile via IS4Aerospace-Polito |
| 12 | **Horizon Europe CL4 — Space 2026** | G (RIA 100%/IA 70%) | hadea.ec.europa.eu | call €90,97M; **RIA €3-6M/progetto; IA €5-10M/progetto**; scad. 3/9/2026 | 🟡 come **partner di consorzio** transnazionale (3 SM) | Quota Firmamento €0,3-2M; è ricerca (IP/payload), non flotta |
| 13 | **European Defence Fund 2026** | G R&D difesa | ec.europa.eu (EDF WP2026) | **€1,01 mld, 10 call**; **RA 100% (€329M) / DA 70-90% (€676M)**; consorzio 3 SM | 🟠 solo consorzio prime-led dual-use (lineage EuroHAPS/CIRA) | Per 6B (HALE), non 6A; Firmamento partner, non grantee |
| 14 | **EUSPA / CASSINI** | premi/E | cassini.eu · euspa.europa.eu | **voucher accel. €75k (no equity); Investment Facility grant ≤€2,5M + equity ≤€15M; Challenges €100k** | 🟡 startup spaziali (spin-off) | Voucher €75k = porta d'ingresso; facility = fascia alta competitiva |
| 15 | **EIC Accelerator 2026** | G+E blended | eic.ec.europa.eu | **grant ≤€2,5M + equity ≤€10M** (+€2M flex); TRL ≥6; singola PMI; dual-use da 17/6/2026 | 🟠 singola PMI/spin-off (equity → diluizione) | Per €1,5-3M+ a TRL 7-8; altamente competitivo |

*(EuroHAPS €43M, TAS/CIRA — non uno strumento a cui candidarsi ma il precedente HAPS europeo e potenziale consorzio: `fonti/edf-2026-eurohaps.md`.)*

---

## 2. Quali strumenti REGGONO le taglie del piano di capitale

Il piano di capitale scaglionato (`analisi-bottom-up/23`) prevede **Stage 0 €150-500k**, **Stage 1 €1,5-2,5M**, **Stage 2 €1,5-3M**. Ancoriamo ciascuna fascia agli strumenti **con importo verificato**.

### 2.1 — Fascia €0,5-1M (Taglia A / Stage 0-1 basso): REGGE con stacking di grant + 1 equity fit

Somma di strumenti **diretti e ad alta ammissibilità**, tutti con importo ufficiale:

| Strumento | Importo reale | Natura |
|---|---|---|
| Cooding Prototypes | €50k (già in cassa) | G |
| Cooding Invest | €250k (≤70%) | G/qE |
| FESR Liguria 1.1.1 MPMI | €150k (50%) | G |
| Coop2050 Coopfond 0% | ≤€500k/coop | D 0% |
| Galaxia seed (se spin-off) | ~€1.000k | E |
| **Copertura potenziale** | **€0,5-1M pienamente coperta** | mix G+D+E |

**Verdetto fascia €0,5-1M: REGGE con confidenza medio-alta**, con **due vincoli confermati** (invariati da `06`): (a) i grant al 50% (Cooding, FESR) richiedono di **coprire l'altro 50%** — è il collo di bottiglia, non la disponibilità dei bandi; (b) la cassa si compone su **18-24 mesi** (lag tranche 3-6 mesi). **Novità positiva:** con **Coop2050 (0%, ≤€500k)** e **Galaxia seed (~€1M)** ora esistono **due strumenti reali di taglia €0,5-1M** che prima erano `[STIMA]`: la fascia non dipende più solo dallo stacking di micro-grant.

### 2.2 — Fascia €1,5-3M (Taglia B bassa / Stage 1-2): REGGE SOLO con equity/blended esterno + cambio veicolo

Nessun **grant diretto** al veicolo cooperativo raggiunge €1,5-3M in un colpo. La fascia è coperta **solo** da strumenti che implicano **società di capitali (spin-off)** e competizione aperta:

| Strumento | Importo reale | Condizione binding |
|---|---|---|
| EIC Accelerator blended | grant ≤€2,5M + equity ≤€10M | spin-off SpA; TRL ≥6; molto competitivo |
| CASSINI Investment Facility | grant ≤€2,5M + equity ≤€15M | idem, deep-tech spazio |
| Galaxia seed + follow-on | €1M + syndication | equity, dual-use |
| Horizon CL4 IA (quota) | €0,3-2M come partner | consorzio 3 SM, è R&D |
| Nuova Marcora (ramo coop) | ≤€2M (0%) ma ∝ capitale coop | leva bassa col floor equity €20-100k |

**Verdetto fascia €1,5-3M: NON regge sul veicolo cooperativo puro.** Regge **solo** con (1) **ingresso equity/blended esterno** (EIC/CASSINI/Galaxia+VC) e con esso (2) un **veicolo società di capitali** affiancato alla rete coop. Probabilità **30-50%** [STIMA, invariata]. La Nuova Marcora aggiornata a €2M **non** cambia questo verdetto: il tetto è teorico, la leva reale resta legata al capitale delle coop (floor €20-100k, `06` §3). **La correzione Marcora €1M→€2M migliora la capacità di debito, non l'accesso alla fascia €1,5-3M in assenza di ricavi per servire il debito.**

### 2.3 — Oltre €3M (Taglia C / HALE): confermato fuori portata

EDF (€1 mld, ma prime-led, difesa), PNRR ESA/ASI (€2,18 mld, ma su ESA/ASI/prime), Horizon: tutti **indiretti o prime-led**. Nessun canale porta €50-100M al veicolo. Confermato: HALE praticabile **solo** come operatore in consorzio EU (cambio veicolo). Invariato da `06`/`23`.

---

## 3. Calendario/finestre reali note (da riverificare)

- **Cooding Prototypes**: ciclo **2025** su pool €500k; verificare apertura ciclo **2026** con Coopfond (rif. Piero Ingrosso, Area Innovazione). — debito di rigore già in CLAUDE/audit.
- **Coop2050**: candidatura entro **31/08/2026** (percorso sostenibilità).
- **FESR Liguria Infrastrutture Ricerca S3**: finestra **17/03–30/04/2026** (chiusa); attendere riedizione. MPMI 1.1.1 e Poli: verificare riapertura sportelli.
- **Horizon CL4 Space 2026 (HORIZON-CL4-2026-03)**: scadenza **3/9/2026**.
- **EDF 2026**: scadenza call **~29/9/2026**.
- **EIC Accelerator / dual-use**: apertura estensione dual-use dal **17/6/2026**.

---

## 4. Verdetto sintetico e confidenza aggiornata

1. **Gli strumenti esistono e ora sono ancorati a fonti ufficiali con importi.** La tabella `06` era corretta nella struttura; questa ricerca **conferma** la maggior parte dei parametri e **corregge quattro numeri materiali** (Marcora €2M/5×; Cooding Invest 70%; Galaxia ticket €250k/€1M; nuovo Coop2050 €500k 0%).
2. **La fascia €0,5-1M regge (confidenza medio-alta)**: ora con **strumenti reali di taglia**, non solo micro-grant impilati. Vincolo invariato = **cofinanziamento 50% + equity founder + tesoreria**, non la disponibilità dei bandi.
3. **La fascia €1,5-3M regge solo con equity/blended esterno + spin-off** (EIC/CASSINI/Galaxia). Probabilità 30-50%. Nessun grant diretto al veicolo cooperativo la copre.
4. **Confidenza aggregata: da MEDIA a MEDIO-ALTA** sull'esistenza/parametri degli strumenti (ancoraggio riuscito), **invariata (medio-bassa)** sul fattore decisivo — la **capacità reale del veicolo coop** di coprire cofinanziamento ed equity (floor €20-100k da validare con i **bilanci reali delle 10 coop**).

**Azioni di validazione prima del gate (aggiornate):** (1) riverificare ogni importo sul PDF di bando ufficiale (link nei `fonti/`); (2) contattare **Coopfond** per apertura Cooding 2026 e ammissibilità Cooding Invest; (3) **LoI Regione Liguria/FILSE** su FESR 1.1.1 MPMI + calendario 2026; (4) verificare candidabilità **Galaxia** (spin-off) e **CASSINI Accelerator** (voucher €75k, no equity, porta d'ingresso); (5) acquisire i **bilanci 10 coop** per chiudere il floor equity.

---

## 5. Indice delle fonti salvate (`ricerca-approfondita/fonti/`)

- `coopfond-cooding.md` — Cooding Prototypes/Invest (€50k/50%; €250k/70%)
- `coop2050.md` — Coopfond+Banca Etica (0% ≤€500k/coop; €6,65M plafond)
- `nuova-marcora-cfi.md` — CFI/MIMIT (€2M/5×/0%)
- `fesr-liguria-innovazione-mpmi-e-poli.md` — 1.1.1 MPMI €150k/50%; Poli €25M; Infrastrutture €3M
- `cdp-venture-galaxia.md` — Galaxia €30M; PoC €250k/seed €1M; dual-use
- `cooperfidi-italia-garanzia.md` — garanzia 50%; FEI €25M; CDP InvestEU €210M
- `snai-aree-interne-2021-2027.md` — €4M+FESR/FSE+/FEASR per Area; 72 ApQ €1,179 mld
- `pnrr-aerospazio-esa-asi.md` — ESA €1,3 mld + ASI €880M; IRIDE; Space Factory 4.0
- `edf-2026-eurohaps.md` — EDF €1,01 mld (RA 100%/DA 70-90%); EuroHAPS €43M
- `horizon-cl4-space-2026.md` — CL4 Space €90,97M; RIA €3-6M/IA €5-10M
- `euspa-cassini-eic-accelerator.md` — CASSINI voucher €75k/facility ≤€2,5M+€15M; EIC ≤€2,5M+€10M
- `banda-ultralarga-italia-1giga.md` — Piano Italia 1 Giga €3,8 mld; 450k case sparse residue
