# Fase B — WP-B5: Costi, TRL e Make-vs-Buy
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | WP-B5: modello di costo, maturità tecnologica (TRL), analisi make-vs-buy |
| **Versione** | 0.1 — bozza |
| **Data** | 2026-07-12 |
| **Input** | `Fase B - Trade Study Architetture` (architettura raccomandata) + deep research dedicata (81 agenti) |
| **Confidenza** | ⚠️ **Bassa sui numeri assoluti di costo.** La ricerca ha stabilito che **prezzi unitari, CAPEX di sviluppo e valori di contratto NON sono pubblici** (dati vendor/difesa riservati). Le cifre qui sono **stime parametriche esplicite**, non dati verificati. |

> **Esito-chiave della ricerca, in chiaro:** i dati di prezzo richiesti (prezzi Flexrotor/AR3/AR5/JOUAV/Quantum, costi sottosistemi, CAPEX R&D, valore contratti EMSA) **non sono reperibili pubblicamente**. Vanno ottenuti via **RFQ diretta ai vendor** o **banche dati di procurement (TED/EU, Gazzetta Ufficiale)**. Ciò che segue combina: (a) i **pochi fatti verificati** (TRL, benchmark Flexrotor, metodologia CBO), (b) un **modello di costo parametrico** costruito da noi, e (c) le **ancore già note** (1ª ricerca: pilota VTOL €600–900k, HALE €35–65M).

---

## 0. Sintesi (verdetto WP-B5)

1. **Doppio binario "BUY per il cash-flow, MAKE per la differenziazione, finanziato dalle ancore".** Un nuovo entrante come Firmamento dovrebbe **integrare/operare** una piattaforma commerciale ad ala fissa (TRL alto, mesi, rischio minimo) per servire subito le ancore e generare ricavi, e **in parallelo** condurre la **R&D del velivolo proprietario** (box-wing/solar-assist) **pagata dai fondi dual-use** (EDF/PNS/PNRM) che *esistono proprio per finanziare il rischio tecnologico*.
2. **Il box-wing è una scelta di differenziazione/appeal, NON di prestazione.** La verifica ha **confutato** il vantaggio aerodinamico del box-wing (nessun L/D superiore dimostrato); il beneficio è **strutturale-aeroelastico** e di **immagine**. Per pura endurance/costo, l'**ala fissa convenzionale** è migliore e più economica. → Il box-wing va tenuto come **vetrina R&D "flagship"** finanziata, non come prodotto di reddito.
3. **TRL di partenza:** ala fissa convenzionale **TRL 8–9**; ibrido-elettrico piccolo UAV **~6–7**; solar-assist **~5–6**; **box-wing ~4–5** (nessun prodotto commerciale di questa classe esiste). → Il rischio/tempo cresce esattamente nell'ordine dei desiderata "wow".
4. **Modello di costo giusto:** **costo di ciclo di vita per ora di volo** (non il costo ricorrente), con **endurance** e **tasso di perdita (attrition)** come driver principali (metodologia CBO 2021).

---

## 1. Stato dell'evidenza (cosa è verificato vs cosa è stima)

