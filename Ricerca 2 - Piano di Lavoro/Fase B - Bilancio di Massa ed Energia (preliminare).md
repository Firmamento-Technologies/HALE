# Fase B — Bilancio di Massa ed Energia (preliminare)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Chiusura del **bilancio di massa completo** (inclusa struttura, avionica certificabile, celle solari) e del **bilancio energetico** con e senza solare, entro il vincolo **MTOM < 25 kg** e **margine 5%** |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Input** | `Trade Propulsione` (§4 dimensionamento, powertrain genset), `Trade Study Architetture` (§3 energia), `Studio Pesi Payload` (payload 4 kg), Resoconto 15/07 §3.1 (bilancio di massa che non chiude) |
| **Scopo** | (1) Chiudere il mass budget **includendo la struttura** e l'**avionica certificabile ENAC**; (2) mostrare che l'"ambizione piena" sfonda i 25 kg; (3) **dimensionare le riduzioni** (solare, carburante/batteria, payload) per rientrare a **≤ 23,75 kg** (margine 5%); (4) confrontare **con e senza solare** guidati dal **cap di peso e di budget**. |
| **Powertrain di riferimento** | **Genset (ibrido-serie, config A2)** — scelta di team (vedi `Trade Propulsione` §8). |

> ⚠️ **Onestà tecnica (coerente col Dossier di Verifica):** tutti i pesi sono **stime parametriche** con banda esplicita, da confermare con progetto di dettaglio/RFQ. L'obiettivo qui è **la chiusura del bilancio e la logica delle riduzioni**, non la precisione al grammo.

---

## 0. Executive summary

1. **Con l'"ambizione piena" il velivolo NON chiude:** 24 h + payload 6 kg + modulo VTOL installato + solare + genset + **struttura + avionica certificabile** ⇒ **≈ 33 kg** (banda 30–37). Sfonda i 25 kg di **~8 kg**. Il bilancio precedente non chiudeva perché **ometteva struttura, avionica e celle solari** (Resoconto §3.1).
2. **La strada per rientrare è una sequenza di rinunce, in ordine di convenienza:**
   - **(a) Togliere il solare** (−~1,5 kg di sistema che, sotto cap di peso, "costa" più carburante di quanto ne risparmi — §3).
   - **(b) Payload 6 → 4 kg** (−2 kg; `Studio Pesi Payload`: nessun applicativo reale raggiunge i 6 kg).
   - **(c) VTOL come modulo rimovibile** (−~3,5 kg): la baseline di endurance certificata vola **ad ala fissa**; il VTOL si installa solo per le missioni che lo richiedono, **pagando payload/endurance** su quelle.
   - **(d) Ri-taratura fine di carburante e/o batteria** per chiudere il **margine 5%**.
3. **Baseline raccomandata "certificabile, in target" ≈ 23,5 kg** (margine ~6%): ala fissa, genset, **niente solare**, payload **4 kg**, batteria buffer + riserva di rientro, carburante per **~20–22 h**. **Non 23,9 kg**: il margine è reale (≥ 5%), non simbolico.
4. **Prezzo onesto della classe C3:** per stare **entro C3 e con margine**, l'endurance di progetto scende leggermente (dai 24 h aspirazionali a **~20–22 h**) e il payload a 4 kg. È il **target leggermente inferiore/paritario** rispetto ai benchmark **non-C3** (AR3 EVO 22 h/6 kg, ma > 3 m): li si eguaglia o li si sfiora **restando in C3**, che è l'obiettivo.
5. **Elettronica certificabile, non hobbistica:** il bilancio usa **avionica certificabile ENAC** (più pesante/costosa di ArduPilot/Pixhawk) e un **motore conforme alle normative sulle emissioni**, perché il velivolo dovrà essere **certificato**: stimare con elettronica non certificabile falserebbe il peso reale (§4).

---

## 1. Perimetro e assunzioni

- **Vincolo duro:** MTOM < 25 kg (soglia classe C3). **Target di progetto ≤ 23,75 kg** (margine 5%).
- **Missione di riferimento (baseline):** ala fissa alto allungamento, lancio assistito, crociera ~400 W (banda 350–500 W), endurance obiettivo 24 h → *da verificare contro il bilancio*.
- **Powertrain:** **genset ibrido-serie (A2)** — ICE al punto ottimo → alternatore/PMSG → bus DC + batteria buffer → motore elettrico di crociera + (se installati) lift VTOL. Motivazioni in `Trade Propulsione` §8.
- **Payload di progetto:** **4 kg** (da `Studio Pesi Payload`; 6 kg = sola capacità strutturale di riserva).
- **Elettronica:** **certificabile ENAC** e **motore emissioni-conforme** (§4), non componentistica hobbistica.

