# Piano di lavoro — Rifacimento Studio di Fattibilità (ciclo v2)

> **Origine.** Riunione del 10/07/2026 (Luca, Gigi, Fede, Ema) — verbale in
> `da revisionare/registrazione-10072026.md` (upload). Mandato: *ricostruire lo
> Studio di Fattibilità partendo da un'analisi di mercato downstream
> iper-approfondita, poi da lì derivare il prodotto*, per massimizzare la leva su
> investitori e istituzioni.
>
> **Data:** 2026-07-10 · **Branch:** `claude/exciting-ride-8eos4l`

---

## 0. Principio guida (metodo Ema, corretto con l'esistente)

**Prima la domanda, poi il prodotto.** La riunione chiede di non partire dalle
conclusioni sul velivolo (HALE/MALE/VTOL) ma dai *parametri da
massimizzare/minimizzare* e dalla nicchia di mercato.

**Attenzione — non si parte da zero.** L'archivio contiene già un'analisi di
mercato downstream matura e adversarialmente verificata:
`analisi-bottom-up/03-mercato.md`, `11-fasce-mercato-multimissione.md`,
`20-SINTESI-fasce-e-proposta.md`, `30-SINTESI-prodotto-vs-servizio.md`;
`ricerca-approfondita/R1–R7`; `studio-di-fattibilita/cap-07`. Il ciclo v2
**estende** questa base, non la ripete.

### Criteri di ottimizzazione dichiarati in riunione (lente di ranking)
1. Massima autonomia (endurance)
2. Minimo costo di realizzazione/esercizio
3. Massima modularità (payload intercambiabile → più casi d'uso)
4. Massimo numero di casi d'uso servibili
5. Minimo peso (preferibilmente < 25 kg → categoria C3, minor attrito normativo)
6. Massima attrazione per investitori + massima leva politico-istituzionale

> ⚠️ Nota critica già emersa: questi criteri sono in **trade-off reciproco** (non
> co-massimizzabili) e "C3 = più facile" è **parzialmente falso** per missioni
> BVLOS di sorveglianza (ricadono in Specific/SORA a prescindere dal peso). Da
> risolvere in Fase 2 con trade study formale.

---

## Fase 1 — Analisi di mercato downstream iper-approfondita  ⟵ IN CORSO (multiagente, background)

**Obiettivo:** individuare i servizi downstream a maggior valore *accessibile e
difendibile* nel contesto Firmamento (Aree Interne + **marittimo/blue economy**,
con la doppia leva mercato × politica), e classificarli contro i 6 criteri.

**Copertura (9 lenti di ricerca, ciascuna verificata dal red-team):**

| # | Lente | Base d'archivio | Focus v2 |
|---|---|---|---|
| 1 | Connettività / NTN / resilienza | `01`, `03§4`, `R7` | refresh 2026, Direct-to-Cell, IoT d'area |
| 2 | Osservazione Terra / ambiente-idrogeologico-incendi-agri | `02` | refresh, nicchia persistenza |
| 3 | Logistica medicale / emergency delivery | `R1`, `11§M1` | refresh capitolati SSN, incumbent |
| 4 | Protezione Civile / resilienza aree interne | `Aree interne/*`, `03` | domanda PA reale, anchor |
| 5 | Sorveglianza & sicurezza (locale + coste/confini) | `11§M5` | refresh prime/dual-use |
| 6 | **Marittimo — security & environmental** ⭐NEW | *(assente)* | coste, confini, SAR, pesca illegale, sversamenti, **cavi/condotte sottomarine**, port security |
| 7 | **Marittimo — commercial / blue economy** ⭐NEW | *(assente)* | operazioni portuali, ship-to-shore, acquacoltura/pesca, offshore wind, MSC/porti Liguria |
| 8 | Domanda politico-istituzionale & fit finanziamenti | `06`, `R5`, `bando/*` | Coopfond/PNRR/FESR + **fondi blue economy (EMFAF/FEAMPA)** + EDF |
| 9 | Competitor & sostituti (incl. marittimi) | `R2`, `R7` | + operatori droni marittimi, satellite maritime (ICEYE/AIS), prime |

**Pipeline per lente:** ricerca (legge archivio + web 2026, output strutturato) →
verifica avversariale (red-team: chi paga davvero? il sostituto è gratis/più
economico? cosa la uccide?) → sintesi finale con barriera.

**Output Fase 1** (in `studio-v2/fase-1-mercato/`):
- `00-SINTESI-mercato-v2.md` — ranking nicchie contro i 6 criteri + menu per
  finanziatori + **handoff alla Fase 2** (per ogni nicchia top: quale servizio →
  quale classe di prodotto richiesta).
- un file per lente con evidenze e fonti graduate (disciplina `epistemic-rigor`).

---

## Fase 2 — Trade study prodotti (post-Fase 1)

**Obiettivo:** confrontare le classi di prodotto (COTS/T0, C3/T1, mid-VTOL/T2,
MALE/T3, HALE/T4) sui servizi selezionati in Fase 1, con matrice decisionale
NASA SE §6.8 + DOCFAP (art. 41 D.Lgs. 36/2023).

**Criteri di confronto:** costo (CapEx/OpEx), autonomia, quota, tempi di
sviluppo, payload, **facilità di certificazione normativa**, buy-vs-build, fit
con le nicchie selezionate, leva investitori/politica.

Deliverable: DOCFAP v2 + raccomandazione prodotto motivata.

---

## Fase 3 — Riscrittura Studio di Fattibilità

Integrazione Fase 1 + Fase 2 nella struttura canonica a 3 volumi (vedi
`CLAUDE.md`), agganciata ai gate Go/No-Go, con RTM/Risk Register/Trade Study
aggiornati. Deliverable finali in `.docx/.pptx/.xlsx`.

---

## Stato

- [x] Inventario archivio esistente
- [ ] **Fase 1 — ricerca mercato multiagente (in corso, background)**
- [ ] Fase 1 — sintesi e re-ranking
- [ ] Fase 2 — trade study prodotti
- [ ] Fase 3 — riscrittura studio
