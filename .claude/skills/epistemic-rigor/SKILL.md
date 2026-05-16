---
name: epistemic-rigor
description: Use whenever the user, an agent, or a skill produces a substantive claim (technical, market, financial, regulatory, strategic) for the HALE project. Trigger phrases - "ogni affermazione", "a prova di bomba", "robusto", "verificabile", "rigore", "fonti", "validare un capitolo", "stress-test", "metti in discussione". Enforces the epistemic discipline of the project - falsifiability, triangulation, source-provenance, confidence levels, pre-mortem. Mandatory before any chapter is closed or any gate review.
---

# Epistemic Rigor — Regole di rigore epistemico per il progetto HALE

Questa skill **non genera contenuti**. Genera **discipline e controlli** che ogni claim del progetto deve superare prima di essere considerato robusto.

## Filosofia operativa

Un progetto HALE che vuole superare gate decisionali, autorità regolatorie, due diligence finanziaria e revisione tecnica indipendente **non può** permettersi affermazioni non sostanziate. Il difetto tipico dei progetti aerospaziali falliti non è una mancanza di entusiasmo, è una mancanza di **rigore epistemico**.

Le regole che seguono sono **vincolanti** per ogni output del progetto.

## Le 7 regole obbligatorie

### Regola 1 — Falsificabilità (Popper)

Ogni claim positivo deve dichiarare la **falsifying observation**: l'evento concreto, osservabile, datato, che — se accadesse — ci direbbe che il claim è falso.

**Esempio non conforme:** "Il payload telecom HALE fornisce alta capacità di backhaul."
**Esempio conforme:** "Il payload telecom HALE fornisce ≥ 100 Mbps aggregati nel beam centrale a 99.5% disponibilità annuale ITU-R P.618 zona K. *Falsifiable se: in test stratosferico la throughput aggregata < 80 Mbps per >5% del tempo annuale.*"

**Test minimo:** se un revisore non può **immaginare** un'osservazione che renderebbe il claim falso, il claim non è scientifico — è ideologia o aspirazione. Va riformulato o eliminato.

### Regola 2 — Triangolazione (≥ 2 fonti indipendenti)

Ogni cifra di mercato, tecnica, normativa, finanziaria deve avere **almeno 2 fonti indipendenti**. Divergenze tra fonti devono essere **esplicitate**, non nascoste.

**Categorie di fonti** (in ordine di affidabilità decrescente):
| Tipo | Esempio | Affidabilità |
|---|---|---|
| **Peer-reviewed** | Articolo IEEE / AIAA / ScienceDirect | **Alta** |
| **Statistico ufficiale** | Eurostat, ISTAT, ITU, EUSPA, ASI annual report | **Alta** |
| **Norma / regolamento** | Reg.UE 2019/947, D.Lgs. 36/2023, EASA AMC, ITU RR | **Alta** (per claim normativi) |
| **Test report indipendente** | RINA, DNV, TÜV, agenzia di certificazione | **Alta** |
| **Pubblicazione tecnica vendor** | Datasheet ufficiale | **Media** (verificato vs claim ma può omettere) |
| **Report commerciale di mercato** | MarkNtel, Grand View, Frost & Sullivan | **Bassa-Media** (orientato a vendere il report) |
| **Stampa specializzata** | Aviation Week, Flight Global, Defense News | **Media** |
| **Stampa generalista** | Sole24, Reuters | **Bassa** |
| **Blog / social** | LinkedIn, Twitter, Medium | **Molto bassa** |
| **Stima interna del progetto** | Calcolo nostro, expert judgment interno | **Bassa-Media** (utile se motivato e con assunzioni dichiarate) |

**Regola pratica:** se un claim cruciale ha **solo 1 fonte commerciale** (es. "il mercato HAPS cresce al 16% CAGR" da MarkNtel), va **declassato** a "stima preliminare" con confidence "low" — non a "dato di mercato".

### Regola 3 — Source provenance esplicita

