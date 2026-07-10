# Piano rifatto da zero — Metodo, criteri e sequenza

> **Origine.** Operazionalizza la riunione del **10/07/2026** ([verbale](./2026-07-10-verbale-briefing-strategico.md)). La riunione **non ha deciso un prodotto**: ha definito un **metodo** — *prima il mercato (downstream), poi i prodotti* — e i **parametri** da ottimizzare. Questo documento traduce quel metodo in un piano di lavoro, **neutro sulla piattaforma** (non assume né HALE, né VTOL, né C3): la soluzione è un **esito**, non una premessa.
>
> **Stato:** bozza di metodo da validare con il team. Le risposte preliminari (§5) e l'annesso marittimo (Annex A) poggiano su ricerca già in repo e su un primo screening a fonti reali; sono **input da ri-validare**, non verdetti.

---

## 0. Cosa significa «rifare da zero»

«Da zero» **non** vuol dire ignorare l'archivio (che è ampio e in gran parte utile), ma **non dare per acquisite le conclusioni** e **rifare il ragionamento nell'ordine giusto**:

1. **Neutralità sulla piattaforma.** La domanda non è *«come costruiamo un velivolo?»* ma *«qual è il servizio che il mercato paga, e qual è la soluzione minima che lo eroga meglio?»*. La soluzione può anche **non essere un velivolo** (es. sensori a terra, COTS a noleggio, satellite orchestrato): va tenuta sul tavolo come opzione, non esclusa per gusto.
2. **L'archivio come *input*, non come *risposta*.** I report esistenti (`analisi-bottom-up/00→30`, `ricerca-approfondita/R1→R7`, `studio-di-fattibilita/cap-*`) diventano **materiale da riesaminare e ri-validare** contro i criteri della riunione — non tesi da difendere. La mappa in §7 dice cosa c'è già.
3. **Ogni numero cita la fonte** (disciplina `epistemic-rigor` del progetto) e dichiara la **confidenza**. Nessun claim entra nel piano senza provenienza.

> **Nota di realtà da mettere subito sul tavolo.** In riunione il ragionamento tende ancora al *«costruiamo una cosa figa che vola»* (istinto legittimo). La ricerca già fatta dal progetto, però, converge su un punto scomodo: **per il *servizio* conviene comprare COTS**, il velivolo *custom* ha senso **solo come dimostratore R&D/vetrina**, e per alcuni bisogni **la soluzione migliore non vola**. Questo non è un verdetto da imporre: è **l'ipotesi di lavoro più forte da falsificare** in Fase 2. Se il metodo «da zero» la conferma di nuovo, va accettata; se la smentisce con dati nuovi, si cambia.

---

## 1. Il ribaltamento della domanda

| Ordine sbagliato (platform-first) | Ordine corretto (demand-first) |
|---|---|
| Scelgo il velivolo (HALE/MALE/VTOL/C3) → cerco a cosa serve | Individuo il **servizio pagato** → derivo la **soluzione minima** che lo eroga → **solo allora** scelgo (se serve) il velivolo |

Motivazione condivisa in riunione (Ema; suggerimento del membro **ASI** al Festival dello Spazio): **concentrarsi sul downstream / servizi**, non sulla vendita del mezzo — coerente col modello di business inderogabile del progetto (Firmamento = **operatore di servizi, non OEM**).

---

## 2. I criteri da ottimizzare (dalla riunione) — e le loro tensioni

I parametri fissati in riunione **non sono indipendenti**: alcuni si oppongono. Renderli espliciti evita di inseguire un ottimo impossibile.

| # | Criterio | Direzione | Come si misura | Tensione principale |
|---|---|---|---|---|
| C1 | Autonomia | max | ore di volo utile in missione | **↔ C3/peso** e **↔ costo**: 24 h a <25 kg *elettrico* non esiste |
| C2 | Costo di realizzazione | min | € CapEx sistema + € time-to-service | ↔ autonomia, ↔ prestazioni |
| C3 | Modularità (payload intercambiabili) | max | n. payload su bus comune / costo di switch | ↔ **buy COTS** (avioniche chiuse ⇒ niente bus comune) |
| C4 | Numero di casi d'uso | max | n. missioni servibili con la stessa piattaforma | ↔ **focus**: troppe nicchie = *morte per mille nicchie* |
| C5 | Peso / categoria | min (pref. **C3 <25 kg**) | MTOM; categoria EASA (Open/Specific) | abilita basso attrito reg. **ma** limita autonomia/raggio/payload |
| C6 | Attrattività investitori | max | interesse Pool A (territoriale) e Pool B (R&D) | i due Pool **premiano cose opposte** (§6) |
| C7 | Leva pubblico-privato | max | % cofinanziamento; n. enti coinvolti | richiede **anchor firmato**, non solo interesse |

