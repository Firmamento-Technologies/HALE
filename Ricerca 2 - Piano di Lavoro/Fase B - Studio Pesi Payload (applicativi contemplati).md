# Fase B — Studio dei Pesi di Payload (applicativi contemplati)
## Studio di Fattibilità H.A.L.E. — Firmamento Technologies

| | |
|---|---|
| **Documento** | Stima parametrica del **peso dei payload** per tutti gli applicativi/nicchie contemplati nel corpus, per verificare il valore di riferimento "6 kg" usato nel bilancio pesi |
| **Versione** | 0.1 — bozza tecnica |
| **Data** | 2026-07-15 |
| **Input** | Payload citati in `Fase A - Downstream Civile Terrestre` (§ tabella segmenti), `Fase A - Approfondimento Subacquea` (ruoli/payload), `Market Analysis (consolidato)`, requisiti `Trade Study Architetture` REQ-03/04/09 |
| **Scopo** | Rispondere alla domanda operativa: **qualcuno degli applicativi realmente previsti raggiunge i 6 kg?** In caso negativo, **abbassare il numero "6 kg" nel bilancio pesi** al valore massimo effettivamente richiesto (target di progetto). |
| **Metodo** | Censimento dei payload contemplati → peso stimato per fascia (light/mid/heavy) su prodotti commerciali reali di classe mini-UAV/C3 → individuazione del **payload dimensionante** (il più pesante realistico) → confronto con il valore 6 kg. |

> ⚠️ **Onestà tecnica (coerente col Dossier di Verifica):** i pesi sono **stime parametriche** su fasce di prodotti reali di classe. I singoli datasheet vanno **confermati via RFQ** prima dello Studio. Nessun peso qui è misurato sul nostro sistema.

---

## 0. Executive summary — la risposta al quesito

**Nessuno degli applicativi contemplati, preso come payload di missione singola, raggiunge i 6 kg.** Il grosso dei sensori sta **≤ 2 kg**; i più pesanti in assoluto (LiDAR survey-grade, SAR di fascia alta) arrivano a **~3,5–5 kg**; una configurazione **bi-payload ISR realistica** (EO/IR + SAR **o** + relay) sta intorno a **3,5–4,5 kg**.

Il valore **"6 kg" non è un payload di missione: è la capacità strutturale massima dell'AR3 EVO** (benchmark di prestazione, **non** C3 — vedi nota sotto), raggiungibile solo impilando più sensori pesanti. Usarlo come *target di dimensionamento* gonfia il bilancio pesi e rende più difficile chiudere sotto i 25 kg con margine.

> **Raccomandazione:** portare il **payload di progetto da 6 kg → 4 kg** nel bilancio pesi. 4 kg copre la quasi totalità delle missioni contemplate, **inclusa** la configurazione bi-sensore ISR più pesante ragionevole. I 6 kg restano solo come **capacità strutturale massima di riserva**, da onorare *solo se* il bilancio di massa chiude con margine (cfr. `Bilancio di Massa ed Energia`). **Il target di peso payload diventa quindi 4 kg.**

> **Nota di classe (allineata al Dossier S15):** l'AR3 EVO **non è marcato C3** (apertura 3,5–4,2 m > 3 m; UAS militare ISR). È usato qui come **benchmark di capacità payload/prestazione**, non come prova che quella capacità sia raggiungibile *entro la classe C3* (< 25 kg **e** < 3 m). Anzi: restare in C3 comporta un velivolo più compatto → **il payload disponibile è, se mai, inferiore** a quello di un benchmark non-C3, il che rende ancora più corretto tarare il progetto su **4 kg**, non su 6.

---

## 1. Censimento dei payload contemplati

Payload/funzioni di missione citati esplicitamente nei documenti Fase A/B, per nicchia:

| # | Payload / funzione | Nicchia/applicativo di riferimento | Fonte nel corpus |
|---|---|---|---|
| P-1 | **EO/IR gimbal** (elettro-ottico + termico stabilizzato) | Incendi/rischi (N3), ISR marittimo (N1), ispezione | Downstream §tab; Subacquea §payload; REQ-09 |
| P-2 | **RGB + termografico** (mappatura geometrica) | Ispezione ponti/infrastrutture lineari | Downstream §ispezione |
| P-3 | **Multispettrale** | Agricoltura di precisione, forestale/ambientale | Downstream §agri/forestale |
| P-4 | **Iperspettrale** | Agricoltura avanzata, ambientale | implicito Downstream |
| P-5 | **LiDAR** | Dissesto idrogeologico, ispezione lineare, rilievo | implicito Downstream (rischi/ispezione) |
| P-6 | **SAR / radar** | Marittimo (all-weather, notte), subacqueo di superficie | Subacquea §139/146; Market N1 |
| P-7 | **Relay comms / gateway** (multi-radio, LoRaWAN di vallata) | Connettività d'emergenza (N6), gateway subacqueo | Downstream §relay; Subacquea §78 |
| P-8 | **Sonobuoy relay / nodo acustico** | ASW / dominio subacqueo (come *nodo*, non lancio) | Subacquea §78/139 |
| P-9 | **Magnetometro** | MCM / anomalie subacquee | implicito Subacquea (MCM) |
| P-10 | **Calcolo AI a bordo (edge)** | Trasversale (autonomia, detection on-board) | REQ-07 |

> P-10 (edge computing) è al confine tra **payload** e **avionica di missione**: qui lo conteggiamo come elettronica di missione condivisa (vedi `Bilancio di Massa`), non come payload utile, per non contarlo due volte.

---

## 2. Peso stimato per payload (fasce su prodotti reali di classe)

Fasce indicative per classe mini-UAV/C3 (25 kg MTOM). "Design point" = scelta tipica per il nostro profilo; "Max" = fascia alta plausibile.

| # | Payload | Esempi reali di classe (indicativi) | Fascia peso | **Design point** | Max plausibile |
|---|---|---|---|---|---|
| P-1 | EO/IR gimbal | NextVision Raptor/Colibri (~0,35–0,7 kg); Trillium HD25/40, Octopus Epsilon 140/175, DST OTUS (~0,8–1,6 kg); turret 3-sensori EO/MWIR/LRF (~1,5–2,8 kg) | 0,35–2,8 kg | **~1,5 kg** | ~2,8 kg |
| P-2 | RGB + termografico | camere doppie tipo Zenmuse H20T-class (~0,8–1,2 kg) | 0,5–1,2 kg | **~1,0 kg** | ~1,2 kg |
| P-3 | Multispettrale | MicaSense RedEdge-P / Altum-PT + DLS (~0,4–0,8 kg) | 0,3–0,8 kg | **~0,7 kg** | ~0,8 kg |
| P-4 | Iperspettrale | sensori compatti UAV (~0,5–2,0 kg) | 0,5–2,0 kg | **~1,5 kg** | ~2,0 kg |
| P-5 | LiDAR | compatto (Zenmuse L2-class ~0,9 kg); custom Livox/Hesai (~1,0–2,0 kg); **survey-grade (~2,5–3,5 kg)** | 0,9–3,5 kg | **~1,5 kg** | ~3,5 kg |
| P-6 | SAR / radar | NanoSAR / IMSAR NSP-class (~1,0–2,5 kg); **SAR/GMTI fascia alta (~3–5 kg)** | 1,0–5,0 kg | **~2,5 kg** | ~5,0 kg |
| P-7 | Relay comms / gateway | radio multi-standard + gateway LoRaWAN + antenne (~1,0–3,0 kg) | 1,0–3,0 kg | **~2,0 kg** | ~3,0 kg |
| P-8 | Sonobuoy relay / nodo acustico | elettronica relay acustico (~1,0–2,0 kg; le boe **non** sono a bordo) | 1,0–2,0 kg | **~2,0 kg** | ~2,0 kg |
| P-9 | Magnetometro | magnetometro UAV + winch/stinger (~0,5–1,5 kg) | 0,5–1,5 kg | **~1,0 kg** | ~1,5 kg |

**Osservazione:** i **singoli** payload dimensionanti sono **P-6 (SAR)** e **P-5 (LiDAR survey)**. Tutto il resto sta comodamente **≤ 2 kg**.

---

## 3. Il payload dimensionante: quanto pesa la missione più pesante?