Ogni cifra deve essere annotata con:

```
[fonte | anno | tipo | confidence]
```

**Esempi:**
- Pathloss free space @ 2.6 GHz, 25 km = 128.7 dB `[ITU-R P.525 | 2019 | norma | high]`
- Mercato HAPS 2030 = $240M `[MarkNtel Advisors | 2025 | commercial report | low]`
- Massa payload JOUAV CW-30E = 8 kg `[JOUAV datasheet CW-30E | 2024 | vendor publication | medium]`
- Pentema GRC 4-5 `[stima interna basata su SORA 2.5 | 2026 | expert judgment progetto | medium]`

**Dove ci sono divergenze tra fonti**, dichiararle:

```
Massa Zephyr 8/S = 60-62 kg
  - 60 kg [Airbus press release 2022 | vendor]
  - 62 kg [Flight Global 2024 article | press specialized]
  → confidence: high (range ristretto, fonte vendor coerente con press)
```

### Regola 4 — Confidence levels

Ogni claim porta esplicitamente un **confidence level**:

| Livello | Quando usarlo | Implicazione per il progetto |
|---|---|---|
| **High** | Norma in vigore + test multipli + consenso esperti | Può essere base di decisione Go/No-Go |
| **Medium** | Fonte vendor verificata + analogia con casi simili | Necessita verifica al gate successivo, non usare per Go finale |
| **Low** | Stima estrapolativa + fonte unica commerciale + analogia debole | Solo per pianificazione preliminare, **non** per giustificare investimenti |
| **Speculative** | Estrapolazione lontana + nessuna validazione | Marcato come "ipotesi da validare", **non** parte del baseline |

### Regola 5 — Pre-mortem prima del closing

Prima di chiudere ogni capitolo / trade study / gate review, è obbligatorio un **pre-mortem strutturato** (Klein 2007):

1. Assumi che il claim/decisione si è rivelato sbagliato 2-5 anni nel futuro
2. Scrivi il **post-mortem retrospettivo** — perché siamo finiti in errore
3. Identifica i **top-3 driver** del fallimento ipotetico
4. Per ognuno: cosa potevamo osservare oggi che ci avrebbe avvertito
5. Aggiungi quegli osservabili come **early warning indicators (EWI)** da monitorare

Il pre-mortem **non è un esercizio retorico**. Invoca `red-team-skeptic` per condurlo.

### Regola 6 — Steel-manning della posizione contraria

Prima di adottare una decisione (es. "scegliamo JOUAV CW-30E"), formula il **caso più forte** per la decisione opposta (es. "non scegliere CW-30E"). Se la tua versione "steel-manned" del contraltare è debole (= straw man), **stai dormendo** — non hai compreso la decisione. Iterare con `red-team-skeptic` o `competitor-intelligence`.

### Regola 7 — Base-rate awareness

Ogni proiezione di successo deve essere confrontata con la **base rate** della categoria:

| Categoria | Base rate successo (stime ordini di grandezza) |
|---|---|
| Startup aerospace seed → operational revenue | 10-20% |
| Programmi HALE solar → operativi commerciali | <30% (Aalto Hawk30 cancellato 2020, Solara 50 fallito, Sanswire/StratXX cancellati) |
| Bandi pubblici R&D vinti al primo tentativo | 15-25% |
| Studi di fattibilità → progetto realizzato | <50% in aerospace |
| Type Certification UAS innovativa <5 anni | ~10% |
| Servizio commerciale aerospace → break-even <5 anni | <30% |

**Se il piano richiede "tutto va bene"** in ognuna di queste dimensioni, il piano sta combattendo la base rate. Non è "ottimismo", è "ingenuità". Riformulare con margini di sicurezza o piano fallback.

## Procedure obbligatorie

### Procedura A — Chiusura di un capitolo dello Studio