> **Il «trilemma» chiave, confermato dal primo screening (Annex A):**
> **`C3 <25 kg` + `basso costo` + `endurance/raggio «da missione seria»` → se ne ottengono due, non tre.**
> Un C3 <25 kg **elettrico** low-cost ⇒ 30–90 min e 5–15 km. Per avere endurance «vera» a <25 kg servono VTOL/ala-fissa a **combustione/ibridi** (classe *Airbus Flexrotor*, 25 kg ma benzina) che **non sono low-cost** (sistema ~€0,8–1,5M). Questo va tenuto presente in **ogni** discussione di prodotto.

---

## 3. Metodo — le due fasi

### FASE 1 — Analisi di mercato del *downstream* (il mercato definisce il prodotto)

**Scopo:** individuare la/le **nicchia/e pagante/i più larga/e e difendibile/i**, non «tutti i mercati possibili».

**Perimetro (verticali da scansionare):**

| Verticale | Missioni | Committente-tipo |
|---|---|---|
| V1 — Connettività aree interne | resilienza emergenza, IoT d'area, relay | Regione/Comuni/PC, MNO |
| V2 — Osservazione della Terra | frane/incendi/vegetazione, post-evento, agricoltura | Regione, Enti Parco, ARPA, PA |
| V3 — Emergenze / Protezione Civile | overwatch, early-detection, supporto | PC, VVF, Regione |
| V4 — Logistica (medicale) | sangue/campioni/farmaci/AED | ASL/118 |
| V5 — **Marittimo / porto / costiero** | port security, ambiente vicino-costa, SAR, anomalie AIS | AdSP, terminalisti (MSC), AMP/ARPA, Guardia Costiera |
| V6 — Sorveglianza ambientale/confini | coste, aree protette, infrastrutture critiche | PA, prime (subfornitura) |

**Per OGNI verticale, cinque domande a prova di fonte:**
1. **Chi paga** (ente/impresa reale, non «il mercato»)?
2. **Quanto vale** (budget unitario €/anno o €/ora; contratti reali)?
3. **Con quale ciclo** (grant / convenzione / procurement / B2B privato) e **tempi**?
4. **Qual è il sostituto** gratuito/economico (Copernicus, Starlink, torri fisse, satellite AIS/SAR, COTS a noleggio, sistemi manned)? *Se il sostituto vince, il verticale cade.*
5. **Qual è la barriera d'ingresso difendibile** (tecnologica? mandato pubblico/cooperativo? radicamento SNAI? canale B2B già agganciato)? *Se la barriera è solo tecnologica, un incumbent ci batte.*

**Output Fase 1:** ranking dei verticali per **valore pagante × difendibilità × vicinanza del ricavo**, con la nicchia-àncora selezionata e i sostituti che la minacciano.

### FASE 2 — Analisi comparativa dei prodotti / architetture

**Regola:** entra **solo dopo** che Fase 1 ha detto *quale servizio* e *quale profilo di missione*. Il payload e la persistenza richiesti dalla nicchia **selezionano** la piattaforma.

**Opzioni sul tavolo (nessuna esclusa a priori):**