---

## 2. Bilancio di massa

### 2.1 CFG-0 — "Ambizione piena" (tutto insieme) → sfonda

| Voce | Peso stimato (kg) | Design (kg) | Note |
|---|---|---|---|
| Struttura/cellula (ala alto-AR, fusoliera, coda, **+ booms VTOL**, recupero) | 6,5–8,5 | **7,5** | La grande incognita omessa prima |
| Avionica **certificabile** (FC ridondante, GNSS, sensori, cablaggi) | 1,0–1,6 | **1,3** | Non hobby-grade (§4) |
| Datalink LOS + BLOS/SATCOM + antenne | 0,6–1,0 | **0,8** | REQ-05 |
| Genset: ICE + alternatore/PMSG + elettronica di potenza | 2,6–4,3 | **3,4** | `Trade Propulsione` §4.5 |
| Motore elettrico crociera + ESC | 0,4–0,8 | **0,6** | via serie |
| Modulo VTOL: 4 motori lift + ESC + eliche + booms | 3,0–4,5 | **3,8** | penalità VTOL |
| Batteria buffer | 2,5–3,3 | **3,0** | picco VTOL + buffer |
| Carburante 24 h (+ penalità serie) | 4,0–5,0 | **4,6** | genset |
| Serbatoio + impianto carburante | 0,4–0,6 | **0,5** | |
| Celle solari (1,4 m²) + MPPT + incapsulamento + cablaggi | 1,2–1,8 | **1,5** | vedi §3 |
| Payload | — | **6,0** | ambizione iniziale |
| Minuteria/margine hardware | 0,4–0,6 | **0,5** | |
| **TOTALE** | **30–37** | **≈ 33,5** | **⊗ sfonda i 25 kg di ~8 kg** |

> **Conclusione:** "24 h + 6 kg + VTOL + solare < 25 kg" **non è simultaneamente fattibile**. Conferma quantitativa del rilievo del Resoconto §3.1: la fisica non concede tutte le cose insieme.

### 2.2 Le leve di riduzione (in ordine di convenienza)

| Leva | Risparmio (kg) | Costo della rinuncia | Priorità |
|---|---|---|---|
| **(a) Togliere il solare** | **~1,5** | Perde ~4–15% di supplemento diurno (in cambio di ~0,15–0,6 kg di carburante) → **sotto cap di peso è un guadagno netto** (§3) | 1ª |
| **(b) Payload 6 → 4 kg** | **~2,0** | Nessuno: nessun applicativo reale supera 4 kg (`Studio Pesi Payload`) | 2ª |
| **(c) VTOL rimovibile (baseline senza)** | **~3,5** | La baseline endurance non fa hover; il VTOL si installa a richiesta, pagando payload/endurance su quelle missioni | 3ª (di configurazione) |
| **(d) Ri-taratura carburante/batteria** | **~0,5–1,0** | Endurance da 24 h → ~20–22 h (fuel) e/o riserva di rientro più stretta (batteria) | 4ª (fine) |

### 2.3 CFG-A — Baseline "certificabile, in target" (raccomandata)

Ala fissa (VTOL rimosso), **niente solare**, payload **4 kg**, genset, carburante ri-tarato.

| Voce | Peso (kg) | Note |
|---|---|---|
| Struttura/cellula (ala alto-AR, fusoliera, coda, recupero) | **6,0** | senza booms VTOL → più leggera |
| Avionica certificabile (FC ridondante, GNSS, sensori, cablaggi) | **1,3** | §4 |
| Datalink LOS + BLOS/SATCOM + antenne | **0,8** | REQ-05 |
| Genset (ICE + alternatore/PMSG + elettronica di potenza) | **3,4** | A2 |
| Motore elettrico crociera + ESC | **0,6** | |
| Batteria (buffer + **riserva di rientro** su avaria ICE) | **2,1** | vedi §5 (ridondanza) |
| Carburante (**endurance ~20–22 h**) | **4,0** | ri-tarato per il margine |
| Serbatoio + impianto carburante | **0,5** | |
| Payload di progetto | **4,0** | `Studio Pesi Payload` |
| Interfaccia lancio + recupero (paracadute/skid) | **0,4** | REQ-06 |
| Minuteria/margine hardware | **0,4** | |
| **TOTALE** | **≈ 23,5** | **✅ margine ~6% sotto i 25 kg** |