1. ☐ Tutti i claim passano la Regola 1 (falsificabilità)?
2. ☐ Tutti i claim numerici passano la Regola 2 (triangolazione)?
3. ☐ Tutti i claim hanno **source provenance** (Regola 3)?
4. ☐ Confidence levels dichiarati per ogni claim cruciale?
5. ☐ Pre-mortem eseguito (`red-team-skeptic`)?
6. ☐ Posizione contraria steel-manned (`red-team-skeptic` o `competitor-intelligence`)?
7. ☐ Base-rate check applicato?

Solo se **tutti** i checkbox sono verdi, il capitolo è chiuso.

### Procedura B — Trade study

1. Steel-man di ciascuna alternativa (incluso `do nothing`)
2. Scoring **con confidence dichiarato per ogni cella della matrice**
3. Sensitivity analysis (Regola 7 sui driver)
4. Pre-mortem della decisione raccomandata
5. Annotazione delle **kill criteria** — quale evento ci farebbe ribaltare la scelta

### Procedura C — Gate review

1. Procedure A su tutti i capitoli di pertinenza
2. Procedura B su tutti i trade study di pertinenza
3. Risk Register aggiornato con **falsifying observations** per ogni rischio
4. **Stress test scenario** condotto da `red-team-skeptic` + `competitor-intelligence` + `regulatory-adversary`
5. Indipendent reviewer (humano esterno o agente non coinvolto) firma off

## Errori tipici da evitare

### Errore 1 — "Cita-e-corri"
"Il mercato HAPS cresce al 16% CAGR." → Citazione mancante / fonte unica commerciale → declassare a "stima preliminare, confidence low".

### Errore 2 — "Esperto dice"
"Un esperto del settore ha detto che..." → Senza pubblicazione/datasheet/test report, è opinione anonima → non utilizzabile per decisione Go/No-Go.

### Errore 3 — "Il vendor lo conferma"
Vendor ha incentivi a vendere. Datasheet OK come **input**, ma non come **verifica indipendente**. Conferma sempre con benchmark / test indipendente / pubblicazione peer-reviewed.

### Errore 4 — "Analogia a Zephyr"
"Zephyr ha volato 64 giorni, quindi noi possiamo fare 30 giorni come MVP." → Survivor bias. Citare anche i programmi falliti (Aalto Hawk30, Solara 50, Sanswire). Base rate.

### Errore 5 — "TRL secondo il vendor"
TRL è una scala soggettiva. **Vendor TRL ≠ EASA TRL ≠ NASA TRL**. Per certificazione, conta solo TRL dichiarato da autorità accreditata (NASA, ESA, EASA, DOD).

### Errore 6 — Confusione "feasibile" / "fattibile" / "operativo"
- **Feasibile** = la fisica lo permette
- **Tecnicamente fattibile** = il design lo permette
- **Operativamente fattibile** = il workflow operativo lo permette
- **Regolatoriamente autorizzabile** = i regolatori lo permettono
- **Economicamente sostenibile** = il business case sta in piedi
- **Operativo** = sta volando, sta vendendo

Un progetto può essere "feasibile" e non "operativo" per **decenni** (vedi Sanswire/StratXX 2005-2015). Usare le 6 categorie distinte.

### Errore 7 — Conformazione al desiderio
Quando il PM vuole dire Go, si trovano motivi per dire Go. Antidoto: red team obbligatorio (`red-team-skeptic` automatico ad ogni gate).

## Output che produce questa skill

- **Checklist epistemica** allegata a ogni capitolo/trade study/gate
- **Source provenance log** centralizzato del progetto
- **Confidence map** sui claim del progetto (high/med/low/speculative)
- **Pre-mortem report** per ogni decisione critica
- **Base-rate adjusted forecast** per il piano operativo

## Quando viene invocata

- **Automaticamente prima di ogni gate review** (parte della Procedura C)
- **Su richiesta dell'utente** quando vuole stress-testare un'affermazione
- **Quando un agente produce numeri o claim importanti** (parte del workflow standard)
- **Quando si aggiorna il Risk Register** (parte della valutazione confidence)
