# Fonti primarie — Spesa pubblica attivabile (ancora SNAI), da archivio

| | |
|---|---|
| **Scopo** | Numeri della **spesa pubblica attivabile** (metrica dell' "ancora" aree interne), estratti dalle **fonti primarie già in archivio** — documenti che il deep research web **non** può raggiungere (host bloccati/PDF locali). |
| **Documenti** | `Aree interne/psnai_finale_30072025_clean_ministro.pdf` (PSNAI, lug 2025); `Aree interne/rapporto-istruttoria_regione-liguria.pdf` |
| **Metodo** | Estrazione testo **solo-stdlib** (zlib) con normalizzazione degli artefatti (il PDF è taggato `it-IT` e senza spazi). ⚠️ **Le cifre delle tabelle vanno verificate a vista sulle pagine del PDF**: l'estrazione incolla i numeri tra celle adiacenti. Le voci discorsive (CIPESS, fondo Covid) sono invece lette in modo netto. |
| **Data** | 2026-07-12 |

---

## 1. PSNAI — risorse nazionali per le Aree Interne (fonte primaria)

> ⚠️ **CORREZIONE POST-VERIFICA (2026-07-12).** Le cifre estratte automaticamente dal PDF in prima battuta erano **ERRATE** (l'estrazione incollava numeri tra celle adiacenti). Il **Dossier di Verifica** (claim **A1, verdetto CONFUTATO**) le ha corrette con **fonte parlamentare primaria**. Di seguito i dati corretti e verificati.

| Voce (delibere 2 agosto 2022) | Importo verificato | Dettaglio |
|---|---|---|
| **Delibera CIPESS n. 41/2022** — rafforzamento/ampliamento SNAI | **€198,6 mln** | €172 mln a **43 nuove aree interne** (4 mln ciascuna) + €21,6 mln alle **72 aree** del ciclo 2014-2020 (300k ciascuna) + €5 mln assistenza tecnica (Agenzia Coesione) |
| **Delibera CIPESS n. 42/2022** — Progetto speciale Isole minori | **€11,4 mln** | (non generico "enti territoriali") |
| **Totale congiunto** | **~€210 mln** | 198,6 + 11,4 |

**Fonte:** `temi.camera.it/leg19/temi/la-strategia-nazionale-per-le-aree-interne-snai-1.html` — *«Con la delibera 2 agosto 2022, n. 41 … sono stati stanziati 21,6 milioni di euro in favore delle 72 aree selezionate nel ciclo 2014-2020, per un importo di 300 mila euro per ciascuna area, e 172 milioni di euro in favore di 43 nuove Aree interne, per un importo di 4 milioni di euro per ciascuna area.»*

> ❌ **Da NON usare** (artefatti d'estrazione, inesistenti nelle delibere): «€100 mln + €100 mln», «€120 mln fondo», «riparto FSC €100 + FdR €72 = €172 mln», «Centro-Nord €104 / Mezzogiorno €68». Il **€172 mln è reale** ma è l'assegnazione alle **43 nuove aree**, non un riparto FSC/FdR.

**Lettura per il progetto:** l'ancora SNAI muove **~€210 mln** sul ciclo corrente, di cui **€4 mln per singola area interna**. Non è denaro "per droni", ma è la **cornice di spesa** entro cui un servizio (monitoraggio, emergenze, connettività) può essere finanziato via Regione/enti. Nota: **€4 mln/area** è vicino ai **€5 mln del modello Calabria** (allerta incendi con droni) → ordine di grandezza plausibile per un servizio drone su una singola area/vallata.

---

## 2. Regione Liguria — istruttoria SNAI (fonte primaria)

Documento **analitico** (selezione/valutazione delle aree), non un piano di spesa: **non contiene importi di finanziamento itemizzati** (gli importi restano nel PSNAI nazionale). Elementi utili estratti:

- **Aree Interne SNAI liguri** (corrette da verifica, claim A4): **Antola-Tigullio**, **Beigua-Sol**, **Val di Vara**, **Valle Arroscia**, **Fontanabuona**. Il caso pilota **Pentema** è una frazione del comune di **Torriglia**, nell'area **Antola-Tigullio** (Città Metropolitana di Genova). *(La prima estrazione riportava "Valli/Alta Val": etichette garbled, da scartare.)*
- **72 comuni** e **35** occorrenze di "aree interne" → conferma l'ampiezza del bacino territoriale ligure.
- Parametri per area presenti: superficie (km²), densità abitativa, popolazione — utili per **dimensionare le missioni** (area di copertura) più che il budget.

---

## 3. Uso e prossimi passi

- Questi numeri **chiudono in parte la lacuna §9** del report *Fase A - Analisi di Mercato* (la "spesa pubblica attivabile" era il buco principale dell'ancora).
- **Cifre corrette e verificate** (Dossier claim A1): €198,6 mln (Del. 41/2022) + €11,4 mln (Del. 42/2022); €172 mln alle 43 nuove aree (€4 mln/area). Le cifre della prima estrazione ("€100+100 mln", "€120 mln", riparto FSC/FdR) sono da scartare.
- Il deep research sul **downstream civile** in corso (`w87rc35m3`) aggiungerà i fondi **PNRR** (dissesto, connettività) e la spesa **Protezione Civile**: si incroceranno con questi dati SNAI per il quadro completo dell'ancora.

---

*Estrazione da fonti primarie d'archivio (PSNAI, istruttoria Liguria) con metodo stdlib; le cifre tabellari sono da confermare a vista sul PDF. Voci discorsive (CIPESS €100+100 mln, fondo €120 mln) lette in modo netto.*
