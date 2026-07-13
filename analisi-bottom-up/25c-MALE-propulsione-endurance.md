# 25c — Propulsione ed Endurance della piattaforma T-SORV (fixed-wing sorveglianza Aree Interne)

> **Volume:** Analisi bottom-up pre-Studio — sottodocumento propulsivo della fascia T3-MALE civile
> **Data:** 13 luglio 2026
> **Autore:** Propulsion & Energy Engineer
> **Mandato:** dimensionare propulsione e bilancio energetico di una piattaforma fixed-wing ad alta endurance (target >10h, obiettivo 20h) per sorveglianza terrestre delle Aree Interne liguri, e valutare **onestamente** quanto contribuiscono i pannelli solari sulle ali a **bassa quota** (NON stratosferica). Riuso della metodologia di `studio-di-fattibilita/allegati/energy-balance/energy_balance_simulation.py`, ricalibrata al caso a bassa quota.
> **Skill applicate:** `epistemic-rigor` (falsificabilità, source provenance, confidence, worst/base/best).

---

## 0. Distinzione critica dal caso HALE — da leggere prima di tutto

Questo documento **NON è il caso HALE** e non ne eredita il verdetto. Le due analisi condividono le formule ma **non le conclusioni**, perché il problema fisico è qualitativamente diverso:

| Dimensione | HALE (20 km, perennial) | T-SORV (2-5 km, missione 10-20h) |
|---|---|---|
| Requisito energetico | Sopravvivere alla **notte invernale intera** per **mesi** (persistenza h24 × 365 gg) | Coprire una **singola missione diurna/quasi-diurna** di 10-20h |
| Vincolo dominante | Bilancio solare inverno 44°N (showstopper) | Massa di carburante/batteria a bordo |
| Densità aria | 0.089 kg/m³ (7% s.l.) → superficie alare enorme obbligata | 0.74-0.91 kg/m³ (60-74% s.l.) → ala normale, motore a combustione **è un'opzione reale** |
| Ruolo del solare | **Unica** fonte possibile (nessun rifornimento in volo per mesi) | **Uno tra vari** vettori; il carburante chimico è disponibile e leggerissimo |
| Verdetto energia | Perennial 44°N marginale/non fattibile con tecnologia baseline | 20h **raggiungibili oggi** con propulsione convenzionale (benchmark reale) |

**Conseguenza operativa esplicita.** Lo showstopper documentato in `ricerca-approfondita/R7-starlink-haps.md` e in `ENERGY-BALANCE-HALE-44N-REPORT.md` ("0 HALE solari operativi commerciali; perennial 44°N impossibile in inverno") **NON si applica a questa piattaforma**. Chi legge il report finale non deve confondere i due casi: qui la domanda non è "sopravvive all'inverno", ma "che mix propulsivo raggiunge 10-20h in una missione". La risposta, anticipata, è **sì — con propulsione a combustione/ibrida — e senza bisogno del solare come abilitante**. `[FATTO, confidence alta]`

**Benchmark reale che chiude la questione della fattibilità** (da `10-fasce-engineering.md` §5, contratto pubblico EMSA): **Tekever AR3/AR5 raggiungono 16-20h con propulsione a combustione convenzionale**, non solare, a MTOM fino 180 kg. `[FATTO, confidence alta — contratto UE]` Il target 10-20h è quindi dimostrato in servizio, oggi, in questa classe.

---

## 1. Punto di progetto e assunzioni dichiarate

Il punto di progetto esatto (MTOM, apertura, quota) è in via di definizione da parte dei colleghi sistemista e aerostrutturista. Adotto un **punto di progetto di lavoro** e testo la sensitivity attorno ad esso.

| Parametro | Range mandato | Punto di lavoro (base) | Confidence |
|---|---|---|---|
| MTOM | 100-250 kg | **150 kg** | vincolo esterno |
| Apertura b | >10 m | 14 m | assunta |
| Allungamento AR | — | 18 | assunta (high-AR loiter) |
| Superficie alare S = b²/AR | — | **10.9 m²** | derivata |
| L/D crociera | 18-25 (scala/quota) | **22** | `[STIMA]` media |
| Quota operativa | 2.000-5.000 m AMSL | **3.000 m** (test a 5.000) | vincolo esterno |
| Area pannelli disponibile | ~30-50% di S | **4-12 m²** (base 8 m²) | `[STIMA]` — vedi §6.1 |
| P sottosistemi (avionica+payload EO/IR) | — | **200 W** | `[STIMA]` |
| η catena motore-elica (elettrica) | — | **0.72** (motore·ESC 0.90 × elica 0.80) | `[STIMA]` |
| η elica (albero→spinta, ICE) | — | **0.80** | `[STIMA]` |

