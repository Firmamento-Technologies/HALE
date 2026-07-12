# Fonti primarie — Spesa pubblica attivabile (ancora SNAI), da archivio

| | |
|---|---|
| **Scopo** | Numeri della **spesa pubblica attivabile** (metrica dell' "ancora" aree interne), estratti dalle **fonti primarie già in archivio** — documenti che il deep research web **non** può raggiungere (host bloccati/PDF locali). |
| **Documenti** | `Aree interne/psnai_finale_30072025_clean_ministro.pdf` (PSNAI, lug 2025); `Aree interne/rapporto-istruttoria_regione-liguria.pdf` |
| **Metodo** | Estrazione testo **solo-stdlib** (zlib) con normalizzazione degli artefatti (il PDF è taggato `it-IT` e senza spazi). ⚠️ **Le cifre delle tabelle vanno verificate a vista sulle pagine del PDF**: l'estrazione incolla i numeri tra celle adiacenti. Le voci discorsive (CIPESS, fondo Covid) sono invece lette in modo netto. |
| **Data** | 2026-07-12 |

---

## 1. PSNAI — risorse nazionali per le Aree Interne (fonte primaria)

| Voce | Importo | Fonte nel documento | Lettura |
|---|---|---|---|
| Rafforzamento e ampliamento **SNAI** | **€100 mln** | Delibera **CIPESS nn. 41/2022 e 42/2022** | **Netta** |
| A favore degli **enti territoriali** (stessa delibera) | **€100 mln** | Delibera CIPESS 41/2022 e 42/2022 | **Netta** |
| Incremento fondo (contesto Covid-19) | **€120 mln** | **Art. 243, comma 1, D.L.** | **Netta** |
| **Totale assegnazione** (tabella di riparto) | **€172 mln** | di cui **FSC €100 mln** + **Fondo di Rotazione €72 mln** | Coerente (100+72=172) — *verificare* |
| — di cui macro-area **Centro-Nord** | **~€104 mln** | tabella riparto per macro-area | *verificare* |
| — di cui macro-area **Mezzogiorno** | **~€68 mln** | tabella riparto (104+68 = 172 ✓) | *verificare* |

> Il documento cita inoltre un **"Finanziamento per ciascuna delle 72 Aree 2014-2020"** (riparto per singola area del ciclo 2014-2020): dettaglio da estrarre a livello di singola area se serve dimensionare il SOM per vallata.

**Lettura per il progetto:** l'ancora SNAI muove **ordini di grandezza di €100–170 mln** a livello nazionale sul ciclo corrente. Non è denaro "per droni", ma è la **cornice di spesa** dentro cui un servizio (connettività, monitoraggio, emergenze) può essere finanziato tramite Regione/enti — coerente con la logica "ancora → scala".

---

## 2. Regione Liguria — istruttoria SNAI (fonte primaria)

Documento **analitico** (selezione/valutazione delle aree), non un piano di spesa: **non contiene importi di finanziamento itemizzati** (gli importi restano nel PSNAI nazionale). Elementi utili estratti:

- **Aree Interne liguri** citate: **Beigua**, **Antola**, **Fontanabuona**, **Valli** (Stura/Orba/Leira), **Alta Val** (Bormida/Trebbia) — coerenti con il caso pilota **Pentema** (area Antola, prov. Genova).
- **72 comuni** e **35** occorrenze di "aree interne" → conferma l'ampiezza del bacino territoriale ligure.
- Parametri per area presenti: superficie (km²), densità abitativa, popolazione — utili per **dimensionare le missioni** (area di copertura) più che il budget.

---

## 3. Uso e prossimi passi

- Questi numeri **chiudono in parte la lacuna §9** del report *Fase A - Analisi di Mercato* (la "spesa pubblica attivabile" era il buco principale dell'ancora).
- **Da verificare a vista** sulle pagine PDF: il riparto €172 mln (FSC/FdR) e la ripartizione Centro-Nord/Mezzogiorno; il finanziamento per singola Area 2014-2020.
- Il deep research sul **downstream civile** in corso (`w87rc35m3`) aggiungerà i fondi **PNRR** (dissesto, connettività) e la spesa **Protezione Civile**: si incroceranno con questi dati SNAI per il quadro completo dell'ancora.

---

*Estrazione da fonti primarie d'archivio (PSNAI, istruttoria Liguria) con metodo stdlib; le cifre tabellari sono da confermare a vista sul PDF. Voci discorsive (CIPESS €100+100 mln, fondo €120 mln) lette in modo netto.*