| Opzione | Cos'è | Buy/Build |
|---|---|---|
| S0 — **A terra / non volare** | torri sensori + ripetitore su crinale; satellite orchestrato | Buy |
| T0 — COTS spot | multirotore/VTOL commerciale a noleggio | Buy |
| T1 — C3 <25 kg (incl. box-wing) | piccolo VTOL/ala-fissa modulare | **Build** (solo se è l'IP) |
| T2 — mid-VTOL ibrido | 25–200 kg, 10–16 h | Buy COTS (JOUAV/Flexrotor…) |
| T3 — MALE | offshore/area vasta persistente | Buy (prime) / subfornitura |
| T4 — HALE stratosferico | copertura regionale persistente | Build R&D (Y6+) |

**Assi di confronto (trade study / DOCFAP):** costo CapEx + time-to-service · limiti tecnici · TRL · autonomia (C1) · peso/categoria (C5) · modularità reale del bus (C3) · attrito regolatorio (SAIL) · finanziabilità (Pool A/B) · **buy-vs-build**.

**Output Fase 2:** matrice ponderata → **soluzione derivata dal mercato** (che può essere «S0 + COTS», non un velivolo custom) + eventuale **linea R&D scorporata** (dimostratore).

---

## 4. Errore da non ripetere: «autonomia» ≠ «alta quota»

Chiarimento tecnico emerso in riunione (Gigi ha ragione sulla fisica): per **endurance lunga** l'**ala fissa** batte il VTOL puro (il VTOL si porta dietro il *drag*/peso dei motori di sollevamento). Un *«VTOL 24 h»* a bassa quota **non è** un HALE (che è definito dalla **quota** ~20 km, non dall'autonomia). Le tre categorie vanno tenute distinte: **VTOL** (decollo verticale/hover) · **long-endurance** (ore di volo) · **HALE** (quota stratosferica). Confonderle porta a requisiti impossibili.

---

## 5. Le 4 domande aperte della riunione — risposta preliminare dal corpus

> *Risposte ancorate ai report già in repo (`analisi-bottom-up/00`, `20`, `30`; `ricerca-approfondita/R6`) e al primo screening marittimo. Confidenza dichiarata. **Da ri-validare in Fase 1/2**, non conclusioni chiuse.*

**Q1 — Un prodotto generalista («barcone») o due progetti specifici?**
Né l'uno né l'altro in purezza. Il corpus indica un **barbell**: **operativamente focus su una nicchia-àncora alla volta** (il «barcone» generalista è letto come *red flag di dispersione* dai finanziatori territoriali — Pool A), **ma architetturalmente un unico bus modulare** («platform play») che è esattamente ciò che attrae i fondi R&D — Pool B. Il rischio reale non è «uno vs due» ma **inseguire >2 nicchie senza un committente firmato per ciascuna** (*morte per mille nicchie*). *(Fonte: `20-SINTESI-fasce`, `00-SINTESI §8`. Confidenza media.)*

**Q2 — VTOL, ala fissa o box-wing?**
Per l'**endurance**: **ala fissa** (o VTOL-ala-fissa ibrido) > VTOL puro. Il **box-wing** non dà vantaggio di crociera misurabile (~0%) né IP brevettabile: tenerlo **solo** come **dimostratore/vetrina**, non come il prodotto. Per il *servizio*, la scelta economica è **comprare COTS** (T2), non costruire. *(Fonte: `30-SINTESI`, `22-boxwing`, `R6-boxwing-aerodinamica`. Confidenza media.)*