**Nota sull'area pannelli.** Il mandato cita "qualche m² a 10-15 m²": la forbice dipende fortemente dall'AR. Con AR 18 e b=14 m, S=10.9 m² e il 30-50% utile dà **3.3-5.5 m²**; i 10-15 m² si raggiungono solo con AR basso (10-12) e apertura 16 m, oppure rivestendo quasi tutta l'ala + stabilizzatori. Adotto un range **4-12 m²** con base 8 m² e dichiaro la dipendenza. Il collega aerostrutturista deve confermare l'area di skin realmente rivestibile (curvatura, vani ispezione, cablaggio). `[STIMA, confidence bassa-media]`

### 1.1 Potenza di crociera (modello bottom-up)

Formula classica steady-level high-AR (identica a `energy_balance_simulation.py` §4, ricalibrata a bassa quota):

```
P_prop_mech = (m·g)^(3/2) / ( √(0.5·ρ·S) · (L/D) )
```

Con ρ da atmosfera standard ISA (ρ(3 km)=0.909, ρ(5 km)=0.736 kg/m³). Risultati per il punto base e sensitivity MTOM/quota:

| MTOM | S (m²) | L/D | Quota | P_prop (mech) | P_elec propulsione (/0.72) | V cruise (~) |
|---|---|---|---|---|---|---|
| 100 kg | 9.0 | 20 | 3.000 m | 759 W | 1.012 kW | ~62 km/h |
| **150 kg** | **10.9** | **22** | **3.000 m** | **1.153 kW** | **1.601 kW** | **~70 km/h** |
| 150 kg | 10.9 | 22 | 5.000 m | 1.281 kW | 1.708 kW | ~77 km/h |
| 200 kg | 12.5 | 22 | 3.000 m | 1.656 kW | 2.208 kW | ~75 km/h |
| 250 kg | 14.2 | 20 | 3.000 m | 2.387 kW | 3.183 kW | ~78 km/h |

`[FATTO/STIMA, confidence media]` — modello deterministico validato con la stessa formula del repo. Cross-check: a 150 kg il carico elettrico totale (propulsione + 200 W sottosistemi) è **~1.8 kW**, coerente con una piattaforma di questa scala.

**Sensitivity quota**: salire da 3.000 a 5.000 m aumenta P_prop di ~+11% (aria più rada) ma può migliorare L/D (meno turbolenza, crociera più efficiente) e riduce interferenza con i crinali. Effetto netto sull'endurance: modesto (±5-10%). Il driver dominante resta la MTOM (P ∝ m^1.5). `[STIMA]`

---

## 2. Trade study propulsione — le quattro architetture

Per ciascuna architettura calcolo la **massa del sistema propulsivo + energia** (motore/e-powertrain + carburante o batteria) necessaria per **10h e 20h** al punto base 150 kg / 3.000 m, con i pesi qualitativi.

### 2.1 Masse energia — calcolo diretto (base 150 kg, P_elec_tot ≈ 1.8 kW, P_shaft ICE ≈ 1.44 kW)

**A) ICE / heavy-fuel puro** — combustibile a 12.9 kWh/kg, BSFC 400-500 g/kWh (albero):

| Endurance | Energia albero | Carburante (BSFC 400-500) | Motore+serbatoio | Massa sistema |
|---|---|---|---|---|
| 10h | 14.4 kWh | **5.8-7.2 kg** | ~6-9 kg | **~12-16 kg** |
| 20h | 28.8 kWh | **11.5-14.4 kg** | ~6-9 kg | **~18-23 kg** |

**B) Elettrico puro + batteria** — pack-level Wh/kg (NON cell-level):