> **Il numero chiave: ≈ 23,5 kg, non 23,9.** Il margine è ≥ 5% reale (≥ 1,25 kg di riserva a MTOM), non un margine simbolico che sparisce alla prima integrazione.

### 2.4 CFG-B — Baseline + modulo VTOL (per confronto)

Partendo da CFG-A (23,5 kg) e **installando il modulo VTOL** (~3,5 kg struttura+motori+booms) si arriva a **~27 kg** → **oltre il target di ~3,3 kg**. Per rientrare in C3 con il VTOL installato si deve **rinunciare altrove**:

| Compromesso per tenere il VTOL in C3 | Effetto |
|---|---|
| Payload 4 → ~1,5 kg | Missione mono-sensore leggera (EO/IR) |
| **e/o** carburante −~2 kg | Endurance ~22 h → **~10–13 h** |

> Coerente coi dati reali: **AR3 EVO −36% endurance in VTOL** e **JUMP 20 (18 h ala fissa → 10–13 h col kit VTOL)**. **Il VTOL va tenuto modulare/rimovibile** e usato solo dove serve l'hover, accettando lì la perdita di payload/endurance.

---

## 3. Bilancio energetico: con e senza solare (guidato dal cap di peso e di budget)

### 3.1 Fabbisogno
Crociera ~400 W (banda 350–500 W) + avionica/payload ~45 W → **energia/24 h ≈ 9,6 kWh** (banda 8,4–12).

### 3.2 Raccolta solare (1,4 m² celle, 24%, perdite ~20%, 44°N Liguria)

| Stagione | Raccolta | % del fabbisogno 24 h | Carburante risparmiato/gg |
|---|---|---|---|
| Estate | ~1,5–1,75 kWh | **~15%** | ~0,5–0,6 kg |
| Equinozio | ~1,1 kWh | ~9% | ~0,35 kg |
| **Inverno** | ~0,43 kWh | **~4%** | ~0,15 kg |

### 3.3 Il confronto sotto vincolo (peso e budget)

| Criterio | **CON solare** | **SENZA solare** |
|---|---|---|
| Massa sistema solare (celle + MPPT + cablaggi) | **+1,5 kg** | 0 |
| Carburante risparmiato (estate → inverno) | −0,15…−0,6 kg | 0 |
| **Impatto netto sul budget di massa** (sotto cap 25 kg) | **+0,9 kg (estate) … +1,35 kg (inverno)** peggiore | **riferimento** |
| Impatto sul budget **€** | Celle alta efficienza + MPPT = voce non banale; **erode il budget** | nessuno |
| Endurance a parità di MTOM | *inferiore* (il solare "mangia" massa utile a carburante/payload) | **superiore** |
| Valore residuo | Narrativa "pseudo-satellite"/green | — |

**Lettura decisiva:** sotto un **cap di peso duro** e con un **budget vincolato**, il sistema solare **aggiunge ~1,5 kg per risparmiarne ≤ 0,6** → è un **guadagno netto negativo di massa utile in ogni stagione**, e in inverno è quasi tutto peso morto (~4%). Poiché il MPPT e le celle ad alta efficienza pesano anche sul **budget €**, il rapporto costo/beneficio non regge per il velivolo in target.

> **Raccomandazione:** **il solare esce dalla baseline certificata/in target.** Resta come **opzione da dimostratore/narrativa** solo su missioni con margine di massa (es. voli a carburante ridotto), **mai** come motore della persistenza. È esattamente la conclusione "supplemento, non motore" già nel corpus, ora **portata alla sua conseguenza sul bilancio**: se pesa sul cap di peso e di budget, si toglie.

---

## 4. Elettronica certificabile ENAC ed emissioni (perché cambia il peso)

Il velivolo dovrà essere **certificato**: stimare pesi con **elettronica hobbistica non certificabile** (ArduPilot/Pixhawk e simili) è privo di senso, perché **non sarà mai quella realmente installata**. Conseguenze sul bilancio:

