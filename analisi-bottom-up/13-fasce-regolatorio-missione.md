# 13 — Matrice regolatoria MISSIONE × FASCIA per la famiglia modulare Firmamento

> **Analisi bottom-up — Percorso "servizio-first / multi-missione modulare"**
> Firmamento Technologies — famiglia di piattaforme a fasce (T1 VTOL C3 ≤25 kg box-wing → T2 mid ~30–150 kg → T3 MALE → T4 HALE), payload intercambiabile.
> **Autore:** Regulatory Counsel (EASA / ENAC / U-Space)
> **Data:** 2026-07-08
> **Base:** estende `04-regolatorio.md` (gradiente per classe di piattaforma) e `00-SINTESI-strategica.md`. **Nuova lente:** il regolatorio non dipende **solo dal peso della fascia**, ma dal **TIPO DI MISSIONE**. Alcune missioni (soprattutto CONSEGNA/TRASPORTO) fanno scattare oneri che l'EO puro non ha, **a parità di piattaforma**.
> **Domanda guida:** qual è la sequenza che parte semplice (EO Open A3) e scala a missioni ad alto valore/alto onere (consegna medicale BVLOS su borgo)? Il LUC è la chiave della strategia multi-missione?

---

## 0. Disclaimer epistemico (fatto normativo vs stima)

- **[FATTO]** = testo di regolamento/AMC/GM in vigore, citato con articolo/tabella e fonte nel repo.
- **[STIMA]** = valutazione di chi scrive (iGRC/SAIL, costi, tempi, classificazione merci). Confidenza dichiarata caso per caso, **medium-low** salvo diverso avviso.
- **Regola dura:** nessuna classificazione SORA è definitiva finché ENAC non la conferma in pre-application (art. 11 Reg. (UE) 2019/947). Tutti i valori sono *preliminary-grade*.
- **PDRA/STS:** gli **STS-01/STS-02** sono in Reg. 947 Appendice 1 [FATTO]; i **PDRA** sono AMC EASA all'art. 11 pubblicati a parte (il testo integrale **non è nel repo**: citati a memoria, confidenza medium-high, da verificare numero/edizione in pre-app).

---

## 1. Il perno nuovo: è la MISSIONE che sposta la categoria, non solo il peso

`04-regolatorio.md` ha dimostrato che il costo cresce **a scalini** (VLOS→BVLOS; dimensione/velocità×densità; quota→spazio controllato). Questa analisi aggiunge un **quarto asse ortogonale**: **il tipo di missione attiva trigger regolatori indipendenti dal peso.** I quattro trigger "di missione" sono fatti normativi:

### 1.1 Trigger CONSEGNA/TRASPORTO — tre effetti a cascata [FATTO]
1. **Esclusione dalla Open.** Art. 4 Reg. 947 (recepito art.1 righe 299–305 del CELEX): in Open «l'aeromobile non trasporta **merci pericolose** e **non lascia cadere alcun materiale**». Quindi **qualsiasi consegna** (sgancio, verricello o atterraggio-e-rilascio) **esce dalla Open** → minimo **Specific**, sempre, a qualunque peso, anche per un drone da 2 kg.
2. **Autorizzazione merci pericolose ENAC.** Reg. ENAC APR Ed.3 §4.5 (riga 424): «Il trasporto di merci pericolose deve essere autorizzato dall'ENAC». È un **procedimento aggiuntivo** sopra la SORA.
3. **Rischio di salto in Certified.** Art. 6 Reg. 947 (righe 358–362): la categoria **Certified** scatta se «è previsto il **trasporto di merci pericolose che può comportare un rischio elevato per terzi** in caso di incidente». Non tutte le merci pericolose: solo quelle **ad alto rischio**.
4. **SORA non copre le merci pericolose "aggiuntive".** Annex ED Decision 2025/018/R §S.1.3(c) (righe 311–315): «The carriage of dangerous goods (e.g. weapons, munitions, explosives, **hazardous medical samples**) … is **excluded from the scope** of this methodology and might require **additional safety considerations** (e.g. demonstration of the ability to **contain** the dangerous goods)». → per la consegna medicale serve una **dimostrazione di contenimento del carico** oltre alla SORA. Rif. GM1 Art. 2(11).

