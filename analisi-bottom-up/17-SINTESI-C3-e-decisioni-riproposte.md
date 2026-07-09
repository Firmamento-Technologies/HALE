# 17 — Sintesi C3/VTOL + fasce alte, e decisioni riproposte

> **Cosa è.** Chiusura del filone "drone C3": lega il trade study configurazioni VTOL (`14`), l'analisi del vincolo di classe C3 (`15`) e l'espansione delle fasce MALE/HALE (`16`), e **riformula le decisioni aperte** alla luce delle nuove evidenze. Supporto alla decisione; le scelte finali (§4) restano dell'utente.
> **Confidenza aggregata:** MEDIA sulle direzioni tecnico-regolatorie (fisica + normativa citata), BASSA sui numeri assoluti (nessuna prova di volo, nessuna RFQ, nessun CFD).

---

## 1. I tre responsi nuovi (in una riga ciascuno)

| Filone | Verdetto | Confidenza |
|---|---|---|
| **Config VTOL (`14`)** | Per il **prodotto operativo** a Pentema vince il **quadplane / lift+cruise ("VTOL a 5 motori", A2)**: massima maturità COTS (JOUAV/Quantum), transizione più collaudata, e un margine di sicurezza specifico (guasto del motore di crociera ≠ perdita dell'atterraggio verticale). **Tilt-rotor (Wingcopter, A3)** è la 2ª scelta legittima (miglior payload, track record di consegna reale). La **baseline non-VTOL** vince ogni criterio "di volo" ma è **squalificata** dallo spazio ristretto di Pentema. Tilt-wing/tail-sitter/tilt-tri: solo R&D, non prodotto. | Media (aero/GNC qualitativo), bassa-media (frazioni di massa) |
| **Vincolo C3 (`15`)** | La classe **C3 NON è troppo stringente — è in gran parte irrilevante** per la consegna: la Open è preclusa a monte (art. 4 Reg. 947 vieta trasporto DG e rilascio) → **si è sempre in Specific, a qualunque peso**. Il "biglietto Open A3" del C3 per la consegna **non si spende mai**. Il tetto 25 kg è un vincolo **autoimposto** che comprime cargo/BRS/contenimento **senza abbassare la categoria**. Il "cliff dei 25 kg" è netto solo in Open; in Specific superarlo costa al più **+1 gradino di SAIL (II→III)**, non un salto di categoria. | Alta sui [FATTO] normativi, media sulle stime SAIL |
| **Fasce alte (`16`)** | **T3 (MALE):** solo il tattico piccolo 150-220 kg (EMSA/Tekever-class) è realistico, e **solo come servizio in consorzio Y3+** con anchor pubblico che copra €7,5-15M/anno di OpEx; il fisso batte il VTOL-MALE (la penalità di hover cancella la persistenza); nodo regolatorio 150 kg irrisolto (0 TC EASA mai emessi). **T4 (HALE):** attivabile solo come **dimostratore co-finanziato in consorzio** (T4a, $10-25M) o nodo di programma sovrano EU; standalone impossibile; energy-balance inverno 44°N resta lo showstopper. | Alta (base-rate storici), media (economia) |

---

## 2. Le tre scoperte che cambiano il modo di porre le domande

1. **La classe C3 e l'architettura VTOL sono due decisioni diverse che il progetto stava trattando come una.** Il concept interno le lega ("UAV di categoria C3 … potenziale per integrazione VTOL"), ma `14` e `15` mostrano che: la **classe** governa il regolatorio (e per la consegna non conta), l'**architettura VTOL** governa la fisica di volo (e conta molto). Vanno decise separatamente.

2. **Per la consegna, "restare in C3" costa capacità senza dare benefici.** Poiché si è comunque in Specific, ogni kg speso per stare sotto i 25 kg è un kg tolto a payload/contenimento/BRS/ridondanza — proprio ciò che alza il SAIL e rende autorizzabile la consegna. La logica corretta è **"C3 dove serve (dimostratore/EO VLOS iniziale, dove il biglietto Open A3 accelera davvero il time-to-first-flight), Specific-native dove pesa (il velivolo di consegna)"**.

3. **La scelta VTOL pesa sul drag di crociera più della scelta d'ala (72% vs 28% del CD0).** Questo **riconferma da un angolo nuovo** che il box-wing/three-lifting-surface non è ciò che rende competitivo il prodotto: qualunque vantaggio d'ala è di second'ordine rispetto all'hardware VTOL. Il box-wing resta un **dimostratore**, coerente con `22`/`30`/`40`.

---

## 3. Come si aggiornano le due decisioni "storiche" (da `30`/`40`)

- **Posizionamento (servizio / R&D / barbell):** invariato nell'impianto (barbell a tre gambe), ma ora con un **prodotto tecnicamente definito**: un VTOL lift+cruise ≤ o oltre i 25 kg *progettato Specific-native per la consegna*, in bundle con servizio. Nessuna delle nuove evidenze spinge verso l'OEM di airframe: `14` conferma **Buy-COTS/adatta-COTS**, non sviluppo da zero.
- **Ruolo del box-wing (dimostratore vs prodotto):** rafforzata l'opzione **(A) dimostratore R&D**. Tre linee di evidenza indipendenti convergono (aero d'ala ≈0% in `22`/`R6`; drag dominato dal VTOL in `14`; nessuna IP in `40`). L'opzione (B) "box-wing come prodotto" ora deve superare un onere probatorio più alto.