| Endurance | Energia elettrica | Batt Li-ion 250 | Li-ion 300 | LiS 350 (ottimista) |
|---|---|---|---|---|
| 10h | 18.0 kWh | **72 kg** | 60 kg | 51 kg |
| 20h | 36.0 kWh | **144 kg** | 120 kg | 103 kg |

**C) Ibrido serie ICE + buffer elettrico**: motore ICE genera crociera; piccolo pack (2-4 kWh, 8-16 kg) per picchi, decollo, e ~30-60 min di **loiter silenzioso** motore spento. Carburante come (A) meno il credito buffer. Massa sistema 10h ≈ 20-28 kg; 20h ≈ 26-33 kg.

**D) Elettrico + solar-assist**: come (B) ma la batteria è ridotta dall'energia solare raccolta in missione (vedi §3). Non cambia la fattibilità di fondo dell'elettrico puro, la **sposta** di qualche ora.

### 2.2 Matrice trade study (Pugh semplificato, riferimento = ICE puro)

| Criterio (peso) | A) ICE/heavy-fuel | B) Elettrico+batt | C) Ibrido ICE+el | D) Elettrico+solar |
|---|---|---|---|---|
| **Endurance 20h @150kg** (0.25) | ✅ ~13 kg carburante → **facile** | ❌ 103-144 kg batt → **infattibile** | ✅ facile (+ buffer) | ⚠️ ~90-130 kg batt anche con solare |
| **Massa sistema** (0.15) | ✅ 18-23 kg (20h) | ❌ 103-144 kg | ➖ 26-33 kg | ❌ 80-120 kg |
| **TRL / maturità** (0.15) | ✅ 8-9 (Tekever, Hermes) | ✅ 8-9 (celle), ⚠️ integrazione a questa endurance | ⚠️ 6-7 (integrazione serie) | ⚠️ 4-6 (solar-assist a questa scala non commerciale) |
| **Complessità** (0.10) | ✅ bassa | ✅ bassa | ❌ alta (2 catene) | ❌ alta (MPPT+skin PV+batt) |
| **Rumore / firma acustica** (0.15) | ❌ motore sempre acceso (sorveglianza "rumorosa") | ✅ **silenzioso** | ✅ **loiter silenzioso** a comando | ✅ silenzioso |
| **Costo** (0.10) | ✅ basso | ➖ medio (batt costosa) | ➖ medio-alto | ❌ alto (PV aerospace) |
| **Firma termica IR / dispiegabilità** (0.10) | ➖ scarico caldo | ✅ bassa | ➖ | ✅ bassa |
| **Verdetto** | **Vincente su endurance/massa/costo** | Perde su massa/endurance | **Vincente su missione (silenzio a comando)** | Marginale: non abilita, aggiunge |

**Lettura**: ICE/heavy-fuel **raggiunge il target da solo** con margine enorme (13 kg carburante per 20h su 150 kg MTOM). Il suo unico vero svantaggio operativo è la **firma acustica** — rilevante per sorveglianza discreta. È proprio qui che l'**ibrido (C)** vince: motore per il transito e la crociera, **loiter silenzioso a batteria** sopra l'obiettivo sensibile. L'elettrico puro (B) **non raggiunge 20h** in questo envelope di massa. Il solar-assist (D) è un **add-on marginale**, non un abilitante. `[STIMA, confidence media-alta]`

---

## 3. Calcolo bottom-up dettagliato — elettrico puro (perché non basta)

Punto base 150 kg, P_elec_tot = 1.8 kW (propulsione 1.60 kW + sottosistemi 0.20 kW).

- **10h** → 18 kWh → **60-72 kg** di batteria Li-ion (300-250 Wh/kg pack). Su 150 kg MTOM è il **40-48% della massa totale** solo in batteria. Con airframe+avionica+payload+propulsione tipicamente al 55-65% della MTOM, resta poco margine: 10h elettrico puro a 150 kg è **al limite, non comodo**.
- **20h** → 36 kWh → **103-144 kg** di batteria (LiS ottimista → Li-ion). È il **69-96% della MTOM** in sola batteria: **fisicamente infattibile** (non resta massa per struttura, motore, payload). `[FATTO, confidence alta]`