### 1.2 Trigger SORVEGLIANZA — overlay privacy [FATTO]
Il profilo di volo (loiter, ripresa persistente su abitato) è affine all'EO, ma **la finalità** attiva GDPR (Reg. (UE) 2016/679) + D.Lgs. 196/2003 + art. 34 Reg. ENAC APR Ed.3 (privacy a bordo) → **DPIA obbligatoria** e, se ripresa di persone/targhe, base giuridica dedicata e ruolo del Garante. È un **binario autorizzativo parallelo** che l'EO ambientale puro non ha.

### 1.3 Trigger CONNETTIVITÀ/RELAY — catena spettro parallela [FATTO]
Il payload radio **non alza la SORA** (è massa e antenna), ma attiva la **seconda catena** indipendente: diritti d'uso spettro (AGCOM/MIMIT/PNRF/ITU). Vedi `04-regolatorio.md` §4. Il collo di bottiglia è **lo spettro, non il volo**.

### 1.4 Trigger EO/sensing — nessun onere di missione aggiuntivo [FATTO]
L'EO ambientale (frane, incendi, vegetazione) **non trasporta nulla, non sgancia, non riprende sistematicamente persone** → **nessun trigger di missione**; l'onere è solo quello "di piattaforma" (VLOS→BVLOS, scala, quota). È la missione a **minimo attrito** ed è il punto di partenza corretto.

---

## 2. MATRICE MISSIONE × FASCIA (deliverable principale)

Ipotesi comune (come `04`): missione reale su/intorno a Pentema (Torriglia, GE), valle appenninica stretta, **spazio Classe G non controllato**, densità locale **< 5 ab/km²** ("Remote") con footprint che può intercettare edifici sparsi/SS45 (banda **< 50**) e, se il buffer è ampio, sfiorare Torriglia (~1.500 ab, banda **< 500**). SAIL da tabella iGRC/SAIL SORA 2.5 (`04` §1). Costi/tempi = **compliance** (consulenza SORA, documentazione, polizza, attestati), **piattaforma esclusa**.

| | **T1 — VTOL C3 ≤25 kg, 1–3 m** (box-wing "boxy") | **T2 — mid ~30–150 kg, 3–8 m** | **T3 — MALE >150 kg, FL200+** |
|---|---|---|---|
| **A) EO / sensing BVLOS** | **Specific · SAIL I–III** (target **II**). Iter: pre-app ENAC → SORA 2.5 → autorizz. + OM/MM; possibile via **PDRA-S01/G01** o **STS-02** (C6) se drop-zone controllata. **9–18 mesi · €25–70k**. Abilita: BVLOS EO valle sparsa, frane/incendi. | **Specific · SAIL III–IV** (iGRC 4–6, footprint largo, DAA robusto). **12–30 mesi · €80–250k**. Abilita: payload EO pesante, endurance lunga, area vasta. | **Specific SAIL IV–VI → de facto Certified** (col. 20 m iGRC, spazio controllato ARC-c/d, art. 6.2). **2–4+ anni · €1–5M+**. Sproporzione per Pentema. |
| **B) CONSEGNA / trasporto medicale** | **Specific** (Open esclusa, §1.1). **SAIL II–IV** secondo l'approccio sul borgo. **+ autorizz. merci pericolose ENAC** + **dimostrazione contenimento** carico. **Nessun STS dedicato**; SORA piena o PDRA parziale. **12–24 mesi (+DG) · €50–150k**. Abilita: consegna sangue/farmaci a punto controllato. **NON può:** sorvolare assembramenti né trasportare DG *ad alto rischio* → **Certified** (art. 6). | **Specific · SAIL III–V** (carico >kg, energia impatto alta → M2 difficile). **18–36 mesi · €150–400k**. Cargo pesante inter-presidi. Alto premio assicurativo. | **Non pertinente** per consegna di prossimità (sproporzione totale); il MALE non è un vettore consegna last-mile. |
| **C) Connettività / relay** | **Specific · SAIL II** (come A) **+ catena spettro**: ISM 2.4/5.8 (no licenza) o **MNO-hosting**. **Volo 9–18 mesi**; spettro giorni–mesi (ISM/MNO) vs 12–36 mesi (banda dedicata). Abilita: relay locale/IoT d'area. | **Specific · SAIL III–IV** + endurance; spettro idem. Cella di valle temporanea, backhaul. | **HAPS = Certified** + **spettro HAPS non licenziato** (WRC-27-dipendente). Vedi riga HALE. |
| **D) Sorveglianza** | **Specific · SAIL II–III** (loiter su abitato alza iGRC) **+ overlay privacy**: DPIA, art. 34 ENAC, base giuridica, Garante. **12–20 mesi · €40–90k** (+ costo DPIA/DPO). Se **P.S./law enforcement** → regime speciale (fuori Reg. 947 civile). | **Specific · SAIL III–IV** + privacy + (se persistente) ARC in salita. **18–30 mesi · €120–300k**. | Come EO T3: **de facto Certified** + privacy pervasiva su area vasta (rischio Garante alto). |

