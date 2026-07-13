# 25d/26b — Percorso di certificazione ENAC/EASA per una piattaforma T-SORV MALE fixed-wing: sorveglianza terrestre (Aree Interne) e marittima (costiera/offshore)

> **Analisi bottom-up — Percorso "servizio-first / piattaforma ad alta endurance"**
> Firmamento Technologies — nuova piattaforma **T-SORV**: UAV ad ala fissa, alto allungamento, endurance 10–20 h, apertura **> 10 m**, MTOM plausibile **100–250 kg**, lancio a **catapulta / traino veicolo** (NON VTOL), recupero da definire (rete/skyhook/pista corta).
> **Due missioni distinte:** (A) **sorveglianza terrestre** delle Aree Interne liguri — antincendio boschivo, viabilità/infrastrutture; (B) **sorveglianza marittima** — traffico commerciale/diportistico, ricerca e soccorso (SAR/uomo in mare), controllo fondali.
> **Autore:** Aviation Regulatory Counsel (EASA / ENAC / U-Space)
> **Data:** 2026-07-13
> **Base:** estende `13-fasce-regolatorio-missione.md` (matrice missione×fascia, riga T3/sorveglianza), `10-fasce-engineering.md` §5.3 (nodo MALE non risolto), `15-C3-vincolo-regolatorio.md` (asse prodotto vs categoria), `16-fasce-MALE-HALE-espanse.md` §2.6–2.7 (economia e nodo regolatorio T3, benchmark EMSA), `04-regolatorio.md` (gradiente iGRC/ARC/SAIL Pentema), `R4-regolatorio-delivery.md` (SORA 2.5 primaria, precedenti ENAC).

---

## 0. Disclaimer epistemico e regola dura del progetto

- **[FATTO]** = testo di regolamento/AMC/GM in vigore, citato con articolo e fonte nel repo.
- **[STIMA]** = valutazione di chi scrive (iGRC/SAIL/costi/tempi/classificazione spazio aereo). Confidenza dichiarata caso per caso, salvo diverso avviso **medium-low**.
- **Regola dura (invariata dall'intero filone bottom-up):** **nessuna classificazione SORA/SAIL è definitiva finché ENAC non la conferma in pre-application** (art. 11 Reg. (UE) 2019/947). Tutti i valori qui sono *preliminary-grade*.
- **Avvertenza forte specifica di questo documento:** la piattaforma T-SORV, per **taglia** (apertura > 10 m, MTOM 100–250 kg) e per **missioni** (antincendio, SAR marittimo), tocca **due porte di uscita dal regime civile EASA ordinario** che il filone precedente aveva solo sfiorato: (i) lo **spartiacque dei 150 kg** verso la Certified Category (`16` §2.7); (ii) l'**esclusione delle attività statali** ex art. 2(3)(a) Reg. (UE) 2018/1139 (antincendio, SAR, guardia costiera). Entrambe **cambiano il percorso** e sono trattate esplicitamente più sotto.

---

## 1. Chiarimento terminologico obbligatorio: "classe C3" è un errore di categoria per questa piattaforma

Il mandato usa impropriamente "classe C3". Va sciolto **prima di tutto**, perché rende la domanda mal posta. Ci sono **due assi ortogonali** (già stabilito in `15` §1):

- **Classe di prodotto C0–C6** = **etichetta del velivolo** apposta dal *fabbricante*, che attesta conformità a requisiti tecnici del **Reg. (UE) 2019/945** (design & manufacture). Per la **classe C3**: MTOM **< 25 kg** e dimensione caratteristica **< 3 m** (Reg. 2019/945, Parte 4). **[FATTO]**
- **Categoria operativa Open / Specific / Certified** = **proprietà dell'operazione** (rischio del volo), decisa dagli artt. 4/5/6 del **Reg. (UE) 2019/947** (operations). **[FATTO]**

**Conseguenza immediata e non negoziabile per T-SORV:**

1. Con **apertura > 10 m** e **MTOM 100–250 kg**, la piattaforma è **fuori da ogni classe C0–C6** (il tetto più alto delle classi di prodotto UAS "Open/Specific" è C6, comunque legato a inviluppi da scenario standard ≤ 3 m / bassa energia): **la marcatura di classe C non è nemmeno rilevante**. Non è "un C3 grande": è un oggetto che **nessuna etichetta di classe di prodotto copre**. **[FATTO — 2019/945 Parte 4; confidenza high]**
2. È **fuori dalla categoria Open** in modo netto: l'art. 4 lett. b Reg. (UE) 2019/947 fissa il tetto Open a **MTOM < 25 kg**. A 100–250 kg si è **sempre e comunque fuori Open**, a qualunque missione. **[FATTO]**
3. Resta quindi solo la scelta **Specific vs Certified** (artt. 5/6 Reg. 947), che è **l'intero oggetto** di questo documento. La classe di prodotto qui non "compra" nulla — a differenza del T1, dove il C3 apre almeno la sotto-categoria Open A3 (`15` §1.1).

> **In una frase:** *per T-SORV non esiste una "classe C3" da rispettare o violare; esiste solo un percorso Specific-vs-Certified da negoziare con ENAC/EASA, e la marcatura di prodotto è un tema del fabbricante, non della sua operazione.*

---
---

# PARTE A — Regolatorio TERRESTRE (sorveglianza Aree Interne liguri)

Missione: **solo EO/IR**, **nessun trasporto/consegna**, **area vasta BVLOS** su territorio SNAI ligure (crinali/boschi, bassa densità abitativa ma sorvolo esteso). Antincendio boschivo + viabilità/infrastrutture.

## A.1 Percorso categoria: lo spartiacque Specific ↔ Certified per MTOM 100–250 kg

**Il perno è duplice — il peso e la dimensione agiscono su leve diverse.**

**(a) Il peso (100–250 kg) — spartiacque dei 150 kg [FATTO/STIMA].**
- L'art. 6 Reg. (UE) 2019/947 elenca i **trigger espliciti** della Certified (assembramenti, trasporto persone, merci pericolose ad alto rischio) **e** il caso in cui **l'autorità competente**, sulla base della valutazione di rischio, **ritenga che il rischio non possa essere mitigato adeguatamente senza certificazione** (art. 6, incl. il rinvio dell'art. 6.2 alla determinazione dell'autorità). **[FATTO]**
- Nella prassi europea la soglia **150 kg** è lo spartiacque storico: sopra i 150 kg di MTOM l'operazione BVLOS continuativa **esce dalla Specific "leggera"** e ricade, con alta probabilità, in **Certified** o in **Specific SAIL IV–VI** con requisiti tecnici/assicurativi quasi assimilabili all'aviazione con equipaggio (`16` §2.7; `10` §5.3). **[STIMA, confidenza medium-high]**
- **Fascia bassa T-SORV (100–150 kg):** *potenzialmente* ancora **Specific**, ma a **SAIL alto (IV–V)** — vedi A.2. **Fascia alta (150–250 kg):** **de facto Certified** o Specific SAIL VI, per determinazione dell'autorità (art. 6.2). **[STIMA, medium]**

**(b) La dimensione (apertura > 10 m) — il vero motore del ground risk [FATTO/STIMA].**
- La SORA 2.5 (Annex a **ED Decision 2025/018/R**, in vigore 15/09/2025) **non legge il peso**: l'iGRC è funzione di **dimensione caratteristica × velocità massima × densità di popolazione** (Table 1). **[FATTO]**
- Con **apertura > 10 m**, la dimensione caratteristica cade nella **banda "20 m"** della Table 1 (la banda che copre 8 m < d ≤ 20 m) — la **penultima riga più severa** della tabella. Questo alza l'iGRC di **2–3 gradini** rispetto a una piattaforma T1/T2 da 3 m, **a parità di densità di popolazione** (coerente con `04` §1.5, "col. 20 m iGRC 5→7+"). **[FATTO strutturale + STIMA sul valore, medium]**

> **Corollario A-1:** lo spartiacque non è un solo numero. Il **peso** decide *se* si scivola in Certified per determinazione dell'autorità (art. 6.2); la **dimensione > 10 m** decide *quanto è alto il SAIL* dentro la Specific. **Per T-SORV le due leve remano nella stessa direzione: verso l'alto.** Nessun precedente italiano di autorizzazione ENAC per un MALE civile in questa fascia in BVLOS su territorio SNAI (`10` §5.3; `16` §2.7 — nessun UAS ha mai ottenuto un TC EASA pieno al luglio 2026; caso più avanzato = primo Design Verification Report per Camcopter S-100, set. 2024). **L'incertezza qui è massima e va dichiarata come tale nello Studio.**

## A.2 SAIL atteso per EO/IR BVLOS area vasta su crinali liguri (quantificazione)

Ipotesi: crinali boscati dell'Appennino ligure interno (es. Val Trebbia/Val d'Aveto/entroterra genovese), **densità locale molto bassa** (< 5 → < 50 ab/km², "Remote"/"Sparsely populated"), spazio **Classe G** in bassa quota, **quota di crociera stimata dal collega ~2–5 km AMSL** (vedi A.4). Il ground risk è **effettivamente più basso** che sul borgo di Pentema, **ma non basso in assoluto**, perché la dimensione del velivolo lo tiene su.

