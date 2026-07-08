# 12 — Fasce, modularità di piattaforma e business model della "famiglia"

> **Progetto HALE — Firmamento Technologies**
> Autore: Business Model Strategist · Data: 2026-07-08
> **Mandato (riframing utente):** valutare la tesi di una **FAMIGLIA di piattaforme volanti modulari a fasce**, payload intercambiabile (connettività / sensori / trasporto), come veicolo per costruire **credibilità ingegneristica** e abilitare **capitale futuro** fino all'HALE. Pentema/aree interne = **trampolino + gancio politico-finanziario**, non il fine.
> **Basi:** `00-SINTESI-strategica.md` (§8 bivio ambizione/eleggibilità + "barbell"); `03-mercato.md`, `05-piattaforme-costi.md`, `06-finanziabilita.md`, `07-REDTEAM-sintesi.md`. Vincolo di progetto (`CLAUDE.md`): **operatore di servizi, non OEM**.
> **Confidenza aggregata: MEDIA.** Alta sui fatti di costo/finanziamento (ereditati da 03/05/06, già triangolati); media sulle analogie di strategia industriale (casi reali UAV, conoscenza di settore non ri-verificata a luglio 2026); dichiarata per blocco.
> **Regola di lettura:** questo capitolo NON riapre i numeri di mercato/costo (li assume da 03/05/06, red-team-corretti). Lavora **un livello sopra**: architettura di prodotto e packaging del capitale. Non reinflaziona il SOM, non assume l'equity founder come esistente, tiene il €1M come condizionato — coerente con `07`.

---

## 0. La domanda del riframing, in forma decidibile

L'utente propone una tesi diversa da quella deflazionata di `00` ("vai piccolo, service-first, HALE come vettore Y6+"). La tesi è: **esiste UN prodotto-famiglia che copre l'intera finestra di opportunità** (da €300k a €100M) e il pilota aree interne ne è il **primo gradino che genera la credibilità per salire**.

Va scomposta in **tre affermazioni separabili**, perché sono vere a gradi diversi:

| Livello di "modularità" | Affermazione | Verdetto sintetico | Confidenza |
|---|---|---|---|
| **(a) Payload entro una fascia** | Stesso airframe, payload intercambiabile (EO ↔ IR ↔ relay LTE ↔ IoT/LoRa ↔ pod cargo) | ✅ **Realistica e già commerciale** (DJI Matrice+Zenmuse, Quantum, Tekever AR5) | Alta |
| **(b) Architettura comune tra 2-3 taglie** | Un **bus** condiviso (avionica, autonomia, GCS, ICD payload, wrapper ops) declinato su 2-3 airframe di taglia diversa | 🟡 **Parzialmente realistica**: comune il bus/software/ground; **non** la cellula, propulsione, energia, base di certificazione | Media-alta |
| **(c) Un airframe che scala €300k→€100M** | Una singola cellula che va dal micro-VTOL all'HALE solare | 🔴 **Irrealistica.** Nessun costruttore al mondo lo fa; sono 2,5+ ordini di grandezza fisici incompatibili | Alta |

**Conseguenza di impostazione.** Il "prodotto-famiglia" difendibile **non è un aereo**: è un **bus + una capacità operativa + un dato**, riusati su una **scala di 2-3 airframe** di cui ciascuno serve una fascia. Questo riconcilia il riframing con il vincolo `CLAUDE.md` ("operatore, non OEM"): la famiglia è una **famiglia di missioni/servizi** poggiata su una **piattaforma-abilitante proprietaria**, non una linea di prodotti da vendere. È la stessa distinzione che rende Anduril un "software company che vola" e non un OEM di cellule.

---

## 1. Cosa è modulare e cosa no — l'unità difendibile

### 1.1 La regola fisica che uccide il "single airframe"

Le fasce non condividono la fisica dominante:

- **T1 micro/small (COTS o demonstrator leggero, <25 kg):** dominata da **costo/semplicità**; missione EO spot, endurance min-ore. CapEx €40k–1M (`05` classi 1-3).
- **T2 medium long-endurance (MALE-class o heavy VTOL ridondante):** dominata da **endurance + payload fraction + ops persistenti**; CapEx €2–15M, benchmark as-a-service EMSA **€7,5–8,75M/anno** (`05` §6).
- **T3 HALE stratosferico:** dominato dal **bilancio energetico solare a 20 km** (invernale 44°N **non risolto**, `05` §8) e dalla **certificazione Certified**; **$50M–1B/programma**, 0/12 programmi solari operativi commercialmente (`05` §7, DR-013).