### Fascia T4 — HALE stratosferico (tutte le missioni)
**Categoria Certified**, **Type Certificate via Special Condition negoziata** (nessun framework HAPS civile EASA/ENAC — showstopper RSK-REG-001). Attraversa spazio controllato FL195+ in salita/discesa → ENAV obbligatorio. Spettro HAPS non allocato. **5–8+ anni · €5–15M+ (sola certificazione)**. **Non abilita alcun servizio nell'orizzonte finanziabile.** Resta **vettore strategico Y6+**, non leva di servizio (invariato rispetto a `04` e `00`).

> **Lettura della matrice:** per fascia (colonna) l'onere cresce come in `04`. La novità è la **riga B (consegna)**: **a parità di fascia T1, la consegna costa e dura più dell'EO** (Open preclusa, +DG, +contenimento, SAIL potenzialmente più alto per l'approccio sull'abitato). La consegna è la missione **a più alto attrito marginale** della famiglia — ed è anche quella a più alto valore/legittimità pubblica (medicale). Questo è il vero trade-off strategico della modularità.

---

## 3. Deep-dive: la CONSEGNA MEDICALE a un borgo montano (il caso nuovo e critico)

### 3.1 Perché non è mai "Open" [FATTO]
Consegnare = rilasciare un carico. Art. 4 Reg. 947 vieta in Open sia il **trasporto di merci pericolose** sia il **rilascio di materiale**. Quindi la consegna è **minimo Specific** anche con un mini-drone. Non esiste scorciatoia Open A3 per la consegna.

### 3.2 È "merce pericolosa"? Dipende dal contenuto [FATTO normativo + STIMA classificazione]
Il regime cambia radicalmente con la **classificazione ICAO-TI/IATA-DGR/ADR** del carico:

| Carico medicale tipico | Classe DG | Regime |
|---|---|---|
| **Farmaci comuni, dispositivi, DPI** | **Non-DG** (di norma) | Nessuna autorizzazione DG; solo SORA. |
| **Campioni diagnostici / sangue per analisi** | **UN3373, Cat. B, Classe 6.2** (basso rischio) | **DG** → **autorizzazione ENAC** (§4.5) + **contenimento** (Annex §S.1.3(c)); **resta Specific** (non "alto rischio"). |
| **Sostanze infettive Cat. A** (es. patogeni) | **UN2814, Classe 6.2** (alto rischio) | Possibile trigger **Certified** (art. 6, "rischio elevato per terzi"). Da evitare nel ConOps. |
| **Ghiaccio secco** (refrigerazione) | **UN1845, Classe 9** | **DG** → autorizzazione + gestione, ma basso rischio. |
| **Emocomponenti per trasfusione** | Generalmente **non-DG** | Come farmaci, ma catena del freddo. |