**Loop di retroazione della massa.** Aumentare la MTOM per portare più batteria non risolve: P ∝ m^1.5, quindi più batteria → più potenza → ancora più batteria. A 200 kg, P_elec_tot ≈ 2.5 kW; 10h = 25 kWh → 83-100 kg (Li-ion) o **71 kg con LiS (36% MTOM)** → **10h elettrico puro diventa fattibile solo in cima all'envelope (≈200 kg) e solo con LiS**. Le 20h elettriche pure restano fuori portata per l'intero range 100-250 kg. `[STIMA, confidence media-alta]`

**Conclusione §3**: l'elettrico puro **non è competitivo** per il target 20h a questa scala. È valido solo per missioni **corte e silenziose** (2-4h), che non sono l'obiettivo di questo mandato.

---

## 4. Contributo realistico del solare a bassa quota

### 4.1 Assunzioni irradianza (Liguria, 2-5 km AMSL)

A bassa quota **non** vale il τ=0.95 stratosferico del modello HALE: sotto ci sono vapore acqueo, aerosol e (soprattutto) **nuvolosità reale**. Uso l'irradianza globale orizzontale (GHI) integrata giornaliera clear-sky tipica per la latitudine, con la quota (2-5 km, sopra gran parte della foschia bassa di valle) che dà un modesto guadagno rispetto al livello del mare:

| Stagione | GHI giorno (kWh/m²) | Note |
|---|---|---|
| Inverno (dic) | ~1.7 | fotoperiodo corto, sole basso 22° |
| Equinozio | ~4.5 | |
| Estate (giu) | ~7.2 | fotoperiodo 15h, sole 69° |

`[STIMA, confidence media]` — valori clear-sky; con copertura nuvolosa media invernale ligure realistica scontare **−30÷−60%**.

### 4.2 Energia solare raccolta in missione ed equivalente-ore

E_solare = GHI · area · η_pannello · η_mppt (0.97). Espressa anche come **ore-equivalenti** di crociera (E/1.8 kW):

| Scenario | Stagione | Area (m²) | η pannello | E raccolta | Ore-equiv. |
|---|---|---|---|---|---|
| **WORST** | inverno nuvoloso | 4 | 0.22 (Si) | **~0.6-1.5 kWh** | **0.3-0.8 h** |
| **BASE** | equinozio | 8 | 0.25 | **~7.5 kWh** | **~4.2 h** |
| **BEST** | estate clear | 12 | 0.30 (GaAs) | **~25 kWh** | **~14 h** |

`[STIMA, confidence bassa-media]` — l'incertezza è alta e dominata da area effettiva, nuvolosità e stagione.

### 4.3 Interpretazione onesta