**Q3 — Un C3 <25 kg fa 24 h di autonomia?**
**No, non elettrico e non low-cost insieme.** Un C3 <25 kg elettrico ⇒ **90 min–3 h**. Le 24 h a quella taglia esistono solo con **combustione/ibrido** (es. Flexrotor 25 kg a benzina), che **non è low-cost** né «facile». Quindi il vincolo C5 (peso) e il criterio C1 (autonomia) **si escludono** oltre una certa soglia. *(Fonte: corpus fasce `10`/`20`; corroborato dall'Annex A. Confidenza alta.)*

**Q4 — Quanto pesa il payload e come influenza la piattaforma?**
È il payload a **selezionare il tier**: gimbal EO/IR leggero (1–5 kg) sta su C3/T2; radar marittimo + SATCOM + DAA (necessari offshore) **non** stanno sotto 25 kg. Quindi **la nicchia (Fase 1) fissa il payload, e il payload fissa la piattaforma** — non il contrario. *(Fonte: `10-fasce-engineering`, Annex A. Confidenza media-alta.)*

---

## 6. Le decisioni che restano al team (non tecniche)

Il metodo non può decidere queste al posto vostro; vanno messe a verbale:

1. **Posizionamento (il vero interruttore):** *Servizio puro* (Pool A, margini piccoli, grant-dipendente) · *R&D-first* (Pool B, upside alto, il servizio è pretesto) · **Barbell** (entrambi scorporati, narrativa comune). I due Pool premiano cose **opposte**: la versione «piccola/COTS» è *eleggibile* per Pool A ma *squalificata* da Pool B, e viceversa. *(vedi `00-SINTESI §8`)*
2. **Identità box-wing:** è l'identità di Firmamento (si paga il premio, scorporato come R&D) o si adotta un VTOL/ala-fissa convenzionale più economico?
3. **Marittimo sì/no e in che ruolo** (vedi Annex A): nicchia porto+ambiente near-shore in proprio, **o** subfornitura ai prime, **o** deprioritizzare.

---

## 7. Cosa esiste già (input da ri-validare) e cosa manca

| Serve per | Già in repo (input) | Gap da colmare |
|---|---|---|
| Fase 1 mercato | `analisi-bottom-up/03,11`; `ricerca-approfondita/R1,R7`; `cap-07` | **V5 marittimo** (solo primo screening, Annex A); willingness-to-pay reale (LoI) |
| Fase 2 prodotti | `analisi-bottom-up/05,10,20,30`; `R3,R6`; `cap-06` | trade study aggiornato ai criteri riunione; sim. box-wing VLM→RANS |
| Regolatorio | `analisi-bottom-up/04,13`; `cap-05` | SORA marittima near-shore (bozza in Annex A) |
| Finanza | `analisi-bottom-up/06,23`; `cap-08` | unit economics con prezzo/volume **reali** |
| Verbale riunione | **questo commit** (`riunioni/`) | — |

> **Nota di rigore:** il corpus **è ampio ma va trattato come materiale, non come verità acquisita**. Il valore di «rifare da zero» è ri-eseguire il ranking di Fase 1 con i criteri della riunione e verificare se la nicchia-àncora regge ai sostituti.

---

## 8. Gate e kill-criteria (demand-first)

- **Gate 0 (subito, <€30k):** *prova di domanda*, non tecnica — ottenere **1 LoI Regione + 1 convenzione** (Ente Parco/AdSP/ASL). **Nessun CapEx di piattaforma prima di una firma.**
- **Gate 1 (dopo la firma, ≤€1M/18–24 mesi):** soluzione derivata (Fase 2) sulla nicchia-àncora; equity founder deliberata.
- **Gate 2 (con ricavi):** scale-up / linea R&D dimostratore su bando **separato**.
- **Kill-criteria:** nessun ente firma ≥€100k/anno entro Gate 1 → mercato falsificato · un sostituto (torri/COTS/satellite/prime) eroga lo stesso servizio → la nicchia cade · >2 nicchie senza anchor ciascuna → ridurre a una.

---

## 9. Prossimi passi operativi

1. **Validare questo metodo** col team (soprattutto §6, le tre decisioni).
2. **Completare V5 marittimo** (Annex A è parziale: mancano competitor/sostituti, reality-check EO subacqueo, platform-fit, red-team — interrotti per limite di sessione, ripristinabili).
3. **Rieseguire il ranking Fase 1** su tutti i verticali con le 5 domande di §3.
4. **Solo dopo**, Fase 2: trade study ponderato sui criteri di §2.
5. In parallelo (a costo ~0): **1 LoI** e la **simulazione box-wing** — le due prove che sbloccano le decisioni di §6.

---

## Annex A — Primo screening del vettore marittimo (V5) *(parziale)*

> Prodotto da 2 dei 6 filoni previsti (mercato/missioni + regolatorio); **competitor/sostituti, reality-check EO subacqueo, fit-piattaforma e red-team NON sono stati completati** (limite di sessione, reset 16:00 UTC). Trattare come **primo screening**, non analisi chiusa. Il canale «Cegeno/MSC» è un **lead non verificabile pubblicamente**: trattato come contatto commerciale, non come pipeline di ricavo.

**Verdetto preliminare:** perseguire il marittimo **solo** come nicchia **porto + ambiente vicino-costa + supporto SAR/PC locale** (dove il C3 <25 kg è idoneo) e come **subfornitura/integrazione-dati ai prime**; **non** promettere sorveglianza offshore/confini (mismatch fisico del C3 <25 kg + mercato saturato). *Confidenza: media sulla direzione, bassa sul sizing italiano (stima non triangolata).*

**Reperti chiave (fonti reali):**

- **Il denaro grosso è offshore ed è già preso dai prime MALE.** EMSA offre la sorveglianza RPAS **gratis** agli Stati membri (paga i prime) → **disintermedia** la vendita diretta alla Guardia Costiera. Framework EMSA–REACT (CLS+**Tekever AR-5**, MALE 180 kg/20 h): **€30M/4 anni**. Frontex: **€50M+€50M** (2020, Airbus/IAI Heron + Elbit Hermes) **+€84,5M** (2021). *(Confidenza alta.* Fonti: emsa.europa.eu/we-do/surveillance/rpas.html; navalnews.com 2021-10; statewatch.org 2020-11.*)*
- **Genova è «acqua di casa»:** EMSA ha già operato l'**AR-5 Tekever da Sarzana** a supporto della Guardia Costiera (safety/security, SAR, cetacei nel Santuario Pelagos). *(Alta.* Fonte: maritimecyprus.com 2023-04.*)*
- **La nicchia aggredibile da un operatore cooperativo asset-light:** (1) **port-basin security & ambiente** per AdSP Genova/Trieste e terminalisti (MSC/PSA/Spinelli) — canale **B2B privato**, procurement più rapido, ricavo più vicino; (2) monitoraggio ambientale **near-shore** per AMP/ARPA/Regione; (3) supporto SAR/PC locale; (4) *eyes-on-cue* su anomalie AIS in acque di avvicinamento. **SAM italiana:** low single-digit €M/anno, capturabile **centinaia di k€/anno** *(confidenza bassa, stima non triangolata)*.
- **Regolatorio (near-shore = fattibile):** operazioni di area portuale/near-coast sono **Specific SAIL II** (mappabili su STS-02 / SORA leggera; auto-autorizzabili con **LUC**) → **il vincolo C3 <25 kg sopravvive**, ma solo near-shore. **Complicazione Genova:** il porto è sotto la **CTR classe D** (con zona di divieto UAS a E/SE dell'aeroporto) → serve comunque coordinamento **ENAC + ENAV**; la Guardia Costiera è **autorità marittima e cliente, non autorità dello spazio aereo**. *(Alta.* Fonti: enac.gov.it; easa.europa.eu STS; aeronauticalinformation.it CTR Genova.*)*
- **Offshore vero = regime distinto, fuori dal C3:** decine di km su rotte navi ⇒ **SAIL III-IV**, containment ad alta integrità, **C2 SATCOM ridondante**, DAA (ED-269/DO-365) → il profilo **<25 kg collassa verso T2/T3 MALE** (benchmark reale: Tekever AR-5 ~180 kg). **Non** è «un volo più lungo» della stessa macchina. *(Media-alta.)*
- **Sostituti da battere:** satellite (**CleanSeaNet** SAR per oil spill), **USV/droni di superficie e subacquei** (già scelti dai porti di Genova e Trieste), sistemi manned Guardia Costiera. L'aereo <25 kg deve dimostrare un vantaggio **costo/persistenza specifico**. *(Media.)*
- **Contesto domanda:** mercato italiano droni marini/subacquei **€93,6M (2024)** → proiezione **€217,6M (2030)** *(analisidifesa.it 2025-10)*; ma è categoria larga, non ricavo di servizio aereo specifico.

**Rischi aperti principali:** crowding-out strutturale «EMSA free-to-state»; trilemma fisico C3 <25 kg; attrito multi-autorità (ENAC+ENAV+Capitaneria); componente dual-use/classificata su confini (rimanda a `riferimenti/RESERVED-rischi-geopolitici.md`); sizing non triangolato; lead «Cegeno/MSC» non confermato.

**Per completare V5** (dopo reset sessione): competitor/sostituti (satellite AIS/SAR, ROV/AUV, prime), reality-check EO su «vedere i cavi dall'alto» (atteso: **non fattibile** sott'acqua; osservabile solo la **superficie** — navi in loitering/ancore/anomalie AIS), fit-piattaforma dettagliato, e **red-team** sul se il marittimo sia dispersione rispetto al focus Aree Interne.