**[STIMA, confidenza medium-high]:** la consegna medicale realistica a Pentema (**sangue/campioni diagnostici, farmaci salvavita, defibrillatore**) ricade quasi sempre in **UN3373 / non-DG / UN1845** → **Specific + autorizzazione DG ENAC**, **non** Certified. Il salto in Certified si evita **escludendo dal ConOps le sostanze Cat. A e gli assembramenti**.

### 3.3 Che SAIL realistico? [STIMA, confidenza medium]
Driver ground-risk della consegna:
- **Transito** su terreno remoto/sparso (< 5 → < 50 ab/km²): drone piccolo (~1–2 m, ~30 m/s) → **iGRC 3–4**.
- **Approccio/rilascio al borgo:** il punto di consegna è **dove stanno i destinatari**. Se il drop è una **controlled ground area** (piazzola nota, destinatario = persona coinvolta, bystander tenuti a distanza) → colonna favorevole. Se invece l'approccio **sorvola il costruito** con persone non coinvolte → iGRC sale.
- Mitigazioni: **M1(A) sheltering** (borgo in pietra), **M1(B)** restrizioni operative (orari, corridoio stretto), **M2** paracadute/BRS + **contenimento carico**.

**Esito preliminare:** **SAIL II** se transito remoto + drop-zone controllata + geofencing stretto; **SAIL III–IV** se l'approccio finale sorvola stabilmente l'abitato o se il buffer intercetta Torriglia. **Confidenza medium** — è la classe di missione più sensibile al dettaglio del ConOps.

### 3.4 Esistono STS/PDRA europei applicabili? [FATTO parziale]
- **STS-01** (Reg. 947 App.1): VLOS su *controlled ground area* in ambiente popolato, **classe C5** — **non** BVLOS, non pensato per rotta di consegna. Non applicabile al transito.
- **STS-02**: BVLOS con **osservatori dello spazio aereo** su *controlled ground area* in ambiente **scarsamente popolato**, **classe C6**, ≤1 km (2 km con osservatori), ≤120 m. **Vicino** al profilo di transito rurale, ma il vincolo "controlled ground area" mal si concilia con l'attraversamento di terreno con edifici sparsi, e la consegna al borgo non è "controlled ground area" lungo tutta la rotta.
- **PDRA-S01 / PDRA-G01 / PDRA-G03** (AMC art. 11, EASA): BVLOS su ambiente scarsamente popolato, tipicamente **SAIL II**, UA fino a ~3 m; un PDRA-G03 copre BVLOS su ambiente controllato/scarsamente popolato. **Se il ConOps di consegna vi rientra**, si evita la SORA piena. **[FATTO con riserva: numero/edizione da verificare in pre-app — testo non nel repo.]**
- **Nessuno STS dedicato alla consegna su area popolata è in vigore** (gli STS-03/04 "delivery"/"popolato" erano in sviluppo EASA, **non adottati** al mio cutoff). → per la consegna al borgo con sorvolo di non-coinvolti si va di **SORA piena**. **[STIMA, confidenza medium — da confermare.]**

### 3.5 U-Space per rotte di consegna [FATTO]
Reg. (UE) 2021/664: U-Space **non è obbligatorio** salvo dove ENAC **designa** un volume (art. 3). Per **rotte di consegna ripetute** è il candidato naturale a gestire il traffico, ma in Italia è **embrionale** (prima R100 San Salvo 28/11/2025; Reg. U-Space ENAC Ed.1 in consultazione gen–apr 2026 — vedi `04` §4.1 e `LG-2023_006`). **Per Pentema nel breve non è prerequisito**: la rotta si autorizza in **Specific + coordinamento ENAV/NOTAM** puntuale. U-Space diventa rilevante **solo** con volumi di traffico e rotte fisse (Y3+).

