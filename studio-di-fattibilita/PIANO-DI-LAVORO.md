# Piano di lavoro — Volume 1 dello Studio di Fattibilità

**Decisione utente:** completare l'intero Volume 1 in una sessione intensiva continua, autonoma. Limite tecnico noto: il runtime Claude Code on the web non supporta esecuzione schedulata multi-sessione, quindi tutto il lavoro è in **una singola sessione viva**.

## Strategia

- **4 subagent in parallelo** (background): Cap. 1, 2, 4, 11 (capitoli stand-alone, struttura ben definita)
- **5 capitoli in sequenza diretta**: Cap. 6 → 8 → 9 → 10 → 0 (tecnico-integrati, richiedono coerenza con capitoli vicini)
- **Commit progressivo dopo ogni capitolo** per non perdere lavoro
- **Quality bar costante**: stessa struttura dei Cap. 3, 5, 7 — NASA SE + art. 41 + epistemic rigor + Red Team check + boundary conditions B1, B2

## Ordine e dipendenze

| # | Capitolo | Modalità | Dipendenze | Dimensione attesa |
|---|---|---|---|---|
| 1 | **Cap. 1 Inquadramento** | Subagent parallelo | Nessuna | 20-25 pp |
| 2 | **Cap. 2 Stakeholder + SMART** | Subagent parallelo | Cap. 1 (sketched) | 20-25 pp |
| 3 | **Cap. 4 Scope + ICD** | Subagent parallelo | Cap. 3 (esiste) | 25-30 pp |
| 4 | **Cap. 11 Roadmap post-fattibilità** | Subagent parallelo | visione-10-anni.md (esiste) | 15-20 pp |
| 5 | **Cap. 6 Analisi Tecnica** | Io (sequenziale) | Cap. 3 (esiste) + fonti tecniche | 35-45 pp |
| 6 | **Cap. 8 Economico-Finanziario** | Io (sequenziale) | Cap. 6 + Cap. 7 (esiste) | 25-35 pp |
| 7 | **Cap. 9 Cronoprogramma + Gate** | Io (sequenziale) | Tutti i capitoli precedenti | 20-25 pp |
| 8 | **Cap. 10 Raccomandazione** | Io (sequenziale) | Sintesi di tutto | 10-15 pp |
| 9 | **Cap. 0 Sintesi Esecutiva** | Io (sequenziale) | Tutti i capitoli completi | 5-8 pp |

## Vincoli di stile (uniformi)

- Italiano formale
- Citazioni numerate `[^N]` con source provenance esplicita
- Confidence levels dichiarati (high/medium/low) per claim cruciali
- Almeno 4-7 falsifying observations per capitolo (epistemic rigor Regola 1)
- Boundary conditions B1 (cooperative+service-only) + B2 (EU sovereign) sempre preservate
- Red Team check finale con agente avversariale appropriato
- Output formato Markdown nel path `studio-di-fattibilita/cap-NN-nome.md`
- Commit dopo ogni capitolo

## Stato corrente all'avvio

- ✅ Cap. 3 (Requisiti + RTM) — commit 937edd2
- ✅ Cap. 5 (Quadro Normativo) — commit 25581d4
- ✅ Cap. 7 (Mercato + Business Case) — commit 67e4f44

## Target finale Volume 1

- 11 capitoli completati: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
- Dimensione attesa: 350-500 KB Markdown, ~150-200 pp A4

## Capisaldi da non perdere

- **No vendita di velivoli** (boundary B1): tutto è erogazione di servizi
- **No "alternativa Starlink europea" in linguaggio pubblico** (boundary B2 + RSK-GEO-001): usare "complementare a IRIS²"
- **Modello cooperativo come dato** (boundary B1): non in discussione
- **Visione 10 anni** (riferimenti/visione-10-anni.md): vettore strategico mantenuto, ma Studio approva solo Fase 1+2
- **Showstopper noti**: energy balance HALE inverno + framework HAPS EASA + capital intensity Phase 5

## Sessione attiva

Inizio: maggio 2026, sessione intensiva continua.