Il payload utile passa da ~2,7 kg (T1) a decine di kg (T3); la propulsione da elettrica-batteria a solare-perenne; i materiali da COTS a strutture high-AR ultraleggere (fibra di lino/CFRP del concept). **Nessuna cellula copre questo inviluppo.** I "product family" reali coprono **~1–1,5 ordini di grandezza di taglia**, mai 2,5:

| Costruttore | Famiglia (scala) | Cosa è realmente comune | Cosa NON è comune | Conf. |
|---|---|---|---|---|
| **General Atomics** | Predator → Reaper → SkyGuardian/SeaGuardian → Gray Eagle | **Ground Control Station comune**, avionica, link, ecosistema payload | Cellula/ali/motore per variante; tutte comunque MALE-class (~1 ordine) | Media-alta [conoscenza settore] |
| **Tekever** | AR3 (small) → AR5 (MALE) → AR-Titan | **Stack autonomia + modello as-a-service + ground** | Cellula e classe di peso | Alta [AR5/EMSA da `05`] |
| **Quantum Systems** | Trinity / Vector / Reliant | **Avionica + software + fabbrica** | Configurazione airframe | Media-alta [valut. $8B da `05`] |
| **Anduril** | Ghost / Altius / Roadrunner + **Lattice OS** | **Lattice (software bus) comune a tutto** | Ogni airframe è diverso | Media [conoscenza settore] |
| **Elbit Hermes** | 45 / 90 / 450 / 900 / StarLiner | Avionica + ground segment + famiglia payload | Cellula per taglia (~1,5 ordini) | Media [conoscenza settore] |
| **DJI** | Matrice + Dock + Zenmuse | **Bay payload standard + ecosistema** — modularità (a) pura | — | Alta |

**Lettura:** il denominatore comune di ogni famiglia UAV di successo è **software/autonomia + ground segment + interfaccia payload + (in Tekever) il modello as-a-service** — *mai* la cellula. Chi ha provato a fare "un airframe per tutto" non esiste come categoria.

### 1.2 L'asset che Firmamento può realmente possedere e riusare: il **BUS**

Il "prodotto-famiglia" difendibile per Firmamento è un **bus a quattro strati**, costruito una volta e riusato su ogni fascia:

1. **Avionica/autopilota + stack di autonomia** (mission planning, DAA, gestione link C2/BLOS).
2. **Ground segment / GCS** e pipeline dati (processing EO, anonimizzazione GDPR, delivery).
3. **Interfaccia payload standardizzata (ICD): meccanica + potenza + dati** — è ciò che rende la modularità (a) reale e monetizzabile.
4. **Wrapper operativo as-a-service:** autorizzazioni **ENAC SORA/BVLOS**, piloti, CONOPS, SLA, assicurazione. In Italia questo è **scarso e difendibile**: `03` §3.4 riporta solo **23 autorizzazioni BVLOS in tutto il 2023** — un track record BVLOS è un asset non-commoditizzato, a differenza del "rivendere Copernicus".

> **Perché questo è la risposta corretta al red-team.** `07` §3.3/§3.5 dimostra che "orchestrare Copernicus + droni a noleggio" **non ha barriera** (Wesii/ARPAL lo replicano in <6 mesi). Il bus sopra **sì**: un demonstrator con dati di volo, IP di autonomia, e un pacchetto di autorizzazioni BVLOS/SORA è **replicabile solo con anni e capitale**. Se Firmamento deve costruire un moat, è **qui**, non nell'integrazione di servizio. Questo sposta consapevolmente il baricentro dal "residuo aviazione" (`07` §3.4) verso l'unica aviazione che ha senso: quella che **genera IP e track record trasferibili**.

### 1.3 Dove sta il payload "TRASPORTO" (nuovo rispetto a 00-07)

Il riframing aggiunge il **trasporto** ai payload. Va trattato con onestà:

- **Non condivide l'airframe** con una piattaforma EO/relay high-AR o solare: il cargo è **payload-fraction-dominated** (heavy-lift VTOL, autonomia corta, quota bassa), regime regolatorio e cliente diversi (sanità/emergenza/logistica isole e valli).
- **Condivide il bus** (autonomia, GCS, autorizzazioni BVLOS) → è una **fascia aggiuntiva legittima della famiglia**, non una variante dello stesso velivolo.
- **Casi reali:** consegna medicale/emergenza in aree isolate (Zipline, Wingcopter, Everdrone; trial italiani ASL/isole) — mercato con **anchor pubblico** e **narrativa politica potentissima** ("defibrillatore/farmaci salvavita a una valle spopolata h+1").
- **Verdetto:** opzione **T2-era**, da attivare **solo su un anchor firmato** (ASL/118, gestore isole, Protezione Civile). Presa presto = dispersione. Presa come **secondo caso d'uso del bus dopo il de-risk**, rafforza la narrativa "servizi essenziali alle aree interne" verso Regione/SNAI/CDP senza costare focus. **Non** metterla nel core commitment Y1.

---

## 2. Roadmap della famiglia: T1 → T2 → T3

Comune il **bus** (v1→v2→v3, che matura); diverso l'airframe e il pool di capitale. Questa è la "product-family strategy" difendibile.

| | **T1 — Trampolino** | **T2 — Motore** | **T3 — Vettore** |
|---|---|---|---|
| **Orizzonte** | Y1–2 | Y3–5 | Y6–10 |
| **Airframe** | COTS heavy (JOUAV/Tekever AR3-class) **+ demonstrator custom leggero** C3 (banco IP) | MALE-class / heavy-VTOL ridondante, **as-a-service** (modello EMSA/Tekever); variante cargo su anchor | HALE solare — **solo nodo di consorzio** (EuroHAPS-adjacent), operatore non OEM |
| **Missione** | EO territorio + IoT/emergenza; flight-test IP | ISR persistente dual-use, sorveglianza coste/confini/PC, trasporto medicale | Layer stratosferico persistente ("complementare a IRIS²") |
| **CapEx** | €0,3–1M (`06` Taglia A) | €3–15M (`06` Taglia B, richiede equity esterno) | €50M+ (`06` Taglia C, cambio veicolo) |
| **Pool capitale** | **A**: Coopfond, FESR, SNAI, convenzioni PA | **B**: PNRR-Aero, Horizon, EDF, CDP Venture, VC difesa, credito R&S | Consorzio EU prime-led, fondi sovrani |
| **Business model** | DaaS + servizio operativo + outcome-based | **Capacity/RPAS-as-a-service** + leasing di capacità + R&D contract | Capacity wholesale / operatore infrastruttura |
| **Cosa produce di trasferibile** | Bus v1, dati di volo, **autorizzazioni BVLOS/SORA**, brand, reference PA | Bus v2, ricavi non-grant, partner prime/ASI, TRL-raising | Posizionamento sovrano |
| **Prob. finanziabilità** | 60–75% condizionata (`06`) | 30–50%, solo con equity esterno (`06`) | Fuori portata standalone (`06`) |

**Il salto critico è T1→T2, non T2→T3.** T2→T3 è già noto come "cambio veicolo" (`06` §4.3). Il vero test della tesi-trampolino è: **T1 produce abbastanza credibilità/IP da abilitare il capitale Pool B che finanzia T2?** → §3.

---

## 3. Il trampolino trasferisce credibilità tra i due pool? (il cuore della tesi)

### 3.1 I due pool comprano prove diverse (fatto, da `06`/`07`)

| | Pool A (piccolo, T1) | Pool B (grande, T2/T3) |
|---|---|---|
| Fonti | Coopfond, FESR, SNAI, PA | PNRR-Aero, Horizon, EDF, CDP Venture, VC difesa |
| **Prova che pretende** | Servizio concreto, beneficio cooperativo, ricavi vicini | **Ambizione tecnologica, IP, TRL-raising, dual-use, team, partner prime** |
| Cosa **squalifica** | Troppo grande/rischioso/astratto | "Rivendita di dati satellitari gratis" (`07` §6) |