---

## 4. Le decisioni riproposte — bene formulate

Le cinque domande aperte, in ordine di ciò che sblocca di più a costo più basso:

### D1 — Strategia di classe del drone di consegna *(nuova, la più operativa)*
La domanda **non** è "C3 sì/no", ma:
> **Progetto il velivolo di consegna "Specific-native" (dimenticando il tetto 25 kg), tenendo il C3 solo per un dimostratore/EO VLOS iniziale? Oppure vincolo tutta la famiglia sotto i 25 kg per una ragione esterna (es. un bando che premia il C3, o una scelta di semplicità di flotta)?**
Raccomandazione dei dati: **Specific-native per la consegna, C3 come scorciatoia solo per il primo dimostratore/EO.** Serve una verifica: esiste un bando/requisito che premia esplicitamente il C-marking? (falsifying observation di `15`).

### D2 — Architettura VTOL del prodotto *(nuova, tecnica)*
> **Adotto il quadplane/lift+cruise (A2) come architettura del prodotto operativo, adattando un COTS esistente? Confermo il tilt-rotor (Wingcopter-class, A3) come alternativa da tenere aperta per la sola missione cargo pesante?**
Raccomandazione: **A2 per il prodotto; A3 come opzione cargo-pesante; tutto il resto (tilt-wing, tail-sitter, tilt-tri) fuori** salvo scopo puramente dimostrativo. Nota: A2 **non** è un add-on al concept attuale (monoplano, elica in prua) — è una ri-progettazione strutturale, da budgetizzare.

### D3 — Ruolo del box-wing/three-lifting-surface *(aggiornata da `30` §4)*
> **Confermo il box-wing come dimostratore/vetrina IP scorporato dalla linea di prodotto (opzione A), oppure scelgo di pagarne il premio come identità di Firmamento (opzione B)?**
Raccomandazione: **(A)**, ora con tre evidenze convergenti. Se (B), va fatto a occhi aperti e la prova che lo salverebbe è una sola: **2 simulazioni (VLM → RANS)** che falsifichino il "≈0% in crociera" e il "+download in hover" (costo quasi nullo, eseguibili in-house).

### D4 — Posizionamento complessivo *(invariata da `30`/`40`, ora con prodotto definito)*
> **Barbell a tre gambe (prodotto-cassa VTOL+bundle / dimostratore-IP box-wing / servizio-grande su anchor) — confermato? O concentro su una sola gamba per Y1?**
Raccomandazione: barbell, ma **spendere Y1 solo sulla gamba 1** (prodotto+servizio EO), tenendo le altre due come opzioni gated.

### D5 — Ambizione sulle fasce alte T3/T4 *(precisata da `16`)*
> **T3/T4 restano vettore strategico "carta da consorzio" fuori dal P&L (raccomandato), o voglio istruire da subito un percorso attivo su una di esse?**
Raccomandazione: **fuori dal P&L**; T3 solo se compare un anchor pubblico stile-EMSA; T4 solo come dimostratore co-finanziato in consorzio (mai standalone).

---

## 5. Cosa serve per chiudere ciascuna (a costo quasi nullo)

| Decisione | Prova che la sblocca | Costo | Chi |
|---|---|---|---|
| D1 | Verifica se un bando premia il C-marking C3; pre-app ENAC su SAIL reale rotta Pentema | basso (già in `verifiche-primarie/04`) | Firmamento + ENAC |
| D2 | 2-3 RFQ vendor europei (JOUAV-alt/Quantum/Wingcopter) → prezzo+TCO reali | basso (già in `verifiche-primarie/01`) | Fornitori |
| D3 | 2 simulazioni box-wing (VLM→RANS) | quasi nullo, in-house | `aerodynamics-structures-engineer` |
| D4 | 3-5 lettere d'intenzione operatori/PA (prezzo+volume reali) | basso | Firmamento |
| D5 | Nessuna azione finché non compare un anchor firmato | zero | — |

---

### Riga di fondo

> Il filone C3 si chiude con tre chiarimenti che **semplificano** le scelte: (1) la classe C3 è quasi irrilevante per la consegna — progetta **Specific-native**, tieni il C3 solo come scorciatoia per il primo dimostratore; (2) l'architettura VTOL giusta per il prodotto è il **quadplane/lift+cruise**, non il tilt-wing né il box-wing, e pesa sul volo più della forma dell'ala; (3) le fasce alte restano **carta strategica da consorzio**, non procurement. Le decisioni vere restano cinque (D1-D5), ma ora ognuna ha una **prova a basso costo** che la chiude — e tre di queste prove sono già pronte come strumenti in `verifiche-primarie/`.