### 3.6 Confronto con operatori delivery reali [FATTO/benchmark]
- **ABzero (Pisa, IT):** consegna di **sangue/campioni/organi** in capsula termica; trial con ENAC e Azienda Ospedaliera Pisana. **Comparatore italiano diretto** del caso "medicale montano". Opera in **Specific** con autorizzazioni puntuali. *(Confidenza media — pubblico ma non da atto ENAC nel repo.)*
- **Matternet + Swiss Post (CH):** campioni tra ospedali (Lugano/Zurigo), **BVLOS su area suburbana con paracadute**; profilo **SAIL ~III**, autorizzazione FOCA (CH è EASA-associata). Mostra che il **contenimento + BRS** è la via per tenere il SAIL gestibile su aree meno remote.
- **Everdrone (SE):** consegna **defibrillatori** BVLOS su area suburbana; SAIL III-ish, forte containment.
- **Wingcopter (DE):** consegna medicale/pacchi, sta perseguendo **EASA LUC** per scalare a molte operazioni/Stati — **prova che il LUC è la via di scala** per un operatore delivery multi-sito (vedi §6).

**Lezione:** la consegna medicale è **fattibile in Specific** (i comparabili lo fanno), ma richiede **contenimento carico + BRS + autorizzazione DG + ConOps chirurgico** sull'approccio, e il **SAIL reale è II–IV**, non I. Tempi realistici **12–24 mesi** oltre l'EO base, costo compliance **€50–150k** (T1), più alto se serve dimostrazione di contenimento certificata.

---

## 4. EO / sensing — aggiornamento con lente multi-missione

Invariato rispetto a `04`: **Open A3 subito** (VLOS versanti disabitati, €1–5k, settimane) → **Specific BVLOS SAIL II** (€25–70k, 9–18 mesi). **Novità multi-missione:** l'EO è la missione che **non consuma trigger di missione**, quindi è la **base autorizzativa** su cui innestare le altre. Un'autorizzazione Specific EO ben scritta (ConOps modulare, volume operativo geo-referenziato) è **riusabile** come scheletro per le missioni successive → **economia di scala regolatoria** interna alla famiglia modulare. È l'argomento a favore del "partire EO".

---

## 5. Connettività/relay e Sorveglianza — sintesi degli overlay

- **Connettività/relay (C):** onere di **volo** = quello EO della fascia; onere aggiuntivo = **spettro** (parallelo, non SORA). Via realistica breve: **ISM locale o MNO-hosting**; banda HAPS dedicata = 12–36 mesi, incerta, WRC-27 (vedi `04` §4). La relay **non alza il SAIL**.
- **Sorveglianza (D):** onere di volo affine all'EO; **overlay privacy** (DPIA, art. 34 ENAC, Garante) è il vero costo aggiuntivo e il vero rischio-blocco (competenza `data-privacy-counsel`). Il loiter persistente su abitato **alza l'iGRC** (footprint stabile su persone) e, se prolungato/alto, l'ARC. **Da trattare come missione a rischio istituzionale**, non solo tecnico.

---

## 6. Il LUC — la chiave (o no) della strategia multi-missione

### 6.1 Cosa è e cosa concede [FATTO]
LUC = **Light UAS Operator Certificate** (art. 2(9) Reg. 947, righe 226; Parte C Allegato, UAS.LUC.010–090). È rilasciato a una **persona giuridica** che dimostra un **Safety Management System** (UAS.LUC.030), un **Manuale LUC** (UAS.LUC.040) e controllo operativo/compliance monitoring. Il privilegio chiave (UAS.LUC.060): l'autorità **concede al titolare il privilegio di autorizzare le proprie operazioni SENZA** (a) presentare dichiarazione operativa, né (b) presentare domanda di autorizzazione operativa. Confermato anche da art. 5.6, art. 12 e artt. 6.4/6.5 (righe 341, 381) che esentano il titolare di LUC "con privilegi adeguati" dai passaggi ordinari.

### 6.2 Perché è (potenzialmente) LA leva della modularità multi-missione [STIMA, confidenza medium-high]
Un operatore che vuole fare **molte missioni diverse** (EO, consegna, sorveglianza, relay) con **molte piattaforme** (T1…T3) affronta, senza LUC, **una SORA/autorizzazione per ogni operazione nuova** → collo di bottiglia ricorrente con ENAC (mesi ciascuna, cfr. `04` RA-02). Con un **LUC a privilegi adeguati**, l'operatore **auto-autorizza** le operazioni **entro l'inviluppo approvato** (portata, tipi di operazione, aree/classi di spazio aereo — UAS.LUC.050(2)). È esattamente il modello che **Wingcopter** persegue per scalare la consegna su più siti/Stati. → **Il LUC trasforma il costo regolatorio da marginale-per-missione a fisso-una-tantum + auto-gestito.** Per una famiglia modulare multi-missione, **è l'abilitatore strutturale**.