**Il punto che `07` §6 martella:** i ricavi di un servizio territoriale da €40–150k **non sono la prova che Pool B compra**. Un investitore EDF/difesa/deep-tech non finanzia perché hai venduto NDVI a tre cooperative; finanzia perché hai **volato qualcosa di tuo, hai IP, hai un prime che ti prende, e hai un mercato dual-use grande**. Quindi:

> **La credibilità NON si trasferisce via ricavi. Si trasferisce via asset ingegneristici e track record.** Un pilota che è **solo servizio** (rivendita Copernicus) trasferisce **quasi zero** verso Pool B — e questo è esattamente il fallimento previsto in `07` §6 e nel pre-mortem §8.5 ("squalificati dalla money grande per essere andati piccoli").

### 3.2 Cosa trasferisce davvero (e come progettare T1 perché lo produca)

Il trampolino regge **solo se T1 è ingegnerizzato per produrre gli asset che Pool B riconosce**. Lista degli asset trasferibili, per forza di trasferimento:

| Asset prodotto in T1 | Trasferisce a Pool B? | Come garantirselo in T1 |
|---|---|---|
| **Autorizzazioni ENAC BVLOS/SORA + track record voli sicuri** | **Forte** (scarso: 23 auth/2023) | Fare voli BVLOS reali, non solo VLOS demo |
| **Demonstrator custom + dati di volo/aeroelasticità (lino-composite)** | **Forte** (IP + TRL) | Finanziare il demonstrator **come R&D separata** (§4), non come procurement servizio |
| **Partnership prime/agenzia (CIRA, ASI, TAS-Leonardo, Polito)** | **Forte** (eleggibilità EDF/PNRR-Aero) | Firmare ≥1 MoU R&D in T1 |
| **Brand "pioniere HAPS IT per Aree Interne" + reference Regione** | Media (apre porte, non finanzia) | LoI Regione + presenza pubblica |
| **Ricavi non-grant del servizio** | **Debole** verso B (ma **forte** verso A e verso sostenibilità) | Perseguirli per Pool A, non aspettarsi che convincano B |

**Corollario operativo (il cuore della raccomandazione):** T1 **non deve essere un puro servizio**. Deve essere un **servizio con un cuore R&D**: il servizio EO/IoT genera i ricavi Pool A e il track record BVLOS; il **demonstrator custom leggero** (il box-wing del concept, €150–400k come da `05` §3.2a, **scorporato dal P&L servizio**) genera l'IP e il TRL che Pool B compra. Sono **due gambe che condividono il bus e la narrativa, ma con due P&L separati** — è il **barbell** di `00` §8 reso concreto.

### 3.3 Il barbell operativo (schema)

```
                    NARRATIVA COMUNE (gancio, non P&L)
         "Sovranità stratosferica europea radicata nel servizio
          alle Aree Interne — complementare a IRIS²"
                              │
        ┌─────────────────────┴─────────────────────┐
   GAMBA A: SERVIZIO                          GAMBA B: R&D
   (Pool A — vicino, ricavi)                  (Pool B — lontano, IP)
   T1 EO/IoT/emergenza, as-a-service          Demonstrator custom → T2 dual-use → T3 HALE
   COTS + wrapper ops                         box-wing/HALE lineage
   P&L che deve tendere all'autofin.          P&L R&D, grant-funded, NON appeso al servizio
        └──────────────── BUS CONDIVISO ───────────────┘
     (avionica · autonomia · GCS · ICD payload · autorizzazioni BVLOS)
```

**Regola di non-contaminazione (da `00` §8.3, ribadita):** il servizio **non** deve dipendere dal successo dell'R&D (altrimenti muore col rischio HALE); l'R&D **non** deve gravare sul P&L del servizio (altrimenti il servizio è già in perdita). Il **bus** e la **narrativa** sono l'unico ponte. Questo è ciò che impedisce di "cadere tra due sedie" (`00` §8, `07` §6).

---

## 4. Business model della piattaforma modulare

### 4.1 Come si monetizzano nicchie diverse con lo stesso asset (modularità (a))

Il vero argomento economico della modularità **entro una fascia** è l'**utilizzo dell'asset**: lo stesso airframe genera più linee di ricavo riconfigurando il payload → **maggiore tasso di utilizzo → migliore unit economics**. È il caso in cui la modularità è un **asset di business genuino**, non narrativa:

| Payload sul medesimo airframe | Cliente | Modello | Pricing (da `03`/mandato, [STIMA]) |
|---|---|---|---|
| EO RGB+IR (NDVI, mapping, frane) | Coop agri, Enti Parco | **DaaS** pacchetto dati | €5–20k/anno aggregato (`03` r.53/56) |
| IR persistente (early-detection incendi) | PC/AIB | **Outcome-based** pay-per-event | €1–10k/evento [mandato] |
| Relay LTE/LoRa (emergenza/IoT) | PC, Comuni | **Servizio operativo** ore-volo + canone | €0–100k/anno (`03` r.49) |
| Pod cargo (medicale) | ASL/118 | **Capacity-as-a-service** per-consegna | da definire su anchor |

**Proof-point reali:** DJI Matrice+Zenmuse (payload hot-swap commerciale di massa), Quantum "payload modulare", Tekever AR5 "SAR/EO/IR/relay modulare" (`05` §6). La modularità-payload **è tecnologia matura e monetizzabile**: qui non c'è rischio di tesi.

### 4.2 Il modello che regge davvero i ricavi non-grant: **as-a-service (T2)**

Il segmento `03` mostra che il **ricorrente non-grant** in T1 è strutturalmente piccolo (€40–150k, worst €30–70k). Il modello che porta ricavi **veri e non-grant** è il **capacity/RPAS-as-a-service di T2**, di cui esiste **benchmark pubblico reale**: **EMSA→Tekever, €30–35M/4 anni/4 velivoli, equipaggio incluso** (`05` §6). Implicazioni:

- Non si **vende** la piattaforma (coerente con `CLAUDE.md`): si vende **capacità operata** (ore-orbita, copertura-area, evento) con SLA.
- Cliente non è la coop né il micro-comune: è **PC nazionale, difesa, sorveglianza coste/confini, grandi utility** — pagatori con budget reale, dove `03` mostrava porte chiuse in T1 ma che in T2 dual-use si riaprono.
- **Leasing di capacità**: modello wholesale/white-label verso telco (NTN backhaul on-demand) o verso un prime — futuro, post-validazione.

### 4.3 Cosa NON fare (dal mandato + red-team)

- **No subscription puro alla PA** (`03`: la PA vuole canoni con SLA e convenzioni, non SaaS).
- **No "scaling SaaS" del servizio territoriale:** `07` §5 dimostra che lo scale-up SNAI è **×22 pratiche di consulenza**, non network-effect. Il servizio è margine piccolo per definizione; la scala vera è in T2 dual-use, non in "22 Pentema".
- **No vendita di airframe** (non siamo OEM): monetizzazione sempre via servizio/capacità/dato.

---

## 5. Packaging per finanziatore — quale fascia, quale narrativa, a chi

**La modularità è un asset di vendita O un red flag?** Dipende dall'interlocutore. Regola generale: **modularità = asset SOLO se raccontata come "bus/piattaforma che scala", MAI come "inseguiamo molte nicchie"** (quest'ultima lettura è il red flag "manca focus" per chiunque scriva assegni).