- **Avionica di volo certificabile** (flight control ridondante, GNSS/PNT con prestazioni richieste, C2 link a integrità garantita, registratore): **più pesante e più costosa** dell'equivalente hobby → allocazione **~1,0–1,6 kg** (vs ~0,3 kg hobby). Il "supporto ArduPilot/Mission Planner" dei genset commerciali (es. Löweheiser) è una **comodità da dimostratore**, non l'avionica del prodotto certificato.
- **Motore conforme alle normative sulle emissioni:** esclude di fatto il **2T a carburatore "sporco"** come powerplant di serie e spinge verso **4T/EFI o heavy-fuel** con controllo delle emissioni (EFI + eventuale trattamento). Questo **converge con la scelta genset**: un motore tenuto al **punto di regime ottimale costante** (§5) è il più facile da rendere **emissioni-conforme e certificabile**, oltre che il più efficiente e durevole.
- **Nota di budget:** l'avionica certificabile e il powerplant certificabile alzano anche il **costo unitario** → da riflettere in `WP-B5` (i prezzi "COTS estero €5–20k/unità" del motore vanno rivisti verso l'alto per la variante certificabile).

---

## 5. Perché il genset (ibrido-serie) regge questo bilancio

Sintesi delle ragioni di team (dettaglio in `Trade Propulsione` §8):

1. **Doppia ridondanza:** genset **+** batteria buffer. In avaria del motore termico in crociera, il velivolo vola **a batteria** (riserva di rientro dimensionata in CFG-A: la voce batteria da 2,1 kg include l'energia per **~15–20 min di rientro**, sufficiente **soprattutto in VLOS**). Questo **vanifica il vantaggio di affidabilità** che giustificherebbe il motore in **presa diretta all'elica**: la ridondanza serie copre il caso di guasto meglio del diretto.
2. **Motore al punto ottimo:** l'ICE gira a **giri/carico costanti** (minimo BSFC), **eliminando le variazioni dirette di erogazione e regime** imposte dal volo → **maggiore durata del motore e intervalli di revisione (TBO) più lunghi**, oltre a emissioni più controllabili (§4).
3. **Penalità accettata:** la doppia conversione costa **~5–12%** di carburante in crociera (già nella voce carburante di CFG-A). È il prezzo, ritenuto **conveniente**, della ridondanza + regime ottimale + durata.

> Nota di coerenza: la matrice del `Trade Propulsione` §6 già assegnava ad **A2 (serie) il punteggio più alto (86,8)**; questa scelta di team **allinea la raccomandazione alla matrice**.

---

## 6. Sintesi delle configurazioni

| Config | Solare | VTOL | Payload | Endurance | **MTOM** | In target C3 (≤ 23,75)? |
|---|---|---|---|---|---|---|
| **CFG-0** ambizione piena | sì | installato | 6 kg | 24 h | **~33 kg** | ❌ sfonda di ~8 kg |
| **CFG-A** baseline certificabile | **no** | rimosso | **4 kg** | ~20–22 h | **~23,5 kg** | ✅ **sì (~6%)** |
| **CFG-B** baseline + VTOL | no | installato | ~1,5 kg *o* endurance ~10–13 h | ridotta | **~23–24 kg** | ✅ solo con rinuncia payload/endurance |

---

## 7. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Frazione strutturale reale (qui parametrica) | Stima di massa da CAD/materiali + eventuale dimostratore in scala |
| Peso/η reali del genset sul nostro punto | Banco genset (già in `Trade Propulsione` §9) |
| Avionica certificabile: peso/costo effettivi | Shortlist fornitori avionica ENAC-compatibile + RFQ |
| Emissioni motore: mappatura vs normativa applicabile | Trade motore emissioni-conforme (4T/EFI/HFE) |
| Budget di **potenza** payload (non solo massa) | Integrare con `Studio Pesi Payload` §5 (SAR/LiDAR energivori) |
| Riserva di rientro: energia reale per il profilo | Simulazione di rientro VLOS/BVLOS con batteria residua |

---

*Analisi first-order stage-appropriate per la fattibilità. Pesi ed energie parametrici con banda esplicita, da raffinare con CAD, banco genset e RFQ. Conclusione: **il bilancio chiude a ≈ 23,5 kg (margine ~6%) solo rinunciando a solare, portando il payload a 4 kg, tenendo il VTOL modulare e ri-tarando il carburante** — con powertrain **genset** ed elettronica **certificabile**.*
