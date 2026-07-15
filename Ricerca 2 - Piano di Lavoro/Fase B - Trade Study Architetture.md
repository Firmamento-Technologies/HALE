# Fase B — Trade Study delle Architetture
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Fase B (WP-B1…B4): requisiti "shall", analisi first-order, matrice di trade-off |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-12 |
| **Input** | `Fase A - MARKET ANALYSIS REPORT (consolidato)` (nicchie + profili di missione) |
| **Metodo** | Budget first-order di massa/energia/potenza/link (calcolo esplicito) + benchmark reali (AR3 EVO, AR5, Flexrotor, Zephyr) + matrice pesata P1–P9 |
| **Nota** | Analisi **first-order** (stage-appropriate per fattibilità): stime parametriche, non design di dettaglio. Dove serve CFD/test è indicato. |

> **Novità criterio (da riunione):** oltre ai parametri P1–P8, il velivolo deve essere **innovativo e "fare colpo"** su pubblico/politica (pannelli solari, autonomia, molti casi d'uso). Aggiunto come **P9 — Innovazione/Appeal** (peso alto).

---

> ⚠️ **Correzioni post-verifica (Dossier di Verifica, 2026-07-12):** (1) **Batteria** — 250–300 Wh/kg è a livello di **cella**, non di pacco: il pacco aeronautico reale è **~160–200 Wh/kg** (celle SOTA ~450, Amprius 2025). → **rafforza** la conclusione (batteria-sola dà ancora meno di 9–11 h). (2) **L'AR3 EVO NON è marcatura "C3"** (apertura 3,5–4,2 m > 3 m; UAS militare ISR): le sue specifiche 25 kg/6 kg/22 h/14 h restano valide come **benchmark di prestazione**, ma "C3 open" è un obiettivo **normativo** distinto (e le operazioni BVLOS long-endurance restano comunque "specific"/SORA). Le conclusioni fisiche di questo documento **non cambiano**.

## 0. Executive summary — la risposta al nodo "24 h in < 25 kg"

**Sì, 24 h a < 25 kg è fisicamente possibile — ma solo ad ala fissa e con propulsione a combustibile/ibrida. NON con batteria-sola e NON con solare-solo.**

| Via energetica | 24 h @ 25 kg? | Perché (first-order) |
|---|---|---|
| **Batteria-sola** | ❌ **Impossibile** | Servirebbero **30–47 kg** di batteria (a 250–400 Wh/kg). Max realistico **~9–11 h**. |
| **Combustione / ibrido-elettrico** | ✅ **Fattibile** | 24 h = **~3,5–4,5 kg** di carburante. Confermato: **AR3 EVO ~22 h, AR5 ~20 h a ~25 kg**. |
| **Solare-solo** | ❌ (a bassa quota/44°N) | L'ala raccoglie **~15% del fabbisogno in estate, ~4% in inverno**. È un **supplemento**, non il motore. |
| **VTOL** | ⚠️ dimezza | Config VTOL **−36% endurance** (dato AR3 EVO: 22 h→14 h) + massa e drag. |

**Conseguenza progettuale:** il team desidera insieme (a) 24 h, (b) payload pieno, (c) pannelli solari, (d) VTOL/hover — **la fisica non le concede tutte a 25 kg** (bilancio di massa: `Bilancio di Massa ed Energia`, che con l'ambizione piena arriva a ~33 kg). La sintesi che le concilia, **restando in classe C3 con margine 5%**:

> **Ala fissa · propulsione ibrido-elettrica a GENSET (serie) · lancio assistito (elastico/catapulta) · payload di progetto 4 kg · modulo VTOL opzionale e removibile per le missioni che richiedono hover · solare solo opzionale/dimostrativo (fuori dalla baseline in target).**

**L'obiettivo è la classe C3** (< 25 kg **e** < 3 m): per rispettarla con margine, l'endurance di progetto si assesta su **~20–22 h** e il payload su **4 kg** — cioè **target leggermente inferiore o, al meglio, paritario** rispetto ai benchmark di prestazione (AR3 EVO 22 h/6 kg) che però **non sono C3** (> 3 m). Il vantaggio distintivo è proprio **restare in C3**. Dettaglio in `Bilancio di Massa ed Energia` e `Studio Pesi Payload`.

Matrice di trade-off (P1–P9): **box-wing 81/100** e **ala fissa lancio-assistito 80/100** in testa; **VTOL ultimo (68)** per la penalità di endurance.

---

## 1. WP-B1 — Requisiti di sistema ("shall") dai profili di missione

Derivati dai profili di missione consolidati (Fase A §6). Soglia = minimo accettabile; Obiettivo = target ambizioso.

| ID | Requisito ("shall") | Soglia | Obiettivo |
|---|---|---|---|
| REQ-01 | Il sistema **deve** avere MTOM < 25 kg **e apertura < 3 m** (categoria **C3** — obiettivo di progetto) | < 25 kg | **< 25 kg con margine ≥ 5% (≤ 23,75 kg) e < 3 m** |
| REQ-02 | Il sistema **deve** fornire endurance | ≥ 12 h | **~20–22 h** (di progetto, in target C3); 24 h aspirazionale |
| REQ-03 | Il sistema **deve** trasportare payload utile intercambiabile | ≥ 4 kg | **4 kg di progetto** (6 kg capacità strutturale max, budget-permitting) |
| REQ-04 | Il sistema **deve** consentire lo **scambio rapido** del payload (EO/IR, SAR, multispettrale, relay) | bay modulare | < 15 min, plug-and-play |
| REQ-05 | Il sistema **deve** fornire datalink | LOS ≥ 100 km | **+ BLOS/SATCOM** |
| REQ-06 | Il sistema **deve** decollare/recuperare da area non preparata | lancio elastico/catapulta | **anche shipborne (≤ 5×5 m)** |
| REQ-07 | Il sistema **deve** operare in autonomia di volo con elaborazione **AI a bordo** | BVLOS auto | swarm/hub-ready |
| REQ-08 | Il sistema **deve** operare in condizioni meteo tipiche | vento ≤ 25 kn | −10…+45 °C |
| REQ-09 | Il payload **deve** includere sensori termici (IR) per il caso rischi/incendi | EO + IR | + multispettrale |
| REQ-10 | Il sistema **può** integrare **assistenza solare** sull'ala (narrativa/dimostratore) — **fuori dalla baseline in target** perché sotto cap di peso/budget il solare è un guadagno netto negativo (`Bilancio di Massa` §3) | opzionale | celle solo se il bilancio di massa chiude con margine |
| REQ-11 | Il costo unitario di realizzazione **deve** restare contenuto | [DA DEFINIRE] | minimizzare |

> REQ-02/REQ-07/REQ-10 codificano l'ambizione "24 h + autonomia + solare"; REQ-04/REQ-03 la modularità ("molti casi d'uso"). Il conflitto REQ-01↔REQ-02 è il nodo risolto in §3.

---

## 2. WP-B2 — Catalogo delle architetture candidate

| Arch. | Descrizione | Endurance tipica (classe 25 kg) | TRL | Benchmark reale |
|---|---|---|---|---|
| **A — VTOL ibrido** (quadplane) | Ala fissa + 4 rotori di sollevamento | ~10–14 h | 8–9 | AR3 EVO (VTOL 14 h), Flexrotor |
| **B — Ala fissa lancio-assistito** | Ala fissa alto allungamento, lancio elastico/catapulta, recupero skid/paracadute | ~18–24 h | 8–9 | AR3 EVO (ala fissa 22 h), AR5 (20 h) |
| **C — Box-wing** (ala scatolata) | Ala chiusa/giuntata, ala fissa | ~16–24 h (da CFD) | 5–6 | dimostratori R&D, UAV box-wing |
| **D — MALE leggero fisso** | Ala fissa più grande, catapulta | ~20–24 h | 7–8 | classe AR5/Hermes (scalati) |
| **E — Solare-elettrico puro** | Ala fissa, celle su tutta l'ala, batteria | perpetuo *solo estate/bassa latitudine*; **non 24 h/365 a 44°N** | 4–6 | Zephyr (classe diversa) |

Varianti di **propulsione** trasversali: batteria-elettrica · **ibrido-elettrico** (generatore a combustibile + buffer batteria) · combustione diretta · **solare-assistito** (celle su ala a supporto).

---

## 3. WP-B3 — Analisi first-order (la risposta quantitativa)

**Assunzioni:** MTOM 25 kg; crociera V ≈ 16–20 m/s; L/D ≈ 14–20 (ala fissa alto allungamento, ottimizzata endurance); drivetrain elettrico η ≈ 0,61; avionica/payload ≈ 45 W.

### 3.1 Potenza di crociera
**P_elettrica ≈ 350–500 W** (banda), nominale ~400 W. → Energia per 24 h ≈ **8,5–12 kWh/giorno**.

### 3.2 Batteria-sola → ❌ impossibile per 24 h
| Batteria | Frazione 55% (13,8 kg) | Per 24 h servono |
|---|---|---|
| 250 Wh/kg (oggi) | 3,4 kWh → **~7 h** | **47 kg** di batteria |
| 300 Wh/kg | 4,1 kWh → **~8 h** | **40 kg** |
| 400 Wh/kg (futuro) | 5,5 kWh → **~11 h** | **30 kg** |

→ **Muro di densità energetica:** anche con celle future, 24 h a batteria supera la massa totale. **Endurance batteria-sola realistica ≈ 9–11 h.**

### 3.3 Combustione / ibrido-elettrico → ✅ fattibile per 24 h
24 h richiedono **~3,5–4,5 kg di carburante** (benzina, motore 22–28%). Entro i 25 kg con payload. **Confermato dai benchmark reali** (AR3 EVO ~22 h, AR5 ~20 h). L'**ibrido-elettrico** (generatore + buffer batteria) aggiunge una **modalità elettrica silenziosa** per tratti sensibili → utile per ISR/marittimo.

### 3.4 Solare → supplemento e "wow", NON motore (onestà tecnica)
Ala S≈2 m², area celle ~1,4 m², celle 24%, perdite 20%:

| Stagione (44°N, Liguria) | Raccolta solare | % del fabbisogno 24 h |
|---|---|---|
| Estate | ~1,75 kWh/gg | **~15%** |
| Equinozio | ~1,1 kWh/gg | ~9% |
| **Inverno** | ~0,43 kWh/gg | **~4%** |

Picco a mezzogiorno ~270 W < crociera ~400–500 W. → **Un C3 a bassa quota NON può volare a energia solare in modo persistente** (è il "showstopper energia invernale" dell'HALE, in miniatura). **Ma** il solare resta prezioso come: (a) **range-extender** che taglia il consumo di carburante di giorno; (b) **narrativa green / "pseudo-satellite" / autonomia** ad alto impatto mediatico-politico (P8/P9). → Framing corretto: **"ibrido solar-assistito"**, non "drone solare".

> ⚠️ **Verifica sotto cap di peso e budget (aggiornamento 2026-07-15):** il sistema solare (celle 1,4 m² + **MPPT** + cablaggi) pesa **~1,5 kg** e risparmia **≤ 0,6 kg** di carburante d'estate (~0,15 kg d'inverno). Sotto un **vincolo duro di 25 kg**, aggiunge quindi **più massa di quanta ne liberi** (+0,9…+1,35 kg netti), oltre a erodere il **budget €** (celle ad alta efficienza + MPPT). **Conclusione operativa: il solare esce dalla baseline certificata/in target** e resta **solo come opzione dimostrativa/narrativa** quando il bilancio di massa ha margine. Confronto quantitativo con/senza in `Bilancio di Massa ed Energia` §3.

### 3.5 Penalità VTOL (dato reale)
**AR3 EVO: 22 h ala fissa → 14 h in VTOL = −36% endurance**, oltre a +2–4 kg di sistema di sollevamento e drag parassita in crociera. → **Incompatibile con l'obiettivo 24 h** se il VTOL è permanente. Conferma l'osservazione di Gigi in riunione (l'ala fissa vince sull'endurance).

### 3.6 Box-wing (l'opzione "innovazione")
- **Pro:** riduzione della **resistenza indotta** a parità di apertura (o apertura più compatta a parità di indotta); efficienza strutturale (consente allungamenti elevati senza penalità di peso); **silhouette distintiva** → forte appeal mediatico (P9). 
- **Contro:** maggiore **area bagnata** (drag parassita), complessità e aeroelasticità, **TRL più basso (5–6)**, drag di interferenza alle giunzioni. **Beneficio netto di endurance da confermare con CFD.**
- **Verdetto:** miglior candidato "flagship" per innovazione/appeal, a rischio tecnico maggiore.

---

## 4. WP-B4 — Matrice di trade-off pesata (P1–P9)

Pesi (somma 100): P1 Autonomia **15** · P2 Costo(basso) 12 · P3 Modularità 12 · P4 Casi d'uso 10 · P5 Peso/C3 8 · P6 Investitori 10 · P7 Funding 9 · P8 Politica/media 9 · **P9 Innovazione 15**. Score 1–5.

| Architettura | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | **TOT** |
|---|---|---|---|---|---|---|---|---|---|---|
| **C — Box-wing (ibrido+solare)** | 4 | 2 | 3 | 4 | 4 | 5 | 5 | 5 | 5 | **81,4** |
| **B — Ala fissa lancio-assistito (ibrido)** | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 3 | **79,8** |
| D — MALE leggero fisso (catapulta) | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 75,8 |
| E — Solare-elettrico puro | 3 | 2 | 3 | 3 | 3 | 5 | 5 | 5 | 5 | 74,8 |
| A — VTOL ibrido (quadplane) | 2 | 3 | 5 | 5 | 3 | 3 | 4 | 3 | 3 | 67,6 |

**Letture:**
- **Box-wing e ala fissa lancio-assistito sono testa a testa** (81 vs 80): il box-wing vince su innovazione/appeal e funding, l'ala fissa "liscia" su endurance, costo e maturità/rischio.
- **VTOL ultimo** (68): paga la penalità di endurance (P1) nonostante la modularità (P3) e i casi d'uso (P4) migliori.
- Analisi di sensibilità: abbassando il peso di P9 (innovazione), **B supera C** → la scelta tra i due dipende da **quanto pesa il fattore "wow"** rispetto a costo/rischio.

---

## 5. Raccomandazione architetturale (condizionata)

**Architettura raccomandata: ala fissa ad alto allungamento, con due configurazioni di prodotto sulla stessa cellula/famiglia:**

1. **Versione "performance" (B):** ala fissa convenzionale, lancio assistito (elastico/catapulta), **propulsione ibrido-elettrica a genset (serie)**, **niente solare nella baseline in target** → **è la variante che centra l'endurance di progetto (~20–22 h)** in classe C3 con margine e con rischio contenuto (TRL 8–9). Il cavallo di battaglia tecnico.
2. **Versione "flagship" (C, box-wing):** stessa avionica/propulsione, **ala scatolata** per la **silhouette distintiva** e il messaggio d'innovazione → **è la variante che fa colpo** su politica/investitori/media. Rischio maggiore (TRL 5–6) → da validare con CFD e un dimostratore in scala.

**Elementi trasversali (entrambe le versioni):**
- **Propulsione ibrido-elettrica a GENSET (serie, A2)** — motore al regime ottimale, **ridondanza** (rientro a batteria su avaria ICE), endurance di progetto ~20–22 h in target C3 (`Trade Propulsione` §8, `Bilancio di Massa`).
- **Solare solo opzionale/dimostrativo** — **fuori dalla baseline in target** (sotto cap di peso/budget è un guadagno netto negativo, §3.4); resta come narrativa "pseudo-satellite" **senza** promettere volo solare perpetuo.
- **Bay payload modulare** (EO/IR termico, SAR, multispettrale, relay) → i "molti casi d'uso"; **payload di progetto 4 kg** (`Studio Pesi Payload`).
- **Modulo VTOL opzionale e removibile** per le missioni che richiedono hover/decollo confinato (accettando la penalità di endurance solo su quelle missioni) → **concilia il dibattito Fede (VTOL/modularità) vs Gigi (ala fissa/endurance)**: cuore ala fissa + VTOL a modulo.

**Come scioglie le tensioni del team:**
| Desiderata | Risoluzione |
|---|---|
| Endurance (24 h aspirazionale) | Ala fissa + genset → **~20–22 h di progetto** in target C3 (la fisica del cap non concede i 24 h pieni con margine) |
| Pannelli solari / "wow" | Narrativa "pseudo-satellite" sì, ma **fuori dalla baseline in target** (peso/budget); solo opzione dimostrativa |
| VTOL / hover / modularità | Modulo VTOL removibile + payload swap (non permanente) |
| **Classe C3 (< 25 kg E < 3 m)** | **Obiettivo di progetto**, rispettato con **margine ≥ 5% (≤ 23,75 kg)** grazie a: genset, no-solare, payload 4 kg, VTOL rimovibile (`Bilancio di Massa`). Prezzo: endurance/payload leggermente inferiori ai benchmark **non-C3** |
| Molti casi d'uso / investitori | Piattaforma comune modulare + versione flagship |

---

## 6. Rischi tecnici e lacune (da chiudere per la Fase B "completa")

| Rischio / lacuna | Impatto | Azione (WP) |
|---|---|---|
| Beneficio endurance del box-wing non dimostrato | Alto | **CFD + dimostratore in scala** (WP-B3 esteso) |
| L/D reale e potenza di crociera (qui parametrici) | Medio | Analisi aerodinamica dedicata / wind tunnel |
| Integrazione ibrido-elettrico (peso, vibrazioni, firma termica) | Medio | Trade propulsione dettagliato |
| Peso/potenza reali dei payload (REQ-03) | Medio | Da profili nicchia (WP-B1 → fornitori) |
| Costi, tempi, TRL per architettura (WP-B5) | — | **Passata benchmark/costi** (fornitori, make-vs-buy) |
| Analisi costi-benefici architettura×nicchia (WP-B6) | — | dopo WP-B5 |
| Normativa BVLOS/SORA e spettro per la config scelta (WP-B8) | Medio | analisi regolatoria |

---

## 7. Ponte verso il resto della Fase B e la Fase C

- **Prossimo passo (WP-B5):** raccolta benchmark di **costi, tempi di sviluppo e TRL** per le architetture shortlist (ala fissa vs box-wing, ibrido vs solar-assist, sistemi di lancio) — con make-vs-buy (integrare AR3/Flexrotor vs costruire).
- **WP-B6:** analisi costi-benefici architettura × nicchia (N1–N5).
- **WP-B7:** conferma "piattaforma comune modulare" (ipotesi già forte).
- **WP-B8:** normativa per la configurazione scelta.
- **Verso Fase C:** la coppia **"ala fissa performance + box-wing flagship, ibrido solar-assistito, modulare"** è la candidata da portare nello Studio di Fattibilità come raccomandazione, con la roadmap (dimostratore in scala → pilota).

---

*Analisi first-order stage-appropriate per la fattibilità. Numeri di massa/energia parametrici (calcolo esplicito in sessione), da raffinare con aerodinamica dedicata e CFD sul box-wing. Benchmark: AR3 EVO, AR5, Flexrotor, Zephyr. La matrice P1–P9 è indicativa: pesi e score da validare col gruppo.*