| Ente | Pool | Fascia da presentare | Narrativa | Modularità: asset o red flag? | Key terms / ticket |
|---|---|---|---|---|---|
| **Coopfond / Legacoop** | A | **T1 servizio** | Servizio mutualistico territoriale, coop **co-titolari**, lavoro, servizi essenziali | 🔴 **Red flag** se enfatizzata ("non siete focalizzati sulla comunità"). Citare solo come "future-proofing" 1 riga | €50–250k, cofin. 50%, ≥10 coop |
| **Regione Liguria / FESR** | A/ponte | **T1 servizio** | S3 "sicurezza e qualità della vita nel territorio"; **efficienza dell'investimento pubblico** (un asset, molti bisogni regionali: frane+incendi+agri+emergenza) | 🟡 **Asset lieve**: "un investimento pubblico, molte funzioni" vende. Ancorare a convenzione concreta | €100–150k, 50% fondo perduto |
| **SNAI / PA territoriale** | A (gancio) | Servizio + **cargo medicale** (narrativa) | Servizi essenziali a territori spopolati; **defibrillatore/farmaci alla valle** | 🟡 Asset narrativo (potente politicamente) | Grant indiretto via ApQ |
| **CDP Venture / capitale di rischio** | B | **Bus + T2 dual-use** | **Piattaforma/bus che scala su mercati grandi dual-use** (à la Anduril Lattice / GA GCS); il servizio T1 è **de-risk/track record**, non la tesi | 🟢 **Asset forte** — MA solo come *platform play*, con mercato grande a valle (difesa/sovranità). Senza quello, red flag "poco focus" | €0,5–5M equity, diluizione |
| **PNRR-Aerospazio / MIMIT / ASI** | B | **Gamba R&D: demonstrator → T2/T3** | Ambizione, TRL-raising, **filiera nazionale dual-use**, IP sovrano; servizio = demonstrator applicativo | 🟢 **Asset**: "famiglia nazionale di piattaforme dual-use" | €0,5–3M, cofin. 20–50%, via partnership prime |
| **Horizon Europe / EDF** | B | **T3 HALE come nodo di consorzio** | Autonomia strategica EU, EuroHAPS-adjacent, **complementare a IRIS²** (mai "alternativa a Starlink", cfr. `CLAUDE.md`) | 🟢 Asset, ma **solo in consorzio 3+ Stati**; ticket d'ingresso = flight-test + IP + prime partner | €5–30M, consorzio |

### 5.1 Il gancio "aree interne + sovranità": quali porte apre davvero

- **Verso Pool A:** apre **direttamente** e finanzia (Coopfond già deliberato €50k al progetto *"H.A.L.E. – Cooding II"* — il nome HALE/aerospazio è già la pitch che ha funzionato, `06` §1).
- **Verso Pool B:** apre come **frame narrativo/legittimante** ("radicati nel servizio pubblico, non un vendor astratto") ma **non finanzia da solo**. Pool B firma su **ambizione+IP+dual-use**. Il gancio evita che Pool B ti veda come "solo un service reseller"; non sostituisce la prova ingegneristica.

> **Sintesi packaging:** stessa azienda, **due pitch deck**. Uno "servizio mutualistico territoriale" (Pool A, T1, modularità nascosta). Uno "famiglia di piattaforme dual-use su bus proprietario, radicata nel servizio alle aree interne" (Pool B, T2/T3, modularità in evidenza come platform play). Il barbell (§3.3) è ciò che rende **onesti entrambi** senza contraddizione.

---

## 6. Value Proposition — 3 segmenti (Osterwalder, sintetico)

**A. PA/Protezione Civile (B2G, T1→T2)** — *Jobs:* monitorare dissesto/incendi, rispondere in emergenza, rendicontare a fondi di coesione. *Pains:* budget vincolato, in-house ARPAL, appalti lenti. *Gain creators:* persistenza+alert termico, dati GDPR+SLA, **efficienza di un asset multi-funzione**, ROI sociale misurabile. *Rischio (red-team):* il "job" è già coperto in-house/Copernicus → vince solo con **convenzione pluriennale + track record BVLOS** che l'in-house non ha.

**B. Cooperative (B2B, T1)** — *Jobs:* NDVI/salute colture, connettività backup, restare rilevanti. *Pains:* micro-budget, nessuna competenza aerea. *Gain creators:* **co-titolarità** (non "vendita SaaS"), mutualità, dati d'area. *Rischio:* è cassa piccola e grant-dipendente (`03`/`07` doppio conteggio) → trattare come **canale/legittimazione**, non ARR.

**C. Capitale Pool B / difesa (investitore, T2/T3)** — *Jobs:* schierare capacità ISR/sovrana dual-use, TRL-raising con de-risk. *Pains:* startup senza flight-test/IP/track record sono unbankable. *Gain creators:* **bus proprietario + autorizzazioni BVLOS scarse + demonstrator con IP + partner prime**. *Rischio:* se T1 è "solo servizio", non ci sono i gain → il capitale non entra (il fallimento di `07` §6).

---

## 7. Verdetto e criteri di falsificazione

### 7.1 Verdetto: la modularità è un asset o una dispersione?

**È un asset strategico — a tre condizioni non negoziabili, altrimenti è dispersione:**