| Voce | Stato | Fonte |
|---|---|---|
| Box-wing/tandem-wing solare ≤25 kg è oggetto di ricerca peer-reviewed | ✅ verificato | MDPI *Aerospace* 2023, 10(2):105 |
| Beneficio box-wing = **strutturale-aeroelastico**, non aerodinamico | ✅ verificato | MDPI 2023 (rimuovendo i giunti d'estremità, il margine dal flutter si **dimezza**) |
| Vantaggio **aerodinamico** del box-wing (L/D 18, più efficienza) | ❌ **confutato** | verifica 0-3 su claim IDINTOS |
| Box-wing small-UAV = **TRL basso, nessun prodotto commerciale** | ✅ verificato | MDPI 2023 + ricerca avversariale (nessun prodotto trovato) |
| Dimostratore box-wing IDINTOS: 30 mesi, 3 modelli in scala + prototipo | ✅ verificato | Frediani/Cipolla (Springer) — ma **velivolo con pilota ~650 kg**, 25× la nostra classe; **importo non pubblico** |
| Flexrotor: ~25 kg VTOL, >30h (picco; ISR 12–14h), payload intercambiabili, ~3,7 m, **~30 addetti** | 🔶 medio | Breaking Defense 2024 (fonte singola) — **prezzo non pubblico** |
| Metodologia: **costo di ciclo di vita/ora**, endurance + attrition driver | ✅ verificato | CBO 2021 (pub. 57260) |
| **Prezzi unitari, CAPEX R&D, valore contratti** | ❌ **non pubblici / non verificati** | — |

---

## 2. TRL e premio di rischio per architettura/sottosistema

| Elemento | TRL stimato | Premio di rischio | Note |
|---|---|---|---|
| Ala fissa convenzionale | **8–9** | minimo | esempi commerciali di successo (AR3/AR5) |
| VTOL ibrido | **8–9** | basso | maturo (Flexrotor) ma −36% endurance |
| Lancio a catapulta/pneumatico | **9** | minimo | tecnologia matura |
| Avionica/autopilota BVLOS | **7–8** | basso-medio | COTS disponibili, ma certificazione BVLOS/SORA |
| Propulsione ibrido-elettrica (piccolo UAV) | **6–7** | medio | integrazione peso/vibrazioni/firma termica |
| Assistenza solare su ala | **5–6** | medio | celle disponibili, integrazione strutturale |
| **Box-wing (ala scatolata) ~25 kg** | **4–5** | **alto** | solo ricerca; validazione multi-modello (CFD + galleria + volo) |

> **Implicazione:** i desiderata più "wow" (box-wing, solare) sono anche i meno maturi → concentrano lì il costo e il tempo, ed è **esattamente il tipo di rischio tecnologico che i bandi R&D dual-use (EDF/PNRM/DIANA) finanziano**.

---

## 3. Modello di costo parametrico (STIME — da validare con RFQ)

> ⚠️ Cifre **stimate** con metodo bottom-up, non verificate. Ancora: 1ª ricerca (pilota VTOL €600–900k = percorso **BUY**), organico Flexrotor (~30 addetti), struttura costi Cooding (>80% personale).

### 3.1 CAPEX di sviluppo (percorso MAKE, fino a dimostratore volante)
Bottom-up (team ingegneristico come driver, coerente con >80% personale):

| Voce | Ipotesi | Stima |
|---|---|---|
| Team ingegneristico | 6–10 persone (aero, strutture, propulsione, avionica, SW, sistemi) | — |
| Costo pieno personale | ~€80–100k/persona-anno × ~8 × ~2 anni | **€1,3–1,6 mln** |
| Prototipazione, materiali compositi, iterazioni | 2–3 prototipi | €0,3–0,6 mln |
| Sottosistemi + payload di test (avionica, propulsione, gimbal) | integrazione | €0,2–0,5 mln |
| Test (galleria/CFD, prove di volo), overhead ~15% | — | €0,2–0,4 mln |
| **CAPEX a dimostratore (ala fissa convenzionale)** | | **≈ €2,0–3,0 mln** |
| **Premio box-wing** (validazione multi-modello, aeroelasticità) | +30–60% | **+€0,7–1,8 mln** → **€2,7–4,8 mln** |

→ **Ordine di grandezza MAKE a dimostratore: €2–3 mln (ala fissa), €3–5 mln (box-wing).** Il prodotto operativo/certificabile costa ulteriormente (verso €5–10 mln), su 3–4 anni. *Nota: è ben più dei €600–900k della 1ª ricerca, che era il percorso **BUY** (comprare JOUAV + operare il pilota), non costruire.*

### 3.2 Costo unitario a regime (stima)
| Configurazione | Stima unitaria di sistema |
|---|---|
| Solo air vehicle (cellula + propulsione + avionica) | €50–150k |
| Sistema completo (+ GCS + datalink) | €150–350k |
| Sistema con payload pesanti (EO/IR gimbal + **radar SAR** + SATCOM) | €300–800k+ |

> Il **payload** (specie radar SAR ed EO/IR di qualità) domina il costo di sistema. La **modularità** permette di vendere il sistema base e i payload separatamente.

### 3.3 Tempi e TRL di partenza
- Dimostratore ala fissa: **~18–24 mesi**; box-wing: **~24–36 mesi** (rif. IDINTOS 30 mesi, benché più grande).
- Prodotto operativo: **~3–4 anni**.
- TRL di partenza (config raccomandata): **6–7** per il nucleo ala fissa ibrida; **4–5** per la variante box-wing.

---

## 4. Make-vs-Buy — analisi e verdetto

| Criterio | BUY / integra-e-opera | MAKE / costruisci proprietario |
|---|---|---|
| Time-to-market | **Mesi** | 2–4 anni |
| Rischio tecnico | **Minimo** (TRL 8–9) | Medio-alto (TRL 4–7) |
| CAPEX iniziale | Basso (acquisto/leasing) | **€2–5 mln** |
| IP / differenziazione | Nulla (dipendi dall'OEM) | **Alta** (IP proprietaria, "wow") |
| Margine | Solo da operatore di servizio | Prodotto + servizio |
| Ammissibilità a bandi R&D (EDF/PNRM/DIANA) | Bassa | **Alta** (finanziano lo sviluppo) |
| Coerenza con ancore | Serve subito SNAI/EMSA | Finanziato da PNS/EDF |

**Verdetto: DOPPIO BINARIO.**
- **Binario BUY (subito):** integrare una piattaforma ad ala fissa commerciale (AR3/AR5, Flexrotor, JOUAV) e operarla come **service provider** → cash-flow immediato, serve le ancore SNAI/EMSA/Protezione Civile, genera dati ed evidenze operative con rischio minimo. *(È la stessa logica del "pilota VTOL €600–900k" della 1ª ricerca.)*
- **Binario MAKE (in parallelo, finanziato):** condurre la **R&D del velivolo proprietario box-wing/solar-assist modulare** come **traccia differenziante finanziata dai fondi dual-use** (EDF ~€20 mln topic seabed, PNRM, NATO DIANA, PNS) — che esistono *proprio* per pagare il premio di rischio tecnologico. Questo è il **cuore della strategia "ancora → scala"**: le ancore **pagano il MAKE**, il BUY **genera trazione**.

> **Onestà tecnica sul box-wing:** poiché il suo vantaggio aerodinamico è **confutato** (beneficio solo strutturale + immagine), il MAKE box-wing va giustificato come **vetrina d'innovazione finanziata** (P9/appeal + IP + accesso ai bandi difesa), **non** come necessità prestazionale. Se il finanziamento R&D non arriva, il ripiego razionale è **MAKE ala fissa convenzionale** (più economico, TRL più alto) o restare su **BUY**.

---

## 5. Modello di costo operativo e business case (metodologia CBO)

- **Metrica:** **costo di ciclo di vita per ora di volo** (ammortizza l'acquisizione), non il costo ricorrente. *(CBO 2021: per RQ-4 il vantaggio scende dal 38% al 17% passando da ricorrente a ciclo-di-vita.)*
- **Driver 1 — Endurance:** più ore/velivolo/anno → costo orario più basso (gli UAS USAF volano ~2× le ore degli ISR con equipaggio). → il posizionamento **long-endurance (~22h)** è anche un **vantaggio di costo**.
- **Driver 2 — Attrition:** gli UAS hanno tassi di perdita più alti → **dimensionare la flotta ~+22%** e includere ricambi nel business case.
- **Ricavo:** modello **data-as-a-service** con committente pubblico ricorrente (riferimento EMSA ~€30 mln pluriennali — *valore da confermare via procurement*). Il business case si chiude su **ore di volo contrattualizzate × tariffa oraria − costo ciclo-di-vita/ora**.
- ⚠️ **Numeri assoluti (tariffa oraria, costo/ora del mini-UAV, valore contratti) NON disponibili** → da reperire.

---

## 6. Lacune e prossimi passi (per rendere WP-B5 "investibile")

1. **RFQ ai vendor** (TEKEVER, JOUAV, Quantum, Schiebel, Airbus) per prezzi di sistema e canoni drone-as-a-service.
2. **Banche dati procurement** (TED/EU, Gazzetta Ufficiale, contratti EMSA/Frontex) per valori reali dei contratti di servizio.
3. **Preventivi sottosistemi** (propulsione ibrida, celle solari €/W, gimbal EO/IR, SAR, SATCOM, catapulta).
4. **Costo operativo/ora** di un mini-UAV drone-service (personale, manutenzione, assicurazione) — da operatori italiani.
5. **Importo e scope reali** di un dimostratore box-wing nella classe 25 kg (IDINTOS è 650 kg, non trasferibile).

→ Chiuse queste, si costruisce **WP-B6** (costi-benefici architettura × nicchia) con numeri solidi.

---

## Fonti (verificate)

- **MDPI *Aerospace* 2023, 10(2):105** — box-wing/tandem-wing solare ≤25 kg; beneficio strutturale-aeroelastico; TRL basso — https://www.mdpi.com/2226-4310/10/2/105
- **Frediani & Cipolla — IDINTOS** (PrandtlPlane, Univ. Pisa; 30 mesi, 3 modelli) — https://www.researchgate.net/publication/320934669
- **Breaking Defense 2024** — Airbus/Aerovel Flexrotor (~25 kg, >30h, ~30 addetti, prezzo non divulgato) — https://breakingdefense.com/2024/05/airbus-finalizes-acquisition-of-aerovel-as-it-eyes-low-cost-drone-market/
- **CBO 2021 (pub. 57260)** — *Usage Patterns and Costs of Unmanned Aerial Systems* (costo ciclo-di-vita/ora; endurance & attrition) — https://www.cbo.gov/publication/57260

*Confutati (da non usare): vantaggio aerodinamico/L/D 18 del box-wing (il beneficio è strutturale). I numeri di costo assoluti sono STIME parametriche nostre, non dati verificati: da confermare con RFQ e banche dati di procurement prima dello Studio.*