**Catena iGRC → GRC → SAIL [STIMA, confidenza medium]:**
- **iGRC di partenza ≈ 5–6.** Banda dimensione "20 m" (apertura > 10 m) × banda densità sparsa (< 5–50 ab/km²) → **iGRC ~5** su terreno realmente remoto, **~6** se il *ground risk buffer* (ampio per un fixed-wing veloce a 100–150 km/h) intercetta strade con traffico (SP/SS, viabilità = **presenza umana in movimento**) o nuclei sparsi. È **1–2 gradini sopra** l'iGRC di Pentema-VTOL (che in `04` §2.2 scende a 3–4 grazie ai 3 m).
- **Mitigazioni:** **M1(A/B/C)** (sheltering strutturale limitato su bosco; restrizioni operative; riduzione del buffer via geofencing e bassa velocità nelle fasi critiche) può abbattere di **−1/−2**. **M2** (containment/BRS + terminazione di volo) è **più difficile da argomentare** su un airframe da 100–250 kg che su un piccolo VTOL (energia d'impatto molto maggiore, paracadute pesante e non sempre efficace). **[STIMA, medium]**
- **GRC finale ≈ 4–5.**
- **ARC ≈ b** in Classe G a bassa quota su crinale remoto (traffico GA sporadico), **ma rischio ARC-c** se la crociera 2–5 km AMSL intercetta aerovie o la TMA di Genova / zone R militari (A.4). **[STIMA, medium-low — dipende dalla struttura reale dello spazio aereo locale, OQ da chiudere]**
- **SAIL risultante:** con **GRC 4–5 × ARC-b → SAIL IV** (range **III se tutto va bene, V se il buffer è largo o l'ARC sale a c**). Table 3 SORA 2.5. **[STIMA, confidenza medium]**

> **Corollario A-2 (quantificato):** la remoteness dei crinali liguri **fa risparmiare ~1–2 gradini** rispetto al sorvolo di un borgo, ma **la dimensione > 10 m riporta il SAIL su a IV** (vs SAIL II del piccolo VTOL a Pentema). **T-SORV terrestre è realisticamente SAIL III–V, con IV come stima centrale** — cioè **la soglia oltre la quale il costo/tempo esplode e la Certified diventa lo scenario probabile** (art. 6.2). Non è un servizio "leggero": è un programma regolatorio pesante.

## A.3 Overlay privacy: sorveglianza sistematica ad area vasta > EO ambientale puro

- L'EO ambientale puro (incendi, vegetazione, frane) **non attiva trigger di missione** (`13` §1.4). Ma la missione qui **include la viabilità/infrastrutture**, cioè **strade con traffico** — presenza umana, veicoli, **targhe potenzialmente riprendibili**. Questo attiva il **binario privacy parallelo**: **GDPR Reg. (UE) 2016/679 + D.Lgs. 196/2003 novellato + art. 34 Reg. ENAC APR Ed.3** (privacy a bordo). **[FATTO]**
- **DPIA obbligatoria** (art. 35 GDPR — trattamento su larga scala, monitoraggio sistematico di area accessibile al pubblico). Base giuridica dedicata; se finalità di sicurezza pubblica/protezione civile, valutazione dell'**interesse pubblico** (art. 6 GDPR); ruolo del **Garante** in caso di consultazione preventiva (art. 36). Competenza operativa: `data-privacy-counsel`. **[FATTO/STIMA]**
- **L'overlay è più stringente che a Pentema** proprio perché **endurance (10–20 h) e area vasta** significano **sorveglianza persistente e ripetuta** su porzioni estese di territorio — il profilo che il Garante tratta con maggiore severità (proporzionalità, minimizzazione, data retention). **[STIMA, medium-high]**

> **Corollario A-3:** il rischio-blocco privacy per T-SORV terrestre **non è tecnico ma istituzionale**, e cresce con l'endurance. Va gestito come **binario autorizzativo autonomo** (DPIA + eventuale accordo di trattamento con PA/Protezione Civile), non come corollario della SORA. Mitigazione tecnica: **blurring/edge-processing** a bordo, GSD deliberatamente non-identificante dove la finalità è ambientale.

## A.4 Sito di lancio a catapulta/traino e integrazione nello spazio aereo

- **Lancio a catapulta / traino veicolo (non VTOL):** richiede un **sito di lancio/recupero** con area libera e superficie di guardia (safety area) — implicazione operativa e demaniale/comunale (uso del suolo), **non aeronautica in sé**, ma rilevante per il ground risk in fase di decollo/recupero (il buffer si concentra lì). **[STIMA]**
- **NOTAM e coordinamento ENAV [FATTO/STIMA]:** ogni operazione BVLOS in Specific richiede **coordinamento con ENAV** e, tipicamente, **emissione di NOTAM** per il volume operativo, in particolare se il sito o la rotta sono vicini a spazio controllato o a strutture ATS. **[FATTO come prassi ENAC/ENAV; art. 26 Reg. ENAC APR Ed.3 per BVLOS]**
- **Il nodo quota:** se la **crociera 2–5 km AMSL** (~6.500–16.000 ft) determinata dal collega **intercetta aerovie, la TMA di Genova (LIMJ) o zone regolamentate/riservate militari** dell'entroterra ligure, l'**ARC sale a c/d** e con esso il SAIL, **indipendentemente dal ground risk** (`04` §1.5 — "la quota è un cancello di costo indipendente dal peso"). Sotto FL195 lo spazio **può essere controllato o non controllato a seconda della struttura locale**: **non è automatico che sia Classe G**. **[FATTO strutturale; STIMA sulla geometria locale — OQ prioritaria da chiudere con ENAV in pre-app]**
- **DAA (Detect-And-Avoid):** per BVLOS ad area vasta con questa quota serve una strategia DAA robusta (cooperativa ADS-B + non-cooperativa) per tenere l'ARC gestibile — competenza `avionics-gnc-engineer`; standard di riferimento **DO-365B/ED-269**. **[STIMA]**

> **Corollario A-4:** il **cancello quota** è potenzialmente più pericoloso del ground risk. Una crociera a 3–5 km AMSL vicino alla TMA di Genova può **da sola** spingere l'ARC a c e il SAIL a V, vanificando il risparmio ottenuto sulla remoteness del terreno. **La geometria dello spazio aereo ligure locale è la prima cosa da mappare con ENAV.**

## A.5 Timeline e costo stimato del percorso di certificazione

Coerente con i bracket di `10` §5.3, `04` §2 (riga MALE) e `16` §2.6–2.7. Costi = **compliance** (SORA, safety case, OSO robusti, consulenza, DAA, assicurazione, eventuale DVR); **piattaforma esclusa**.

| Scenario | Categoria | Iter | Tempo | Costo compliance |
|---|---|---|---|---|
| **Fascia bassa (100–150 kg), SAIL IV Specific** | Specific SAIL IV | SORA 2.5 piena + OSO ad alta robustezza + DAA + coordinamento ENAV; possibile via **Design Verification Report (DVR)** invece del TC pieno (`16` §2.7 — DVR ~€45k/anno, €250/h EASA) | **2–4 anni** | **€1–5M+** |
| **Fascia alta (150–250 kg), de facto Certified** | Certified (art. 6.2) | Certification Basis custom + Special Condition + Certification Plan EASA + eventuale TC (mai ottenuto da alcun UAS al 2026) | **3–7+ anni** | **€5–15M+** (territorio HALE per intensità di capitale) |

- Il **DVR** (Design Verification Report EASA) è la **via di mitigazione realistica** che evita il TC pieno "che non esiste per nessuno": consente di operare in Specific SAIL alto dando all'autorità un'evidenza di progetto verificata da EASA, senza il peso completo della Certified. **[FATTO — R3/`16` §2.7; confidenza high sul meccanismo, medium sull'applicabilità a T-SORV]**
- **Regime "agenzia":** se la missione antincendio è svolta **da/per un ente pubblico** (Protezione Civile, Corpo dei Vigili del Fuoco, Regione), si apre la porta A.6 (esclusione statale), che **cambia il regime** e i tempi.

> **Corollario A-5:** **T-SORV terrestre non è finanziabile né autorizzabile nell'orizzonte Y1–Y3 come procurement autonomo Firmamento** (tetto "comodo" ~€1M, `06`; CapEx 6A realistico €2,5–3,5M, `05`). È coerente con il verdetto invariato del filone: **fascia MALE = servizio-in-consorzio con anchor pubblico Y3+, non asset da comprare e sperare** (`16` §2.6).

## A.6 Precedenti/comparabili e la porta dell'esclusione statale (antincendio)

- **Precedenti civili italiani per MALE in sorveglianza territoriale BVLOS su SNAI: nessuno identificato.** Il precedente ENAC più citato (**ABzero**, Patti–Eolie, lug 2024) è **delivery medicale**, non sorveglianza, e su piattaforma piccola (`R4` §1) — **non è un comparabile** per taglia né missione. Utile solo come prova che l'iter Specific rotta-per-rotta esiste. **[FATTO]**
- **Comparabile europeo di missione (non di taglia civile italiana):** il **servizio EMSA-Tekever** (AR3/AR5, sorveglianza marittima e territoriale per agenzie UE) mostra che il **modello RPAS-as-a-Service in fascia MALE opera in "spazio agenzia"**, con equipaggio del contractor incluso, non come operatore civile puro Reg. 947 (`16` §2.6). **[FATTO]**
- **⚠️ Porta dell'esclusione statale — art. 2(3)(a) Reg. (UE) 2018/1139 [FATTO, rilevanza high]:** il Reg. Basic esclude dal proprio ambito (e quindi dal regime EASA civile 947/945) gli aeromobili che svolgono attività **militari, doganali, di polizia, di ricerca e soccorso, antincendio, controllo delle frontiere, guardia costiera o affini**, effettuate **da o per conto di un ente investito di pubblici poteri**. **L'antincendio boschivo è espressamente in elenco.** Se T-SORV opera **per conto della Protezione Civile/Regione in funzione antincendio**, l'attività **può ricadere fuori dal regime civile Reg. 947** e nel regime degli **aeromobili di Stato** (Codice della Navigazione, R.D. 327/1942, art. 744 ss.), con **autorizzazione secondo un binario nazionale/statale diverso** — potenzialmente **più rapido** ma **meno standardizzato** e dipendente dalla committenza pubblica. **[FATTO sulla norma; STIMA sull'applicabilità e sull'esito, medium — da confermare con ENAC/committente in pre-app]**

> **Corollario A-6:** la missione antincendio **non è "una missione EO come le altre"**: apre una **via alternativa** (regime aeromobili di Stato) che può **scavalcare** in parte l'iter Specific/Certified civile — ma **solo** se esiste un **committente pubblico** che assume l'operazione come propria attività statale. Questo rafforza la tesi "**serve l'anchor pubblico prima dell'asset**" e la trasforma da vincolo economico a **vincolo anche regolatorio**.

## A.7 Almeno 5 falsifying observations — Parte A

1. **FO-A1 (falsifica A.1/A.2):** se ENAC in pre-application classificasse la banda densità del *footprint* reale come "< 500" (tesi conservativa tipo `A11`/`04` §5) invece di "< 5–50", **e** confermasse la banda dimensione "20 m", l'iGRC salirebbe a **6–7** → **GRC 5–6 → SAIL V–VI → Certified quasi certa**. Il singolo driver di costo più pesante. → **OQ: banda densità del footprint + banda dimensione effettiva.**
2. **FO-A2 (falsifica A.4):** se la crociera 2–5 km AMSL **intercetta stabilmente** la TMA di Genova o aerovie/zone R, l'**ARC-b cade** e il SAIL sale a V–VI **a prescindere dal ground risk** — l'intero risparmio della remoteness svanisce. → **OQ ENAV: struttura verticale dello spazio aereo sull'entroterra ligure alla quota di crociera.**
3. **FO-A3 (falsifica A.6):** se il committente pubblico **NON** assume l'antincendio come propria attività statale (art. 2(3)(a)), la porta "aeromobili di Stato" **si chiude** e resta solo l'iter civile Specific/Certified pieno, con i tempi/costi peggiori. → **OQ: chi è il soggetto vestito di pubblici poteri che assume l'operazione?**
4. **FO-A4 (falsifica A.5):** se EASA/ENAC **non accetta il DVR** come via alternativa al TC per questa taglia/ConOps, l'unica strada resta il **Type Certificate pieno — mai ottenuto da alcun UAS** — con tempi 5–7+ anni: T-SORV terrestre diventa **non fattibile nell'orizzonte del progetto**. → **OQ: EASA conferma applicabilità del percorso DVR a un MALE 100–250 kg civile?**
5. **FO-A5 (falsifica A.3):** se il Garante ritiene **sproporzionata** la sorveglianza persistente di viabilità (retention, larga scala, ripresa di targhe/persone), può **imporre limiti operativi** (aree escluse, GSD massimo, no ripresa strade) che **svuotano la missione "viabilità/infrastrutture"** — restando fattibile solo l'antincendio ambientale puro. → **OQ: perimetro accettabile dal Garante per la componente "viabilità".**
6. **FO-A6 (falsifica A.1):** se emergesse un **precedente ENAC** (o EASA in altro Stato membro) di autorizzazione Specific per MALE civile > 150 kg in sorveglianza territoriale, la tesi "nessun precedente, incertezza massima" si indebolirebbe e il rischio-showstopper si ridurrebbe. **Finora non identificato** (`10` §5.3). → **OQ: due-diligence su autorizzazioni Specific SAIL IV–VI concesse in UE.**

## A.8 Riga di fondo — Parte A

**T-SORV terrestre è un programma regolatorio pesante, non un servizio leggero.** Fuori C-marking e fuori Open per definizione (apertura > 10 m, MTOM 100–250 kg): il gioco è **Specific SAIL alto vs Certified**. La **remoteness dei crinali liguri fa risparmiare 1–2 gradini di ground risk**, ma la **dimensione > 10 m riporta il SAIL a IV** (range III–V), e il **peso oltre 150 kg** apre lo scivolo verso la **Certified per determinazione dell'autorità (art. 6.2)**. Sopra si innestano **due binari paralleli**: la **privacy** (DPIA/Garante, più stringente per endurance/area vasta, con la componente "viabilità" come punto di frizione) e il **cancello quota** (ARC-c se la crociera intercetta la TMA di Genova/aerovie). Tempi **2–4 anni / €1–5M+** in Specific con DVR; **3–7+ anni / €5–15M+** se Certified. **Nessun precedente civile italiano**: incertezza massima, da dichiarare. **La leva che può accorciare tutto è l'esclusione statale ex art. 2(3)(a) Reg. 2018/1139** per l'antincendio — ma **solo con un committente pubblico** che assuma l'operazione: **serve l'anchor pubblico prima dell'asset, anche per ragioni regolatorie**. Nulla è definitivo prima della pre-application ENAC (art. 11).

---
---

# PARTE B — Regolatorio MARITTIMO (sorveglianza costiera/offshore)

Missione: sorveglianza marittima con **AIS/radar/EO-IR** (eventuale bathymetria) — traffico commerciale/diportistico, **SAR/uomo in mare (MOB)**, controllo fondali. Stessa piattaforma T-SORV.

## B.1 Framework overwater: SORA sul mare e i nuovi attori autorizzativi

**Il ground risk cambia natura sull'acqua [FATTO/STIMA].**
- La SORA 2.5 resta la metodologia (Table 1 iGRC), ma su **acque aperte** la **densità di popolazione a terra tende a zero**: l'iGRC scende di **2–3 bande di densità** rispetto a terra, **anche per un velivolo da 20 m**. Su mare aperto, lontano da rotte diportistiche, l'iGRC per T-SORV può scendere a **~3–4** (vs 5–6 a terra). **[STIMA, medium]**
- **Ma il ground risk NON è nullo:** (i) **vicino a costa/porti/spiagge** (la costa ligure è **densamente popolata**, spiagge affollate in stagione) la densità di "persone a rischio" **risale bruscamente**; (ii) il **traffico diportistico e commerciale** costituisce "terze parti mobili" sull'acqua (persone su imbarcazioni); (iii) la fase di **lancio/recupero**, se da terra sulla fascia costiera, concentra il buffer sull'area più popolata. **[STIMA, medium-high]**
- **ARC marittimo:** su mare aperto a bassa quota il traffico aereo è **diverso** — meno GA, ma **rotte commerciali costiere**, elicotteri SAR/offshore, e la **TMA di Genova** (LIMJ, aeroporto costiero). L'ARC può essere **b offshore** ma **c/d in avvicinamento a costa/aeroporto**. **[STIMA, medium-low]**

**Chi altro autorizza — oltre ENAC/ENAV [FATTO, rilevanza high]:**
- **ENAC** (aeronavigabilità/categoria) + **ENAV** (integrazione spazio aereo/FIR) restano competenti.
- **NUOVO rispetto al caso terrestre: la Guardia Costiera / Capitaneria di Porto** (Corpo delle Capitanerie di Porto — Guardia Costiera, dipendente dal Ministero delle Infrastrutture e dei Trasporti; **Comando Generale** e **IMRCC Roma** per il SAR marittimo) ha **giurisdizione sul SAR marittimo, sull'ordinamento della navigazione e sul demanio marittimo** (Codice della Navigazione R.D. 327/1942; D.P.R. 662/1994 sul SAR marittimo, che recepisce la Convenzione SAR di Amburgo 1979). Per operazioni sul mare — specie SAR e uso di siti costieri demaniali — **la Capitaneria è un interlocutore/autorizzatore aggiuntivo**, non solo ENAC. **[FATTO sulla giurisdizione; STIMA sul ruolo autorizzativo puntuale, medium]**

> **Corollario B-1:** sul mare **il ground risk migliora ma la catena di autorizzatori si allunga**: al binario ENAC/ENAV si aggiunge **la Guardia Costiera/Capitaneria** (SAR + demanio) e, per i fondali, l'**Istituto Idrografico della Marina** (B.4). Il rischio si sposta **dal ground risk alla governance multi-autorità**.

## B.2 SAR / uomo in mare (MOB): esiste un framework dedicato?

- **Framework SAR-UAS civile dedicato in Italia/EASA: non esiste un regime ad hoc standardizzato.** Il SAR marittimo è disciplinato dalla **Convenzione SAR di Amburgo 1979** (recepita con **D.P.R. 662/1994**) e coordinato dall'**IMRCC** della Guardia Costiera; **non c'è un "SORA per il SAR-UAS"** né una PDRA dedicata al soccorso in mare. **[FATTO sulla cornice SAR; STIMA sull'assenza di framework UAS dedicato, medium-high]**
- **La porta dell'esclusione statale è qui ancora più forte che a terra [FATTO]:** l'art. 2(3)(a) Reg. (UE) 2018/1139 esclude espressamente **ricerca e soccorso** e **guardia costiera**. Un T-SORV che svolga **SAR/MOB per conto della Guardia Costiera** ricade con alta probabilità **fuori dal regime civile Reg. 947** e nel **regime di aeromobili di Stato / attività statale**, con autorizzazione secondo il binario della committenza pubblica. **[FATTO sulla norma; STIMA sull'applicabilità, medium-high]**
- **Comparabili europei [FATTO/benchmark]:** diverse guardie costiere UE **già impiegano UAS a lungo raggio per sorveglianza e SAR**, tipicamente **via il framework EMSA** (RPAS-as-a-Service): **Tekever AR5**, **Airbus Flexrotor**, **Schiebel Camcopter S-100** operati per EMSA e messi a disposizione delle autorità nazionali (incluse operazioni nel Mediterraneo). È il **precedente operativo più solido** per il caso B — e conferma che **il MALE marittimo europeo vive nello "spazio agenzia", non nell'operatore civile puro** (`16` §2.6). **[FATTO, confidenza medium-high]**

> **Corollario B-2:** per il SAR, **il percorso realistico non è "certifica un UAS civile e vendi il servizio", ma "opera per/con la Guardia Costiera come attività statale"** (à la EMSA). Questo **semplifica il nodo di categoria** (esce dal Reg. 947 civile) ma **subordina tutto all'esistenza di un committente-agenzia**. Senza Guardia Costiera come controparte, il SAR-UAS ricade nell'iter civile pesante della Parte A.

## B.3 Traffico commerciale/diportistico: regime privacy più leggero

- **La sorveglianza AIS/radar del traffico navale NON pone problemi di privacy paragonabili al caso terrestre.** Il **tracciamento delle navi via AIS è per definizione un dato già pubblico** (l'AIS trasmette in chiaro identificativo, posizione, rotta; ricevibile da chiunque, aggregato da servizi pubblici tipo MarineTraffic). Il MMSI/nome nave è **dato dell'imbarcazione**, non dato personale nel senso pieno del GDPR (salvo piccola nautica dove il natante è riconducibile a persona fisica identificabile). **[FATTO sul carattere pubblico dell'AIS; STIMA sulla qualificazione GDPR, medium]**
- **Il regime privacy è quindi più leggero** per la componente AIS/radar. **Ma non è azzerato:** l'**EO/IR ad alta risoluzione su imbarcazioni da diporto o su bagnanti sotto costa può riprendere persone identificabili** → in quel caso il GDPR (art. 35 DPIA) **si riattiva**, specie sotto costa. La distinzione operativa è netta: **tracce AIS/radar = regime leggero; imagery EO/IR ravvicinata di persone = regime pieno**. **[STIMA, medium-high]**

> **Corollario B-3:** la **privacy è un problema minore in mare aperto** (dominata da dati AIS pubblici) e **torna problema solo sotto costa/su imbarcazioni** con EO/IR identificante. È l'**inverso del caso terrestre**, dove la componente "viabilità/persone" è pervasiva. Mitigazione: minimizzazione EO ravvicinata, focalizzazione su tracce/anomalie di traffico.

## B.4 Controllo fondali / bathymetria: autorizzazioni specifiche e aree protette

- **Bathymetria e cartografia nautica — Istituto Idrografico della Marina (IIM) [FATTO/STIMA]:** in Italia la **produzione di cartografia nautica ufficiale è competenza esclusiva dell'IIM** (Marina Militare, Genova). Un rilievo batimetrico sistematico **non produce automaticamente carte ufficiali** e, se destinato alla navigazione, **deve raccordarsi con l'IIM**; il rilievo idro-oceanografico in acque nazionali può inoltre richiedere **autorizzazioni** (specie in aree militari o per soggetti terzi/stranieri). **[STIMA sul perimetro autorizzativo, medium — da verificare]**
- **Il payload batimetrico da HALE/MALE è tecnicamente delicato:** la batimetria ottica (LiDAR batimetrico) da quota è limitata a **acque basse e limpide**; sul sensing **non aggiunge trigger aeronautici** (è massa+ottica, come l'EO — `13` §1.3), ma **aggiunge il binario autorizzativo idrografico**. **[STIMA]**
- **Aree marine protette e Santuario Pelagos [FATTO, rilevante per la Liguria]:** la costa ligure ricade nel **Santuario Pelagos** per i mammiferi marini (Accordo Italia-Francia-Monaco 1999, ratificato con **L. 391/2001**) e comprende **Aree Marine Protette** (es. Portofino, Cinque Terre — L. 979/1982 e L. 394/1991). Il **sorvolo a bassa quota** di UAV su queste aree può porre temi di **disturbo alla fauna** (cetacei) e richiedere **coordinamento/nulla-osta con l'ente gestore dell'AMP** e attenzione ai vincoli del Santuario. **[FATTO sull'esistenza dei regimi; STIMA sull'onere autorizzativo concreto per UAV, medium-low — da verificare con enti gestori]**

> **Corollario B-4:** la batimetria/controllo fondali **non alza il SAIL** ma **apre due binari amministrativi nuovi e specifici**: (i) **idrografico** (IIM, cartografia/rilievo); (ii) **ambientale-marino** (AMP/Pelagos). Sono oneri **diversi** da quelli aeronautici e vanno mappati separatamente. Per la Liguria, **Pelagos è un vincolo reale da non sottovalutare**.

## B.5 Spazio aereo sul mare: classificazione, rotte, aeroporti costieri

- **Lo spazio aereo sul mare resta spazio aereo italiano/gestito [FATTO/STIMA]:** entro le **12 miglia** (mare territoriale) si è in spazio nazionale; oltre, fino al limite della **FIR** (Flight Information Region — es. FIR Milano/Roma), lo spazio è **internazionale ma soggetto a responsabilità ATS** dello Stato competente (ICAO Annex 2 / Reg. (UE) 923/2012 SERA su alto mare). **Il BVLOS su alto mare non è "terra di nessuno"**: resta soggetto a coordinamento ENAV/FIR. **[FATTO]**
- **Classificazione differenziata rispetto a terra:** offshore a bassa quota lo spazio è spesso **Classe G / non controllato** con traffico rarefatto (ARC potenzialmente **b**), **ma:** (i) **la TMA di Genova (LIMJ)** è un aeroporto **costiero** — l'avvicinamento a costa alza rapidamente la classe/ARC; (ii) esistono **rotte commerciali costiere** e traffico elicotteristico (SAR, offshore, elisoccorso); (iii) possibili **zone R/D militari** in mare. **[STIMA, medium]**
- **Componente internazionale:** operazioni che si avvicinano ad **acque francesi/monegasche** (costa ligure di ponente, prossimità Costa Azzurra/Principato) intersecano **FIR e giurisdizioni confinanti** → possibile necessità di **coordinamento transfrontaliero**. **[STIMA, medium-low — rilevante solo per operazioni a ponente vicino confine]**

> **Corollario B-5:** in mare **il vantaggio (ground risk basso offshore, ARC-b) si concentra al largo**, mentre **tutti i colli di bottiglia si addensano sotto costa** (densità umana, TMA Genova, AMP/Pelagos, demanio, avvicinamento). Il ConOps marittimo ottimale **massimizza il tempo al largo e minimizza le fasi costiere** — ma lancio/recupero e la missione SAR/diporto **sono intrinsecamente costieri**, quindi il vantaggio è parziale.

## B.6 Almeno 5 falsifying observations — Parte B

1. **FO-B1 (falsifica B.1/B.2):** se la Guardia Costiera **NON** assume l'operazione come propria attività statale (art. 2(3)(a)), il SAR-UAS **ricade nell'iter civile Reg. 947 pieno** — con lo stesso peso della Parte A (SAIL alto/Certified) **più** la complicazione overwater del lancio/recupero costiero. La "scorciatoia agenzia" **si chiude**. → **OQ: la Guardia Costiera è disposta a fungere da soggetto committente/autorità dell'operazione?**
2. **FO-B2 (falsifica B.1):** se ENAC valuta che il **ground risk vicino a costa/porti liguri** (densità elevata, spiagge affollate, traffico diportistico intenso) **domina** il profilo di missione, l'iGRC risale a livelli terrestri e il **vantaggio "mare = ground risk basso" evapora** per la parte utile della missione (che è costiera). → **OQ: quota/distanza da costa minima accettabile e relativo iGRC.**
3. **FO-B3 (falsifica B.5):** se la **TMA di Genova** e le rotte costiere rendono l'**ARC-c** su gran parte dell'area operativa utile, il SAIL sale come a terra e il vantaggio marittimo sull'air risk **non si materializza**. → **OQ ENAV: struttura dello spazio aereo sul Golfo Ligure alla quota operativa.**
4. **FO-B4 (falsifica B.4):** se il **Santuario Pelagos / le AMP liguri** impongono limiti di quota o divieti di sorvolo a tutela dei cetacei, la **missione batimetrica/controllo fondali sotto costa può essere ristretta o vietata** in porzioni rilevanti della costa ligure. → **OQ: vincoli di sorvolo UAV su Pelagos e AMP con gli enti gestori.**
5. **FO-B5 (falsifica B.3):** se il Garante qualifica come **dato personale** anche il tracciamento sistematico della **piccola nautica** (natante riconducibile a persona fisica) o la **profilazione dei comportamenti di navigazione**, il "regime privacy leggero" del mare **si irrigidisce** almeno per il diporto. → **OQ: perimetro GDPR del tracciamento diportistico.**
6. **FO-B6 (falsifica B.4):** se il rilievo batimetrico richiede **autorizzazione idro-oceanografica IIM/Marina Militare** più onerosa del previsto (specie in prossimità di aree militari o per finalità cartografiche), il caso d'uso "controllo fondali" **acquisisce un lead-time autorizzativo indipendente** dall'iter aeronautico. → **OQ: regime autorizzativo IIM per rilievi batimetrici da UAV di soggetto civile.**

## B.7 Riga di fondo — Parte B

**In mare il baricentro del rischio si sposta dal "quanto è alto il SAIL" al "quante autorità devono dire sì".** Sull'acqua il **ground risk crolla al largo** (iGRC ~3–4 anche per un velivolo da 20 m) e l'ARC può essere **b offshore**, abbassando in linea di principio il SAIL rispetto a terra — **ma tutti i colli di bottiglia si addensano sotto costa** (densità umana, TMA di Genova, AMP/**Santuario Pelagos**, demanio marittimo, lancio/recupero), dove la missione utile (SAR, diporto, fondali) in realtà vive. La **catena di autorizzatori si allunga**: a ENAC/ENAV si aggiungono la **Guardia Costiera/Capitaneria** (SAR + demanio, Codice Navigazione + D.P.R. 662/1994) e l'**Istituto Idrografico della Marina** (batimetria). La **privacy è più leggera** (AIS pubblico) e torna problema **solo con EO/IR identificante sotto costa** — l'inverso del caso terrestre. La leva decisiva è la stessa: l'**esclusione statale ex art. 2(3)(a) Reg. 2018/1139** — qui **più forte** perché SAR e guardia costiera sono espressamente elencati — che sposta il SAR-UAS **fuori dal Reg. 947 civile** e nel regime di attività statale, **à la EMSA-Tekever/Flexrotor/Schiebel**. **Senza un committente Guardia Costiera, il SAR marittimo ricade nell'iter civile pesante della Parte A.** Nulla è definitivo prima della pre-application ENAC (art. 11) e del coordinamento con la Capitaneria.

---
---

## Sintesi comparativa Terra vs Mare (colpo d'occhio)

| Dimensione | Parte A — Terra (Aree Interne) | Parte B — Mare (costiera/offshore) |
|---|---|---|
| **Categoria** | Specific SAIL alto ↔ Certified (spartiacque 150 kg) | Idem come cornice civile; **ma** SAR/guardia costiera → possibile **fuori Reg. 947** (art. 2(3)(a)) |
| **Ground risk (iGRC)** | Alto per dimensione > 10 m: **~5–6** anche in area remota | **Basso al largo (~3–4)**, alto sotto costa/porti |
| **SAIL centrale [STIMA]** | **IV** (range III–V) | **II–III offshore**, sale a IV sotto costa |
| **Air risk (ARC)** | b su crinale, **c** se crociera intercetta TMA Genova/aerovie | b offshore, **c** in avvicinamento costa/TMA Genova |
| **Autorità** | ENAC + ENAV (+ Protezione Civile per antincendio statale) | ENAC + ENAV **+ Guardia Costiera/Capitaneria + IIM** (batimetria) |
| **Privacy** | **Pesante** (viabilità = persone/targhe; endurance → sorveglianza persistente) | **Leggera** (AIS pubblico); pesante solo con EO/IR sotto costa |
| **Vincoli ambientali** | Aree protette terrestri (parchi) — non dominante | **Santuario Pelagos + AMP liguri** — potenzialmente vincolante |
| **Esclusione statale art. 2(3)(a)** | Sì, via **antincendio** (se committente pubblico) | Sì, via **SAR/guardia costiera** — **più forte** |
| **Precedenti** | Nessuno civile IT per MALE su SNAI | **EMSA (Tekever/Flexrotor/Schiebel)** — modello agenzia |
| **Tempi/costi compliance** | 2–4 anni / €1–5M+ (Specific+DVR); 3–7+ anni / €5–15M+ (Certified) | Simili, **ma** la via "agenzia" può accorciare se c'è la Guardia Costiera |

**Differenza chiave in una frase:** *a terra il problema è il SAIL alto imposto dalla taglia del velivolo su territorio abitato (con la privacy come binario di rischio istituzionale); in mare il problema è la governance multi-autorità sotto costa (con il ground risk basso al largo come unico vero sconto). In entrambi i casi la leva risolutiva non è tecnica ma istituzionale: l'esclusione statale ex art. 2(3)(a) Reg. 2018/1139, cioè un committente pubblico (Protezione Civile a terra, Guardia Costiera in mare) che assuma l'operazione come attività statale.*

---

## Tabella fonti e confidenza complessiva

| # | Elemento | Confidenza | Fonte |
|---|---|---|---|
| 1 | Classe C0–C6 (prodotto) ≠ categoria Open/Specific/Certified (operazione); T-SORV fuori C-marking e fuori Open | **high** [FATTO] | Reg. (UE) 2019/945 Parte 4 (C3: <25 kg/<3 m); Reg. (UE) 2019/947 art. 4 lett. b; `15` §1 |
| 2 | Trigger Certified (assembramenti/persone/DG alto rischio) + determinazione autorità | **high** [FATTO] | Reg. (UE) 2019/947 art. 6 / 6.2; `04` §1.1 |
| 3 | Spartiacque 150 kg → Certified/Specific SAIL IV–VI; nessun TC EASA UAS al 2026; DVR Camcopter S-100 set. 2024 | **medium-high** [STIMA/FATTO] | `16` §2.7; `10` §5.3; R3 §4 |
| 4 | SORA 2.5 = Annex ED Decision 2025/018/R (in vigore 15/09/2025); iGRC = dim × vel × densità (Table 1), SAIL (Table 3) | **high** [FATTO] | `fonti/annex_to_ed_decision_2025-018-r_1.md`; `R4` §1 |
| 5 | Apertura > 10 m → banda dimensione "20 m" → iGRC +2/3 gradini; iGRC terra ~5–6, SAIL IV (III–V) | **medium** [STIMA] | Table 1 SORA 2.5; `04` §1.5; stima di chi scrive |
| 6 | iGRC mare ~3–4 al largo, risale sotto costa; ARC b offshore / c su costa-TMA | **medium** [STIMA] | Table 1 SORA 2.5; stima di chi scrive |
| 7 | Overlay privacy terra (viabilità/persone): GDPR + D.Lgs. 196/2003 + art. 34 ENAC; DPIA art. 35 | **high** [FATTO] | Reg. (UE) 2016/679; Reg. ENAC APR Ed.3 art. 34; `13` §1.2 |
| 8 | Privacy mare più leggera (AIS pubblico); pesante solo con EO/IR identificante sotto costa | **medium** [STIMA] | Carattere pubblico AIS; qualificazione GDPR di chi scrive |
| 9 | Cancello quota / ARC-c da TMA Genova; BVLOS su mare resta sotto FIR/ENAV (SERA Reg. 923/2012) | **medium** [STIMA/FATTO] | `04` §1.5; Reg. (UE) 923/2012; art. 26 ENAC APR (BVLOS) |
| 10 | Esclusione attività statali (antincendio, SAR, guardia costiera) dal regime EASA civile | **high** [FATTO] sulla norma / **medium** [STIMA] sull'applicabilità | Reg. (UE) 2018/1139 art. 2(3)(a); Codice Navigazione R.D. 327/1942 |
| 11 | Guardia Costiera/Capitaneria autorità SAR + demanio; SAR marittimo D.P.R. 662/1994 (Conv. Amburgo 1979) | **high** [FATTO] sulla giurisdizione / **medium** [STIMA] sul ruolo autorizzativo puntuale | Codice Navigazione; D.P.R. 662/1994 |
| 12 | Comparabili marittimi europei via EMSA (Tekever AR5, Airbus Flexrotor, Schiebel S-100) = modello "agenzia" | **medium-high** [FATTO/benchmark] | `16` §2.6; R3 §2 |
| 13 | Batimetria → IIM (cartografia nautica); Santuario Pelagos (L. 391/2001) + AMP liguri (L. 979/1982, L. 394/1991) | **medium** [FATTO su esistenza regimi / STIMA su onere UAV] | L. 391/2001; L. 979/1982; L. 394/1991 |
| 14 | Nessun precedente civile italiano di autorizzazione ENAC per MALE su SNAI in BVLOS | **high** [FATTO — assenza riscontrata] | `10` §5.3; `16` §2.7 |
| 15 | Via DVR (~€45k/anno, €250/h EASA) come alternativa al TC pieno | **high** [FATTO sul meccanismo] / **medium** [STIMA sull'applicabilità a T-SORV] | R3 §4; `16` §2.7 |
| 16 | Regola dura: nessuna classificazione SORA definitiva prima della pre-application ENAC | **high** [FATTO] | art. 11 Reg. (UE) 2019/947 |

### Fonti (repo e norme)
- **Norme UE:** Reg. (UE) 2018/1139 (Basic, **art. 2(3)(a)** esclusione attività statali); Reg. (UE) 2019/947 (**art. 4** Open, **art. 5** Specific, **art. 6/6.2** Certified, **art. 11** pre-app); Reg. (UE) 2019/945 (Parte 4 classi C); Reg. (UE) 2016/679 (GDPR); Reg. (UE) 923/2012 (SERA); SORA 2.5 = Annex a ED Decision 2025/018/R.
- **Norme nazionali:** D.Lgs. 196/2003 novellato; Reg. ENAC APR Ed.3+Em. (art. 26 BVLOS, art. 34 privacy, §4.5 DG); Codice della Navigazione R.D. 327/1942; D.P.R. 662/1994 (SAR marittimo, Conv. Amburgo 1979); L. 391/2001 (Santuario Pelagos); L. 979/1982 e L. 394/1991 (aree protette/AMP).
- **Base repo:** `analisi-bottom-up/04-regolatorio.md`, `13-fasce-regolatorio-missione.md`, `15-C3-vincolo-regolatorio.md`, `10-fasce-engineering.md` §5.3, `16-fasce-MALE-HALE-espanse.md` §2.6–2.7; `ricerca-approfondita/R4-regolatorio-delivery.md`, `R3-costi-cots-certificazione.md`; `fonti/annex_to_ed_decision_2025-018-r_1.md`, `fonti/CELEX_32019R0947_IT_TXT.md`, `fonti/CELEX_32019R0945_IT_TXT.md`, `fonti/Regolamento_APR_Ed_3_Emend_1.md`.
- **Comparabili esterni (pubblici, non nel repo — confidenza media):** EMSA-Tekever AR5, Airbus Flexrotor, Schiebel Camcopter S-100 (servizi RPAS marittimi UE); ABzero (IT, delivery — non comparabile di taglia/missione).
</content>
</invoke>