1. **Modulare è il BUS, non l'airframe.** Modularità (a) payload-entro-fascia e (b) bus-su-2-3-taglie = asset reale e industry-proven. Modularità (c) un-airframe-per-tutto = irrealistica: **non venderla mai**, è il red flag che squalifica.
2. **Barbell con P&L separati.** Il servizio T1 (Pool A) e la R&D demonstrator→T2/T3 (Pool B) condividono **solo** bus e narrativa. Contaminarli = cadere tra due sedie (`07` §6).
3. **T1 ingegnerizzato per produrre asset trasferibili** (autorizzazioni BVLOS, demonstrator+IP, partner prime), non solo ricavi. Un T1 "rivendita Copernicus" trasferisce **zero** a Pool B → il trampolino non scatta.

**Come venderla ai finanziatori:** due pitch. A Pool A "un asset pubblico multi-funzione, servizio mutualistico focalizzato" (modularità sottotraccia). A Pool B "famiglia dual-use scalabile su bus proprietario + track record operativo" (modularità = platform play, con mercato grande a valle). Mai un pitch solo che prova a fare entrambi — è il red flag "manca focus".

### 7.2 Kill criteria (falsificabili, coerenti con `00` §7 / `07` §9)

- **Trampolino fallito:** se a M+18 il T1 non ha prodotto **≥1 autorizzazione BVLOS reale** *e* **≥1 MoU con prime/agenzia** *e* dati di volo del demonstrator → gli asset trasferibili non esistono → Pool B resta chiuso → la tesi-famiglia decade a "servizio puro Pool A".
- **Founder equity (da `07` §2.3):** senza delibera equity founder ≥€150k per iscritto entro M+9, la gamba R&D non parte e T1 resta al floor €300–600k (`06` §5) — niente demonstrator, niente trampolino.
- **Dispersione:** se in 24 mesi si aprono >2 fasce/payload contemporaneamente senza anchor firmato per ciascuno (incl. cargo) → segnale di perdita di focus → i finanziatori Pool B leggono red flag → ritirare le fasce non-ancorate.
- **Bus non proprietario:** se a M+24 il "bus" è solo integrazione di COTS senza IP/autonomia propria né track record BVLOS esclusivo → non c'è moat (`07` §3.5) → la famiglia è indistinguibile da uno dei 657 operatori droni → riconsiderare l'intera tesi.

---

## 8. Fonti e confidenza

**Interne (ereditate, già triangolate):** `00-SINTESI-strategica.md` §8 (barbell, bivio); `03-mercato.md` (SOM, pagatori, 23 BVLOS/2023, Wesii); `05-piattaforme-costi.md` (classi, EMSA €30-35M, demonstrator €150-400k, HALE $50M-1B); `06-finanziabilita.md` (Taglie A/B/C, floor equity, strumenti); `07-REDTEAM-sintesi.md` (doppio conteggio, moat assente, squalifica Pool B). Vincolo `CLAUDE.md` (operatore non OEM; linguaggio IRIS²).

**Casi reali di strategia modulare UAV (conoscenza di settore, cutoff gen-2026, NON ri-verificati a luglio 2026 — confidenza media):** General Atomics (GCS comune, famiglia MALE); Anduril (Lattice OS come bus software comune); Elbit Hermes (ladder 45→900); AeroVironment (portfolio multi-taglia); Zipline/Wingcopter/Everdrone (cargo medicale). Casi con numeri già nel repo (confidenza più alta): Tekever AR3/AR5 + EMSA; Quantum Systems ($8B); Skydweller ($40M Series A, Leonardo); Wingtra/Quantum funding.

**Limiti dichiarati:** (1) le analogie industriali sono *pattern*, non garanzie che Firmamento le replichi; (2) la forza di trasferimento della credibilità T1→Pool B è **stima**, non dato — il vero test è empirico (kill criteria §7.2); (3) il numero founder-equity resta **assente dai documenti** (`06`/`07`) e l'intera gamba R&D vi poggia; (4) questo capitolo assume validi i numeri di `03`/`05`/`06` red-team-corretti e non li riapre.

**Azione prima del gate:** decidere esplicitamente il posizionamento (`00` §8: servizio puro / R&D-first / barbell). Questo capitolo raccomanda il **barbell** e ne fornisce l'architettura, ma la scelta è dell'utente e seleziona tutto il resto.