### 6.3 Il prezzo del LUC [STIMA, confidenza medium]
Il LUC **non è un titolo iniziale**: richiede un'**organizzazione matura** — SMS documentato, dirigente responsabile (accountable manager), funzione indipendente di compliance monitoring, gestione subappaltatori, registri ≥3 anni (UAS.LUC.020–030). È un **investimento organizzativo pesante** (stimo **€150–400k + 12–24 mesi** per costruirlo e farlo approvare, più personale dedicato permanente). **Non ha senso a Y1** con una manciata di voli: il rapporto costo/beneficio del LUC diventa positivo **solo quando il numero e la varietà di missioni sono alti** (Y3+). Prima, si va di **autorizzazioni Specific singole** (più eventuale copertura via STS/PDRA per ridurre l'onere delle prime).

> **Verdetto LUC:** è la **chiave della fase di scala** della strategia modulare (Y3+), **non** la porta d'ingresso. La sequenza corretta è: *prime missioni con autorizzazioni Specific / STS-PDRA → maturare SMS e track-record → domanda LUC → auto-autorizzazione multi-missione.* Chiedere il LUC troppo presto brucia capitale su un'organizzazione più grande delle operazioni che deve autorizzare.

---

## 7. VERDETTO — sequenza di scaling regolatorio a minimo attrito

Scala a gradini per la **famiglia modulare multi-missione**; ogni gradino sblocca valore incrementale al minimo costo regolatorio marginale e **riusa** la base autorizzativa del precedente:

- **S0 — Subito (settimane, €1–5k): T1 in Open A3, VLOS, missione EO su versanti disabitati.** Zero SORA, zero trigger di missione. Genera track-record ENAC.
- **S1 — 9–18 mesi (€25–70k): T1 in Specific BVLOS, missione EO, target SAIL II.** ConOps modulare e riusabile (geofencing stretto, no sorvolo borgo/assembramenti, VLL Classe G, M1(A)+M2). È la **base autorizzativa madre**. Dove possibile, agganciarsi a **PDRA/STS-02** per ridurre l'onere.
- **S2 — connettività/relay come *payload* sulla base S1** (nessun nuovo SAIL): spettro via **ISM/MNO-hosting**, non banda dedicata.
- **S3 — 12–24 mesi aggiuntivi (€50–150k): consegna medicale T1 in Specific.** Estende il ConOps S1 con **autorizzazione DG ENAC + dimostrazione di contenimento + BRS**; ConOps chirurgico sull'approccio per tenere **SAIL II–III** ed **escludere Cat. A / assembramenti** (evita Certified). Modellare sui comparabili (ABzero, Matternet).
- **S4 — solo a volumi/varietà alti (Y3+, €150–400k, 12–24 mesi): domanda LUC.** Trasforma l'onere per-missione in auto-autorizzazione. È il vero **abilitatore della modularità** su scala.
- **NON in orizzonte finanziabile:** T3 MALE e **T4 HALE** (Certified, framework HAPS assente, ENAV FL195+, spettro non licenziato — showstopper invariato).

**Sintesi:** la strategia modulare multi-missione **funziona regolatoriamente se e solo se rispetta l'ordine "missione a minimo trigger prima"**: EO (nessun trigger) → relay (trigger spettro, non SAIL) → consegna (trigger Open-exclusion + DG + contenimento, SAIL più alto) → e **il LUC come cerniera di scala, non come porta d'ingresso**. Il peso della fascia conta, ma **è il tipo di missione a decidere quanti binari autorizzativi paralleli** (SORA + DG + privacy + spettro) devi percorrere insieme.

---

## 8. Confidenza e domande aperte