Non tutti i payload volano insieme. Le combinazioni realistiche per missione:

| Profilo di missione | Payload combinati | Peso stimato |
|---|---|---|
| **Incendi/rischi (N3)** | EO/IR (P-1) + edge AI | **~1,5–2 kg** |
| **Agricoltura/forestale** | Multispettrale (P-3) *o* iperspettrale (P-4) | **~0,7–2 kg** |
| **Ispezione lineare** | LiDAR (P-5) *o* RGB+termo (P-2) | **~1–3,5 kg** |
| **ISR marittimo (N1)** | EO/IR (P-1) + SAR (P-6) | **~4,0–4,5 kg** |
| **Gateway multi-dominio subacqueo** | Relay/gateway (P-7) + EO/IR (P-1) | **~3,0–3,5 kg** |
| **ISR "pieno carico" (worst-case ragionevole)** | EO/IR (P-1, 2,8) + SAR fascia alta (P-6, 5,0) | **~7,8 kg → oltre il velivolo** |

**Letture:**
- La **missione tipica** sta tra **1,5 e 3,5 kg**.
- La **missione ISR bi-sensore realistica** (EO/IR + SAR *design point*) sta a **~4 kg**.
- Solo impilando i **massimi assoluti** di due sensori pesanti (EO/IR heavy + SAR/GMTI top) si supera abbondantemente il velivolo (~7,8 kg): **questa non è una configurazione di prodotto C3**, è la dimostrazione che il velivolo non è un contenitore infinito.
- **Nessun payload singolo, e nessuna combinazione di missione ragionevole, raggiunge i 6 kg.** Il 6 kg è la capacità strutturale di un benchmark non-C3 più grande, non un requisito di missione del nostro velivolo.

---

## 4. Raccomandazione: 6 kg → 4 kg (payload di progetto)

| Voce | Valore precedente | **Valore raccomandato** | Motivo |
|---|---|---|---|
| **Payload di progetto** (dimensionamento bilancio pesi) | 6 kg | **4 kg** | Copre ~tutte le missioni contemplate, inclusa la bi-sensore ISR (EO/IR + SAR) più pesante ragionevole (~4 kg) |
| **Payload "soglia" minimo** (REQ-03) | 4 kg | 4 kg (invariato) | Resta il minimo accettabile; ora coincide col target di progetto |
| **Capacità strutturale massima** (riserva) | — | 6 kg (solo se il mass budget chiude con margine) | Onorata come *capacità*, non come *requisito di dimensionamento* |

**Conseguenza sul bilancio pesi:** il `Bilancio di Massa ed Energia` va ricalcolato con **payload = 4 kg**. Questo libera **~2 kg** rispetto all'ipotesi 6 kg, contributo decisivo per rientrare nel **target < 25 kg con margine 5%** (≤ 23,75 kg) insieme alla rimozione del solare e alla ri-taratura di carburante/batteria.

**Impatto su REQ-03 (`Trade Study Architetture`):** aggiornare l'Obiettivo da "≥ 6–8 kg" a **"4 kg di progetto (6 kg capacità strutturale max, budget-permitting)"**. La modularità (REQ-04) resta invariata: si cambia payload, non si somma.

---

## 5. Lacune e prossimi passi

| Lacuna | Azione |
|---|---|
| Pesi da datasheet primario (qui fasce) | RFQ ai vendor dei payload shortlist per nicchia (EO/IR, SAR, LiDAR, relay) |
| Potenza elettrica dei payload (non solo peso) | Aggiungere il budget di potenza payload al `Bilancio di Massa ed Energia` (P-6/P-5 sono anche i più energivori) |
| Volume/ingombro e interfaccia bay modulare | Definire l'envelope del bay payload (REQ-04) sul payload dimensionante (~4 kg, SAR/EO-IR) |
| Payload dual-use difesa (magnetometro, acustico) | Verifica classificazione/export e requisiti dedicati in Fase C |

---

*Analisi first-order stage-appropriate per la fattibilità. Pesi parametrici su fasce di prodotti reali di classe, da confermare via RFQ. Conclusione operativa: **payload di progetto 4 kg**, 6 kg come sola capacità strutturale di riserva.*