1. **Potenza di picco solare vs crociera**: in estate a mezzogiorno, 8 m² × 1.000 W/m² × 0.25 ≈ **2 kW di picco**, superiore alla potenza di crociera (1.8 kW). Per **poche ore attorno al mezzogiorno estivo**, il solare può quasi sostenere la crociera. Ma questo è il picco, non la media, e collassa in inverno/nuvole.
2. **Su una piattaforma ICE/ibrida** (l'architettura vincente), il solare **non sostituisce carburante di crociera in modo utile**: potrebbe alimentare al più i sottosistemi (~200 W), risparmiando <1 kg di carburante su 20h. **Contributo trascurabile.**
3. **Su una piattaforma elettrica**, il solare estende l'endurance di **+0.3h (worst inverno)** a **+14h (best estate clear)**, base **~+4h**. Sembra molto, ma parte da una base elettrica che **non raggiunge comunque le 20h** e che dipende da meteo/stagione non contrattualizzabili per un SLA. **Estende una configurazione che resta non competitiva.**

**Sintesi**: il solare a bassa quota è un **bonus stagionale e meteo-dipendente**, non un abilitante. Al contrario del caso HALE — dove il solare è l'**unica** opzione — qui esiste il carburante chimico, 10× più denso in energia per kg utile e indipendente da sole e nuvole. `[STIMA, confidence media]`

---

## 5. Raccomandazione finale

### 5.1 Architettura raccomandata: IBRIDO SERIE ICE/heavy-fuel + buffer elettrico

| Configurazione | Endurance @150kg | Massa sistema | Verdetto |
|---|---|---|---|
| **Ibrido ICE + buffer (RACCOMANDATO)** | **20h+ raggiungibile** | ~26-33 kg | **GO** — target + loiter silenzioso |
| ICE/heavy-fuel puro | 20h+ facile | 18-23 kg | GO tecnico (ma sempre rumoroso) |
| Elettrico puro | 10h al limite, 20h no | 60-144 kg | NO per il target 20h |
| Elettrico + solar-assist | 10-14h stagionale | 80-130 kg | Marginale — non finanziabile su SLA |

**Motivazione.** Il target 20h è raggiungibile **oggi, con TRL 8-9**, tramite propulsione a combustione (dimostrato: Tekever 16-20h, Hermes 450 17-20h). L'**ibrido serie** aggiunge il valore operativo specifico della sorveglianza delle Aree Interne: **modalità loiter silenziosa** sopra l'obiettivo (motore spento, batteria) per ~30-60 min, riducendo firma acustica e IR — differenziante reale rispetto al puro ICE. Il costo è complessità di integrazione (TRL 6-7) e ~10 kg di massa in più. `[STIMA, confidence media-alta]`

### 5.2 Verdetto onesto sul solare: MARGINALE ("nice to have"), NON abilitante

A differenza del caso HALE (dove il solare è l'unica opzione e il suo bilancio invernale è lo showstopper #1), **qui il solare non è determinante**:
- non serve per raggiungere le 20h (il carburante lo fa con 13 kg);
- il suo contributo è stagionale (base +4h-equiv., worst +0.3h) e meteo-dipendente, quindi non contrattualizzabile;
- su architettura ICE/ibrida (la vincente) risparmia carburante trascurabile.

**Raccomandazione sul solare**: **non includerlo nella baseline**. Valutarlo come **opzione R&D di secondo livello** solo se emergesse un requisito di *silenzio esteso* (loiter silenzioso multi-ora, dove ricaricare il buffer col sole avrebbe senso) o una missione *estiva dedicata* a lunghissima permanenza diurna. In quel caso, 8-12 m² di pannelli su un ibrido darebbero un'estensione utile del loiter silenzioso — ma è un caso d'uso di nicchia, non la baseline. `[STIMA, confidence media]`

---

## 6. Falsifying observations (≥5)

1. **L/D reale < 18 in operazione.** Il modello assume L/D 22. Se la piattaforma reale (turbolenza sui crinali, payload esterno, disturbi) atterra a L/D 15-16, la potenza di crociera sale di ~+30-45% e **tutte le masse energia crescono in proporzione**. Impatto sproporzionalmente maggiore sull'elettrico. Falsifica: rende l'elettrico ancora meno fattibile, ma **non** cambia il verdetto ICE/ibrido (13 kg → ~18 kg carburante, ancora banale).

2. **BSFC del motore heavy-fuel > 550 g/kWh.** Piccoli motori a benzina/heavy-fuel in questa classe possono essere meno efficienti dell'assunto. A 600 g/kWh il carburante 20h sale a ~17 kg: ancora perfettamente gestibile. Il verdetto ICE regge anche in questo worst case.

3. **Area pannelli effettiva < 4 m².** Se l'aerostrutturista conferma che solo il 20-25% dell'ala è rivestibile (cablaggio, vani, curvatura), il contributo solare crolla a <1h-equiv. anche in estate → il solare diventa **irrilevante**, rafforzando "marginale".

4. **Requisito acustico stringente (sorveglianza covert).** Se il cliente (Protezione Civile / sicurezza) richiede firma acustica bassa **per l'intera missione** e non solo in loiter, l'ICE puro viene squalificato e il trade study si sposta verso **ibrido con frazione elettrica maggiore** o elettrico puro a endurance ridotta (2-4h). In quel caso il solare recupererebbe rilevanza. Da verificare con il requisito reale.

5. **Vincolo regolatorio MTOM > 150 kg (Certified Category).** Come segnalato in `10-fasce-engineering.md` §5.3, salire sopra 150 kg fa uscire dalla Specific Category. Se il punto di progetto deve restare ≤150 kg per ragioni regolatorie, l'elettrico puro 20h (che richiederebbe MTOM molto più alta) è **doppiamente escluso** — non solo per fisica ma per normativa. Rafforza ICE/ibrido leggero.

6. **Batterie LiS non disponibili a 350 Wh/kg pack entro la timeline.** Il calcolo elettrico "ottimista" usa LiS 350. Se restano solo Li-ion 250-300 pack (probabile a breve termine), l'elettrico puro peggiora ulteriormente. Non tocca il verdetto ICE/ibrido.

**Cosa NON è stato modellato (debito residuo)**: profilo di missione reale (climb, transito vs loiter hanno potenze diverse), consumo termico batteria a 5.000 m (−15÷−20 °C, minore che a 20 km ma non nullo), massa cablaggio/BMS (10-15% del pacco, inclusa solo qualitativamente), degradazione pannelli, riserva energetica regolatoria per rientro. Da chiudere quando sistemista e aerostrutturista fissano il punto di progetto.

---

## 7. Riga di fondo

**La piattaforma T-SORV raggiunge il target 20h OGGI, con propulsione a combustione (heavy-fuel) TRL 8-9 — dimostrato da Tekever AR3/AR5 (16-20h) e Hermes 450 (17-20h) nella stessa classe.** Bastano ~13 kg di carburante su 150 kg di MTOM. L'architettura **raccomandata è l'ibrido serie ICE + buffer elettrico**: raggiunge le 20h col carburante e aggiunge una **modalità loiter silenziosa a batteria** (30-60 min) che è il vero valore operativo per la sorveglianza discreta delle Aree Interne. L'**elettrico puro è escluso** per il target 20h (103-144 kg di sola batteria su 150 kg MTOM = infattibile; 10h solo al limite, e solo a ~200 kg con LiS). Il **solare a bassa quota è marginale ("nice to have"), non abilitante**: contributo stagionale/meteo-dipendente (worst +0.3h, base +4h, best +14h-equivalenti), trascurabile su architettura ICE/ibrida e comunque insufficiente a rendere competitivo l'elettrico. **Questo è l'opposto del caso HALE**, dove il solare è l'unica opzione e il suo bilancio invernale è lo showstopper — distinzione da mantenere esplicita nel report finale per evitare contaminazione tra i due casi. **Non includere il solare nella baseline**; tenerlo come opzione R&D solo se emerge un requisito di silenzio esteso.

---

## 8. Fonti e confidence

| Elemento | Fonte | Confidence |
|---|---|---|
| Formula P_cruise, catene η, metodo | `studio-di-fattibilita/allegati/energy-balance/energy_balance_simulation.py` (riuso ricalibrato) | Alta (metodo) |
| Densità ISA 0-5 km | Atmosfera standard ISA (calcolo diretto) | Alta |
| Benchmark endurance 16-20h reale (Tekever/Hermes) | `analisi-bottom-up/10-fasce-engineering.md` §5 (contratto EMSA, fonti pubbliche) | Alta |
| Non-applicabilità showstopper HALE | `ricerca-approfondita/R7-starlink-haps.md`; `ENERGY-BALANCE-HALE-44N-REPORT.md` | Alta |
| Densità energia batterie (pack Li-ion 250-300, LiS 350) | Persona propulsion-energy-engineer; SOA 2025-2026 | Media-alta |
| BSFC heavy-fuel 400-500 g/kWh, energia benzina 12.9 kWh/kg | Dati ingegneristici standard motori piccoli | Media |
| GHI stagionali Liguria 2-5 km | Stima climatologica clear-sky | Media |
| Area pannelli 4-12 m² | Assunzione (attende output aerostrutturista) | Bassa-media |
| L/D 18-25, punto base 22 | Stima per scala/quota | Media |
| Masse energia 10h/20h (calcolo) | Calcolo bottom-up deterministico (script scratchpad) | Media-alta |

**Confidence aggregata: MEDIA.** Il verdetto qualitativo (ICE/ibrido raggiunge 20h; elettrico puro no; solare marginale) è **robusto** perché deriva da rapporti di massa con margini di un ordine di grandezza (13 kg carburante vs 103-144 kg batteria), non da numeri al limite. La quantificazione precisa attende il punto di progetto definitivo di sistemista e aerostrutturista.

---

*Documento prodotto dal Propulsion & Energy Engineer — Analisi bottom-up HALE/Firmamento, 13 luglio 2026. Riuso metodologico di `energy_balance_simulation.py`, ricalibrato al regime a bassa quota non-perennial.*