| Elemento | Confidenza | Nota |
|---|---|---|
| Open esclude trasporto DG e drop → consegna = min. Specific | **high** [FATTO] | art. 4 Reg. 947 (righe 299–305) |
| Certified trigger = assembramenti / persone / DG alto rischio | **high** [FATTO] | art. 6 Reg. 947 (righe 358–362) |
| DG richiede autorizzazione ENAC + contenimento fuori SORA | **high** [FATTO] | ENAC APR §4.5; Annex §S.1.3(c) r.311–315 |
| Classificazione medicale (UN3373 vs Cat. A vs non-DG) | **medium-high** [STIMA] | Dipende dal carico specifico; ICAO-TI/IATA-DGR |
| SAIL consegna medicale Pentema II–IV | **medium** [STIMA] | Sensibilissimo al ConOps di approccio; da pre-app |
| STS-02/PDRA applicabilità alla rotta di consegna | **medium** [STIMA/FATTO parziale] | STS in Reg. 947 [FATTO]; PDRA n./ed. da verificare; nessun STS "delivery" adottato al cutoff |
| LUC = auto-autorizzazione multi-missione (UAS.LUC.060) | **high** [FATTO] | Parte C Allegato, righe 1589–1596 |
| LUC conviene solo Y3+ (costo org.) | **medium** [STIMA] | Base-rate SMS aeronautico; non validato |
| HALE/MALE = Certified fuori orizzonte | **high** [FATTO] | Invariato da `04`/`00` |

**Domande da chiudere in pre-application ENAC (M+0–3):**
1. **OQ-B1** — la consegna al borgo con drop-zone controllata tiene **SAIL II–III**, o l'approccio sull'abitato la spinge a IV?
2. **OQ-B2** — quali carichi medicali ENAC classifica DG e quale dimostrazione di **contenimento** richiede (verricello vs atterraggio vs sgancio)?
3. **OQ-B3** — esiste un **PDRA** applicabile alla rotta rurale di consegna (riduzione onere vs SORA piena)?
4. **OQ-LUC** — soglia di volumi/varietà oltre cui ENAC/EASA vede il **LUC** come via preferenziale; tempi realistici di approvazione in Italia.
5. **OQ-USP** — orizzonte di designazione di un **volume U-Space** utile a rotte di consegna nell'Appennino ligure.

---

### Fonti (repo)
- `fonti/CELEX_32019R0947_IT_TXT.md` — Reg. (UE) 2019/947: art. 2(9) LUC / 2(3) assembramenti / 2(11) merci pericolose (r.207–230); art. 4 Open, divieto DG e drop (r.299–305); art. 6 Certified triggers (r.347–392); art. 5.6/12 esenzioni LUC (r.335–341, 381); STS Appendice 1 (r.1629+); **Parte C — LUC UAS.LUC.010–090** (r.1443–1626), privilegi UAS.LUC.060 (r.1589–1596).
- `fonti/annex_to_ed_decision_2025-018-r_1.md` — SORA 2.5: **§S.1.3(c) esclusione merci pericolose / contenimento** (r.311–315); §S.3.2.2 verifica STS/PDRA/Certified pre-SORA (r.819–847); Table 1 iGRC / Table 3 SAIL / Table 5 mitigazioni (cfr. `04`).
- `fonti/Regolamento_APR_Ed_3_Emend_1.md` — ENAC APR Ed.3+Em.1: **§4.5 autorizzazione merci pericolose** (r.424); art. 26 BVLOS (r.633, 1209–1230); art. 34 privacy.
- `fonti/CELEX_32021R0664_IT_TXT.md` + `fonti/LG-2023_006-UAS-Linee-Guida-U-Space.md` — U-Space non obbligatorio salvo designazione ENAC; Italia embrionale.
- `fonti/CELEX_32019R0945_IT_TXT.md` — classi C5/C6 (STS), C3 (T1).
- Base interna: `analisi-bottom-up/04-regolatorio.md`, `analisi-bottom-up/00-SINTESI-strategica.md`.
- Comparabili esterni (pubblici, non nel repo — confidenza media): ABzero (IT), Matternet+Swiss Post (CH), Everdrone (SE), Wingcopter (DE, percorso LUC).
